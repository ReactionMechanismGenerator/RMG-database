#!/usr/bin/env python
# encoding: utf-8

name = "XY_Addition_DoubleBond/rules"
shortDesc = u""
longDesc = u"""
"""
entry(
    index = 560,
    label = "doublebond;X_Y",
    kinetics = ArrheniusEP(
        A = (100, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

