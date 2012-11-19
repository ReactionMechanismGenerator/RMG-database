#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_ROR/rules"
shortDesc = u""
longDesc = u"""
561 - 570 Some of the tortional motions in the alkyl part of the 

transition states are treated as free rotations as they are relatively loose TSs.
"""
recommended = True

entry(
    index = 560,
    label = "doublebond;R_OR",
    group1 = "OR{Cd_Cdd, Cdd_Cd, Cd_Cd, Sd_Cd}",
    group2 = "OR{H_OR, R_OH}",
    kinetics = ArrheniusEP(
        A = (100, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 561,
    label = "Cd/H2_Cd/Nd2;H_OCmethyl",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (93.6, 'cm^3/(mol*s)'),
        n = 2.85,
        alpha = 0,
        E0 = (41.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 562,
    label = "Cd/H2_Cd/H/Nd;H_OCmethyl",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (24.8, 'cm^3/(mol*s)'),
        n = 2.93,
        alpha = 0,
        E0 = (43.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 563,
    label = "Cd/unsub_Cd/unsub;H_OCmethyl",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    Cs 0 {2,S} {4,S} {5,S} {6,S}
4    H  0 {3,S}
5    H  0 {3,S}
6    H  0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (47.3, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 564,
    label = "cco_2H;H_OH",
    group1 = 
"""
1 *1 Cd  0 {2,D} {4,S} {5,S}
2 *2 Cdd 0 {1,D} {3,D}
3    Od  0 {2,D}
4    H   0 {1,S}
5    H   0 {1,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (157, 'cm^3/(mol*s)'),
        n = 3.04,
        alpha = 0,
        E0 = (39.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 565,
    label = "cco_HNd;H_OH",
    group1 = 
"""
1 *1 Cd       0 {2,D} {4,S} {5,S}
2 *2 Cdd      0 {1,D} {3,D}
3    Od       0 {2,D}
4    H        0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (51.5, 'cm^3/(mol*s)'),
        n = 3.05,
        alpha = 0,
        E0 = (41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 566,
    label = "cco_Nd2;H_OH",
    group1 = 
"""
1 *1 Cd       0 {2,D} {4,S} {5,S}
2 *2 Cdd      0 {1,D} {3,D}
3    Od       0 {2,D}
4    {Cs,O,S} 0 {1,S}
5    {Cs,O,S} 0 {1,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1450, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (40.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 567,
    label = "Cd/unsub_Cd/unsub;H_OH",
    group1 = 
"""
1 *1 Cd 0 {2,D} {3,S} {4,S}
2 *2 Cd 0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {2,S}
6    H  0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (147, 'cm^3/(mol*s)'),
        n = 2.94,
        alpha = 0,
        E0 = (53.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 568,
    label = "Cd/H/Nd_Cd/H2;H_OH",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    {Cs,O,S} 0 {1,S}
5    H        0 {2,S}
6    H        0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (227, 'cm^3/(mol*s)'),
        n = 2.74,
        alpha = 0,
        E0 = (56.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 569,
    label = "Cd/H2_Cd/H/Nd;H_OH",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    H        0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (65.2, 'cm^3/(mol*s)'),
        n = 2.92,
        alpha = 0,
        E0 = (50.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 570,
    label = "Cd/H2_Cd/Nd2;H_OH",
    group1 = 
"""
1 *1 C        0 {2,D} {3,S} {4,S}
2 *2 C        0 {1,D} {5,S} {6,S}
3    H        0 {1,S}
4    H        0 {1,S}
5    {Cs,O,S} 0 {2,S}
6    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1250, 'cm^3/(mol*s)'),
        n = 2.76,
        alpha = 0,
        E0 = (48.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 701,
    label = "Sd_Cd/unsub;H_OH",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    H  0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (960, 'cm^3/(mol*s)'),
        n = 2.43,
        alpha = 0,
        E0 = (28.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculations by CAC""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 702,
    label = "Sd_Cd/H/Nd;H_OH",
    group1 = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    H        0 {2,S}
4    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (5.96, 'cm^3/(mol*s)'),
        n = 2.77,
        alpha = 0,
        E0 = (20.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CBS-QB3 calculations by CAC, F12 energy""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 703,
    label = "Thiophene2;H_OH",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2 *2 C  0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    Cd 0 {1,S} {7,D}
5    H  0 {2,S}
6    S  0 {2,S} {7,S}
7    C  0 {4,D} {6,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (15, 'cm^3/(mol*s)'),
        n = 3.15,
        alpha = 0,
        E0 = (63.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CBS-QB3 calc w/ 1dhr, by CAC""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 704,
    label = "Thiophene3;H_OH",
    group1 = 
"""
1 *1 C  0 {2,D} {3,S} {4,S}
2 *2 C  0 {1,D} {5,S} {6,S}
3    H  0 {1,S}
4    S  0 {1,S} {7,S}
5    H  0 {2,S}
6    Cd 0 {2,S} {7,D}
7    C  0 {4,S} {6,D}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (51, 'cm^3/(mol*s)'),
        n = 3.11,
        alpha = 0,
        E0 = (63.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CBS-QB3 calc w/ 1dhr, by CAC""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 705,
    label = "Sd_Cd/H/Cb;H_OH",
    group1 = 
"""
1 *1 Sd 0 {2,D}
2 *2 Cd 0 {1,D} {3,S} {4,S}
3    H  0 {2,S}
4    Cb 0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (369, 'cm^3/(mol*s)'),
        n = 2.58,
        alpha = 0,
        E0 = (32.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""CBS-QB3 calc w/ 1dhr, CAC""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 706,
    label = "Sd_Cd/Nd2;H_OH",
    group1 = 
"""
1 *1 Sd       0 {2,D}
2 *2 Cd       0 {1,D} {3,S} {4,S}
3    {Cs,O,S} 0 {2,S}
4    {Cs,O,S} 0 {2,S}
""",
    group2 = 
"""
1 *3 H  0 {2,S}
2 *4 Os 0 {1,S} {3,S}
3    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (0.909, 'cm^3/(mol*s)'),
        n = 3.14,
        alpha = 0,
        E0 = (36.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""CBS-QB3 HO""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

