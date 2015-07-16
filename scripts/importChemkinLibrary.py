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
from rmgpy.data.thermo import ThermoLibrary
from rmgpy.data.kinetics import KineticsLibrary
from rmgpy.data.base import Entry
from rmgpy.chemkin import loadChemkinFile, getSpeciesIdentifier
from rmgpy import settings
          
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('chemkinPath', metavar='CHEMKIN', type=str, nargs=1,
        help='The path of the chemkin file')    
    parser.add_argument('dictionaryPath', metavar='DICTIONARY', type=str, nargs=1,
        help='The path of the RMG dictionary file')     
    parser.add_argument('name', metavar='NAME', type=str, nargs=1,
        help='Name of the chemkin library to be saved') 
    
    args = parser.parse_args()
    chemkinPath = args.chemkinPath[0]
    dictionaryPath = args.dictionaryPath[0]
    name = args.name[0]
        
    speciesList, reactionList = loadChemkinFile(chemkinPath, dictionaryPath)
    
    # Make full species identifier the species labels
    for species in speciesList:
        species.label = getSpeciesIdentifier(species)
        species.index = -1
    # load thermo library entries
    thermoLibrary = ThermoLibrary()
    for i in range(len(speciesList)): 
        species = speciesList[i]
        if species.thermo:
            thermoLibrary.loadEntry(index = i + 1,
                                    label = species.label,
                                    molecule = species.molecule[0].toAdjacencyList(),
                                    thermo = species.thermo,
                                    shortDesc = species.thermo.comment
           )                
        else:
            logging.warning('Species {0} did not contain any thermo data and was omitted from the thermo library.'.format(str(species)))
                        
    # load kinetics library entries                    
    kineticsLibrary = KineticsLibrary()
    kineticsLibrary.entries = {}
    for i in range(len(reactionList)):
        reaction = reactionList[i]        
        entry = Entry(
                index = i+1,
                label = str(reaction),
                item = reaction,
                data = reaction.kinetics,
            )
        entry.longDesc = reaction.kinetics.comment
        kineticsLibrary.entries[i+1] = entry
    
    kineticsLibrary.checkForDuplicates()
    kineticsLibrary.convertDuplicatesToMulti()

    # Save in Py format
    databaseDirectory = settings['database.directory']
    try:
        os.makedirs(os.path.join(databaseDirectory, 'kinetics', 'libraries',name))
    except:
        pass
    
    thermoLibrary.save(os.path.join(databaseDirectory, 'thermo' ,' libraries', name + '.py'))
    kineticsLibrary.save(os.path.join(databaseDirectory, 'kinetics', 'libraries', name, 'reactions.py'))
    kineticsLibrary.saveDictionary(os.path.join(databaseDirectory, 'kinetics', 'libraries', name, 'dictionary.txt'))
