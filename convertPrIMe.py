#!/usr/bin/env python
# encoding: utf-8

import sys

from rmgpy.data.kinetics import KineticsDatabase
from rmgpy.data.rmg import RMGDatabase

def convertPrIMe(family):

    print 'Loading kinetics families...'
    database = RMGDatabase()
    database.kinetics = KineticsDatabase()
    database.kinetics.loadFamilies('input/kinetics/families')
    database.loadForbiddenStructures('input/forbiddenStructures.py')
    
    for depository in database.kinetics.families[family].depositories:
        if depository.label == '{0}/PrIMe'.format(family):
            break
    else:
        raise Exception('Could not find PrIMe depository in {0} family.'.format(family))
    
    entries = []
    
    print 'Determining unique list of reactions...'
    for entry0 in depository.entries.values():
        for entry in entries:
            if entry.item.isIsomorphic(entry0.item):
                break
        else:
            entries.append(entry0)
    print 'Found {0:d} unique reactions out of {1:d} entries.'.format(len(entries), len(depository.entries))
    
    print 'Sorting unique reactions...'
    entries.sort(key=lambda entry: sum([1 for r in entry.item.reactants for a in r.atoms if a.isNonHydrogen()]))
    
    print 'Saving reactions...'
    for index, entry in enumerate(entries):
        
        label = entry.label
        reaction = entry.item
        
        # Determine degeneracy in both directions
        reactions = database.kinetics.generateReactionsFromFamilies(reaction.reactants, reaction.products, only_families=[family])
        if len(reactions) != 1:
            print 'Warning: could not determine forward degeneracy for reaction #{0:d}.'.format(index+1)
            forwardDegeneracy = 1
        else:
            forwardDegeneracy = reactions[0].degeneracy
        reactions = database.kinetics.generateReactionsFromFamilies(reaction.products, reaction.reactants, only_families=[family])
        if len(reactions) != 1:
            print 'Warning: could not determine reverse degeneracy for reaction #{0:d}.'.format(index+1)
            reverseDegeneracy = 1
        else:
            reverseDegeneracy = reactions[0].degeneracy
        
        saveReaction('input/kinetics/families/{0}/training/{0}.py'.format(family, index+1), index+1, label, reaction, forwardDegeneracy, reverseDegeneracy)

def saveReaction(filename, index, label, reaction, forwardDegeneracy, reverseDegeneracy):
    
    with open(filename, 'w') as f:

        f.write('#!/usr/bin/env python\n')
        f.write('# encoding: utf-8\n\n')
        
        f.write('reaction(\n')
        f.write('    index = {0:d},\n'.format(index))
        f.write('    label = "{0!s}",\n'.format(label))
        f.write('    reactant1 = \n')
        f.write('"""\n')
        f.write(reaction.reactants[0].toAdjacencyList())
        f.write('""",\n')
        f.write('    reactant2 = \n')
        f.write('"""\n')
        f.write(reaction.reactants[1].toAdjacencyList())
        f.write('""",\n')
        f.write('    product1 = \n')
        f.write('"""\n')
        f.write(reaction.products[0].toAdjacencyList())
        f.write('""",\n')
        f.write('    product2 = \n')
        f.write('"""\n')
        f.write(reaction.products[1].toAdjacencyList())
        f.write('""",\n')
        f.write('    forwardDegeneracy = {0:d},\n'.format(forwardDegeneracy))
        f.write('    reverseDegeneracy = {0:d},\n'.format(reverseDegeneracy))
        f.write(')\n\n')

################################################################################

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        raise Exception('You must provide the name of the reaction family as the lone command-line argument.')
    
    convertPrIMe(family=sys.argv[1])
    