#!/usr/bin/env python
# encoding: utf-8

name = "GRI-HCO"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
HCO
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    reactant2 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H
1 H 1 0
""",
    product2 = 
"""
CO
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    product3 = 
"""
H2O
1 O 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5e+18, 'cm^3/(mol*s)'),
        n = -1,
        Ea = (17000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from GRI-HCO.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    reactant1 = 
"""
HCO
1 C 1 0 {2,D} {3,S}
2 O 0 2 {1,D}
3 H 0 0 {1,S}
""",
    product1 = 
"""
H
1 H 1 0
""",
    product2 = 
"""
CO
1 C 0 1 {2,T}
2 O 0 1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.87e+17, 'cm^3/(mol*s)'),
            n = -1,
            Ea = (17000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 0.0, '[H][H]': 2.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from GRI-HCO.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

