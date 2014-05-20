#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    label        = "R_ROR",
    group1 = 
"""
1 *1 R U0 {2,D}
2 *2 R U0 {1,D} {3,S}
3 *3 O U0 {2,S} {4,S}
4 *4 R U0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (100000, 's^-1'),
        n = 2,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""A. G. Vandeputte, general rate""",
    longDesc = 
u"""

""",
)

entry(
    index        = 2,
    label        = "Cds/H2_Cds/CsOH",
    group1 = 
"""
1 *1 C  U0 {2,D} {5,S} {6,S}
2 *2 C  U0 {1,D} {3,S} {7,S}
3 *3 O  U0 {2,S} {4,S}
4 *4 H  U0 {3,S}
5    H  U0 {1,S}
6    H  U0 {1,S}
7    Cs U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (205000, 's^-1'),
        n = 2.37,
        alpha = 0,
        E0 = (48.8, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, CBS-QB3, HO""",
    longDesc = 
u"""

""",
)

entry(
    index        = 3,
    label        = "Cds/H2_Cds/HOH",
    group1 = 
"""
1 *1 C U0 {2,D} {5,S} {6,S}
2 *2 C U0 {1,D} {3,S} {7,S}
3 *3 O U0 {2,S} {4,S}
4 *4 H U0 {3,S}
5    H U0 {1,S}
6    H U0 {1,S}
7    H U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (7040, 's^-1'),
        n = 2.66,
        alpha = 0,
        E0 = (48.8, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, BMK/cbsb7, HO""",
    longDesc = 
u"""

""",
)

entry(
    index        = 4,
    label        = "S_Cds/HOH",
    group1 = 
"""
1 *1 S U0 {2,D}
2 *2 C U0 {1,D} {3,S} {5,S}
3 *3 O U0 {2,S} {4,S}
4 *4 H U0 {3,S}
5    H U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (52, 's^-1'),
        n = 3.26,
        alpha = 0,
        E0 = (19.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""

""",
)

entry(
    index        = 5,
    label        = "S_Cds/CH3OH",
    group1 = 
"""
1 *1 S  U0 {2,D}
2 *2 C  U0 {1,D} {3,S} {5,S}
3 *3 O  U0 {2,S} {4,S}
4 *4 H  U0 {3,S}
5    Cs U0 {2,S} {6,S} {7,S} {8,S}
6    H  U0 {5,S}
7    H  U0 {5,S}
8    H  U0 {5,S}
""",
    kinetics = ArrheniusEP(
        A = (104, 's^-1'),
        n = 3.21,
        alpha = 0,
        E0 = (18.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""

""",
)

entry(
    index        = 6,
    label        = "S_Cds/CH2CH3OH",
    group1 = 
"""
1  *1 S  U0 {2,D}
2  *2 C  U0 {1,D} {3,S} {5,S}
3  *3 O  U0 {2,S} {4,S}
4  *4 H  U0 {3,S}
5     Cs U0 {2,S} {6,S} {7,S} {8,S}
6     Cs U0 {5,S} {9,S} {10,S} {11,S}
7     H  U0 {5,S}
8     H  U0 {5,S}
9     H  U0 {6,S}
10    H  U0 {6,S}
11    H  U0 {6,S}
""",
    kinetics = ArrheniusEP(
        A = (87.5, 's^-1'),
        n = 3.23,
        alpha = 0,
        E0 = (18.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""

""",
)

