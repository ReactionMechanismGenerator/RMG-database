#!/usr/bin/env python
# encoding: utf-8

"""
This script is used for working with the kinetics group additivity values in
RMG. There are several different types of operations this script can do, and
each of these has a number of required and optional command-line arguments.
Use the "-h" flag to get more information.
"""

import os.path
import time
import math
import numpy
import pylab
import scipy.stats
import matplotlib
matplotlib.rc('mathtext', fontset='stixsans', default='regular')

import rmgpy
from rmgpy.quantity import constants
from rmgpy.kinetics import Arrhenius, ArrheniusEP, KineticsData
from rmgpy.data.base import getAllCombinations

from importOldDatabase import getUsername
user = getUsername()

################################################################################

def loadDatabase():
    print 'Loading RMG database...'
    from rmgpy.data.rmg import RMGDatabase
    database = RMGDatabase()
    database.load('input')
    return database

def getRateCoefficientUnits(family):
    """
    For the given reaction `family`, return the units of its forward kinetics.
    This is hardcoding of reaction families, but at least it will fail loudly
    if it encounters an unexpected family.
    """
    if family.label in ['H_Abstraction', 'R_Addition_MultipleBond', 'R_Recombination', 'HO2_Elimination_from_PeroxyRadical', 'Disproportionation', '1+2_Cycloaddition', '2+2_cycloaddition_Cd', '2+2_cycloaddition_CO', '2+2_cycloaddition_CCO', 'Diels_alder_addition', '1,2_Insertion', '1,3_Insertion_CO2', '1,3_Insertion_ROR', 'R_Addition_COm', 'Oa_R_Recombination']:
        return 'm^3/(mol*s)'
    elif family.label in ['intra_H_migration', 'Birad_recombination', 'intra_OH_migration', 'Cyclic_Ether_Formation', 'Intra_R_Add_Exocyclic', 'Intra_R_Add_Endocyclic', '1,2-Birad_to_alkene', 'Intra_Disproportionation']:
        return 's^-1'
    else:
        raise ValueError('Unable to determine units of rate coefficient for reaction family "{0}".'.format(family.label))

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
    
def createDataSet(labels, family, database):
    dataset = []
    for label in labels:
        data = []
        
        if label in ['rules','training','test','PrIMe','PrIMe_RMG_Java']:
            depository = getattr(family,label)
        else:
            raise ValueError('Invalid value "{0}" for label parameter.'.format(label))
        
        for entry in depository.entries.values():
            if isinstance(entry.data, ArrheniusEP):
                if entry.data.alpha.value != 0:
                    continue # skip things with Evans-Polanyi values
            reaction, template = database.kinetics.getForwardReactionForFamilyEntry(entry=entry, family=family.label, thermoDatabase=database.thermo)
            data.append([reaction, template, entry])
        
        if len(data) > 0:
            dataset.append([label, data])
    return dataset
    
################################################################################

def generateKineticsGroupValues(family, database, trainingSetLabels, method):
    """
    Evaluate the kinetics group additivity values for the given reaction 
    `family` using the specified lists of depository components 
    `trainingSetLabels` as the training set. The already-loaded RMG database 
    should be given as the `database` parameter.
    """
    
    kunits = getRateCoefficientUnits(family)
    
    print 'Categorizing reactions in training sets for {0}'.format(family.label)
    trainingSets = createDataSet(trainingSetLabels, family, database)
    trainingSet = []
    for label, data in trainingSets:
        trainingSet.extend(data)
    #reactions = [reaction for label, trainingSet in trainingSets for reaction, template, entry in trainingSet]
    #templates = [template for label, trainingSet in trainingSets for reaction, template, entry in trainingSet]
    #entries = [entry for label, trainingSet in trainingSets for reaction, template, entry in trainingSet]
    
    print 'Fitting new group additivity values for {0}...'.format(family.label)
    
    # keep track of previous values so we can detect if they change
    old_entries = dict()
    for label,entry in family.groups.entries.iteritems():
        if entry.data is not None:
            old_entries[label] = entry.data
    
    # Determine a complete list of the entries in the database, sorted as in the tree
    groupEntries = family.groups.top[:]
    for entry in family.groups.top:
        groupEntries.extend(family.groups.descendants(entry))
    
    # Determine a unique list of the groups we will be able to fit parameters for
    groupList = []
    for reaction, template, entry in trainingSet:
        for group in template:
            if group not in family.groups.top:
                groupList.append(group)
                groupList.extend(family.groups.ancestors(group)[:-1])
    groupList = list(set(groupList))
    groupList.sort(key=lambda x: x.index)
    
    if method == 'KineticsData':
        # Fit a discrete set of k(T) data points by training against k(T) data
        
        Tdata = [300,400,500,600,800,1000,1500,2000]
        
        #kmodel = numpy.zeros_like(kdata)
        
        # Initialize dictionaries of fitted group values and uncertainties
        groupValues = {}; groupUncertainties = {}; groupCounts = {}; groupComments = {}
        for entry in groupEntries:
            groupValues[entry] = []
            groupUncertainties[entry] = []
            groupCounts[entry] = []
            groupComments[entry] = set()
        
        # Generate least-squares matrix and vector
        A = []; b = []
        
        kdata = []
        for reaction, template, entry in trainingSet:
            
            if isinstance(reaction.kinetics, Arrhenius) or isinstance(reaction.kinetics, KineticsData):
                kd = [reaction.kinetics.getRateCoefficient(T) / reaction.degeneracy for T in Tdata]
            elif isinstance(reaction.kinetics, ArrheniusEP):
                kd = [reaction.kinetics.getRateCoefficient(T, 0) / reaction.degeneracy for T in Tdata]
            else:
                raise Exception('Unexpected kinetics model of type {0} for reaction {1}.'.format(reaction.kinetics.__class__, reaction))
            kdata.append(kd)
                
            # Create every combination of each group and its ancestors with each other
            combinations = []
            for group in template:
                groups = [group]; groups.extend(family.groups.ancestors(group))
                combinations.append(groups)
            combinations = getAllCombinations(combinations)
            # Add a row to the matrix for each combination
            for groups in combinations:
                Arow = [1 if group in groups else 0 for group in groupList]
                Arow.append(1)
                brow = [math.log10(k) for k in kd]
                A.append(Arow); b.append(brow)
                
                for group in groups:
                    groupComments[group].add("{0!s}".format(template))
            
        if len(A) == 0:
            logging.warning('Unable to fit kinetics groups for family "{0}"; no valid data found.'.format(family.groups.label))
            return
        A = numpy.array(A)
        b = numpy.array(b)
        kdata = numpy.array(kdata)
        
        x, residues, rank, s = numpy.linalg.lstsq(A, b)
        
        for t, T in enumerate(Tdata):
            
            # Determine error in each group (on log scale)
            stdev = numpy.zeros(len(groupList)+1, numpy.float64)
            count = numpy.zeros(len(groupList)+1, numpy.int)
            
            for index in range(len(trainingSet)):
                reaction, template, entry = trainingSet[index]
                kd = math.log10(kdata[index,t])
                km = x[-1,t] + sum([x[groupList.index(group),t] for group in template if group in groupList])
                variance = (km - kd)**2
                for group in template:
                    groups = [group]; groups.extend(family.groups.ancestors(group))
                    for g in groups:
                        if g not in family.groups.top:
                            ind = groupList.index(g)
                            stdev[ind] += variance
                            count[ind] += 1
                stdev[-1] += variance
                count[-1] += 1
            stdev = numpy.sqrt(stdev / (count - 1))
            ci = scipy.stats.t.ppf(0.975, count - 1) * stdev
            
            # Update dictionaries of fitted group values and uncertainties
            for entry in groupEntries:
                if entry == family.groups.top[0]:
                    groupValues[entry].append(10**x[-1,t])
                    groupUncertainties[entry].append(10**ci[-1])
                    groupCounts[entry].append(count[-1])
                elif entry in groupList:
                    index = groupList.index(entry)
                    groupValues[entry].append(10**x[index,t])
                    groupUncertainties[entry].append(10**ci[index])
                    groupCounts[entry].append(count[index])
                else:
                    groupValues[entry] = None
                    groupUncertainties[entry] = None
                    groupCounts[entry] = None
        
        # Store the fitted group values and uncertainties on the associated entries
        for entry in groupEntries:
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
        
        # Print the group values
        print '=============================== =========== =========== =========== ======='
        print 'Group                           T (K)       k(T) (SI)   CI (95%)    Count'
        print '=============================== =========== =========== =========== ======='
        entry = family.groups.top[0]
        for i in range(len(entry.data.Tdata.values)):
            label = ', '.join(['%s' % (top.label) for top in family.groups.top]) if i == 0 else ''
            T = Tdata[i]
            value = groupValues[entry][i]
            uncertainty = groupUncertainties[entry][i]
            count = groupCounts[entry][i]
            print '%-31s %-11g %-11.4e %-11.4e %-7i' % (label, T, value, uncertainty, count)
        print '------------------------------- ----------- ----------- ----------- -------'
        for entry in groupEntries:
            if entry.data is not None:
                for i in range(len(entry.data.Tdata.values)):
                    label = entry.label if i == 0 else ''
                    T = Tdata[i]
                    value = groupValues[entry][i]
                    uncertainty = groupUncertainties[entry][i]
                    count = groupCounts[entry][i]
                    print '%-31s %-11g %-11.4e %-11.4e %-7i' % (label, T, value, uncertainty, count)
        print '=============================== =========== =========== =========== ======='
    
    elif method == 'Arrhenius':
        # Fit Arrhenius parameters (A, n, Ea) by training against k(T) data
        
        Tdata = [300,400,500,600,800,1000,1500,2000]
        
        A = []; b = []
        
        kdata = []
        for reaction, template, entry in trainingSet:
            
            if isinstance(reaction.kinetics, Arrhenius) or isinstance(reaction.kinetics, KineticsData):
                kd = [reaction.kinetics.getRateCoefficient(T) / reaction.degeneracy for T in Tdata]
            elif isinstance(reaction.kinetics, ArrheniusEP):
                kd = [reaction.kinetics.getRateCoefficient(T, 0) / reaction.degeneracy for T in Tdata]
            else:
                raise Exception('Unexpected kinetics model of type {0} for reaction {1}.'.format(reaction.kinetics.__class__, reaction))
            kdata.append(kd)
            
            # Create every combination of each group and its ancestors with each other
            combinations = []
            for group in template:
                groups = [group]; groups.extend(family.groups.ancestors(group))
                combinations.append(groups)
            combinations = getAllCombinations(combinations)
            
            # Add a row to the matrix for each combination at each temperature
            for t, T in enumerate(Tdata):
                logT = math.log(T)
                Tinv = 1000.0 / (constants.R * T)
                for groups in combinations:
                    Arow = []
                    for group in groupList:
                        if group in groups:
                            Arow.extend([1,logT,-Tinv])
                        else:
                            Arow.extend([0,0,0])
                    Arow.extend([1,logT,-Tinv])
                    brow = math.log(kd[t])
                    A.append(Arow); b.append(brow)
        
        if len(A) == 0:
            logging.warning('Unable to fit kinetics groups for family "{0}"; no valid data found.'.format(family.groups.label))
            return
        A = numpy.array(A)
        b = numpy.array(b)
        kdata = numpy.array(kdata)
        
        x, residues, rank, s = numpy.linalg.lstsq(A, b)
        
        # Store the results
        family.groups.top[0].data = Arrhenius(
            A = (math.exp(x[-3]),kunits),
            n = x[-2],
            Ea = (x[-1]*1000.,"J/mol"),
            T0 = (1,"K"),
        )
        for i, group in enumerate(groupList):
            group.data = Arrhenius(
                A = (math.exp(x[3*i]),kunits),
                n = x[3*i+1],
                Ea = (x[3*i+2]*1000.,"J/mol"),
                T0 = (1,"K"),
            )
        
        # Print the results
        print '======================================= =========== =========== ==========='
        print 'Group                                   log A (SI)  n           Ea (kJ/mol)   '
        print '======================================= =========== =========== ==========='
        entry = family.groups.top[0]
        label = ', '.join(['%s' % (top.label) for top in family.groups.top])
        logA = math.log10(entry.data.A.value)
        n = entry.data.n.value
        Ea = entry.data.Ea.value / 1000.
        print '%-39s %11.3f %11.3f %11.3f' % (label, logA, n, Ea)
        print '--------------------------------------- ----------- ----------- -----------'
        for i, group in enumerate(groupList):
            label = group.label
            logA = math.log10(group.data.A.value)
            n = group.data.n.value
            Ea = group.data.Ea.value / 1000.
            print '%-39s %11.3f %11.3f %11.3f' % (label, logA, n, Ea)
        print '======================================= =========== =========== ==========='
        
    
    elif method == 'Arrhenius2':
        # Fit Arrhenius parameters (A, n, Ea) by training against (A, n, Ea) values
        
        A = []; b = []
        
        for reaction, template, entry in trainingSet:
            
            # Create every combination of each group and its ancestors with each other
            combinations = []
            for group in template:
                groups = [group]; groups.extend(family.groups.ancestors(group))
                combinations.append(groups)
            combinations = getAllCombinations(combinations)
                    
            # Add a row to the matrix for each parameter
            if isinstance(entry.data, Arrhenius) or (isinstance(entry.data, ArrheniusEP) and entry.data.alpha.value == 0):
                for groups in combinations:
                    Arow = []
                    for group in groupList:
                        if group in groups:
                            Arow.append(1)
                        else:
                            Arow.append(0)
                    Arow.append(1)
                    Ea = entry.data.E0.value if isinstance(entry.data, ArrheniusEP) else entry.data.Ea.value
                    brow = [math.log(entry.data.A.value), entry.data.n.value, Ea / 1000.]
                    A.append(Arow); b.append(brow)
        
        if len(A) == 0:
            logging.warning('Unable to fit kinetics groups for family "{0}"; no valid data found.'.format(family.groups.label))
            return
        A = numpy.array(A)
        b = numpy.array(b)
        
        x, residues, rank, s = numpy.linalg.lstsq(A, b)
        
        # Store the results
        family.groups.top[0].data = Arrhenius(
            A = (math.exp(x[-1,0]),kunits),
            n = x[-1,1],
            Ea = (x[-1,2]*1000.,"J/mol"),
            T0 = (1,"K"),
        )
        for i, group in enumerate(groupList):
            group.data = Arrhenius(
                A = (math.exp(x[i,0]),kunits),
                n = x[i,1],
                Ea = (x[i,2]*1000.,"J/mol"),
                T0 = (1,"K"),
            )
        
        # Print the results
        print '======================================= =========== =========== ==========='
        print 'Group                                   log A (SI)  n           Ea (kJ/mol)   '
        print '======================================= =========== =========== ==========='
        entry = family.groups.top[0]
        label = ', '.join(['%s' % (top.label) for top in family.groups.top])
        logA = math.log10(entry.data.A.value)
        n = entry.data.n.value
        Ea = entry.data.Ea.value / 1000.
        print '%-39s %11.3f %11.3f %11.3f' % (label, logA, n, Ea)
        print '--------------------------------------- ----------- ----------- -----------'
        for i, group in enumerate(groupList):
            label = group.label
            logA = math.log10(group.data.A.value)
            n = group.data.n.value
            Ea = group.data.Ea.value / 1000.
            print '%-39s %11.3f %11.3f %11.3f' % (label, logA, n, Ea)
        print '======================================= =========== =========== ==========='
    
    # Add a note to the history of each changed item indicating that we've generated new group values
    changed = False
    event = [time.asctime(),user,'action','Generated new group additivity values for this entry.']
    for label, entry in family.groups.entries.iteritems():
        if entry.data is not None and old_entries.has_key(label):
            if (isinstance(entry.data, KineticsData) and 
                isinstance(old_entries[label], KineticsData) and
                len(entry.data.kdata.values) == len(old_entries[label].kdata.values) and
                all(abs(entry.data.kdata.values / old_entries[label].kdata.values - 1) < 0.01)):
                #print "New group values within 1% of old."
                pass
            elif (isinstance(entry.data, Arrhenius) and 
                isinstance(old_entries[label], Arrhenius) and
                abs(entry.data.A.value / old_entries[label].A.value - 1) < 0.01 and
                abs(entry.data.n.value / old_entries[label].n.value - 1) < 0.01 and
                abs(entry.data.Ea.value / old_entries[label].Ea.value - 1) < 0.01 and
                abs(entry.data.T0.value / old_entries[label].T0.value - 1) < 0.01):
                #print "New group values within 1% of old."
                pass
            else:
                changed = True
                entry.history.append(event)
    
    return changed

################################################################################

def evaluateKineticsGroupValues(family, database, testSetLabels, mode, plot):
    """
    Evaluate the kinetics group additivity values for the given reaction 
    `family` using the specified lists of depository components 
    `testSetLabels` as the test set. The already-loaded RMG database should be 
    given as the `database` parameter.
    """
    kunits = getRateCoefficientUnits(family)
    
    # If in Java mode, only keep test sets with RMG-Java data
    if mode == 'java':
        testSetLabels0 = testSetLabels; testSetLabels = []
        for label in testSetLabels0:
            if os.path.exists(os.path.join('input', 'kinetics', 'families', family.label, '{0}_RMG_Java.py'.format(label))):
                # Okay, we've found RMG-Java data
                testSetLabels.append(label)
                testSetLabels.append('{0}_RMG_Java'.format(label))
                
    print 'Categorizing reactions in test sets for {0}'.format(family.label)
    testSets = createDataSet(testSetLabels, family, database)
    
    # For each entry in each test set, determine the kinetics as predicted by
    # RMG-Py and as given by the entry in the test set
    # Note that this is done on a per-site basis!
    if mode == 'python':
    
        kineticsModels = []; kineticsData = []
        for testSetLabel, testSet in testSets:
            for index in range(len(testSet)):
                reaction, template, entry = testSet[index]
                kmodel = family.getKineticsForTemplate(template, degeneracy=1)
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
                        kmodel = convertKineticsToPerSiteBasis(entry.data, reaction.degeneracy)
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
                print label
                print 'template = [%s]' % (', '.join([g.label for g in template]))
                print 'entry = %r' % (entry)
                print '%s' % (reaction)
                print 'k_data   = %9.2e %s' % (xdata[ind], kunits)
                print 'k_model  = %9.2e %s' % (ydata[ind], kunits)
            
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
    trainingSets = args.training
    if not trainingSets:
        trainingSets = ['rules', 'training']
        
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
        changed = generateKineticsGroupValues(
            database = database,
            family = family,
            trainingSetLabels = trainingSets,
            method = method,
        )
        if changed:
            family.saveGroups(os.path.join('input', 'kinetics', 'families', label, 'groups.py'))
    
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
        testSets = ['rules', 'training', 'PrIMe', 'test']
    
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
        changed = evaluateKineticsGroupValues(
            database = database,
            family = family,
            testSetLabels = testSets,
            mode = mode,
            plot = plot,
        )
        

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
        except Exception as e:
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

if __name__ == '__main__':

    import argparse
    
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
