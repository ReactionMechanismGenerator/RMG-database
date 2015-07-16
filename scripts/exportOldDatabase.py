#!/usr/bin/env python
# encoding: utf-8

"""
This script exports the database to the old RMG-Java format. The script
requires two command-line arguments: the path to the database to import, and
the path to save the old RMG-Java database to.
"""

import os
import argparse
from rmgpy.data.rmg import RMGDatabase
from rmgpy import settings


###############################################################################


def export(input, output, database=None):

    print 'Loading the new RMG-Py database...'
    if not database:
        database = RMGDatabase()
    database.load(input, kineticsFamilies='all', kineticsDepositories='all')

    print 'Constructing additional rate rules from kinetics depository...'    
    for family in database.kinetics.families.values():
        family.addKineticsRulesFromTrainingSet(thermoDatabase=database.thermo)

    print "Deleting thermo library entries with atoms RMG-Java can't understand..."
    database.thermo.pruneHeteroatoms(allowed=['C','H','O','S'])
    print 'Saving old RMG-Java database...'
    database.saveOld(output)
    print "Done!"


###############################################################################



if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('outputPath', metavar='OUTPUT', type=str, nargs=1,
        help='the outputPath for the RMG-Java database directory')   
    
    args = parser.parse_args()
    outputPath = args.outputPath[0]
    
    inputPath = settings['database.directory']
    export(inputPath, outputPath)
