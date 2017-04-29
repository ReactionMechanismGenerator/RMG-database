#!/usr/bin/env python
# encoding: utf-8

name = "Ketene_related"
shortDesc = u"Correct rates for ketene formation or consumption"
longDesc = u"""
"""

entry(
    index = 1,
    label = "H + CH2CO <=> CH3 + CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(3428, 'cal/mol'), T0=(1, 'K')),
)
