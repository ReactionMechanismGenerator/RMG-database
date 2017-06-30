#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_ROR/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "CH4O + C4H8 <=> C5H12O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (93.6, 'cm^3/(mol*s)'),
        n = 2.85,
        alpha = 0,
        E0 = (41.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H2_Cd/Nd2;H_OCmethyl
""",
)

entry(
    index = 1,
    label = "CH4O + C3H6 <=> C4H10O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (24.8, 'cm^3/(mol*s)'),
        n = 2.93,
        alpha = 0,
        E0 = (43.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H2_Cd/H/Nd;H_OCmethyl
""",
)

entry(
    index = 2,
    label = "CH4O + C2H4 <=> C3H8O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (94.6, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_OCmethyl
""",
)

entry(
    index = 3,
    label = "H2O + C2H2O <=> C2H4O2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (314, 'cm^3/(mol*s)'),
        n = 3.04,
        alpha = 0,
        E0 = (39.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: cco_2H;H_OH
""",
)

entry(
    index = 4,
    label = "H2O + C3H4O <=> C3H6O2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (103, 'cm^3/(mol*s)'),
        n = 3.05,
        alpha = 0,
        E0 = (41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: cco_HNd;H_OH
""",
)

entry(
    index = 5,
    label = "H2O + C4H6O <=> C4H8O2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2900, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (40.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: cco_Nd2;H_OH
""",
)

entry(
    index = 6,
    label = "H2O + C2H4 <=> C2H6O",
    degeneracy = 4.0,
    kinetics = ArrheniusEP(
        A = (588, 'cm^3/(mol*s)'),
        n = 2.94,
        alpha = 0,
        E0 = (53.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_OH
""",
)

entry(
    index = 7,
    label = "H2O + C3H6-2 <=> C3H8O-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (454, 'cm^3/(mol*s)'),
        n = 2.74,
        alpha = 0,
        E0 = (56.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H/Nd_Cd/H2;H_OH
""",
)

entry(
    index = 8,
    label = "H2O + C3H6 <=> C3H8O-3",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (130.4, 'cm^3/(mol*s)'),
        n = 2.92,
        alpha = 0,
        E0 = (50.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H2_Cd/H/Nd;H_OH
""",
)

entry(
    index = 9,
    label = "H2O + C4H8 <=> C4H10O-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2500, 'cm^3/(mol*s)'),
        n = 2.76,
        alpha = 0,
        E0 = (48.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H2_Cd/Nd2;H_OH
""",
)

entry(
    index = 10,
    label = "H2O + CH2S <=> CH4OS",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.486, 'cm^3/(mol*s)'),
        n = 3.55,
        alpha = 0,
        E0 = (24.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations by CAC, F12a energy""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Sd_Cd/unsub;H_OH
""",
)

entry(
    index = 11,
    label = "H2O + C2H4S <=> C2H6OS",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.00532, 'cm^3/(mol*s)'),
        n = 3.95,
        alpha = 0,
        E0 = (24.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations by CAC, F12a energy""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Sd_Cd/H/Nd;H_OH
""",
)

entry(
    index = 12,
    label = "H2O + C4H4S <=> C4H6OS",
    degeneracy = 4.0,
    kinetics = ArrheniusEP(
        A = (24.08, 'cm^3/(mol*s)'),
        n = 3.27,
        alpha = 0,
        E0 = (63.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Thiophene2;H_OH
""",
)

entry(
    index = 13,
    label = "H2O + C4H4S-2 <=> C4H6OS-2",
    degeneracy = 4.0,
    kinetics = ArrheniusEP(
        A = (83.2, 'cm^3/(mol*s)'),
        n = 3.23,
        alpha = 0,
        E0 = (61.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Thiophene3;H_OH
""",
)

entry(
    index = 14,
    label = "H2O + C7H6S <=> C7H8OS",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.0164, 'cm^3/(mol*s)'),
        n = 3.89,
        alpha = 0,
        E0 = (29.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: Sd_Cd/H/Cb;H_OH
""",
)

entry(
    index = 15,
    label = "H2O + C3H6S <=> C3H8OS",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.0001012, 'cm^3/(mol*s)'),
        n = 4.54,
        alpha = 0,
        E0 = (24.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Sd_Cd/CsCs;H_OH
""",
)

entry(
    index = 16,
    label = "H2O + C4H8-2 <=> C4H10O-3",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.0362e+08, 'cm^3/(mol*s)'),
        n = 1.302,
        alpha = 0,
        E0 = (62.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/Nd2_Cd/H2;H_OH
""",
)

entry(
    index = 17,
    label = "H2O + C4H6 <=> C4H8O",
    degeneracy = 4.0,
    kinetics = ArrheniusEP(
        A = (0.0001096, 'cm^3/(mol*s)'),
        n = 4.73,
        alpha = 0,
        E0 = (52.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""AG Vandeputte, CBS-QB3 + HO""",
    longDesc = 
u"""
Taken from entry: Updated by AG Vandeputte, CBSQB3 + HO,
    calculated for butadiene + H2O -> 2-butenol

Converted to training reaction from rate rule: Cd/H/De_Cd/H2;H_OH
""",
)

entry(
    index = 18,
    label = "CH4O-2 + C2H4 <=> C3H8O-4",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (3.58e-05, 'cm^3/(mol*s)'),
        n = 3.97,
        alpha = 0,
        E0 = (78.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""AG Vandeputte, CBS-QB3 + HO""",
    longDesc = 
u"""
Taken from entry: AG Vandeputte, calculated the rate coefficient for methanol + ethene -> propanol

Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;CH3OH
""",
)

entry(
    index = 19,
    label = "H2O + C2H4OS <=> C2H6O2S",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.08e-05, 'cm^3/(mol*s)'),
        n = 4.64,
        alpha = 0,
        E0 = (32.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Sd_Cd/CsOs;H_OH
""",
)

entry(
    index = 20,
    label = "COS + H2O <=> CH2O2S",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (8.78e-07, 'cm^3/(mol*s)'),
        n = 5.4,
        alpha = 0,
        E0 = (45.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Sd_Cdd/Od;H_OH
""",
)

entry(
    index = 21,
    label = "H2O + C3H4S <=> C3H6OS",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.1196, 'cm^3/(mol*s)'),
        n = 3.75,
        alpha = 0,
        E0 = (29.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CBS-QB3 1d-hr by CAC, F12a energy""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Sd_Cd/H/Cd;H_OH
""",
)

