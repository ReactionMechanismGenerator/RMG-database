#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 561,
    label = "carbene;ethene",
    kinetics = ArrheniusEP(
        A = (6.63e+11, 'cm^3/(mol*s)'),
        n = 0.0073,
        alpha = 0,
        E0 = (-1.045, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino""",
)

entry(
    index = 562,
    label = "carbene;Cd_pri",
    kinetics = ArrheniusEP(
        A = (3.5e+10, 'cm^3/(mol*s)'),
        n = 0.465,
        alpha = 0,
        E0 = (-1.742, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino, [carbene,propadiene] as model reaction""",
)

entry(
    index = 563,
    label = "carbene;acetylene",
    kinetics = ArrheniusEP(
        A = (1.65e+07, 'cm^3/(mol*s)'),
        n = 1.475,
        alpha = 0,
        E0 = (-1.651, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino""",
)

entry(
    index = 564,
    label = "carbene;Ct_H",
    kinetics = ArrheniusEP(
        A = (1.02e+08, 'cm^3/(mol*s)'),
        n = 1.249,
        alpha = 0,
        E0 = (-2.214, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene, propyne] as model reaction""",
)

entry(
    index = 565,
    label = "carbene;C_pri/Cd",
    kinetics = ArrheniusEP(
        A = (6.62e+12, 'cm^3/(mol*s)'),
        n = 0.324,
        alpha = 0,
        E0 = (-0.935, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene,propene]""",
)

entry(
    index = 566,
    label = "carbene;C_pri/Ct",
    kinetics = ArrheniusEP(
        A = (2.47e+09, 'cm^3/(mol*s)'),
        n = 0.797,
        alpha = 0,
        E0 = (-1.174, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene,2-butyne]""",
)

entry(
    index = 567,
    label = "carbene;Cd/H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.07e+13, 'cm^3/(mol*s)'),
        n = -0.274,
        alpha = 0,
        E0 = (-0.686, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene,propene]""",
)

entry(
    index = 568,
    label = "carbene;Cd/H/OneDe",
    kinetics = ArrheniusEP(
        A = (1.84e+10, 'cm^3/(mol*s)'),
        n = 0.498,
        alpha = 0,
        E0 = (-1.758, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (200, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene,1,3-butadiene]""",
)

