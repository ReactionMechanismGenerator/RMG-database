#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_cyclization/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "XSYJ;YJ;C;S",
    kinetics = ArrheniusEP(
        A = (1e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

