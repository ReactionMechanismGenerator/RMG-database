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
from rmgpy.data.rmg import RMGDatabase
from rmgpy.chemkin import saveChemkinFile, saveSpeciesDictionary
from rmgpy.rmg.model import Species
from rmgpy import settings
    
################################################################################

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('library', metavar='LIBRARYNAME', type=str, nargs=1,
        help='the name of the kinetic library to be exported')    
    args = parser.parse_args()
    libraryName = args.library[0]

    print 'Loading RMG-Py database...'
    database = RMGDatabase()
    database.load(settings['database.directory'], kineticsFamilies='all', kineticsDepositories='all')
    

    print 'Loading {0} library'.format(libraryName)
    kineticLibrary = database.kinetics.libraries[libraryName]
    
    reactionList = []    
    for index, entry in kineticLibrary.entries.iteritems():
        reaction = entry.item
        reaction.kinetics = entry.data
        reactionList.append(reaction)

    speciesList = []
    index = 0
    speciesDict = kineticLibrary.getSpecies(os.path.join(settings['database.directory'],'kinetics', 'libraries', libraryName, 'dictionary.txt'))
    for spec in speciesDict.values():
        index = index + 1
        species = Species(molecule = spec.molecule)
        species.generateThermoData(database)
        species.index = index
        speciesList.append(species)

    for reaction in reactionList:
        for reactant in reaction.reactants:
            for spec in speciesList:
                if reactant.isIsomorphic(spec):
                    reactant.index = spec.index
                    spec.label = reactant.label
        for product in reaction.products:
            for spec in speciesList:
                if product.isIsomorphic(spec):
                    product.index = spec.index
                    spec.label = product.label
            

    print 'Saving the chem.inp and species_dictionary.txt to local directory'
    saveChemkinFile('chem.inp', speciesList, reactionList)
    saveSpeciesDictionary('species_dictionary.txt', speciesList)
    

