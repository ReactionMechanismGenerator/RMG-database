#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_ROR/rules"
shortDesc = u""
longDesc = u"""
561 - 570 Some of the tortional motions in the alkyl part of the 

transition states are treated as free rotations as they are relatively loose TSs.
"""
entry(
    index = 560,
    label = "doublebond;R_OR",
    kinetics = ArrheniusEP(
        A = (100, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 561,
    label = "Cd/H2_Cd/Nd2;H_OCmethyl",
    kinetics = ArrheniusEP(
        A = (93.6, 'cm^3/(mol*s)'),
        n = 2.85,
        alpha = 0,
        E0 = (41.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 562,
    label = "Cd/H2_Cd/H/Nd;H_OCmethyl",
    kinetics = ArrheniusEP(
        A = (24.8, 'cm^3/(mol*s)'),
        n = 2.93,
        alpha = 0,
        E0 = (43.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 563,
    label = "Cd/unsub_Cd/unsub;H_OCmethyl",
    kinetics = ArrheniusEP(
        A = (47.3, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 564,
    label = "cco_2H;H_OH",
    kinetics = ArrheniusEP(
        A = (157, 'cm^3/(mol*s)'),
        n = 3.04,
        alpha = 0,
        E0 = (39.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 565,
    label = "cco_HNd;H_OH",
    kinetics = ArrheniusEP(
        A = (51.5, 'cm^3/(mol*s)'),
        n = 3.05,
        alpha = 0,
        E0 = (41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 566,
    label = "cco_Nd2;H_OH",
    kinetics = ArrheniusEP(
        A = (1450, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (40.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 567,
    label = "Cd/unsub_Cd/unsub;H_OH",
    kinetics = ArrheniusEP(
        A = (147, 'cm^3/(mol*s)'),
        n = 2.94,
        alpha = 0,
        E0 = (53.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 568,
    label = "Cd/H/Nd_Cd/H2;H_OH",
    kinetics = ArrheniusEP(
        A = (227, 'cm^3/(mol*s)'),
        n = 2.74,
        alpha = 0,
        E0 = (56.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 569,
    label = "Cd/H2_Cd/H/Nd;H_OH",
    kinetics = ArrheniusEP(
        A = (65.2, 'cm^3/(mol*s)'),
        n = 2.92,
        alpha = 0,
        E0 = (50.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 570,
    label = "Cd/H2_Cd/Nd2;H_OH",
    kinetics = ArrheniusEP(
        A = (1250, 'cm^3/(mol*s)'),
        n = 2.76,
        alpha = 0,
        E0 = (48.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 701,
    label = "Sd_Cd/unsub;H_OH",
    kinetics = ArrheniusEP(
        A = (0.243, 'cm^3/(mol*s)'),
        n = 3.55,
        alpha = 0,
        E0 = (24.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations by CAC, F12a energy""",
)

entry(
    index = 702,
    label = "Sd_Cd/H/Nd;H_OH",
    kinetics = ArrheniusEP(
        A = (0.00266, 'cm^3/(mol*s)'),
        n = 3.95,
        alpha = 0,
        E0 = (24.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations by CAC, F12a energy""",
)

entry(
    index = 703,
    label = "Thiophene2;H_OH",
    kinetics = ArrheniusEP(
        A = (6.02, 'cm^3/(mol*s)'),
        n = 3.27,
        alpha = 0,
        E0 = (63.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
)

entry(
    index = 704,
    label = "Thiophene3;H_OH",
    kinetics = ArrheniusEP(
        A = (20.8, 'cm^3/(mol*s)'),
        n = 3.23,
        alpha = 0,
        E0 = (61.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
)

entry(
    index = 705,
    label = "Sd_Cd/H/Cb;H_OH",
    kinetics = ArrheniusEP(
        A = (0.0164, 'cm^3/(mol*s)'),
        n = 3.89,
        alpha = 0,
        E0 = (29.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC""",
)

entry(
    index = 706,
    label = "Sd_Cd/CsCs;H_OH",
    kinetics = ArrheniusEP(
        A = (5.06e-05, 'cm^3/(mol*s)'),
        n = 4.54,
        alpha = 0,
        E0 = (24.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
)

entry(
    index = 707,
    label = "Cd/H/Nd_Cd/H2;H_OH",
    kinetics = ArrheniusEP(
        A = (6.104e+07, 'cm^3/(mol*s)'),
        n = 1.287,
        alpha = 0,
        E0 = (60.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
)

entry(
    index = 708,
    label = "Cd/Nd2_Cd/H2;H_OH",
    kinetics = ArrheniusEP(
        A = (5.181e+07, 'cm^3/(mol*s)'),
        n = 1.302,
        alpha = 0,
        E0 = (62.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
)

entry(
    index = 709,
    label = "Cd/H2_Cd/Nd2;H_OH",
    kinetics = ArrheniusEP(
        A = (301300, 'cm^3/(mol*s)'),
        n = 1.82,
        alpha = 0,
        E0 = (51.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
)

entry(
    index = 710,
    label = "Cd/H/De_Cd/H2;H_OH",
    kinetics = ArrheniusEP(
        A = (2.74e-05, 'cm^3/(mol*s)'),
        n = 4.73,
        alpha = 0,
        E0 = (52.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, CBS-QB3 + HO""",
    longDesc = 
    """
    Updated by AG Vandeputte, CBSQB3 + HO,
    calculated for butadiene + H2O -> 2-butenol
    """,
)

entry(
    index = 712,
    label = "doublebond;R_OH",
    kinetics = ArrheniusEP(
        A = (1e-05, 'cm^3/(mol*s)'),
        n = 4,
        alpha = 0,
        E0 = (80, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 713,
    label = "Cd/unsub_Cd/unsub;CH3OH",
    kinetics = ArrheniusEP(
        A = (1.79e-05, 'cm^3/(mol*s)'),
        n = 3.97,
        alpha = 0,
        E0 = (78.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, CBS-QB3 + HO""",
    longDesc = 
    """
AG Vandeputte, calculated the rate coefficient for methanol + ethene -> propanol
    """,
)

entry(
    index = 717,
    label = "Sd_Cd/CsOs;H_OH",
    kinetics = ArrheniusEP(
        A = (1.04e-05, 'cm^3/(mol*s)'),
        n = 4.64,
        alpha = 0,
        E0 = (32.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
)

entry(
    index = 718,
    label = "Sd_Cdd/Od;H_OH",
    kinetics = ArrheniusEP(
        A = (4.39e-07, 'cm^3/(mol*s)'),
        n = 5.4,
        alpha = 0,
        E0 = (45.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
)

entry(
    index = 719,
    label = "Sd_Cd/H/Cd;H_OH",
    kinetics = ArrheniusEP(
        A = (0.0598, 'cm^3/(mol*s)'),
        n = 3.75,
        alpha = 0,
        E0 = (29.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 1d-hr by CAC, F12a energy""",
)

