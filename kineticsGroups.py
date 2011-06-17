#!/usr/bin/env python
# encoding: utf-8

"""
This script will generate the kinetics group additivity values for a single
reaction family, using the entries in that family's kinetics depository as a
training or test set. You can change the reaction family and the training and
test sets at the bottom of the file.
"""

import time
import math
import numpy
import pylab

from rmgpy.kinetics import Arrhenius, ArrheniusEP, KineticsData

################################################################################

def getRateCoefficientUnits(family):
    """
    For the given reaction `family`, return the units of its forward kinetics.
    This is hardcoding of reaction families, but at least it will fail loudly
    if it encounters an unexpected family.
    """
    if family in ['H_Abstraction', 'R_Addition_MultipleBond', 'R_Recombination', 'HO2_Elimination_from_PeroxyRadical', 'Disproportionation', '1+2_Cycloaddition', '2+2_cycloaddition_Cd', '2+2_cycloaddition_CO', '2+2_cycloaddition_CCO', 'Diels_alder_addition', '1,2_Insertion', '1,3_Insertion_CO2', '1,3_Insertion_ROR', 'R_Addition_COm', 'Oa_R_Recombination']:
        return 'm^3/(mol*s)'
    elif family in ['intra_H_migration', 'Birad_recombination', 'intra_OH_migration', 'Cyclic_Ether_Formation', 'Intra_R_Add_Exocyclic', 'Intra_R_Add_Endocyclic', '1,2-Birad_to_alkene', 'Intra_Disproportionation']:
        return 's^-1'
    else:
        raise ValueError('Unable to determine units of rate coefficient for reaction family "{0}".'.format(family))

def generateKineticsGroupValues(family, database, Tdata, trainingSetLabels, testSetLabels=None, plot=False):
    """
    Evaluate the kinetics group additivity values for the given reaction 
    `family` using the specified lists of depository components 
    `trainingSetLabels` as the training set and `testSetLabels` as the test 
    set. The already-loaded RMG database should be given as the `database` 
    parameter.
    """
    testSetLabels = testSetLabels or []
    
    groups = database.kinetics.groups[family]
    
    print 'Categorizing reactions in training and test sets for {0}'.format(family)
    trainingSet = []
    for label in trainingSetLabels:
        for entry in database.kinetics.depository['{0}/{1}'.format(family,label)].entries.values():
            if isinstance(entry.data, ArrheniusEP):
                if entry.data.alpha.value != 0:
                    continue # skip things with Evans-Polanyi values
            reaction, template = database.kinetics.getForwardReactionForFamilyEntry(entry=entry, family=family, thermoDatabase=database.thermo)
            trainingSet.append([reaction, template, entry])
    testSet = []
    for label in testSetLabels:
        for entry in database.kinetics.depository['{0}/{1}'.format(family,label)].entries.values():
            reaction, template = database.kinetics.getForwardReactionForFamilyEntry(entry=entry, family=family, thermoDatabase=database.thermo)
            testSet.append([reaction, template, entry])
    
    print 'Fitting new group additivity values for {0}...'.format(family)
    kdata_training = []
    for reaction, template, entry in trainingSet:
        if isinstance(reaction.kinetics, Arrhenius) or isinstance(reaction.kinetics, KineticsData):
            kdata_training.append([(reaction.kinetics.getRateCoefficient(T) / reaction.degeneracy) for T in Tdata])
        elif isinstance(reaction.kinetics, ArrheniusEP):
            kdata_training.append([(reaction.kinetics.getRateCoefficient(T, 0) / reaction.degeneracy) for T in Tdata])
        else:
            raise Exception('Unexpected kinetics model of type {0} for reaction {1}.'.format(reaction.kinetics.__class__, reaction))
    kdata_training = numpy.array(kdata_training, numpy.float64)
    
    kunits = getRateCoefficientUnits(family)
    trainingTemplates = [template for reaction, template, entry in trainingSet]
    groupValues, groupUncertainties, groupCounts, kmodel = groups.fitGroupValues(trainingTemplates, Tdata, kdata_training, kunits)
    # Add a note to the history of each item indicating that we've generated new group values
    event = [time.asctime(),'jwallen','action','jwallen generated new group additivity values for this entry.']
    for label, entry in groups.entries.iteritems():
        if entry.data is not None:
            entry.history.append(event)
    
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
    
    if plot:
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
        generateParityPlot(T, kdata_training[:,t], kmodel_training[:,t], kdata_test[:,t], kmodel_test[:,t], ci, trainingSet, testSet, family)

################################################################################

def generate(args, database):
    """
    This function is called when the "generate" command is given on the command
    line. It causes group additivity kinetics values to be generated and saved
    for all reaction families.
    """
    Tdata = numpy.array([300,400,500,600,800,1000,1500,2000], numpy.float64)
    for family in database.kinetics.groups:
        generateKineticsGroupValues(
            database = database,
            family = family,
            Tdata = Tdata,
            trainingSetLabels = ['rules'],
            plot = False,
        )
    print 'Saving RMG database...'
    database.save('input')
    
def evaluate(args, database):
    """
    This function is called when the "evaluate" command is given on the command
    line. It causes group additivity kinetics values to be generated and 
    evaluated for one reaction family.
    """
    family = args.family[0]
    Tdata = numpy.array([500,1000,1500,2000], numpy.float64)
    generateKineticsGroupValues(
        database = database,
        family = family,
        Tdata = Tdata,
        trainingSetLabels = ['rules'],
        testSetLabels = ['PrIMe'],
        plot = True,
    )

################################################################################

if __name__ == '__main__':

    import argparse
    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', help='')
    
    generateParser = subparsers.add_parser('generate', help='generate and save kinetics group values for all families')
    generateParser.set_defaults(run=generate)
    
    evaluateParser = subparsers.add_parser('evaluate', help='evaluate kinetics group values for one family')
    evaluateParser.add_argument('family', metavar='<family>', type=str, nargs=1, help='the family to evaluate')
    evaluateParser.set_defaults(run=evaluate)
    
    args = parser.parse_args()
    
    print 'Loading RMG database...'
    from rmgpy.data.rmg import RMGDatabase
    database = RMGDatabase()
    database.load('input')

    args.run(args, database)
    