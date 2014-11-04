#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Disproportionation/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "R3;Y_rad;XH_Rrad",
    kinetics = ArrheniusEP(
        A = (1.62e+11, 's^-1'),
        n = -0.305,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
)

entry(
    index = 2,
    label = "R4;Y_rad;XH_Rrad",
    kinetics = ArrheniusEP(
        A = (7.76e+08, 's^-1'),
        n = 0.311,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
)

entry(
    index = 3,
    label = "R5;Y_rad;XH_Rrad",
    kinetics = ArrheniusEP(
        A = (3.21e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
)

entry(
    index = 4,
    label = "R6;Y_rad;XH_Rrad",
    kinetics = ArrheniusEP(
        A = (3.21e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
)

entry(
    index = 5,
    label = "R7;Y_rad;XH_Rrad",
    kinetics = ArrheniusEP(
        A = (3.21e+09, 's^-1'),
        n = 0.137,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Herbinet et al.(2006) reference Ea and Warth et al.(1998) prefactor with deltan_int=-1""",
)

