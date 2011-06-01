#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_ROR/rules"
shortDesc = ""
longDesc = """
561 - 570 Some of the tortional motions in the alkyl part of the 

transition states are treated as free rotations as they are relatively loose TSs.
"""

entry(
    index = 560,
    label = "doublebond;R_OR",
    group1 = "OR{Cd_Cdd, Cdd_Cd, Cd_Cd}",
    group2 = "OR{H_OR, R_OH}",
    kinetics = ArrheniusEP(
        A = (100,"cm^3/(mol*s)"),
        n = 3,
        alpha = 0,
        E0 = (45,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = """Default""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 561,
    label = "Cd/H2_Cd/Nd2;H_OCmethyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2  *2 C 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {5,S} {6,S}
4     H 0 {3,S}
5     H 0 {3,S}
6     H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (93.6,"cm^3/(mol*s)"),
        n = 2.85,
        alpha = 0,
        E0 = (41.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 562,
    label = "Cd/H2_Cd/H/Nd;H_OCmethyl",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2  *2 C 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {5,S} {6,S}
4     H 0 {3,S}
5     H 0 {3,S}
6     H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (24.8,"cm^3/(mol*s)"),
        n = 2.93,
        alpha = 0,
        E0 = (43.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 563,
    label = "Cd/unsub_Cd/unsub;H_OCmethyl",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {5,S} {6,S}
4     H 0 {3,S}
5     H 0 {3,S}
6     H 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (47.3,"cm^3/(mol*s)"),
        n = 3,
        alpha = 0,
        E0 = (47,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 564,
    label = "cco_2H;H_OH",
    group1 = 
"""
1  *1 Cd 0 {2,D} {4,S} {5,S}
2  *2 Cdd 0 {1,D} {3,D}
3     Od 0 {2,D}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (157,"cm^3/(mol*s)"),
        n = 3.04,
        alpha = 0,
        E0 = (39.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 565,
    label = "cco_HNd;H_OH",
    group1 = 
"""
1  *1 Cd 0 {2,D} {4,S} {5,S}
2  *2 Cdd 0 {1,D} {3,D}
3     Od 0 {2,D}
4     H 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (51.5,"cm^3/(mol*s)"),
        n = 3.05,
        alpha = 0,
        E0 = (41,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 566,
    label = "cco_Nd2;H_OH",
    group1 = 
"""
1  *1 Cd 0 {2,D} {4,S} {5,S}
2  *2 Cdd 0 {1,D} {3,D}
3     Od 0 {2,D}
4     {Cs,O} 0 {1,S}
5     {Cs,O} 0 {1,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1450,"cm^3/(mol*s)"),
        n = 2.8,
        alpha = 0,
        E0 = (40.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 567,
    label = "Cd/unsub_Cd/unsub;H_OH",
    group1 = 
"""
1  *1 Cd 0 {2,D} {3,S} {4,S}
2  *2 Cd 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (147,"cm^3/(mol*s)"),
        n = 2.94,
        alpha = 0,
        E0 = (53.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 568,
    label = "Cd/H/Nd_Cd/H2;H_OH",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2  *2 C 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     {Cs,O} 0 {1,S}
5     H 0 {2,S}
6     H 0 {2,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (227,"cm^3/(mol*s)"),
        n = 2.74,
        alpha = 0,
        E0 = (56.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 569,
    label = "Cd/H2_Cd/H/Nd;H_OH",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2  *2 C 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (65.2,"cm^3/(mol*s)"),
        n = 2.92,
        alpha = 0,
        E0 = (50.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 570,
    label = "Cd/H2_Cd/Nd2;H_OH",
    group1 = 
"""
1  *1 C 0 {2,D} {3,S} {4,S}
2  *2 C 0 {1,D} {5,S} {6,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     {Cs,O} 0 {2,S}
6     {Cs,O} 0 {2,S}
""",
    group2 = 
"""
1  *3 H 0 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1250,"cm^3/(mol*s)"),
        n = 2.76,
        alpha = 0,
        E0 = (48.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = """[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

