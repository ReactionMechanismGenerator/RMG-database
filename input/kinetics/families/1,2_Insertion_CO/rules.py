#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 553,
    label = "COS;RR'",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 2,
        alpha = 0,
        E0 = (80, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.
""",
)

