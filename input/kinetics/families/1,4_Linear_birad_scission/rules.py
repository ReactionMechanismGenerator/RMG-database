#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Linear_birad_scission/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "RJJ",
    kinetics = ArrheniusEP(
        A = (5000000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""AG Vandeputte estimate (should be fast)""",
    longDesc = 
u"""

""",
)

