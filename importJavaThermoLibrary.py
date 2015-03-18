#!/usr/bin/env python
# encoding: utf-8

"""
This script imports an individual RMG-Java themo library from a local directory and saves the output
thermo library py file into a path of the user's choosing.  This library will be automatically
saved to libraryname.py in the input/thermo/libraries directory and can 
be used directly as an RMG-Py thermo library.

usage:
importJavaThermoLibrary.py [-h] INPUT LIBRARYNAME

positional arguments:
INPUT       the input path of the RMG-Java thermo library directory
LIBRARYNAME      the libraryname for the RMG-Py format thermo library

"""

import argparse
import os
from rmgpy.data.thermo import ThermoLibrary
          
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('inputPath', metavar='INPUT', type=str, nargs=1,
        help='the input path of the RMG-Java thermo library directory')
    parser.add_argument('libraryName', metavar='OUTPUT', type=str, nargs=1,
        help='the libraryName for the RMG-Py format thermo library')   
    
    args = parser.parse_args()
    inputPath = args.inputPath[0]
    libraryName = args.libraryName[0]
    
    library = ThermoLibrary()
    library.loadOld(
        dictstr = os.path.join(inputPath, 'Dictionary.txt'),
        treestr = '',
        libstr = os.path.join(inputPath, 'Library.txt'),
        numParameters = 12,
        numLabels = 1,
        pattern = False,
    )
    library.name = libraryName

    # Save in Py format    
    library.save(os.path.join('input/thermo/libraries/', libraryName+'.py'))
