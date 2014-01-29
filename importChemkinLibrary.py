#!/usr/bin/env python
# encoding: utf-8

"""
This script imports a chemkin file (along with RMG dictionary) from a local directory and saves a set of
RMG-Py kinetics library and thermo library files.  These py files can be added to the 
input/kinetics/libraries or input/thermo/libraries folder.
"""

import argparse
import time
import logging
import os
from rmgpy.data.thermo import ThermoLibrary
from rmgpy.data.kinetics import KineticsLibrary
from rmgpy.data.base import Entry
from rmgpy.molecule import Molecule
from rmgpy.chemkin import loadChemkinFile
from importOldDatabase import getUsername
          
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('chemkinPath', metavar='CHEMKIN', type=str, nargs=1,
        help='The path of the chemkin file')    
    parser.add_argument('dictionaryPath', metavar='DICTIONARY', type=str, nargs=1,
        help='The path of the RMG dictionary file')     
    parser.add_argument('outputDirectory', metavar='OUTPUTDIR', type=str, nargs=1,
        help='The desired output directory for the library files') 
    parser.add_argument('-r', '--removeH', action='store_true', help='remove explicit hydrogens')
    
    args = parser.parse_args()
    chemkinPath = args.chemkinPath[0]
    dictionaryPath = args.dictionaryPath[0]
    outputDir = args.outputDirectory[0]
    removeH = args.removeH
    
    print removeH
    
    speciesList, reactionList = loadChemkinFile(chemkinPath, dictionaryPath)
    
    # load thermo library entries
    thermoLibrary = ThermoLibrary()
    for i in range(len(speciesList)): 
        species = speciesList[i]
        rdkitmol = species.molecule[0].toRDKitMol(removeHs=False)
        species.molecule = [Molecule().fromRDKitMol(rdkitmol)]#[0].toAdjacencyList(removeH=False)
        print species.molecule[0].toAdjacencyList(removeH = removeH)
        if species.thermo:
            thermoLibrary.loadEntry(index = i + 1,
                                    label = species.label,
                                    molecule = species.molecule[0].toAdjacencyList(removeH = removeH),
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
                item = reaction,
                data = reaction.kinetics,
            )
        entry.longDesc = reaction.kinetics.comment
        kineticsLibrary.entries[i+1] = entry
    
    kineticsLibrary.checkForDuplicates()
    kineticsLibrary.convertDuplicatesToMulti()
        
    # Assign history to all entries
    user = getUsername()    # Pulls username from current git repository
    #user = '{0} <{1}>'.format(name, email)   # If not in git repository, then enter user information manually
    event = [time.asctime(),user,'action','{0} imported this entry from the old RMG database.'.format(user)]
    for label, entry in thermoLibrary.entries.iteritems():
        entry.history.append(event)
    for label, entry in kineticsLibrary.entries.iteritems():
        entry.history.append(event)
        
    # Save in Py format
    if not os.path.exists(outputDir):
        os.makedirs(os.path.join(self.path))
    
    thermoLibrary.save(os.path.join(outputDir, 'chemkinThermoLibrary.py'), removeH=removeH)
    kineticsLibrary.save(os.path.join(outputDir, 'chemkinKineticsLibrary.py'), removeH=removeH)
