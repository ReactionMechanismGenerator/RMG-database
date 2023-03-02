#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Linear_birad_scission/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 0,
    label = "C8H12_DVT <=> C4H6_BD + C4H6_BD2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.42238e+12, 's^-1'),
        n = -0.0448663,
        Ea = (52.0893, 'kJ/mol'),
        T0 = (1, 'K')),
    rank = 5,
    shortDesc = u"""Level of theory: CBS-QB3 with 1D rotors in B3LYP/CBSB7""",
    longDesc = 
u"""
calculated by Duminda Ranasinghe and Hao-Wei Pang in March 2019
""",
)
