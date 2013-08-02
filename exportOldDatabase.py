#!/usr/bin/env python
# encoding: utf-8

"""
This script exports the database to the old RMG-Java format. The script
requires two command-line arguments: the path to the database to import, and
the path to save the old RMG-Java database to.
"""

import os
import sys

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
        generateRules(family, database)

    print 'Saving old RMG-Java database...'
    database.saveOld(output)


###############################################################################


def generateRules(family, database):
    """
    For a given reaction `family` label, generate additional rate rules from
    the corresponding depository training set. This function does automatically
    what users used to do by hand to construct a rate rule from reaction
    kinetics found in the literature, i.e. determine the groups involved,
    adjust to a per-site basis, etc.
    """

    # Load rules and determine starting index
    rules = family.rules
    
    entries = rules.entries.values()
    if any(isinstance(item, list) for item in entries):
        # if the entries are lists
        entries = reduce(lambda x,y: x+y, entries)
    index = max([entry.index for entry in entries] or [0]) + 1

    # Load training entries
    for depository in family.depositories:
        if 'training' in depository.name:
            entries = sorted(depository.entries.values(),
                             key=lambda entry: (entry.index, entry.label))
            break

    # Generate a rate rule for each training entry
    for entry in entries:

        # Load entry's reaction, template, and kinetics
        reaction, template = database.kinetics.getForwardReactionForFamilyEntry(entry=entry,
                                                                                family=family.name,
                                                                                thermoDatabase=database.thermo)
        kinetics = reaction.kinetics

        # Convert KineticsData to Arrhenius
        if isinstance(kinetics, KineticsData):
            kinetics = Arrhenius().fitToData(Tdata=kinetics.Tdata.values,
                                             kdata=kinetics.kdata.values,
                                             kunits=kinetics.kdata.units,
                                             T0=1)

        # Ignore other kinetics types
        if not isinstance(kinetics, Arrhenius):
            continue

        # Change reference temperature to 1 K if necessary
        if kinetics.T0.value != 1:
            kinetics = kinetics.changeT0(1)

        # Convert kinetics to a per-site basis
        kinetics.A.value /= reaction.degeneracy

        # Convert to ArrheniusEP
        kinetics = ArrheniusEP(A=kinetics.A,
                               n=kinetics.n,
                               alpha=0,
                               E0=kinetics.Ea,
                               Tmin=kinetics.Tmin,
                               Tmax=kinetics.Tmax)

        # Add new rate rule
        rules.entries[index] = Entry(index=index,
                                     label=';'.join([group.label for group in template]),
                                     item=Reaction(reactants=template[:],
                                                   products=None),
                                     data=kinetics,
                                     reference=entry.reference,
                                     rank=entry.rank,
                                     shortDesc=entry.shortDesc,
                                     longDesc=entry.longDesc,
                                     history=entry.history)
        index += 1


###############################################################################


if __name__ == '__main__':

    main()
