#!/usr/bin/env python
# encoding: utf-8

name = "1,2_shiftS/training"
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
        A = (1e+08, 's^-1'),
        n = 2,
        alpha = 0,
        E0 = (40, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 1,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: XSYJ;YJ-Ss;C-Ss
""",
)

