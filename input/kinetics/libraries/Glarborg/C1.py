#!/usr/bin/env python
# encoding: utf-8

name = "Glarborg/C1"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
O
1     O     2T
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+15,"cm^3/(mol*s)"),
        n = -0.41,
        Ea = (16600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
H
1     H     1
""",
    reactant3 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+17,"cm^6/(mol^2*s)"),
        n = -0.6,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
H
1     H     1
""",
    reactant3 = 
"""
H2O
1     O     0
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+19,"cm^6/(mol^2*s)"),
        n = -1,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (3.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (7948,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (8.8e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19175,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
O
1     O     2T
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4300,"cm^3/(mol*s)"),
        n = 2.7,
        Ea = (-1822,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+08,"cm^3/(mol*s)"),
        n = 1.52,
        Ea = (3449,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (740000,"cm^3/(mol*s)"),
        n = 2.433,
        Ea = (53502,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-445,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.89e+13,"cm^3/(mol*s)","*|/",1.58),
        n = 0,
        Ea = (-497,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.9e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1408,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11034,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3580,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3760,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.6e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (3970,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.9e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (427,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.6e+18,"cm^3/(mol*s)"),
        n = 0,
        Ea = (29410,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (60500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000,"cm^3/(mol*s)"),
        n = 2.18,
        Ea = (17943,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
HOCO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (4.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-89,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
HOCO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (9.5e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-89,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
HOCO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
HOCO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.9e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1e+08,"cm^3/(mol*s)"),
        n = 1.47,
        Ea = (2444,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.2e+11,"cm^3/(mol*s)"),
        n = 0.57,
        Ea = (2760,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (240000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (36461,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e+07,"cm^3/(mol*s)"),
        n = 1.63,
        Ea = (-1055,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (41000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (10206,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32,"cm^3/(mol*s)"),
        n = 3.36,
        Ea = (4310,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4100,"cm^3/(mol*s)"),
        n = 3.156,
        Ea = (8755,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (440000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (6577,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+06,"cm^3/(mol*s)"),
        n = 2.182,
        Ea = (2506,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (21000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10030,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    reactant1 = 
"""
CH4
1     C     0
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.9e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1100,"cm^3/(mol*s)"),
        n = 3,
        Ea = (2780,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
H2O
1     O     0
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+15,"cm^3/(mol*s)"),
        n = -0.6,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH4
1     C     0
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000,"cm^3/(mol*s)"),
        n = 2.228,
        Ea = (-3020,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
        n = 0.2688,
        Ea = (-687.5,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (28297,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.9e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (9842,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH4
1     C     0
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (16055,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+22,"cm^3/(mol*s)"),
        n = -3.3,
        Ea = (2867,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+21,"cm^3/(mol*s)"),
        n = -3.3,
        Ea = (2867,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+21,"cm^3/(mol*s)"),
        n = -3.3,
        Ea = (2867,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6e+21,"cm^3/(mol*s)"),
        n = -3.3,
        Ea = (2867,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+21,"cm^3/(mol*s)"),
        n = -3.3,
        Ea = (2867,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 67,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
H2O
1     O     0
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.9e+09,"cm^3/(mol*s)"),
        n = 1.24,
        Ea = (4491,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+08,"cm^3/(mol*s)"),
        n = 1.24,
        Ea = (4491,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5305,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (5305,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+08,"cm^3/(mol*s)"),
        n = 1.4434,
        Ea = (113,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.7e+07,"cm^3/(mol*s)"),
        n = 1.4434,
        Ea = (113,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (46600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (54800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-693,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (7.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3736,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (2.9e+16,"cm^3/(mol*s)"),
        n = -1.5,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5500,"cm^3/(mol*s)"),
        n = 2.81,
        Ea = (5862,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 93,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
CH4
1     C     0
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22,"cm^3/(mol*s)"),
        n = 3.1,
        Ea = (16227,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (745,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (745,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1749,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.5e+25,"cm^3/(mol*s)"),
        n = -4.93,
        Ea = (9080,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH4
1     C     0
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15073,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2981,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    reactant1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    reactant1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.4e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    reactant1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    reactant1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    reactant1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.7e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (4750,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    reactant1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-437,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
    reactant1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.2e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-258,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    reactant1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (41000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (10206,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-445,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+15,"cm^3/(mol*s)"),
        n = -0.6,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+11,"cm^3/(mol*s)"),
        n = 0.6,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.5e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1490,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1411,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH4
1     C     0
""",
    product1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (21000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
H
1     H     1
""",
    product3 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000,"cm^3/(mol*s)"),
        n = 2.18,
        Ea = (17940,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (41000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (10206,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (0,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (19400,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (1.1e+18,"cm^3/(mol*s)"),
        n = -2.4,
        Ea = (1800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (7e+10,"cm^3/(mol*s)"),
        n = 0,
        Ea = (800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"cm^3/(mol*s)"),
        n = -0.55,
        Ea = (-1600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
CH3CH2O
1     C     0 {2,S}
2     C     0 {1,S} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.1e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-1410,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    reactant1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
C2H5
1     C     1 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (19,"cm^3/(mol*s)"),
        n = 3.64,
        Ea = (17100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(8e+15,"s^-1"), n=0, Ea=(87726,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(3.734e+15,"s^-1"), n=0, Ea=(73479,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "N#N": 1, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
    reactant1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(3.7e+13,"s^-1"), n=0, Ea=(71969,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(5.661e+15,"s^-1"), n=0, Ea=(65849,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "N#N": 1, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.5e+12,"cm^3/(mol*s)"), n=0.6, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(3.5e+16,"cm^3/(mol*s)"), n=-0.41, Ea=(-1116,"cal/mol"), T0=1),
        efficiencies = {"N#N": 0, "O": 11, "[Ar]": 0, "[H][H]": 2, "[O][O]": 0.78},
        alpha = 0.5,
        T3 = (1e-30,"K"),
        T1 = (1e+30,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    reactant1 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4e+11,"s^-1"), n=0, Ea=(37137,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(2.291e+16,"s^-1"), n=0, Ea=(43638,"cal/mol"), T0=1),
        efficiencies = {"O": 12, "[Ar]": 0.64, "[H][H]": 2.5},
        alpha = 0.5,
        T3 = (1e-30,"K"),
        T1 = (1e+30,"K"),
        T2 = (1e+30,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.8e+10,"cm^3/(mol*s)"), n=0, Ea=(2384,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.35e+24,"cm^3/(mol*s)"), n=-2.79, Ea=(4191,"cal/mol"), T0=1),
        efficiencies = {"C(=O)=O": 3.8, "O": 12, "[C]=O": 1.9, "[H][H]": 2.5},
        alpha = 1,
        T3 = (1e-30,"K"),
        T1 = (1e+30,"K"),
        T2 = (1e+30,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 135,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.1e+14,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(6.467e+23,"cm^3/(mol*s)"), n=-1.8, Ea=(0,"cal/mol"), T0=1),
        efficiencies = {"C": 1.9, "CC": 4.8},
        alpha = 0.6376,
        T3 = (1e-30,"K"),
        T1 = (3230,"K"),
        T2 = (1e+30,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.8e+16,"cm^3/(mol*s)"), n=-0.8, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(4.8e+27,"cm^3/(mol*s)"), n=-3.14, Ea=(1230,"cal/mol"), T0=1),
        efficiencies = {"N#N": 1, "O": 6, "[Ar]": 0.7},
        alpha = 0.68,
        T3 = (78,"K"),
        T1 = (1995,"K"),
        T2 = (5590,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.6e+13,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.269e+41,"cm^3/(mol*s)"), n=-7, Ea=(2762,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "N#N": 1, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.62,
        T3 = (73,"K"),
        T1 = (1180,"K"),
        T2 = (1e+30,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
    reactant1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.1e+18,"s^-1"), n=-0.6148, Ea=(92540,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(2.6e+49,"s^-1"), n=-8.8, Ea=(101500,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "N#N": 1, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.7656,
        T3 = (1910,"K"),
        T1 = (59.51,"K"),
        T2 = (9374,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 139,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.8e+14,"s^-1"), n=-0.73, Ea=(32820,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(6.01e+33,"s^-1"), n=-5.39, Ea=(36200,"cal/mol"), T0=1),
        efficiencies = {"C(=O)=O": 3, "O": 5, "[C]=O": 2, "[H][H]": 2},
        alpha = 0.96,
        T3 = (67.6,"K"),
        T1 = (1855,"K"),
        T2 = (7543,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    reactant1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.3e+15,"cm^3/(mol*s)"), n=-0.79, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(3.844e+37,"cm^3/(mol*s)"), n=-6.21, Ea=(1333,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "N#N": 1, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.25,
        T3 = (210,"K"),
        T1 = (1434,"K"),
        T2 = (1e+30,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.8e+13,"s^-1"), n=0, Ea=(26154,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.867e+25,"s^-1"), n=-3, Ea=(24291,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "N#N": 1, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.5,
        T3 = (1000,"K"),
        T1 = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    reactant1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.4e+12,"cm^3/(mol*s)"), n=0.515, Ea=(50,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(4.66e+41,"cm^3/(mol*s)"), n=-7.44, Ea=(14080,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "N#N": 1, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.7,
        T3 = (100,"K"),
        T1 = (90000,"K"),
        T2 = (10000,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(7e+17,"cm^3/(mol*s)"), n=-1, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"N#N": 0, "O": 0, "[H][H]": 0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(6.2e+16,"cm^3/(mol*s)"), n=-0.6, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"O": 5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(1.9e+13,"cm^3/(mol*s)"), n=0, Ea=(-1788,"cal/mol"), T0=(1,"K")),
        efficiencies = {"N#N": 1.5, "O": 10, "[O][O]": 1.5},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(4.5e+22,"cm^3/(mol*s)"), n=-2, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"O": 12, "[Ar]": 0.38, "[H][H]": 0.73},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    product1 = 
"""
CH2
1     C     2T
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(1e+13,"s^-1"), n=0, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"N#N": 0, "O": 0, "[Ar]": 0, "[H]": 0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.001,1,3,10,20,50,80,100,650,2000],"atm"),
        arrhenius = [
            Arrhenius(A=(9.3e+10,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(8e+10,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(7e+10,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(3.7e+12,"cm^3/(mol*s)"), n=0, Ea=(12518,"cal/mol"), T0=1),
            Arrhenius(A=(2.9e+12,"cm^3/(mol*s)"), n=0, Ea=(11922,"cal/mol"), T0=1),
            Arrhenius(A=(1.5e+12,"cm^3/(mol*s)"), n=0, Ea=(13909,"cal/mol"), T0=1),
            Arrhenius(A=(1.5e+11,"cm^3/(mol*s)"), n=0, Ea=(1987,"cal/mol"), T0=1),
            Arrhenius(A=(1.5e+11,"cm^3/(mol*s)"), n=0, Ea=(1987,"cal/mol"), T0=1),
            Arrhenius(A=(2.3e+11,"cm^3/(mol*s)"), n=0.2, Ea=(4968,"cal/mol"), T0=1),
            Arrhenius(A=(3.7e+07,"cm^3/(mol*s)"), n=1.34, Ea=(2186,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.001,1,3,10,20,50,80,100,650,2000],"atm"),
        arrhenius = [
            Arrhenius(A=(710000,"cm^3/(mol*s)"), n=1.8, Ea=(1133,"cal/mol"), T0=1),
            Arrhenius(A=(880000,"cm^3/(mol*s)"), n=1.77, Ea=(954,"cal/mol"), T0=1),
            Arrhenius(A=(290000,"cm^3/(mol*s)"), n=1.9, Ea=(397,"cal/mol"), T0=1),
            Arrhenius(A=(9.3e+07,"cm^3/(mol*s)"), n=1.1, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(4.5e+07,"cm^3/(mol*s)"), n=1.2, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(5.8e+06,"cm^3/(mol*s)"), n=1.5, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(250000,"cm^3/(mol*s)"), n=1.9, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(190000,"cm^3/(mol*s)"), n=1.94, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(700000,"cm^3/(mol*s)"), n=1.7, Ea=(298,"cal/mol"), T0=1),
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 150,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HOCO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.001,1,3,10,20,50,80,100,650,2000],"atm"),
        arrhenius = [
            Arrhenius(A=(1e+25,"cm^3/(mol*s)"), n=-6, Ea=(2981,"cal/mol"), T0=1),
            Arrhenius(A=(6e+26,"cm^3/(mol*s)"), n=-5.6, Ea=(2881,"cal/mol"), T0=1),
            Arrhenius(A=(2.2e+27,"cm^3/(mol*s)"), n=-5.6, Ea=(3239,"cal/mol"), T0=1),
            Arrhenius(A=(1.5e+25,"cm^3/(mol*s)"), n=-5, Ea=(1987,"cal/mol"), T0=1),
            Arrhenius(A=(4.2e+26,"cm^3/(mol*s)"), n=-5.7, Ea=(1927,"cal/mol"), T0=1),
            Arrhenius(A=(4.9e+25,"cm^3/(mol*s)"), n=-5.2, Ea=(1987,"cal/mol"), T0=1),
            Arrhenius(A=(5.2e+25,"cm^3/(mol*s)"), n=-5.2, Ea=(1987,"cal/mol"), T0=1),
            Arrhenius(A=(1.1e+28,"cm^3/(mol*s)"), n=-6, Ea=(2384,"cal/mol"), T0=1),
            Arrhenius(A=(3.2e+41,"cm^3/(mol*s)"), n=-10, Ea=(6955,"cal/mol"), T0=1),
            Arrhenius(A=(5.5e+44,"cm^3/(mol*s)"), n=-11, Ea=(7948,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HOCO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.001,1,3,10,20,50,80,100,650,2000],"atm"),
        arrhenius = [
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(1.3e+37,"cm^3/(mol*s)"), n=-8.4, Ea=(7948,"cal/mol"), T0=1),
            Arrhenius(A=(7.5e+28,"cm^3/(mol*s)"), n=-6, Ea=(3775,"cal/mol"), T0=1),
            Arrhenius(A=(4e+38,"cm^3/(mol*s)"), n=-9, Ea=(6955,"cal/mol"), T0=1),
            Arrhenius(A=(7.7e+35,"cm^3/(mol*s)"), n=-8, Ea=(6557,"cal/mol"), T0=1),
            Arrhenius(A=(1.8e+36,"cm^3/(mol*s)"), n=-8, Ea=(7153,"cal/mol"), T0=1),
            Arrhenius(A=(2.9e+66,"cm^3/(mol*s)"), n=-17.1, Ea=(19870,"cal/mol"), T0=1),
            Arrhenius(A=(2.7e+67,"cm^3/(mol*s)"), n=-17, Ea=(22851,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
    reactant1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HOCO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([0.001,1,3,10,20,50,80,100,650,2000],"atm"),
        arrhenius = [
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(4e+39,"cm^3/(mol*s)"), n=-9, Ea=(9935,"cal/mol"), T0=1),
            Arrhenius(A=(5e+43,"cm^3/(mol*s)"), n=-10, Ea=(13015,"cal/mol"), T0=1),
            Arrhenius(A=(9e+47,"cm^3/(mol*s)"), n=-11.2, Ea=(15499,"cal/mol"), T0=1),
            Arrhenius(A=(2e+54,"cm^3/(mol*s)"), n=-13, Ea=(19671,"cal/mol"), T0=1),
            Arrhenius(A=(2e+63,"cm^3/(mol*s)"), n=-15.2, Ea=(27421,"cal/mol"), T0=1),
            Arrhenius(A=(1e+74,"cm^3/(mol*s)"), n=-18, Ea=(37157,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
    reactant1 = 
"""
HOCO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([1,10,20,50,100],"atm"),
        arrhenius = [
            Arrhenius(A=(3.5e+56,"s^-1"), n=-15, Ea=(46500,"cal/mol"), T0=1),
            Arrhenius(A=(3.2e+57,"s^-1"), n=-15, Ea=(46500,"cal/mol"), T0=1),
            Arrhenius(A=(6e+57,"s^-1"), n=-15, Ea=(46500,"cal/mol"), T0=1),
            Arrhenius(A=(1.4e+58,"s^-1"), n=-15, Ea=(46500,"cal/mol"), T0=1),
            Arrhenius(A=(2.8e+58,"s^-1"), n=-15, Ea=(46500,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    reactant1 = 
"""
HOCO
1     C     1 {2,D} {3,S}
2     O     0 {1,D}
3     O     0 {1,S}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([1,10,20,50,100],"atm"),
        arrhenius = [
            Arrhenius(A=(2.5e+69,"s^-1"), n=-18, Ea=(60000,"cal/mol"), T0=1),
            Arrhenius(A=(2.2e+70,"s^-1"), n=-18, Ea=(60000,"cal/mol"), T0=1),
            Arrhenius(A=(4.3e+70,"s^-1"), n=-18, Ea=(60000,"cal/mol"), T0=1),
            Arrhenius(A=(1e+71,"s^-1"), n=-18, Ea=(60000,"cal/mol"), T0=1),
            Arrhenius(A=(2e+71,"s^-1"), n=-18, Ea=(60000,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1,10,20,50,100],"atm"),
        arrhenius = [
            Arrhenius(A=(9.9e+11,"s^-1"), n=-0.865, Ea=(16755,"cal/mol"), T0=1),
            Arrhenius(A=(7.2e+12,"s^-1"), n=-0.865, Ea=(16755,"cal/mol"), T0=1),
            Arrhenius(A=(1.3e+13,"s^-1"), n=-0.865, Ea=(16755,"cal/mol"), T0=1),
            Arrhenius(A=(2.9e+13,"s^-1"), n=-0.865, Ea=(16755,"cal/mol"), T0=1),
            Arrhenius(A=(5.3e+13,"s^-1"), n=-0.865, Ea=(16755,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([1,10,20,50,100],"atm"),
        arrhenius = [
            Arrhenius(A=(5e+22,"cm^3/(mol*s)"), n=-3.85, Ea=(2000,"cal/mol"), T0=1),
            Arrhenius(A=(3.4e+21,"cm^3/(mol*s)"), n=-3.2, Ea=(2300,"cal/mol"), T0=1),
            Arrhenius(A=(4.1e+20,"cm^3/(mol*s)"), n=-2.94, Ea=(1900,"cal/mol"), T0=1),
            Arrhenius(A=(2.8e+18,"cm^3/(mol*s)"), n=-2.2, Ea=(1400,"cal/mol"), T0=1),
            Arrhenius(A=(1.1e+19,"cm^3/(mol*s)"), n=-2.3, Ea=(1800,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OO
1     O     0 {2,S} {3,S}
2     O     1 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = PDepArrhenius(
        pressures = ([1,10,20,50,100],"atm"),
        arrhenius = [
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(0,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=1),
            Arrhenius(A=(3.3e+29,"cm^3/(mol*s)"), n=-5.6, Ea=(6850,"cal/mol"), T0=1),
            Arrhenius(A=(5.6e+28,"cm^3/(mol*s)"), n=-5.25, Ea=(6850,"cal/mol"), T0=1),
            Arrhenius(A=(4.1e+30,"cm^3/(mol*s)"), n=-5.7, Ea=(8750,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    reactant1 = 
"""
CH3OOH
1     O     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product1 = 
"""
CH3O
1     O     1 {2,S}
2     C     0 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([1,10,50,1000],"atm"),
        arrhenius = [
            Arrhenius(A=(2e+35,"s^-1"), n=-6.7, Ea=(47450,"cal/mol"), T0=1),
            Arrhenius(A=(1.1e+28,"s^-1"), n=-4.15, Ea=(46190,"cal/mol"), T0=1),
            Arrhenius(A=(2.8e+26,"s^-1"), n=-3.5, Ea=(46340,"cal/mol"), T0=1),
            Arrhenius(A=(2.2e+17,"s^-1"), n=-0.42, Ea=(44622,"cal/mol"), T0=1),
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

