#!/usr/bin/env python
# encoding: utf-8

name = "OxygenSingTrip"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
O2S
1     O     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (0.00023,"s^-1"),
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
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
O2S
1     O     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(4.05,"s^-1"), n=0, Ea=(0,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"C(=O)=O": 4.29, "[O][O]": 5.43},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
O2S
1     O     0 {2,D}
2     O     0 {1,D}
""",
    product1 = 
"""
O2
1     O     1 {2,S}
2     O     1 {1,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = ThirdBody(
        arrheniusHigh = Arrhenius(A=(3e+06,"s^-1"), n=0, Ea=(0,"kJ/mol"), T0=(1,"K")),
        efficiencies = {"N#N": 0.028, "O": 1.783, "[Ar]": 0.00166, "[C]=O": 14, "[H][H]": 1, "[O][O]": 0.34, "c1ccccc1": 1.067},
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

