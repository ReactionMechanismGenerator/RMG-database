#!/usr/bin/env python
# encoding: utf-8

name = "C6H4C2H_C2H2_highP"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C6H4C2H + C2H2 <=> A12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(13400, 'cm^3/(mol*s)'), n=2.499, Ea=(1283, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "A12 <=> C10H7-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.948e+11, 's^-1'), n=0.045, Ea=(5395, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "C10H7-1 + H <=> C10H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.87e+13, 'cm^3/(mol*s)'), n=0.13, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

