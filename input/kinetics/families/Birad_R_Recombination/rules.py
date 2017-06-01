#!/usr/bin/env python
# encoding: utf-8

name = "Birad_R_Recombination/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1000,
    label = "Y_rad;Oa",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
)

entry(
    index = 2000,
    label = "Y_rad;Sa",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
)

entry(
    index = 2000,
    label = "Y_rad;N_R_birad",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
)

