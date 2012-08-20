#!/usr/bin/env python
# encoding: utf-8

name = "GRI-Mech3.0"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
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
H
1     H     1
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (38700,"cm^3/(mol*s)"),
        n = 2.7,
        Ea = (6260,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
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
        A = (2e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
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
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.63e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (4000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
CH
1     C     3
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
    kinetics = Arrhenius(
        A = (5.7e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
CH2
1     C     2T
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.06e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH4
1     C     0
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.02e+09,"cm^3/(mol*s)"),
        n = 1.5,
        Ea = (8600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3540,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (388000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (3100,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130000,"cm^3/(mol*s)"),
        n = 2.5,
        Ea = (5000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    product1 = 
"""
CH
1     C     3
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.35e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6e+19,"cm^3/(mol*s)"),
        n = -1.41,
        Ea = (28950,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH2
1     C     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.94e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25e+07,"cm^3/(mol*s)"),
        n = 1.83,
        Ea = (220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.24e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.98e+07,"cm^3/(mol*s)"),
        n = 1.92,
        Ea = (5690,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
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
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
CH2
1     C     2T
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
        A = (1.75e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1350,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 28,
    reactant1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
O
1     O     2T
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
        A = (2.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (47800,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 29,
    reactant1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (40000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 30,
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
    reactant3 = 
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.08e+19,"cm^6/(mol^2*s)"),
        n = -1.24,
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 31,
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
    reactant3 = 
"""
H2O
1     O     0
""",
    product1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.126e+19,"cm^6/(mol^2*s)"),
        n = -0.76,
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 32,
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
        A = (2.65e+16,"cm^3/(mol*s)"),
        n = -0.6707,
        Ea = (17041,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 33,
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
        A = (9e+16,"cm^6/(mol^2*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 34,
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
        A = (6e+19,"cm^6/(mol^2*s)"),
        n = -1.25,
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 35,
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
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
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
        A = (5.5e+20,"cm^6/(mol^2*s)"),
        n = -2,
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 36,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
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
        A = (3.97e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (671,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 37,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
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
        A = (4.48e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1068,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 38,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
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
        Ea = (635,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 39,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
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
        A = (1.21e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (5200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 40,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
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
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 41,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
C
1     C     4
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+14,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 42,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
""",
    product1 = 
"""
CH
1     C     3
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 43,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH4
1     C     0
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
        A = (6.6e+08,"cm^3/(mol*s)"),
        n = 1.62,
        Ea = (10840,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 44,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.34e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 45,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
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
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.74e+07,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (2742,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 46,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 47,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.65e+11,"cm^3/(mol*s)"),
        n = 0.65,
        Ea = (-284,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2(S)
1     C     2S
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.28e+13,"cm^3/(mol*s)"),
        n = -0.09,
        Ea = (610,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 49,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.15e+07,"cm^3/(mol*s)"),
        n = 1.63,
        Ea = (1924,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 51,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+12,"cm^3/(mol*s)"),
        n = 0.5,
        Ea = (-110,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 52,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH2(S)
1     C     2S
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.62e+14,"cm^3/(mol*s)"),
        n = -0.23,
        Ea = (1070,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 53,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
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
        A = (1.7e+07,"cm^3/(mol*s)"),
        n = 2.1,
        Ea = (4870,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 54,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
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
        A = (4.2e+06,"cm^3/(mol*s)"),
        n = 2.1,
        Ea = (4870,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 55,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 56,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.325e+06,"cm^3/(mol*s)"),
        n = 2.53,
        Ea = (12240,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 57,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 58,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.15e+08,"cm^3/(mol*s)"),
        n = 1.9,
        Ea = (7530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 59,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
CH2(S)
1     C     2S
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 60,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (8000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 61,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3428,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 62,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
HCCOH
1     C     0 {2,T} {3,S}
2     C     0 {1,T}
3     O     0 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 63,
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
        A = (2.16e+08,"cm^3/(mol*s)"),
        n = 1.51,
        Ea = (3430,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 64,
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
        A = (35700,"cm^3/(mol*s)"),
        n = 2.4,
        Ea = (-2110,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 65,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiKinetics(
        kineticsList = [
            Arrhenius(A=(1.45e+13,"cm^3/(mol*s)"), n=0, Ea=(-500,"cal/mol"), T0=(1,"K")),
            Arrhenius(A=(5e+15,"cm^3/(mol*s)"), n=0, Ea=(17330,"cal/mol"), T0=(1,"K"))
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 66,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiKinetics(
        kineticsList = [
            Arrhenius(A=(2e+12,"cm^3/(mol*s)"), n=0, Ea=(427,"cal/mol"), T0=(1,"K")),
            Arrhenius(A=(1.7e+18,"cm^3/(mol*s)"), n=0, Ea=(29410,"cal/mol"), T0=(1,"K"))
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 68,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C
1     C     4
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 69,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 70,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 71,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
CH
1     C     3
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (3000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 72,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 73,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH3
1     C     1
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
        A = (5.6e+07,"cm^3/(mol*s)"),
        n = 1.6,
        Ea = (5420,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 74,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH2(S)
1     C     2S
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.44e+17,"cm^3/(mol*s)"),
        n = -1.34,
        Ea = (1417,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH4
1     C     0
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
        A = (1e+08,"cm^3/(mol*s)"),
        n = 1.6,
        Ea = (3120,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 76,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
H
1     H     1
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
        A = (4.76e+07,"cm^3/(mol*s)"),
        n = 1.228,
        Ea = (70,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 77,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 78,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
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
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.43e+09,"cm^3/(mol*s)"),
        n = 1.18,
        Ea = (-447,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 79,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 80,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 81,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
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
        A = (1.44e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (-840,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 82,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.3e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (1500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 83,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 84,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000218,"cm^3/(mol*s)"),
        n = 4.5,
        Ea = (-1000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 85,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
HCCOH
1     C     0 {2,T} {3,S}
2     C     0 {1,T}
3     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (504000,"cm^3/(mol*s)"),
        n = 2.3,
        Ea = (13500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 86,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+07,"cm^3/(mol*s)"),
        n = 2,
        Ea = (14000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 87,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000483,"cm^3/(mol*s)"),
        n = 4,
        Ea = (-2000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 88,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 89,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.6e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (2500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 90,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.54e+06,"cm^3/(mol*s)"),
        n = 2.12,
        Ea = (870,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 91,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (2000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 92,
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiKinetics(
        kineticsList = [
            Arrhenius(A=(1.3e+11,"cm^3/(mol*s)"), n=0, Ea=(-1630,"cal/mol"), T0=(1,"K")),
            Arrhenius(A=(4.2e+14,"cm^3/(mol*s)"), n=0, Ea=(12000,"cal/mol"), T0=(1,"K"))
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 94,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 95,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+12,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 96,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.78e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 97,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
OH
1     O     1
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
        A = (1.5e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (23600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
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
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.6e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (12000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 99,
    reactant1 = 
"""
C
1     C     4
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (576,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 100,
    reactant1 = 
"""
C
1     C     4
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 101,
    reactant1 = 
"""
C
1     C     4
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 102,
    reactant1 = 
"""
CH
1     C     3
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
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.71e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 103,
    reactant1 = 
"""
CH
1     C     3
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
CH2
1     C     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3110,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 104,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
H2O
1     O     0
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.71e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-755,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 105,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 106,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 107,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
CH4
1     C     0
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 108,
    reactant1 = 
"""
CH
1     C     3
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
HCO
1     C     1 {2,D}
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
        A = (1.9e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (15792,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 109,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.46e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-515,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 110,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 111,
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
OH
1     O     1
""",
    product2 = 
"""
H
1     H     1
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 112,
    reactant1 = 
"""
CH2
1     C     2T
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
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (500000,"cm^3/(mol*s)"),
        n = 2,
        Ea = (7230,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 113,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+15,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11944,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 114,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 115,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
CH4
1     C     0
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
        A = (2.46e+06,"cm^3/(mol*s)"),
        n = 2,
        Ea = (8270,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 116,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 117,
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
H
1     H     1
""",
    product2 = 
"""
OH
1     O     1
""",
    product3 = 
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 118,
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
H2O
1     O     0
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 119,
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 120,
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 121,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-570,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 122,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
CH4
1     C     0
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
        A = (1.6e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-570,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9e+12,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 124,
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
CH2
1     C     2T
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
        A = (7e+12,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 126,
    reactant1 = 
"""
CH2(S)
1     C     2S
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-550,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
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
O
1     O     2T
""",
    product2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.56e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (30480,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
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
OH
1     O     1
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.31e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (20315,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24500,"cm^3/(mol*s)"),
        n = 2.47,
        Ea = (5180,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 130,
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
H
1     H     1
""",
    product2 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.84e+12,"cm^3/(mol*s)"),
        n = 0.1,
        Ea = (10600,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 131,
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
        A = (2.648e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 132,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
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
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3320,"cm^3/(mol*s)"),
        n = 2.81,
        Ea = (5860,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 133,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+07,"cm^3/(mol*s)"),
        n = 1.5,
        Ea = (9940,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 134,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+07,"cm^3/(mol*s)"),
        n = 1.5,
        Ea = (9940,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (227000,"cm^3/(mol*s)"),
        n = 2,
        Ea = (9200,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 136,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    product1 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product2 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.14e+06,"cm^3/(mol*s)"),
        n = 1.74,
        Ea = (10450,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 137,
    reactant1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
H2O
1     O     0
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
    product3 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+18,"cm^3/(mol*s)"),
        n = -1,
        Ea = (17000,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 138,
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
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.345e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (900,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 140,
    reactant1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
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
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e-13,"cm^3/(mol*s)"),
        n = 7.6,
        Ea = (-3530,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 141,
    reactant1 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (-755,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 142,
    reactant1 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
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
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68e+10,"cm^3/(mol*s)"),
        n = 0.9,
        Ea = (1993,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 143,
    reactant1 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
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
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+16,"cm^3/(mol*s)"),
        n = -1.39,
        Ea = (1015,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    reactant1 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+11,"cm^3/(mol*s)"),
        n = 0,
        Ea = (3875,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 145,
    reactant1 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    reactant2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.2e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (854,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 146,
    reactant1 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    reactant2 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 147,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.37e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 148,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+06,"cm^3/(mol*s)"),
        n = 1.83,
        Ea = (220,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 149,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH3CHO
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.096e+14,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 151,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8e+09,"cm^3/(mol*s)"),
        n = 0.5,
        Ea = (-1755,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 152,
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
H
1     H     1
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
        A = (5.8e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 153,
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
O
1     O     2T
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
        Ea = (1500,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 154,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
H
1     H     1
""",
    product3 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+14,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10989,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 155,
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
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.82e+10,"cm^3/(mol*s)"),
        n = 0.25,
        Ea = (-935,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 156,
    reactant1 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
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
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.03e+11,"cm^3/(mol*s)"),
        n = 0.29,
        Ea = (11,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 157,
    reactant1 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
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
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.337e+06,"cm^3/(mol*s)"),
        n = 1.61,
        Ea = (-384,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 158,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1808,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 159,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CH3
1     C     1
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.92e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (1808,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 160,
    reactant1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
CH3
1     C     1
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)"),
        n = 0,
        Ea = (39150,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 161,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09,"cm^3/(mol*s)"),
        n = 1.16,
        Ea = (2405,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 162,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
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
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.05e+09,"cm^3/(mol*s)"),
        n = 1.16,
        Ea = (2405,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 163,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
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
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.343e+10,"cm^3/(mol*s)"),
        n = 0.73,
        Ea = (-1113,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 164,
    reactant1 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
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
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+12,"cm^3/(mol*s)"),
        n = 0,
        Ea = (11923,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 165,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
CH3CHO
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH4
1     C     0
""",
    product3 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.72e+06,"cm^3/(mol*s)"),
        n = 1.77,
        Ea = (5920,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 166,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2
1     C     2T
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
        A = (1.5e+14,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 167,
    reactant1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+10,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 168,
    reactant1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
OH
1     O     1
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product3 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.35e+10,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 169,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.2e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 170,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 171,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 172,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)"),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 173,
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
        arrheniusLow = Arrhenius(A=(1.2e+17,"cm^3/(mol*s)"), n=-1, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"C": 2, "C(=O)=O": 3.6, "CC": 3, "O": 15.4, "[Ar]": 0.83, "[C]=O": 1.75, "[H][H]": 2.4},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 174,
    reactant1 = 
"""
O
1     O     2T
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
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(5e+17,"cm^3/(mol*s)"), n=-1, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 175,
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
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.8e+18,"cm^3/(mol*s)"), n=-0.86, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"C(=O)=O": 1.5, "CC": 1.5, "N#N": 0, "O": 0, "[Ar]": 0, "[C]=O": 0.75, "[O][O]": 0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 176,
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
        arrheniusLow = Arrhenius(A=(1e+18,"cm^3/(mol*s)"), n=-1, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"C": 2, "C(=O)=O": 0, "CC": 3, "O": 0, "[Ar]": 0.63, "[H][H]": 0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 177,
    reactant1 = 
"""
H
1     H     1
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
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(2.2e+22,"cm^3/(mol*s)"), n=-2, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"C": 2, "CC": 3, "O": 3.65, "[Ar]": 0.38, "[H][H]": 0.73},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 178,
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
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.87e+17,"s^-1"), n=-1, Ea=(17000,"cal/mol"), T0=(1,"K")),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 0, "[C]=O": 1.5, "[H][H]": 2},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 179,
    reactant1 = 
"""
O
1     O     2T
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.8e+10,"cm^3/(mol*s)"), n=0, Ea=(2385,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(6.02e+14,"cm^3/(mol*s)"), n=0, Ea=(3000,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 3.5, "CC": 3, "O": 6, "[Ar]": 0.5, "[C]=O": 1.5, "[H][H]": 2, "[O][O]": 6},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 180,
    reactant1 = 
"""
H
1     H     1
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6e+14,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.04e+26,"cm^3/(mol*s)"), n=-2.76, Ea=(1600,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.562,
        T3 = (91,"K"),
        T1 = (5836,"K"),
        T2 = (8552,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 181,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH4
1     C     0
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.39e+16,"cm^3/(mol*s)"), n=-0.534, Ea=(536,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(2.62e+33,"cm^3/(mol*s)"), n=-4.76, Ea=(2440,"cal/mol"), T0=1),
        efficiencies = {"C": 3, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.783,
        T3 = (74,"K"),
        T1 = (2941,"K"),
        T2 = (6964,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 182,
    reactant1 = 
"""
H
1     H     1
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.09e+12,"cm^3/(mol*s)"), n=0.48, Ea=(-260,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(2.47e+24,"cm^3/(mol*s)"), n=-2.57, Ea=(425,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.7824,
        T3 = (271,"K"),
        T1 = (2755,"K"),
        T2 = (6570,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 183,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.4e+11,"cm^3/(mol*s)"), n=0.454, Ea=(3600,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.27e+32,"cm^3/(mol*s)"), n=-4.82, Ea=(6530,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.7187,
        T3 = (103,"K"),
        T1 = (1291,"K"),
        T2 = (4160,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 184,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.4e+11,"cm^3/(mol*s)"), n=0.454, Ea=(2600,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(2.2e+30,"cm^3/(mol*s)"), n=-4.8, Ea=(5560,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.758,
        T3 = (94,"K"),
        T1 = (1555,"K"),
        T2 = (4200,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 185,
    reactant1 = 
"""
H
1     H     1
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.055e+12,"cm^3/(mol*s)"), n=0.5, Ea=(86,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(4.36e+31,"cm^3/(mol*s)"), n=-4.65, Ea=(5080,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.6,
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 186,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.43e+12,"cm^3/(mol*s)"), n=0.515, Ea=(50,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(4.66e+41,"cm^3/(mol*s)"), n=-7.44, Ea=(14080,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 187,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1e+17,"cm^3/(mol*s)"), n=-1, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(3.75e+33,"cm^3/(mol*s)"), n=-4.8, Ea=(1900,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.6464,
        T3 = (132,"K"),
        T1 = (1315,"K"),
        T2 = (5566,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 188,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.6e+12,"cm^3/(mol*s)"), n=0, Ea=(2400,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(3.8e+40,"cm^3/(mol*s)"), n=-7.27, Ea=(7220,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.7507,
        T3 = (98.5,"K"),
        T1 = (1302,"K"),
        T2 = (4167,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 189,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.08e+12,"cm^3/(mol*s)"), n=0.27, Ea=(280,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.4e+30,"cm^3/(mol*s)"), n=-3.86, Ea=(3320,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.782,
        T3 = (207.5,"K"),
        T1 = (2663,"K"),
        T2 = (6095,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 190,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.4e+11,"cm^3/(mol*s)"), n=0.454, Ea=(1820,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(6e+41,"cm^3/(mol*s)"), n=-7.62, Ea=(6970,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.9753,
        T3 = (210,"K"),
        T1 = (984,"K"),
        T2 = (4374,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 191,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product1 = 
"""
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.21e+17,"cm^3/(mol*s)"), n=-0.99, Ea=(1580,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.99e+41,"cm^3/(mol*s)"), n=-7.08, Ea=(6685,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.8422,
        T3 = (125,"K"),
        T1 = (2219,"K"),
        T2 = (6882,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 192,
    reactant1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.3e+07,"cm^3/(mol*s)"), n=1.5, Ea=(79600,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(5.07e+27,"cm^3/(mol*s)"), n=-3.42, Ea=(84350,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.932,
        T3 = (197,"K"),
        T1 = (1540,"K"),
        T2 = (10300,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 193,
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
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(7.4e+13,"cm^3/(mol*s)"), n=-0.37, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(2.3e+18,"cm^3/(mol*s)"), n=-0.9, Ea=(-1700,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.7346,
        T3 = (94,"K"),
        T1 = (1756,"K"),
        T2 = (5182,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 194,
    reactant1 = 
"""
OH
1     O     1
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.79e+18,"cm^3/(mol*s)"), n=-1.43, Ea=(1330,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(4e+36,"cm^3/(mol*s)"), n=-5.92, Ea=(3140,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.412,
        T3 = (195,"K"),
        T1 = (5900,"K"),
        T2 = (6394,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 195,
    reactant1 = 
"""
CH
1     C     3
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
HCCO
1     C     0 {2,T}
2     C     0 {1,T} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5e+13,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(2.69e+28,"cm^3/(mol*s)"), n=-3.74, Ea=(1936,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.5757,
        T3 = (237,"K"),
        T1 = (1652,"K"),
        T2 = (5069,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 196,
    reactant1 = 
"""
CH2
1     C     2T
""",
    reactant2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.1e+11,"cm^3/(mol*s)"), n=0.5, Ea=(4510,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(2.69e+33,"cm^3/(mol*s)"), n=-5.11, Ea=(7095,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.5907,
        T3 = (275,"K"),
        T1 = (1226,"K"),
        T2 = (5185,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 197,
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
CH3OH
1     C     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.82e+17,"cm^3/(mol*s)"), n=-1.16, Ea=(1145,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.88e+38,"cm^3/(mol*s)"), n=-6.36, Ea=(5040,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.6027,
        T3 = (208,"K"),
        T1 = (3922,"K"),
        T2 = (10180,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 198,
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
        arrheniusHigh = Arrhenius(A=(6.77e+16,"cm^3/(mol*s)"), n=-1.18, Ea=(654,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(3.4e+41,"cm^3/(mol*s)"), n=-7.03, Ea=(2762,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.619,
        T3 = (73.2,"K"),
        T1 = (1180,"K"),
        T2 = (9999,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 199,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8e+12,"s^-1"), n=0.44, Ea=(86770,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.58e+51,"s^-1"), n=-9.3, Ea=(97800,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.7345,
        T3 = (180,"K"),
        T1 = (1035,"K"),
        T2 = (5417,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 200,
    reactant1 = 
"""
CH
1     C     3
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.97e+12,"cm^3/(mol*s)"), n=0.43, Ea=(-370,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(4.82e+25,"cm^3/(mol*s)"), n=-2.8, Ea=(590,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.578,
        T3 = (122,"K"),
        T1 = (2535,"K"),
        T2 = (9365,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 201,
    reactant1 = 
"""
H
1     H     1
""",
    reactant2 = 
"""
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
CH2CHO
1     C     0 {2,D}
2     C     0 {1,D} {3,S}
3     O     1 {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.865e+11,"cm^3/(mol*s)"), n=0.422, Ea=(-1755,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.012e+42,"cm^3/(mol*s)"), n=-7.63, Ea=(3854,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.465,
        T3 = (201,"K"),
        T1 = (1773,"K"),
        T2 = (5333,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 202,
    reactant1 = 
"""
CH3
1     C     1
""",
    reactant2 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product1 = 
"""
C3H8
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     C     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(9.43e+12,"cm^3/(mol*s)"), n=0, Ea=(0,"cal/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(2.71e+74,"cm^3/(mol*s)"), n=-16.82, Ea=(13065,"cal/mol"), T0=1),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 6, "[Ar]": 0.7, "[C]=O": 1.5, "[H][H]": 2},
        alpha = 0.1527,
        T3 = (291,"K"),
        T1 = (2742,"K"),
        T2 = (7748,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

