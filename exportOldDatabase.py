#!/usr/bin/env python
# encoding: utf-8

"""
This script exports the database to the old RMG-Java format. The script 
requires two command-line arguments: the path to the database to import, and 
the path to save the old RMG-Java database to.
"""

import sys

from rmgpy.data.rmg import RMGDatabase

################################################################################

if __name__ == '__main__':

    oldPath = 'output/RMG_database'
    newPath = 'input'
    
    print 'Loading the new RMG-Py database...'
    database = RMGDatabase()
    database.load(newPath)
    
    print 'Saving old RMG-Java database...'
    database.saveOld(oldPath)
