#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step1/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C3H6O3 <=> C3H6O3-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.1e-12, 's^-1'),
        n = 6.17,
        alpha = 0,
        E0 = (19.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 0,
    shortDesc = u"""CanTherm calculations using F12-QZ energies for reactants and TS. b3lyp/cbsb7 rotor potentials for HOOQ=O were used.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: RCH(OOH)CH2C(O)R'
""",
)

