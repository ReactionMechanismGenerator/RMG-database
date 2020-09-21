#!/usr/bin/env python
# encoding: utf-8

name = "API_1,4_Cyclic_birad_scission/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "RJJ",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""AG Vandeputte estimate (should be fast)""",
)

