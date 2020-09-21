#!/usr/bin/env python
# encoding: utf-8

name = "API_R_Addition_MultipleBond/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 3000,
    label = "R_R;YJ",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

