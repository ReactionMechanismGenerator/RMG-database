#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/rules"
shortDesc = u""
longDesc = u"""
572 - 575 Some of the tortional motions in the alkyl part of the 
transition states are treated as free rotations as they are relatively loose TSs. 

The dictionary defines CO2 in two ways, allowing the R-R' to insert either way
around. However, there are only rates for one of these ways. The other is
presumably matching the top level node.
"""
entry(
    index        = 571,
    label        = "CO2;RR'",
    group1 = "OR{CO2_Od, CO2_Cdd}",
    group2 = "OR{R_H, R_R'}",
    kinetics = ArrheniusEP(
        A = (100000, 'cm^3/(mol*s)'),
        n = 2,
        alpha = 0,
        E0 = (75, 'kcal/mol'),
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
    index        = 572,
    label        = "CO2_Cdd;H2",
    group1 = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Od  U0 {1,D}
3    Od  U0 {1,D}
""",
    group2 = 
"""
1 *3 H U0 {2,S}
2 *4 H U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1510000000.0, 'cm^3/(mol*s)'),
        n = 1.23,
        alpha = 0,
        E0 = (73.9, 'kcal/mol'),
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
    index        = 573,
    label        = "CO2_Cdd;C_methane",
    group1 = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Od  U0 {1,D}
3    Od  U0 {1,D}
""",
    group2 = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4530, 'cm^3/(mol*s)'),
        n = 2.83,
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
    index        = 574,
    label        = "CO2_Cdd;C_pri/NonDeC",
    group1 = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Od  U0 {1,D}
3    Od  U0 {1,D}
""",
    group2 = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.56,
        alpha = 0,
        E0 = (76.6, 'kcal/mol'),
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
    index        = 575,
    label        = "CO2_Cdd;C/H2/NonDeC",
    group1 = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Od  U0 {1,D}
3    Od  U0 {1,D}
""",
    group2 = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (106000, 'cm^3/(mol*s)'),
        n = 2.13,
        alpha = 0,
        E0 = (77, 'kcal/mol'),
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
    index        = 576,
    label        = "CO2_Od;C_methyl_C_pri",
    group1 = 
"""
1 *2 Cdd U0 {2,D} {3,D}
2 *1 Od  U0 {1,D}
3    Od  U0 {1,D}
""",
    group2 = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs U0 {1,S} {6,S} {7,S} {8,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    H  U0 {2,S}
7    H  U0 {2,S}
8    C  U0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (73, 'cm^3/(mol*s)'),
        n = 3.13,
        alpha = 0,
        E0 = (118, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte calculation for methylpropanate using BMK/CBSB7""",
    longDesc = 
u"""

""",
)

