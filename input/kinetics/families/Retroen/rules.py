#!/usr/bin/env python
# encoding: utf-8

name = "Retroen/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "alkylaromatic",
    kinetics = ArrheniusEP(
        A = (8.50e11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (54.40, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Burkle-Virtzthum DOI: 10.1021/ie030086f""",
)
