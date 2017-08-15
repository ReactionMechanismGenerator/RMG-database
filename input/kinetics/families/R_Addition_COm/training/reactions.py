#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""


entry(
    index = 1,
    label = "CO + C7H7 <=> C8H7O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (73810, 'cm^3/(mol*s)'),
        n = 2.309,
        Ea = (10.738, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: OH_phenylacetylene_CBSQB3""",
    longDesc = 
u"""
Taken from entry: benzyl + CO <=> i20
""",
)



entry(
    index = 2,
    label = "CO + CH3 <=> C2H3O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.634e+07, 'cm^3/(mol*s)'),
        n = 1.512,
        Ea = (6.013, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2006_Senosiain_H_CH2CO_High_P""",
    longDesc = 
u"""
Taken from entry: CH3 + CO <=> CH3CO
""",
)

