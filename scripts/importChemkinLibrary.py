#!/usr/bin/env python
# encoding: utf-8

"""
This script imports a chemkin file (along with RMG dictionary) from a local directory and saves a set of
RMG-Py kinetics library and thermo library files.  These py files are automatically added to the 
appropriate kinetics/libraries and thermo/libraries folder under the user-specified `name` for the chemkin library.
"""

import argparse
import logging
import os

from rmgpy import settings
from rmgpy.chemkin import load_chemkin_file
from rmgpy.data.base import Entry
from rmgpy.data.kinetics import KineticsLibrary
from rmgpy.data.thermo import ThermoLibrary

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('chemkin_path', metavar='CHEMKIN', type=str, nargs=1,
        help='The path of the chemkin file')    
    parser.add_argument('dictionary_path', metavar='DICTIONARY', type=str, nargs=1,
        help='The path of the RMG dictionary file')     
    parser.add_argument('name', metavar='NAME', type=str, nargs=1,
        help='Name of the chemkin library to be saved') 
    
    args = parser.parse_args()
    chemkin_path = args.chemkin_path[0]
    dictionary_path = args.dictionary_path[0]
    name = args.name[0]
        
    species_list, reaction_list = load_chemkin_file(chemkin_path, dictionary_path)
    
    thermo_library = ThermoLibrary(name=name)
    for i in range(len(species_list)):
        species = species_list[i]
        if species.thermo:
            thermo_library.load_entry(index = i + 1,
                                    label = species.label,
                                    molecule = species.molecule[0].to_adjacency_list(),
                                    thermo = species.thermo,
           )
        else:
            logging.warning("""Species {0} did not contain any thermo data and was omitted from the thermo 
                               library.""".format(str(species)))
                        
    # load kinetics library entries                    
    kinetics_library = KineticsLibrary(name=name)
    kinetics_library.entries = {}
    for i in range(len(reaction_list)):
        reaction = reaction_list[i]
        entry = Entry(
                index = i+1,
                label = str(reaction),
                item = reaction,
                data = reaction.kinetics,
            )
        try:
            entry.long_desc = 'Originally from reaction library: ' + reaction.library + "\n" + reaction.kinetics.comment
        except AttributeError:
            entry.long_desc = reaction.kinetics.comment
        kinetics_library.entries[i+1] = entry
    
    # Mark as duplicates where there are mixed pressure dependent and non-pressure dependent duplicate kinetics
    # Even though CHEMKIN does not require a duplicate flag, RMG needs it.
    # Using flag mark_duplicates = True
    kinetics_library.check_for_duplicates(mark_duplicates=True)
    kinetics_library.convert_duplicates_to_multi()

    # Save in Py format
    database_directory = settings['database.directory']
    try:
        os.makedirs(os.path.join(database_directory, 'kinetics', 'libraries',name))
    except:
        pass
    
    thermo_library.save(os.path.join(database_directory, 'thermo' ,'libraries', name + '.py'))
    kinetics_library.save(os.path.join(database_directory, 'kinetics', 'libraries', name, 'reactions.py'))
    kinetics_library.save_dictionary(os.path.join(database_directory, 'kinetics', 'libraries', name, 'dictionary.txt'))
