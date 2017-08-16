#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_CSm/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "H + CS <=> CHS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20.92, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: CSm;Y_rad
""",
)

entry(
    index = 1,
    label = "H + CS <=> CHS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.18e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.3386, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""Guessed from CO+H_rad""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: CSm;H_rad
""",
)

entry(
    index = 2,
    label = "CS + CH3 <=> C2H3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 2.11,
        Ea = (10.2926, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CAC CBS-QB3 calc (using methyl group), HO Approx""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: CSm;C_methyl
""",
)

entry(
    index = 3,
    label = "CS + C2H5 <=> C3H5S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+10, 'cm^3/(mol*s)'),
        n = 2.22,
        Ea = (1.63176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CAC CBS-QB3 calc (using ethyl group), HO approx""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: CSm;CH2CH3
""",
)

