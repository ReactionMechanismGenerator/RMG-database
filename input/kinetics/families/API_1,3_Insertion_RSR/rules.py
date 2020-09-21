#!/usr/bin/env python
# encoding: utf-8

name = "API_1,3_Insertion_RSR/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 100,
    label = "doublebond;R_SR",
    kinetics = ArrheniusEP(
        A = (100, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

