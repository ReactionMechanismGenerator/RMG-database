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
    longDesc = u"""Use the rate from GRI Mech 3.0""",
)

entry(
    index = 2,
    label = "CH2CO + H <=> CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+08, 'cm^3/(mol*s)'), n=1.61, Ea=(2627, 'cal/mol'), T0=(1, 'K')),
    longDesc = u"""Use the rate from Glarborg library""",
)

entry(
    index = 3,
    label = "C3H3 + CH2CO <=> C5H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.94e+03, 'cm^3/(mol*s)'), n=2.305, Ea=(5213, 'cal/mol'), T0=(1, 'K')),
    longDesc = u"""Use the rate from the average value from master branch 04/30/2017""",
)

