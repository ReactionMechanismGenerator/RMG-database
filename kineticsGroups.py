#!/usr/bin/env python
# encoding: utf-8

"""
This script will generate the kinetics group additivity values for a single
reaction family, using the entries in that family's kinetics depository as a
training or test set. You can change the reaction family and the training and
test sets at the bottom of the file.
"""

import os.path
import time
import math
import numpy
import pylab

from rmgpy.kinetics import Arrhenius, ArrheniusEP, KineticsData
from rmgpy.data.base import getAllCombinations

from importOldDatabase import getUsername
user = getUsername()

################################################################################

def fitGroupValues(groupDatabase, templates, Tdata, kdata, kunits):
    """
    Fit group additivity values based on a matrix of rate coefficient
    data `kdata` corresponding to a list of reaction `templates` and a
    set of temperatures `Tdata`. The provided rate coefficient data should
    be for the high-pressure limit and should be given on a per-site basis.
    The groups in the templates should also be in this reaction family's
    tree.
    """

    import scipy.stats

    kmodel = numpy.zeros_like(kdata)

    # Determine a complete list of the entries in the database, sorted as in the tree
    entries = groupDatabase.top[:]
    for entry in groupDatabase.top:
        entries.extend(groupDatabase.descendants(entry))

    # Determine a unique list of the groups we will be able to fit parameters for
    groupList = []
    for template in templates:
        for group in template:
            if group not in groupDatabase.top:
                groupList.append(group)
                groupList.extend(groupDatabase.ancestors(group)[:-1])
    groupList = list(set(groupList))
    groupList.sort(key=lambda x: x.index)

    # Initialize dictionaries of fitted group values and uncertainties
    groupValues = {}; groupUncertainties = {}; groupCounts = {}
    groupComments = {}
    for entry in entries:
        groupValues[entry] = []
        groupUncertainties[entry] = []
        groupCounts[entry] = []
        groupComments[entry] = set()

    # Fit group values at each temperature
    for t, T in enumerate(Tdata):

        # Generate least-squares matrix and vector
        A = []; b = []
        for index, template in enumerate(templates):

            # Create every combination of each group and its ancestors with each other
            combinations = []
            for group in template:
                groups = [group]; groups.extend(groupDatabase.ancestors(group))
                combinations.append(groups)
            combinations = getAllCombinations(combinations)
            # Add a row to the matrix for each combination
            for groups in combinations:
                Arow = [1 if group in groups else 0 for group in groupList]
                Arow.append(1)
                brow = math.log10(kdata[index,t])
                A.append(Arow); b.append(brow)
                
                for group in groups:
                    groupComments[group].add("{0!s}".format(template))

        if len(A) == 0:
            logging.warning('Unable to fit kinetics groups for family "{0}"; no valid data found.'.format(groupDatabase.label))
            return
        A = numpy.array(A)
        b = numpy.array(b)

        x, residues, rank, s = numpy.linalg.lstsq(A, b)

        # Determine error in each group (on log scale)
        stdev = numpy.zeros(len(groupList)+1, numpy.float64)
        count = numpy.zeros(len(groupList)+1, numpy.int)
        for index, template in enumerate(templates):
            kd = math.log10(kdata[index,t])
            km = x[-1] + sum([x[groupList.index(group)] for group in template if group in groupList])
            kmodel[index,t] = 10**km
            variance = (km - kd)**2
            for group in template:
                groups = [group]; groups.extend(groupDatabase.ancestors(group))
                for g in groups:
                    if g not in groupDatabase.top:
                        index = groupList.index(g)
                        stdev[index] += variance
                        count[index] += 1
            stdev[-1] += variance
            count[-1] += 1
        stdev = numpy.sqrt(stdev / (count - 1))
        ci = scipy.stats.t.ppf(0.975, count - 1) * stdev

        # Update dictionaries of fitted group values and uncertainties
        for entry in entries:
            if entry == groupDatabase.top[0]:
                groupValues[entry].append(10**x[-1])
                groupUncertainties[entry].append(10**ci[-1])
                groupCounts[entry].append(count[-1])
            elif entry in groupList:
                index = groupList.index(entry)
                groupValues[entry].append(10**x[index])
                groupUncertainties[entry].append(10**ci[index])
                groupCounts[entry].append(count[index])
            else:
                groupValues[entry] = None
                groupUncertainties[entry] = None
                groupCounts[entry] = None

    # Store the fitted group values and uncertainties on the associated entries
    for entry in entries:
        if groupValues[entry] is not None:
            entry.data = KineticsData(Tdata=(Tdata,"K"), kdata=(groupValues[entry],kunits))
            if not any(numpy.isnan(numpy.array(groupUncertainties[entry]))):
                entry.data.kdata.uncertainties = numpy.array(groupUncertainties[entry])
                entry.data.kdata.uncertaintyType = '*|/'
            entry.shortDesc = "Group additive kinetics."
            entry.longDesc = "Fitted to {0} rates.\n".format(groupCounts[entry])
            entry.longDesc += "\n".join(groupComments[entry])
        else:
            entry.data = None

    return groupValues, groupUncertainties, groupCounts, kmodel
    
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
    trainingSets = []
    for label in trainingSetLabels:
        trainingSet = []
        for entry in database.kinetics.depository['{0}/{1}'.format(family,label)].entries.values():
            if isinstance(entry.data, ArrheniusEP):
                if entry.data.alpha.value != 0:
                    continue # skip things with Evans-Polanyi values
            reaction, template = database.kinetics.getForwardReactionForFamilyEntry(entry=entry, family=family, thermoDatabase=database.thermo)
            trainingSet.append([reaction, template, entry])
        if len(trainingSet) > 0:
            trainingSets.append([label, trainingSet])
    testSets = []
    for label in testSetLabels:
        testSet = []
        for entry in database.kinetics.depository['{0}/{1}'.format(family,label)].entries.values():
            reaction, template = database.kinetics.getForwardReactionForFamilyEntry(entry=entry, family=family, thermoDatabase=database.thermo)
            testSet.append([reaction, template, entry])
        if len(testSet) > 0:
            testSets.append([label, testSet])
        
    print 'Fitting new group additivity values for {0}...'.format(family)
    kdata_training = []
    for label, trainingSet in trainingSets:
        kdata = []
        for reaction, template, entry in trainingSet:
            if isinstance(reaction.kinetics, Arrhenius) or isinstance(reaction.kinetics, KineticsData):
                kdata.append([(reaction.kinetics.getRateCoefficient(T) / reaction.degeneracy) for T in Tdata])
            elif isinstance(reaction.kinetics, ArrheniusEP):
                kdata.append([(reaction.kinetics.getRateCoefficient(T, 0) / reaction.degeneracy) for T in Tdata])
            else:
                raise Exception('Unexpected kinetics model of type {0} for reaction {1}.'.format(reaction.kinetics.__class__, reaction))
        kdata = numpy.array(kdata, numpy.float64)
        kdata_training.append(kdata)
    
    kunits = getRateCoefficientUnits(family)
    trainingKinetics = []
    for kdata in kdata_training:
        trainingKinetics.extend(list(kdata))
    trainingKinetics = numpy.array(trainingKinetics, numpy.float64)
    trainingTemplates = [template for label, trainingSet in trainingSets for reaction, template, entry in trainingSet]
   
    # keep track of previous values so we can detect if they change
    old_entries = dict()
    for label,entry in groups.entries.iteritems():
        if entry.data is not None:
            old_entries[label] = entry.data.kdata.values * 1.0
    
    # fit group values
    groupValues, groupUncertainties, groupCounts, kmodel = fitGroupValues(groups, trainingTemplates, Tdata, trainingKinetics, kunits)

    # Add a note to the history of each changed item indicating that we've generated new group values
    event = [time.asctime(),user,'action','Generated new group additivity values for this entry.']
    for label, entry in groups.entries.iteritems():
        if entry.data is not None:
            if old_entries.has_key(label) and len(old_entries[label]) == len(entry.data.kdata.values) and all(abs(entry.data.kdata.values/old_entries[label]-1)<0.01):
                #print "New group values within 1% of old."
                pass
            else:
                entry.history.append(event)
    
    # Evaluate kmodel for the training set
    kmodel_training = []
    for label, trainingSet in trainingSets:
        kmodel = []
        for reaction, template, entry in trainingSet:
            kinetics = groups.getKineticsForTemplate(template, degeneracy=1)
            kmodel.append([kinetics.getRateCoefficient(T) for T in Tdata])
        kmodel = numpy.array(kmodel, numpy.float64)
        kmodel_training.append(kmodel)
    
    # Evaluate kdata and kmodel for the test set
    kdata_test = []; kmodel_test = []
    for label, testSet in testSets:
        kdata = []; kmodel = []
        for reaction, template, entry in testSet:
            kinetics = groups.getKineticsForTemplate(template, degeneracy=1)
            kmodel.append([kinetics.getRateCoefficient(T) for T in Tdata])
            if isinstance(reaction.kinetics, Arrhenius) or isinstance(reaction.kinetics, KineticsData):
                kdata.append([(reaction.kinetics.getRateCoefficient(T) / reaction.degeneracy) for T in Tdata])
            elif isinstance(reaction.kinetics, ArrheniusEP):
                kdata.append([(reaction.kinetics.getRateCoefficient(T, 0) / reaction.degeneracy) for T in Tdata])
            else:
                raise Exception('Unexpected kinetics model of type {0} for reaction {1}.'.format(reaction.kinetics.__class__, reaction))
        kdata = numpy.array(kdata, numpy.float64)
        kdata_test.append(kdata)
        kmodel = numpy.array(kmodel, numpy.float64)
        kmodel_test.append(kmodel)
    
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
        generateParityPlots(Tdata, kdata_training, kmodel_training, kdata_test, kmodel_test, groups, trainingSets, testSets, family)
    
################################################################################

def generateParityPlots(Tdata, kdata_training, kmodel_training, kdata_test, kmodel_test, groups, trainingSets, testSets, family):
    """
    Generate and show a set of parity plots of the predicted and actual values 
    of k(T) at various temperature. The predicted (model) and actual (data) k(T)
    values are split into a training set (used to train the model) and a test
    set (not used to train the model).
    """
    import matplotlib.pyplot as plt
    from matplotlib.widgets import CheckButtons
    
    for t, T in enumerate(Tdata):
        ci = math.log10(groups.top[0].data.kdata.uncertainties[t])
        
        fig = pylab.figure(figsize=(10,8))
        ax = plt.subplot(1, 1, 1)
        
        lines = []
        for index in range(len(kdata_training)):
            lines.append(ax.loglog(kdata_training[index][:,t], kmodel_training[index][:,t], 'o', picker=5)[0])
        for index in range(len(kdata_test)):
            lines.append(ax.loglog(kdata_test[index][:,t], kmodel_test[index][:,t], 's', picker=5)[0])
        
        legend = []
        for label, trainingSet in trainingSets:
            legend.append(label)
        for label, testSet in testSets:
            legend.append(label)

        xlim = pylab.xlim()
        ylim = pylab.ylim()
        lim = (min(xlim[0], ylim[0])*0.1, max(xlim[1], ylim[1])*10)
        ax.loglog(lim, lim, '-k')
        ax.loglog(lim, [lim[0] * 10**ci, lim[1] * 10**ci], '--k')
        ax.loglog(lim, [lim[0] / 10**ci, lim[1] / 10**ci], '--k')
        pylab.xlabel('Actual rate coefficient')
        pylab.ylabel('Predicted rate coefficient')
        pylab.legend(legend, loc=4)
        pylab.title('%s, T = %g K' % (family, T))
        pylab.xlim(lim)
        pylab.ylim(lim)

        rax = plt.axes([0.15, 0.65, 0.2, 0.2])
        check = CheckButtons(rax, legend, [True for label in legend])

        def func(label):
            for index in range(len(lines)):
                if legend[index] == label:
                    lines[index].set_visible(not lines[index].get_visible())
            plt.draw()
        check.on_clicked(func)
        
        def onpick(event):
            index = lines.index(event.artist)
            if index < len(trainingSets):
                label, data = trainingSets[index]
                kdata = kdata_training[index][:,t]
                kmodel = kmodel_training[index][:,t]
            else:
                index = index - len(trainingSets)
                label, data = testSets[index]
                kdata = kdata_test[index][:,t]
                kmodel = kmodel_test[index][:,t]
            for ind in event.ind:
                reaction, template, entry = data[ind]
                kunits = 'm^3/(mol*s)' if len(reaction.reactants) == 2 else 's^-1'
                print label
                print 'template = [%s]' % (', '.join([g.label for g in template]))
                print 'entry = %r' % (entry)
                print '%s' % (reaction)
                print 'k_data   = %9.2e %s' % (kdata[ind], kunits)
                print 'k_model  = %9.2e %s' % (kmodel[ind], kunits)

        connection_id = fig.canvas.mpl_connect('pick_event', onpick)

        pylab.show()
        
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
            trainingSetLabels = ['rules', 'training'],
            testSetLabels = [],
            plot = False,
        )
    print 'Saving new kinetics group values...'
    database.kinetics.saveGroups(os.path.join('input', 'kinetics', 'groups'))
    
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
        trainingSetLabels = ['rules', 'training'],
        testSetLabels = ['PrIMe', 'test'],
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
    