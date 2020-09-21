#!/usr/bin/env python
# encoding: utf-8

name = "API_Birad_recombination/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 480,
    label = "Rn;Y_rad_out;Ypri_rad_out",
    kinetics = ArrheniusEP(
        A = (5e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (30, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

