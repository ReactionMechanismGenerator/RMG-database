#!/usr/bin/env python
# encoding: utf-8

"""
This script is meant to use statistical tests to evaluate the rate rules of RMG.
"""

import os.path
import math
import numpy
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import re
import copy
import csv

from rmgpy.thermo import *
from rmgpy.kinetics import *
from rmgpy.data.reference import *
from rmgpy.data.base import Entry
from rmgpy.data.thermo import ThermoDatabase
from rmgpy.data.kinetics import saveEntry
from rmgpy.molecule import Molecule
from rmgpy.species import Species
from rmgpy.reaction import Reaction
from rmgpy.data.rmg import RMGDatabase
from rmgpy.data.kinetics.common import UndeterminableKineticsError

def getKineticsDepository(FullDatabase, family, depositoryLabel):
    """
    Retrieve dictionaries of exact kinetics from NIST depository and approximated kinetics 
    for those same reactions from RMG.  
    Note: does NOT average up the database or create any rate rules from training data.  
    If that is desired it must be done prior to entering this function.
    """
    
    depository = None
    for tempDepository in family.depositories:
        if re.search(re.escape(depositoryLabel), tempDepository.label):
            depository=tempDepository
            break
    else:
        print 'Depository {} not found in {} family.'.format(depositoryLabel, family.label)
        return
            
    
    exactKinetics={}
    approxKinetics={}
    
    for key, entry in depository.entries.iteritems():
        try:
            reaction=entry.item
            template=family.getReactionTemplate(reaction)
            exactKinetics[key]=entry.data
            approxKinetics[key]=family.rules.estimateKinetics(template)[0]
        except UndeterminableKineticsError:
            # See if the reaction was written in the reverse direction
            reaction = Reaction(reactants = copy.deepcopy(entry.item.products),
                                products = copy.deepcopy(entry.item.reactants),
                                kinetics = copy.deepcopy(entry.data)
                                )
            
            template=family.getReactionTemplate(reaction)

            # Getting thermo data erases the atomLabels, so do this after finding the template
            # But we need it for setting the reverse kinetics
            for spec in reaction.reactants + reaction.products:
                spec.getThermoData()

            reverseKinetics = reaction.generateReverseRateCoefficient()
            reaction.kinetics = reverseKinetics
            
            exactKinetics[key]=reaction.kinetics
            approxKinetics[key]=family.rules.estimateKinetics(template)[0]

    return exactKinetics, approxKinetics
        
def getKineticsLeaveOneOut(family, averaging=True):
    """
    Performs the leave one out test on a family. It returns a dictionary of 
    the original exact nodes and a dictionary of the new averaged nodes. 
    The returned dictionary entries will be of a KineticModel class
    It deletes a single entry in the family, and then re-averages the tree
    and then tries to re-estimate that original deleted entry.
    
    The original family should not contained averaged nodes when starting out.  The
    leave one out test should be performed only for original exact matches.
    
    There are two methods of performing the leave one out test:
    
    averaging=True, each exact entry is removed, and the family's trees
    are re-averaged WITHOUT that entry and used to estimate the original entry. 
    This method tests how the database performs to estimate data when it is
    missing.  Speed of this test is slow.
    
    averaging=False, the family is pre-averaged, and then the exact entry
    is removed, and RMG is used to re-estimate that entry.  This method
    tests how the database averaging scheme performs, since we expect the
    estimate to use a more general node that still incorporates the data
    from the original exact entry. Speed of this test is fast.
    """   
    exactKinetics={}
    approxKinetics={}

    rootTemplate = family.getRootTemplate()

    for entryKey in family.rules.entries.keys():
        template = family.retrieveTemplate(entryKey.split(';'))
        exactKineticsEntry=family.rules.getRule(template)  # fetch the best matched rule
        if exactKineticsEntry.rank == 0:
            # Skip rank zero entries, because they are replaced by averaged values
            # during model generation
            continue

        exactKineticsData = exactKineticsEntry.data
        if exactKineticsData.comment:
            if 'training' not in exactKineticsData.comment:
                # Averaged nodes have kinetics data comments, so skip them unless 
                # They were created from training reactions
                continue

        exactKinetics[entryKey] = exactKineticsData

        if averaging:
            # In this scheme, we remove the data fully and try to pretend the database 
            # wants this kinetic value when we know nothing about it
            familyCopy=copy.deepcopy(family)
            familyCopy.rules.entries.pop(entryKey)
            familyCopy.fillKineticsRulesByAveragingUp()
            approxKinetics[entryKey], approxKineticsEntry=familyCopy.rules.estimateKinetics(template)
        else:
            # In this scheme, do not re-average the tree, just try to see if the nearest
            # best node provides a good estimate for the original kinetics.  
            # This takes significanty less time to run, but is not a true validation of the data, 
            # it is just testing our kinetics selection algorithm

            # Skip the top node in this scheme, because nothing can predict it if removed

            if template == rootTemplate:
                continue

            originalEntry = family.rules.entries[entryKey]
            family.rules.entries.pop(entryKey)
            approxKinetics[entryKey], approxKineticsEntry=family.rules.estimateKinetics(template)
            # Re-add the data back into the original family
            family.rules.entries[entryKey] = originalEntry


        
        

    return exactKinetics, approxKinetics

        

def calculateParity(exactKineticModel, approxKineticModel, T):
    '''
    Calculates the parity values between two sets of kinetics evaluated at temperature T
    '''
    exact = exactKineticModel.getRateCoefficient(T)
    approx = approxKineticModel.getRateCoefficient(T)
    
    return float(approx)/float(exact)


def analyzeForParity(exactKinetics, approxKinetics, T=1000.0):
    """
    Creates a parity plot from the exactKinetics and approxKinetics (dictionarys with 
    kineticModels are entries). Uses the user specified temperature T to 
    compare the two sets of kinetics k(T). Returns the parityData in a dictionary with
    {key: [exactCoefficient(T), approxCoefficient(T)}
    """
    parityData={}
    for key in approxKinetics:
            
        exact=exactKinetics[key].getRateCoefficient(T)
        approx=approxKinetics[key].getRateCoefficient(T)
        dataPoint=[exact, approx]
        parityData[key]=dataPoint

    return parityData


def calculateQ(parityData):
    """
    Calculates the predicted root mean square error
    """
    Q=0.0
    for key, value in parityData.iteritems():
        Q+=(math.log10(value[0]/value[1]))**2
    return (Q/len(parityData))**0.5

def createParityPlot(parityData):
    
    keyList=parityData.keys()
    xAxis=[]
    yAxis=[]
    for key in keyList:
        xAxis.append(parityData[key][0])
        yAxis.append(parityData[key][1])
    
    plt.loglog(xAxis,yAxis, 'ks')
    
    minimum=min(min(xAxis), min(yAxis))
    maximum=max(max(xAxis), max(yAxis))
    plt.loglog([minimum/10,maximum*10], [minimum/10,maximum*10], 'k')
    plt.loglog([minimum*10,maximum*10], [minimum/10,maximum/10], 'k--')
    plt.loglog([minimum/10,maximum/10],[minimum*10,maximum*10], 'k--')
    plt.xlabel('Actual rate coefficient (cm^3/mol-s)')
    plt.ylabel('Estimated rate coefficient (cm^3/mol-s)')
    plt.axis([minimum/10, maximum*10, minimum/10, maximum*10])

def countNodes(family):
    """
    Count the number of groups under each tree in the Family's Groups.
    Returns a list containing the following information
    [Family Label, Number of Rules, Top Node Label 1, Number of Children, ..., Top Node Label N, Number of Children]
    """
    countList=[family.label]
    
    #get top nodes
    forwardTemplate = family.groups.top[:]

    temporary = []
    for entry in forwardTemplate:
        if entry not in temporary:
            temporary.append(entry)
        else:
            # Duplicate node found at top of tree
            # eg. R_recombination: ['Y_rad', 'Y_rad']
            assert len(forwardTemplate)==2 , 'Duplicate entries in the top nodes must only be in symmetric trees containing exactly 2 total nodes, i.e. [Yrad, Yrad]'
            
    forwardTemplate = temporary
    
    countList.append(len(family.rules.entries))
    for group in forwardTemplate:
        checkList=[group]
        childrenList=[group]
        while len(checkList)>0:
            childrenList.extend(checkList[0].children)
            checkList.extend(checkList[0].children)
            del checkList[0]
        
        countList.extend([group.label, len(childrenList)])
    
    return countList


###########################################################################################################
# Functions for the full Database

def obtainKineticsFamilyStatistics(FullDatabase, trialDir):
    """
    Obtains statistics for the kinetics families by creating
    a FamilyStatistics.csv file that gives information about each family: the total number of
    rules, and the top node names and the number of groups under each.
    Note: does NOT average up the database or create any rate rules from training data.  
    If that is desired it must be done prior to entering this function.  (averaging may not be desired
    as it would add non-exact rules to the rule count)
    """
    allFamilyNames=FullDatabase.kinetics.families.keys()
    allFamilyNames.sort(key=str.lower)  # Perform test on families alphabetically
    
    with open(os.path.join(trialDir, 'FamilyStatistics.csv'), 'wb') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(['Family','Number of Rules', 'Top Node 1', 'Number of Groups', 'Top Node 2', 'Number of Groups', 'Top Node 3', 'Number of Groups'])
        
        for familyName in allFamilyNames: 
            family=FullDatabase.kinetics.families[familyName]
            print "Processing", familyName + '...', '(' + str(len(family.rules.entries)) + ' rate rules)'
            # Save to csv file
            csvwriter.writerow(countNodes(family))


def compareNIST(FullDatabase, trialDir, pruneForExact=False):
    """
    Compare NIST reaction kinetics with estimates from RMG.  Creates parity plot and
    calculates the predicted root mean square error from the families.
    Note: does NOT average up the database or create any rate rules from training data.  
    If that is desired it must be done prior to entering this function.
    
    if pruneForExact=True, only the comparisons again exact match kinetics from RMG are returned
    otherwise, estimated and exact matches are all included in the parity data.
    """
    trialDir=os.path.join(trialDir, 'compareNIST')
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
    

    allFamilyNames=FullDatabase.kinetics.families.keys()
    allFamilyNames.sort(key=str.lower)  # Perform test on families alphabetically
    
    QDict={}
    
    with open(os.path.join(trialDir, 'QDict_LOO.csv'), 'wb') as csvfile:
        csvwriter=csv.writer(csvfile)
        for familyName in allFamilyNames: 
            family=FullDatabase.kinetics.families[familyName]
            print "Processing", familyName + '...', '(' + str(len(family.rules.entries)) + ' rate rules)'
            if len(family.rules.entries) < 2:
                print '    Skipping', familyName, ': only has one rate rule...'
            else:
                exactKinetics, approxKinetics = getKineticsDepository(FullDatabase, family, 'NIST')
                
                
                if pruneForExact:
                    # prune for exact matches only
                    keysToRemove=[]
                    for key, kinetics in approxKinetics.iteritems():
                        if not re.search('Exact', kinetics.comment):
                            keysToRemove.append(key)
                    
                    for key in keysToRemove:
                        del approxKinetics[key]
                
                parityData=analyzeForParity(exactKinetics, approxKinetics)

                if len(parityData)<2:
                    print '    Skipping', familyName, ': {} reactions were compared...'.format(len(parityData))
                    continue
                QDict[familyName]=calculateQ(parityData)
                createParityPlot(parityData)
                plt.title(familyName)
                plt.savefig(os.path.join(trialDir, familyName +'.png'))
                plt.clf()
                   
                if not os.path.exists(os.path.join(os.path.join(trialDir, 'ParityData'))):
                    os.makedirs(os.path.join(trialDir, 'ParityData'))
                   
                with open(os.path.join(trialDir, 'ParityData', familyName + '.csv'), 'wb') as paritycsvfile:
                    paritycsvwriter=csv.writer(paritycsvfile)
                    for key, value in parityData.iteritems():
                        paritycsvwriter.writerow([key, value[0]/value[1], approxKinetics[key].comment]) 
            
                # Save data to csv file
                csvwriter.writerow([familyName, QDict[familyName]])
              
      



def leaveOneOut(FullDatabase, trialDir, averaging=True):
    """
    Performs leave one out analysis on all the kinetics families.
    The algorithm deletes a single entry in the family, and then re-averages the tree
    and then tries to re-estimate that original deleted entry.  The difference between
    these values is used to create a parity plot and averaged mean squared error statistics.
    
    Note: training data and averaging of the database is not performed at the beginning of
    this function, and must be performed outside the function.  Averaging the trees should not
    be performed so as to not perform the leave one out test on rate rules that were averaged.
    """
    
    trialDir=os.path.join(trialDir, 'leaveOneOut')
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
    
    allFamilyNames=FullDatabase.kinetics.families.keys()
    allFamilyNames.sort(key=str.lower)  # Perform test on families alphabetically
    QDict={}


    with open(os.path.join(trialDir, 'QDict_LOO.csv'), 'wb') as csvfile:
        csvwriter=csv.writer(csvfile)

        for familyName in allFamilyNames: 
            family=FullDatabase.kinetics.families[familyName]
            print "Processing", familyName + '...', '(' + str(len(family.rules.entries)) + ' rate rules)'
            if len(family.rules.entries) < 2:
                print '    Skipping', familyName, ': only has one rate rule...'
            else:
                if not averaging:
                    # Pre-average the family if averaging is not turned on
                    family.fillKineticsRulesByAveragingUp()
                exactKinetics, approxKinetics = getKineticsLeaveOneOut(family, averaging)
                parityData=analyzeForParity(exactKinetics, approxKinetics)

                if len(parityData)<2:
                    print '    Skipping', familyName, ': {} rate rules were compared...'.format(len(parityData))
                    continue
                QDict[familyName]=calculateQ(parityData)
                createParityPlot(parityData)
                plt.title(familyName)
                plt.savefig(os.path.join(trialDir, familyName +'.png'))
                plt.clf()
                  
                if not os.path.exists(os.path.join(os.path.join(trialDir, 'ParityData'))):
                    os.makedirs(os.path.join(trialDir, 'ParityData'))
                  
                with open(os.path.join(trialDir, 'ParityData', familyName + '.csv'), 'wb') as paritycsvfile:
                    paritycsvwriter=csv.writer(paritycsvfile)
                    for key, value in parityData.iteritems():
                        paritycsvwriter.writerow([key, value[0]/value[1], approxKinetics[key].comment]) 

                # Save to csv file
                csvwriter.writerow([familyName, QDict[familyName]])
     
    return


if __name__ == '__main__':
    from rmgpy import settings
    
    # Create the data evaluation directory
    trialDir = os.path.join(settings['database.directory'],'..','testing','eval')
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
        
    print 'Loading the RMG database...'
    FullDatabase=RMGDatabase()
    FullDatabase.load(settings['database.directory'], 
                      kineticsFamilies='all', 
                      kineticsDepositories='all',
                      thermoLibraries=['primaryThermoLibrary'],   # Use just the primary thermo library, which contains necessary small molecular thermo
                      reactionLibraries=[],
                      )

    # Prepare the database by loading training reactions but not averaging the rate rules
    for family in FullDatabase.kinetics.families.values():
        family.addKineticsRulesFromTrainingSet(thermoDatabase=FullDatabase.thermo)
    
    print '--------------------------------------------'
    print 'Obtaining statistics for the families...'
    obtainKineticsFamilyStatistics(FullDatabase, trialDir)
    
    print '--------------------------------------------'
    print 'Performing the leave on out test on the kinetics families...'
    leaveOneOut(FullDatabase, trialDir, averaging=False)
    
    print '--------------------------------------------'
    print 'Filling up the family rate rules by averaging... Expect larger number of rate rules in subsequent tests'
    # Fill in the rate rules by averaging when we are ready to compare real kinetics
    for family in FullDatabase.kinetics.families.values():
        family.fillKineticsRulesByAveragingUp()
    

    print '--------------------------------------------'
    print 'Evaluating the NIST Kinetics against the RMG estimates...'
    compareNIST(FullDatabase, trialDir)
    