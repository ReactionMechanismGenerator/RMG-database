#!/usr/bin/env python
# encoding: utf-8

name = "phenyl_diacetylene_benzofulvenyl_effective"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "i2_trans <=> i3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.992e+11, 's^-1'), n=0.670, Ea=(58.336, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "i2_trans <=> i4",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.992e+11, 's^-1'), n=0.670, Ea=(58.336, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

