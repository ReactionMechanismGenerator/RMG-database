#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_isomerization/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "XSYJ;C;YJ",
    kinetics = ArrheniusEP(
        A = (1e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""A. G. Vandeputte""",
)

