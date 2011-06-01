#!/usr/bin/env python
# encoding: utf-8

name = "GRI-HCO"
shortDesc = ""
longDesc = """

"""

entry(
    index = 1,
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
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
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
        arrheniusHigh = Arrhenius(A=(1.87e+17,"s^-1"), n=-1, Ea=(17000,"cal/mol"), T0=(1,"K")),
        efficiencies = {"C": 2, "C(=O)=O": 2, "CC": 3, "O": 0, "[C]=O": 1.5, "[H][H]": 2},
    ),
    reference = None,
    referenceType = "",
    shortDesc = """""",
    longDesc = 
"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","jwallen","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

