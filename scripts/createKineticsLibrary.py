from rmgpy.rmg.model import Species
from rmgpy import settings
from rmgpy.data.kinetics.library import KineticsLibrary

from rmgpy.data.reference import *
import os.path
from rmgpy.kinetics.arrhenius import Arrhenius
from rmgpy.quantity import ScalarQuantity
from rmgpy.data.base import Entry
from rmgpy.reaction import Reaction
import re
"""
The purpose of this script is to create a reaction library from the least amount of input.

Might eventually make it so it reads in a csv instead of hard-coding inputs below.

Currently the numbers below are all made up, so they should not be used by any means.

For the inputs, every variable that is a list has elements where the indexes correspond with entry in another list
For example, one complete data entry for Arrhenius parameters would be A[i], n[i], and Ea[i]
"""

#initalize library variables
libraryName = 'test'
library = KineticsLibrary()
library.name = libraryName
library.label =libraryName
library.shortDesc = "Library with made up rates"
library.longDesc = """
This library is a test created to showcase the createKineticsLibrary.py script
"""

#smiles for reactants and products
#can use empty string of None for unimolecular reactions
react1smiles = ["CC=CC", "C=C", 'CCCCC[CH2]']
react2smiles = ['[CH3]', '[CH3]', '']
product1smiles = ["[CH2]C=CC", "[CH]=C", "C[CH]CCCC"]
product2smiles = ['C', 'C', None]

#kinetics parameters
AunitsBimolecular = 'cm^3/(mol*s)'
AunitsUnimolecular = 's^-1'
EaUnits = 'kcal/mol'
A = [18.06, 26.3, 18.4]
n = [3.27, 3.24, 3.27]
Ea = [6.85, 7.03, 7.15]

#write comments
shortDesc0 = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/631G(d)"""
longDesc0 = u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at
B3LYP/631G(d)" using Gaussian 03 and Gaussian 09. High-pressure-limit rate
coefficient computed TST with Eckart Tunnelling"
"""
reference0 = Article(
    authors=["K. Wang", "S. Villano", "A. Dean"],
    title=u'Reactions of allylic radicals that impact molecular weight growth kinetics',
    journal="Phys. Chem. Chem. Phys.",
    volume="17",
    pages="""6255-6273""",
    year="2015",
)
# flexible lists so that different entries can have different comments
# if you want no shortDesc or longDesc, you should use empty strings for Desc
shortDescList= [shortDesc0, '', '']
longDescList = [longDesc0, '', '']
# if you want no reference you should use None
referenceList = [reference0, None, None]

#done with inputs
#################################################################################################################
#check list lengths (useful check for some assurance you've entered things correctly)
length = len(react1smiles)
assert len(react2smiles) == length, "react2smiles has a different length than other lists"
assert len(product1smiles) == length, "product1smiles has a different length than other lists"
assert len(product2smiles) == length, "product2smiles has a different length than other lists"
assert len(A) == length, "A has a different length than other lists"
assert len(n) == length, "n has a different length than other lists"
assert len(Ea) == length, "Ea has a different length than other lists"
assert len(shortDescList) == length, "shortDescList has a different length than other lists"
assert len(longDescList) == length, "longDescList has a different length than other lists"
assert len(referenceList) == length, "referenceList has a different length than other lists"

#create entries in the library
speciesDict={}
for index, r1smiles in enumerate(react1smiles):
    bimolecular = False
    #example item
    r2smiles = react2smiles[index]
    p1smiles = product1smiles[index]
    p2smiles = product2smiles[index]

    #make species
    r1 = Species().fromSMILES(r1smiles)
    p1 = Species().fromSMILES(p1smiles)
    r2 = None
    p2 = None
    if r2smiles: r2 = Species().fromSMILES(r2smiles)
    if p2smiles: p2 = Species().fromSMILES(p2smiles)

    #make species labels
    changeDict={} #necessary in case any species already exists in the speciesDict (isomorphic not same instance)
    for spec in [r1, r2, p1, p2]:
        if spec:
            for speciesLabel, existingSpecies in speciesDict.iteritems():
                if spec.isIsomorphic(existingSpecies):
                    changeDict[spec] = existingSpecies #species already in speciesDict
                    break
            else: #species is new
                changeDict[spec] = spec
                spec_formula = spec.molecule[0].getFormula()
                if spec_formula not in speciesDict:
                    spec.label = spec_formula
                else:
                    duplicateNumber = 2
                    while (spec_formula + '-{}'.format(duplicateNumber)) in speciesDict:
                        duplicateNumber += 1
                    spec.label = spec_formula + '-{}'.format(duplicateNumber)
                speciesDict[spec.label] = spec

    #Remake species accounting for duplicates
    r1 = changeDict[r1]
    p1 = changeDict[p1]
    if r2: r2 = changeDict[r2]
    if p2: p2 = changeDict[p2]

    #create reaction
    newReaction = None
    if r2:
        bimolecular = True
        if p2:
            newReaction = Reaction(reactants = [r1, r2], products = [p1, p2])
        else:
            newReaction = Reaction(reactants = [r1, r2], products = [p1])
    elif p2:
        newReaction = Reaction(reactants = [r1], products = [p1, p2])
    else:
        newReaction = Reaction(reactants = [r1], products = [p1])

    #set Arrhenius
    newArrhenius = Arrhenius()
    if bimolecular:
        Ainstance = ScalarQuantity(A[index], AunitsBimolecular)
    else:
        Ainstance = ScalarQuantity(A[index], AunitsUnimolecular)
    newArrhenius = Arrhenius(A = Ainstance,
                             n = ScalarQuantity(n[index], ''),
                             Ea = ScalarQuantity(Ea[index], EaUnits))

    #create library entry
    referenceType = None
    if referenceList[index]: referenceType = re.sub('.*\.', '', str(referenceList[index].__class__))
    newEntry = Entry(index= index,
                     label=str(newReaction),
                     item=newReaction,
                     parent=None,
                     children=None,
                     data=newArrhenius,
                     reference=referenceList[index],
                     referenceType= referenceType,
                     shortDesc=shortDescList[index],
                     longDesc=longDescList[index],
                     rank=None,)

    #add to entry to library
    library.entries[index] = newEntry

library.save(os.path.join(settings['database.directory'],'kinetics/libraries/{0}/reactions.py'.format(libraryName)))
library.saveDictionary(os.path.join(settings['database.directory'],'kinetics/libraries/{0}/dictionary.txt'.format(libraryName)))