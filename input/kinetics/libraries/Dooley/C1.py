#!/usr/bin/env python
# encoding: utf-8

name = "Dooley/C1"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3547000000000000.0, 'cm^3/(mol*s)'),
        n = -0.406,
        Ea = (16599, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 2,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    reactant2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50800, 'cm^3/(mol*s)'),
        n = 2.67,
        Ea = (6290, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 3,
    reactant1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (216000000.0, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 4,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    reactant2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2970000.0, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (13400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 5,
    reactant1 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (823, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 6,
    reactant1 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70790000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (295, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 7,
    reactant1 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 8,
    reactant1 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 9,
    reactant1 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
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
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 11,
    reactant1 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 12,
    reactant1 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (48200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 13,
    reactant1 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9550000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 14,
    reactant1 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 16,
    reactant1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2530000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 17,
    reactant1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (23000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 18,
    reactant1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (222900, 'cm^3/(mol*s)'),
        n = 1.89,
        Ea = (-1158.7, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 19,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7580000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (410, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 20,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (72300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 21,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 22,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 23,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 24,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product3 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 25,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (26500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 26,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product3 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 27,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 28,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
O2CHO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 O U1 L2 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 29,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2CHO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HO2CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {4,D} {5,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {6,S}
4 O U0 L2 E0  {1,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1990000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11660, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 30,
    reactant1 = 
"""
HO2CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {4,D} {5,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {6,S}
4 O U0 L2 E0  {1,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
OCHO
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501000000000000.0, 's^-1'),
        n = 0,
        Ea = (40150, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 31,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (57400000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2748.6, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 32,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3080, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 33,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3430000000.0, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (-447, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 34,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1230000.0, 'cm^3/(mol*s)'),
        n = 3,
        Ea = (52000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 35,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (41100, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10210, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 36,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.636e-06, 'cm^3/(mol*s)'),
        n = 5.42,
        Ea = (998, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 37,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
OCH2O2H
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 O U1 L2 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 38,
    reactant1 = 
"""
OCH2O2H
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 O U1 L2 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
HOCH2O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {7,S}
3 O U0 L2 E0  {1,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {3,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 's^-1'),
        n = 0,
        Ea = (8600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 39,
    reactant1 = 
"""
HOCH2O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {7,S}
3 O U0 L2 E0  {1,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {3,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HOCH2O2H
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,S} {7,S}
4 O U0 L2 E0  {2,S} {8,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {4,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (35000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-3275, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 40,
    reactant1 = 
"""
HOCH2O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 O U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HOCH2O2H
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,S} {7,S}
4 O U0 L2 E0  {2,S} {8,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 41,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (84300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 42,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.99e+18, 'cm^3/(mol*s)'),
        n = -1.57,
        Ea = (29230, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 43,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.351, 'cm^3/(mol*s)'),
        n = 3.524,
        Ea = (7380, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 44,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24100000000.0, 'cm^3/(mol*s)'),
        n = 0.76,
        Ea = (-2325, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 45,
    reactant1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54700000.0, 'cm^3/(mol*s)'),
        n = 1.97,
        Ea = (11210, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 46,
    reactant1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3150000000000.0, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (10290, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 47,
    reactant1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5720000.0, 'cm^3/(mol*s)'),
        n = 1.96,
        Ea = (2639, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 48,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3160000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 49,
    reactant1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (181000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18580, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 50,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14.4, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (6935, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 51,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 52,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 53,
    reactant1 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3O2H
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1990000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11660, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 54,
    reactant1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH3O2H
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (181000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (18480, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 55,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH3O2H
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1810000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (13710, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 56,
    reactant1 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5080000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1411, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 57,
    reactant1 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3O2H
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (247000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1570, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 58,
    reactant1 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product3 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (311000000000000.0, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (-1051, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 59,
    reactant1 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    product1 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product3 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 60,
    reactant1 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 61,
    reactant1 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (36000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 62,
    reactant1 = 
"""
CH3O2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 63,
    reactant1 = 
"""
CH3O2H
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (631000000000000.0, 's^-1'),
        n = 0,
        Ea = (42300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 64,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 65,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96350000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 66,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (42000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 67,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 68,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 70,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 71,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 72,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 73,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 74,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 75,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HOCH2O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 O U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 76,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 77,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 78,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 79,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 81,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 82,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 83,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 84,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 85,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6095, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 86,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6095, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 87,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (388000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (3080, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 88,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000.0, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (496.7, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 89,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7100000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (-596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 90,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (44900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 91,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9635, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (13110, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 92,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (39800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 93,
    reactant1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31.9, 'cm^3/(mol*s)'),
        n = 3.17,
        Ea = (7172, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 94,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4060, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 95,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
C2H5
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4990000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 96,
    reactant1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2460000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (8270, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 97,
    reactant1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-570, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 98,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (56000000.0, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (5420, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 99,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 100,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H4
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 101,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H4
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-570, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 102,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 103,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (80000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 104,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 105,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (500000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (7230, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 106,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 107,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 108,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 109,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 110,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 111,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 112,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 113,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (15000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 114,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 115,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 116,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product3 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (28000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 117,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 118,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 119,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 120,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 122,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11300000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 123,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 124,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
C_(V)
multiplicity 5
1 C U4 L0 E0 
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 125,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (57000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 126,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 127,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17130000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-755, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 128,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (685, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 129,
    reactant1 = 
"""
HOCH2O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 O U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 's^-1'),
        n = 0,
        Ea = (14900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 130,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HOCH2O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 O U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4500000000000000.0, 'cm^3/(mol*s)'),
        n = -1.11,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 131,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.593e+18, 's^-1'),
        n = -0.46,
        Ea = (108300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 132,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product3 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2620000.0, 'cm^3/(mol*s)'),
        n = 2.06,
        Ea = (916, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 133,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product3 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18500000.0, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (-962, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 134,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product3 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4240000.0, 'cm^3/(mol*s)'),
        n = 2.1,
        Ea = (4868, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 135,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product3 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60300000000000.0, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (2988, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 136,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product3 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.9e-07, 'cm^3/(mol*s)'),
        n = 5.8,
        Ea = (2200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 137,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product3 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11920, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 138,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product3 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.77e+18, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (2975, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 139,
    reactant1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4.577e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104380, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.0, '[C]=O': 1.9, '[Ar]': 0.0},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 140,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (6165000000000000.0, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.0, '[C]=O': 1.9, '[Ar]': 0.0},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 141,
    reactant1 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.714e+18, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.75, '[C]=O': 1.9, '[Ar]': 0.75},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 142,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.8e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.38, '[C]=O': 1.9, '[Ar]': 0.38},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 143,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        efficiencies = {'[H][H]': 2.0, '[C]=O': 1.9, '[O][O]': 0.78, 'O=C=O': 3.8, 'O': 11.0},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 144,
    reactant1 = 
"""
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.64, '[C]=O': 1.9, '[Ar]': 0.64},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 145,
    reactant1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
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
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12.0, '[Ar]': 0.87},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 146,
    reactant1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (474850000000.0, 'cm^3/(mol*s)'),
            n = 0.659,
            Ea = (14874, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 6.0},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 147,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (3.3e+39, 'cm^3/(mol*s)'),
            n = -6.3,
            Ea = (99900, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12.0, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 148,
    reactant1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(3.1e+45, 'cm^3/(mol*s)'), n=-8, Ea=(97510, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12.0, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 149,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H6
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
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
        efficiencies = {'[C]=O': 2.0, 'O=C=O': 3.0, 'O': 5.0},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 150,
    reactant1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 151,
    reactant1 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 152,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 153,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 154,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 155,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 156,
    reactant1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product1 = 
"""
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,D}
3 O U0 L2 E0  {2,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 157,
    reactant1 = 
"""
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (9000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (600, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[C]=O': 0.0, 'O=C=O': 0.0, 'O': 0.0, '[Ar]': 0.0},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 158,
    reactant1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
OCHO
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 O U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
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
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 159,
    reactant1 = 
"""
CH2OH
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
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
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 160,
    reactant1 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
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
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 161,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 162,
    reactant1 = 
"""
HCOOH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 O U0 L2 E0  {1,S} {5,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.5e+16, 'cm^3/(mol*s)'), n=0, Ea=(57000, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = 'Reaction and kinetics from Dooley\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

