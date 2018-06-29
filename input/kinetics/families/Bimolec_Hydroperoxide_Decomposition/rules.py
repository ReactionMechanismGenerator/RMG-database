#!/usr/bin/env python
# encoding: utf-8

name = "Bimolec_Hydroperoxide_Decomposition/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "ROOH;ROOH",
    kinetics = ArrheniusEP(
        A = (1.096e5, 'm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (96.1, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc =
u"""

""",
)
