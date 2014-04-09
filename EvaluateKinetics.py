#!/usr/bin/env python
# encoding: utf-8

"""
This script is meant to use statistical tests to evaluate the rate rules of RMG.

It may eventually be merged into kinetics Training
"""

import kineticsTraining as kT
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

from rmgpy.quantity import Quantity, constants
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


def getKineticsDepository(family, depositoryKeyword, missingGroups):
    for tempDepository in family.depositories:
        if re.search(depositoryKeyword, tempDepository.label):
            depository=tempDepository
    
    family.fillKineticsRulesByAveragingUp()
    
    exactKinetics={}
    approxKinetics={}
    
    for key, entry in depository.entries.iteritems():
        try:
            reaction=entry.item
            template=family.getReactionTemplate(reaction)
            exactKinetics[key]=entry.data
            approxKinetics[key]=family.rules.estimateKinetics(template)

        except UndeterminableKineticsError:
            missingGroups.append([family.label, re.split(';', key), 'No Template found'])
        
        except Exception as inst:
            missingGroups.append([family.label, re.split(';', key), 'Other error, needs further investigation'])
        
        except AttributeError:
#             if family.label in logicErrorNodes.keys():
#                 logicErrorNodes[family.label].append(entryKey)
#             else:
#                 logicErrorNodes[family.label]=[entryKey]
            pass #maybe add more later

    return exactKinetics, approxKinetics, missingGroups
        
"""performs the leave one out test on a family. It returns a dictionary of the original exact nodes
and a dictionary of the new averaged nodes. The returned dictionary entries will be of a KineticModel class"""   
def getKineticsLeaveOneOut(family, missingGroups):
    entryKeys=family.rules.entries.keys()
    
    exactKinetics={}
    approxKinetics={}
    index=0
    for entryKey in entryKeys:
        index+=1
#         templateKeys=re.split(';', entryKey)
#         print entryKey, templateKeys, index
        try:
#             print entryKey
            template=family.getReactionTemplate(family.rules.entries[entryKey][0].item)

            print entryKey, [templateEntry.label for templateEntry in template], index
            exactKinetics[entryKey]=family.rules.estimateKinetics(template)
            
            familyCopy=copy.deepcopy(family)
            familyCopy.rules.entries.pop(entryKey)
            familyCopy.fillKineticsRulesByAveragingUp()
            
            approxKinetics[entryKey]=familyCopy.rules.estimateKinetics(template)
        
        except UndeterminableKineticsError:
            missingGroups.append([family.label, re.split(';', entryKey), 'No Template found'])
        
        except Exception as inst:
            missingGroups.append([family.label, re.split(';', entryKey), 'Other error, needs further investigation'])
        
        except AttributeError:
#             if family.label in logicErrorNodes.keys():
#                 logicErrorNodes[family.label].append(entryKey)
#             else:
#                 logicErrorNodes[family.label]=[entryKey]
            pass #maybe add more later

    return exactKinetics, approxKinetics, missingGroups

#returns the average temperature for the range given by the kinetic model
def getAverageTemp(kineticModel):
#     try:
#         return (kineticModel.Tmin.value + kineticModel.Tmax.value)/2
#     except AttributeError:
    return 1000
        
#calculates the parity values for each
def calculateParity(exactKineticModel, approxKineticModel, T):
    exact = exactKineticModel.getRateCoefficient(T)
    approx = approxKineticModel.getRateCoefficient(T)
    
    return float(approx)/float(exact)

"""creates a parity plot from the exactKinetics and approxKinetics (dictionarys with kineticModels are entries)
Uses the median temperature of the exactKinetics to give the best comparison. Returns the parityData in a dictionary with
{key: [exactCoefficient(T), approxCoefficient(T)}"""
def analyzeForParity(exactKinetics, approxKinetics, T=None, cutoff=0):
    parityData={}
    for key in approxKinetics:
        if T is None:
            T=getAverageTemp(exactKinetics[key])
        exact=exactKinetics[key].getRateCoefficient(T)
        approx=approxKinetics[key].getRateCoefficient(T)
        dataPoint=[exact, approx]
        if cutoff!=0 and math.log10((float(exact)/float(approx)))**2 > cutoff**2:
            continue
        parityData[key]=dataPoint
    

        
    
    return parityData

"""calculates the predicted root mean square error"""
def calculateQ(parityData):
    Q=0
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


def getKineticsFromRules(family, entryKey):
    
    #initalize family
    family.addKineticsRulesFromTrainingSet(thermoDatabase=FullDatabase.thermo)
    family.fillKineticsRulesByAveragingUp()
    
    entryKeys=re.split(';', entryKey)
    
    template=[]
    for key in entryKeys:
        template.append(family.groups.entries[key])
    
    return family.rules.estimateKinetics(template)
    

###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
###########################################################################################################
#Functions for the full Database

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
              
def consistencyTest(FullDatabase):
    
    for family in FullDatabase.kinetics.families.values():
        family.addKineticsRulesFromTrainingSet(thermoDatabase=FullDatabase.thermo)
         

    allFamilyNames=FullDatabase.kinetics.families.keys()
#     familyName='2+2_cycloaddition_CO'
#     allFamilyNames=[familyName]

    incorrectNodes={}
    logicErrorNodes={}
    
    for familyName in allFamilyNames: 
        family=FullDatabase.kinetics.families[familyName]
        print "Processing", familyName + '...', '(' + str(len(family.rules.entries)) + ' nodes)'
        entryKeys=family.rules.entries.keys()
        index=0
        for entryKey in entryKeys:
            try:
                index+=1
                print entryKey, index
                family.getReactionTemplate(family.rules.entries[entryKey][0].item)
            
            except UndeterminableKineticsError:
                if family.label in incorrectNodes.keys():
                    incorrectNodes[family.label].append([entryKey, index])
                else:
                    incorrectNodes[family.label]=[[entryKey, index]]
            
            except AttributeError:
                if family.label in logicErrorNodes.keys():
                    logicErrorNodes[family.label].append(entryKey)
                else:
                    logicErrorNodes[family.label]=[entryKey]
    
    print 'Nodes that need correcting:'
    for badFamily, badValues in incorrectNodes.iteritems():
        print badFamily, badValues
    
    print '\n'
    print 'Logic errors caused by unhandled groups:'
    for badFamily, badValues in logicErrorNodes.iteritems():
        print badFamily, badValues

    return incorrectNodes, logicErrorNodes

def NISTExact(FullDatabase, trialDir):
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
    
    trialDir=os.path.join(trialDir, 'NISTExact')
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
    
    for family in FullDatabase.kinetics.families.values():
        family.addKineticsRulesFromTrainingSet(thermoDatabase=FullDatabase.thermo)
    

    allFamilyNames=FullDatabase.kinetics.families.keys()
#     familyName='Disproportionation'
#     allFamilyNames=[familyName]
    
    missingGroups=[]
    QDict={}
    familiesWithErrors=[]
    for familyName in allFamilyNames: 
        family=FullDatabase.kinetics.families[familyName]
        print "Processing", familyName + '...', '(' + str(len(family.rules.entries)) + ' nodes)'
        if len(family.rules.entries) < 2:
            print '    Skipping', familyName, ': only has one node...'
        else:
            ##getKineticsDepository
            exactKinetics, approxKinetics, missingGroups=getKineticsDepository(family, 'NIST', missingGroups)
            
            #prune for exact matches only
            keysToRemove=[]
            for key, kinetics in approxKinetics.iteritems():
                if not re.search('Exact', kinetics.comment):
                    keysToRemove.append(key)
            
            for key in keysToRemove:
                del approxKinetics[key]
            
            try:
                parityData=analyzeForParity(exactKinetics, approxKinetics, None, 8)
            except KeyError:
                familiesWithErrors.append(family.label)
                continue
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
              
    with open(os.path.join(trialDir, 'missingNodes.csv'), 'wb') as csvfile:
        csvwriter=csv.writer(csvfile)
        for missingNode in missingGroups:
            csvwriter.writerow(missingNode)
      
    print 'These families had errors:', familiesWithErrors
#     return

"""Performs leave one out analysis on the entire database"""
def LeaveOneOut(FullDatabase, trialDir):
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
    
    trialDir=os.path.join(trialDir, 'LeaveOneOut')
    if not os.path.exists(trialDir):
        os.makedirs(trialDir)
    
    for family in FullDatabase.kinetics.families.values():
        family.addKineticsRulesFromTrainingSet(thermoDatabase=FullDatabase.thermo)
    
#     familyName='intra_substitutionCS_isomerization'
#     allFamilyNames=[familyName]
    allFamilyNames=FullDatabase.kinetics.families.keys()
    
    missingGroups=[]
    QDict={}
    familiesWithErrors=[]
    for familyName in allFamilyNames: 
        family=FullDatabase.kinetics.families[familyName]
        print "Processing", familyName + '...', '(' + str(len(family.rules.entries)) + ' nodes)'
        if len(family.rules.entries) < 2:
            print '    Skipping', familyName, ': only has one node...'
        else:
            ##getKineticsLeaveOneOut
            exactKinetics, approxKinetics, missingGroups=getKineticsLeaveOneOut(family, missingGroups)
            try:
                parityData=analyzeForParity(exactKinetics, approxKinetics, None, 8)
            except KeyError:
                familiesWithErrors.append(family.label)
                continue
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
             
    with open(os.path.join(trialDir, 'missingNodes.csv'), 'wb') as csvfile:
        csvwriter=csv.writer(csvfile)
        for missingNode in missingGroups:
            csvwriter.writerow(missingNode)
     
    print 'These families had errors:', familiesWithErrors
    return

def checkFamilies(FullDatabase):
    familyStatus={}
    for family in FullDatabase.kinetics.families:
        print family
        familyStatus[family]=FullDatabase.kinetics.families[family].checkWellFormed()
        
    with open(r'DatabaseWellFormedSummary.txt', 'wb') as outputFile:
        for family, problems in familyStatus.iteritems():
            problemsExist=[]
            for problem in problems:
                problemsExist.append(not problem==[] and not problem=={})
            if True in problemsExist:
                outputFile.write(family + '\n')
                if problemsExist[0]:
                    outputFile.write('\n' + 'These groups exist in rules.py but not groups.py:' + '\n' + "A suggested match could be incorrect, but if 'No match' is written, it is true (and most unfortunate)" + '\n')
                    for group, matchedGroups in problems[0].iteritems():
                        outputFile.write(group + ', Suggested match from groups.py: ')
                        for matchedGroup in matchedGroups:
                            if matchedGroup==matchedGroups[-1]:
                                if len(matchedGroups)>1:
                                    outputFile.write('and ')
                                outputFile.write(matchedGroup + '\n')
                            else:
                                outputFile.write(matchedGroup +', ' )
                if problemsExist[1]:
                    outputFile.write('\n' + 'These groups do not match the definition in the rule' + '\n')
                    for rule, groups in problems[1].iteritems():
                        for group in groups:
                            if group==groups[-1]:
                                if len(groups)>1:
                                    outputFile.write('and ')
                                outputFile.write(group + ' ')
                            else:
                                outputFile.write(group +', ' )
                        outputFile.write('in ' + rule + '\n')
                if problemsExist[2]:
                    outputFile.write('\n' + 'These groups are not in the tree:' + '\n')
                    for group in problems[2]:
                        outputFile.write(group + '\n')
                if problemsExist[3]:
                    outputFile.write('\n' + 'These groups are not unique' + '\n')
                    for key, groups in problems[3].iteritems():
                        outputFile.write(key + ' matches ')
                        for group in groups:
                            if group==groups[-1]:
                                if len(groups)>1:
                                    outputFile.write('and ')
                                outputFile.write(group + '\n')
                            else:
                                outputFile.write(group +', ' )
                if problemsExist[4]:
                    outputFile.write('\n' + 'These groups are not actually subgroups of their parent' + '\n')
                    for group, parent in problems[4].iteritems():
                        outputFile.write('Child: ' + group + ', Parent: ' + parent + '\n') 
                if problemsExist[5]:
                    outputFile.write('\n' + 'These groups are probably products, but you should check them anyway' + '\n')
                    for group in problems[5]:
                        outputFile.write(group + '\n')
                outputFile.write('\n\n')
if __name__ == '__main__':

    databaseProjectRootPath = os.path.dirname( os.path.abspath( __file__ ))
    #Thermo stuff
#     ThermoDatabase=ThermoDatabase()
#     ThermoDatabase.load(path)
#     ThermoDatabase.save(r'C:\RMG-database\input\thermo_test')
#     ThermoDatabase.save(path)
    FullDatabase=RMGDatabase()
#     path=r'C:\RMG-database\input\thermo'
    path = os.path.join(databaseProjectRootPath, 'input')
#     FullDatabase.load(thermoLibraries=)
    FullDatabase.load(path, kineticsFamilies='all')
    checkFamilies(FullDatabase)
#     trialDir=r'C:\Users\User1\Dropbox\Research\RMG\kinetics\LeaveOneOut\test'
#     trialDir=r'C:\RMG-database\input_test'
#     family=FullDatabase.kinetics.families['Disproportionation']
#     entryKey='Y_1centerbirad;O_Cdrad'
#     
#     test=getKineticsFromRules(family, entryKey)
#     
#     print test.comment
#     print test
    
#     NISTExact(FullDatabase, trialDir)
#     countNodesAll(NISTDatabase, trialDir)
#     consistencyTest(FullDatabase)
#     LeaveOneOut(FullDatabase, trialDir)
    