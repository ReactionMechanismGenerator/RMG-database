#!/usr/bin/env python
# encoding: utf-8

name = "methanoate_hydrolysis/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "BNX + H2O <=> P1 + P2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.7e+11, 'cm^3/(mol*s)'), n=0, Ea=(25, 'kcal/mol')),
    rank = 5,
    shortDesc = u"""est.""",
    longDesc =
u"""

""",
)
