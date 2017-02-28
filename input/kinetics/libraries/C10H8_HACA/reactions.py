#!/usr/bin/env python
# encoding: utf-8

name = "C10H8_HACA"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "A3a + C2H2 <=> A4b",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (750000, 'cm^3/(mol*s)'),
        n = 1.979,
        Ea = (5066, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "A8 <=> A9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.135e+12, 's^-1'), n=0.056, Ea=(2127, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "A9 + H <=> N1 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+08, 'cm^3/(mol*s)'),
        n = 1.245,
        Ea = (3405, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "A5 + H <=> N1 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+09, 'cm^3/(mol*s)'),
        n = 1.081,
        Ea = (2011, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

