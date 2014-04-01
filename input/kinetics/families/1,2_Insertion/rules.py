#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion/rules"
shortDesc = u""
longDesc = u"""
553 - 559 Some of the tortional motions in the alkyl part of the 

transition states are treated as free rotations as they are relatively loose TSs.
"""
entry(
    index = 553,
    label = "CO_birad;RR'",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = "OR{R_H, R_R'}",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 2,
        alpha = 0,
        E0 = (80, 'kcal/mol'),
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
    index = 554,
    label = "CO_birad;C_methyl_C_methyl",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs 0 {1,S} {6,S} {7,S} {8,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    H  0 {1,S}
6    H  0 {2,S}
7    H  0 {2,S}
8    H  0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (538, 'cm^3/(mol*s)'),
        n = 3.29,
        alpha = 0,
        E0 = (104.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
)

entry(
    index = 555,
    label = "CO_birad;H2",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 H 0 {2,S}
2 *3 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2890000000.0, 'cm^3/(mol*s)'),
        n = 1.16,
        alpha = 0,
        E0 = (82.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
)

entry(
    index = 556,
    label = "CO_birad;C_methane",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.86,
        alpha = 0,
        E0 = (86.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
)

entry(
    index = 557,
    label = "CO_birad;C_pri/NonDeC",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (91400, 'cm^3/(mol*s)'),
        n = 2.53,
        alpha = 0,
        E0 = (85.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
)

entry(
    index = 558,
    label = "CO_birad;C/H2/NonDeC",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  0 {1,S}
3    H  0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (766000, 'cm^3/(mol*s)'),
        n = 2.07,
        alpha = 0,
        E0 = (82.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
)

entry(
    index = 559,
    label = "CO_birad;C/H/Cs3",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  0 {1,S}
3    Cs 0 {1,S}
4    Cs 0 {1,S}
5    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (88900000.0, 'cm^3/(mol*s)'),
        n = 1.51,
        alpha = 0,
        E0 = (79.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""

""",
)

entry(
    index = 560,
    label = "CO_birad;CsO_H",
    group1 = 
"""
1 *1 C {2S,2T} {2,D}
2    O 0       {1,D}
""",
    group2 = 
"""
1 *2 O  0 {2,S} {3,S}
2 *3 H  0 {1,S}
3    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (0.127, 'cm^3/(mol*s)'),
        n = 3.7,
        alpha = 0,
        E0 = (53.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations by Franklin, 2010""",
    longDesc = 
u"""
CBS-QB3 calculations by CFG, Jan 2010 
Methyl group was hindered rotor. ester CO bond also a rotor.
""",
)

entry(
    index = 561,
    label = "carbene;ethene",
    group1 = 
"""
1 *1 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D} {5,S} {6,S}
3 *3 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (663000000000.0, 'cm^3/(mol*s)'),
        n = 0.0073,
        alpha = 0,
        E0 = (-1.045, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino""",
    longDesc = 
u"""

""",
)

entry(
    index = 562,
    label = "carbene;Cd_pri",
    group1 = 
"""
1 *1 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 C 0 {2,D} {3,S} {4,S}
2    C 0 {1,D}
3 *3 H 0 {1,S}
4    H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (35000000000.0, 'cm^3/(mol*s)'),
        n = 0.465,
        alpha = 0,
        E0 = (-1.742, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino, [carbene,propadiene] as model reaction""",
    longDesc = 
u"""

""",
)

entry(
    index = 563,
    label = "carbene;acetylene",
    group1 = 
"""
1 *1 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 Ct 0 {2,S} {3,T}
2 *3 H  0 {1,S}
3    Ct 0 {1,T} {4,S}
4    H  0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (16500000.0, 'cm^3/(mol*s)'),
        n = 1.475,
        alpha = 0,
        E0 = (-1.651, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino""",
    longDesc = 
u"""

""",
)

entry(
    index = 564,
    label = "carbene;Ct_H",
    group1 = 
"""
1 *1 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 Ct 0 {2,S}
2 *3 H  0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (102000000.0, 'cm^3/(mol*s)'),
        n = 1.249,
        alpha = 0,
        E0 = (-2.214, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene, propyne] as model reaction""",
    longDesc = 
u"""

""",
)

entry(
    index = 565,
    label = "carbene;C_pri/Cd",
    group1 = 
"""
1 *1 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Cd 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6620000000000.0, 'cm^3/(mol*s)'),
        n = 0.324,
        alpha = 0,
        E0 = (-0.935, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene,propene]""",
    longDesc = 
u"""

""",
)

entry(
    index = 566,
    label = "carbene;C_pri/Ct",
    group1 = 
"""
1 *1 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 C  0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  0 {1,S}
3    H  0 {1,S}
4    H  0 {1,S}
5    Ct 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2470000000.0, 'cm^3/(mol*s)'),
        n = 0.797,
        alpha = 0,
        E0 = (-1.174, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene,2-butyne]""",
    longDesc = 
u"""

""",
)

entry(
    index = 567,
    label = "carbene;Cd/H/NonDeC",
    group1 = 
"""
1 *1 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 C  0 {2,D} {3,S} {4,S}
2    C  0 {1,D}
3 *3 H  0 {1,S}
4    Cs 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10700000000000.0, 'cm^3/(mol*s)'),
        n = -0.274,
        alpha = 0,
        E0 = (-0.686, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene,propene]""",
    longDesc = 
u"""

""",
)

entry(
    index = 568,
    label = "carbene;Cd/H/OneDe",
    group1 = 
"""
1 *1 C 2S {2,S} {3,S}
2    H 0  {1,S}
3    H 0  {1,S}
""",
    group2 = 
"""
1 *2 C             0 {2,D} {3,S} {4,S}
2    C             0 {1,D}
3 *3 H             0 {1,S}
4    {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (18400000000.0, 'cm^3/(mol*s)'),
        n = 0.498,
        alpha = 0,
        E0 = (-1.758, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (200, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Polino [carbene,1,3-butadiene]""",
    longDesc = 
u"""

""",
)

