#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 553,
    label = "CO_birad;RR'",
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
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.
""",
)

entry(
    index = 554,
    label = "CO_birad;C_methyl_C_methyl",
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
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.
""",
)

entry(
    index = 555,
    label = "CO_birad;H2",
    kinetics = ArrheniusEP(
        A = (2.89e+09, 'cm^3/(mol*s)'),
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
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.
""",
)

entry(
    index = 556,
    label = "CO_birad;C_methane",
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
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.
""",
)

entry(
    index = 557,
    label = "CO_birad;C_pri/NonDeC",
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
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.
""",
)

entry(
    index = 558,
    label = "CO_birad;C/H2/NonDeC",
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
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.
""",
)

entry(
    index = 559,
    label = "CO_birad;C/H/Cs3",
    kinetics = ArrheniusEP(
        A = (8.89e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        alpha = 0,
        E0 = (79.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
)

entry(
    index = 560,
    label = "CO_birad;CsO_H",
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

