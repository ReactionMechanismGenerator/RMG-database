#!/usr/bin/env python
# encoding: utf-8

"""
This script imports an individual RMG-Java kinetics library from a local directory and saves the output
kinetics library py file into a path of the user's choosing.  This py file can be added to the 
input/kinetics/libraries folder to be used as an RMG-Py kinetics library.  
"""

import argparse
import time
from rmgpy.data.kinetics import KineticsLibrary
from importOldDatabase import getUsername
          
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('inputPath', metavar='INPUT', type=str, nargs=1,
        help='the input path of the RMG-Java kinetics library directory')
    parser.add_argument('outputPath', metavar='OUTPUT', type=str, nargs=1,
        help='the libraryname.py output file for the RMG-Py format kinetics library')   
    
    args = parser.parse_args()
    inputPath = args.inputPath[0]
    outputPath = args.outputPath[0]
    
    library = KineticsLibrary()
    library.loadOld(inputPath)
    
        
    # Save in Py format
    library.save(outputPath)
