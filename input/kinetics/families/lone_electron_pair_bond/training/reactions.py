#!/usr/bin/env python
# encoding: utf-8

name = "lone_electron_pair_bond/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "O + H3N <=> H3NO",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (100, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: N3sRRR;O_atom_singlet
""",
)

