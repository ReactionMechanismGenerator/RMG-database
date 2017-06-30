#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C2H4O <=> C2H4O-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (100000, 's^-1'),
        n = 2,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""A. G. Vandeputte, general rate""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R_ROR;R1_doublebond;R2_doublebond;R_O
""",
)

entry(
    index = 1,
    label = "C4H8O <=> C4H8O-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (205000, 's^-1'),
        n = 2.37,
        alpha = 0,
        E0 = (48.8, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, CBS-QB3, HO""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_CsC;R_O_H
""",
)

entry(
    index = 2,
    label = "C2H4O <=> C2H4O-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (7040, 's^-1'),
        n = 2.66,
        alpha = 0,
        E0 = (48.8, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, BMK/cbsb7, HO""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H
""",
)

entry(
    index = 3,
    label = "CH2OS <=> CH2OS",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (52, 's^-1'),
        n = 3.26,
        alpha = 0,
        E0 = (19.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R_ROR;R1_doublebond_S;R2_doublebond_H;R_O_H
""",
)

entry(
    index = 4,
    label = "C2H4OS <=> C2H4OS",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (104, 's^-1'),
        n = 3.21,
        alpha = 0,
        E0 = (18.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R_ROR;R1_doublebond_S;R2_doublebond_CH3;R_O_H
""",
)

entry(
    index = 5,
    label = "C3H6OS <=> C3H6OS",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (87.5, 's^-1'),
        n = 3.23,
        alpha = 0,
        E0 = (18.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: R_ROR;R1_doublebond_S;R2_doublebond_CH2CH3;R_O_H
""",
)

