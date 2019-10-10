#!/usr/bin/env python
# encoding: utf-8

"""
This script exports an individual RMG-Py kinetics library to a chemkin
and dictionary file.  Thermo is taken from RMG's estimates and libraries.  
In order to use more specific thermo, you must tweak the thermoLibraries and 
estimators in use when loading the database. The script will save the
chem.inp and species_dictionary.txt files in the local directory.

usage:
exportKineticsLibrarytoChemkin.py [-h] LIBRARYNAME

positional arguments:
LIBRARYNAME      the libraryname of the RMG-Py format kinetics library
"""
import argparse
import os

from rmgpy import settings

from rmgpy.data.rmg import RMGDatabase
from rmgpy.data.kinetics.library import LibraryReaction
from rmgpy.chemkin import save_chemkin_file, save_species_dictionary
from rmgpy.rmg.model import Species

################################################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('library', metavar='LIBRARYNAME', type=str, nargs=1,
        help='the name of the kinetic library to be exported')    
    args = parser.parse_args()
    library_name = args.library[0]

    print('Loading RMG-Py database...')
    database = RMGDatabase()
    database.load(settings['database.directory'], kinetics_families='all', kinetics_depositories='all')
    

    print('Loading {0} library'.format(library_name))
    kinetic_library = database.kinetics.libraries[library_name]
    
    reaction_list = []    
    for index, entry in kinetic_library.entries.items():
        reaction = entry.item
        reaction.kinetics = entry.data
        library_reaction = LibraryReaction(index=reaction.index,
                     reactants=reaction.reactants,
                     products=reaction.products,
                     reversible=reaction.reversible,
                     kinetics=reaction.kinetics,
                     library=library_name
                     )
        reaction_list.append(library_reaction)

    species_list = []
    index = 0
    species_dict = kinetic_library.get_species(os.path.join(settings['database.directory'],'kinetics', 'libraries', library_name, 'dictionary.txt'))
    for spec in list(species_dict.values()):
        index = index + 1
        species = Species(molecule = spec.molecule)
        species.get_thermo_data()
        species.index = index
        species_list.append(species)

    for reaction in reaction_list:
        for reactant in reaction.reactants:
            for spec in species_list:
                if reactant.is_isomorphic(spec):
                    reactant.index = spec.index
                    spec.label = reactant.label
        for product in reaction.products:
            for spec in species_list:
                if product.is_isomorphic(spec):
                    product.index = spec.index
                    spec.label = product.label
            

    print('Saving the chem.inp and species_dictionary.txt to local directory')
    save_chemkin_file('chem.inp', species_list, reaction_list)
    save_species_dictionary('species_dictionary.txt', species_list)
    

