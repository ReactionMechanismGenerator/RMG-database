#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_RSR/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 100,
    label = "doublebond;R_SR",
    kinetics = ArrheniusEP(
        A = (100, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 101,
    label = "Od_Cd/unsub;H_SH",
    kinetics = ArrheniusEP(
        A = (12.2, 'cm^3/(mol*s)'),
        n = 3.27,
        alpha = 0,
        E0 = (37.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations from CAC, energy from F12a""",
)

entry(
    index = 102,
    label = "Od_Cd/H/Nd;H_SH",
    kinetics = ArrheniusEP(
        A = (306, 'cm^3/(mol*s)'),
        n = 2.96,
        alpha = 0,
        E0 = (36.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations from CAC, energy from F12a""",
)

entry(
    index = 107,
    label = "Od_Cd/H/Cb;H_SH",
    kinetics = ArrheniusEP(
        A = (96.5, 'cm^3/(mol*s)'),
        n = 2.84,
        alpha = 0,
        E0 = (34.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 by CAC""",
)

entry(
    index = 108,
    label = "Cd/unsub_Cd/unsub;H_SH",
    kinetics = ArrheniusEP(
        A = (0.444, 'cm^3/(mol*s)'),
        n = 3.55,
        alpha = 0,
        E0 = (44.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
)

entry(
    index = 109,
    label = "Cd/H2_Cd/H/Nd;H_SH",
    kinetics = ArrheniusEP(
        A = (47.1, 'cm^3/(mol*s)'),
        n = 3.02,
        alpha = 0,
        E0 = (42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
)

entry(
    index = 110,
    label = "Cd/H2_Cd/Cs2;H_SH",
    kinetics = ArrheniusEP(
        A = (46.7, 'cm^3/(mol*s)'),
        n = 3.02,
        alpha = 0,
        E0 = (42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
)

entry(
    index = 111,
    label = "Cd/unsub_Cd/unsub;H_SCs(HHH)",
    kinetics = ArrheniusEP(
        A = (0.36, 'cm^3/(mol*s)'),
        n = 3.64,
        alpha = 0,
        E0 = (41.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
)

entry(
    index = 112,
    label = "Cd/H2_Cd/H/Nd;H_SCs(HHH)",
    kinetics = ArrheniusEP(
        A = (2.5, 'cm^3/(mol*s)'),
        n = 3.33,
        alpha = 0,
        E0 = (40.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
)

entry(
    index = 113,
    label = "Cd/H2_Cd/Cs2;H_SCs(HHH)",
    kinetics = ArrheniusEP(
        A = (34, 'cm^3/(mol*s)'),
        n = 3.07,
        alpha = 0,
        E0 = (39.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
)

entry(
    index = 113,
    label = "Cd/H2_Cd/Cs2;H_SCs(CsCsCs)",
    kinetics = ArrheniusEP(
        A = (1.24, 'cm^3/(mol*s)'),
        n = 3.33,
        alpha = 0,
        E0 = (40.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
)

entry(
    index = 114,
    label = "Cd/unsub_Cd/unsub;H_SCs(CsHH)",
    kinetics = ArrheniusEP(
        A = (0.261, 'cm^3/(mol*s)'),
        n = 3.67,
        alpha = 0,
        E0 = (41.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
)

entry(
    index = 115,
    label = "Cd/H/Nd_Cd/H/Os;H_SH",
    kinetics = ArrheniusEP(
        A = (21700, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 by CAC, 1dhr""",
)

entry(
    index = 116,
    label = "Od_Cd/CsCs;H_SH",
    kinetics = ArrheniusEP(
        A = (1.65, 'cm^3/(mol*s)'),
        n = 3.45,
        alpha = 0,
        E0 = (37.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by CAC with 1d-hr, F12a energies""",
)

entry(
    index = 117,
    label = "Od_Cd/CsOs;H_SH",
    kinetics = ArrheniusEP(
        A = (0.313, 'cm^3/(mol*s)'),
        n = 3.56,
        alpha = 0,
        E0 = (38.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by CAC with 1d-hr, F12a energies""",
)

entry(
    index = 118,
    label = "Od_Cdd;H_SH",
    kinetics = ArrheniusEP(
        A = (6.32e-10, 'cm^3/(mol*s)'),
        n = 6.38,
        alpha = 0,
        E0 = (47.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 by CAC with 1d-hr, F12a energies""",
)

entry(
    index = 119,
    label = "Od_Cd/H/Cd;H_SH",
    kinetics = ArrheniusEP(
        A = (804, 'cm^3/(mol*s)'),
        n = 2.64,
        alpha = 0,
        E0 = (36.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr by CAC, F12a energy""",
)

