#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "ROO_rad;ROO_rad",
    kinetics = ArrheniusEP(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        alpha = 0,
        E0 = (1860, 'cal/mol'),
        Tmin=(300, 'K'),
        Tmax=(1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc =
u"""

""",
)
