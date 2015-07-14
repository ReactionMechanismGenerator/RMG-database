#!/usr/bin/env python
# encoding: utf-8

"""
This script imports an RMG-Java database from the output directory and saves
it in the user-specified database directory.

The outputDirectory can then be used to overwrite the existing RMG-database files.
"""

import os
import argparse

from rmgpy.data.rmg import RMGDatabase

################################################################################


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('inputPath', metavar='INPUT', type=str, nargs=1,
        help='the input path of the RMG-Java database directory')
    parser.add_argument('outputPath', metavar='OUTPUT', type=str, nargs=1,
        help='output path for the desired RMG-Py database directory')   
    
    args = parser.parse_args()
    inputPath = args.inputPath[0]
    outputPath = args.outputPath[0]
    
    newPath = 'input'
    
    print 'Loading old RMG-Java database...'
    database = RMGDatabase()
    database.loadOld(inputPath)
    
    try:
        os.makedirs(outputPath)
    except:
        pass
    
    print 'Saving the new RMG-Py database...'
    database.save(outputPath)
    print "Done!"
