#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_CSm/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 416,
    label = "CSm;Y_rad",
    group1 = 
"""
1 *1 C 2 {2,D}
2    S 0 {1,D}
""",
    group2 = 
"""
1 *2 R 1
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
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
    index = 417,
    label = "CSm;H_rad",
    group1 = 
"""
1 *1 C 2 {2,D}
2    S 0 {1,D}
""",
    group2 = 
"""
1 *2 H 1
""",
    kinetics = ArrheniusEP(
        A = (118000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Guessed from CO+H_rad""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 418,
    label = "CSm;C_methyl",
    group1 = 
"""
1 *1 C 2 {2,D}
2    S 0 {1,D}
""",
    group2 = 
"""
1 *2 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 2.11,
        alpha = 0,
        E0 = (2.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CAC CBS-QB3 calc (using methyl group), HO Approx""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 419,
    label = "CSm;CH2CH3",
    group1 = 
"""
1 *1 C 2 {2,D}
2    S 0 {1,D}
""",
    group2 = 
"""
1 *2 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    kinetics = ArrheniusEP(
        A = (20100000000.0, 'cm^3/(mol*s)'),
        n = 2.22,
        alpha = 0,
        E0 = (0.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CAC CBS-QB3 calc (using ethyl group), HO approx""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

