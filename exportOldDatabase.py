#!/usr/bin/env python
# encoding: utf-8

"""
This script exports the database to the old RMG-Java format. The script 
requires two command-line arguments: the path to the database to import, and 
the path to save the old RMG-Java database to.
"""

import sys

from rmgpy.data.rmg import RMGDatabase
from rmgpy.data.base import Entry
from rmgpy.reaction import Reaction
from rmgpy.kinetics import Arrhenius, ArrheniusEP, KineticsData

################################################################################

def generateAdditionalRateRules(family, database):
    """
    For a given reaction `family` label, generate additional rate rules from
    the corresponding depository training set. This function does automatically
    what users used to do by hand to construct a rate rule from reaction
    kinetics found in the literature, i.e. determine the groups involved,
    adjust to a per-site basis, etc.
    """
    
    # Find the database components we will need
    rules = database.kinetics.depository['{0}/rules'.format(family)]
    groups = database.kinetics.groups[family]
    
    index = max([entry.index for entry in rules.entries.values()]) + 1
    
    for depositoryLabel in ['training']:
        depository = database.kinetics.depository['{0}/{1}'.format(family, depositoryLabel)]
        
        entries = depository.entries.values()
        entries.sort(key=lambda x: (x.index, x.label))
        
        for entry0 in entries:
            
            reaction, template = database.kinetics.getForwardReactionForFamilyEntry(entry=entry0, family=family, thermoDatabase=database.thermo)
            
            # We must convert the kinetics to ArrheniusEP to finish our rate rule
            kinetics = reaction.kinetics
            # If kinetics are KineticsData, then first convert to Arrhenius
            if isinstance(kinetics, KineticsData):
                kinetics = Arrhenius().fitToData(
                    Tdata=kinetics.Tdata.values,
                    kdata=kinetics.kdata.values,
                    kunits=kinetics.kdata.units,
                    T0=1,
                )
            
            # Now convert from Arrhenius to ArrheniusEP
            # If not Arrhenius (or KineticsData), then skip this entry
            if isinstance(kinetics, Arrhenius):
                if kinetics.T0.value != 1:
                    kinetics.changeT0(1)
                kinetics = ArrheniusEP(
                    A = kinetics.A,
                    n = kinetics.n,
                    alpha = 0,
                    E0 = kinetics.Ea,
                    Tmin = kinetics.Tmin,
                    Tmax = kinetics.Tmax,
                )
            else:
                break
            
            # Put the kinetics on a per-site basis
            kinetics.A.value /= reaction.degeneracy
                
            # Construct a new entry for the new rate rule
            label = ';'.join([group.label for group in template])
            item = Reaction(
                reactants = template[:],
                products = None,
            )
            entry = Entry(
                index = index,
                label = label,
                item = item,
                data = kinetics,
                reference = entry0.reference,
                rank = entry0.rank,
                shortDesc = entry0.shortDesc,
                longDesc = entry0.longDesc,
                history = entry0.history,
            )

            # Add the new rate rule to the depository of rate rules
            rules.entries[entry.index] = entry
            
            index += 1
            
################################################################################

if __name__ == '__main__':

    oldPath = 'output/RMG_database'
    newPath = 'input'
    
    print 'Loading the new RMG-Py database...'
    database = RMGDatabase()
    database.load(newPath)
    
    print 'Constructing additional rate rules from kinetics depository...'
    for family in database.kinetics.groups:
        generateAdditionalRateRules(family, database)
    
    print 'Saving old RMG-Java database...'
    database.saveOld(oldPath)
