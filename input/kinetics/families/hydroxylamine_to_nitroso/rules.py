#!/usr/bin/env python
# encoding: utf-8

name = "hydroxylamine_to_nitroso/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "hydroxylamine",
    kinetics = ArrheniusEP(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

