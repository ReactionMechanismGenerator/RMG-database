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
    label = "C3H3 + CH2CO <=> C5H5O_1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.94e+03, 'cm^3/(mol*s)'), n=2.305, Ea=(5213, 'cal/mol'), T0=(1, 'K')),
    longDesc = u"""Use the rate from the average value from master branch 04/30/2017""",
)

entry(
    index = 4,
    label = "C3H3 + CH2CO <=> C5H5O_2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.08e+0, 'cm^3/(mol*s)'), n=3.05, Ea=(13100, 'cal/mol'), T0=(1, 'K')),
    longDesc = u"""Use the rate from the average value from master branch 05/03/2017""",
)

entry(
    index = 5,
    label = "CH3 + CH2CO <=> C3H5O_1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.05855e+04, 'cm^3/(mol*s)'), n=2.41, Ea=(8055, 'cal/mol'), T0=(1, 'K')),
    longDesc = u"""Use the rate from the average value from master branch 05/03/2017""",
)

entry(
    index = 6,
    label = "C3H5O_2 <=> CH3 + CH2CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+14, 's^-1'), n=0, Ea=(31000, 'cal/mol'), T0=(1, 'K')),
    longDesc = u"""Use the rate from Dooley/methylformate/288""",
)



