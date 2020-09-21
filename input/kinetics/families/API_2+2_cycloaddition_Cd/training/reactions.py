#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_Cd/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CH2O + C2H4 <=> C3H6O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.66e+06, 'cm^3/(mol*s)', '*|/', 5),
        n = 1.65,
        Ea = (226.564, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    longDesc = 
u"""
Converted to training reaction from rate rule: db_2H;mb_OC
""",
)

