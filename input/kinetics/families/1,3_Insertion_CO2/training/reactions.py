#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "H2 + CO2 <=> CH2O2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.51e+09, 'cm^3/(mol*s)'),
        n = 1.23,
        alpha = 0,
        E0 = (73.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: CO2_Cdd;H2
""",
)

entry(
    index = 1,
    label = "CO2 + CH4 <=> C2H4O2",
    degeneracy = 8.0,
    kinetics = ArrheniusEP(
        A = (36240, 'cm^3/(mol*s)'),
        n = 2.83,
        alpha = 0,
        E0 = (79.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: CO2_Cdd;C_methane
""",
)

entry(
    index = 2,
    label = "CO2 + C2H6 <=> C3H6O2",
    degeneracy = 12.0,
    kinetics = ArrheniusEP(
        A = (130800, 'cm^3/(mol*s)'),
        n = 2.56,
        alpha = 0,
        E0 = (76.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: CO2_Cdd;C_pri/NonDeC
""",
)

entry(
    index = 3,
    label = "CO2 + C3H8 <=> C4H8O2",
    degeneracy = 4.0,
    kinetics = ArrheniusEP(
        A = (424000, 'cm^3/(mol*s)'),
        n = 2.13,
        alpha = 0,
        E0 = (77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: CO2_Cdd;C/H2/NonDeC
""",
)

entry(
    index = 4,
    label = "CO2-2 + C3H8-2 <=> C4H8O2-2",
    degeneracy = 4.0,
    kinetics = ArrheniusEP(
        A = (292, 'cm^3/(mol*s)'),
        n = 3.13,
        alpha = 0,
        E0 = (118, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""Aaron Vandeputte calculation for methylpropanate using BMK/CBSB7""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: CO2_Od;C_methyl_C_pri
""",
)

