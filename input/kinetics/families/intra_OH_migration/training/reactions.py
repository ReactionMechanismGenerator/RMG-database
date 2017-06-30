#!/usr/bin/env python
# encoding: utf-8

name = "intra_OH_migration/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C2H5O2 <=> C2H5O2-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.39e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OOH_S;C_rad_out_2H
""",
)

entry(
    index = 1,
    label = "C3H7O2 <=> C3H7O2-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.69e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (24.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R2OOH_S;C_rad_out_H/NonDeC
""",
)

entry(
    index = 2,
    label = "C3H7O2-3 <=> C3H7O2-4",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (4.47e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (27.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OOH_SS;C_rad_out_2H
""",
)

entry(
    index = 3,
    label = "C4H9O2 <=> C4H9O2-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.88e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OOH_SS;C_rad_out_H/NonDeC
""",
)

entry(
    index = 4,
    label = "C5H11O2 <=> C5H11O2-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (4.79e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R3OOH_SS;C_rad_out_Cs2
""",
)

entry(
    index = 5,
    label = "C4H9O2-3 <=> C4H9O2-4",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.12e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (16.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OOH_SSS;C_rad_out_2H
""",
)

entry(
    index = 6,
    label = "C5H11O2-3 <=> C5H11O2-4",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OOH_SSS;C_rad_out_H/NonDeC
""",
)

entry(
    index = 7,
    label = "C6H13O2 <=> C6H13O2-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (8.71e+09, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R4OOH_SSS;C_rad_out_Cs2
""",
)

