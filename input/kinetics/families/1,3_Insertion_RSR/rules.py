#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_RSR/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 100,
    label        = "doublebond;R_SR",
    group1 = "OR{Cd_Cdd, Cdd_Cd, Cd_Cd, Od_Cd, Sd_Cd}",
    group2 = "OR{H_SR, R_SH}",
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
    longDesc = 
u"""

""",
)

entry(
    index        = 101,
    label        = "Od_Cd/unsub;H_SH",
    group1 = 
"""
1 *1 Od U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    H  U0 {2,S}
4    H  U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (50.2, 'cm^3/(mol*s)'),
        n = 3.01,
        alpha = 0,
        E0 = (38.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations from CAC""",
    longDesc = 
u"""

""",
)

entry(
    index        = 102,
    label        = "Od_Cd/H/Nd;H_SH",
    group1 = 
"""
1 *1 Od       U0 {2,D}
2 *2 Cd       U0 {1,D} {3,S} {4,S}
3    H        U0 {2,S}
4    {Cs,O,S} U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (61.3, 'cm^3/(mol*s)'),
        n = 2.77,
        alpha = 0,
        E0 = (36.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations from CAC, energy from F12""",
    longDesc = 
u"""

""",
)

entry(
    index        = 103,
    label        = "Cd/unsub_Cd/unsub;H_SH",
    group1 = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (34.8, 'cm^3/(mol*s)'),
        n = 3.35,
        alpha = 0,
        E0 = (49.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by CAC""",
    longDesc = 
u"""

""",
)

entry(
    index        = 104,
    label        = "Cd/H2_Cd/H/Nd;H_SH",
    group1 = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    H        U0 {1,S}
5    H        U0 {2,S}
6    {Cs,O,S} U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (5.79, 'cm^3/(mol*s)'),
        n = 3.42,
        alpha = 0,
        E0 = (51.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by CAC""",
    longDesc = 
u"""

""",
)

entry(
    index        = 105,
    label        = "Cd/H/Nd_Cd/H2;H_SH",
    group1 = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    H        U0 {2,S}
6    H        U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (25.1, 'cm^3/(mol*s)'),
        n = 3.02,
        alpha = 0,
        E0 = (47.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3 by CAC""",
    longDesc = 
u"""

""",
)

entry(
    index        = 106,
    label        = "Cd/H/Nd_Cd/H2;H_SCs",
    group1 = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    H        U0 {2,S}
6    H        U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    Cs U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.78, 'cm^3/(mol*s)'),
        n = 3.2,
        alpha = 0,
        E0 = (43.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by CAC""",
    longDesc = 
u"""

""",
)

entry(
    index        = 107,
    label        = "Od_Cd/H/Cb;H_SH",
    group1 = 
"""
1 *1 Od U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    H  U0 {2,S}
4    Cb U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (108, 'cm^3/(mol*s)'),
        n = 2.74,
        alpha = 0,
        E0 = (35.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by CAC""",
    longDesc = 
u"""

""",
)

entry(
    index        = 108,
    label        = "Cd/unsub_Cd/unsub;H_SH",
    group1 = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
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
    longDesc = 
u"""

""",
)

entry(
    index        = 109,
    label        = "Cd/H2_Cd/H/Nd;H_SH",
    group1 = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    H        U0 {1,S}
5    H        U0 {2,S}
6    {Cs,O,S} U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
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
    longDesc = 
u"""

""",
)

entry(
    index        = 110,
    label        = "Cd/H2_Cd/Cs2;H_SH",
    group1 = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2 *2 C  U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
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
    longDesc = 
u"""

""",
)

entry(
    index        = 111,
    label        = "Cd/unsub_Cd/unsub;H_SCs(HHH)",
    group1 = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    Cs U0 {2,S} {4,S} {5,S} {6,S}
4    H  U0 {3,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
""",
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
    longDesc = 
u"""

""",
)

entry(
    index        = 112,
    label        = "Cd/H2_Cd/H/Nd;H_SCs(HHH)",
    group1 = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    H        U0 {1,S}
5    H        U0 {2,S}
6    {Cs,O,S} U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    Cs U0 {2,S} {4,S} {5,S} {6,S}
4    H  U0 {3,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
""",
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
    longDesc = 
u"""

""",
)

entry(
    index        = 113,
    label        = "Cd/H2_Cd/Cs2;H_SCs(HHH)",
    group1 = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2 *2 C  U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    Cs U0 {2,S} {4,S} {5,S} {6,S}
4    H  U0 {3,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
""",
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
    longDesc = 
u"""

""",
)

entry(
    index        = 113,
    label        = "Cd/H2_Cd/Cs2;H_SCs(CsCsCs)",
    group1 = 
"""
1 *1 C  U0 {2,D} {3,S} {4,S}
2 *2 C  U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {2,S}
6    Cs U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    Cs U0 {2,S} {4,S} {5,S} {6,S}
4    Cs U0 {3,S}
5    Cs U0 {3,S}
6    Cs U0 {3,S}
""",
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
    longDesc = 
u"""

""",
)

entry(
    index        = 114,
    label        = "Cd/unsub_Cd/unsub;H_SCs(CsHH)",
    group1 = 
"""
1 *1 Cd U0 {2,D} {3,S} {4,S}
2 *2 Cd U0 {1,D} {5,S} {6,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {2,S}
6    H  U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    Cs U0 {2,S} {4,S} {5,S} {6,S}
4    Cs U0 {3,S}
5    H  U0 {3,S}
6    H  U0 {3,S}
""",
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
    longDesc = 
u"""

""",
)

entry(
    index        = 114,
    label        = "Od_Cd/H/Os;H_SH",
    group1 = 
"""
1 *1 Od U0 {2,D}
2 *2 Cd U0 {1,D} {3,S} {4,S}
3    H  U0 {2,S}
4    O  U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (7.78, 'cm^3/(mol*s)'),
        n = 2.97,
        alpha = 0,
        E0 = (39.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""CBS-QB3 by CAC HO""",
    longDesc = 
u"""

""",
)

entry(
    index        = 115,
    label        = "Cd/H/Nd_Cd/H/Os;H_SH",
    group1 = 
"""
1 *1 C        U0 {2,D} {3,S} {4,S}
2 *2 C        U0 {1,D} {5,S} {6,S}
3    H        U0 {1,S}
4    {Cs,O,S} U0 {1,S}
5    H        U0 {2,S}
6    O        U0 {2,S}
""",
    group2 = 
"""
1 *3 H  U0 {2,S}
2 *4 Ss U0 {1,S} {3,S}
3    H  U0 {2,S}
""",
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
    longDesc = 
u"""

""",
)

