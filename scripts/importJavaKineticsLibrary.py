#!/usr/bin/env python
# encoding: utf-8

"""
This script imports an individual RMG-Java kinetics library from a local directory and saves the output
kinetics library py file into a path of the user's choosing.  This library will be automatically
added to the 'libraryname' folder in the input/kinetics/libraries directory and can 
be used directly as an RMG-Py kinetics library.

usage:
importJavaKineticsLibrary.py [-h] INPUT LIBRARYNAME

positional arguments:
INPUT       the input path of the RMG-Java kinetics library directory
LIBRARYNAME      the libraryname for the RMG-Py format kinetics library

"""

import argparse
import os
from rmgpy.data.kinetics import KineticsLibrary
from rmgpy import settings
          
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('inputPath', metavar='INPUT', type=str, nargs=1,
        help='the input path of the RMG-Java kinetics library directory')
    parser.add_argument('libraryName', metavar='OUTPUT', type=str, nargs=1,
        help='the libraryName for the RMG-Py format kinetics library')   
    
    args = parser.parse_args()
    inputPath = args.inputPath[0]
    libraryName = args.libraryName[0]
    
    library = KineticsLibrary()
    library.loadOld(inputPath)
    
    try:
        os.makedirs(os.path.join(settings['database.directory'], 'kinetics', 'libraries', libraryName))
    except:
        pass
    
    # Save in Py format    
    library.save(os.path.join(settings['database.directory'], 'kinetics', 'libraries', libraryName, 'reactions.py'))
    library.saveDictionary(os.path.join(settings['database.directory'], 'kinetics', 'libraries', libraryName,'dictionary.txt'))
