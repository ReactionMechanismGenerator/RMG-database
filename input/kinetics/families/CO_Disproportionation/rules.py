#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 485,
    label = "Y_rad_birad_trirad_quadrad;HCO_HCS",
    kinetics = ArrheniusEP(
        A = (3e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

