#!/usr/bin/env python
# encoding: utf-8

"""
This script exports the database to the old RMG-Java format. The script
requires two command-line arguments: the path to the database to import, and
the path to save the old RMG-Java database to.
"""

import os
import sys
import logging
from rmgpy.data.rmg import RMGDatabase
from rmgpy.data.base import Entry
from rmgpy.reaction import Reaction
from rmgpy.kinetics import Arrhenius, ArrheniusEP, KineticsData

###############################################################################


def main():

    if len(sys.argv) != 3:
        raise Exception('You must pass input and output '
                        'directories as parameters.')

    newPath = sys.argv[1]
    oldPath = os.path.join(sys.argv[2], 'RMG_database')

    export(newPath, oldPath)


###############################################################################


def export(input, output, database=None):

    print 'Loading the new RMG-Py database...'
    if not database:
        database = RMGDatabase()
    database.load(input)

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
    logging.getLogger().setLevel(logging.INFO)
    main()
