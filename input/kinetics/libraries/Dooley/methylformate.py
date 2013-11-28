#!/usr/bin/env python
# encoding: utf-8

name = "Dooley/methylformate"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
O
1 O 2T
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3547000000000000.0, 'cm^3/(mol*s)'),
        n = -0.406,
        Ea = (16599, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Complete Dryer / Curran mechanism for C1-C3 chemistry
CFG





Dryer

****************************************************************************
H2/O2 MECHANISM OF LI ET AL. IJCK 36:565 (2004)                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
O
1 O 2T
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(50800, 'cm^3/(mol*s)'), n=2.67, Ea=(6290, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (216000000.0, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
O
1 O 2T
""",
    reactant2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2970000.0, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (13400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (823, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
H2+AR = H+H+AR                              5.840E+18 -1.10  1.0438E+05  0.0 0.0 0.0
H2+HE = H+H+HE                              5.840E+18 -1.10  1.0438E+05  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70790000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (295, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (420000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (11982, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (130000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1629.3, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (48200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9550000.0, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (580000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (9557, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2530000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
//!****************************  CO/HCO REACTIONS  *************************                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (23000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (222900, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (-1158.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7580000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (410, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (72300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
O2CHO
1 C 0 {2,S} {3,D} {5,S}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
4 O 1 {2,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O2CHO
1 C 0 {2,S} {3,D} {5,S}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
4 O 1 {2,S}
5 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
HO2CHO
1 C 0 {2,S} {4,D} {5,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {6,S}
4 O 0 {1,D}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1990000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11660, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    reactant1 = 
"""
HO2CHO
1 C 0 {2,S} {4,D} {5,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {6,S}
4 O 0 {1,D}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product1 = 
"""
OCHO
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501000000000000.0, 's^-1'),
        n = 0,
        Ea = (40150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (57400000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2748.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
H+CO2+M = OCHO+M                 7.500E+13 0.00 2.900E+04   0.0 0.0 0.0


*****************************************************************************
!****************************  CH2O REACTIONS  *************************                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3080, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3430000000.0, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-447, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1230000.0, 'cm^3/(mol*s)'),
        n = 3,
        Ea = (52000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41100, 'cm^3/(mol*s)'), n=2.5, Ea=(10210, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.636e-06, 'cm^3/(mol*s)'),
        n = 5.42,
        Ea = (998, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
OCH2O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 O 1 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    reactant1 = 
"""
OCH2O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 O 1 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product1 = 
"""
HOCH2O2
1 C 0 {2,S} {3,S} {5,S} {6,S}
2 O 0 {1,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(300000000000.0, 's^-1'), n=0, Ea=(8600, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    reactant1 = 
"""
HOCH2O2
1 C 0 {2,S} {3,S} {5,S} {6,S}
2 O 0 {1,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
HOCH2O2H
1 C 0 {2,S} {3,S} {5,S} {6,S}
2 O 0 {1,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (35000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3275, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    reactant1 = 
"""
HOCH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 O 1 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HOCH2O2H
1 C 0 {2,S} {3,S} {5,S} {6,S}
2 O 0 {1,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
!****************************  CH3 REACTIONS  *************************                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+18, 'cm^3/(mol*s)'),
        n = -1.57,
        Ea = (29230, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.351, 'cm^3/(mol*s)'), n=3.524, Ea=(7380, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24100000000.0, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-2325, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54700000.0, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (11210, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3150000000000.0, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (10290, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5720000.0, 'cm^3/(mol*s)'),
        n = 1.96,
        Ea = (2639, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3160000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (181000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18580, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14.4, 'cm^3/(mol*s)'), n=3.1, Ea=(6935, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
!****************************  CH3O REACTIONS  *************************                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1990000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11660, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (181000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18480, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1810000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13710, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5080000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1411, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (247000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1570, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (311000000000000.0, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (-1051, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product3 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    reactant1 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (631000000000000.0, 's^-1'),
        n = 0,
        Ea = (42300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
!****************************  CH2OH REACTIONS  *************************                                                            *
*****************************************************************************


CH2OH+M = CH2O+H+M                          1.000E+14  0.00  2.510E+04  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96350000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (241000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5017, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1510000000000000.0, 'cm^3/(mol*s)'),
                n = -1,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
HOCH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 O 1 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
!****************************  CH3O REACTIONS  *************************                                                            *
*****************************************************************************


CH3O+M = CH2O+H+M                           8.300E+17 -1.20  1.550E+04  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (90330000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (11980, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (22000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (1748, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6095, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
!****************************  CH3OH REACTIONS  *************************                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6095, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(388000, 'cm^3/(mol*s)'), n=2.5, Ea=(3080, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000.0, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (496.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7100000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (44900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9635, 'cm^3/(mol*s)'), n=2.9, Ea=(13110, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (39800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(31.9, 'cm^3/(mol*s)'), n=3.17, Ea=(7172, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4060, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4990000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2460000.0, 'cm^3/(mol*s)'), n=2, Ea=(8270, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-570, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5420, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-570, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (80000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
!****************************  CH/CH2/CH2(S) REACTIONS  ******************                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(500000, 'cm^3/(mol*s)'), n=2, Ea=(7230, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2(S)+AR = CH2+AR                          9.000E+12  0.00  6.000E+02  0.0 0.0 0.0
!CH2(S)+H = CH+H2                            3.000E+13  0.00  0.000E+00  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product3 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+18, 'cm^3/(mol*s)'), n=-1.56, Ea=(0, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (270000000000.0, 'cm^3/(mol*s)'),
                n = 0.67,
                Ea = (25700, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11300000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C(T)
1 C 4T
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (57000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17130000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-755, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (685, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    reactant1 = 
"""
HOCH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 O 1 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 's^-1'),
        n = 0,
        Ea = (14900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
!****************************  Formic Acid REACTIONS  ******************                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HOCH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 O 1 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4500000000000000.0, 'cm^3/(mol*s)'),
        n = -1.11,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.593e+18, 's^-1'), n=-0.46, Ea=(108300, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
HCOOH+M = CO+H2O+M                          2.300E+13  0.00  5.000E+04   0.0 0.0 0.0
HCOOH+M = CO2+H2+M                          1.500E+16  0.00  5.700E+04   0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2620000.0, 'cm^3/(mol*s)'),
        n = 2.06,
        Ea = (916, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18500000.0, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4240000.0, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4868, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60300000000000.0, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (2988, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e-07, 'cm^3/(mol*s)'), n=5.8, Ea=(2200, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.77e+18, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (2975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (115000000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
!************************** C2H6 REACTIONS  ******************                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3550000.0, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5830, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14800000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (51870, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.51e-07, 'cm^3/(mol*s)'), n=6, Ea=(6047, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(34.6, 'cm^3/(mol*s)'), n=3.61, Ea=(16920, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(19.4, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (241000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7090, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-260, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    reactant1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    reactant1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (482000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (71530, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(11800, 'cm^3/(mol*s)'), n=2.45, Ea=(-2921, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (110000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    reactant1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42800000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1097, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CURRAN ESTIMATE
CH3+CH2O = C2H5O                3.000E+11 0.00 6.336E+03    0.0 0.0 0.0

!HEALY ET AL C&F, 155: 45//!1 461 (2008)
!FROM CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.876e+56, 'cm^3/(mol*s)'),
        n = -13.82,
        Ea = (14620, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    reactant1 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1990000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11660, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM TSANG & HAMPSON, METHANE, J. PHYS. CHEM. REF. DATA, VOL 15, 1986
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (181000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18480, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BASED ON CH4+CH3O2
!FROM TSANG & HAMPSON, METHANE, J. PHYS. CHEM. REF. DATA, VOL 15, 1986
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 162,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1810000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13710, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
! TSANG, JPC REF. DATA, 16:471 (1987)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    reactant1 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3275, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
! TSANG, JPC REF. DATA, 16:471 (1987)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CARSTENSEN AND DEAN 30TH SYMPOSIUM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    reactant1 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    product1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (631000000000000.0, 's^-1'),
        n = 0,
        Ea = (42300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CARSTENSEN AND DEAN 30TH SYMPOSIUM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H4O2H
1 C 1 {2,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {4,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.814e+45, 'cm^3/(mol*s)'),
        n = -11.5,
        Ea = (14600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (756100000000000.0, 'cm^3/(mol*s)'),
                n = -1.01,
                Ea = (4749, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(0.4, 'cm^3/(mol*s)'), n=3.88, Ea=(13620, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM


!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (162600000000.0, 'cm^3/(mol*s)'),
        n = -0.31,
        Ea = (6150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 170,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(826.5, 'cm^3/(mol*s)'), n=2.41, Ea=(5285, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    reactant1 = 
"""
C2H4O2H
1 C 1 {2,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {4,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {4,S}
""",
    product1 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.203e+36, 's^-1'), n=-8.13, Ea=(27020, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    reactant1 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52e+41, 's^-1'), n=-10.2, Ea=(43710, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
    reactant1 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.815e+38, 's^-1'), n=-8.45, Ea=(37890, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 174,
    reactant1 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+43, 's^-1'), n=-10.46, Ea=(45580, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
    reactant1 = 
"""
C2H4O2H
1 C 1 {2,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {4,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {4,S}
""",
    product1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.848e+30, 's^-1'), n=-6.08, Ea=(20660, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
    reactant1 = 
"""
C2H4O2H
1 C 1 {2,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {4,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {4,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98e+34, 's^-1'), n=-7.25, Ea=(23250, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    reactant1 = 
"""
C2H4O2H
1 C 1 {2,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {4,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {4,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.188e+34, 's^-1'), n=-9.02, Ea=(29210, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM C2H5 CHEMISTRY FROM DE SAIN ET AL.
!J. PHYS. CHEM. A. 2003 107:4415-4427.
!AT 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
    reactant1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(36300000000000.0, 's^-1'), n=0, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM LIFSHITZ ET AL. 1983
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    reactant1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7407000000000.0, 's^-1'), n=0, Ea=(53800, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM FIT TO DATA ON NIST STANDARD REFERENCE DATABASE 17 -2Q98
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    reactant1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H3O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3610, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BALDWIN ET AL. 1984.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    reactant1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H3O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (80000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9680, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BALDWIN ET AL. 1984.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    reactant1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H3O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CURRAN, ANALOGY TO ETHENE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    reactant1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
C2H3O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CURRAN, ANALOGY TO ETHENE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    reactant1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
C2H3O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CURRAN, ANALOGY TO ETHENE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    reactant1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H3O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1070000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11830, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BALDWIN, KEEN AND WALKER,
!J. CHEM. SOC. FARADAY TRANS. 1, 80, 435 (1984).
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    reactant1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
C2H3O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6750, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    reactant1 = 
"""
C2H3O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (850000000000000.0, 's^-1'),
        n = 0,
        Ea = (14000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BALDWIN, KEEN AND WALKER,
!J. CHEM. SOC. FARADAY TRANS. 1, 80, 435 (1984).
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    reactant1 = 
"""
C2H3O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product1 = 
"""
CH2CHO
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 's^-1'),
        n = 0,
        Ea = (14000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BALDWIN, KEEN AND WALKER,
!J. CHEM. SOC. FARADAY TRANS. 1, 80, 435 (1984).
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3110, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM WHYSTOCK ET AL. 1976.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5940000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1868, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM FIT TO DATA ON NIST STANDARD REFERENCE DATABASE 17 -2Q98
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 192,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (1300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM TAYLOR ET AL. 1996.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (39150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BAULCH ET AL. J. PHYS. CHEM. REF. DATA, 21, 411--429, 1992.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 194,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1760, 'cm^3/(mol*s)'), n=2.79, Ea=(4950, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM FIT TO DATA ON NIST STANDARD REFERENCE DATABASE 17 -2Q98
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 195,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BAULCH ET AL. J. PHYS. CHEM. REF. DATA, 21, 411--429, 1992.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 196,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BAULCH ET AL. J. PHYS. CHEM. REF. DATA, 21, 411--429, 1992.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 197,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BAULCH ET AL. J. PHYS. CHEM. REF. DATA, 21, 411--429, 1992.
!ANALOGY TO CH3CHO+CH3O2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 198,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000000.0, 'cm^3/(mol*s)'),
        n = -1.08,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!WKM!REACTION AND RATE TAKEN FROM NUIG BUT NAMING SCHEME CHANGED
!HOCHO CHANGED TO HCOOH

!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM TAYLOR ET AL. 1996.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 199,
    reactant1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CHO
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(172000, 'cm^3/(mol*s)'), n=2.4, Ea=(815, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM TAYLOR ET AL. 1996.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 201,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 202,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 203,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 204,
    reactant1 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3275, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 205,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2410000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9936, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 206,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (181000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18480, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 207,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1990000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11660, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM TSANG & HAMPSON, METHANE, J. PHYS. CHEM. REF. DATA, VOL 15, 1986
!ANALOGY WITH CH3O2 + CH2O
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 208,
    reactant1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CURRAN
!ANALOGY TO C2H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 209,
    reactant1 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    product1 = 
"""
CH3CO2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 1 {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501000000000000.0, 's^-1'),
        n = 0,
        Ea = (40150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!REV/ 1.450E+12 0.04 9.460E+03 /

!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SAHETCHIAN ET AL. 1992
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 210,
    reactant1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CHO
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!REV/ 3.618E+07 1.76 1.338E+03 /

!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 211,
    reactant1 = 
"""
CH2CHO
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BAULCH ET AL. J. PHYS. CHEM. REF. DATA, 21, 411--429, 1992
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 212,
    reactant1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM WARNATZ, J., UNPUBLISHED
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    reactant1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 214,
    reactant1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1750000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1350, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 215,
    reactant1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 216,
    reactant1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 217,
    reactant1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 218,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 219,
    reactant1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 220,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 221,
    reactant1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (80000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 222,
    reactant1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (850, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM HIDAKA ??
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 223,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (94600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-515, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SMITH ET AL., GRI MECH 2.11
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 224,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SMITH ET AL., GRI MECH 2.11
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 225,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50700000.0, 'cm^3/(mol*s)'),
        n = 1.93,
        Ea = (12950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM KNYAZEV,V.D.; BENCSURA,A.; STOLIAROV,S.I.; SLAGLE,I.R.
!J. PHYS. CHEM. 100, 11346-1135 (1996)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 226,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8564000.0, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BAULCH ET AL. 2005
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 227,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CHO
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4986000.0, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BAULCH ET AL. 2005
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 228,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1800000.0, 'cm^3/(mol*s)'), n=2, Ea=(2500, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!FROM LI DME PAPER
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 229,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.62, 'cm^3/(mol*s)'), n=3.7, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM TSANG
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 230,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (58200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 231,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6750, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM TSANG & HAMPSON, METHANE, J. PHYS. CHEM. REF. DATA, VOL 15, 1986
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 232,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2230000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17190, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BAULCH ET AL. J. PHYS. CHEM. REF. DATA, 21, 411--429, 1992
!ANALOGY TO C2H4+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 233,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2230000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17190, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BAULCH ET AL. J. PHYS. CHEM. REF. DATA, 21, 411--429, 1992
!ANALOGY TO C2H4+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 234,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 235,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2820000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17110, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 236,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2820000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17110, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 237,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H4O1-2
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2230000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17190, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 238,
    reactant1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM BUTLER, FLEMING, GOSS, LIN, ACS SYMP. SER. 134 (1980)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 239,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16, 'cm^3/(mol*s)'),
        n = -1.39,
        Ea = (1015, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
C2H2 chemistry
!WKM
!FROM GRI MECH 3.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 240,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1337000.0, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-384, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!WKM
!FROM GRI MECH 3.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 241,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
O
1 O 2T
""",
    product2 = 
"""
CH2CHO
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0.29,
        Ea = (11, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!WKM
! WANG ET AL. EASTERN ESTATES MEETING COMBUSTION INSTITUTE, PAPER 129 (1999)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 242,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (392000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 243,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GRI MECH 3.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 244,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GRI MECH 3.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 245,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (30100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 246,
    reactant1 = 
"""
O
1 O 2T
""",
    reactant2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product1 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19, 'cm^3/(mol*s)'),
        n = -1.4,
        Ea = (28950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GRI MECH 3.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 247,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6940000.0, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GRI MECH 3.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 248,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13500000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GRI MECH 3.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 249,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
3 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33700000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (14000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 250,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32360000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 251,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.000483, 'cm^3/(mol*s)'), n=4, Ea=(-2000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GRI MECH 3.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 252,
    reactant1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
HCCOH
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 O 0 {1,S} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(504000, 'cm^3/(mol*s)'), n=2.3, Ea=(13500, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GRI MECH 3.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 253,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
HCCOH
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 O 0 {1,S} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SMITH ET AL., GRI MECH 2.11
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 254,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (52800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 255,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (50150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 256,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (174000000000.0, 'cm^3/(mol*s)'),
        n = 0.27,
        Ea = (600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 257,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (464000000000.0, 'cm^3/(mol*s)'),
        n = 0.15,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 258,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (746000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (1634, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 259,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12300000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (5098, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 260,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25800000.0, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (2827, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 261,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (3038, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 262,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12300, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 263,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 264,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 265,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12300, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
!ANOLOGY TO C2H5OH+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 266,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8200, 'cm^3/(mol*s)'), n=2.55, Ea=(10750, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
!ANOLOGY TO C2H5OH+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 267,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM NICK MARINOV
!IJCK 31: 183 220, 1999
!ANOLOGY TO C2H5OH+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 268,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (94100000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (5459, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 269,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18800000.0, 'cm^3/(mol*s)'),
        n = 1.85,
        Ea = (1824, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 270,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15800000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (4448, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 271,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(133, 'cm^3/(mol*s)'), n=3.18, Ea=(9362, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 272,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(444, 'cm^3/(mol*s)'), n=2.9, Ea=(7690, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 273,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(134, 'cm^3/(mol*s)'), n=2.92, Ea=(7452, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 274,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CURRAN ESTIMATE
!1/2 OF C4H10+C2H5
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 275,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 276,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.17e+20, 'cm^3/(mol*s)'),
        n = -2.84,
        Ea = (1240, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM FIT TO DATA ON NIST STANDARD REFERENCE DATABASE 17 -2Q98
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 277,
    reactant1 = 
"""
O2C2H4OH
1  O 0 {2,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
PC2H4OH
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.9e+16, 's^-1'), n=-1, Ea=(30000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
!BASED ON C3H6OH+O2 REACTION
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 278,
    reactant1 = 
"""
O2C2H4OH
1  O 0 {2,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product3 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3125000000.0, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 279,
    reactant1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3810000.0, 'cm^3/(mol*s)'), n=2, Ea=(1641, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
!ANALOGY TO CH2OH+O2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 280,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(125000, 'cm^3/(mol*s)'), n=2.48, Ea=(445, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
END C2 CHEMISTRY

!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 281,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(980000, 'cm^3/(mol*s)'), n=2.43, Ea=(5160, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 282,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (513000000000.0, 'cm^3/(mol*s)'),
        n = 0.21,
        Ea = (4890, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM FIT TO DATA ON NIST STANDARD REFERENCE DATABASE 17 -2Q98
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 283,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (396000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9784, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 284,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (434000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 285,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (48500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 286,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO ETHANE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 287,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!REV/ 6.397E+14 -0.75 1.383E+04 /

!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO ETHANE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 288,
    reactant1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 's^-1'),
        n = 0,
        Ea = (31000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO PROPANE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 289,
    reactant1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3COCH2O2
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 {2,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 1 {5,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 290,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
CH3COCH2O2
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 {2,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 1 {5,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
""",
    product1 = 
"""
CH3COCH2
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {4,S}
3 C 0 {2,S} {5,S} {6,S} {7,S}
4 C 1 {2,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product2 = 
"""
CH3COCH2O2H
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 {2,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 0 {5,S} {12,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
12 H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 291,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3COCH2O2
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 {2,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 1 {5,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
CH3COCH2O2H
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 {2,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 0 {5,S} {12,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
12 H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (128800000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 292,
    reactant1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    reactant2 = 
"""
CH3COCH2O2
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 {2,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 1 {5,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
""",
    product1 = 
"""
CH3COCH2O2H
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 {2,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 0 {5,S} {12,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
12 H 0 {6,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 293,
    reactant1 = 
"""
CH3COCH2O2H
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {7,S} {8,S} {9,S}
4  C 0 {2,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 0 {5,S} {12,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
12 H 0 {6,S}
""",
    product1 = 
"""
CH3COCH2O
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {6,S} {7,S} {8,S}
4  C 0 {2,S} {5,S} {9,S} {10,S}
5  O 1 {4,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 294,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3COCH2O
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {6,S} {7,S} {8,S}
4  C 0 {2,S} {5,S} {9,S} {10,S}
5  O 1 {4,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 295,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 296,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 297,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5940000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1868, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 298,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!MARINOV ET AL. COMBUST SCI TECH 116:211 1996
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 299,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000.0, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!MARINOV ET AL. COMBUST SCI TECH 116:211 1996
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 300,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9240000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM TAYLOR ET AL. 1996.
!ANALOGY WITH CH3CHO+OH
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 301,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10050000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 302,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BASED ON CH3CHO+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 303,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2608000.0, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (5911, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BASED ON CH3CHO+CH3
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 304,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1740000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8440, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH ACETALDEHYDE.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 305,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH CH3CHO + CH3O
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 306,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BASED ON CH3CHO + HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 307,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (151000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4810, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM TSANG & HAMPSON, METHANE, J. PHYS. CHEM. REF. DATA, VOL 15, 1986
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    reactant1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2CHO
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+20, 'cm^3/(mol*s)'),
        n = -2.72,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!ALZUETA & GLARBORG IJCK 32: 498-522, 2000.
!PRIVATE COMMUNICATION WITH BOZZELLI (ZHONG'S THESIS)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    reactant1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!MARINOV ET AL. COMBUST SCI TECH 116:211 1996
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 310,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 311,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH CH3CHO + H
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 312,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1790, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH CH3CHO + O
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 313,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26900000000.0, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-340, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 314,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2608000.0, 'cm^3/(mol*s)'),
        n = 1.78,
        Ea = (5911, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM FIT TO DATA ON NIST STANDARD REFERENCE DATABASE 17 -2Q98
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 315,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH CH3CHO + HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 316,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH CH3CHO + CH3O
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 317,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH CH3CHO + HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 318,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ACETALDEHYDE ANALOG
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 319,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (602600000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3300, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ACETALDEHYDE ANALOG
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 320,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BASED ON CH3CHO + HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 321,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10050000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (40700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 322,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BASED ON CH3CHO + HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 323,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8440, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH ACETALDEHYDE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 324,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (151000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4810, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 325,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(935000, 'cm^3/(mol*s)'), n=2.29, Ea=(-781, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!WKM
!NEW DME RATE CONSTANTS FROM CURRAN.
!PRIVATE COMMUNICATION
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 326,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(36120, 'cm^3/(mol*s)'), n=2.88, Ea=(2996, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!NEW DME RATE CONSTANTS FROM CURRAN.
!PRIVATE COMMUNICATION
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 327,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (775000000.0, 'cm^3/(mol*s)'),
        n = 1.36,
        Ea = (2250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!NEW DME RATE CONSTANTS FROM CURRAN.
!PRIVATE COMMUNICATION
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 328,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13440000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!NEW DME RATE CONSTANTS FROM CURRAN.
!PRIVATE COMMUNICATION
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 329,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13440000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!NEW DME RATE CONSTANTS FROM CURRAN.
!PRIVATE COMMUNICATION
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 330,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.445e-06, 'cm^3/(mol*s)'),
        n = 5.73,
        Ea = (5699, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 331,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (41000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (44910, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 332,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (602000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4074, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 333,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3OCH2O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH3OCH2O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {11,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 334,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O2CHO
1 C 0 {2,S} {3,D} {5,S}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
4 O 1 {2,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
HO2CHO
1 C 0 {2,S} {4,D} {5,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {6,S}
4 O 0 {1,D}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(44250, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 335,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OCHO
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 336,
    reactant1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(16000000000000.0, 's^-1'), n=0, Ea=(25500, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 337,
    reactant1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 338,
    reactant1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5490, 'cm^3/(mol*s)'), n=2.8, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 339,
    reactant1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1260000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8499, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 340,
    reactant1 = 
"""
CH3OCH2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3OCH2O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 341,
    reactant1 = 
"""
CH3OCH2O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {11,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {5,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11660, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!1/2 TSANG/HAMPSON CH3O2 + CH2O = CH3O2H + HCO
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 342,
    reactant1 = 
"""
CH3OCH2O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3OCH2O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {11,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {5,S}
""",
    product2 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 343,
    reactant1 = 
"""
CH3OCH2O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
CH3OCH2O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product2 = 
"""
CH3OCH2O
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product3 = 
"""
CH3OCH2O
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21e+23, 'cm^3/(mol*s)'), n=-4.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 344,
    reactant1 = 
"""
CH3OCH2O
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {11,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 345,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3OCH2O
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 346,
    reactant1 = 
"""
CH3OCH2O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
CH2OCH2O2H
1  C 1 {2,S} {6,S} {7,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {10,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(60000000000.0, 's^-1'), n=0, Ea=(21580, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
!CH3OCH2O+O2 = CH3OCHO+HO2             5.000E+10 0.00 5.000E+02   0.0 0.0 0.0

!HEALY ET AL C&F, 155: 451 461 (2008)
!CH3OCHO+H = CH3OCH2O                 1.000E+13 0.00 7.838E+03   0.0 0.0 0.0

!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 347,
    reactant1 = 
"""
CH2OCH2O2H
1  C 1 {2,S} {6,S} {7,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {10,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {5,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product3 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(15000000000000.0, 's^-1'), n=0, Ea=(20760, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 348,
    reactant1 = 
"""
CH2OCH2O2H
1  C 1 {2,S} {6,S} {7,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {10,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {5,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
O2CH2OCH2O2H
1  C 0 {2,S} {6,S} {8,S} {9,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  O 0 {1,S} {7,S}
7  O 1 {6,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 349,
    reactant1 = 
"""
O2CH2OCH2O2H
1  C 0 {2,S} {6,S} {8,S} {9,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  O 0 {1,S} {7,S}
7  O 1 {6,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    product1 = 
"""
HO2CH2OCHO
1  O 0 {2,S} {7,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {5,S}
5  C 0 {4,S} {6,D} {10,S}
6  O 0 {5,D}
7  H 0 {1,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {5,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40000000000.0, 's^-1'), n=0, Ea=(18580, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 350,
    reactant1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
/ BEGIN C3 Chemistry

!HEALY ET AL C&F, 155: 451 461 (2008)
!ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 351,
    reactant1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 352,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (49640, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 353,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (52290, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 354,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1300000.0, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (4471, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 355,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1330000.0, 'cm^3/(mol*s)'),
        n = 2.54,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 356,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(549000, 'cm^3/(mol*s)'), n=2.5, Ea=(3140, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 357,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3710000.0, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (5505, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 358,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10540000000.0, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 359,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (46700000.0, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 360,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(58800, 'cm^3/(mol*s)'), n=2.5, Ea=(14860, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SCOTT AND WALKER C&F 129(4) 365--377 2002 (*1.2)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 361,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(81000, 'cm^3/(mol*s)'), n=2.5, Ea=(16690, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SCOTT AND WALKER C&F 129(4) 365--377 2002 (*1.5)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 362,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(64000, 'cm^3/(mol*s)'), n=2.17, Ea=(7520, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM FIT TO DATA ON NIST STANDARD REFERENCE DATABASE 17 -2Q98
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 363,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!TSANG, W. CHEMICAL KINETIC DATA BASE FOR COMBUSTION CHEMISTRY. PART 3. PROPANE
!J. PHYS. CHEM. REF. DATA 17, 887 (1988)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 364,
    reactant1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (12900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM HAUTMAN, D. J., SANTORO, R. J., DRYER, F. L.,
!AND GLASSMAN, I., TO BE PUBLISHED.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 365,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM HAUTMAN, D. J., SANTORO, R. J., DRYER, F. L.,
!AND GLASSMAN, I., TO BE PUBLISHED.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 366,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM HAUTMAN, D. J., SANTORO, R. J., DRYER, F. L.,
!AND GLASSMAN, I., TO BE PUBLISHED.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 367,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM HAUTMAN, D. J., SANTORO, R. J., DRYER, F. L.,
!AND GLASSMAN, I., TO BE PUBLISHED.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 368,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM HAUTMAN, D. J., SANTORO, R. J., DRYER, F. L.,
!AND GLASSMAN, I., TO BE PUBLISHED.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 369,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (794000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM DAGAUT, P, CATHONNET, M., AND BOETTNER, J-C,
!CST 71, 111(1990)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 370,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (794000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM DAGAUT, P, CATHONNET, M., AND BOETTNER, J-C,
!CST 71, 111(1990)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 371,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FRED DRYER ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 372,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FRED DRYER ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 373,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(81000, 'cm^3/(mol*s)'), n=2.5, Ea=(16690, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SCOTT AND WALKER C&F 129(4) 365--377 2002 (*1.5)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 374,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(58800, 'cm^3/(mol*s)'), n=2.5, Ea=(14860, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SCOTT AND WALKER C&F 129(4) 365--377 2002 (*1.2)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 375,
    reactant1 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    product2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(81000, 'cm^3/(mol*s)'), n=2.5, Ea=(16690, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SCOTT AND WALKER C&F 129(4) 365--377 2002 (*1.5)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 376,
    reactant1 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    product2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(58800, 'cm^3/(mol*s)'), n=2.5, Ea=(14860, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SCOTT AND WALKER C&F 129(4) 365--377 2002 (*1.2)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 377,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANAOLGY TO C2H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 378,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM WALKER, R. W., REACTION KINETICS,
!VOL. 1, S. P. R. CHEMICAL SOCIETY, 1975
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 379,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANAOLGY TO C2H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 380,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM WALKER, R. W., REACTION KINETICS,
!VOL. 1, S. P. R. CHEMICAL SOCIETY, 1975
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 381,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM WALKER, R. W., REACTION KINETICS,
!VOL. 1, S. P. R. CHEMICAL SOCIETY, 1975
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 382,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANAOLGY TO C2H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 383,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
O2CHO
1 C 0 {2,S} {3,D} {5,S}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
4 O 1 {2,S}
5 H 0 {1,S}
""",
    product1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
HO2CHO
1 C 0 {2,S} {4,D} {5,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {6,S}
4 O 0 {1,D}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(55200, 'cm^3/(mol*s)'), n=2.55, Ea=(16480, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!REV/ 1.673E+12 -0.01 9.570E+03 /

!HEALY ET AL C&F, 155: 451 461 (2008)
!ANAOLGY TO C2H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 384,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
O2CHO
1 C 0 {2,S} {3,D} {5,S}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
4 O 1 {2,S}
5 H 0 {1,S}
""",
    product1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
HO2CHO
1 C 0 {2,S} {4,D} {5,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {6,S}
4 O 0 {1,D}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(14750, 'cm^3/(mol*s)'), n=2.6, Ea=(13910, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANAOLGY TO C2H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 385,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2160, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 386,
    reactant1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 387,
    reactant1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.5e-19, 'cm^3/(mol*s)'), n=0, Ea=(5020, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!THIS REACTION HAS BEEN EFFECTIVELY REMOVED BY CURRAN
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 388,
    reactant1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!TSANG, W. CHEMICAL KINETIC DATA BASE FOR COMBUSTION CHEMISTRY. PART 3. PROPANE
!J. PHYS. CHEM. REF. DATA 17, 887 (1988)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 389,
    reactant1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (48180000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!TSANG, W. CHEMICAL KINETIC DATA BASE FOR COMBUSTION CHEMISTRY. PART 3. PROPANE
!J. PHYS. CHEM. REF. DATA 17, 887 (1988)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 390,
    reactant1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (48180000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!TSANG, W. CHEMICAL KINETIC DATA BASE FOR COMBUSTION CHEMISTRY. PART 3. PROPANE
!J. PHYS. CHEM. REF. DATA 17, 887 (1988)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 391,
    reactant1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.97e+40, 's^-1'), n=-8.6, Ea=(41430, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 392,
    reactant1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.78e+39, 's^-1'), n=-8.1, Ea=(46580, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 393,
    reactant1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e-19, 'cm^3/(mol*s)'), n=0, Ea=(3000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!THIS REACTION HAS BEEN EFFECTIVELY REMOVED BY CURRAN
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 394,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8440, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH ACETALDEHYDE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 395,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8440, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH ACETALDEHYDE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 396,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product2 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8440, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY WITH ACETALDEHYDE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 397,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.71e+69, 's^-1'), n=-16.09, Ea=(140000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 398,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e+71, 's^-1'), n=-16.58, Ea=(139300, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 399,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15800000.0, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (-1216, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM KOERT ET AL. ENERGY & FUELS
!VOL 6: 485-493 1992
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 400,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25000000.0, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM KOERT ET AL. ENERGY & FUELS
!VOL 6: 485-493 1992
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 401,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CHCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,D} {8,S}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25000000.0, 'cm^3/(mol*s)'),
        n = 1.76,
        Ea = (76, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM KOERT ET AL. ENERGY & FUELS
!VOL 6: 485-493 1992
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 402,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (524000000000.0, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (5884, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM KOERT ET AL. ENERGY & FUELS
!VOL 6: 485-493 1992
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 403,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (8959, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM KOERT ET AL. ENERGY & FUELS
!VOL 6: 485-493 1992
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 404,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60300000000.0, 'cm^3/(mol*s)'),
        n = 0.7,
        Ea = (7632, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM KOERT ET AL. ENERGY & FUELS
!VOL 6: 485-493 1992
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 405,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3120000.0, 'cm^3/(mol*s)'), n=2, Ea=(-298, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 406,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2110000.0, 'cm^3/(mol*s)'), n=2, Ea=(2778, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!REV/ 1.347E+07 1.91 3.027E+04 /

!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 407,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1110000.0, 'cm^3/(mol*s)'), n=2, Ea=(1451, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!REV/ 2.968E+04 2.39 9.916E+03 /

!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 408,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(27000, 'cm^3/(mol*s)'), n=2.5, Ea=(12340, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!REV/ 3.576E+03 2.59 1.070E+04 /

!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SCOTT AND WALKER C&F 129(4) 365--377 2002
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 409,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18000, 'cm^3/(mol*s)'), n=2.5, Ea=(27620, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SCOTT AND WALKER C&F 129(4) 365--377 2002
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 410,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9000, 'cm^3/(mol*s)'), n=2.5, Ea=(23590, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM SCOTT AND WALKER C&F 129(4) 365--377 2002
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 411,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+24, 'cm^3/(mol*s)'),
        n = -3.04,
        Ea = (15610, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL IJCK 32 589-614 2000
!!!!!!!!!PRESSURE DEPENDANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!91TSA RRKM 0.1 ATM
!C3H6+H = C2H4+CH3                      8.80E+16 -1.05 6461.0   0.0 0.0 0.0
!91TSA RRKM 1 ATM
!C3H6+H = C2H4+CH3                      8.00E+21 -2.39 11180.0   0.0 0.0 0.0
!91TSA RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 412,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(173000, 'cm^3/(mol*s)'), n=2.5, Ea=(2490, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 413,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(400000, 'cm^3/(mol*s)'), n=2.5, Ea=(9790, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 414,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(804000, 'cm^3/(mol*s)'), n=2.5, Ea=(12283, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 415,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (39900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 416,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (62900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 417,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 418,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.21, 'cm^3/(mol*s)'), n=3.5, Ea=(5675, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!TSANG, W. CHEMICAL KINETIC DATA BASE FOR COMBUSTION CHEMISTRY. PART 3. PROPANE
!J. PHYS. CHEM. REF. DATA 17, 887 (1988)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 419,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.348, 'cm^3/(mol*s)'), n=3.5, Ea=(12850, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!REV/ 8.184E+02 3.07 2.289E+04 /

!HEALY ET AL C&F, 155: 451 461 (2008)
!TSANG, W. CHEMICAL KINETIC DATA BASE FOR COMBUSTION CHEMISTRY. PART 3. PROPANE
!J. PHYS. CHEM. REF. DATA 17, 887 (1988)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 420,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.84, 'cm^3/(mol*s)'), n=3.5, Ea=(11660, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!REV/ 1.626E+00 3.55 6.635E+03 /

!HEALY ET AL C&F, 155: 451 461 (2008)
!TSANG, W. CHEMICAL KINETIC DATA BASE FOR COMBUSTION CHEMISTRY. PART 3. PROPANE
!J. PHYS. CHEM. REF. DATA 17, 887 (1988)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 421,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ALLARA, D. L. AND SHAW, R.,
!J. PHYS. CHEM. REF. DATA 9, 523 (1980)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 422,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH3CO3H
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 0 {4,S} {9,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
9 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (324000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO C3H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 423,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (324000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO C3H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 424,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1290000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 425,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
C2H5O2H
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  O 0 {2,S} {4,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (324000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO C3H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 426,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (324000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO C3H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 427,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (324000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (14900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO C3H6+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 428,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C3H6OH
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 1 {1,S} {3,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {11,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (993000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-960, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO C3H6+HO2
CFG assumes HOCH2CHCH3
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 429,
    reactant1 = 
"""
C3H6OH
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 1 {1,S} {3,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {11,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {4,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HOC3H6O2
1  O 0 {2,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {5,S} {10,S}
4  C 0 {3,S} {11,S} {12,S} {13,S}
5  O 0 {3,S} {6,S}
6  O 1 {5,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {4,S}
12 H 0 {4,S}
13 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WILK, CERNANSKY, PITZ, AND WESTBROOK, C&F 1988.
CFG assumes HOCH2CH(OO*)CH3
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 430,
    reactant1 = 
"""
HOC3H6O2
1  O 0 {2,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {5,S} {10,S}
4  C 0 {3,S} {11,S} {12,S} {13,S}
5  O 0 {3,S} {6,S}
6  O 1 {5,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {4,S}
12 H 0 {4,S}
13 H 0 {4,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12500000000.0, 's^-1'), n=0, Ea=(18900, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 431,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 432,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 433,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+20, 'cm^3/(mol*s)'),
        n = -1.56,
        Ea = (26330, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!!!PRESSURE DEPENDANCE!!!!!!!!!!!!!!!!!!!!!!!!!!
!91TSA RRKM 0.1 ATM
!C3H5-A+OH = C2H3CHO+H+H              5.30E+37 -6.71 29306.0  0.0 0.0 0.0
!91TSA RRKM 1 ATM
!C3H5-A+OH = C2H3CHO+H+H              4.20E+32 -5.16 30126.0   0.0 0.0 0.0
!91TSA RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 434,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 435,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.18e+21, 'cm^3/(mol*s)'),
        n = -2.85,
        Ea = (30755, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!!!PRESSURE DEPENDANCE!!!!!!!!!!!!!!!!!!!!!!!!!!
!93BOZ/DEA RRKM 1 ATM
!C3H5-A+O2 = C3H4-A+HO2                  4.99E+15 -1.40 22428.0    0.0 0.0 0.0
!93BOZ/DEA RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 436,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7140000000000000.0, 'cm^3/(mol*s)'),
        n = -1.21,
        Ea = (21046, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!!!PRESSURE DEPENDANCE!!!!!!!!!!!!!!!!!!!!!!!!!!
!93BOZ/DEA RRKM 1 ATM
!C3H5-A+O2 = CH3CO+CH2O                  1.19E+15 -1.01 20128.0  0.0 0.0 0.0
!93BOZ/DEA RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 437,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24700000000000.0, 'cm^3/(mol*s)'),
        n = -0.45,
        Ea = (23017, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!!!PRESSURE DEPENDANCE!!!!!!!!!!!!!!!!!!!!!!!!!!
!93BOZ/DEA RRKM 1 ATM
!C3H5-A+O2 = C2H3CHO+OH                  1.82E+13 -0.41 22859.0    0.0 0.0 0.0
!93BOZ/DEA RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 438,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 439,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-131, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 440,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.86e+53, 's^-1'), n=-12.81, Ea=(75883, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!!!PRESSURE DEPENDANCE!!!!!!!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H5-A = C3H5-T                      7.06E+56 -14.08 75868.0    0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C3H5-A = C3H5-T                      4.80E+55 -13.59 75949.0    0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 441,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.7e+48, 's^-1'), n=-11.73, Ea=(73700, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!!!PRESSURE DEPENDANCE!!!!!!!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H5-A = C3H5-S                      5.00E+51 -13.02 73300.0    0.0 0.0 0.0
!99DAV/LAW RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 442,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.04e+51, 'cm^3/(mol*s)'),
        n = -11.89,
        Ea = (36476, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!99DAV/LAW RRKM 100 ATM
!C3H5-A = C3H5-S                      4.86E+44 -9.84 73400.0  0.0 0.0 0.0

!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C2H2+CH3 = C3H5-A                      2.68E+53 -12.82 35730.0    0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C2H2+CH3 = C3H5-A                      3.64E+52 -12.46 36127.0   0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 443,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
C3H5O
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 444,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product2 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM DAGAUT, P, CATHONNET, M., AND BOETTNER, J-C,
!CST 71, 111(1990)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 445,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!//!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM DAGAUT, P, CATHONNET, M., AND BOETTNER, J-C,
!CST 71, 111(1990)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 446,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM DAGAUT, P, CATHONNET, M., AND BOETTNER, J-C,
!CST 71, 111(1990)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 447,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84300000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-262, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!WANG
!J. PHYS. CHEM. REF. DATA 20, 221-273, (1991)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 448,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H5O
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!!!!!UNCOMMENT WHEN MECH USED AS BASE FOR AROMATIC MECH!!!!!!!!!!
!ZIEGLER ET AL. J. ANAL.APPLY.PYROLYSIS 73 212-230 (2005)
!C3H5-A+C2H2 = C*CCJC*C                  1.0E+12 0.0 6883.4  0.0 0.0 0.0

!ZIEGLER ET AL. J. ANAL.APPLY.PYROLYSIS 73 212-230 (2005)
!C3H5-A+C2H3 = C5H6+H+H                  1.6E+35 -14.0 61137.7  0.0 0.0 0.0

!ZIEGLER ET AL. J. ANAL.APPLY.PYROLYSIS 73 212-230 (2005)
!C3H5-A+C3H3 = C6H6+H+H                  5.6E+20 -2.54 1696.9  0.0 0.0 0.0

!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 449,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+38, 'cm^3/(mol*s)'),
        n = -8.21,
        Ea = (17100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C2H2+CH3 = C3H5-S                      3.20E+35 -7.76 13300.0    0.0 0.0 0.0
!99DAV/LAW RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 450,
    reactant1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3340000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!99DAV/LAW RRKM 100 ATM
!C2H2+CH3 = C3H5-S                      1.40E+39 -8.06 20200.0  0.0 0.0 0.0

!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 451,
    reactant1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 452,
    reactant1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!//!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 453,
    reactant1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 454,
    reactant1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 455,
    reactant1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 456,
    reactant1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 457,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.31e+25, 'cm^3/(mol*s)'),
        n = -5.06,
        Ea = (21150, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C2H2+CH3 = C3H5-T                      4.99E+22 -4.39 18850.0  0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C2H2+CH3 = C3H5-T                      6.00E+23 -4.60 19571.0  0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 458,
    reactant1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.1e+52, 's^-1'), n=-13.37, Ea=(57200, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H5-T = C3H5-S                      1.50E+48 -12.71 53900.0  0.0 0.0 0.0
!99DAV/LAW RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 459,
    reactant1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3340000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!99DAV/LAW RRKM 100 ATM
!C3H5-T = C3H5-S                      5.80E+51 -12.43 59200.0  0.0 0.0 0.0

!//!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 460,
    reactant1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 461,
    reactant1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 462,
    reactant1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 463,
    reactant1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 464,
    reactant1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 465,
    reactant1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 466,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (92000000000.0, 'cm^3/(mol*s)'),
        n = 0.54,
        Ea = (23950, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C2H2+CH3 = C3H4-A+H                  5.14E+09 0.86 22153.0  0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C2H2+CH3 = C3H4-A+H                  1.33E+10 0.75 22811.0  0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 467,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1300000.0, 'cm^3/(mol*s)'), n=2, Ea=(5500, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 468,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+31, 'cm^3/(mol*s)'),
        n = -6.23,
        Ea = (18700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H4-A+H = C3H5-S                      5.40E+29 -6.09 16300.0    0.0 0.0 0.0
!99DAV/LAW RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 469,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.98e+44, 'cm^3/(mol*s)'),
        n = -9.7,
        Ea = (14032, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!99DAV/LAW RRKM 100 ATM
!C3H4-A+H = C3H5-S                      3.20E+31 -5.88 21500.0  0.0 0.0 0.0

!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H4-A+H = C3H5-T                      9.46E+42 -9.43 11190.0  0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C3H4-A+H = C3H5-T                      8.47E+43 -9.59 12462.0  0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 470,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.34e+54, 'cm^3/(mol*s)'),
        n = -12.09,
        Ea = (26187, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H4-A+H = C3H5-A                      1.52E+59 -13.54 26949.0  0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C3H4-A+H = C3H5-A                      3.78E+57 -12.98 26785.0  0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 471,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 472,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5300000.0, 'cm^3/(mol*s)'), n=2, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 473,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!//!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 474,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 475,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product2 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (500000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (64746.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!ZIEGLER ET AL. J. ANAL.APPLY.PYROLYSIS 73 212-230 (2005)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 476,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM DAGAUT, P, CATHONNET, M., AND BOETTNER, J-C,
!CST 71, 111(1990)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 477,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product1 = 
"""
CC3H4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 C 0 {1,S} {2,D} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.92e+40, 's^-1'), n=-8.69, Ea=(68706, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!!!!!UNCOMMENT WHEN MECH USED AS BASE FOR AROMATIC MECH!!!!!!!!!!
!ZIEGLER ET AL. J. ANAL.APPLY.PYROLYSIS 73 212-230 (2005)
!C3H4-A+C3H3 = C6H6+H                  1.4E+12 0.0 9990.4  0.0 0.0 0.0

!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM KINF
!C3H4-P = CC3H4                          1.73E+12 0.31 60015.0   0.0 0.0 0.0
!99DAV/LAW RRKM 0.4 ATM
!C3H4-P = CC3H4                          2.84E+45 -10.45 69284.0   0.0 0.0 0.0
!99DAV/LAW RRKM 1 ATM
!C3H4-P = CC3H4                          1.20E+44 -9.92 69250.0   0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C3H4-P = CC3H4                          5.47E+42 -9.43 69089.0  0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 478,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.12e+58, 's^-1'), n=-13.07, Ea=(92680, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 0.4 ATM
!C3H4-P = C3H4-A                      5.81E+62 -14.63 91211.0    0.0 0.0 0.0
!99DAV/LAW RRKM 1 ATM
!C3H4-P = C3H4-A                      5.15E+60 -13.93 91117.0     0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C3H4-P = C3H4-A                      7.64E+59 -13.59 91817.0   0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 479,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+18, 'cm^3/(mol*s)'),
        n = -1.01,
        Ea = (11523, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H4-P+H = C3H4-A+H                  6.27E+17 -0.91 10079.0   0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C3H4-P+H = C3H4-A+H                  1.50E+18 -1.00 10756.0    0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 480,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5-T
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 C 0 {2,D} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.62e+47, 'cm^3/(mol*s)'),
        n = -10.55,
        Ea = (15910, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H4-P+H = C3H5-T                      1.66E+47 -10.58 13690.0    0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C3H4-P+H = C3H5-T                      5.04E+47 -10.61 14707.0  0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 481,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5-S
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 C 1 {2,D} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+34, 'cm^3/(mol*s)'), n=-6.88, Ea=(8900, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H4-P+H = C3H5-S                      5.50E+28 -5.74 4300.0   0.0 0.0 0.0
!99DAV/LAW RRKM 10 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 482,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.02e+59, 'cm^3/(mol*s)'),
        n = -13.89,
        Ea = (33953, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!99DAV/LAW RRKM 100 ATM
!C3H4-P+H = C3H5-S                      9.70E+37 -7.63 13800.0  0.0 0.0 0.0

!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C3H4-P+H = C3H5-A                      4.91E+60 -14.37 31644.0   0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C3H4-P+H = C3H5-A                      3.04E+60 -14.19 32642.0   0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 483,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1300000.0, 'cm^3/(mol*s)'), n=2, Ea=(5500, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!//!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 484,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6140000.0, 'cm^3/(mol*s)'),
        n = 1.74,
        Ea = (10450, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 485,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 486,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 487,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1000000.0, 'cm^3/(mol*s)'), n=2, Ea=(100, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 488,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
3 H 0 {1,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 489,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 490,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (251000000000.0, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (15453, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM 1 ATM
!C2H2+CH3 = C3H4-P+H                  2.56E+09 1.10 13644.0   0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!C2H2+CH3 = C3H4-P+H                  2.07E+10 0.85 14415.0  0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 491,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM DAGAUT, P, CATHONNET, M., AND BOETTNER, J-C,
!CST 71, 111(1990)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 492,
    reactant1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM DAGAUT, P, CATHONNET, M., AND BOETTNER, J-C,
!CST 71, 111(1990)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 493,
    reactant1 = 
"""
CC3H4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 C 0 {1,S} {2,D} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.33e+41, 's^-1'), n=-8.93, Ea=(50475, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
!!!!!!!!!!!!! PRESSURE DEPENDANCE !!!!!!!!!!!!!!!!!!!!!
!99DAV/LAW RRKM INF
!CC3H4 = C3H4-A                          1.98E+12 0.56 42240.0   0.0 0.0 0.0
!99DAV/LAW RRKM 0.4 ATM
!CC3H4 = C3H4-A                          7.59E+40 -9.07 48831.0   0.0 0.0 0.0
!99DAV/LAW RRKM 1 ATM
!CC3H4 = C3H4-A                          4.89E+41 -9.17 49594.0  0.0 0.0 0.0
!99DAV/LAW RRKM 2 ATM
!CC3H4 = C3H4-A                          8.81E+41 -9.15 50073.0  0.0 0.0 0.0
!99DAV/LAW RRKM 5 ATM
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 494,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 495,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 496,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 497,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al is this: http://dx.doi.org/10.1002/1097-4601(2000)32:10%3C589::AID-KIN2%3E3.0.CO;2-U
For its C3 rates it cites these:
[1] Davis, S. G.; Law, C. K.; Wang, H. Twenty-Seventh Symposium (International) on Combustion; The Combustion Institute: Pittsburgh, PA, 1998; pp 305-312.
[2] Davis, S. G.; Law, C. K.; Wang, H. J Phys Chem A 1999, 103, 5889. doi:10.1021/jp982762a
[3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
The last of these has the above rate attributed to [40] Pauwels, J-F., Volponi, J. V., and Miller, J. A., Com-bust. Sci. Technol., 110 -111:249-276 (1995).

!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 498,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 499,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2868, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al. attribute this to [3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
doi:10.1016/S0010-2180(99)00070-X attributes this to [41] Miller, J. A., and Bowman, C. T., Prog. Energy Combust. Sci. 15:287-338 (1989). doi:10.1016/0360-1285(89)90017-8
doi:10.1016/0360-1285(89)90017-8 have it as reaction 121, but I can't see where they get it from (if anywhere) nor any clue what it is.

!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 500,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 501,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 502,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 503,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 504,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H4-P
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,T}
3 C 0 {2,T} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 505,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product1 = 
"""
C4H4
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,T}
4 C 0 {3,T} {8,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 506,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C4H3-I
1 C 0 {2,T} {5,S}
2 C 0 {1,T} {3,S}
3 C 1 {2,S} {4,D}
4 C 0 {3,D} {6,S} {7,S}
5 H 0 {1,S}
6 H 0 {4,S}
7 H 0 {4,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 507,
    reactant1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C4H4
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,T}
4 C 0 {3,T} {8,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 508,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!!!----CFG


!!!!!UNCOMMENT WHEN MECH USED AS BASE FOR AROMATIC MECH!!!!!!!!!!
!LASKIN ET AL. IJCK 32 589-614 2000
!C3H3+C3H3 = C6H5+H                      5.000E+12 0.0 0.0   0.0 0.0 0.0
!C3H3+C3H3 = C6H6                      2.000E+12 0.0 0.0   0.0 0.0 0.0
!C3H3+C4H6 = C6H5CH3+H                  6.53E+5 1.28 -4611.0   0.0 0.0 0.0

!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 509,
    reactant1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H3
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 C 1 {2,D} {6,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 510,
    reactant1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (68000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al. attribute this to [3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
doi:10.1016/S0010-2180(99)00070-X atrributes this to [estimated]!

!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 511,
    reactant1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (68000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al. attribute this to [3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
doi:10.1016/S0010-2180(99)00070-X atrributes this to [43] Warnatz,J., Bockhorn,H., Moser,A., and Wenz,H. W., Nineteenth Symposium (International) on Combustion, The Combustion Institute, Pittsburgh, 1983, p.197.

!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 512,
    reactant1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al. attribute this to [3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
doi:10.1016/S0010-2180(99)00070-X atrributes this to [43] Warnatz,J., Bockhorn,H., Moser,A., and Wenz,H. W., Nineteenth Symposium (International) on Combustion, The Combustion Institute, Pittsburgh, 1983, p.197.

!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 513,
    reactant1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C4H2
1 C 0 {2,S} {3,T}
2 C 0 {1,S} {4,T}
3 C 0 {1,T} {5,S}
4 C 0 {2,T} {6,S}
5 H 0 {3,S}
6 H 0 {4,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al. attribute this to [3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
doi:10.1016/S0010-2180(99)00070-X atrributes this to [40] Pauwels, J-F., Volponi, J. V., and Miller, J. A., Combust. Sci. Technol., 110 -111:249-276 (1995).

!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 514,
    reactant1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
C4H3-N
1 C 0 {2,T} {5,S}
2 C 0 {1,T} {3,S}
3 C 0 {2,S} {4,D} {6,S}
4 C 1 {3,D} {7,S}
5 H 0 {1,S}
6 H 0 {3,S}
7 H 0 {4,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al. attribute this to [3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
doi:10.1016/S0010-2180(99)00070-X atrributes this to [32] Wang, H., and Frenklach, M., Combust. Flame 110:173-221 (1997).

!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 515,
    reactant1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C4H4
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,T}
4 C 0 {3,T} {8,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al. attribute this to [3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
doi:10.1016/S0010-2180(99)00070-X atrributes this to [32] Wang, H., and Frenklach, M., Combust. Flame 110:173-221 (1997).

!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 516,
    reactant1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product1 = 
"""
C4H3-N
1 C 0 {2,T} {5,S}
2 C 0 {1,T} {3,S}
3 C 0 {2,S} {4,D} {6,S}
4 C 1 {3,D} {7,S}
5 H 0 {1,S}
6 H 0 {3,S}
7 H 0 {4,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al. attribute this to [3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
doi:10.1016/S0010-2180(99)00070-X atrributes this to [32] Wang, H., and Frenklach, M., Combust. Flame 110:173-221 (1997).

!LASKIN ET AL. IJCK 32 589-614 2000
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 517,
    reactant1 = 
"""
C3H2
1 C 0 {2,D} {3,D}
2 C 1 {1,D} {4,S}
3 C 1 {1,D} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Laskin et al. attribute this to [3] Davis, S. G.; Law, C. K.; Wang, H. Combust Flame 1999, 119, 375. doi:10.1016/S0010-2180(99)00070-X
doi:10.1016/S0010-2180(99)00070-X atrributes this to [32] Wang, H., and Frenklach, M., Combust. Flame 110:173-221 (1997).

!//!//!//!//!UNCOMMENT WHEN MECH USED AS BASE FOR AROMATIC MECH//!//!//!//!//!//!//!//!//!//!
!LASKIN ET AL. IJCK 32 589-614 2000
!C3H2+C3H3 = C6H5                      7.00E+12 0.0 0.0   0.0 0.0 0.0

!HEALY ET AL C&F, 155: 451 461 (2008)
CFG not sure about C3H2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 518,
    reactant1 = 
"""
CH3CHCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,D} {8,S}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1730000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 519,
    reactant1 = 
"""
CH3CHCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,D} {8,S}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 520,
    reactant1 = 
"""
CH3CHCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,D} {8,S}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1459, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 521,
    reactant1 = 
"""
CH3CHCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,D} {8,S}
3 C 0 {2,D} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-437, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 522,
    reactant1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 523,
    reactant1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 524,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 525,
    reactant1 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 526,
    reactant1 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 527,
    reactant1 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7540000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 528,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO CH2O+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 529,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product1 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!HALF OF CH2O+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 530,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO CH2O+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 531,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product1 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!HALF OF CH2O+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 532,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3275, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 533,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3275, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 534,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO C2H4+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 535,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (30430, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO C2H4+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 536,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19360, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO CH3OH+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 537,
    reactant1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    reactant2 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19360, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO CH3OH+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 538,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!HALF OF CH2O+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 539,
    reactant1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C2H3CO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 C 1 {1,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!HALF OF CH2O+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 540,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24640, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO CH4+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 541,
    reactant1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (24640, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ANALOGY TO CH4+HO2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 542,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 543,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 544,
    reactant1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
! TSANG AND HAMPSON, JPC REF. DATA, 15:1087 (1986)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 545,
    reactant1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (26030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
! TSANG AND HAMPSON, JPC REF. DATA, 15:1087 (1986)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 546,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product1 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 547,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product1 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20460, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 548,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    product1 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 549,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    product1 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product2 = 
"""
C2H5CO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 550,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
CH3CO2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 1 {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 551,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH3CO3
1 C 0 {2,S} {6,S} {7,S} {8,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 0 {2,S} {5,S}
5 O 1 {4,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {1,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
CH3CO2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 1 {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 552,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 553,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5O2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,S} {8,S} {9,S}
3 O 0 {2,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {2,S}
9 H 0 {2,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 554,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product2 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product3 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 555,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product2 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product3 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 556,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 557,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 558,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 559,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 560,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 561,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
C3H5O
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 562,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 563,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
C2H5O
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 564,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
IC3H7
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 1 {1,S} {3,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 565,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
NC3H7
1  C 1 {2,S} {4,S} {5,S}
2  C 0 {1,S} {3,S} {6,S} {7,S}
3  C 0 {2,S} {8,S} {9,S} {10,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {2,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 566,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    reactant2 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
C3H5O
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FROM GLAUDE,P.A.,MELIUS,C.,PITZ,W.J.,AND WESTBROOK,C.K.,
!"CHEMICAL KINETICS OF ORGANOPHOSPHORUS COMPOUNDS", PROCEEDINGS OF THE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 567,
    reactant1 = 
"""
NC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 568,
    reactant1 = 
"""
IC3H7O2H
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {13,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9450000000000000.0, 's^-1'),
        n = 0,
        Ea = (42600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 569,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3496, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 570,
    reactant1 = 
"""
C2H5CHO
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,D} {10,S}
4  O 0 {3,D}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
NC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 1 {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6260, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 571,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9256, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 572,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7270, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 573,
    reactant1 = 
"""
IC3H7O
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 1 {2,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9090000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (390, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BALLA, NELSON, AND MCDONALD,
!CHEM. PHYSICS, 99, 323 (1985)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 574,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C3H6OOH1-2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 {1,S} {3,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(600000000000.0, 's^-1'), n=0, Ea=(26850, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 575,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C3H6OOH1-3
1  C 1 {2,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(112500000000.0, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 576,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C3H6OOH2-1
1  C 1 {2,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1800000000000.0, 's^-1'), n=0, Ea=(29400, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 577,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+35, 's^-1'), n=-6.96, Ea=(48880, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BOZZELLI, J. AND DEAN, A, 1992
CFG thinks C3H6OOH2-2 isn't stable (beta-hydroperoyl-radical)
Replace this product with the product of C3H6OOH2-2 decomp
IC3H7O2 = C3H6OOH2-2                     1.230E+35 -6.96 4.888E+04   0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 578,
    reactant1 = 
"""
C3H6OOH1-2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 {1,S} {3,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    product1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(600000000000.0, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 579,
    reactant1 = 
"""
C3H6OOH1-3
1  C 1 {2,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    product1 = 
"""
C3H6O1-3
1  O 0 {2,S} {3,S}
2  C 0 {1,S} {4,S} {5,S} {6,S}
3  C 0 {1,S} {4,S} {7,S} {8,S}
4  C 0 {2,S} {3,S} {9,S} {10,S}
5  H 0 {2,S}
6  H 0 {2,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(75000000000.0, 's^-1'), n=0, Ea=(15250, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
CFG assumes C3H6O1-3 is propen-2-ol
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 580,
    reactant1 = 
"""
C3H6OOH2-1
1  C 1 {2,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    product1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(600000000000.0, 's^-1'), n=0, Ea=(22000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 581,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H6OOH1-2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 {1,S} {3,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 582,
    reactant1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
C3H6OOH2-1
1  C 1 {2,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11750, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 583,
    reactant1 = 
"""
C3H6OOH1-3
1  C 1 {2,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product3 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3035000000000000.0, 's^-1'),
        n = -0.79,
        Ea = (27400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 584,
    reactant1 = 
"""
C3H6OOH2-1
1  C 1 {2,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    product1 = 
"""
C2H3OOH
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 O 0 {2,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.54e+27, 's^-1'), n=-5.14, Ea=(38320, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BOZZELLI AND PITZ, 1995
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 585,
    reactant1 = 
"""
C3H6OOH1-2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 {1,S} {3,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.31e+33, 's^-1'), n=-7.01, Ea=(48120, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BOZZELLI AND PITZ, 1995
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 586,
    reactant1 = 
"""
C3H6OOH1-2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 1 {1,S} {3,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C3H6OOH1-2O2
1  C 0 {2,S} {8,S} {9,S} {10,S}
2  C 0 {1,S} {3,S} {6,S} {11,S}
3  C 0 {2,S} {4,S} {12,S} {13,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {14,S}
6  O 0 {2,S} {7,S}
7  O 1 {6,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {1,S}
11 H 0 {2,S}
12 H 0 {3,S}
13 H 0 {3,S}
14 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
CFG thinks C3H6OOH2-2 isn't stable (beta-hydroperoxyl-radical)
C3H6OOH2-2 = CH3COCH3+OH                 9.000E+14 0.00 1.500E+03   0.0 0.0 0.0

!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 587,
    reactant1 = 
"""
C3H6OOH1-3
1  C 1 {2,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {8,S} {9,S}
3  C 0 {2,S} {4,S} {10,S} {11,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C3H6OOH1-3O2
1  O 0 {2,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  C 0 {3,S} {5,S} {11,S} {12,S}
5  C 0 {4,S} {6,S} {13,S} {14,S}
6  O 0 {5,S} {7,S}
7  O 1 {6,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {4,S}
12 H 0 {4,S}
13 H 0 {5,S}
14 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 588,
    reactant1 = 
"""
C3H6OOH2-1
1  C 1 {2,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C3H6OOH2-1O2
1  C 0 {2,S} {8,S} {9,S} {10,S}
2  C 0 {1,S} {3,S} {6,S} {11,S}
3  C 0 {2,S} {4,S} {12,S} {13,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  O 0 {2,S} {7,S}
7  O 0 {6,S} {14,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {1,S}
11 H 0 {2,S}
12 H 0 {3,S}
13 H 0 {3,S}
14 H 0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4520000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 589,
    reactant1 = 
"""
C3H6OOH1-2O2
1  C 0 {2,S} {8,S} {9,S} {10,S}
2  C 0 {1,S} {3,S} {6,S} {11,S}
3  C 0 {2,S} {4,S} {12,S} {13,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {14,S}
6  O 0 {2,S} {7,S}
7  O 1 {6,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {1,S}
11 H 0 {2,S}
12 H 0 {3,S}
13 H 0 {3,S}
14 H 0 {5,S}
""",
    product1 = 
"""
C3KET12
1  C 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 {1,S} {3,S} {4,S} {10,S}
3  C 0 {2,S} {6,D} {11,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {12,S}
6  O 0 {3,D}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(600000000000.0, 's^-1'), n=0, Ea=(26400, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 590,
    reactant1 = 
"""
C3H6OOH1-3O2
1  O 0 {2,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  C 0 {3,S} {5,S} {11,S} {12,S}
5  C 0 {4,S} {6,S} {13,S} {14,S}
6  O 0 {5,S} {7,S}
7  O 1 {6,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {4,S}
12 H 0 {4,S}
13 H 0 {5,S}
14 H 0 {5,S}
""",
    product1 = 
"""
C3KET13
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {7,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  C 0 {3,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 0 {5,S} {12,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
12 H 0 {6,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(75000000000.0, 's^-1'), n=0, Ea=(21400, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 591,
    reactant1 = 
"""
C3H6OOH2-1O2
1  C 0 {2,S} {8,S} {9,S} {10,S}
2  C 0 {1,S} {3,S} {6,S} {11,S}
3  C 0 {2,S} {4,S} {12,S} {13,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  O 0 {2,S} {7,S}
7  O 0 {6,S} {14,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {1,S}
11 H 0 {2,S}
12 H 0 {3,S}
13 H 0 {3,S}
14 H 0 {7,S}
""",
    product1 = 
"""
C3KET21
1  C 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 {1,S} {3,S} {4,D}
3  C 0 {2,S} {5,S} {10,S} {11,S}
4  O 0 {2,D}
5  O 0 {3,S} {6,S}
6  O 0 {5,S} {12,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {6,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(300000000000.0, 's^-1'), n=0, Ea=(23850, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 592,
    reactant1 = 
"""
C3H6OOH2-1O2
1  C 0 {2,S} {8,S} {9,S} {10,S}
2  C 0 {1,S} {3,S} {6,S} {11,S}
3  C 0 {2,S} {4,S} {12,S} {13,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  O 0 {2,S} {7,S}
7  O 0 {6,S} {14,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {1,S}
11 H 0 {2,S}
12 H 0 {3,S}
13 H 0 {3,S}
14 H 0 {7,S}
""",
    product1 = 
"""
C3H51-2,3OOH
1  C 1 {2,S} {8,S} {9,S}
2  C 0 {1,S} {3,S} {6,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  O 0 {2,S} {7,S}
7  O 0 {6,S} {14,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
14 H 0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(112500000000.0, 's^-1'), n=0, Ea=(24400, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 593,
    reactant1 = 
"""
C3H6OOH1-2O2
1  C 0 {2,S} {8,S} {9,S} {10,S}
2  C 0 {1,S} {3,S} {6,S} {11,S}
3  C 0 {2,S} {4,S} {12,S} {13,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {14,S}
6  O 0 {2,S} {7,S}
7  O 1 {6,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {1,S}
11 H 0 {2,S}
12 H 0 {3,S}
13 H 0 {3,S}
14 H 0 {5,S}
""",
    product1 = 
"""
C3H51-2,3OOH
1  C 1 {2,S} {8,S} {9,S}
2  C 0 {1,S} {3,S} {6,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  O 0 {2,S} {7,S}
7  O 0 {6,S} {14,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
14 H 0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(900000000000.0, 's^-1'), n=0, Ea=(29400, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 594,
    reactant1 = 
"""
C3H51-2,3OOH
1  C 1 {2,S} {8,S} {9,S}
2  C 0 {1,S} {3,S} {6,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {13,S}
6  O 0 {2,S} {7,S}
7  O 0 {6,S} {14,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
13 H 0 {5,S}
14 H 0 {7,S}
""",
    product1 = 
"""
AC3H5OOH
1  C 0 {2,D} {6,S} {7,S}
2  C 0 {1,D} {3,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {11,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {5,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25600000000000.0, 's^-1'),
        n = -0.49,
        Ea = (17770, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BOZZELLI AND PITZ, 1993
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 595,
    reactant1 = 
"""
C3H6OOH1-3O2
1  O 0 {2,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  C 0 {3,S} {5,S} {11,S} {12,S}
5  C 0 {4,S} {6,S} {13,S} {14,S}
6  O 0 {5,S} {7,S}
7  O 1 {6,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {4,S}
12 H 0 {4,S}
13 H 0 {5,S}
14 H 0 {5,S}
""",
    product1 = 
"""
C3H52-1,3OOH
1  O 0 {2,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  C 1 {3,S} {5,S} {11,S}
5  C 0 {4,S} {6,S} {12,S} {13,S}
6  O 0 {5,S} {7,S}
7  O 0 {6,S} {14,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {4,S}
12 H 0 {5,S}
13 H 0 {5,S}
14 H 0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(600000000000.0, 's^-1'), n=0, Ea=(26850, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 596,
    reactant1 = 
"""
C3H52-1,3OOH
1  O 0 {2,S} {8,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  C 1 {3,S} {5,S} {11,S}
5  C 0 {4,S} {6,S} {12,S} {13,S}
6  O 0 {5,S} {7,S}
7  O 0 {6,S} {14,S}
8  H 0 {1,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {4,S}
12 H 0 {5,S}
13 H 0 {5,S}
14 H 0 {7,S}
""",
    product1 = 
"""
AC3H5OOH
1  C 0 {2,D} {6,S} {7,S}
2  C 0 {1,D} {3,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {11,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {5,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (115000000000000.0, 's^-1'),
        n = -0.63,
        Ea = (17250, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!BOZZELLI AND PITZ, 1993
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 597,
    reactant1 = 
"""
C3KET12
1  C 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 {1,S} {3,S} {4,S} {10,S}
3  C 0 {2,S} {6,D} {11,S}
4  O 0 {2,S} {5,S}
5  O 0 {4,S} {12,S}
6  O 0 {3,D}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {5,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9450000000000000.0, 's^-1'),
        n = 0,
        Ea = (43000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 598,
    reactant1 = 
"""
C3KET13
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {7,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  C 0 {3,S} {5,S} {10,S} {11,S}
5  O 0 {4,S} {6,S}
6  O 0 {5,S} {12,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
12 H 0 {6,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2CHO
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 599,
    reactant1 = 
"""
C3KET21
1  C 0 {2,S} {7,S} {8,S} {9,S}
2  C 0 {1,S} {3,S} {4,D}
3  C 0 {2,S} {5,S} {10,S} {11,S}
4  O 0 {2,D}
5  O 0 {3,S} {6,S}
6  O 0 {5,S} {12,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {1,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {6,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 600,
    reactant1 = 
"""
C3H5O
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
AC3H5OOH
1  C 0 {2,D} {6,S} {7,S}
2  C 0 {1,D} {3,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {3,S} {5,S}
5  O 0 {4,S} {11,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 601,
    reactant1 = 
"""
C3H5O
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 's^-1'),
        n = 0,
        Ea = (29100, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 602,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H5O
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 603,
    reactant1 = 
"""
C3H5O
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
C2H3CHO
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!ACETALDEHYDE ANALOG
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 604,
    reactant1 = 
"""
C2H3OOH
1 C 0 {2,D} {5,S} {6,S}
2 C 0 {1,D} {3,S} {7,S}
3 O 0 {2,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    product1 = 
"""
CH2CHO
1 C 1 {2,S} {4,S} {5,S}
2 C 0 {1,S} {3,D} {6,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (840000000000000.0, 's^-1'),
        n = 0,
        Ea = (43000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!PITZ ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 605,
    reactant1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (600000000000000.0, 's^-1'),
        n = 0,
        Ea = (60000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!FLOWERS, M. C.,
!J. CHEM. SOC. FAR. TRANS. I 73, 1927 (1977)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 606,
    reactant1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 607,
    reactant1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26300000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 608,
    reactant1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 609,
    reactant1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 610,
    reactant1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 611,
    reactant1 = 
"""
C3H6O1-2
1  C 0 {2,S} {5,S} {6,S} {7,S}
2  C 0 {1,S} {3,S} {4,S} {8,S}
3  C 0 {2,S} {4,S} {9,S} {10,S}
4  O 0 {2,S} {3,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 612,
    reactant1 = 
"""
C3H6O1-3
1  O 0 {2,S} {3,S}
2  C 0 {1,S} {4,S} {5,S} {6,S}
3  C 0 {1,S} {4,S} {7,S} {8,S}
4  C 0 {2,S} {3,S} {9,S} {10,S}
5  H 0 {2,S}
6  H 0 {2,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (600000000000000.0, 's^-1'),
        n = 0,
        Ea = (60000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!WESTBROOK AND PITZ ESTIMATE (1983)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 613,
    reactant1 = 
"""
C3H6O1-3
1  O 0 {2,S} {3,S}
2  C 0 {1,S} {4,S} {5,S} {6,S}
3  C 0 {1,S} {4,S} {7,S} {8,S}
4  C 0 {2,S} {3,S} {9,S} {10,S}
5  H 0 {2,S}
6  H 0 {2,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!PITZ ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 614,
    reactant1 = 
"""
C3H6O1-3
1  O 0 {2,S} {3,S}
2  C 0 {1,S} {4,S} {5,S} {6,S}
3  C 0 {1,S} {4,S} {7,S} {8,S}
4  C 0 {2,S} {3,S} {9,S} {10,S}
5  H 0 {2,S}
6  H 0 {2,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!PITZ ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 615,
    reactant1 = 
"""
C3H6O1-3
1  O 0 {2,S} {3,S}
2  C 0 {1,S} {4,S} {5,S} {6,S}
3  C 0 {1,S} {4,S} {7,S} {8,S}
4  C 0 {2,S} {3,S} {9,S} {10,S}
5  H 0 {2,S}
6  H 0 {2,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26300000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!PITZ ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 616,
    reactant1 = 
"""
C3H6O1-3
1  O 0 {2,S} {3,S}
2  C 0 {1,S} {4,S} {5,S} {6,S}
3  C 0 {1,S} {4,S} {7,S} {8,S}
4  C 0 {2,S} {3,S} {9,S} {10,S}
5  H 0 {2,S}
6  H 0 {2,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!PITZ ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 617,
    reactant1 = 
"""
C3H6O1-3
1  O 0 {2,S} {3,S}
2  C 0 {1,S} {4,S} {5,S} {6,S}
3  C 0 {1,S} {4,S} {7,S} {8,S}
4  C 0 {2,S} {3,S} {9,S} {10,S}
5  H 0 {2,S}
6  H 0 {2,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!PITZ ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 618,
    reactant1 = 
"""
C3H6O1-3
1  O 0 {2,S} {3,S}
2  C 0 {1,S} {4,S} {5,S} {6,S}
3  C 0 {1,S} {4,S} {7,S} {8,S}
4  C 0 {2,S} {3,S} {9,S} {10,S}
5  H 0 {2,S}
6  H 0 {2,S}
7  H 0 {3,S}
8  H 0 {3,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product3 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!PITZ ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 619,
    reactant1 = 
"""
IC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {4,S} {9,S}
3  C 0 {2,S} {10,S} {11,S} {12,S}
4  O 0 {2,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {3,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.015e+43, 's^-1'), n=-9.41, Ea=(41490, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 620,
    reactant1 = 
"""
NC3H7O2
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  C 0 {2,S} {4,S} {11,S} {12,S}
4  O 0 {3,S} {5,S}
5  O 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {3,S}
12 H 0 {3,S}
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.044e+38, 's^-1'), n=-8.11, Ea=(40490, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 621,
    reactant1 = 
"""
CH2CCH2OH
1 C 0 {2,D} {5,S} {6,S}
2 C 1 {1,D} {3,S}
3 C 0 {2,S} {4,S} {7,S} {8,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product1 = 
"""
C3H5OH
1  C 0 {2,D} {5,S} {6,S}
2  C 0 {1,D} {3,S} {7,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3010000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2583, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
-----------------
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 622,
    reactant1 = 
"""
C3H5OH
1  C 0 {2,D} {5,S} {6,S}
2  C 0 {1,D} {3,S} {7,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CCH2OH
1 C 0 {2,D} {5,S} {6,S}
2 C 1 {1,D} {3,S}
3 C 0 {2,S} {4,S} {7,S} {8,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {4,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5060000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5960, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 623,
    reactant1 = 
"""
C3H5OH
1  C 0 {2,D} {5,S} {6,S}
2  C 0 {1,D} {3,S} {7,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CCH2OH
1 C 0 {2,D} {5,S} {6,S}
2 C 1 {1,D} {3,S}
3 C 0 {2,S} {4,S} {7,S} {8,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {4,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(390000, 'cm^3/(mol*s)'), n=2.5, Ea=(5821, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 624,
    reactant1 = 
"""
C3H5OH
1  C 0 {2,D} {5,S} {6,S}
2  C 0 {1,D} {3,S} {7,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2CCH2OH
1 C 0 {2,D} {5,S} {6,S}
2 C 1 {1,D} {3,S}
3 C 0 {2,S} {4,S} {7,S} {8,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {4,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60690, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 625,
    reactant1 = 
"""
C3H5OH
1  C 0 {2,D} {5,S} {6,S}
2  C 0 {1,D} {3,S} {7,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2CCH2OH
1 C 0 {2,D} {5,S} {6,S}
2 C 1 {1,D} {3,S}
3 C 0 {2,S} {4,S} {7,S} {8,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {4,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 626,
    reactant1 = 
"""
CH2CCH2OH
1 C 0 {2,D} {5,S} {6,S}
2 C 1 {1,D} {3,S}
3 C 0 {2,S} {4,S} {7,S} {8,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H5OH
1  C 0 {2,D} {5,S} {6,S}
2  C 0 {1,D} {3,S} {7,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  O 0 {3,S} {10,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
CH2CCH2OH+CH3 = IC4H7OH                  3.000E+13 0.00 0.000E+00    0.0 0.0 0.0

!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 627,
    reactant1 = 
"""
CH2CCH2OH
1 C 0 {2,D} {5,S} {6,S}
2 C 1 {1,D} {3,S}
3 C 0 {2,S} {4,S} {7,S} {8,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4335000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 628,
    reactant1 = 
"""
CH2CCH2OH
1 C 0 {2,D} {5,S} {6,S}
2 C 1 {1,D} {3,S}
3 C 0 {2,S} {4,S} {7,S} {8,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {4,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.163e+40, 's^-1'), n=-8.31, Ea=(45110, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 629,
    reactant1 = 
"""
C3H4-A
1 C 0 {3,D} {4,S} {5,S}
2 C 0 {3,D} {6,S} {7,S}
3 C 0 {1,D} {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2CCH2OH
1 C 0 {2,D} {5,S} {6,S}
2 C 1 {1,D} {3,S}
3 C 0 {2,S} {4,S} {7,S} {8,S}
4 O 0 {3,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!HEALY ET AL C&F, 155: 451 461 (2008)
!CURRAN ESTIMATE
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 630,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!METHYL FORMATE SUBMECHANISM, DOOLEY ET AL. IJCK 2009
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 631,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 632,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (665417, 'cm^3/(mol*s)'),
        n = 2.537,
        Ea = (6494.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 633,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8858000000000.0, 'cm^3/(mol*s)'),
        n = 0.054,
        Ea = (3340.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 634,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.291, 'cm^3/(mol*s)'), n=3.7, Ea=(6823.8, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 635,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56594.9, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (16594.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 636,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56594.9, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (16594.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 637,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4590000000.0, 'cm^3/(mol*s)'),
        n = 0.45,
        Ea = (4823.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 638,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (884347, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (4593.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 639,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15330000000000.0, 'cm^3/(mol*s)'),
        n = 0.0796,
        Ea = (51749.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 640,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(102500, 'cm^3/(mol*s)'), n=2.5, Ea=(18430, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 641,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 642,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 643,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OCHO
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56594.9, 'cm^3/(mol*s)'),
        n = 2.44,
        Ea = (16594.3, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 644,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (257664, 'cm^3/(mol*s)'),
        n = 2.52,
        Ea = (5736.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 645,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.22e+16, 'cm^3/(mol*s)'),
        n = -0.981,
        Ea = (4946.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 646,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.09212, 'cm^3/(mol*s)'),
        n = 3.69,
        Ea = (6052.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 647,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O2
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
CH3O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156602, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (16544.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 648,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156602, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (16544.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 649,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5270000000.0, 'cm^3/(mol*s)'),
        n = 0.83,
        Ea = (2912.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 650,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (245142, 'cm^3/(mol*s)'),
        n = 2.47,
        Ea = (4047.8, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 651,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3847000000000.0, 'cm^3/(mol*s)'),
        n = 0.113,
        Ea = (50759.6, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 652,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5400000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (17010, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 653,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 654,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 655,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
OCHO
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product2 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156602, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (16544.4, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 656,
    reactant1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    reactant2 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10400, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 657,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47600000.0, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (34700, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 658,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1550000.0, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (5730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 659,
    reactant1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (262000000000.0, 's^-1'),
        n = -0.03,
        Ea = (38178, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 660,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (389000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (22000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 661,
    reactant1 = 
"""
OCH2OCHO
1 O 1 {2,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {4,S}
4 C 0 {3,S} {5,D} {8,S}
5 O 0 {4,D}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    product1 = 
"""
HOCH2OCO
1 O 0 {2,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {4,S}
4 C 1 {3,S} {5,D}
5 O 0 {4,D}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(100000000000.0, 's^-1'), n=0, Ea=(14000, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 662,
    reactant1 = 
"""
HOCH2OCO
1 O 0 {2,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {4,S}
4 C 1 {3,S} {5,D}
5 O 0 {4,D}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product1 = 
"""
HOCH2O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 O 1 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.238e+19, 's^-1'), n=-2.02, Ea=(19690, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 663,
    reactant1 = 
"""
HOCH2OCO
1 O 0 {2,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {4,S}
4 C 1 {3,S} {5,D}
5 O 0 {4,D}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.413e+17, 's^-1'), n=-1.57, Ea=(22120, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 664,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
OCHO
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
OCH2OCHO
1 O 1 {2,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {4,S}
4 C 0 {3,S} {5,D} {8,S}
5 O 0 {4,D}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (389000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!CH2O+VINYL RAUK ET AL. IMPORTANT: DO NOT DISCARD IN SUBMECHANISM, THIS REACTION IS ALSO DESCRIBED IN DME OXIDATION.
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 665,
    reactant1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 666,
    reactant1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 667,
    reactant1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
HOOCH2OCHO
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {7,S}
3  O 0 {2,S} {4,S}
4  C 0 {3,S} {5,S} {8,S} {9,S}
5  O 0 {4,S} {6,S}
6  O 0 {5,S} {10,S}
7  H 0 {2,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Removed because RMG doesn't like CH3OC*OOOH ("forbidden by CO3")
CH3OCO  + HO2 = CH3OC*OOOH               7E12        0             -1000  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 668,
    reactant1 = 
"""
OCH2OCHO
1 O 1 {2,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {4,S}
4 C 0 {3,S} {5,D} {8,S}
5 O 0 {4,D}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HOOCH2OCHO
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {7,S}
3  O 0 {2,S} {4,S}
4  C 0 {3,S} {5,S} {8,S} {9,S}
5  O 0 {4,S} {6,S}
6  O 0 {5,S} {10,S}
7  H 0 {2,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1550000.0, 'cm^3/(mol*s)'),
        n = 2.41,
        Ea = (-4132, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!Reverse of NC3H7O2H = NC3H7O + OH  computed from forward e*pressions of Healy et al,
Removed because RMG doesn't like CH3OC*OO ("forbidden by CO3.") or CH3OC*OOOH ("forbidden by CO3")
CH3OC*OO + OH = CH3OC*OOOH               1.550E+06   2.41      -4.132E+03     0.0 0.0 0.0
!Reverse of NC3H7O2H = NC3H7O + OH  computed from forward e*pressions of Healy et al,
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 669,
    reactant1 = 
"""
CH3OCO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
OCH2OCHO
1 O 1 {2,S}
2 C 0 {1,S} {3,S} {6,S} {7,S}
3 O 0 {2,S} {4,S}
4 C 0 {3,S} {5,D} {8,S}
5 O 0 {4,D}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Removed because RMG doesn't like CH3OC*OO ("forbidden by CO3.")
CH2OCHO + CH3O  = CH3OC*OO + CH3         7E12        0.0           -1000  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 670,
    reactant1 = 
"""
CH2OCHO
1 C 1 {3,S} {5,S} {6,S}
2 C 0 {3,S} {4,D} {7,S}
3 O 0 {1,S} {2,S}
4 O 0 {2,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
OOCH2OCHO
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {7,S}
3 O 0 {2,S} {4,S}
4 C 0 {3,S} {5,S} {8,S} {9,S}
5 O 0 {4,S} {6,S}
6 O 1 {5,S}
7 H 0 {2,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Removed because RMG doesn't like CH3OC*OO ("forbidden by CO3.")
CO2 + CH3O = CH3OC*OO                    1.00E+11    0.0          9200.0   0.0 0.0 0.0
Removed because RMG doesn't like CH3OC*OOO ("forbidden by CO3")
CH3OCO + O2 = CH3OC*OOO                  4.50E+12    0.0             0.0   0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 671,
    reactant1 = 
"""
OCH2O2H
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 O 1 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
HOOCH2OC*O
1 O 0 {2,D}
2 C 1 {1,D} {3,S}
3 O 0 {2,S} {4,S}
4 C 0 {3,S} {5,S} {7,S} {8,S}
5 O 0 {4,S} {6,S}
6 O 0 {5,S} {9,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10800000.0, 'cm^3/(mol*s)'),
        n = 1.633,
        Ea = (5588, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Removed because RMG doesn't like CH3OC*OOO ("forbidden by CO3")
OOCH2OCHO = HOOCH2OC*O                   2.47E11     0.0           28900   0.0 0.0 0.0
CH3OC*OOO = CH2OC*OOOH                   7.41E11     0.0           28900   0.0 0.0 0.0
CFG thinks CH2O2H isn't stable
CH2O2H+CO2 = HOOCH2OC*O                  2.92E6      1.65          36591   0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 672,
    reactant1 = 
"""
OCHO
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
CHOOCO
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {6,S}
3 O 0 {2,S} {4,S}
4 C 1 {3,S} {5,D}
5 O 0 {4,D}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CFG thinks CH2O2H isn't stable
OH+CH2O  = CH2O2H                        2.30E+10    0.0           12900   0.0 0.0 0.0
CH2OC*OOOH => CH2O + CO2 + OH            3.801E+18  -1.47      3.736E+04   0.0 0.0 0.0
CH2OC*OOOH => CH2O + CO + HO2            3.801E+18  -1.47      3.736E+04   0.0 0.0 0.0
CH2OC*OOOH => CYOCH2OC*O + OH            7.50E+10    0.0         15250.0   0.0 0.0 0.0
HOOCH2OC*O => CYOCH2OC*O + OH            7.50E+10    0.0         15250.0   0.0 0.0 0.0
CH2OC*OOOH + O2 = OOCH2OC*OOOH           4.52E+12    0.0             0.0   0.0 0.0 0.0
HOOCH2OC*O + O2 = HOOCH2OC*OOO           7.54E+12    0.0             0.0   0.0 0.0 0.0
HOOCH2OC*OOO = O*CHOC*OOOH + OH          2.89E+10    0.0           21863   0.0 0.0 0.0
O*CHOC*OOOH => CO2 + OCHO + OH           1.050E+16   0.0         41600.0   0.0 0.0 0.0
CYOCH2OC*O + H = CHOOCO + H2             4.800E+08   1.5          2005.0   0.0 0.0 0.0
CYOCH2OC*O + OH = CHOOCO + H2O           2.400E+06   2.0         -1192.2   0.0 0.0 0.0
CYOCH2OC*O + HO2 = CHOOCO + H2O2         4.000E+12   0.0         12976.7   0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 673,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    reactant2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
CHOOCO
1 O 0 {2,D}
2 C 0 {1,D} {3,S} {6,S}
3 O 0 {2,S} {4,S}
4 C 1 {3,S} {5,D}
5 O 0 {4,D}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (36730, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 674,
    reactant1 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104380, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O': 12.0, '[H][H]': 2.5, '[He]': 0.0, 'C(=O)=O': 3.8, '[C]=O': 1.9, '[Ar]': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CFG



C0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 675,
    reactant1 = 
"""
O
1 O 2T
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6165000000000000.0, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O': 12.0, '[H][H]': 2.5, '[He]': 0.0, 'C(=O)=O': 3.8, '[C]=O': 1.9, '[Ar]': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 676,
    reactant1 = 
"""
O
1 O 2T
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O': 12.0, '[H][H]': 2.5, '[He]': 0.75, 'C(=O)=O': 3.8, '[C]=O': 1.9, '[Ar]': 0.75},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 677,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.8e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O': 12.0, '[H][H]': 2.5, '[He]': 0.38, 'C(=O)=O': 3.8, '[C]=O': 1.9, '[Ar]': 0.38},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 678,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1475000000000.0, 'cm^3/(mol*s)'),
            n = 0.6,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.366e+20, 'cm^6/(mol^2*s)'),
            n = -1.72,
            Ea = (524.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.8,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 1.9, '[O][O]': 0.78, 'C(=O)=O': 3.8, 'O': 11.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
MAIN BATH GAS IS N2 (COMMENT THIS REACTION OTHERWISE)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 679,
    reactant1 = 
"""
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (295100000000000.0, 's^-1'),
            n = 0,
            Ea = (48430, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.202e+17, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (45500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'O': 12.0, '[H][H]': 2.5, '[He]': 0.64, 'C(=O)=O': 3.8, '[C]=O': 1.9, '[Ar]': 0.64},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
MAIN BATH GAS IS AR OR HE (COMMENT THIS REACTION OTHERWISE)
H+O2(+M) = HO2(+M)                         1.475E+12  0.60  0.000E+00  0.0 0.0 0.0
LOW/9.042E+19 -1.50  4.922E+02/
TROE/0.5 1E-30  1E+30/
H2/3.0/ H2O/16/ O2/1.1/ CO/2.7/ CO2/5.4/ HE/1.2/
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 680,
    reactant1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (18000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (2384, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.55e+24, 'cm^6/(mol^2*s)'),
            n = -2.79,
            Ea = (4191, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'C(=O)=O': 3.8, 'O': 12.0, '[Ar]': 0.87},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
C1
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 681,
    reactant1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product1 = 
"""
H
1 H 1
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (474850000000.0, 'cm^3/(mol*s)'),
            n = 0.659,
            Ea = (14874, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'C(=O)=O': 3.8, 'O': 6.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 682,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.3e+39, 'cm^3/(mol*s)'),
            n = -6.3,
            Ea = (99900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'C(=O)=O': 3.8, 'O': 12.0, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 683,
    reactant1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.1e+45, 'cm^3/(mol*s)'), n=-8, Ea=(97510, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'C(=O)=O': 3.8, 'O': 12.0, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 684,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2277000000000000.0, 'cm^3/(mol*s)'),
            n = -0.69,
            Ea = (174.86, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (8.054e+31, 'cm^6/(mol^2*s)'),
            n = -3.75,
            Ea = (981.6, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        T3 = (570, 'K'),
        T1 = (1e-10, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[C]=O': 2.0, 'C(=O)=O': 3.0, 'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 685,
    reactant1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1.27e+16, 'cm^3/(mol*s)'),
            n = -0.63,
            Ea = (383, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.477e+33, 'cm^6/(mol^2*s)'),
            n = -4.76,
            Ea = (2440, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.783,
        T3 = (74, 'K'),
        T1 = (2941, 'K'),
        T2 = (6964, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 686,
    reactant1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2.79e+18, 'cm^3/(mol*s)'),
            n = -1.43,
            Ea = (1330, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4e+36, 'cm^6/(mol^2*s)'),
            n = -5.92,
            Ea = (3140, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.412,
        T3 = (195, 'K'),
        T1 = (5900, 'K'),
        T2 = (6394, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 687,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1055000000000.0, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (86, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.36e+31, 'cm^6/(mol^2*s)'),
            n = -4.65,
            Ea = (5080, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 688,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2430000000000.0, 'cm^3/(mol*s)'),
            n = 0.515,
            Ea = (50, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.66e+41, 'cm^6/(mol^2*s)'),
            n = -7.44,
            Ea = (14080, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (100, 'K'),
        T1 = (90000, 'K'),
        T2 = (10000, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 689,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (4.82e+17, 'cm^3/(mol*s)'),
            n = -1.16,
            Ea = (1145, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.88e+38, 'cm^6/(mol^2*s)'),
            n = -6.36,
            Ea = (5040, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6027,
        T3 = (208, 'K'),
        T1 = (3922, 'K'),
        T2 = (10180, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 690,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.5e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.2e+27, 'cm^6/(mol^2*s)'),
            n = -3.14,
            Ea = (1230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.68,
        T3 = (78, 'K'),
        T1 = (1995, 'K'),
        T2 = (5590, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 691,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
CH2CO
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (810000000000.0, 'cm^3/(mol*s)'),
            n = 0.5,
            Ea = (4510, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.69e+33, 'cm^6/(mol^2*s)'),
            n = -5.11,
            Ea = (7095, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5907,
        T3 = (275, 'K'),
        T1 = (1226, 'K'),
        T2 = (5185, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 692,
    reactant1 = 
"""
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product1 = 
"""
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (9000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[C]=O': 0.0, 'C(=O)=O': 0.0, 'O': 0.0, '[Ar]': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 693,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product1 = 
"""
OCHO
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (75000000000000.0, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (29000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 694,
    reactant1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (100000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (25100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 695,
    reactant1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (8.3e+17, 'cm^3/(mol*s)'),
            n = -1.2,
            Ea = (15500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 696,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (23000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (50000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 697,
    reactant1 = 
"""
HCOOH
1 C 0 {2,S} {3,D} {4,S}
2 O 0 {1,S} {5,S}
3 O 0 {1,D}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.5e+16, 'cm^3/(mol*s)'), n=0, Ea=(57000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 698,
    reactant1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H6
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 0 {1,S} {6,S} {7,S} {8,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.21e+17, 'cm^3/(mol*s)'),
            n = -0.99,
            Ea = (1580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.99e+41, 'cm^6/(mol^2*s)'),
            n = -7.08,
            Ea = (6685, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.842,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[He]': 0.7, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
C2
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 699,
    reactant1 = 
"""
H
1 H 1
""",
    reactant2 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (810000000000.0, 'cm^3/(mol*s)'),
            n = 0.454,
            Ea = (1820, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (9e+41, 'cm^6/(mol^2*s)'),
            n = -7.62,
            Ea = (6970, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9753,
        T3 = (210, 'K'),
        T1 = (984, 'K'),
        T2 = (4374, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[He]': 0.7, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 700,
    reactant1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(3000000000000.0, 's^-1'), n=0, Ea=(16720, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1200000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (12518, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 701,
    reactant1 = 
"""
CH3CO2
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 C 0 {1,S} {3,D} {4,S}
3 O 0 {2,D}
4 O 1 {2,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4400000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (10500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 702,
    reactant1 = 
"""
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
""",
    product1 = 
"""
CH
1 C 3 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6500000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (58820, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 703,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (136000000000000.0, 'cm^3/(mol*s)'),
            n = 0.17,
            Ea = (660, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.4e+30, 'cm^6/(mol^2*s)'),
            n = -3.86,
            Ea = (3320, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (207.5, 'K'),
        T1 = (2663, 'K'),
        T2 = (6095, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[He]': 0.7, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 704,
    reactant1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8000000000000.0, 's^-1'),
            n = 0.44,
            Ea = (88770, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.58e+51, 'cm^3/(mol*s)'),
            n = -9.3,
            Ea = (97800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.735,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[He]': 0.7, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 705,
    reactant1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5600000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (2400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.8e+40, 'cm^6/(mol^2*s)'),
            n = -7.27,
            Ea = (7220, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.751,
        T3 = (98.5, 'K'),
        T1 = (1302, 'K'),
        T2 = (4167, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[He]': 0.7, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 706,
    reactant1 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
3 H 0 {1,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.75e+33, 'cm^6/(mol^2*s)'),
            n = -4.8,
            Ea = (1900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.646,
        T3 = (132, 'K'),
        T1 = (1315, 'K'),
        T2 = (5566, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[He]': 0.7, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 707,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product1 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.71e+23, 's^-1'), n=-1.68, Ea=(94400, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (3.11e+85, 'cm^3/(mol*s)'),
            n = -18.84,
            Ea = (113100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (550, 'K'),
        T1 = (825, 'K'),
        T2 = (6100, 'K'),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'C(=O)=O': 3.0, 'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 708,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product1 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+23, 's^-1'), n=-1.62, Ea=(99540, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.11e+85, 'cm^3/(mol*s)'),
            n = -18.8,
            Ea = (118770, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (650, 'K'),
        T1 = (800, 'K'),
        T2 = (1000000000000000.0, 'K'),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'C(=O)=O': 3.0, 'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 709,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (27900000000000.0, 's^-1'),
            n = 0.09,
            Ea = (66140, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.57e+83, 'cm^3/(mol*s)'),
            n = -18.85,
            Ea = (86453, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7,
        T3 = (350, 'K'),
        T1 = (800, 'K'),
        T2 = (3800, 'K'),
        efficiencies = {'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 710,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(724000000000.0, 's^-1'), n=0.1, Ea=(91010, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.46e+87, 'cm^3/(mol*s)'),
            n = -19.42,
            Ea = (115580, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.9,
        T3 = (900, 'K'),
        T1 = (1100, 'K'),
        T2 = (3500, 'K'),
        efficiencies = {'O': 5.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 711,
    reactant1 = 
"""
SC2H4OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,S} {7,S}
3 O 0 {2,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH3CHO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,D} {7,S}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (100000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (25000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 712,
    reactant1 = 
"""
CH3COCH3
1  O 0 {2,D}
2  C 0 {1,D} {3,S} {4,S}
3  C 0 {2,S} {5,S} {6,S} {7,S}
4  C 0 {2,S} {8,S} {9,S} {10,S}
5  H 0 {3,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    product1 = 
"""
CH3CO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 1 {1,S} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    product2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.108e+21, 's^-1'), n=-1.57, Ea=(84680, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (7.013e+89, 'cm^3/(mol*s)'),
            n = -20.38,
            Ea = (107150, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.863,
        T3 = (10000000000.0, 'K'),
        T1 = (416.4, 'K'),
        T2 = (3290000000.0, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 713,
    reactant1 = 
"""
CH3OCH3
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.848e+21, 's^-1'), n=-1.56, Ea=(83130, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.118e+71, 'cm^3/(mol*s)'),
            n = -14.53,
            Ea = (100430, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.843,
        T3 = (9490000000.0, 'K'),
        T1 = (556.36, 'K'),
        T2 = (6710000000.0, 'K'),
        efficiencies = {},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
!UNIMOLECULAR DECOMPOSITION OF DME (BATH GAS: N2)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 714,
    reactant1 = 
"""
C3H8
1  C 0 {2,S} {4,S} {5,S} {6,S}
2  C 0 {1,S} {3,S} {7,S} {8,S}
3  C 0 {2,S} {9,S} {10,S} {11,S}
4  H 0 {1,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {2,S}
9  H 0 {3,S}
10 H 0 {3,S}
11 H 0 {3,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
C2H5
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.29e+37, 's^-1'), n=-5.84, Ea=(97380, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.64e+74, 'cm^3/(mol*s)'),
            n = -15.74,
            Ea = (98714, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.31,
        T3 = (50, 'K'),
        T1 = (3000, 'K'),
        T2 = (9000, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[He]': 0.7, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 715,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (200000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.33e+60, 'cm^6/(mol^2*s)'),
            n = -12,
            Ea = (5967.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.02,
        T3 = (1096.6, 'K'),
        T1 = (1096.6, 'K'),
        T2 = (6859.5, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 716,
    reactant1 = 
"""
C2H3
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C3H6
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 0 {2,S} {7,S} {8,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (25000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.27e+58, 'cm^6/(mol^2*s)'),
            n = -11.94,
            Ea = (9769.8, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.175,
        T3 = (1340.6, 'K'),
        T1 = (60000, 'K'),
        T2 = (10139.8, 'K'),
        efficiencies = {'C': 2.0, '[C]=O': 1.5, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'C=C': 3.0, 'C#C': 3.0, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 717,
    reactant1 = 
"""
C3H5-A
1 C 0 {2,D} {4,S} {5,S}
2 C 0 {1,D} {3,S} {6,S}
3 C 1 {2,S} {7,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    reactant2 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
C4H8-1
1  C 0 {2,D} {5,S} {6,S}
2  C 0 {1,D} {3,S} {7,S}
3  C 0 {2,S} {4,S} {8,S} {9,S}
4  C 0 {3,S} {10,S} {11,S} {12,S}
5  H 0 {1,S}
6  H 0 {1,S}
7  H 0 {2,S}
8  H 0 {3,S}
9  H 0 {3,S}
10 H 0 {4,S}
11 H 0 {4,S}
12 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (100000000000000.0, 'cm^3/(mol*s)'),
            n = -0.32,
            Ea = (-262.3, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.91e+60, 'cm^6/(mol^2*s)'),
            n = -12.81,
            Ea = (6250, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.104,
        T3 = (1606, 'K'),
        T1 = (60000, 'K'),
        T2 = (6118.4, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 718,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH3OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 0 {1,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(20000000000000.0, 's^-1'), n=0, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.4e+59, 'cm^3/(mol*s)'),
            n = -11.8,
            Ea = (71400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.23991,
        T3 = (555.11, 'K'),
        T1 = (8336780000.0, 'K'),
        T2 = (8213940000.0, 'K'),
        efficiencies = {'O': 6.0, '[H][H]': 3.0, '[He]': 1.2, '[O][O]': 1.1, 'C(=O)=O': 5.4, '[C]=O': 2.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
////////////////////////////////////////////////////////
methyl formate bits
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 719,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1500000000000.0, 's^-1'), n=0, Ea=(59700, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.63e+61, 'cm^3/(mol*s)'),
            n = -12.79,
            Ea = (71100, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.179405,
        T3 = (357.541, 'K'),
        T1 = (9918710000.0, 'K'),
        T2 = (3289900000.0, 'K'),
        efficiencies = {'O': 6.0, '[H][H]': 3.0, '[He]': 1.2, '[O][O]': 1.1, 'C(=O)=O': 5.4, '[C]=O': 2.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 720,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1000000000000.0, 's^-1'), n=0, Ea=(60500, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.55e+57, 'cm^3/(mol*s)'),
            n = -11.57,
            Ea = (71700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.780745,
        T3 = (6490130000.0, 'K'),
        T1 = (618.799, 'K'),
        T2 = (6710100000.0, 'K'),
        efficiencies = {'O': 6.0, '[H][H]': 3.0, '[He]': 1.2, '[O][O]': 1.1, 'C(=O)=O': 5.4, '[C]=O': 2.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 721,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
OCHO
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 O 1 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.17e+24, 's^-1'), n=-2.401, Ea=(92600, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.71e+47, 'cm^3/(mol*s)'),
            n = -8.43,
            Ea = (98490, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 6.8932e-15,
        T3 = (4734.1, 'K'),
        T1 = (9330200000.0, 'K'),
        T2 = (1786000000.0, 'K'),
        efficiencies = {'O': 6.0, '[H][H]': 3.0, '[He]': 1.2, '[O][O]': 1.1, 'C(=O)=O': 5.4, '[C]=O': 2.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 722,
    reactant1 = 
"""
CH3OCHO
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {8,S}
4 O 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.18e+16, 's^-1'), n=0, Ea=(97000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5.27e+63, 'cm^3/(mol*s)'),
            n = -12.32,
            Ea = (109180, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.89375,
        T3 = (7499100000.0, 'K'),
        T1 = (647.04, 'K'),
        T2 = (669800000.0, 'K'),
        efficiencies = {'O': 6.0, '[H][H]': 3.0, '[He]': 1.2, '[O][O]': 1.1, 'C(=O)=O': 5.4, '[C]=O': 2.7},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

