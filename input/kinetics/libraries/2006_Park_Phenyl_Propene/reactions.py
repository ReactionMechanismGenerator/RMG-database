#!/usr/bin/env python
# encoding: utf-8

name = "2006_Park_Phenyl_Propene"
shortDesc = u""
longDesc = u"""
TST entrance kinetics for Phenyl + Propene from:

Park, J.; Nam, G. J.; Tokmakov, I. V.; Lin, M. C., 
Experimental and Theoretical Studies of the Phenyl Radical Reaction with Propene. 
J. Phys. Chem. A 2006, 110, 8729-8735. 

Predictions are partially validated against CRDS epxeriments.

"""
entry(
    index = 1,
    label = "C6H5 + C3H6 <=> i1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (0.735, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2006 Park',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2006 Park
""",
)

entry(
    index = 2,
    label = "C6H5 + C3H6 <=> i2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (1.683, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2006 Park',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2006 Park
""",
)

entry(
    index = 3,
    label = "C6H5 + C3H6 <=> CH2CHCH2 + C6H6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.36, 'cm^3/(mol*s)'),
        n = 3.82,
        Ea = (1.437, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2006 Park',
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
From 2006 Park
""",
)

