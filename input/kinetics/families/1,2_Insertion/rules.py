#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion/rules"
shortDesc = u""
longDesc = u"""
553 - 559 Some of the tortional motions in the alkyl part of the 

transition states are treated as free rotations as they are relatively loose TSs.
"""
recommended = True

entry(
    index = 553,
    label = "CO_birad;RR'",
    group1 = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    group2 = "OR{R_H, R_R'}",
    kinetics = ArrheniusEP(
        A = (100000,"cm^3/(mol*s)"),
        n = 2,
        alpha = 0,
        E0 = (80,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 554,
    label = "CO_birad;C_methyl_C_methyl",
    group1 = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    group2 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (538,"cm^3/(mol*s)"),
        n = 3.29,
        alpha = 0,
        E0 = (104.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 555,
    label = "CO_birad;H2",
    group1 = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    group2 = 
"""
1  *2 H 0 {2,S}
2  *3 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.89e+09,"cm^3/(mol*s)"),
        n = 1.16,
        alpha = 0,
        E0 = (82.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 556,
    label = "CO_birad;C_methane",
    group1 = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    group2 = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (16400,"cm^3/(mol*s)"),
        n = 2.86,
        alpha = 0,
        E0 = (86.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 557,
    label = "CO_birad;C_pri/NonDeC",
    group1 = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    group2 = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (91400,"cm^3/(mol*s)"),
        n = 2.53,
        alpha = 0,
        E0 = (85.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 558,
    label = "CO_birad;C/H2/NonDeC",
    group1 = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    group2 = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (766000,"cm^3/(mol*s)"),
        n = 2.07,
        alpha = 0,
        E0 = (82.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 559,
    label = "CO_birad;C/H/Cs3",
    group1 = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    group2 = 
"""
1  *2 C 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     Cs 0 {1,S}
5     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.89e+07,"cm^3/(mol*s)"),
        n = 1.51,
        alpha = 0,
        E0 = (79.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5600,
    label = "CO_birad;CsO_H",
    group1 = 
"""
1  *1 C {2S,2T} {2,D}
2     O 0 {1,D}
""",
    group2 = 
"""
1  *2 O 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.127,"cm^3/(mol*s)"),
        n = 3.7,
        alpha = 0,
        E0 = (53.36,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations by Franklin, 2010""",
    longDesc = 
u"""
CBS-QB3 calculations by CFG, Jan 2010 
Methyl group was hindered rotor. ester CO bond also a rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

