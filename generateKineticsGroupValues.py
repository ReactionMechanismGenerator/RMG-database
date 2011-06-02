#!/usr/bin/env python
# encoding: utf-8

"""
This script will generate the kinetics group additivity values for a single
reaction family, using the entries in that family's kinetics depository as a
training or test set. You can change the reaction family and the training and
test sets at the bottom of the file.
"""

import math
import numpy
import pylab

from rmgpy.data.rmg import RMGDatabase
from rmgpy.data.base import LogicNode
from rmgpy.molecule import Molecule
from rmgpy.group import Group
from rmgpy.species import Species
from rmgpy.reaction import Reaction
from rmgpy.kinetics import Arrhenius, ArrheniusEP, KineticsData

################################################################################

def matchSpeciesToMolecules(species, molecules):
    """
    For a given list of :class:`Species` objects `species` and list of
    :class:`Molecule` objects `molecules`, return ``True`` if the lists
    represent the same species (in any order) or ``False`` if not.
    """
    if len(species) == len(molecules) == 1:
        for mol in species[0].molecule:
            if mol.isIsomorphic(molecules[0]):
                return True
    elif len(species) == len(molecules) == 2:
        for molA in species[0].molecule:
            for molB in species[1].molecule:
                if molA.isIsomorphic(molecules[0]) and molB.isIsomorphic(molecules[1]):
                    return True
                elif molA.isIsomorphic(molecules[1]) and molB.isIsomorphic(molecules[0]):
                    return True
    return False

def generateThermoData(species, database):
    """
    Return the thermodynamics data for a given `species` as generated from
    the specified `database`.
    """
    thermoData = [database.thermo.getThermoData(molecule) for molecule in species.molecule]
    thermoData.sort(key=lambda x: x.getEnthalpy(298))
    return thermoData[0]

def getForwardReactionForEntry(entry, database, family):
    """
    For a given depository `entry`, return the reaction with kinetics and
    degeneracy for the "forward" direction as defined by the reaction family.
    For families that are their own reverse, the direction the kinetics is
    given in will be preserved.
    
    If the entry contains functional groups for the reactants, assume that it
    is given in the forward direction and simply return.
    
    If the entry contains real molecules for the reactants and products, create
    Species objects for the reaction
    """
    
    reaction = None; template = None
    
    if all([(isinstance(reactant, Group) or isinstance(reactant, LogicNode)) for reactant in entry.item.reactants]):
        # The entry is a rate rule, containing functional groups only
        # By convention, these are always given in the forward direction and
        # have kinetics defined on a per-site basis
        reaction = Reaction(
            reactants = entry.item.reactants[:],
            products = [],
            kinetics = entry.data,
            degeneracy = 1,
        )
        template = [database.kinetics.groups[family].entries[label] for label in entry.label.split(';')]
        
    elif (all([isinstance(reactant, Molecule) for reactant in entry.item.reactants]) and
        all([isinstance(product, Molecule) for product in entry.item.products])):
        # The entry is a real reaction, containing molecules
        # These could be defined for either the forward or reverse direction
        # and could have a reaction-path degeneracy
        
        reaction = Reaction(reactants=[], products=[])
        for molecule in entry.item.reactants:
            molecule.makeHydrogensExplicit()
            reactant = Species(molecule=[molecule], label=molecule.toSMILES())
            reactant.generateResonanceIsomers()
            reactant.thermo = generateThermoData(reactant, database)
            reaction.reactants.append(reactant)
        for molecule in entry.item.products:
            molecule.makeHydrogensExplicit()
            product = Species(molecule=[molecule], label=molecule.toSMILES())
            product.generateResonanceIsomers()
            product.thermo = generateThermoData(product, database)
            reaction.products.append(product)
    
        # Generate all possible reactions involving the reactant species
        generatedReactions = database.kinetics.generateReactionsFromGroups([reactant.molecule for reactant in reaction.reactants], only_families=[family])
        
        # Remove from that set any reactions that don't produce the desired reactants and products
        forward = []; reverse = []
        for rxn in generatedReactions:
            if matchSpeciesToMolecules(reaction.reactants, rxn.reactants) and matchSpeciesToMolecules(reaction.products, rxn.products):
                forward.append(rxn)
            if matchSpeciesToMolecules(reaction.reactants, rxn.products) and matchSpeciesToMolecules(reaction.products, rxn.reactants):
                reverse.append(rxn)
        
        # We should now know whether the reaction is given in the forward or
        # reverse direction
        if len(forward) == 1 and len(reverse) == 0:
            # The reaction is in the forward direction, so use as-is
            reaction = forward[0]
            template = database.kinetics.groups[family].getReactionTemplate(entry.item)
            # Don't forget to overwrite the estimated kinetics from the database with the kinetics for this entry
            reaction.kinetics = entry.data
        elif len(reverse) == 1 and len(forward) == 0:
            # The reaction is in the reverse direction
            # First fit Arrhenius kinetics in that direction
            Tdata = 1.0/numpy.arange(0.0005,0.0035,0.0001,numpy.float64)
            kdata = []
            for T in Tdata:
                kdata.append(entry.data.getRateCoefficient(T) / reaction.getEquilibriumConstant(T))
            kdata = numpy.array(kdata, numpy.float64)
            kunits = 'm^3/(mol*s)' if len(reverse[0].reactants) == 2 else 's^-1'
            kinetics = Arrhenius().fitToData(Tdata, kdata, kunits, T0=1.0)
            # Now flip the direction
            reaction = reverse[0]
            reaction.kinetics = kinetics
            template = database.kinetics.groups[family].getReactionTemplate(
                Reaction(reactants=entry.item.products, products=entry.item.reactants),
            )
        elif len(reverse) > 0 and len(forward) > 0:
            print 'FAIL: Multiple reactions found for "%s".' % (entry.label)
        elif len(reverse) == 0 and len(forward) == 0:
            print 'FAIL: No reactions found for "%s".' % (entry.label)
        else:
            print 'FAIL: Unable to estimate kinetics for "%s".' % (entry.label)

    assert reaction is not None
    assert template is not None
    return reaction, template, entry
        
################################################################################

def generateKineticsGroupValues(family, trainingSet, testSet, database):
    """
    Generate the kinetics group additivity values for the given reaction 
    `family` using the specified lists of depository components `trainingSet`
    as the training set and `testSet` as the test set. The already-loaded
    RMG database should be given as the `database` parameter.
    """
    
    groups = database.kinetics.groups[family]
    
    print 'Categorizing reactions in training and test sets for {0}'.format(family)
    trainingSetLabels = trainingSet; trainingSet = []
    for label in trainingSetLabels:
        for entry in database.kinetics.depository['{0}/{1}'.format(family,label)].entries.values():
            trainingSet.append(getForwardReactionForEntry(entry=entry, database=database, family=family))
    testSetLabels = testSet; testSet = []
    for label in testSetLabels:
        for entry in database.kinetics.depository['{0}/{1}'.format(family,label)].entries.values():
            testSet.append(getForwardReactionForEntry(entry=entry, database=database, family=family))
    
    print 'Fitting new group additivity values...'
    Tdata = numpy.array([500,1000,1500,2000], numpy.float64)
    kdata_training = []
    for reaction, template, entry in trainingSet:
        if isinstance(reaction.kinetics, Arrhenius) or isinstance(reaction.kinetics, KineticsData):
            kdata_training.append([(reaction.kinetics.getRateCoefficient(T) / reaction.degeneracy) for T in Tdata])
        elif isinstance(reaction.kinetics, ArrheniusEP):
            kdata_training.append([(reaction.kinetics.getRateCoefficient(T, 0) / reaction.degeneracy) for T in Tdata])
        else:
            raise Exception('Unexpected kinetics model of type {0} for reaction {1}.'.format(reaction.kinetics.__class__, reaction))
    kdata_training = numpy.array(kdata_training, numpy.float64)
    
    kunits = 'm^3/(mol*s)' if len(testSet[0][0].reactants) == 2 else 's^-1'
    trainingTemplates = [template for reaction, template, entry in trainingSet]
    groupValues, groupUncertainties, groupCounts, kmodel = groups.fitGroupValues(trainingTemplates, Tdata, kdata_training, kunits)
    
    # Evaluate kmodel for the training set
    kmodel_training = []
    for reaction, template, entry in trainingSet:
        kinetics = groups.getKineticsForTemplate(template, degeneracy=1)
        kmodel_training.append([kinetics.getRateCoefficient(T) for T in Tdata])
    kmodel_training = numpy.array(kmodel_training, numpy.float64)
    
    # Evaluate kdata and kmodel for the test set
    kdata_test = []; kmodel_test = []
    for reaction, template, entry in testSet:
        kinetics = groups.getKineticsForTemplate(template, degeneracy=1)
        kmodel_test.append([kinetics.getRateCoefficient(T) for T in Tdata])
        if isinstance(reaction.kinetics, Arrhenius) or isinstance(reaction.kinetics, KineticsData):
            kdata_test.append([(reaction.kinetics.getRateCoefficient(T) / reaction.degeneracy) for T in Tdata])
        elif isinstance(reaction.kinetics, ArrheniusEP):
            kdata_test.append([(reaction.kinetics.getRateCoefficient(T, 0) / reaction.degeneracy) for T in Tdata])
        else:
            raise Exception('Unexpected kinetics model of type {0} for reaction {1}.'.format(reaction.kinetics.__class__, reaction))
    kdata_test = numpy.array(kdata_test, numpy.float64)
    kmodel_test = numpy.array(kmodel_test, numpy.float64)
    
    # Print the group values
    entries = groups.top[:]
    for entry in groups.top:
        entries.extend(groups.descendants(entry))
    print '=============================== =========== =========== =========== ======='
    print 'Group                           T (K)       k(T) (SI)   CI (95%)    Count'
    print '=============================== =========== =========== =========== ======='
    entry = groups.top[0]
    for i in range(len(entry.data.Tdata.values)):
        label = ', '.join(['%s' % (top.label) for top in groups.top]) if i == 0 else ''
        T = Tdata[i]
        value = groupValues[entry][i]
        uncertainty = groupUncertainties[entry][i]
        count = groupCounts[entry][i]
        print '%-31s %-11g %-11.4e %-11.4e %-7i' % (label, T, value, uncertainty, count)
    print '------------------------------- ----------- ----------- ----------- -------'
    for entry in entries:
        if entry.data is not None:
            for i in range(len(entry.data.Tdata.values)):
                label = entry.label if i == 0 else ''
                T = Tdata[i]
                value = groupValues[entry][i]
                uncertainty = groupUncertainties[entry][i]
                count = groupCounts[entry][i]
                print '%-31s %-11g %-11.4e %-11.4e %-7i' % (label, T, value, uncertainty, count)
    print '=============================== =========== =========== =========== ======='
    
    # Generate plots
    generateParityPlots(Tdata, kdata_training, kmodel_training, kdata_test, kmodel_test, groups, trainingSet, testSet, family)
    
################################################################################

def generateParityPlot(T, kdata_training, kmodel_training, kdata_test, kmodel_test, ci, trainingSet, testSet, family):
    """
    Generate and show a parity plot of the predicted and actual values of k(T)
    at a given temperature `T`. The predicted (model) and actual (data) k(T)
    values are split into a training set (used to train the model) and a test
    set (not used to train the model). The `ci` parameter gives the overall
    uncertainty in the model at that temperature.
    """
    fig = pylab.figure(figsize=(8,6))
    pylab.loglog(kdata_training, kmodel_training, 'ob', picker=5)
    pylab.loglog(kdata_test, kmodel_test, 'or', picker=5)
    
    xlim = pylab.xlim()
    ylim = pylab.ylim()
    lim = (min(xlim[0], ylim[0])*0.1, max(xlim[1], ylim[1])*10)
    pylab.loglog(lim, lim, '-k')
    pylab.loglog(lim, [lim[0] * 10**ci, lim[1] * 10**ci], '--k')
    pylab.loglog(lim, [lim[0] / 10**ci, lim[1] / 10**ci], '--k')
    pylab.xlabel('Actual rate coefficient')
    pylab.ylabel('Predicted rate coefficient')
    pylab.title('%s, T = %g K' % (family, T))
    pylab.xlim(lim)
    pylab.ylim(lim)

    def onpick(event):
        thisline = event.artist
        kdata = thisline.get_xdata()
        kmodel = thisline.get_ydata()
        if len(kdata) == len(trainingSet):
            data = trainingSet
        else:
            data = testSet
        for ind in event.ind:
            reaction, template, entry = data[ind]
            kunits = 'm^3/(mol*s)' if len(reaction.reactants) == 2 else 's^-1'
            print 'template = [%s]' % (', '.join([g.label for g in template]))
            print 'entry = %r' % (entry)
            print '%s' % (reaction)
            print 'k_data   = %9.2e %s' % (kdata[ind], kunits)
            print 'k_model  = %9.2e %s' % (kmodel[ind], kunits)

    connection_id = fig.canvas.mpl_connect('pick_event', onpick)

    pylab.show()

def generateParityPlots(Tdata, kdata_training, kmodel_training, kdata_test, kmodel_test, groups, trainingSet, testSet, family):
    """
    Generate and show a set of parity plots of the predicted and actual values 
    of k(T) at various temperature. The predicted (model) and actual (data) k(T)
    values are split into a training set (used to train the model) and a test
    set (not used to train the model).
    """
    for t, T in enumerate(Tdata):
        ci = math.log10(groups.top[0].data.kdata.uncertainties[t])
        generatePlot(T, kdata_training[:,t], kmodel_training[:,t], kdata_test[:,t], kmodel_test[:,t], ci, trainingSet, testSet, family)

################################################################################

if __name__ == '__main__':

    print 'Loading RMG database...'
    database = RMGDatabase()
    database.load('input')

    generateKineticsGroupValues(
        family = 'H_Abstraction',
        #family = 'R_Addition_MultipleBond',
        #family = 'R_Recombination',
        trainingSet = ['rules'],
        testSet = ['PrIMe'],
        database = database,
    )
    