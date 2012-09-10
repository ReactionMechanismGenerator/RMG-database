#!/usr/bin/env python
# encoding: utf-8

name = "Glarborg/C0"
shortDesc = u""
longDesc = u"""

"""
recommended = False

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
CFG
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(3.8e+12,"cm^3/(mol*s)"), n=0, Ea=(7948,"cal/mol"), T0=(1,"K")),
            Arrhenius(A=(8.8e+14,"cm^3/(mol*s)"), n=0, Ea=(19175,"cal/mol"), T0=(1,"K"))
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.9e+11,"cm^3/(mol*s)"), n=0, Ea=(-1408,"cal/mol"), T0=(1,"K")),
            Arrhenius(A=(1e+14,"cm^3/(mol*s)"), n=0, Ea=(11034,"cal/mol"), T0=(1,"K"))
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
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
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.9e+12,"cm^3/(mol*s)"), n=0, Ea=(427,"cal/mol"), T0=(1,"K")),
            Arrhenius(A=(1.6e+18,"cm^3/(mol*s)"), n=0, Ea=(29410,"cal/mol"), T0=(1,"K"))
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
    index = 20,
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
        arrheniusLow = Arrhenius(A=(3.5e+16,"cm^6/(mol^2*s)"), n=-0.41, Ea=(-1116,"cal/mol"), T0=1),
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
CFG from Glarborg; extra collision efficiencies taken from Leeds
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
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
        arrheniusLow = Arrhenius(A=(2.291e+16,"cm^3/(mol*s)"), n=0, Ea=(43638,"cal/mol"), T0=1),
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
H + O2 (+AR) = HO2 (+AR)                   1.5E12   0.600       0  0.0 0.0 0.0
LOW  / 9.04E19 -1.500 490 /
TROE / 0.5 1.0E-30 1.0E30 /

H + O2 (+N2) = HO2 (+N2)                   1.5E12   0.600       0  0.0 0.0 0.0
LOW  / 6.37E20 -1.720 520 /
TROE / 0.8 1.0E-30 1.0E30 /
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
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
        arrheniusLow = Arrhenius(A=(7e+17,"cm^6/(mol^2*s)"), n=-1, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"N#N": 0, "O": 0, "[H][H]": 0},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
reduced by cfg
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
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
        arrheniusLow = Arrhenius(A=(6.2e+16,"cm^6/(mol^2*s)"), n=-0.6, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"O": 5},
    ),
    reference = None,
    referenceType = "",
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
        arrheniusLow = Arrhenius(A=(1.9e+13,"cm^6/(mol^2*s)"), n=0, Ea=(-1788,"cal/mol"), T0=(1,"K")),
        efficiencies = {"N#N": 1.5, "O": 10, "[O][O]": 1.5},
    ),
    reference = None,
    referenceType = "",
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
        arrheniusLow = Arrhenius(A=(4.5e+22,"cm^6/(mol^2*s)"), n=-2, Ea=(0,"cal/mol"), T0=(1,"K")),
        efficiencies = {"O": 12, "[Ar]": 0.38, "[H][H]": 0.73},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

