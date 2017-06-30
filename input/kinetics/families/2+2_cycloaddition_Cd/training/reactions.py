#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "CH2O + C2H4 <=> C3H6O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.33e+06, 'cm^3/(mol*s)', '*|/', 5),
        n = 1.65,
        alpha = 0,
        E0 = (54.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: db_2H;mb_OC
""",
)

