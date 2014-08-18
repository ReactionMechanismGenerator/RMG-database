#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step1/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "RCH(OOH)CH2C(O)R'",
    kinetics = ArrheniusEP(
        A = (2.1e-12, 's^-1'),
        n = 6.17,
        alpha = 0,
        E0 = (19.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""CanTherm calculations using F12-QZ energies for reactants and TS. b3lyp/cbsb7 rotor potentials for HOOQ=O were used.""",
    longDesc = 
u"""

""",
)

