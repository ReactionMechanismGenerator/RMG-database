#!/usr/bin/env python
# encoding: utf-8

name = "API_Fake_HOCK_rearrangement/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "CC-OOH",
    kinetics = ArrheniusEP(
        A = (3e+6, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)
