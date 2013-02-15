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
        kinetics.kdata.values /= degeneracy
    elif isinstance(kinetics, Arrhenius):
        kinetics.A.value /= degeneracy
    elif isinstance(kinetics, ArrheniusEP):
        kinetics.A.value /= degeneracy
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

def getRatesFromRMGJava(family_label, database, testSetLabels):
    """
    Get rates from RMG java for the given reaction `family` using the
    specified lists of depository components `testSetLabels` as the test sets.
    The already-loaded RMG database should be given as the `database`
    parameter.
    """
    # RMG website must be on your python path, as that's where the RMG-java interface is defined.
    from rmgweb.database import tools
    
    family = database.kinetics.families[family_label]
    
    for set_label in testSetLabels:
        depository = getKineticsSet(family, set_label)
        if depository is None:
            continue
        print "Running reactions from {0}/{1} through RMG-java...".format(family_label,set_label)
        try:
            output = rmgpy.data.kinetics.KineticsDepository(
                label = '{0}/{1}_RMG_java'.format(family_label,set_label),
                name = '{0}/{1}_RMG_java'.format(family_label,set_label),
                shortDesc = "Reactions from {0}/{1} with kinetics estimated by RMG-Java.".format(family_label,set_label),
                longDesc = "Reactions from {0}/{1} with kinetics estimated by RMG-Java.".format(family_label,set_label)
            )
            

            for entry in depository.entries.values():
                reaction, template = database.kinetics.getForwardReactionForFamilyEntry(entry=entry, family=family.label, thermoDatabase=database.thermo)
                
                reaction_from_java = tools.getRMGJavaKineticsFromReaction(reaction)
                # make the longDesc before reversing entry.item
                longDesc = """
The PrIMe reaction {0!s}
with description "{1}"
and kinetics {2!s}
was predicted by RMG-Java
as reaction {3!s}
with kinetics {4!s}
and comment "{5!s}"\n""".format(entry.item,
                           entry.longDesc,
                           entry.data,
                           reaction_from_java,
                           reaction_from_java.kinetics,
                           reaction_from_java.kinetics.comment)
                if not reaction_from_java.isIsomorphic(entry.item):
                    print """
 Reaction {0} from java is not the same as reaction sent to java.
 Probably this is just a resonance isomer and it is in fact the same,
 but if we can't pass the isomorphism check then we can't safely tell which
 direction it should be in, so we will skip the reaction entirely.
 """.format(entry.index)
                    continue #skip to next entry
                if not reaction_from_java.isIsomorphic(entry.item, eitherDirection=False):
                    # reverse the entry.item so the kinetics from the java represent it in the direction as written.
                    temporary = entry.item.reactants
                    entry.item.reactants = entry.item.products
                    entry.item.products = temporary
                    longDesc += "The reaction was reversed from the direction given in PrIMe to match the RMG-Java kinetics\n"
                    
                entry.data = reaction_from_java.kinetics
                entry.longDesc = longDesc
                entry.reference = None
                entry.referenceType = ''
                entry.history.append([time.asctime(),user,'action','Replaced kinetics with those estimated using RMG-Java.'])
                entry.shortDesc = "Rate estimated by RMG-Java"
                output.entries[entry.index] = entry
                print longDesc
        finally:
            filename = 'input/kinetics/families/{0}/{1}_RMG_Java.py'.format(family_label,set_label)
            print "Saving results (so far) in "+filename
            output.save(filename)

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
    if method not in ['KineticsData', 'Arrhenius', 'Arrhenius2']:
        raise ArgumentError('Invalid method "{0}" specified'.format(method))
        
    # If training sets are not specified, 'training' and 'rules' are used
    trainingSetLabels = args.training
    if not trainingSetLabels:
        trainingSetLabels = ['rules', 'training']
        
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
    mode = 'java' if args.java else 'python'
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
            #method = 'rate rules',
            method = 'group additivity',
            testSetLabels = testSets,
            mode = mode,
            plot = plot,
        )

def evaluateKineticsGroupValues(family, database, method, testSetLabels, mode, plot):
    """
    Evaluate the kinetics group additivity values for the given reaction 
    `family` using the specified lists of depository components 
    `testSetLabels` as the test set. The already-loaded RMG database should be 
    given as the `database` parameter.
    """
    kunits = family.getRateCoefficientUnits()
    
    # If in Java mode, only keep test sets with RMG-Java data
    if mode == 'java':
        testSetLabels0 = testSetLabels; testSetLabels = []
        for label in testSetLabels0:
            if os.path.exists(os.path.join('input', 'kinetics', 'families', family.label, '{0}_RMG_Java.py'.format(label))):
                # Okay, we've found RMG-Java data
                testSetLabels.append(label)
                testSetLabels.append('{0}_RMG_Java'.format(label))
                
    print 'Categorizing reactions in test sets for {0}'.format(family.label)
    testSets = []
    for testSetLabel in testSetLabels:
        testSet = createDataSet(testSetLabel, family, database)
        testSets.append((testSetLabel, testSet))
    
    for testSetLabel, testSet in testSets:
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
    if mode == 'python':
    
        kineticsModels = []; kineticsData = []
        for testSetLabel, testSet in testSets:
            for index in range(len(testSet)):
                reaction, template, entry = testSet[index]
                kmodel = family.getKineticsForTemplate(template, degeneracy=1, method=method)
                kdata = convertKineticsToPerSiteBasis(entry.data, reaction.degeneracy)
                testSet[index] = reaction, template, entry, kmodel, kdata
    
    elif mode == 'java':
        testSets0 = testSets; testSets = []
        # Every other item in the test sets should be an RMG-Java library
        for index in range(len(testSets0)/2):
            
            testSetLabel, testSet0 = testSets0[2*index]
            testSet0JavaLabel, testSet0Java = testSets0[2*index+1]
            
            testSet = []
            
            for reaction0, template0, entry0 in testSet0:
                for reaction, template, entry in testSet0Java:
                    if entry0.index == entry.index and entry0.label == entry.label:
                        # The java-estimated rates:
                        assert reaction.isIsomorphic(reaction0)
                        if not re.search('Average of:',entry.longDesc):
                            # exact match - unfair advantage. skip it
                            break
                        if reaction.isIsomorphic(reaction0, eitherDirection=False):
                            # it's in the right direction
                            kmodel = entry.data
                            # The following line replaces it with the python-estimated rate (so that you can compare the parity plots)
                            #kmodel = family.getKineticsForTemplate(template, degeneracy=reaction.degeneracy)
                        else:
                            # it's in the wrong direction
                            break # for now, skip it, because generating the reverse doesn't seem to work
                            kmodel = reaction.generateReverseRateCoefficient()
                        kmodel = convertKineticsToPerSiteBasis(kmodel, reaction.degeneracy)
                        # The prime database rates:
                        kdata = convertKineticsToPerSiteBasis(entry0.data, reaction0.degeneracy)
                        testSet.append([reaction, template, entry, kmodel, kdata])
                        break
            
            testSets.append([testSetLabel, testSet])
    
    # Generate parity plots at several temperatures
    print 'Generating parity plots for {0}'.format(family.label)
    
    import matplotlib.pyplot as plt
    from matplotlib.widgets import CheckButtons
    
    Tdata = [500,1000,1500,2000]
    
    if kunits == 'm^3/(mol*s)':
        kunits = 'cm^3/mol*s'; kfactor = 1.0e6
    elif kunits == 's^-1':
        kunits = 's^{-1}'; kfactor = 1.0
    
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
                
            for reaction, template, entry, kineticsModel, kineticsData in testSet:
                
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
        pylab.legend(legend, loc=4)
        pylab.title('%s, T = %g K' % (family.label, T))
        pylab.xlim(lim)
        pylab.ylim(lim)
        
        def onpick(event):
            index = lines.index(event.artist)
            xdata = event.artist.get_xdata()
            ydata = event.artist.get_ydata()
            testSetLabel, testSet = testSets[index]
            for ind in event.ind:
                reaction, template, entry, kmodel, kdata = testSet[ind]
                kunits = 'm^3/(mol*s)' if len(reaction.reactants) == 2 else 's^-1'
                print testSetLabel
                print 'template = [{0}]'.format(', '.join([g.label for g in template]))
                print 'entry = {0!r}'.format(entry)
                print str(reaction)
                print 'k_data   = {0:9.2e} {1}'.format(xdata[ind], kunits)
                print 'k_model  = {0:9.2e} {1}'.format(ydata[ind], kunits)
                print kmodel.comment
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
            
        else:
            fig.subplots_adjust(left=0.15, bottom=0.12, right=0.95, top=0.93, wspace=0.20, hspace=0.20)
            pylab.savefig('%s_%g_test.pdf' % (family.label, T))
          
        pylab.show()

################################################################################

class VerySpecificException(Exception):
    """
    This is just so that you can have an except block catch something that is never thrown,
    so that you can disable the try/except thing without changing the code much.
    """
    pass

def getFromJava(args):
    """
    This function is called when the "java" command is given on the command
    line. It causes group additivity kinetics values to be estimated by
    RMG-java and saved for all reaction families.
    """
    successes = []
    failures = []
    for family in database.kinetics.families.keys():
        try: 
         getRatesFromRMGJava(
            database = database,
            family_label = family,
            testSetLabels = ['PrIMe'],
         )
        except (VerySpecificException, Exception) as e:
            print "FAILED on "+family
            print "EXCEPTION: "+str(e)
            failures.append(family)
        else:
            successes.append(family)
    print 'COMPLETED making RMG-Java kinetics for:'
    for family in successes:
        print "  "+family
    print 'FAILED while making RMG-Java kinetics for:'
    for family in failures:
        print "  "+family
    
    #database.kinetics.saveGroups(os.path.join('input', 'kinetics', 'groups'))

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
    evaluateParser.add_argument('--java', action='store_true', help='use RMG-Java estimates instead of RMG-Py estimates')
    evaluateParser.set_defaults(run=evaluate)
    
    # java - generate kinetics estimates from RMG-Java
    javaParser = subparsers.add_parser('java', help='evaluate kinetics from RMG java for all families')
    javaParser.set_defaults(run=getFromJava)
    
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
