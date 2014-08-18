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
    index = 571,
    label = "CO2;RR'",
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
    index = 572,
    label = "CO2_Cdd;H2",
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
    index = 573,
    label = "CO2_Cdd;C_methane",
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
    index = 574,
    label = "CO2_Cdd;C_pri/NonDeC",
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
    index = 575,
    label = "CO2_Cdd;C/H2/NonDeC",
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
    index = 576,
    label = "CO2_Od;C_methyl_C_pri",
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

