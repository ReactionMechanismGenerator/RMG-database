#!/usr/bin/env python
# encoding: utf-8

name = "Glarborg/C2"
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
        A = (3600000000000000.0, 'cm^3/(mol*s)'),
        n = -0.41,
        Ea = (16600, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CFG





Glarborg,

*****************************************************************************
H2/O2 subset                                                             *
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
H
1 H 1
""",
    reactant2 = 
"""
H
1 H 1
""",
    reactant3 = 
"""
H2
1 H 0 {2,S}
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
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
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
H
1 H 1
""",
    reactant2 = 
"""
H
1 H 1
""",
    reactant3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
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
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+19, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
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
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3800000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (7948, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (880000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (19175, 'cal/mol'),
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
    index = 6,
    reactant1 = 
"""
OH
1 O 1 {2,S}
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
O
1 O 2T
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4300, 'cm^3/(mol*s)'), n=2.7, Ea=(-1822, 'cal/mol'), T0=(1, 'K')),
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
OH
1 O 1 {2,S}
2 H 0 {1,S}
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
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (210000000.0, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (3449, 'cal/mol'),
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
H2
1 H 0 {2,S}
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
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (740000, 'cm^3/(mol*s)'),
        n = 2.433,
        Ea = (53502, 'cal/mol'),
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
        A = (84000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (400, 'cal/mol'),
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
    index = 10,
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
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400000000000.0, 'cm^3/(mol*s)'),
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
    index = 11,
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
OH
1 O 1 {2,S}
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
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-445, 'cal/mol'),
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
        A = (28900000000000.0, 'cm^3/(mol*s)', '*|/', 1.58),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
These three add up to give Glarborg's preferred rate, but the third of them
has a negative A which RMG does not like:
HO2 + OH = H2O + O2                        3.6E21  -2.100    9000  0.0 0.0 0.0
//  DUPLICATE
HO2 + OH = H2O + O2                        2.0E15  -0.600       0  0.0 0.0 0.0
//  DUPLICATE
HO2 + OH = H2O + O2                       -2.2E96 -24.000   49000 0.0 0.0 0.0
//  DUPLICATE
Instead here is a rate from Baulch et al JPCRF 1994 as reported by
http://kinetics.nist.gov/kinetics/Detail?id=1994BAU/COB847-1033:91
although the valid temperature range is not very large...
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
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
                A = (190000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1408, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (100000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (11034, 'cal/mol'),
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
    index = 15,
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
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3580, 'cal/mol'),
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
    index = 16,
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
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3760, 'cal/mol'),
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
    index = 17,
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
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9600000.0, 'cm^3/(mol*s)'), n=2, Ea=(3970, 'cal/mol'), T0=(1, 'K')),
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
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1900000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (427, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1.6e+18, 'cm^3/(mol*s)'), n=0, Ea=(29410, 'cal/mol'), T0=(1, 'K')),
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
    index = 20,
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
        A = (4700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60500, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
CO/CO2 subset                                                            *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
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
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17943, 'cal/mol'),
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
HOCO
1 C 1 {2,S} {3,D}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
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
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
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
                A = (4600000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-89, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(9500000.0, 'cm^3/(mol*s)'), n=2, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
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
    index = 24,
    reactant1 = 
"""
HOCO
1 C 1 {2,S} {3,D}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
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
    index = 25,
    reactant1 = 
"""
HOCO
1 C 1 {2,S} {3,D}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
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
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
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
        A = (990000000000.0, 'cm^3/(mol*s)'),
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
        A = (410000000.0, 'cm^3/(mol*s)'),
        n = 1.47,
        Ea = (2444, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
CH2O subset                                                              *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
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
        A = (420000000000.0, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (2760, 'cal/mol'),
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
    kinetics = Arrhenius(A=(240000, 'cm^3/(mol*s)'), n=2.5, Ea=(36461, 'cal/mol'), T0=(1, 'K')),
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
        A = (78000000.0, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1055, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
SCRATCH: RMG doesn't like this rate; cfg replaced it with baulch
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
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
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2O + OH = HCO + H2O                  4.9E12   0.0     -79.5  0.0 0.0 0.0
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
    kinetics = Arrhenius(A=(32, 'cm^3/(mol*s)'), n=3.36, Ea=(4310, 'cal/mol'), T0=(1, 'K')),
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
    index = 32,
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
    index = 33,
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
    index = 34,
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
    index = 35,
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
    index = 36,
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
        A = (3400000000000.0, 'cm^3/(mol*s)'),
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
    index = 37,
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
    index = 38,
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
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
        A = (27000000000000.0, 'cm^3/(mol*s)'),
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
    index = 39,
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
    kinetics = Arrhenius(A=(4100, 'cm^3/(mol*s)'), n=3.156, Ea=(8755, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
CH4 subset                                                               *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
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
    kinetics = Arrhenius(A=(440000, 'cm^3/(mol*s)'), n=2.5, Ea=(6577, 'cal/mol'), T0=(1, 'K')),
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
        A = (1000000.0, 'cm^3/(mol*s)'),
        n = 2.182,
        Ea = (2506, 'cal/mol'),
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
    index = 42,
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
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
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
    kinetics = Arrhenius(
        A = (4300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10030, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH4 + O2 = CH3 + HO2                               see reverse
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
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
        A = (43000000000000.0, 'cm^3/(mol*s)'),
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
    index = 45,
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
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15100, 'cal/mol'),
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
        A = (72000000000000.0, 'cm^3/(mol*s)'),
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
    index = 47,
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
        A = (69000000000000.0, 'cm^3/(mol*s)'),
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
O
1 O 2T
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
    index = 49,
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
    kinetics = Arrhenius(A=(1100, 'cm^3/(mol*s)'), n=3, Ea=(2780, 'cal/mol'), T0=(1, 'K')),
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
        A = (3000000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
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
    index = 51,
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
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.228,
        Ea = (-3020, 'cal/mol'),
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
    index = 52,
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
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0.2688,
        Ea = (-687.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
RMG dislikes!  replaced with Jasper
CH3 + HO2 = CH4 + O2                       2.5E08   1.250   -1630  0.0 0.0 0.0
CH3 + HO2 = CH4 + O2                       1.8E03   2.830   -3730  0.0 0.0 0.0

replace with Jasper
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
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
        A = (7500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28297, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH3 + HO2 = CH3O + OH                      2.0E13   0.000    1075  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
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
    kinetics = Arrhenius(
        A = (190000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9842, 'cal/mol'),
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
    index = 56,
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
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16055, 'cal/mol'),
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
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
CH2 + H = CH + H2                          1.0E18 -1.560        0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
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
    index = 59,
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
    index = 60,
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
        A = (2.2e+22, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2 + OH = CH + H2O                        1.1E07  2.000     3000  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
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
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
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
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
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
    kinetics = Arrhenius(
        A = (2.6e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
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
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
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
    index = 65,
    reactant1 = 
"""
CH2
1 C 2T {2,S} {3,S}
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
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
        Ea = (1000, 'cal/mol'),
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
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000000.0, 'cm^3/(mol*s)'),
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
CH2(S) + H = CH + H2                       3.0E13  0.000        0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
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
    index = 69,
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
    index = 70,
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
    index = 71,
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
    index = 72,
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
        A = (2900000000.0, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (4491, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH + H = C + H2                            1.5E14  0.000        0  0.0 0.0 0.0
CH + O = CO + H                            5.7E13  0.000        0  0.0 0.0 0.0
CH + OH = HCO + H                          3.0E13  0.000        0  0.0 0.0 0.0
CH + OH = C + H2O                          4.0E07  2.000     3000  0.0 0.0 0.0
CH + O2 = HCO + O                          3.3E13  0.000        0  0.0 0.0 0.0
CH + H2O = CH2O + H                        5.7E12  0.000     -755  0.0 0.0 0.0
CH + CO2 = HCO + CO                        8.8E06  1.750    -1040  0.0 0.0 0.0
C + OH = CO + H                            5.0E13  0.000        0  0.0 0.0 0.0
C + O2 = CO + O                            2.0E13  0.000        0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
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
        A = (510000000.0, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (4491, 'cal/mol'),
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
    kinetics = Arrhenius(
        A = (21000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5305, 'cal/mol'),
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
        A = (3700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5305, 'cal/mol'),
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
        A = (150000000.0, 'cm^3/(mol*s)'),
        n = 1.4434,
        Ea = (113, 'cal/mol'),
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
    index = 77,
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
        A = (27000000.0, 'cm^3/(mol*s)'),
        n = 1.4434,
        Ea = (113, 'cal/mol'),
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15000, 'cal/mol'),
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
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46600, 'cal/mol'),
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
    index = 80,
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
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
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
        Ea = (54800, 'cal/mol'),
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
    index = 81,
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
    index = 82,
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
    index = 83,
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
        A = (66000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-693, 'cal/mol'),
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
    index = 85,
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
    index = 86,
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
                A = (72000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (3736, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(2.9e+16, 'cm^3/(mol*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
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
    index = 88,
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
    index = 89,
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
    index = 90,
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
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
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
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5862, 'cal/mol'), T0=(1, 'K')),
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
        A = (4800000000000.0, 'cm^3/(mol*s)'),
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
    index = 92,
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
        A = (2400000000000.0, 'cm^3/(mol*s)'),
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
    index = 93,
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
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
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
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(22, 'cm^3/(mol*s)'), n=3.1, Ea=(16227, 'cal/mol'), T0=(1, 'K')),
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
        A = (53000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (745, 'cal/mol'),
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
        A = (4600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (745, 'cal/mol'),
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
        A = (3800000000000.0, 'cm^3/(mol*s)'),
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
    index = 97,
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
    index = 98,
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
    index = 99,
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
    kinetics = Arrhenius(
        A = (22000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1749, 'cal/mol'),
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
        A = (9.5e+25, 'cm^3/(mol*s)'),
        n = -4.93,
        Ea = (9080, 'cal/mol'),
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
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
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
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15073, 'cal/mol'),
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2981, 'cal/mol'),
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
    index = 104,
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
    index = 105,
    reactant1 = 
"""
CH3OOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
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
    product3 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54000000000.0, 'cm^3/(mol*s)'),
        n = 0,
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
    index = 106,
    reactant1 = 
"""
CH3OOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
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
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
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
        A = (54000000000.0, 'cm^3/(mol*s)'),
        n = 0,
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
    index = 107,
    reactant1 = 
"""
CH3OOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
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
        A = (12000000000.0, 'cm^3/(mol*s)'),
        n = 0,
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
    index = 108,
    reactant1 = 
"""
CH3OOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
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
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4750, 'cal/mol'),
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
CH3OOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
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
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
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
        A = (8700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4750, 'cal/mol'),
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
CH3OOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
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
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
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
        A = (1100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-437, 'cal/mol'),
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
CH3OOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
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
    product3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (720000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-258, 'cal/mol'),
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
CH3OOH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 0 {2,S} {7,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
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
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
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
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
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
    index = 113,
    reactant1 = 
"""
CH3OO
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
    index = 114,
    reactant1 = 
"""
CH3OO
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
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-445, 'cal/mol'),
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
CH3OO
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
        A = (2000000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
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
CH3OO
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
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
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
        A = (400000000000.0, 'cm^3/(mol*s)'),
        n = 0.6,
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
CH3OO
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
CH3OOH
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
        A = (250000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1490, 'cal/mol'),
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
CH3OO
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
        A = (5100000000000.0, 'cm^3/(mol*s)'),
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
    index = 119,
    reactant1 = 
"""
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
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
CH3OOH
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
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
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
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
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
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    product2 = 
"""
H
1 H 1
""",
    product3 = 
"""
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
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
    index = 121,
    reactant1 = 
"""
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
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
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
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
    index = 122,
    reactant1 = 
"""
CH3OO
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
CH3OOH
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
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
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
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
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
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH3OOH
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
    index = 124,
    reactant1 = 
"""
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
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
CH3OOH
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
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
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
    index = 125,
    reactant1 = 
"""
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
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
    product3 = 
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
                A = (1.1e+18, 'cm^3/(mol*s)'),
                n = -2.4,
                Ea = (1800, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (70000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (800, 'cal/mol'),
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
    index = 127,
    reactant1 = 
"""
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    reactant2 = 
"""
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
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
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000.0, 'cm^3/(mol*s)'),
        n = -0.55,
        Ea = (-1600, 'cal/mol'),
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
CH3OO
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
CH3CH2O
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
        A = (5100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1410, 'cal/mol'),
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
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
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
CH3OOH
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
    kinetics = Arrhenius(A=(19, 'cm^3/(mol*s)'), n=3.64, Ea=(17100, 'cal/mol'), T0=(1, 'K')),
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
    index = 130,
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
        A = (98000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9220, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
C2 subset                                                                *
*****************************************************************************
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
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
    kinetics = Arrhenius(A=(1.1e-07, 'cm^3/(mol*s)'), n=6.5, Ea=(274, 'cal/mol'), T0=(1, 'K')),
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
    index = 132,
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
    kinetics = Arrhenius(A=(9200000.0, 'cm^3/(mol*s)'), n=2, Ea=(990, 'cal/mol'), T0=(1, 'K')),
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
    kinetics = Arrhenius(A=(110000, 'cm^3/(mol*s)'), n=2.5, Ea=(16850, 'cal/mol'), T0=(1, 'K')),
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
    kinetics = Arrhenius(A=(730000, 'cm^3/(mol*s)'), n=2.5, Ea=(49160, 'cal/mol'), T0=(1, 'K')),
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (56000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (9418, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (840000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (22250, 'cal/mol'),
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
    index = 137,
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
CH2(S)
1 C 2S {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
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
    index = 138,
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
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
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
    index = 139,
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
        A = (53000000000000.0, 'cm^3/(mol*s)'),
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
    index = 140,
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
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31000000000000.0, 'cm^3/(mol*s)'),
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
    index = 141,
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
    index = 142,
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
CH3CH2O
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
        A = (31000000000000.0, 'cm^3/(mol*s)'),
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
    index = 143,
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
    kinetics = Arrhenius(
        A = (14000000.0, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (-1975, 'cal/mol'),
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
    index = 144,
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5500, 'cm^3/(mol*s)'), n=2.81, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (43000000000000.0, 'cm^3/(mol*s)'),
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
    index = 146,
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
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
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
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
C2H5 + HCO = C2H6 + CO                     1.2E14   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
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
        A = (1500000000000.0, 'cm^3/(mol*s)'),
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
    index = 148,
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
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.62, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
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
CH4 + CH = C2H4 + H                        3.0E13   0.000    -400  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3900000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (1494, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (62000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (6855, 'cal/mol'),
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
    index = 153,
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1700000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (1494, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (28000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (6855, 'cal/mol'),
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
    index = 155,
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
    kinetics = Arrhenius(
        A = (54000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (4166, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
RMG doesn't like this rate; I replaced it with NIST
C2H4 + OH = C2H3 + H2O                     1.3E-1   4.200    -860  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
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
cC2H4O
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
        A = (2200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17200, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Alternative fit to  60 atm,600-900K    with  no duplicate
fit to  60 atm,600-900K
C2H4 + OH = CH2CH2OH                     2.4E20  -2.399    3294  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
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
        A = (71000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60010, 'cal/mol'),
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
    kinetics = Arrhenius(
        A = (60000000.0, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (16630, 'cal/mol'),
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
    index = 159,
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
        A = (45000000000000.0, 'cm^3/(mol*s)'),
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
    index = 160,
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
CH3 + CH = C2H3 + H                        3.0E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
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
    index = 162,
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
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
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
    index = 163,
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
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+36, 'cm^3/(mol*s)'), n=-8, Ea=(5680, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
PM 60 bar
RMG dislikes; cfg replaced w mclin
C2H3 + O2 = CH2CHOO                      1.1E12   0.000   -1680  0.0 0.0 0.0
C.F.Goldsmith replaced the above rate expression from Glarborg with the following rate expression from
A. M. Mebel, E. W. G. Diau, M. C. Lin, and K. Morokuma J. Am. Chem. Soc. 1996, 118, 9759-9771  http://dx.doi.org/10.1021/ja961476e
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
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
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
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
        A = (6300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3130, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
PM 60 bar
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
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
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4800, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
PM 60 bar
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
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
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
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
        A = (760000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7930, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
PM 60 bar
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
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
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (280000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3130, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
PM 60 bar
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
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
        A = (13000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3130, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
PM 60 bar
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
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
    kinetics = Arrhenius(A=(5400, 'cm^3/(mol*s)'), n=2.81, Ea=(5860, 'cal/mol'), T0=(1, 'K')),
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
    index = 170,
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
    index = 171,
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
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
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
        A = (21000000000000.0, 'cm^3/(mol*s)'),
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
    index = 172,
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
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
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
C2H3 + CH = CH2 + C2H2                     5.0E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
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
C2H2
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
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
    index = 174,
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
CH3 + C = C2H2 + H                         5.0E13   0.000       0  0.0 0.0 0.0
CH2 + CH = C2H2 + H                        4.0E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
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
        A = (14000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2 + CH2 = C2H2 + H + H                     4.0E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
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
    kinetics = Arrhenius(A=(6100000.0, 'cm^3/(mol*s)'), n=2, Ea=(1900, 'cal/mol'), T0=(1, 'K')),
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
    index = 177,
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
        A = (3200000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
        Ea = (15000, 'cal/mol'),
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
    index = 178,
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10000, 'cal/mol'),
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
    index = 179,
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
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
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
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10000, 'cal/mol'),
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
    index = 180,
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
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
        A = (70000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (30600, 'cal/mol'),
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
    index = 181,
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
CH2(S)
1 C 2S {2,S} {3,S}
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
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
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
    index = 182,
    reactant1 = 
"""
H2CC
1 C 0  {2,D} {3,S} {4,S}
2 C 2S {1,D}
3 H 0  {1,S}
4 H 0  {1,S}
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
    kinetics = Arrhenius(A=(10000000.0, 's^-1'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
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
    index = 183,
    reactant1 = 
"""
H2CC
1 C 0  {2,D} {3,S} {4,S}
2 C 2S {1,D}
3 H 0  {1,S}
4 H 0  {1,S}
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
H
1 H 1
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
    index = 184,
    reactant1 = 
"""
H2CC
1 C 0  {2,D} {3,S} {4,S}
2 C 2S {1,D}
3 H 0  {1,S}
4 H 0  {1,S}
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
    index = 185,
    reactant1 = 
"""
H2CC
1 C 0  {2,D} {3,S} {4,S}
2 C 2S {1,D}
3 H 0  {1,S}
4 H 0  {1,S}
""",
    reactant2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
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
    index = 186,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
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
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(400000, 'cm^3/(mol*s)'), n=2.4, Ea=(1000, 'cal/mol'), T0=(1, 'K')),
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
    index = 187,
    reactant1 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
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
CH2 + C = C2H + H                          5.0E13   0.000       0  0.0 0.0 0.0
C2H + O = CH + CO                          5.0E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    reactant1 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
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
C2
1 C 1 {2,T}
2 C 1 {1,T}
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
        A = (40000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8000, 'cal/mol'),
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
    index = 189,
    reactant1 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
3 H 0 {1,S}
""",
    reactant2 = 
"""
H2
1 H 0 {2,S}
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
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(410000, 'cm^3/(mol*s)'), n=2.39, Ea=(864, 'cal/mol'), T0=(1, 'K')),
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
    index = 190,
    reactant1 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47000000000000.0, 'cm^3/(mol*s)'),
        n = -0.16,
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
    index = 191,
    reactant1 = 
"""
C2H
1 C 0 {2,T} {3,S}
2 C 1 {1,T}
3 H 0 {1,S}
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
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
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
        A = (7200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (976, 'cal/mol'),
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
    index = 192,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
C2O
1 C 0  {2,D} {3,D}
2 C 2T {1,D}
3 O 0  {1,D}
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
C2 + O = C + CO                            1.0E14   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
    reactant1 = 
"""
C2
1 C 1 {2,T}
2 C 1 {1,T}
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (980, 'cal/mol'),
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
    index = 194,
    reactant1 = 
"""
CH3CH2OH
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
CH3CHOH
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
        A = (26000000.0, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (2827, 'cal/mol'),
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
    index = 195,
    reactant1 = 
"""
CH3CH2OH
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
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
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
        A = (12000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (5098, 'cal/mol'),
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
    index = 196,
    reactant1 = 
"""
CH3CH2OH
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
CH3CH2O
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
        n = 1.65,
        Ea = (3038, 'cal/mol'),
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
    index = 197,
    reactant1 = 
"""
CH3CH2OH
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
CH3CHOH
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
        A = (19000000.0, 'cm^3/(mol*s)'),
        n = 1.85,
        Ea = (1824, 'cal/mol'),
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
    index = 198,
    reactant1 = 
"""
CH3CH2OH
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
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
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
        A = (94000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (5459, 'cal/mol'),
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
    index = 199,
    reactant1 = 
"""
CH3CH2OH
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
CH3CH2O
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
        A = (16000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (4448, 'cal/mol'),
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
    index = 200,
    reactant1 = 
"""
CH3CH2OH
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
CH3CHOH
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
        A = (460000000000.0, 'cm^3/(mol*s)'),
        n = 0.15,
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
    index = 201,
    reactant1 = 
"""
CH3CH2OH
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
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
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
        A = (170000000000.0, 'cm^3/(mol*s)'),
        n = 0.27,
        Ea = (600, 'cal/mol'),
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
    index = 202,
    reactant1 = 
"""
CH3CH2OH
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
CH3CH2O
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
        A = (750000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (1634, 'cal/mol'),
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
    index = 203,
    reactant1 = 
"""
CH3CH2OH
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
CH3CHOH
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

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 204,
    reactant1 = 
"""
CH3CH2OH
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
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
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
    kinetics = Arrhenius(A=(12000, 'cm^3/(mol*s)'), n=2.55, Ea=(15750, 'cal/mol'), T0=(1, 'K')),
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
    index = 205,
    reactant1 = 
"""
CH3CH2OH
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
CH3CH2O
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

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 206,
    reactant1 = 
"""
CH3CH2OH
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
CH3CHOH
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
    kinetics = Arrhenius(A=(730, 'cm^3/(mol*s)'), n=2.99, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
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
    index = 207,
    reactant1 = 
"""
CH3CH2OH
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
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
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
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=3.18, Ea=(9622, 'cal/mol'), T0=(1, 'K')),
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
    index = 208,
    reactant1 = 
"""
CH3CH2OH
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
CH3CH2O
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
    kinetics = Arrhenius(A=(150, 'cm^3/(mol*s)'), n=2.99, Ea=(7649, 'cal/mol'), T0=(1, 'K')),
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
    index = 209,
    reactant1 = 
"""
CH3CHOH
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
OH
1 O 1 {2,S}
2 H 0 {1,S}
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
    index = 210,
    reactant1 = 
"""
CH3CHOH
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
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
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
    index = 211,
    reactant1 = 
"""
CH3CHOH
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
    index = 212,
    reactant1 = 
"""
CH3CHOH
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
OH
1 O 1 {2,S}
2 H 0 {1,S}
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

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 213,
    reactant1 = 
"""
CH3CHOH
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
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
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
    index = 214,
    reactant1 = 
"""
CH3CHOH
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (8400000000000000.0, 'cm^3/(mol*s)'),
                n = -1.2,
                Ea = (0, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (480000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (5017, 'cal/mol'),
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
    index = 216,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220000, 's^-1'), n=2.84, Ea=(32920, 'cal/mol'), T0=(1, 'K')),
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
    index = 217,
    reactant1 = 
"""
CH3CH2O
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
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e-29, 's^-1'), n=11.9, Ea=(4450, 'cal/mol'), T0=(1, 'K')),
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
    index = 218,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
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
    index = 219,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
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
    index = 220,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
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
CH2CH2OH + O = HOCH2CHO + H                5.0E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 221,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
CH3CH2OH
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
CH2CH2OH + OH = HOCH2CHOH                3.3E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 222,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    reversible = False,
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
    index = 223,
    reactant1 = 
"""
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
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
        A = (14000000.0, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (-1975, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2CH2OH + HO2 = HOCH2CH2O + OH            3.0E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 224,
    reactant1 = 
"""
CH3CH2O
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
    kinetics = Arrhenius(A=(13000000000000.0, 's^-1'), n=0, Ea=(20060, 'cal/mol'), T0=(1, 'K')),
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
    index = 225,
    reactant1 = 
"""
CH3CH2O
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
H
1 H 1
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
    index = 226,
    reactant1 = 
"""
CH3CH2O
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
OH
1 O 1 {2,S}
2 H 0 {1,S}
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
    index = 227,
    reactant1 = 
"""
CH3CH2O
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
        A = (15000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (645, 'cal/mol'),
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
    index = 228,
    reactant1 = 
"""
CH3CH2O
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
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
        A = (9.5e+25, 'cm^3/(mol*s)'),
        n = -4.93,
        Ea = (9080, 'cal/mol'),
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
    index = 229,
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
        A = (47000000000000.0, 'cm^3/(mol*s)'),
        n = -0.35,
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
    index = 230,
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
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1900000000000.0, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (5359, 'cal/mol'),
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
    index = 231,
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
        A = (1.8e+18, 'cm^3/(mol*s)'),
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
    index = 232,
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
        A = (37000000000000.0, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (3556, 'cal/mol'),
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
    index = 233,
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
        A = (240000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
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
    index = 234,
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
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
        Ea = (800, 'cal/mol'),
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
    index = 235,
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
        A = (2.4e+19, 'cm^3/(mol*s)'),
        n = -2.2,
        Ea = (14030, 'cal/mol'),
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
    index = 236,
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
H2O2
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (230000000000.0, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (14864, 'cal/mol'),
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
    index = 237,
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
    kinetics = Arrhenius(A=(120000, 'cm^3/(mol*s)'), n=2.5, Ea=(37554, 'cal/mol'), T0=(1, 'K')),
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
    index = 238,
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
    index = 239,
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
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(25, 'cm^3/(mol*s)'), n=3.15, Ea=(5727, 'cal/mol'), T0=(1, 'K')),
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
    index = 240,
    reactant1 = 
"""
cC2H4O
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
        A = (18000000000000.0, 's^-1'),
        n = 0.2,
        Ea = (71780, 'cal/mol'),
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
    index = 241,
    reactant1 = 
"""
cC2H4O
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
    kinetics = Arrhenius(
        A = (56000000000000.0, 's^-1'),
        n = 0.4,
        Ea = (61880, 'cal/mol'),
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
    index = 242,
    reactant1 = 
"""
cC2H4O
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
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 's^-1'),
        n = 0.25,
        Ea = (65310, 'cal/mol'),
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
    index = 243,
    reactant1 = 
"""
cC2H4O
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
        A = (3600000000000.0, 's^-1'),
        n = -0.2,
        Ea = (63030, 'cal/mol'),
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
    index = 244,
    reactant1 = 
"""
cC2H4O
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
    kinetics = Arrhenius(
        A = (3200000000000.0, 's^-1'),
        n = -0.75,
        Ea = (46424, 'cal/mol'),
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
    index = 245,
    reactant1 = 
"""
cC2H4O
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
        A = (7600000000000.0, 's^-1'),
        n = 0.06,
        Ea = (69530, 'cal/mol'),
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
    index = 246,
    reactant1 = 
"""
cC2H4O
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
cC2H3O
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (8310, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
cC2H4O + H = CH3CHO + H                     5.6E13   0.000   10950  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 247,
    reactant1 = 
"""
cC2H4O
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
    kinetics = Arrhenius(
        A = (5000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5000, 'cal/mol'),
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
    index = 248,
    reactant1 = 
"""
cC2H4O
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
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (95000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5000, 'cal/mol'),
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
    index = 249,
    reactant1 = 
"""
cC2H4O
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
O
1 O 2T
""",
    product1 = 
"""
cC2H3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
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
        A = (1900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5250, 'cal/mol'),
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
    index = 250,
    reactant1 = 
"""
cC2H4O
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
cC2H3O
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
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3610, 'cal/mol'),
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
    index = 251,
    reactant1 = 
"""
cC2H4O
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
cC2H3O
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
        A = (4000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (17000, 'cal/mol'),
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
    index = 252,
    reactant1 = 
"""
cC2H4O
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
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    product1 = 
"""
cC2H3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
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
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (61500, 'cal/mol'),
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
    index = 253,
    reactant1 = 
"""
cC2H4O
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
cC2H3O
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
        A = (1100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11830, 'cal/mol'),
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
    index = 254,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {3,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(240, 'cm^3/(mol*s)'), n=3.63, Ea=(11266, 'cal/mol'), T0=(1, 'K')),
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
    index = 255,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
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
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
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
    index = 256,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3900000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (1494, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (62000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (6855, 'cal/mol'),
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
    index = 258,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
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
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (4400, 'cal/mol'),
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
    index = 259,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
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
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
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
    kinetics = Arrhenius(A=(0.13, 'cm^3/(mol*s)'), n=4.2, Ea=(-860, 'cal/mol'), T0=(1, 'K')),
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
    index = 260,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
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
    kinetics = Arrhenius(
        A = (750000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (1600, 'cal/mol'),
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
    index = 261,
    reactant1 = 
"""
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
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
    reversible = False,
    kinetics = Arrhenius(
        A = (35000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (39000, 'cal/mol'),
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
    index = 262,
    reactant1 = 
"""
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {3,S}
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

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 263,
    reactant1 = 
"""
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {3,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
OCHCHO
1 C 0 {2,S} {3,D} {5,S}
2 C 0 {1,S} {4,D} {6,S}
3 O 0 {1,D}
4 O 0 {2,D}
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
    index = 264,
    reactant1 = 
"""
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
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
HCCOH
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 O 0 {1,S} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    product2 = 
"""
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(140, 'cm^3/(mol*s)'), n=3.4, Ea=(3700, 'cal/mol'), T0=(1, 'K')),
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
    index = 265,
    reactant1 = 
"""
cC2H3O
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
    kinetics = Arrhenius(A=(8.7e+31, 's^-1'), n=-6.9, Ea=(14994, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
#CHCHOH + O2 = OCHCHO + OH                  2.5E12   0.000       0 0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 266,
    reactant1 = 
"""
cC2H3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
    kinetics = Arrhenius(A=(50000000000000.0, 's^-1'), n=0, Ea=(14863, 'cal/mol'), T0=(1, 'K')),
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
    index = 267,
    reactant1 = 
"""
cC2H3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {3,S} {6,S}
3 O 0 {1,S} {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
    kinetics = Arrhenius(A=(7100000000000.0, 's^-1'), n=0, Ea=(14280, 'cal/mol'), T0=(1, 'K')),
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
    index = 268,
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
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
    index = 269,
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
    index = 270,
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

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 271,
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
    index = 272,
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

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 273,
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
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
    index = 274,
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (490000000000000.0, 'cm^3/(mol*s)'),
        n = -0.5,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
#CH2CHO + O2 = OCHCHO + OH                  2.2E11  0.000 1500  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 275,
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
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = -0.5,
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
    index = 276,
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
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
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
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = -0.5,
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
    index = 277,
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
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
    index = 278,
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
        A = (230000000.0, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (2627, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2CHO + CH = C2H3 + HCO                   1.0E14   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 279,
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
        A = (21000000000000.0, 'cm^3/(mol*s)'),
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
    index = 280,
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
    index = 281,
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

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 282,
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
        A = (53000000000000.0, 'cm^3/(mol*s)'),
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
    index = 283,
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
    index = 284,
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
CH3OO
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
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
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
    index = 285,
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
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
    index = 286,
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
        A = (53000000000000.0, 'cm^3/(mol*s)'),
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
    index = 287,
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
        A = (1900000000000.0, 'cm^3/(mol*s)'),
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
    index = 288,
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
        A = (33000000000.0, 'cm^3/(mol*s)'),
        n = 0.851,
        Ea = (2840, 'cal/mol'),
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
    index = 289,
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
        A = (30000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (10000, 'cal/mol'),
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
    index = 290,
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
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
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
        A = (1800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1350, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH + CH2O = CH2CO + H                      9.5E13   0.000    -517  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 291,
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
        A = (20000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (10000, 'cal/mol'),
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
    index = 292,
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
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1013, 'cal/mol'),
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
    index = 293,
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
        A = (670000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1013, 'cal/mol'),
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
    index = 294,
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
        A = (10000000.0, 'cm^3/(mol*s)'),
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
    index = 295,
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

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 296,
    reactant1 = 
"""
HCCOH
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 O 0 {1,S} {5,S}
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
        A = (30000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1000, 'cal/mol'),
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
    index = 297,
    reactant1 = 
"""
HCCOH
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 O 0 {1,S} {5,S}
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
        A = (20000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
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
    index = 298,
    reactant1 = 
"""
HCCOH
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 O 0 {1,S} {5,S}
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
        A = (10000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1000, 'cal/mol'),
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
    index = 299,
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000000.0, 'cm^3/(mol*s)'),
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
    index = 300,
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
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
    index = 301,
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
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
    index = 302,
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
C2O
1 C 0  {2,D} {3,D}
2 C 2T {1,D}
3 O 0  {1,D}
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
    index = 303,
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
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    product2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4900000000000.0, 'cm^3/(mol*s)'),
        n = -0.142,
        Ea = (1150, 'cal/mol'),
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
    index = 304,
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
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
        A = (160000000000.0, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (1020, 'cal/mol'),
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
    index = 305,
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
    product3 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(220, 'cm^3/(mol*s)'), n=2.69, Ea=(3540, 'cal/mol'), T0=(1, 'K')),
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
    index = 306,
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
CH2
1 C 2T {2,S} {3,S}
2 H 0  {1,S}
3 H 0  {1,S}
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
    index = 307,
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
HCCO
1 C 1 {2,D} {4,S}
2 C 0 {1,D} {3,D}
3 O 0 {2,D}
4 H 0 {1,S}
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
    product3 = 
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
HCCO + CH = C2H2 + CO                      5.0E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 308,
    reactant1 = 
"""
C2O
1 C 0  {2,D} {3,D}
2 C 2T {1,D}
3 O 0  {1,D}
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (52000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
C2O + H = CH + CO                          1.3E13   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 309,
    reactant1 = 
"""
C2O
1 C 0  {2,D} {3,D}
2 C 2T {1,D}
3 O 0  {1,D}
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
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
    index = 310,
    reactant1 = 
"""
C2O
1 C 0  {2,D} {3,D}
2 C 2T {1,D}
3 O 0  {1,D}
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
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product3 = 
"""
O
1 O 2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2600, 'cal/mol'),
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
    index = 311,
    reactant1 = 
"""
C2O
1 C 0  {2,D} {3,D}
2 C 2T {1,D}
3 O 0  {1,D}
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
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2600, 'cal/mol'),
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
    index = 312,
    reactant1 = 
"""
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
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
    product3 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (65000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
C2O + C = CO + C2                          1.0E14   0.000       0  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 313,
    reactant1 = 
"""
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
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
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
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
    kinetics = Arrhenius(
        A = (43000000000.0, 'cm^3/(mol*s)'),
        n = 0,
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
    index = 314,
    reactant1 = 
"""
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
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
CH3CH2O
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
        A = (12000000000.0, 'cm^3/(mol*s)'),
        n = 0,
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
    index = 315,
    reactant1 = 
"""
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
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
    product3 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4750, 'cal/mol'),
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
    index = 316,
    reactant1 = 
"""
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
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
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
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
        A = (8700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4750, 'cal/mol'),
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
    index = 317,
    reactant1 = 
"""
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
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
    product3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (720000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-258, 'cal/mol'),
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
    index = 318,
    reactant1 = 
"""
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
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
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
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
    kinetics = Arrhenius(
        A = (1100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-437, 'cal/mol'),
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
    index = 319,
    reactant1 = 
"""
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
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
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
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
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
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
    index = 320,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH3CH2O
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
    index = 321,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH3CH2O
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
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-145, 'cal/mol'),
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
    index = 322,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CH2OH
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
    product2 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
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
    index = 323,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CH3CH2O
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
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000000000.0, 'cm^3/(mol*s)'),
        n = 0.6,
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
    index = 324,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
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
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
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
        A = (450000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1391, 'cal/mol'),
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
    index = 325,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
CO
1 C 2T {2,D}
2 O 0  {1,D}
""",
    product1 = 
"""
CH3CH2O
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
CO2
1 C 0 {2,D} {3,D}
2 O 0 {1,D}
3 O 0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
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
    index = 326,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
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
CH3CH2O
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
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5100000000000.0, 'cm^3/(mol*s)'),
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
    index = 327,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
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
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
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
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
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
    index = 328,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
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
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
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
        A = (40000000000000.0, 'cm^3/(mol*s)'),
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
    index = 329,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
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
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
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
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
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
    index = 330,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
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
CH3CH2O
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
CH3CH2O
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
        A = (5100000000000.0, 'cm^3/(mol*s)'),
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
    index = 331,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
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
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
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
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
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
    index = 332,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
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
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
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
        A = (2.4e+19, 'cm^3/(mol*s)'),
        n = -2.2,
        Ea = (14030, 'cal/mol'),
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
    index = 333,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
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
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
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
        A = (230000000000.0, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (14864, 'cal/mol'),
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
    index = 334,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product1 = 
"""
CH3CH2O
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
CH3CH2O
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
        A = (290000000000.0, 'cm^3/(mol*s)'),
        n = -0.27,
        Ea = (408, 'cal/mol'),
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
    index = 335,
    reactant1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    reactant2 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
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
CH3CH2OH
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
    product3 = 
"""
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4300000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-850, 'cal/mol'),
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
    index = 336,
    reactant1 = 
"""
CH2CH2OOH
1 O 0 {2,S} {5,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {6,S} {7,S}
4 C 1 {3,S} {8,S} {9,S}
5 H 0 {1,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product1 = 
"""
cC2H4O
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
    kinetics = Arrhenius(A=(13000000000.0, 's^-1'), n=0.72, Ea=(15380, 'cal/mol'), T0=(1, 'K')),
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
    index = 337,
    reactant1 = 
"""
CH2CH2OOH
1 O 0 {2,S} {5,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {6,S} {7,S}
4 C 1 {3,S} {8,S} {9,S}
5 H 0 {1,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product1 = 
"""
CH3CH2OO
1 O 1 {2,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {5,S} {6,S}
4 C 0 {3,S} {7,S} {8,S} {9,S}
5 H 0 {3,S}
6 H 0 {3,S}
7 H 0 {4,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(12000000.0, 's^-1'), n=1.04, Ea=(17980, 'cal/mol'), T0=(1, 'K')),
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
    index = 338,
    reactant1 = 
"""
CH2CH2OOH
1 O 0 {2,S} {5,S}
2 O 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {6,S} {7,S}
4 C 1 {3,S} {8,S} {9,S}
5 H 0 {1,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {4,S}
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
    kinetics = Arrhenius(
        A = (130000000000.0, 's^-1'),
        n = 0.52,
        Ea = (16150, 'cal/mol'),
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
    index = 339,
    reactant1 = 
"""
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    reactant2 = 
"""
H
1 H 1
""",
    product1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
        A = (43000000000.0, 'cm^3/(mol*s)'),
        n = 0,
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
    index = 340,
    reactant1 = 
"""
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
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
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000.0, 'cm^3/(mol*s)'),
        n = 0,
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
    index = 341,
    reactant1 = 
"""
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    reactant2 = 
"""
O
1 O 2T
""",
    product1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
        A = (8700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4750, 'cal/mol'),
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
    index = 342,
    reactant1 = 
"""
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
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
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
        A = (1100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-437, 'cal/mol'),
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
    index = 343,
    reactant1 = 
"""
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
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
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
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
    index = 344,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
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
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+48, 's^-1'), n=-8.868, Ea=(110591, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
100 atm
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 345,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
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
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.1e+47, 's^-1'), n=-8.701, Ea=(111046, 'cal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
100 atm
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 346,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
60atm, 6-900K fit
CH2CHOO = CYCOOC.                      3.9E09   0.000   22250  0.0 0.0 0.0
100 atm
CH2CHOO = CYCOOC.                      1.1E19  -2.782   26427  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 347,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
O2
1 O 1 {2,S}
2 O 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-145, 'cal/mol'),
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
    index = 348,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
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
        A = (2000000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
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
    index = 349,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
HO2
1 O 0 {2,S} {3,S}
2 O 1 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000000000.0, 'cm^3/(mol*s)'),
        n = 0.6,
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
    index = 350,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
        A = (450000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1391, 'cal/mol'),
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
    index = 351,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
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
    index = 352,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
CH3O
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 O 1 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5100000000000.0, 'cm^3/(mol*s)'),
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
    index = 353,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
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
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
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
    kinetics = Arrhenius(A=(47000, 'cm^3/(mol*s)'), n=2.5, Ea=(21000, 'cal/mol'), T0=(1, 'K')),
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
    index = 354,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
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
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
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
        A = (40000000000000.0, 'cm^3/(mol*s)'),
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
    index = 355,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
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
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
""",
    product2 = 
"""
HCO
1 C 1 {2,D} {3,S}
2 O 0 {1,D}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(41000, 'cm^3/(mol*s)'), n=2.5, Ea=(10206, 'cal/mol'), T0=(1, 'K')),
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
    index = 356,
    reactant1 = 
"""
CH2CHOO
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 1 {3,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
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
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {4,S}
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
    kinetics = Arrhenius(A=(8.6, 'cm^3/(mol*s)'), n=3.76, Ea=(17200, 'cal/mol'), T0=(1, 'K')),
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
    index = 357,
    reactant1 = 
"""
OCHCHO
1 C 0 {2,S} {3,D} {5,S}
2 C 0 {1,S} {4,D} {6,S}
3 O 0 {1,D}
4 O 0 {2,D}
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
CH2O
1 C 0 {2,D} {3,S} {4,S}
2 O 0 {1,D}
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
60atm, 6-900K fit
CYCOOC. = CH2O + HCO                     6.1E10   0.000     914  0.0 0.0 0.0
meohcys4e (100 atm)
CYCOOC. = OCHCHO + H                     1.6E13  -1.093    3159  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 358,
    reactant1 = 
"""
OCHCHO
1 C 0 {2,S} {3,D} {5,S}
2 C 0 {1,S} {4,D} {6,S}
3 O 0 {1,D}
4 O 0 {2,D}
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
    product3 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6600000000000.0, 'cm^3/(mol*s)'),
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
    index = 359,
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
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (8000000000000000.0, 's^-1'),
            n = 0,
            Ea = (87726, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3734000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (73479, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CFG from Glarborg



C1
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 360,
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
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(37000000000000.0, 's^-1'), n=0, Ea=(71969, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5661000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (65849, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
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
    index = 361,
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
            A = (1500000000000.0, 'cm^3/(mol*s)'),
            n = 0.6,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.5e+16, 'cm^6/(mol^2*s)'),
            n = -0.41,
            Ea = (-1116, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.0, '[O][O]': 0.78, 'O': 11.0, 'N#N': 0.0, '[Ar]': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CFG from Glarborg; extra collision efficiencies taken from Leeds
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 362,
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
        arrheniusHigh = Arrhenius(A=(400000000000.0, 's^-1'), n=0, Ea=(37137, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.291e+16, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (43638, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.5, 'O': 12.0, '[Ar]': 0.64},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
H + O2 (+AR) = HO2 (+AR)                   1.5E12   0.600       0  0.0 0.0 0.0
LOW  / 9.04E19 -1.500 490 /
TROE / 0.5 1.0E-30 1.0E30 /

H + O2 (+N2) = HO2 (+N2)                   1.5E12   0.600       0  0.0 0.0 0.0
LOW  / 6.37E20 -1.720 520 /
TROE / 0.8 1.0E-30 1.0E30 /
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 363,
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
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (18000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (2384, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.35e+24, 'cm^6/(mol^2*s)'),
            n = -2.79,
            Ea = (4191, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'C(=O)=O': 3.8, 'O': 12.0},
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
    index = 364,
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
            A = (210000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.467e+23, 'cm^6/(mol^2*s)'),
            n = -1.8,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.6376,
        T3 = (1e-30, 'K'),
        T1 = (3230, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'CC': 4.8, 'C': 1.9},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
C1 system
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 365,
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
        arrheniusHigh = Arrhenius(A=(3.8e+16, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.8e+27, 'cm^6/(mol^2*s)'),
            n = -3.14,
            Ea = (1230, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.68,
        T3 = (78, 'K'),
        T1 = (1995, 'K'),
        T2 = (5590, 'K'),
        efficiencies = {'O': 6.0, 'N#N': 1.0, '[Ar]': 0.7},
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
    index = 366,
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
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.1e+18, 's^-1'), n=-0.6148, Ea=(92540, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.6e+49, 'cm^3/(mol*s)'),
            n = -8.8,
            Ea = (101500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7656,
        T3 = (1910, 'K'),
        T1 = (59.51, 'K'),
        T2 = (9374, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
replaced by value in CFG_propane using Klippenstein's numbers
CH3 + CH3 (+M) = C2H6 (+M)                 3.6E13   0.000       0  0.0 0.0 0.0
N2/1/ H2/2/ H2O/6/ CH4/2/ CO/1.5/ CO2/2/ C2H6/3/
LOW  /1.269E41 -7.0 2762/
TROE /0.62 73 1180 1E30/
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 367,
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
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (280000000000000.0, 's^-1'),
            n = -0.73,
            Ea = (32820, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.01e+33, 'cm^3/(mol*s)'),
            n = -5.39,
            Ea = (36200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.96,
        T3 = (67.6, 'K'),
        T1 = (1855, 'K'),
        T2 = (7543, 'K'),
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
    index = 368,
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
            A = (4300000000000000.0, 'cm^3/(mol*s)'),
            n = -0.79,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.844e+37, 'cm^6/(mol^2*s)'),
            n = -6.21,
            Ea = (1333, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.25,
        T3 = (210, 'K'),
        T1 = (1434, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
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
    index = 369,
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
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(68000000000000.0, 's^-1'), n=0, Ea=(26154, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.867e+25, 'cm^3/(mol*s)'),
            n = -3,
            Ea = (24291, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1000, 'K'),
        T1 = (2000, 'K'),
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
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
    index = 370,
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
            A = (2400000000000.0, 'cm^3/(mol*s)'),
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
        efficiencies = {'C': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'C(=O)=O': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
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
    index = 371,
    reactant1 = 
"""
H
1 H 1
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
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0.0, 'O': 0.0, 'N#N': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
reduced by cfg
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 372,
    reactant1 = 
"""
H
1 H 1
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
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.2e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
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
    index = 373,
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
            A = (19000000000000.0, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[O][O]': 1.5, 'O': 10.0, 'N#N': 1.5},
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
    index = 374,
    reactant1 = 
"""
OH
1 O 1 {2,S}
2 H 0 {1,S}
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
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0.73, 'O': 12.0, '[Ar]': 0.38},
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
    index = 375,
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
            A = (10000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H]': 0.0, 'O': 0.0, 'N#N': 0.0, '[Ar]': 0.0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
C1

CH2 + M = CH + H + M                         5.6E15  0.000    89000  0.0 0.0 0.0
CH2 + M = C + H2 + M                         5.8E12  0.500    68500  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 376,
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
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (93000000000.0, 'cm^3/(mol*s)'),
                        n = 0,
                        Ea = (0, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (80000000000.0, 'cm^3/(mol*s)'),
                        n = 0,
                        Ea = (0, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (70000000000.0, 'cm^3/(mol*s)'),
                        n = 0,
                        Ea = (0, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (3700000000000.0, 'cm^3/(mol*s)'),
                        n = 0,
                        Ea = (12518, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2900000000000.0, 'cm^3/(mol*s)'),
                        n = 0,
                        Ea = (11922, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1500000000000.0, 'cm^3/(mol*s)'),
                        n = 0,
                        Ea = (13909, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (150000000000.0, 'cm^3/(mol*s)'),
                        n = 0,
                        Ea = (1987, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (150000000000.0, 'cm^3/(mol*s)'),
                        n = 0,
                        Ea = (1987, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (230000000000.0, 'cm^3/(mol*s)'),
                        n = 0.2,
                        Ea = (4968, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (37000000.0, 'cm^3/(mol*s)'),
                        n = 1.34,
                        Ea = (2186, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
                highPlimit = Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(1, 'cal/mol'), T0=(1, 'K')),
            ),
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(A=(710000, 'cm^3/(mol*s)'), n=1.8, Ea=(1133, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(880000, 'cm^3/(mol*s)'), n=1.77, Ea=(954, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(290000, 'cm^3/(mol*s)'), n=1.9, Ea=(397, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(93000000.0, 'cm^3/(mol*s)'), n=1.1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(45000000.0, 'cm^3/(mol*s)'), n=1.2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5800000.0, 'cm^3/(mol*s)'), n=1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(250000, 'cm^3/(mol*s)'), n=1.9, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(190000, 'cm^3/(mol*s)'), n=1.94, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(700000, 'cm^3/(mol*s)'), n=1.7, Ea=(298, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                ],
                highPlimit = Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(2, 'cal/mol'), T0=(1, 'K')),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
PLOG Reactions: CO/CO2 subset                                            *
*****************************************************************************

(0.001-2000 bar, 300<T<2000K)
Well-skipping reaction, so high-P limit is zero.


(0.001-2000 bar, 300<T<2000K)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 378,
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
HOCO
1 C 1 {2,S} {3,D}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
4 H 0 {2,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(A=(1e+25, 'cm^3/(mol*s)'), n=-6, Ea=(2981, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6e+26, 'cm^3/(mol*s)'), n=-5.6, Ea=(2881, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (2.2e+27, 'cm^3/(mol*s)'),
                        n = -5.6,
                        Ea = (3239, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1.5e+25, 'cm^3/(mol*s)'), n=-5, Ea=(1987, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (4.2e+26, 'cm^3/(mol*s)'),
                        n = -5.7,
                        Ea = (1927, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.9e+25, 'cm^3/(mol*s)'),
                        n = -5.2,
                        Ea = (1987, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.2e+25, 'cm^3/(mol*s)'),
                        n = -5.2,
                        Ea = (1987, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1.1e+28, 'cm^3/(mol*s)'), n=-6, Ea=(2384, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.2e+41, 'cm^3/(mol*s)'), n=-10, Ea=(6955, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5.5e+44, 'cm^3/(mol*s)'), n=-11, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
                ],
                highPlimit = Arrhenius(A=(5.5e+44, 'cm^3/(mol*s)'), n=-11, Ea=(7948, 'cal/mol'), T0=(1, 'K')),
            ),
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (1.3e+37, 'cm^3/(mol*s)'),
                        n = -8.4,
                        Ea = (7948, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(7.5e+28, 'cm^3/(mol*s)'), n=-6, Ea=(3775, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4e+38, 'cm^3/(mol*s)'), n=-9, Ea=(6955, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(7.7e+35, 'cm^3/(mol*s)'), n=-8, Ea=(6557, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.8e+36, 'cm^3/(mol*s)'), n=-8, Ea=(7153, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (2.9e+66, 'cm^3/(mol*s)'),
                        n = -17.1,
                        Ea = (19870, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.7e+67, 'cm^3/(mol*s)'),
                        n = -17,
                        Ea = (22851, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
                highPlimit = Arrhenius(
                    A = (2.7e+67, 'cm^3/(mol*s)'),
                    n = -17,
                    Ea = (22851, 'cal/mol'),
                    T0 = (1, 'K'),
                ),
            ),
            PDepArrhenius(
                pressures = ([0.001, 1, 3, 10, 20, 50, 80, 100, 650, 2000], 'atm'),
                arrhenius = [
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4e+39, 'cm^3/(mol*s)'), n=-9, Ea=(9935, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(5e+43, 'cm^3/(mol*s)'), n=-10, Ea=(13015, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (9e+47, 'cm^3/(mol*s)'),
                        n = -11.2,
                        Ea = (15499, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(2e+54, 'cm^3/(mol*s)'), n=-13, Ea=(19671, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (2e+63, 'cm^3/(mol*s)'),
                        n = -15.2,
                        Ea = (27421, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(1e+74, 'cm^3/(mol*s)'), n=-18, Ea=(37157, 'cal/mol'), T0=(1, 'K')),
                ],
                highPlimit = Arrhenius(A=(1e+74, 'cm^3/(mol*s)'), n=-18, Ea=(37157, 'cal/mol'), T0=(1, 'K')),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
(0.001-2000 bar, 300<T<2000K)


(0.001 bar, 300<T<2000K)


(0.001 bar, 300<T<2000K)
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 381,
    reactant1 = 
"""
HOCO
1 C 1 {2,S} {3,D}
2 O 0 {1,S} {4,S}
3 O 0 {1,D}
4 H 0 {2,S}
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
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([1, 10, 20, 50, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(3.5e+56, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(3.2e+57, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(6e+57, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1.4e+58, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.8e+58, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
                ],
                highPlimit = Arrhenius(A=(2.8e+58, 's^-1'), n=-15, Ea=(46500, 'cal/mol'), T0=(1, 'K')),
            ),
            PDepArrhenius(
                pressures = ([1, 10, 20, 50, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(2.5e+69, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2.2e+70, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(4.3e+70, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(1e+71, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(2e+71, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
                ],
                highPlimit = Arrhenius(A=(2e+71, 's^-1'), n=-18, Ea=(60000, 'cal/mol'), T0=(1, 'K')),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
(1-100 bar, 300<T<2000K)
HOCO = CO2 + H         3.5E56*P[bar]^0.95 -15.000   46500



(1-100 bar, 300<T<2000K)
HOCO = CO2 + H               2.5E69*P[bar]^0.95 -18.000   60000
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 383,
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 20, 50, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (990000000000.0, 's^-1'),
                n = -0.865,
                Ea = (16755, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7200000000000.0, 's^-1'),
                n = -0.865,
                Ea = (16755, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (13000000000000.0, 's^-1'),
                n = -0.865,
                Ea = (16755, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (29000000000000.0, 's^-1'),
                n = -0.865,
                Ea = (16755, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (53000000000000.0, 's^-1'),
                n = -0.865,
                Ea = (16755, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        highPlimit = Arrhenius(
            A = (53000000000000.0, 's^-1'),
            n = -0.865,
            Ea = (16755, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
PLOG Reactions: CH2O subset                                              *
*****************************************************************************


General pressure dependency
HCO = H + CO               9.83E11*P[bar]^0.865  -0.865   16755  0.0 0.0 0.0
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 384,
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
CH3OO
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 O 0 {1,S} {3,S}
3 O 1 {2,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([1, 10, 20, 50, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(5e+22, 'cm^3/(mol*s)'), n=-3.85, Ea=(2000, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.4e+21, 'cm^3/(mol*s)'),
                        n = -3.2,
                        Ea = (2300, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.1e+20, 'cm^3/(mol*s)'),
                        n = -2.94,
                        Ea = (1900, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (2.8e+18, 'cm^3/(mol*s)'),
                        n = -2.2,
                        Ea = (1400, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.1e+19, 'cm^3/(mol*s)'),
                        n = -2.3,
                        Ea = (1800, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
                highPlimit = Arrhenius(
                    A = (1.1e+19, 'cm^3/(mol*s)'),
                    n = -2.3,
                    Ea = (1800, 'cal/mol'),
                    T0 = (1, 'K'),
                ),
            ),
            PDepArrhenius(
                pressures = ([1, 10, 20, 50, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(A=(0, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (3.3e+29, 'cm^3/(mol*s)'),
                        n = -5.6,
                        Ea = (6850, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (5.6e+28, 'cm^3/(mol*s)'),
                        n = -5.25,
                        Ea = (6850, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.1e+30, 'cm^3/(mol*s)'),
                        n = -5.7,
                        Ea = (8750, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
                highPlimit = Arrhenius(
                    A = (4.1e+30, 'cm^3/(mol*s)'),
                    n = -5.7,
                    Ea = (8750, 'cal/mol'),
                    T0 = (1, 'K'),
                ),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
*****************************************************************************
PLOG Reactions:  CH4 subset                                              *
*****************************************************************************


fit to FER/TRO06
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 386,
    reactant1 = 
"""
CH3OOH
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 50, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(2e+35, 's^-1'), n=-6.7, Ea=(47450, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e+28, 's^-1'), n=-4.15, Ea=(46190, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+26, 's^-1'), n=-3.5, Ea=(46340, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.2e+17, 's^-1'), n=-0.42, Ea=(44622, 'cal/mol'), T0=(1, 'K')),
        ],
        highPlimit = Arrhenius(A=(2.2e+17, 's^-1'), n=-0.42, Ea=(44622, 'cal/mol'), T0=(1, 'K')),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's high-PL rate
1000 atm rate is Glarborg's high-PL rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 387,
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
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1800000.0, 'cm^3/(mol*s)'),
                n = 1.68,
                Ea = (2061, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (2400000000.0, 'cm^3/(mol*s)'),
                n = 0.56,
                Ea = (6007, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (28000000000000.0, 'cm^3/(mol*s)'),
                n = -0.5,
                Ea = (11455, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        highPlimit = Arrhenius(
            A = (28000000000000.0, 'cm^3/(mol*s)'),
            n = -0.5,
            Ea = (11455, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Since CFG converted all CH2OOH into CH2O + OH, this reaction is redundant.
1 atm
CH2OOH => CH2O + OH                      2.4E12  -0.925    1567  0.0 0.0 0.0
10 atm
CH2OOH => CH2O + OH                      2.5E13  -0.927    1579  0.0 0.0 0.0
100 atm
CH2OOH => CH2O + OH                      7.0E14  -1.064    1744  0.0 0.0 0.0
However, if it did exist, it would look something like this in PLOG form:
// High-P limit rate is Garborg's 100 atm rate
CH2OOH => CH2O + OH       7.0E14  -1.064    1744      0.0 0.0 0.0
PLOG  /         1             2.4E12  -0.925    1567 /
PLOG  /         10            2.5E13  -0.927    1579 /
PLOG  /         100           7.0E14  -1.064    1744 /

*****************************************************************************
PLOG Reactions:  C2 subset                                              *
*****************************************************************************



JIM/GLA08 fit to SEN/MIL06 60 atm,600-900K
C2H4+OH=CH3+CH2O                     3.3E11   0.000    9079
High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 388,
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(0.024, 'cm^3/(mol*s)'), n=3.91, Ea=(1723, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (820000000.0, 'cm^3/(mol*s)'),
                n = 1.01,
                Ea = (10507, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (6800000000.0, 'cm^3/(mol*s)'),
                n = 0.81,
                Ea = (13867, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        highPlimit = Arrhenius(
            A = (6800000000.0, 'cm^3/(mol*s)'),
            n = 0.81,
            Ea = (13867, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
JIM/GLA08 fit to SEN/MIL06 60 atm,600-900K
C2H4+OH=CH3CHO+H                     1.4E33  -6.114   24907
High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 389,
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
CH2CHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 O 0 {1,S} {7,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(320000, 'cm^3/(mol*s)'), n=2.19, Ea=(5256, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (190000000.0, 'cm^3/(mol*s)'),
                n = 1.43,
                Ea = (7829, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (85000000000.0, 'cm^3/(mol*s)'),
                n = 0.75,
                Ea = (11491, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        highPlimit = Arrhenius(
            A = (85000000000.0, 'cm^3/(mol*s)'),
            n = 0.75,
            Ea = (11491, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
JIM/GLA08 fit to SEN/MIL06 60 atm,600-900K
C2H4+OH=CH2CHOH+H                    1.7E13   0.000   11527
High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 390,
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
CH2CH2OH
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 C 1 {1,S} {6,S} {7,S}
3 O 0 {1,S} {8,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {2,S}
7 H 0 {2,S}
8 H 0 {3,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(A=(6e+37, 'cm^3/(mol*s)'), n=-8.14, Ea=(8043, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (6e+37, 'cm^3/(mol*s)'),
                        n = -7.77,
                        Ea = (10736, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6e+37, 'cm^3/(mol*s)'),
                        n = -7.44,
                        Ea = (14269, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
                highPlimit = Arrhenius(
                    A = (6e+37, 'cm^3/(mol*s)'),
                    n = -7.44,
                    Ea = (14269, 'cal/mol'),
                    T0 = (1, 'K'),
                ),
            ),
            PDepArrhenius(
                pressures = ([1, 10, 100], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (7.3e+23, 'cm^3/(mol*s)'),
                        n = -6.91,
                        Ea = (2855, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(A=(3e+26, 'cm^3/(mol*s)'), n=-4.87, Ea=(2297, 'cal/mol'), T0=(1, 'K')),
                    Arrhenius(
                        A = (2.8e+19, 'cm^3/(mol*s)'),
                        n = -2.41,
                        Ea = (1011, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
                highPlimit = Arrhenius(
                    A = (2.8e+19, 'cm^3/(mol*s)'),
                    n = -2.41,
                    Ea = (1011, 'cal/mol'),
                    T0 = (1, 'K'),
                ),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's 100 atm rate


High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 392,
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (1300000000.0, 'cm^3/(mol*s)'),
                n = 0.73,
                Ea = (2579, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (430000000.0, 'cm^3/(mol*s)'),
                n = 0.92,
                Ea = (3736, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(830000, 'cm^3/(mol*s)'), n=1.77, Ea=(4697, 'cal/mol'), T0=(1, 'K')),
        ],
        highPlimit = Arrhenius(A=(830000, 'cm^3/(mol*s)'), n=1.77, Ea=(4697, 'cal/mol'), T0=(1, 'K')),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 393,
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
HCCOH
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 O 0 {1,S} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (2400000.0, 'cm^3/(mol*s)'),
                n = 2,
                Ea = (12713, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (3200000.0, 'cm^3/(mol*s)'),
                n = 1.97,
                Ea = (12810, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (7300000.0, 'cm^3/(mol*s)'),
                n = 1.89,
                Ea = (13603, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        highPlimit = Arrhenius(
            A = (7300000.0, 'cm^3/(mol*s)'),
            n = 1.89,
            Ea = (13603, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 394,
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
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {3,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiPDepArrhenius(
        arrhenius = [
            PDepArrhenius(
                pressures = ([1, 10, 100, 1000], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (1.9e+44, 'cm^3/(mol*s)'),
                        n = -11.38,
                        Ea = (6299, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.5e+24, 'cm^3/(mol*s)'),
                        n = -4.06,
                        Ea = (3261, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (6.2e+20, 'cm^3/(mol*s)'),
                        n = -2.8,
                        Ea = (2831, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (110000000.0, 'cm^3/(mol*s)'),
                        n = 1.34,
                        Ea = (332, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
                highPlimit = Arrhenius(
                    A = (110000000.0, 'cm^3/(mol*s)'),
                    n = 1.34,
                    Ea = (332, 'cal/mol'),
                    T0 = (1, 'K'),
                ),
            ),
            PDepArrhenius(
                pressures = ([1, 10, 100, 1000], 'atm'),
                arrhenius = [
                    Arrhenius(
                        A = (3.5e+31, 'cm^3/(mol*s)'),
                        n = -6.2,
                        Ea = (6635, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (4.5e+31, 'cm^3/(mol*s)'),
                        n = -5.92,
                        Ea = (8761, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (1.6e+29, 'cm^3/(mol*s)'),
                        n = -4.91,
                        Ea = (9734, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                    Arrhenius(
                        A = (60000000.0, 'cm^3/(mol*s)'),
                        n = 1.62,
                        Ea = (240, 'cal/mol'),
                        T0 = (1, 'K'),
                    ),
                ],
                highPlimit = Arrhenius(
                    A = (60000000.0, 'cm^3/(mol*s)'),
                    n = 1.62,
                    Ea = (240, 'cal/mol'),
                    T0 = (1, 'K'),
                ),
            ),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's >>100 atm rate
1000 atm rate is Glarborg's ">>100 atm" rate


High-P limit rate is Garborg's >>100 atm rate
1000 atm rate is Glarborg's ">>100 atm" rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 396,
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (7500000.0, 'cm^3/(mol*s)'),
                n = 1.55,
                Ea = (2106, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (5100000.0, 'cm^3/(mol*s)'),
                n = 1.65,
                Ea = (3400, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(15000, 'cm^3/(mol*s)'), n=2.45, Ea=(4477, 'cal/mol'), T0=(1, 'K')),
        ],
        highPlimit = Arrhenius(A=(15000, 'cm^3/(mol*s)'), n=2.45, Ea=(4477, 'cal/mol'), T0=(1, 'K')),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 397,
    reactant1 = 
"""
CHCHOH
1 C 0 {2,D} {3,S} {4,S}
2 C 1 {1,D} {5,S}
3 O 0 {1,S} {6,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {3,S}
""",
    product1 = 
"""
HCCOH
1 C 0 {2,T} {3,S}
2 C 0 {1,T} {4,S}
3 O 0 {1,S} {5,S}
4 H 0 {2,S}
5 H 0 {3,S}
""",
    product2 = 
"""
H
1 H 1
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.1e+31, 's^-1'), n=-6.153, Ea=(51383, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.5e+32, 's^-1'), n=-6.168, Ea=(52239, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.5e+29, 's^-1'), n=-5.057, Ea=(52377, 'cal/mol'), T0=(1, 'K')),
        ],
        highPlimit = Arrhenius(A=(5.5e+29, 's^-1'), n=-5.057, Ea=(52377, 'cal/mol'), T0=(1, 'K')),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 398,
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
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(2.4e+25, 's^-1'), n=-4.8, Ea=(43424, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.4e+30, 's^-1'), n=-5.86, Ea=(46114, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+34, 's^-1'), n=-6.57, Ea=(49454, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(3.5e+36, 's^-1'), n=-6.92, Ea=(52979, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.2e+36, 's^-1'), n=-6.48, Ea=(55171, 'cal/mol'), T0=(1, 'K')),
        ],
        highPlimit = Arrhenius(
            A = (1400000000000000.0, 's^-1'),
            n = -0.15,
            Ea = (45606, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's high-PL rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 399,
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
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(1.2e+30, 's^-1'), n=-6.07, Ea=(41332, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.4e+32, 's^-1'), n=-6.57, Ea=(44282, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.5e+34, 's^-1'), n=-6.87, Ea=(47191, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.2e+35, 's^-1'), n=-6.76, Ea=(49548, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.2e+33, 's^-1'), n=-5.97, Ea=(50448, 'cal/mol'), T0=(1, 'K')),
        ],
        highPlimit = Arrhenius(
            A = (2900000000000.0, 's^-1'),
            n = 0.29,
            Ea = (40326, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's high-PL rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 400,
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (5.7e+17, 'cm^3/(mol*s)'),
                n = -1.757,
                Ea = (11067, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (110000000000000.0, 'cm^3/(mol*s)'),
                n = -0.61,
                Ea = (11422, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1.5e-10, 'cm^3/(mol*s)'),
                n = 6.69,
                Ea = (4868, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        highPlimit = Arrhenius(
            A = (1.5e-10, 'cm^3/(mol*s)'),
            n = 6.69,
            Ea = (4868, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 401,
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
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (690000000000000.0, 's^-1'),
                n = -1.97,
                Ea = (14584, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(2e+16, 's^-1'), n=-2.09, Ea=(15197, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(6.5e+18, 's^-1'), n=-2.52, Ea=(16436, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.2e+19, 's^-1'), n=-2.55, Ea=(17263, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.3e+20, 's^-1'), n=-2.32, Ea=(18012, 'cal/mol'), T0=(1, 'K')),
        ],
        highPlimit = Arrhenius(
            A = (1100000000000.0, 's^-1'),
            n = 0.63,
            Ea = (16895, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's high-PL rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 402,
    reactant1 = 
"""
CH3CH2OOH
1  O 0 {2,S} {5,S}
2  O 0 {1,S} {3,S}
3  C 0 {2,S} {4,S} {6,S} {7,S}
4  C 0 {3,S} {8,S} {9,S} {10,S}
5  H 0 {1,S}
6  H 0 {3,S}
7  H 0 {3,S}
8  H 0 {4,S}
9  H 0 {4,S}
10 H 0 {4,S}
""",
    product1 = 
"""
CH3CH2O
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(2e+35, 's^-1'), n=-6.7, Ea=(47450, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e+28, 's^-1'), n=-4.15, Ea=(46190, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+26, 's^-1'), n=-3.5, Ea=(46340, 'cal/mol'), T0=(1, 'K')),
        ],
        highPlimit = Arrhenius(A=(2.2e+17, 's^-1'), n=-0.42, Ea=(44622, 'cal/mol'), T0=(1, 'K')),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
( = CH3OOH = CH3O + OH[ZHU/LIN01b],high P limit)
High-P limit rate is Garborg's high-PL rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 403,
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(
                A = (3500000000000.0, 'cm^3/(mol*s)'),
                n = -0.947,
                Ea = (979, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (35000000000000.0, 'cm^3/(mol*s)'),
                n = -0.947,
                Ea = (980, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (580000000000000.0, 'cm^3/(mol*s)'),
                n = -1.012,
                Ea = (1068, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        highPlimit = Arrhenius(
            A = (580000000000000.0, 'cm^3/(mol*s)'),
            n = -1.012,
            Ea = (1068, 'cal/mol'),
            T0 = (1, 'K'),
        ),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
High-P limit rate is Garborg's 100 atm rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 404,
    reactant1 = 
"""
CH2CHOOH
1 C 0 {2,D} {3,S} {5,S}
2 C 0 {1,D} {6,S} {7,S}
3 O 0 {1,S} {4,S}
4 O 0 {3,S} {8,S}
5 H 0 {1,S}
6 H 0 {2,S}
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 50], 'atm'),
        arrhenius = [
            Arrhenius(A=(2e+35, 's^-1'), n=-6.7, Ea=(47450, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e+28, 's^-1'), n=-4.15, Ea=(46190, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+26, 's^-1'), n=-3.5, Ea=(46340, 'cal/mol'), T0=(1, 'K')),
        ],
        highPlimit = Arrhenius(A=(2.2e+17, 's^-1'), n=-0.42, Ea=(44622, 'cal/mol'), T0=(1, 'K')),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
est = CH3OOH = CH3O + OH,high P limit)
High-P limit rate is Garborg's high-PL rate
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

