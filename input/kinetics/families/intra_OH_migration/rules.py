#!/usr/bin/env python
# encoding: utf-8

name = "intra_OH_migration/rules"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 826,
    label = "RnOOH;Y_rad_out",
    group1 = "OR{ROOH, R2OOH, R3OOH, R4OOH}",
    group2 = 
"""
1  *1 {Cd,Cs,Sid,Sis} 1
""",
    kinetics = ArrheniusEP(
        A = (1e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (15,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 827,
    label = "R2OOH_S;C_rad_out_2H",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.39e+11,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (26.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 828,
    label = "R2OOH_S;C_rad_out_H/NonDeC",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3  *2 O 0 {2,S} {4,S}
4  *3 O 0 {3,S} {5,S}
5     H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.69e+11,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (24.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 829,
    label = "R3OOH_SS;C_rad_out_2H",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.47e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (27.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 830,
    label = "R3OOH_SS;C_rad_out_H/NonDeC",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.88e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (26.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 831,
    label = "R3OOH_SS;C_rad_out_Cs2",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
4  *2 O 0 {3,S} {5,S}
5  *3 O 0 {4,S} {6,S}
6     H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.79e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (26.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 832,
    label = "R4OOH_SSS;C_rad_out_2H",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
4     {Cd,Cs} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.12e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (16.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 833,
    label = "R4OOH_SSS;C_rad_out_H/NonDeC",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
4     {Cd,Cs} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (15.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 834,
    label = "R4OOH_SSS;C_rad_out_Cs2",
    group1 = 
"""
1  *1 {Cd,Cs} 1 {2,S}
2  *4 {Cd,Cs} 0 {1,S} {3,S}
3     {Cd,Cs} 0 {2,S} {4,S}
4     {Cd,Cs} 0 {3,S} {5,S}
5  *2 O 0 {4,S} {6,S}
6  *3 O 0 {5,S} {7,S}
7     H 0 {6,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.71e+09,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (14.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

