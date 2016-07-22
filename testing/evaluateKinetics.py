#!/usr/bin/env python
# encoding: utf-8

"""
This script is meant to use statistical tests to evaluate the rate rules of RMG.
"""

import os.path
import math
import numpy
import matplotlib
matplotlib.rc('mathtext', fontset='stixsans', default='regular')
import matplotlib.pyplot as plt
import pylab
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


def getKineticsDepository(family, depositoryLabel):
    
    depository = None
    for tempDepository in family.depositories:
        if re.search(depositoryLabel, tempDepository.label):
            depository=tempDepository
            
    family.fillKineticsRulesByAveragingUp()
    
    exactKinetics={}
    approxKinetics={}
    
    for key, entry in depository.entries.iteritems():
        try:
            reaction=entry.item
            template=family.getReactionTemplate(reaction)
            exactKinetics[key]=entry.data
            approxKinetics[key]=family.rules.estimateKinetics(template)[0]
        except Exception as e:
            print entry.item
            print e

    return exactKinetics, approxKinetics
        
def getKineticsLeaveOneOut(family):
    """
    Performs the leave one out test on a family. It returns a dictionary of 
    the original exact nodes and a dictionary of the new averaged nodes. 
    The returned dictionary entries will be of a KineticModel class
    """   

    entryKeys=family.rules.entries.keys()
    
    exactKinetics={}
    approxKinetics={}
    index=0
    for entryKey in entryKeys:
        index+=1
        
        nodes = entryKey.split(';')
        template = [family.groups.entries[node] for node in nodes]
        exactKinetics[entryKey], exactKineticsEntry=family.rules.estimateKinetics(template)
        
        familyCopy=copy.deepcopy(family)
        familyCopy.rules.entries.pop(entryKey)
        familyCopy.fillKineticsRulesByAveragingUp()
        
        approxKinetics[entryKey], approxKineticsEntry=familyCopy.rules.estimateKinetics(template)

    return exactKinetics, approxKinetics

        

def calculateParity(exactKineticModel, approxKineticModel, T):
    '''
    Calculates the parity values between two sets of kinetics evaluated at temperature T
    '''
    exact = exactKineticModel.getRateCoefficient(T)
    approx = approxKineticModel.getRateCoefficient(T)
    
    return float(approx)/float(exact)


def analyzeForParity(exactKinetics, approxKinetics, T=1000.0, cutoff=0.0):
    """
    Creates a parity plot from the exactKinetics and approxKinetics (dictionarys with 
    kineticModels are entries). Uses the median temperature of the exactKinetics to 
    give the best comparison. Returns the parityData in a dictionary with
    {key: [exactCoefficient(T), approxCoefficient(T)}
    """
    parityData={}
    for key in approxKinetics:
            
        exact=exactKinetics[key].getRateCoefficient(T)
        approx=approxKinetics[key].getRateCoefficient(T)
        dataPoint=[exact, approx]
        if cutoff!=0 and math.log10((float(exact)/float(approx)))**2 > cutoff**2:
            continue
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
    
    #unpack the data
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
    countList=[family.label]
    
    #get top nodes
    forwardTemplate = family.groups.top[:]

    temporary = []
    symmetricTree = False
    for entry in forwardTemplate:
        if entry not in temporary:
            temporary.append(entry)
        else:
            # duplicate node found at top of tree
            # eg. R_recombination: ['Y_rad', 'Y_rad']
            assert len(forwardTemplate)==2 , 'Can currently only do symmetric trees with nothing else in them'
            symmetricTree = True
    forwardTemplate = temporary
    
    for group in forwardTemplate:
        checkList=[group]
        childrenList=[group]
        while len(checkList)>0:
            childrenList.extend(checkList[0].children)
            checkList.extend(checkList[0].children)
            del checkList[0]
        
        countList.append(len(childrenList))
    return countList


###########################################################################################################
# Functions for the full Database

def countNodesAll(FullDatabase, trialDir):
    for family in FullDatabase.kinetics.families.values():
        family.addKineticsRulesFromTrainingSet(thermoDatabase=FullDatabase.thermo)

    allFamilyNames=FullDatabase.kinetics.families.keys()
    
    familyCount={}
    
    for familyName in allFamilyNames: 
        family=FullDatabase.kinetics.families[familyName]
        print "Processing", familyName + '...', '(' + str(len(family.rules.entries)) + ' nodes)'
        familyCount[familyName]=countNodes(family)
    
    with open(os.path.join(trialDir, 'NodeCount.csv'), 'wb') as csvfile:
        csvwriter=csv.writer(csvfile)
        for key, value in familyCount.iteritems():
            csvwriter.writerow(value)


def NISTExact(FullDatabase, trialDir):
    
    trialDir=os.path.join(trialDir, 'NISTExact')
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
    
    for family in FullDatabase.kinetics.families.values():
        family.addKineticsRulesFromTrainingSet(thermoDatabase=FullDatabase.thermo)
    

    allFamilyNames=FullDatabase.kinetics.families.keys()
#     familyName='Disproportionation'
#     allFamilyNames=[familyName]
    
    QDict={}
    
    for familyName in allFamilyNames: 
        family=FullDatabase.kinetics.families[familyName]
        print "Processing", familyName + '...', '(' + str(len(family.rules.entries)) + ' nodes)'
        if len(family.rules.entries) < 2:
            print '    Skipping', familyName, ': only has one node...'
        else:
            exactKinetics, approxKinetics =getKineticsDepository(family, 'NIST')
            
            #prune for exact matches only
            keysToRemove=[]
            for key, kinetics in approxKinetics.iteritems():
                if not re.search('Exact', kinetics.comment):
                    keysToRemove.append(key)
            
            for key in keysToRemove:
                del approxKinetics[key]
            
            parityData=analyzeForParity(exactKinetics, approxKinetics, cutoff=8.0)

            if len(parityData)<2:
                print '    Skipping', familyName, ': only one node was calculated...'
                continue
            QDict[familyName]=calculateQ(parityData)
            createParityPlot(parityData)
            plt.title(familyName)
            plt.savefig(os.path.join(trialDir, familyName +'.png'))
            plt.clf()
               
            if not os.path.exists(os.path.join(os.path.join(trialDir, 'ParityData'))):
                os.makedirs(os.path.join(trialDir, 'ParityData'))
               
            with open(os.path.join(trialDir, 'ParityData', familyName + '.csv'), 'wb') as csvfile:
                csvwriter=csv.writer(csvfile)
                for key, value in parityData.iteritems():
                    csvwriter.writerow([key, value[0]/value[1], approxKinetics[key].comment]) 
 
    with open(os.path.join(trialDir, 'QDict_LOO.csv'), 'wb') as csvfile:
        csvwriter=csv.writer(csvfile)
        for key, value in QDict.iteritems():
            csvwriter.writerow([key, value])
              
      



def leaveOneOut(FullDatabase, trialDir):
    """
    Performs leave one out analysis on all the kinetics families.
    """
    
    trialDir=os.path.join(trialDir, 'LeaveOneOut')
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
    
    for family in FullDatabase.kinetics.families.values():
        family.addKineticsRulesFromTrainingSet(thermoDatabase=FullDatabase.thermo)
    
#     familyName='intra_substitutionCS_isomerization'
#     allFamilyNames=[familyName]
    allFamilyNames=FullDatabase.kinetics.families.keys()
    
    QDict={}

    for familyName in allFamilyNames: 
        family=FullDatabase.kinetics.families[familyName]
        print "Processing", familyName + '...', '(' + str(len(family.rules.entries)) + ' nodes)'
        if len(family.rules.entries) < 2:
            print '    Skipping', familyName, ': only has one node...'
        else:
            exactKinetics, approxKinetics =getKineticsLeaveOneOut(family)
            parityData=analyzeForParity(exactKinetics, approxKinetics, cutoff=8.0)

            if len(parityData)<2:
                print '    Skipping', familyName, ': only one node was calculated...'
                continue
            QDict[familyName]=calculateQ(parityData)
            createParityPlot(parityData)
            plt.title(familyName)
            plt.savefig(os.path.join(trialDir, familyName +'.png'))
            plt.clf()
              
            if not os.path.exists(os.path.join(os.path.join(trialDir, 'ParityData'))):
                os.makedirs(os.path.join(trialDir, 'ParityData'))
              
            with open(os.path.join(trialDir, 'ParityData', familyName + '.csv'), 'wb') as csvfile:
                csvwriter=csv.writer(csvfile)
                for key, value in parityData.iteritems():
                    csvwriter.writerow([key, value[0]/value[1], approxKinetics[key].comment]) 

    with open(os.path.join(trialDir, 'QDict_LOO.csv'), 'wb') as csvfile:
        csvwriter=csv.writer(csvfile)
        for key, value in QDict.iteritems():
            csvwriter.writerow([key, value])
     
    return


if __name__ == '__main__':
    from rmgpy import settings
    print 'Loading the RMG database...'
    FullDatabase=RMGDatabase()
    FullDatabase.load(settings['database.directory'], 
                      kineticsFamilies=['Disproportionation'], 
                      kineticsDepositories='all',
                      thermoLibraries=[],
                      reactionLibraries=[],
                      )

    trialDir = os.path.join(settings['database.directory'],'..','testing','eval')
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
    print 'Evaluating the NIST Kinetics against the RMG estimates...'
    NISTExact(FullDatabase, trialDir)
    
    print 'Counting the rate rules in the families...'
    countNodesAll(FullDatabase, trialDir)
    
    print 'Performing the leave on out test on the kinetics families...'
    leaveOneOut(FullDatabase, trialDir)
    