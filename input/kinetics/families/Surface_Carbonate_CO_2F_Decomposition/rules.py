#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Carbonate_CO_2F_Decomposition/rules"
shortDesc = u""
longDesc = u"""
"""

entry(
    index = 1,
    label = "CarbonateRing;SurfaceSite1;SurfaceSite2",
    kinetics = StickingCoefficientBEP(
            A = 0.2,
            n = 0,
            alpha = 0,
            E0 = (0, 'kcal/mol'),
            Tmin = (200, 'K'),
            Tmax = (3000, 'K'),
        ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u""""""
)
