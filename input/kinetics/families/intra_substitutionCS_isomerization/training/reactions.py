#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_isomerization/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C2H5S <=> C2H5S-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.03e+09, 's^-1'),
        n = 1.057,
        alpha = 0,
        E0 = (45.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR3J_S;C-HHH;CsJ-HH
""",
)

entry(
    index = 1,
    label = "C3H7S <=> C3H7S-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (6.76e+10, 's^-1'),
        n = 0.394,
        alpha = 0,
        E0 = (45.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR4J_SS_Cs;C-HHH;CsJ-HH
""",
)

entry(
    index = 2,
    label = "C2H5S2 <=> C2H5S2-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.51e+11, 's^-1'),
        n = 0.327,
        alpha = 0,
        E0 = (55.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSR4J_SS_Ss;C-HHH;CsJ-HH
""",
)

