#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C10H11_2"
shortDesc = u"Indene reacting with CH3"
longDesc = u"""
Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene
Alexander M. Mebel, Yuri Georgievskii, Ahren W. Jasper and Stephen J. Klippenstein
Faraday Discuss., 2016, 195, 637

Potential energy diagram for the indene + CH3 reaction calculated at the G3(MP2,CC)//B3LYP/6-311G** level of theory.
"""
entry(
    index = 1,
    label = "3_methylindene + H <=> W1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.059e+08, 'cm^3/(mol*s)'),
        n = 1.596,
        Ea = (4.69, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "1_methylindene + H <=> W1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.904e+08, 'cm^3/(mol*s)'),
        n = 1.534,
        Ea = (3.418, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "Indene + CH3 <=> W1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3206, 'cm^3/(mol*s)'),
        n = 2.611,
        Ea = (8.195, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "2_methylindene + H <=> W2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.441e+08, 'cm^3/(mol*s)'),
        n = 1.514,
        Ea = (2.403, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "Indene + CH3 <=> W2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5064, 'cm^3/(mol*s)'),
        n = 2.608,
        Ea = (5.867, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

