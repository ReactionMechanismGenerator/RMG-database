#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 812,
    label = "RnOOR;Y_rad_intra",
    group1 = "OR{R2OOH, R3OOH, R4OOH, R5OOH, R2OOR, R3OOR, R4OOR, R5OOR}",
    group2 = 
"""
1 *1 R 1
""",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 813,
    label = "R2OOH_S;C_pri_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    H       0 {4,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4 *4 C 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3980000000000.0, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 813,
    label = "R2OOR_S;C_pri_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    R!H     0 {4,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4 *4 C 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3980000000000.0, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 814,
    label = "R2OOH_S;C_sec_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    H       0 {4,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3 *4 C   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1380000000000.0, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 814,
    label = "R2OOR_S;C_sec_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    R!H     0 {4,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3 *4 C   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1380000000000.0, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 815,
    label = "R2OOR_S;C_ter_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    R!H     0 {4,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2 *4 C   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3090000000000.0, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 815,
    label = "R2OOH_S;C_ter_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    H       0 {4,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2 *4 C   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3090000000000.0, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 816,
    label = "R3OOH_SS;C_pri_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4 *2 O          0 {3,S} {5,S}
5 *3 O          0 {4,S} {6,S}
6    H          0 {5,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4 *4 C 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (447000000000.0, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 816,
    label = "R3OOR_SS;C_pri_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4 *2 O          0 {3,S} {5,S}
5 *3 O          0 {4,S} {6,S}
6    R!H        0 {5,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4 *4 C 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (447000000000.0, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 817,
    label = "R3OOH_SS;C_sec_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4 *2 O          0 {3,S} {5,S}
5 *3 O          0 {4,S} {6,S}
6    H          0 {5,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3 *4 C   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (204000000000.0, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 817,
    label = "R3OOR_SS;C_sec_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4 *2 O          0 {3,S} {5,S}
5 *3 O          0 {4,S} {6,S}
6    R!H        0 {5,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3 *4 C   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (204000000000.0, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 818,
    label = "R3OOR_SS;C_ter_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4 *2 O          0 {3,S} {5,S}
5 *3 O          0 {4,S} {6,S}
6    R!H        0 {5,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2 *4 C   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (331000000000.0, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 818,
    label = "R3OOH_SS;C_ter_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4 *2 O          0 {3,S} {5,S}
5 *3 O          0 {4,S} {6,S}
6    H          0 {5,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2 *4 C   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (331000000000.0, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 819,
    label = "R4OOR_SSS;C_pri_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5 *2 O          0 {4,S} {6,S}
6 *3 O          0 {5,S} {7,S}
7    R!H        0 {6,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4 *4 C 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (51300000000.0, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (14.8, 'kcal/mol', '+|-', 2),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 819,
    label = "R4OOH_SSS;C_pri_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5 *2 O          0 {4,S} {6,S}
6 *3 O          0 {5,S} {7,S}
7    H          0 {6,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4 *4 C 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (51300000000.0, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (14.8, 'kcal/mol', '+|-', 2),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 820,
    label = "R4OOR_SSS;C_sec_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5 *2 O          0 {4,S} {6,S}
6 *3 O          0 {5,S} {7,S}
7    R!H        0 {6,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3 *4 C   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (36300000000.0, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (13, 'kcal/mol', '+|-', 2.5),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 820,
    label = "R4OOH_SSS;C_sec_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5 *2 O          0 {4,S} {6,S}
6 *3 O          0 {5,S} {7,S}
7    H          0 {6,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2    H   0 {1,S}
3 *4 C   0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (36300000000.0, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (13, 'kcal/mol', '+|-', 2.5),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 821,
    label = "R4OOR_SSS;C_ter_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5 *2 O          0 {4,S} {6,S}
6 *3 O          0 {5,S} {7,S}
7    R!H        0 {6,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2 *4 C   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (25700000000.0, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (11.5, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 821,
    label = "R4OOH_SSS;C_ter_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5 *2 O          0 {4,S} {6,S}
6 *3 O          0 {5,S} {7,S}
7    H          0 {6,S}
""",
    group2 = 
"""
1 *1 C   1 {2,S} {3,S} {4,S}
2 *4 C   0 {1,S}
3    R!H 0 {1,S}
4    R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (25700000000.0, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (11.5, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 822,
    label = "R2OOR_S;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    R!H     0 {4,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (600000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 822,
    label = "R2OOH_S;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    H       0 {4,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (600000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 823,
    label = "R3OOR_SS;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4 *2 O          0 {3,S} {5,S}
5 *3 O          0 {4,S} {6,S}
6    R!H        0 {5,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (75000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 823,
    label = "R3OOH_SS;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4 *2 O          0 {3,S} {5,S}
5 *3 O          0 {4,S} {6,S}
6    H          0 {5,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (75000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 824,
    label = "R4OOR_SSS;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5 *2 O          0 {4,S} {6,S}
6 *3 O          0 {5,S} {7,S}
7    R!H        0 {6,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9380000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 824,
    label = "R4OOH_SSS;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5 *2 O          0 {4,S} {6,S}
6 *3 O          0 {5,S} {7,S}
7    H          0 {6,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9380000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 825,
    label = "R5OOH_SSSS;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5    {Cd,Cs,CO} 0 {4,S} {6,S}
6 *2 O          0 {5,S} {7,S}
7 *3 O          0 {6,S} {8,S}
8    H          0 {7,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1170000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 825,
    label = "R5OOR_SSSS;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs}    1 {2,S}
2 *4 {Cd,Cs}    0 {1,S} {3,S}
3    {Cd,Cs,CO} 0 {2,S} {4,S}
4    {Cd,Cs,CO} 0 {3,S} {5,S}
5    {Cd,Cs,CO} 0 {4,S} {6,S}
6 *2 O          0 {5,S} {7,S}
7 *3 O          0 {6,S} {8,S}
8    R!H        0 {7,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1170000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 826,
    label = "R5OOR_SSSSCO;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3    {Cd,Cs} 0 {2,S} {4,S}
4    {Cd,Cs} 0 {3,S} {5,S}
5    CO      0 {4,S} {6,S}
6 *2 O       0 {5,S} {7,S}
7 *3 O       0 {6,S} {8,S}
8    R!H     0 {7,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (127000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment of hindered rotor (SSM)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 826,
    label = "R5OOH_SSSSCO;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3    {Cd,Cs} 0 {2,S} {4,S}
4    {Cd,Cs} 0 {3,S} {5,S}
5    CO      0 {4,S} {6,S}
6 *2 O       0 {5,S} {7,S}
7 *3 O       0 {6,S} {8,S}
8    H       0 {7,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (127000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment of hindered rotor (SSM)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 827,
    label = "R2OOR_SCO;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 CO      0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    R!H     0 {4,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6920000000000000.0, 's^-1'),
        n = -0.53,
        alpha = 0,
        E0 = (24.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment for hindered rotor, QTST Calculation (CFG & JWA)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 827,
    label = "R2OOH_SCO;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 CO      0 {1,S} {3,S}
3 *2 O       0 {2,S} {4,S}
4 *3 O       0 {3,S} {5,S}
5    H       0 {4,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6920000000000000.0, 's^-1'),
        n = -0.53,
        alpha = 0,
        E0 = (24.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment for hindered rotor, QTST Calculation (CFG & JWA)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 828,
    label = "R4OOR_SSSCO;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3    {Cd,Cs} 0 {2,S} {4,S}
4    CO      0 {3,S} {5,S}
5 *2 O       0 {4,S} {6,S}
6 *3 O       0 {5,S} {7,S}
7    R!H     0 {6,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (127000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 828,
    label = "R4OOH_SSSCO;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3    {Cd,Cs} 0 {2,S} {4,S}
4    CO      0 {3,S} {5,S}
5 *2 O       0 {4,S} {6,S}
6 *3 O       0 {5,S} {7,S}
7    H       0 {6,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (127000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 829,
    label = "R3OOH_SSCO;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3    CO      0 {2,S} {4,S}
4 *2 O       0 {3,S} {5,S}
5 *3 O       0 {4,S} {6,S}
6    H       0 {5,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (127000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 829,
    label = "R3OOR_SSCO;Cs_rad_intra",
    group1 = 
"""
1 *1 {Cd,Cs} 1 {2,S}
2 *4 {Cd,Cs} 0 {1,S} {3,S}
3    CO      0 {2,S} {4,S}
4 *2 O       0 {3,S} {5,S}
5 *3 O       0 {4,S} {6,S}
6    R!H     0 {5,S}
""",
    group2 = 
"""
1 *1 C 1 {2,S} {3,S} {4,S}
2 *4 C 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (127000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 17:51:43 2013","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> imported this entry from the old RMG database."""),
    ],
)


