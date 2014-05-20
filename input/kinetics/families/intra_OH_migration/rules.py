#!/usr/bin/env python
# encoding: utf-8

name = "intra_OH_migration/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 826,
    label        = "RnOOH;Y_rad_out",
    group1 = "OR{ROOH, R2OOH, R3OOH, R4OOH}",
    group2 = 
"""
1 *1 {Cd,Cs,Sid,Sis} U1
""",
    kinetics = ArrheniusEP(
        A = (10000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 827,
    label        = "R2OOH_S;C_rad_out_2H",
    group1 = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3 *2 O       U0 {2,S} {4,S}
4 *3 O       U0 {3,S} {5,S}
5    H       U0 {4,S}
""",
    group2 = 
"""
1 *1 C U1 {2,S} {3,S}
2    H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (339000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 828,
    label        = "R2OOH_S;C_rad_out_H/NonDeC",
    group1 = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3 *2 O       U0 {2,S} {4,S}
4 *3 O       U0 {3,S} {5,S}
5    H       U0 {4,S}
""",
    group2 = 
"""
1 *1 C  U1 {2,S} {3,S}
2    H  U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (269000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (24.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 829,
    label        = "R3OOH_SS;C_rad_out_2H",
    group1 = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4 *2 O       U0 {3,S} {5,S}
5 *3 O       U0 {4,S} {6,S}
6    H       U0 {5,S}
""",
    group2 = 
"""
1 *1 C U1 {2,S} {3,S}
2    H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (44700000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (27.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 830,
    label        = "R3OOH_SS;C_rad_out_H/NonDeC",
    group1 = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4 *2 O       U0 {3,S} {5,S}
5 *3 O       U0 {4,S} {6,S}
6    H       U0 {5,S}
""",
    group2 = 
"""
1 *1 C  U1 {2,S} {3,S}
2    H  U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (28800000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 831,
    label        = "R3OOH_SS;C_rad_out_Cs2",
    group1 = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4 *2 O       U0 {3,S} {5,S}
5 *3 O       U0 {4,S} {6,S}
6    H       U0 {5,S}
""",
    group2 = 
"""
1 *1 C  U1 {2,S} {3,S}
2    Cs U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (47900000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 832,
    label        = "R4OOH_SSS;C_rad_out_2H",
    group1 = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4    {Cd,Cs} U0 {3,S} {5,S}
5 *2 O       U0 {4,S} {6,S}
6 *3 O       U0 {5,S} {7,S}
7    H       U0 {6,S}
""",
    group2 = 
"""
1 *1 C U1 {2,S} {3,S}
2    H U0 {1,S}
3    H U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (11200000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (16.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 833,
    label        = "R4OOH_SSS;C_rad_out_H/NonDeC",
    group1 = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4    {Cd,Cs} U0 {3,S} {5,S}
5 *2 O       U0 {4,S} {6,S}
6 *3 O       U0 {5,S} {7,S}
7    H       U0 {6,S}
""",
    group2 = 
"""
1 *1 C  U1 {2,S} {3,S}
2    H  U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
)

entry(
    index        = 834,
    label        = "R4OOH_SSS;C_rad_out_Cs2",
    group1 = 
"""
1 *1 {Cd,Cs} U1 {2,S}
2 *4 {Cd,Cs} U0 {1,S} {3,S}
3    {Cd,Cs} U0 {2,S} {4,S}
4    {Cd,Cs} U0 {3,S} {5,S}
5 *2 O       U0 {4,S} {6,S}
6 *3 O       U0 {5,S} {7,S}
7    H       U0 {6,S}
""",
    group2 = 
"""
1 *1 C  U1 {2,S} {3,S}
2    Cs U0 {1,S}
3    Cs U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8710000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
)

