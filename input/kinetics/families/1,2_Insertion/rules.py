#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion/rules"
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

