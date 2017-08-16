#!/usr/bin/env python
# encoding: utf-8

name = "2016_Mebel_C6H5_C2H2_High_P"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "W1 <=> P1 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.323e+10, 's^-1'), n=1.103, Ea=(38.251, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 1,
    label = "W1 <=> W3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.445e+06, 's^-1'), n=1.735, Ea=(23.162, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "R1 + C2H2 <=> W1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.954e+07, 'cm^3/(mol*s)'),
        n = 1.638,
        Ea = (3.448, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

