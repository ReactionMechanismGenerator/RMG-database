#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_isomerization/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C2H5S2 <=> C2H5S2-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.29e+11, 's^-1'),
        n = 0.211,
        alpha = 0,
        E0 = (31.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR3J_S;CsJ-HH;S-Cs(HHH)Ss
""",
)

entry(
    index = 1,
    label = "C2H5S2-3 <=> C2H5S2-4",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.88e+11, 's^-1'),
        n = 0.108,
        alpha = 0,
        E0 = (21.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR4J_SS_Cs;CsJ-HH;S-HSs
""",
)

