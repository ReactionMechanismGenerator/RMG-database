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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
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
    longDesc = 
u"""

""",
)

entry(
    index = 701,
    label = "Sd_Cd/unsub;H_OH",
    kinetics = ArrheniusEP(
        A = (960, 'cm^3/(mol*s)'),
        n = 2.43,
        alpha = 0,
        E0 = (28.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 calculations by CAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 702,
    label = "Sd_Cd/H/Nd;H_OH",
    kinetics = ArrheniusEP(
        A = (5.96, 'cm^3/(mol*s)'),
        n = 2.77,
        alpha = 0,
        E0 = (20.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 calculations by CAC, F12 energy""",
    longDesc = 
u"""

""",
)

entry(
    index = 703,
    label = "Thiophene2;H_OH",
    kinetics = ArrheniusEP(
        A = (15, 'cm^3/(mol*s)'),
        n = 3.15,
        alpha = 0,
        E0 = (63.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 calc w/ 1dhr, by CAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 704,
    label = "Thiophene3;H_OH",
    kinetics = ArrheniusEP(
        A = (51, 'cm^3/(mol*s)'),
        n = 3.11,
        alpha = 0,
        E0 = (63.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 calc w/ 1dhr, by CAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 705,
    label = "Sd_Cd/H/Cb;H_OH",
    kinetics = ArrheniusEP(
        A = (369, 'cm^3/(mol*s)'),
        n = 2.58,
        alpha = 0,
        E0 = (32.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 calc w/ 1dhr, CAC""",
    longDesc = 
u"""

""",
)

entry(
    index = 706,
    label = "Sd_Cd/Nd2;H_OH",
    kinetics = ArrheniusEP(
        A = (0.909, 'cm^3/(mol*s)'),
        n = 3.14,
        alpha = 0,
        E0 = (36.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""CBS-QB3 HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 707,
    label = "Cd/H/Nd_Cd/H2;H_OH",
    kinetics = ArrheniusEP(
        A = (61040000.0, 'cm^3/(mol*s)'),
        n = 1.287,
        alpha = 0,
        E0 = (60.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 708,
    label = "Cd/Nd2_Cd/H2;H_OH",
    kinetics = ArrheniusEP(
        A = (51810000.0, 'cm^3/(mol*s)'),
        n = 1.302,
        alpha = 0,
        E0 = (62.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
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
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 710,
    label = "Cd/H/De_Cd/H2;H_OH",
    kinetics = ArrheniusEP(
        A = (61040000.0, 'cm^3/(mol*s)'),
        n = 1.287,
        alpha = 0,
        E0 = (60.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Same as rule 707""",
    longDesc = 
u"""

""",
)

