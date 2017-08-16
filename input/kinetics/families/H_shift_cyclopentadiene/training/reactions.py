#!/usr/bin/env python
# encoding: utf-8

name = "H_shift_cyclopentadiene/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.39e+07, 's^-1'), n=1.58, Ea=(21.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product21
""",
)

entry(
    index = 1,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.06e+07, 's^-1'), n=1.74, Ea=(24.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product21 <=> product22
""",
)

entry(
    index = 2,
    label = "C5H6 <=> C5H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.06e+07, 's^-1'),
        n = 1.74,
        Ea = (101.671, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 4,
    shortDesc = u"""AG Vandeputte, CBS-QB3""",
    longDesc = 
u"""
Taken from entry: Rate taken from H shift in ethyleneCPD

Degeneracy not recalculated

Converted to training reaction from rate rule: cyclopentadiene
""",
)

