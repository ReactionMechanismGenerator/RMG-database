#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 1,
    label = "R_ROR",
    group1 = 
"""
1 *1 R 0 {2,D}
2 *2 R 0 {1,D} {3,S}
3 *3 O 0 {2,S} {4,S}
4 *4 R 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (100000, 's^-1'),
        n = 2,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""A. G. Vandeputte, general rate""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "Cds/H2_Cds/CsOH",
    group1 = 
"""
1 *1 C  0 {2,D} {5,S} {6,S}
2 *2 C  0 {1,D} {3,S} {7,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    H  0 {1,S}
6    H  0 {1,S}
7    Cs 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (205000, 's^-1'),
        n = 2.37,
        alpha = 0,
        E0 = (48.8, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, CBS-QB3, HO""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "Cds/H2_Cds/HOH",
    group1 = 
"""
1 *1 C 0 {2,D} {5,S} {6,S}
2 *2 C 0 {1,D} {3,S} {7,S}
3 *3 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (7040, 's^-1'),
        n = 2.66,
        alpha = 0,
        E0 = (48.8, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, BMK/cbsb7, HO""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "S_Cds/HOH",
    group1 = 
"""
1 *1 S 0 {2,D}
2 *2 C 0 {1,D} {3,S} {5,S}
3 *3 O 0 {2,S} {4,S}
4 *4 H 0 {3,S}
5    H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (52, 's^-1'),
        n = 3.26,
        alpha = 0,
        E0 = (19.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "S_Cds/CH3OH",
    group1 = 
"""
1 *1 S  0 {2,D}
2 *2 C  0 {1,D} {3,S} {5,S}
3 *3 O  0 {2,S} {4,S}
4 *4 H  0 {3,S}
5    Cs 0 {2,S} {6,S} {7,S} {8,S}
6    H  0 {5,S}
7    H  0 {5,S}
8    H  0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (104, 's^-1'),
        n = 3.21,
        alpha = 0,
        E0 = (18.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 6,
    label = "S_Cds/CH2CH3OH",
    group1 = 
"""
1  *1 S  0 {2,D}
2  *2 C  0 {1,D} {3,S} {5,S}
3  *3 O  0 {2,S} {4,S}
4  *4 H  0 {3,S}
5     Cs 0 {2,S} {6,S} {7,S} {8,S}
6     Cs 0 {5,S} {9,S} {10,S} {11,S}
7     H  0 {5,S}
8     H  0 {5,S}
9     H  0 {6,S}
10    H  0 {6,S}
11    H  0 {6,S}
""",
    kinetics = ArrheniusEP(
        A = (87.5, 's^-1'),
        n = 3.23,
        alpha = 0,
        E0 = (18.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

