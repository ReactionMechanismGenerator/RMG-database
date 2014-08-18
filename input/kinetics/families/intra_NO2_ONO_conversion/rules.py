#!/usr/bin/env python
# encoding: utf-8

name = "intra_NO2_ONO_conversion/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "RNO2",
    kinetics = ArrheniusEP(
        A = (2.76e+14, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (67.0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"",
    longDesc = 
u"""

""",
)