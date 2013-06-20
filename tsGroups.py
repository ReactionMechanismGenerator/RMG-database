#!/usr/bin/env python
# encoding: utf-8

"""
This script is used for working with the kinetics group additivity values in
RMG. There are several different types of operations this script can do, and
each of these has a number of required and optional command-line arguments.
Use the "-h" flag to get more information.
"""

import argparse
import os.path
import time
import math
import numpy
import pylab
import scipy.stats
import matplotlib
matplotlib.rc('mathtext', fontset='stixsans', default='regular')
import re
import rmgpy
from rmgpy.quantity import constants
from rmgpy.kinetics import Arrhenius, ArrheniusEP, KineticsData
from rmgpy.data.base import getAllCombinations
from rmgpy.species import Species

from importOldDatabase import getUsername
user = getUsername()

################################################################################

def loadDatabase():
    print 'Loading RMG database...'
    from rmgpy.data.rmg import RMGDatabase
    database = RMGDatabase()
    database.load('input')
    return database

def convertKineticsToPerSiteBasis(kinetics, degeneracy):
    """
    Given high-pressure-limit `kinetics` which includes reaction-path
    `degeneracy`, convert the kinetics to be on a per-site basis.
    """
    if isinstance(kinetics, KineticsData):
        kinetics.kdata.value_si /= degeneracy
    elif isinstance(kinetics, Arrhenius):
        kinetics.A.value_si /= degeneracy
    elif isinstance(kinetics, ArrheniusEP):
        kinetics.A.value_si /= degeneracy
    else:
        raise Exception('Unable to convert kinetics of type {0} to per-site basis.'.format(kinetics.__class__))
    return kinetics
    
################################################################################

def createDataSet(label, family, database):
    """
    Create a data set from the component of the kinetics `family` indicated by
    the given `label`. The full RMG `database` must be loaded so that we can
    get thermodynamics for some species.
    """
    dataset = []
        
    if label == 'rules':
        for label, entries in family.rules.entries.items():
            for entry in entries:
                # Skip ArrheniusEP entries with Evans-Polanyi values
                if isinstance(entry.data, ArrheniusEP) and entry.data.alpha.value != 0: continue
                # Also skip entries with rank of zero (since they are just made-up numbers)
                if entry.rank == 0: continue
                template = [family.groups.entries[node] for node in label.split(';')]
                reaction = entry.item
                dataset.append([reaction, template, entry])
    else:
        label = '{0}/{1}'.format(family.label, label)
        for depository in family.depositories:
            if depository.label == label:
                break
        else:
            raise ValueError('Invalid value "{0}" for label parameter.'.format(label))
    
        for entry in depository.entries.values():
            reaction, template = database.kinetics.getForwardReactionForFamilyEntry(entry=entry, family=family.label, thermoDatabase=database.thermo)
            dataset.append([reaction, template, entry])

    return dataset

################################################################################

class ArgumentError(Exception):
    """
    An exception raised when the command-line arguments given to the script are
    invalid. Pass a string describing why the arguments are invalid.
    """
    pass

################################################################################

def generate(args):
    """
    Generate kinetics group additivity values for one (or more) reaction
    families. The `args` parameter provides the results of parsing the 
    command-line arguments using argparse.
    """
    
    # Make sure we have at least one family to generate values for
    if len(args.family) == 0 and not args.all:
        raise ArgumentError('No reaction families specified')
    
    # Make sure the method is valid
    method = args.method
    if method not in ['DistanceGeometry']:
        raise ArgumentError('Invalid method "{0}" specified'.format(method))
        
    # If training sets are not specified, 'training' and 'rules' are used
    trainingSetLabels = args.training
    if not trainingSetLabels:
        trainingSetLabels = ['TS_training']
        
    # Load the database
    database = loadDatabase()
    
    # If --all flag was specified, use all reaction families
    families = []
    if args.all:
        families = database.kinetics.families.keys()
    else:
        families = args.family
    
    # Iterate over each family, generating and saving group values
    for label in families:
        family = database.kinetics.families[label]
        family.addKineticsRulesFromTrainingSet(thermoDatabase=database.thermo)
        
        trainingSet = []
        for trainingSetLabel in trainingSetLabels:
            for reaction, template, entry in createDataSet(trainingSetLabel, family, database):
                kinetics = reaction.kinetics or entry.data
                trainingSet.append((template, kinetics))
        
        kunits = family.getRateCoefficientUnits()
        
        # Generate the group values (implemented on the KineticsGroups class)
        changed = family.groups.generateGroupAdditivityValues(trainingSet, kunits, method=method)
        
        if changed:
            # Add a note to the history of each changed item indicating that we've generated new group values
            event = [time.asctime(),user,'action','Generated new group additivity values for this entry.']
            for entry in family.groups.entries.values():
                entry.history.append(event)
            # Save the new group values to disk
            family.saveGroups(os.path.join('input', 'kinetics', 'families', label, 'groups.py'))

################################################################################

def evaluate(args):
    """
    Evaluate kinetics group additivity values for one (or more) reaction
    families. The `args` parameter provides the results of parsing the 
    command-line arguments using argparse.
    """
    method = 'rate rules' if args.rules else 'group additivity'
    plot = 'interactive' if args.interactive else 'normal'
    
    # If test sets are not specified, choose some
    testSets = args.test
    if not testSets:
        testSets = ['NIST']
    
    # Load the database
    database = loadDatabase()
    
    # If --all flag was specified, use all reaction families
    families = []
    if args.all:
        families = database.kinetics.families.keys()
    else:
        families = args.family
    
    # Iterate over each family, generating and saving group values
    for label in families:
        family = database.kinetics.families[label]
        family.addKineticsRulesFromTrainingSet(thermoDatabase=database.thermo)
        changed = evaluateKineticsGroupValues(
            database = database,
            family = family,
            method = method,
            testSetLabels = testSets,
            plot = plot,
            exactOnly = args.exact,
            estimateOnly = args.estimate,
        )

def evaluateKineticsGroupValues(family, database, method, testSetLabels, plot, exactOnly=False, estimateOnly=False):
    """
    Evaluate the kinetics group additivity values for the given reaction 
    `family` using the specified lists of depository components 
    `testSetLabels` as the test set. The already-loaded RMG database should be 
    given as the `database` parameter.
    """
    kunits = family.getRateCoefficientUnits()
    
    assert not (exactOnly and estimateOnly)
                    
    print 'Categorizing reactions in test sets for {0}'.format(family.label)
    testSets0 = []
    for testSetLabel in testSetLabels:
        testSet = createDataSet(testSetLabel, family, database)
        testSets0.append((testSetLabel, testSet))
    
    for testSetLabel, testSet in testSets0:
        for index in range(len(testSet)):
            reaction, template, entry = testSet[index]
            for reactant in reaction.reactants:
                if isinstance(reactant, Species) and not reactant.label and len(reactant.molecule) > 0:
                    reactant.label = reactant.molecule[0].toSMILES()
            for product in reaction.products:
                if isinstance(product, Species) and not product.label and len(product.molecule) > 0:
                    product.label = product.molecule[0].toSMILES()
    
    # For each entry in each test set, determine the kinetics as predicted by
    # RMG-Py and as given by the entry in the test set
    # Note that this is done on a per-site basis!
    kineticsModels = []; kineticsData = []
    testSets = []
    for testSetLabel, testSet0 in testSets0:
        testSet = []
        for index in range(len(testSet0)):
            reaction, template, entry = testSet0[index]
            krule = family.getKineticsForTemplate(template, degeneracy=1, method='rate rules')
            kgroup = family.getKineticsForTemplate(template, degeneracy=1, method='group additivity')
            kdata = convertKineticsToPerSiteBasis(reaction.kinetics, reaction.degeneracy)
            if exactOnly and not re.search('Exact', krule.comment):
                continue
            elif estimateOnly and not re.search('Estimated', krule.comment):
                continue   
            testSet.append((reaction, template, entry, krule, kgroup, kdata))
        testSets.append((testSetLabel, testSet))
    
    # Generate parity plots at several temperatures
    print 'Generating parity plots for {0}'.format(family.label)
    
    import matplotlib.pyplot as plt
    from matplotlib.widgets import CheckButtons
    
    Tdata = [500,1000,1500,2000]
    
    if kunits == 'm^3/(mol*s)':
        kunits = 'cm$^3$/mol*s'; kfactor = 1.0e6
    elif kunits == 's^-1':
        kunits = 's$^{-1}$'; kfactor = 1.0
    
    for T in Tdata:
        
        stdev_total = 0; ci_total = 0; count_total = 0
        
        # Initialize plot
        if plot == 'interactive':
            fig = pylab.figure(figsize=(10,8))
            ax = plt.subplot(1, 1, 1)
        else:
            fig = pylab.figure(figsize=(6,5))
            ax = plt.subplot(1, 1, 1) 
        ax = plt.subplot(1, 1, 1)
        lines = []
        legend = []
        
        # Iterate through the test sets, plotting each
        for testSetLabel, testSet in testSets:
            
            kmodel = []; kdata = []
            stdev = 0; ci = 0; count = 0
                
            for reaction, template, entry, kineticsRule, kineticsGroup, kineticsData in testSet:
                
                if method == 'rate rules':
                    kineticsModel = kineticsRule
                elif method == 'group additivity':
                    kineticsModel = kineticsGroup
                
                # Honor temperature ranges when plotting data
                # Place a dummy value so that the points so that the
                # interactivity is still correct
                if not kineticsData.isTemperatureValid(T):
                    kmodel.append(0.0)
                    kdata.append(0.0)
                    continue
                
                # Evaluate k(T) for both model and data at this temperature
                if isinstance(kineticsModel, ArrheniusEP):
                    km = kineticsModel.getRateCoefficient(T, 0) * kfactor
                else:
                    km = kineticsModel.getRateCoefficient(T) * kfactor
                kmodel.append(km)
                if isinstance(kineticsData, ArrheniusEP):
                    kd = kineticsData.getRateCoefficient(T, 0) * kfactor
                else:
                    kd = kineticsData.getRateCoefficient(T) * kfactor
                kdata.append(kd)
                
                # Evaluate variance
                stdev += (math.log10(km) - math.log10(kd))**2
                count += 1
            
            stdev_total += stdev
            count_total += count
            stdev = math.sqrt(stdev / (count - 1))
            ci = scipy.stats.t.ppf(0.975, count - 1) * stdev
            
            assert len(kmodel) == len(testSet)
            assert len(kdata) == len(testSet)
            
            print "Test set {0} contained {1} rates.".format(testSetLabel, count)
            print 'Confidence interval at T = {0:g} K for test set "{1}" = 10^{2:g}'.format(T, testSetLabel, ci)
        
            # Add this test set to the plot
            lines.append(ax.loglog(kdata, kmodel, 'o', picker=5)[0])
            legend.append(testSetLabel)
        
        stdev_total = math.sqrt(stdev_total / (count_total - 1))
        ci_total = scipy.stats.t.ppf(0.975, count_total - 1) * stdev_total
        
        print 'Total confidence interval at T = {0:g} K for all test sets = 10^{1:g}'.format(T, ci_total)
                
        # Finish plots
        xlim = pylab.xlim()
        ylim = pylab.ylim()
        lim = (min(xlim[0], ylim[0])*0.1, max(xlim[1], ylim[1])*10)
        ax.loglog(lim, lim, '-k')
        ax.loglog(lim, [lim[0] * 10**ci_total, lim[1] * 10**ci_total], '--k')
        ax.loglog(lim, [lim[0] / 10**ci_total, lim[1] / 10**ci_total], '--k')
        pylab.xlabel('Actual rate coefficient ({0})'.format(kunits))
        pylab.ylabel('Predicted rate coefficient ({0})'.format(kunits))
        if len(testSets) > 1:
            pylab.legend(legend, loc=4, numpoints=1)
        pylab.title('%s, T = %g K' % (family.label, T))
        pylab.xlim(lim)
        pylab.ylim(lim)
        
        plot_range = math.log10(lim[1] / lim[0])
        if plot_range > 25:
            majorLocator = matplotlib.ticker.LogLocator(1e5)
            minorLocator = matplotlib.ticker.LogLocator(1e5, subs=[1, 10, 100, 1000, 10000])
        elif plot_range > 20:
            majorLocator = matplotlib.ticker.LogLocator(1e4)
            minorLocator = matplotlib.ticker.LogLocator(1e4, subs=[1, 10, 100, 1000])
        elif plot_range > 15:
            majorLocator = matplotlib.ticker.LogLocator(1e3)
            minorLocator = matplotlib.ticker.LogLocator(1e3, subs=[1, 10, 100])
        elif plot_range > 10:
            majorLocator = matplotlib.ticker.LogLocator(1e2)
            minorLocator = matplotlib.ticker.LogLocator(1e2, subs=[1, 10])
        else:
            majorLocator = matplotlib.ticker.LogLocator(1e1)
            minorLocator = None   
        ax.xaxis.set_major_locator(majorLocator)
        ax.yaxis.set_major_locator(majorLocator)
        if minorLocator:
            ax.xaxis.set_minor_locator(minorLocator)
            ax.yaxis.set_minor_locator(minorLocator)
        
        def onpick(event):
            index = lines.index(event.artist)
            xdata = event.artist.get_xdata()
            ydata = event.artist.get_ydata()
            testSetLabel, testSet = testSets[index]
            for ind in event.ind:
                reaction, template, entry, krule, kgroup, kdata = testSet[ind]
                kunits = 'm^3/(mol*s)' if len(reaction.reactants) == 2 else 's^-1'
                print testSetLabel
                print 'template = [{0}]'.format(', '.join([g.label for g in template]))
                print 'entry = {0!r}'.format(entry)
                print str(reaction)
                print 'k_data   = {0:9.2e} {1}'.format(xdata[ind], kunits)
                print 'k_model  = {0:9.2e} {1}'.format(ydata[ind], kunits)
                print krule
                if kgroup: print kgroup
                print krule.comment
                if kgroup: print kgroup.comment
                print
                
        connection_id = fig.canvas.mpl_connect('pick_event', onpick)
        
        if plot == 'interactive':
            rax = plt.axes([0.15, 0.65, 0.2, 0.2])
            check = CheckButtons(rax, legend, [True for label in legend])
            
            def func(label):
                for index in range(len(lines)):
                    if legend[index] == label:
                        lines[index].set_visible(not lines[index].get_visible())
                plt.draw()
            check.on_clicked(func)
            
            fig.subplots_adjust(left=0.10, bottom=0.10, right=0.97, top=0.95, wspace=0.20, hspace=0.20)

        else:
            fig.subplots_adjust(left=0.15, bottom=0.14, right=0.95, top=0.93, wspace=0.20, hspace=0.20)
            filename = '{0}_{1:g}'.format(family.label, T)
            if method == 'rate rules':
                filename += '_rules'
            elif method == 'group additivity':
                filename += '_groups'
            if exactOnly:
                filename += '_exact'
            elif estimateOnly:
                filename += '_estimate'
            pylab.savefig('{0}.pdf'.format(filename))
            pylab.savefig('{0}.png'.format(filename), dpi=200)
          
        pylab.show()

################################################################################

def parseAndRunCommandLineArguments():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', help='')
    
    # generate - generate and save kinetics group additivity values
    generateParser = subparsers.add_parser('generate', help='generate and save kinetics group values for one or more families')
    generateParser.add_argument('family', metavar='<family>', type=str, nargs='*', help='the family to generate, or --all for all families')
    generateParser.add_argument('-a', '--all', action='store_true', help='generate for all families')
    generateParser.add_argument('-m', '--method', metavar='<method>', type=str, nargs='?', default='Arrhenius', help='the method to use')
    generateParser.add_argument('--training', metavar='<trainingset>', type=str, nargs='*', help='the training set(s) to use')
    generateParser.set_defaults(run=generate)
    
    # evaluate - load and evaluate kinetics group additivity values
    evaluateParser = subparsers.add_parser('evaluate', help='evaluate kinetics group values for one family')
    evaluateParser.add_argument('family', metavar='<family>', type=str, nargs=1, help='the family to evaluate')
    evaluateParser.add_argument('-a', '--all', action='store_true', help='generate for all families')
    evaluateParser.add_argument('--test', metavar='<testset>', type=str, nargs='*', help='the test set(s) to use')
    evaluateParser.add_argument('-i', '--interactive', action='store_true', help='evaluate using interactive plots')
    evaluateParser.add_argument('--rules', action='store_true', help='use rate rules instead of group additivity')
    evaluateParser.add_argument('--exact', action='store_true', help='only plot exact matches')
    evaluateParser.add_argument('--estimate', action='store_true', help='only plot estimated matches')
    evaluateParser.set_defaults(run=evaluate)
    
    args = parser.parse_args()
    
    try:
        args.run(args)
    except ArgumentError, e:
        for choice, subparser in subparsers.choices.iteritems():
            if args.command == choice:
                subparser.print_help()
                break
        else:
            parser.print_help()
        print 'ArgumentError: {0}'.format(e)

################################################################################

if __name__ == '__main__':
    parseAndRunCommandLineArguments()
