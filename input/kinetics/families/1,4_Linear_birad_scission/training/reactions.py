#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Linear_birad_scission/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C4H8 <=> C2H4 + C2H4-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (5e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 5,
    shortDesc = u"""AG Vandeputte estimate (should be fast)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: RJJ
""",
)

