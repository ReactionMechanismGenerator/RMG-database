#!/usr/bin/env python
# encoding: utf-8

name = "Tert_Peroxyl_Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "R2CHOO_rad;R2CHOO_rad",
    kinetics = ArrheniusEP(
        A = (1.48e9, 'm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (35.6, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc =
u"""

""",
)
