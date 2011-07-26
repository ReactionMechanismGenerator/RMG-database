#!/usr/bin/env python
# encoding: utf-8

name = "combustion_core/version4"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
O
1     O     2T
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
        A = (2.17e+06,"cm^3/(mol*s)","*|/",1.2),
        n = 2.1,
        Ea = (6.57,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
small molecule oxidation library, reaction file, version 2, JS, August 6, 2003
originally from Leeds methane oxidation mechanism v1.5
http://www.chem.leeds.ac.uk/Combustion/Combustion.html
fix bug for O2 + HCO = HO2 + CO 1.52E13 0.00 -7.09, change E into positive, change A into 5.12E13 according to NIST



part with CO
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.06e+06,"cm^3/(mol*s)","*|/",1.2),
        n = 2.1,
        Ea = (6.57,"kJ/mol"),
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
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C3H2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {3,S}
3     C     2S {1,S} {2,S}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.89e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (5.64,"kJ/mol"),
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
        A = (1.26e+13,"cm^3/(mol*s)","*|/",1.7),
        n = 0,
        Ea = (196.9,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH
1     C     3
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
        A = (1.66e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH
1     C     3
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
        A = (1.66e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2
1     C     2T
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
        A = (5.43e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (6.24,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2
1     C     2T
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
        A = (5.43e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (6.24,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2
1     C     2T
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
        A = (8.15e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (6.24,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2
1     C     2T
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
        A = (1.48e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (6.24,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2
1     C     2T
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
        A = (4.2e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (6.24,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
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
        A = (3.13e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.12e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (7.09,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+12,"cm^3/(mol*s)","*|/",1.7),
        n = 0,
        Ea = (3.58,"kJ/mol"),
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
    kinetics = Arrhenius(
        A = (1.66e+07,"cm^3/(mol*s)","*|/",1.5),
        n = 1.3,
        Ea = (-3.2,"kJ/mol"),
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
        A = (1.51e+14,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (99.02,"kJ/mol"),
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.77e+11,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-7.15,"kJ/mol"),
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
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
CH
1     C     3
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
        A = (3.43e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (2.87,"kJ/mol"),
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
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    reactant2 = 
"""
CH2
1     C     2T
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
        A = (2.35e+10,"cm^3/(mol*s)","*|/",1.2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (14.13,"kJ/mol"),
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
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
O
1     O     2T
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
        A = (1.33e+12,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (5.65,"kJ/mol"),
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
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.58e+11,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (5.65,"kJ/mol"),
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
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
        A = (2.52e+11,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (5.65,"kJ/mol"),
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
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+11,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (5.65,"kJ/mol"),
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
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
CO2
1     C     0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.52e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH2CO
1     C     0 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.68e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (9.03e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (0,"kJ/mol"),
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
H
1     H     1
""",
    reactant2 = 
"""
HCCO
1     C     1 {2,D}
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+14,"cm^3/(mol*s)","*|/",1.4),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH
1     C     3
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.97e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (1.2e+14,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (0,"kJ/mol"),
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
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    reactant2 = 
"""
O
1     O     2T
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
        A = (1e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
C2H
1     C     0 {2,T}
2     C     1 {1,T}
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13,"cm^3/(mol*s)","*|/",1.7),
        n = 0,
        Ea = (0,"kJ/mol"),
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
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
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
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
H2CCCH
1     C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
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
        A = (1.39e+14,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (3.01e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (0,"kJ/mol"),
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
O
1     O     2T
""",
    reactant2 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
        A = (9.64e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (1.02e+14,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (0,"kJ/mol"),
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
OH
1     O     1
""",
    reactant2 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
OH
1     O     1
""",
    reactant2 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
        A = (1e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (3.01e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (0,"kJ/mol"),
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
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    reactant2 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
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
        A = (1e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH
1     C     3
""",
    reactant2 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (7.2e+13,"cm^3/(mol*s)","*|/",1.7),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (4.8e+13,"cm^3/(mol*s)","*|/",1.7),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH2
1     C     2T
""",
    reactant2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
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
        A = (1.81e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH2
1     C     2T
""",
    reactant2 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
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
        A = (3e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
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
CH
1     C     3
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
part with CO2
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 48,
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
        A = (3.01e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH4
1     C     0
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-1.66,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
part with CH
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 50,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    product2 = 
"""
CH2
1     C     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.11e+14,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-0.51,"kJ/mol"),
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
C3H4
1     C     0 {3,D}
2     C     0 {3,D}
3     C     0 {1,D} {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+14,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-1.44,"kJ/mol"),
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
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08e+14,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-1.1,"kJ/mol"),
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
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    reactant2 = 
"""
CH
1     C     3
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (-2.16,"kJ/mol"),
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
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.02e+12,"cm^3/(mol*s)","*|/",1.7),
        n = 0,
        Ea = (-7.48,"kJ/mol"),
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
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH
1     C     3
""",
    reactant2 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product1 = 
"""
CH2
1     C     2T
""",
    product2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH
1     C     3
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
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (3.33,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
part with CH2 and CH2(S)
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
CH2
1     C     2T
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
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
        A = (1.08e+14,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (3.33,"kJ/mol"),
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.22e+13,"cm^3/(mol*s)","*|/",1.4),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH2
1     C     2T
""",
    reactant2 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.81e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (1.81e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
CH2
1     C     2T
""",
    reactant2 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product1 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    product2 = 
"""
CH2O
1     C     0 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (8.37,"kJ/mol"),
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
        A = (4.3e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (42,"kJ/mol"),
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
    index = 66,
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
        A = (7e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
    index = 67,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
CH2
1     C     2T
""",
    product1 = 
"""
C3H4
1     C     0 {3,D}
2     C     0 {3,D}
3     C     0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (27.69,"kJ/mol"),
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
    index = 68,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
""",
    product1 = 
"""
H2CCCH
1     C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+14,"cm^3/(mol*s)","*|/",1.7),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (2e+14,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
H2
1     H     0 {2,S}
2     H     0 {1,S}
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
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.23e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (0,"kJ/mol"),
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
CH2(S)
1     C     2S
""",
    product1 = 
"""
C3H6
1     C     0 {2,S}
2     C     0 {1,S} {3,D}
3     C     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.64e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
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
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+14,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (7.23e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (11.64,"kJ/mol"),
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
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product1 = 
"""
H2CCCCH
1     C     0 {2,D}
2     C     1 {1,D} {3,S}
3     C     0 {2,S} {4,T}
4     C     0 {3,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+09,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (242,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
others
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 75,
    reactant1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    product1 = 
"""
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
H
1     H     1
""",
    product2 = 
"""
CH2HCO
1     C     1 {2,S}
2     C     0 {1,S} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.74e+06,"cm^3/(mol*s)","*|/",1.3),
        n = 1.88,
        Ea = (0.75,"kJ/mol"),
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
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
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.13e+06,"cm^3/(mol*s)","*|/",1.3),
        n = 1.88,
        Ea = (0.75,"kJ/mol"),
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
O
1     O     2T
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
        A = (680000,"cm^3/(mol*s)","*|/",1.3),
        n = 1.88,
        Ea = (0.75,"kJ/mol"),
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
C4H2
1     C     0 {2,S} {3,T}
2     C     0 {1,S} {4,T}
3     C     0 {1,T}
4     C     0 {2,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C3H2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {3,S}
3     C     2S {1,S} {2,S}
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.68e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (-1.71,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
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
        A = (6.89e+15,"cm^6/(mol^2*s)","*|/",1.5),
        n = 0,
        Ea = (-8.73,"kJ/mol"),
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
O2
1     O     1 {2,S}
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
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.756e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (62.11,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
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
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+11,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (37.42,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    product1 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.05e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
C3H2
1     C     0 {2,D} {3,S}
2     C     0 {1,D} {3,S}
3     C     2S {1,S} {2,S}
""",
    product1 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    product2 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
H2CCCH
1     C     1 {2,S}
2     C     0 {1,S} {3,T}
3     C     0 {2,T}
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
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+10,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (12,"kJ/mol"),
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
        A = (2.41e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (16.59,"kJ/mol"),
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
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+13,"cm^3/(mol*s)","*|/",1.6),
        n = 0,
        Ea = (56.54,"kJ/mol"),
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
        A = (1.69e+14,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (3.66,"kJ/mol"),
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
        A = (3.01e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (7.2,"kJ/mol"),
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
        A = (1.02e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (8.43e+13,"cm^3/(mol*s)","*|/",1.2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.8e+13,"cm^3/(mol*s)","*|/",1.7),
        n = 0,
        Ea = (0,"kJ/mol"),
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
    index = 93,
    reactant1 = 
"""
C2H
1     C     0 {2,T}
2     C     1 {1,T}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
HCCO
1     C     1 {2,D}
2     C     0 {1,D} {3,D}
3     O     0 {2,D}
""",
    product2 = 
"""
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (0,"kJ/mol"),
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
    index = 94,
    reactant1 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
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
CH3
1     C     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.62e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
""",
    product1 = 
"""
CH3O
1     C     0 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
O
1     O     2T
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.4e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (131.37,"kJ/mol"),
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
        A = (1.51e+09,"cm^3/(mol*s)","*|/",1.2),
        n = 1.14,
        Ea = (0.42,"kJ/mol"),
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
H2
1     H     0 {2,S}
2     H     0 {1,S}
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
H
1     H     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (51200,"cm^3/(mol*s)","*|/",1.2),
        n = 2.67,
        Ea = (26.27,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
new adding from version 2 to version 3
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 98,
    reactant1 = 
"""
H2O
1     O     0
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
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.52e+08,"cm^3/(mol*s)","*|/",1.2),
        n = 1.6,
        Ea = (77.08,"kJ/mol"),
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
        A = (7.23e+08,"cm^3/(mol*s)","*|/",1.2),
        n = 1.56,
        Ea = (35.5,"kJ/mol"),
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
        A = (1.57e+07,"cm^3/(mol*s)","*|/",1.15),
        n = 1.83,
        Ea = (11.64,"kJ/mol"),
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
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
OH
1     O     1
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
        A = (6e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (54.04,"kJ/mol"),
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
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
        A = (5.42e+14,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (62.36,"kJ/mol"),
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
OH
1     O     1
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
        A = (2.05e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (24.86,"kJ/mol"),
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
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
H
1     H     1
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
        A = (1.45e+09,"cm^3/(mol*s)","*|/",1.3),
        n = 1.5,
        Ea = (31.01,"kJ/mol"),
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
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
CH3
1     C     1
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
        A = (1.51e-07,"cm^3/(mol*s)","*|/",1.2),
        n = 6,
        Ea = (25.3,"kJ/mol"),
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
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
O
1     O     2T
""",
    product1 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+09,"cm^3/(mol*s)","*|/",1.15),
        n = 1.5,
        Ea = (24.28,"kJ/mol"),
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
C2H6
1     C     0 {2,S}
2     C     0 {1,S}
""",
    reactant2 = 
"""
OH
1     O     1
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
        A = (7.23e+06,"cm^3/(mol*s)","*|/",1.1),
        n = 2,
        Ea = (3.62,"kJ/mol"),
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
C2H6
1     C     0 {2,S}
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
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    product2 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.32e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (85.63,"kJ/mol"),
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
        A = (6.02e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (170.11,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
CH3O
1     C     0 {2,S}
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
        A = (2.17e+10,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (7.32,"kJ/mol"),
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
        A = (1.69e+12,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (15.71,"kJ/mol"),
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
        A = (6.62e+11,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (16.63,"kJ/mol"),
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
    kinetics = Arrhenius(
        A = (7.83e+12,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (5.57,"kJ/mol"),
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
        A = (1.26e+08,"cm^3/(mol*s)","*|/",1.3),
        n = 1.62,
        Ea = (9.06,"kJ/mol"),
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
CH4
1     C     0
""",
    product2 = 
"""
HCO
1     C     1 {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.09e+12,"cm^3/(mol*s)","*|/",1.2),
        n = 0,
        Ea = (36.95,"kJ/mol"),
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
        A = (4.16e+11,"cm^3/(mol*s)","*|/",1.3),
        n = 0.57,
        Ea = (11.56,"kJ/mol"),
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
        A = (3.43e+09,"cm^3/(mol*s)","*|/",1.5),
        n = 1.18,
        Ea = (-1.87,"kJ/mol"),
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
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    product2 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.28e+13,"cm^3/(mol*s)","*|/",1.3),
        n = 0,
        Ea = (5.9,"kJ/mol"),
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
        A = (1.81e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    product2 = 
"""
OH
1     O     1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.19e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (0,"kJ/mol"),
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
        A = (2.89e+13,"cm^3/(mol*s)","*|/",1.5),
        n = 0,
        Ea = (-2.08,"kJ/mol"),
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
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H9_1
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.12e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (81.1,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
n-butane + HO2, JS, 12/10/2003, from NIST
use C4H10 + HO2 in Pitz et al, Combustion and Flame, 63: 113-133(1986)
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 123,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
HO2
1     O     0 {2,S}
2     O     1 {1,S}
""",
    product1 = 
"""
C4H9_2
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4     C     1 {1,S} {3,S}
""",
    product2 = 
"""
H2O2
1     O     0 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.76e+12,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (71.1,"kJ/mol"),
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
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H9_1
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     1 {2,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.31e+07,"cm^3/(mol*s)","*|/",2),
        n = 1.8,
        Ea = (3.99,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
C4H10 + HO2 = C4H9_1 + H2O2	4.76E4	2.55	69.01	*2.0	0	0
C4H10 + HO2 = C4H9_2 + H2O2	9.63E3	2.6	58.20	*2.0	0	0
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 125,
    reactant1 = 
"""
C4H10
1     C     0 {2,S} {3,S}
2     C     0 {1,S} {4,S}
3     C     0 {1,S}
4     C     0 {2,S}
""",
    reactant2 = 
"""
OH
1     O     1
""",
    product1 = 
"""
C4H9_2
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     C     0 {4,S}
4     C     1 {1,S} {3,S}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.36e+06,"cm^3/(mol*s)","*|/",2),
        n = 2,
        Ea = (-2.49,"kJ/mol"),
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
    kinetics = Arrhenius(
        A = (1e+13,"cm^3/(mol*s)","*|/",2),
        n = 0,
        Ea = (4.18,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2O + HO2 = HCO + H2O2	4.11E4	2.5	42.68	*2.0	0	0

JS, from Kojima, S., Combustion and Flame, 99:87-136
C4H9O = CH3CHO + C2H5	2.51E14	0	61.1 	*3.16	0	0

HO2 disprop, from NIST
use H2O2 + O2 in Pitz et al, Combustion and Flame, 63: 113-133(1986)
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 127,
    reactant1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    reactant2 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
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
        A = (4.56e+16,"cm^3/(mol*s)","*|/",3.16),
        n = -1.39,
        Ea = (4.22,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
From NIST
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 128,
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
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(1.54e+15,"cm^3/(mol*s)","*|/",1.2), n=0, Ea=(12.56,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
small molecule oxidation library, third body reaction file, version 2, JS, August 6, 2003
originally from Leeds methane oxidation mechanism v1.5
http://www.chem.leeds.ac.uk/Combustion/Combustion.html
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 129,
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
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(1.4e+36,"s^-1","*|/",1.2), n=-5.54, Ea=(404.58,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
CH2O
1     C     0 {2,D}
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
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(3.26e+36,"s^-1","*|/",1.2), n=-5.54, Ea=(404.58,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
CO
1     C     2T {2,D}
2     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(6.57e+15,"s^-1","*|/",1.2), n=0, Ea=(241.03,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
        arrheniusHigh = Arrhenius(A=(1.51e+13,"s^-1","*|/",1.2), n=0, Ea=(0,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 0.48, "C#C": 3.2, "C(=O)=O": 1.5, "C=C": 1.6, "CC": 1.44, "N#N": 0.4, "O": 6.5, "[Ar]": 0.24, "[C]=O": 0.75, "[O][O]": 0.4},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
HCO   + M                =    H      + CO  + M    4.49E14   0.00    65.93	*1.2	0	0
N2/0.4/ O2/0.4/ CO/0.75/ CO2/1.5/ H2O/6.5/ CH4/3.0/ C2H6/3.0/ AR/0.35/
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
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(2.91e+16,"s^-1","*|/",1.2), n=0, Ea=(379.14,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product1 = 
"""
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    product2 = 
"""
H2
1     H     0 {2,S}
2     H     0 {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(9.97e+16,"s^-1","*|/",1.2), n=0, Ea=(299.32,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
        arrheniusHigh = Arrhenius(A=(5.4e+13,"cm^3/(mol*s)","*|/",1.2), n=0, Ea=(-7.48,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
O2
1     O     1 {2,S}
2     O     1 {1,S}
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
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(2.1e+18,"cm^3/(mol*s)","*|/",1.2), n=-0.8, Ea=(0,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.67, "O": 0, "[Ar]": 0.29, "[C]=O": 0.75, "[O][O]": 0.4},
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
H
1     H     1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(7.4e+17,"s^-1","*|/",1.2), n=0, Ea=(404.09,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
        arrheniusHigh = Arrhenius(A=(1.87e+18,"cm^3/(mol*s)","*|/",1.2), n=-1, Ea=(0,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[H][H]": 0, "[O][O]": 0.4},
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
        arrheniusHigh = Arrhenius(A=(1.18e+19,"cm^3/(mol*s)","*|/",1.2), n=-1, Ea=(0,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
        arrheniusHigh = Arrhenius(A=(5.53e+22,"cm^3/(mol*s)","*|/",1.2), n=-2, Ea=(0,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 2.55, "[Ar]": 0.15, "[C]=O": 0.75, "[O][O]": 0.4},
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
CH3O
1     C     0 {2,S}
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
H
1     H     1
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(1.55e+14,"s^-1","*|/",1.2), n=0, Ea=(56.46,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(1.26e+16,"s^-1","*|/",1.2), n=0, Ea=(125.6,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
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
C2H2
1     C     0 {2,T}
2     C     0 {1,T}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H3
1     C     0 {2,D}
2     C     1 {1,D}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(8.43e+12,"cm^3/(mol*s)","*|/",1.2), n=0, Ea=(10.81,"kJ/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(3.43e+18,"cm^3/(mol*s)"), n=0, Ea=(6.15,"kJ/mol"), T0=1),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
        alpha = 1,
        T3 = (1,"K"),
        T1 = (1,"K"),
        T2 = (1231,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Small molecule oxidation library, pressure-dependent reaction file, PEY, 7-Jul-04
Originally from Leeds methane oxidation mechanism v1.5. Includes all of
the Leeds pressure-dependent reactions.
The order of reactions is the same as the original model.
http://www.chem.leeds.ac.uk/Combustion/Combustion.html
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 144,
    reactant1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    reactant2 = 
"""
H
1     H     1
""",
    product1 = 
"""
C2H5
1     C     0 {2,S}
2     C     1 {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(3.97e+09,"cm^3/(mol*s)","*|/",1.2), n=1.28, Ea=(5.4,"kJ/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.35e+19,"cm^3/(mol*s)"), n=0, Ea=(3.16,"kJ/mol"), T0=1),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
        alpha = 0.76,
        T3 = (40,"K"),
        T1 = (1025,"K"),
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
        arrheniusHigh = Arrhenius(A=(7.23e+13,"cm^3/(mol*s)","*|/",1.2), n=-0.37, Ea=(0,"kJ/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(5.53e+19,"cm^3/(mol*s)"), n=-0.76, Ea=(0,"kJ/mol"), T0=1),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
        alpha = 1,
        T3 = (1,"K"),
        T1 = (1,"K"),
        T2 = (1040,"K"),
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
        arrheniusHigh = Arrhenius(A=(1.688e+14,"cm^3/(mol*s)","*|/",1.2), n=0, Ea=(0,"kJ/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(1.408e+24,"cm^3/(mol*s)"), n=-1.8, Ea=(0,"kJ/mol"), T0=1),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
        alpha = 0.37,
        T3 = (3315,"K"),
        T1 = (61,"K"),
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
        arrheniusHigh = Arrhenius(A=(3.61e+13,"cm^3/(mol*s)","*|/",1.2), n=0, Ea=(0,"kJ/mol"), T0=(1,"K")),
        arrheniusLow = Arrhenius(A=(3.63e+41,"cm^3/(mol*s)"), n=-7, Ea=(11.56,"kJ/mol"), T0=1),
        efficiencies = {"C": 3, "C(=O)=O": 1.5, "CC": 3, "N#N": 0.4, "O": 6.5, "[Ar]": 0.35, "[C]=O": 0.75, "[O][O]": 0.4},
        alpha = 0.62,
        T3 = (73,"K"),
        T1 = (1180,"K"),
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

