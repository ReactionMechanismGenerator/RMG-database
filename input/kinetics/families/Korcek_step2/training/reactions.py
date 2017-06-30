#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step2/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C3H6O3 <=> C2H4O + CH2O2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (6e+09, 's^-1'),
        n = 1.38,
        alpha = 0,
        E0 = (34.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""CanTherm calculations using F12-QZ energies for reactants and TS. OH rotor potentials for cyclic peroxide obtained at th3 b3lyp/cbsb7 level of theory""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: C1(R)(H)(O(OC3(OH)(R'))C2)
""",
)

