#!/usr/bin/env python
# encoding: utf-8

name = ""
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
        A = (105040000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15310, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3193500000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (7950, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (960750000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (19180, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (206710000.0, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (3437, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
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
O_(T)
multiplicity 3
1 O U2 L2 E0 
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
        A = (31959, 'cm^3/(mol*s)'),
        n = 2.42,
        Ea = (-1928, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.1713e+25, 'cm^3/(mol*s)'),
        n = -2.44,
        Ea = (120200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (3507000.0, 'cm^3/(mol*s)'),
        n = 2.087,
        Ea = (-1455, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (62516000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
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
        A = (1450000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 10,
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
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
        A = (13382000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-445, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (6776000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1093, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (475200000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (10930, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
                A = (193220000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-1409, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (87241000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (11040, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 15,
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
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
        A = (29065000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (34318000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (9630000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (1740000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (318, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (90701000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (7270, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
O_(T)
multiplicity 3
1 O U2 L2 E0 
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
        A = (2588200000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (47700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H
multiplicity 2
1 H U1 L0 E0 
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(65424, 'cm^3/(mol*s)'), n=2.053, Ea=(-356, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(
                A = (5356800000000.0, 'cm^3/(mol*s)'),
                n = -0.664,
                Ea = (332, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (157000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17944, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (90300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
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
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (116530000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
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
        A = (79396000000.0, 'cm^3/(mol*s)'),
        n = 0.521,
        Ea = (-521, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C_(T)
multiplicity 3
1 C U4 L0 E0 
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
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C_(T)
multiplicity 3
1 C U4 L0 E0 
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (636, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C_(T)
multiplicity 3
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
        A = (108680000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
    kinetics = Arrhenius(
        A = (57000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H
multiplicity 2
1 H U1 L0 E0 
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
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (169400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3320, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (3430000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-884, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
O_(T)
multiplicity 3
1 O U2 L2 E0 
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
        A = (184000000.0, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (1200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (278390000.0, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (1200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (184000000.0, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (1200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product3 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (283650000.0, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (1200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (63800000.0, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (-715, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
    product3 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (81440000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (31574000000000.0, 'cm^3/(mol*s)'),
        n = 0.12,
        Ea = (-162, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (863000, 'cm^3/(mol*s)'),
        n = 2.02,
        Ea = (6776, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (583000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (7230, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product3 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3155100000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
    product3 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (3254700000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
O_(T)
multiplicity 3
1 O U2 L2 E0 
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
    reversible = False,
    kinetics = Arrhenius(
        A = (1517500000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
C_(T)
multiplicity 3
1 C U4 L0 E0 
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
    product3 = 
"""
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (200000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10989, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2CC_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U2 L0 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11944, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
    product3 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (68952000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
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
        A = (31300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (15100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-431, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (68200000000.0, 'cm^3/(mol*s)'),
        n = 0.25,
        Ea = (-935, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2_(S)
multiplicity 1
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
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
        A = (129000000000000.0, 'cm^3/(mol*s)'),
        n = -0.138,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (13300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
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
        A = (6620000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (61935000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (2742, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (413920000000.0, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (2762, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (76558000.0, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1055, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        A = (404550, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (36460, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (82118, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10210, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 69,
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
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-517, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
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
        A = (0.074, 'cm^3/(mol*s)'),
        n = 4.21,
        Ea = (1120, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
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
        A = (13300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-550, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5400, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5862, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5400, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5862, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (56703000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
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
    reversible = False,
    kinetics = Arrhenius(
        A = (23654000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (44402, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (3998, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (5.2872e+17, 'cm^3/(mol*s)'),
        n = -1.34,
        Ea = (1417, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (8272000000.0, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-1755, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
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
        A = (26496000.0, 'cm^3/(mol*s)'),
        n = 1.49,
        Ea = (-1673, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 80,
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (11482000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-590, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
O_(T)
multiplicity 3
1 O U2 L2 E0 
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
        A = (9822600000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28297, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (112.44, 'cm^3/(mol*s)'),
        n = 2.86,
        Ea = (9768, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
C_(T)
multiplicity 3
1 C U4 L0 E0 
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
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
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30690000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (115970000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7845000000000.0, 'cm^3/(mol*s)'),
        n = 0.1,
        Ea = (10600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
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
        A = (33.016, 'cm^3/(mol*s)'),
        n = 3.36,
        Ea = (4310, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H
multiplicity 2
1 H U1 L0 E0 
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
        A = (41500000.0, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (1924, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (37900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (596, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (1500000000000.0, 'cm^3/(mol*s)'),
        n = 0.5,
        Ea = (-110, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (262000000000000.0, 'cm^3/(mol*s)'),
        n = -0.23,
        Ea = (1070, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3780000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        A = (18100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        A = (21700000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1750, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (24400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (10500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (32800000000000.0, 'cm^3/(mol*s)'),
        n = -0.09,
        Ea = (610, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (90300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        A = (24100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
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
        A = (72300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3736, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (497340, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (9588, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (665280000.0, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (8485, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (968000, 'cm^3/(mol*s)'),
        n = 2.182,
        Ea = (2446, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (47846, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (21000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
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
C2H4
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-397, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (18644000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (3430000000.0, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (4491, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (1140000000.0, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (5860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (24700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5306, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (8200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9040, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        Ea = (497, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (358000, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (42760, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 121,
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
        A = (2.28e-05, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (10213, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2O2
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 O U0 L2 E0  {1,S} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0334, 'cm^3/(mol*s)'),
        n = 4.12,
        Ea = (16233, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.04e+18, 'cm^3/(mol*s)'),
        n = -1.93,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (32, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (7175, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (14.5, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (6940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (7000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-550, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-550, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (665, 'cm^3/(mol*s)'),
        n = 3.03,
        Ea = (8720, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
        A = (21500, 'cm^3/(mol*s)'),
        n = 2.27,
        Ea = (8710, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
        A = (1200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
        A = (32, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (7175, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
        A = (14.5, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (6940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        A = (54000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2110000.0, 'cm^3/(mol*s)'),
        n = 2.32,
        Ea = (882, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (161860000000000.0, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
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
CH2_(S)
multiplicity 1
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
        A = (131340000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
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
    product3 = 
"""
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (173000000000000.0, 'cm^3/(mol*s)'),
        n = -0.112,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
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
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1113, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
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
        A = (1630000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (854, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
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
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product3 = 
"""
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (846040000.0, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (2206, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    product2 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (214090000.0, 'cm^3/(mol*s)'),
        n = 1.4,
        Ea = (2206, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.85746, 'cm^3/(mol*s)'),
        n = 3.566,
        Ea = (-2370, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
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
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
        A = (2630000.0, 'cm^3/(mol*s)'),
        n = 2.14,
        Ea = (17060, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
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
        A = (614000, 'cm^3/(mol*s)'),
        n = 1.62,
        Ea = (-731, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2CC_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U2 L0 E0  {1,D}
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2CC_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U2 L0 E0  {1,D}
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
H2CC_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U2 L0 E0  {1,D}
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
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
        A = (42000000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (11850, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (777000000.0, 'cm^3/(mol*s)'),
        n = 1.45,
        Ea = (2780, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
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
        A = (1080000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1351, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (361000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1351, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (361000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1351, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
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
        A = (11200, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (2220, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (680000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1013, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1010000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1013, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
        A = (145000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 163,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1210000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 164,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
H2CC_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U2 L0 E0  {1,D}
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
        A = (63089000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 165,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 166,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 167,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
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
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 168,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 169,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
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
        A = (6324500000000000.0, 'cm^3/(mol*s)'),
        n = -1.04,
        Ea = (827, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 170,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14164000000.0, 'cm^3/(mol*s)'),
        n = 0.656,
        Ea = (848, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 171,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
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
        A = (3690, 'cm^3/(mol*s)'),
        n = 2.4,
        Ea = (1778, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 172,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-765, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 173,
    reactant1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
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
        A = (22000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 174,
    reactant1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
        A = (11000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 175,
    reactant1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
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
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 176,
    reactant1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product3 = 
"""
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (158000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 177,
    reactant1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 178,
    reactant1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
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
        A = (30100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 179,
    reactant1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (23000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 180,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 181,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
        A = (52700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 182,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (158000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 183,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 184,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 185,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
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
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 186,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
    product2 = 
"""
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (23000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 187,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6080000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 188,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
        A = (2050000000.0, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2405, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 189,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
        A = (2050000000.0, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (2405, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 190,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
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
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2920000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1808, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 191,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
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
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2920000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1808, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 192,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
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
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
        A = (269000000.0, 'cm^3/(mol*s)'),
        n = 1.35,
        Ea = (-1574, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 193,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
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
    product2 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (37560, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 194,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
        A = (41000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 195,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
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
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
        A = (2720000.0, 'cm^3/(mol*s)'),
        n = 1.77,
        Ea = (5920, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 196,
    reactant1 = 
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
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
        A = (214.32, 'cm^3/(mol*s)'),
        n = 3.62,
        Ea = (11270, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 197,
    reactant1 = 
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8130000.0, 'cm^3/(mol*s)'),
        n = 1.88,
        Ea = (183, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 198,
    reactant1 = 
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
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3622300000.0, 'cm^3/(mol*s)'),
        n = 0.907,
        Ea = (839, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 199,
    reactant1 = 
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
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (13804, 'cm^3/(mol*s)'),
        n = 2.62,
        Ea = (459, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 200,
    reactant1 = 
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
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
        A = (23415, 'cm^3/(mol*s)'),
        n = 2.745,
        Ea = (2216, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 201,
    reactant1 = 
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
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
        A = (60200000.0, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (16630, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 202,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
C2H4
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1810000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 203,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 204,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (58900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 205,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
C2H4
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (29400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 206,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
    product2 = 
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
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14100000.0, 'cm^3/(mol*s)'),
        n = 1.09,
        Ea = (-1975, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 207,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
C2H4
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 208,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
        A = (5500, 'cm^3/(mol*s)'),
        n = 2.81,
        Ea = (5860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 209,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
        A = (32, 'cm^3/(mol*s)'),
        n = 3.2,
        Ea = (7175, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 210,
    reactant1 = 
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
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
        A = (113510000.0, 'cm^3/(mol*s)'),
        n = 1.9,
        Ea = (7530, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 211,
    reactant1 = 
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
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (167790, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (5803, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 212,
    reactant1 = 
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
    reactant2 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
        A = (9543500.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (994, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 213,
    reactant1 = 
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
    reactant2 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
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
C2H4
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (108000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-262, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 214,
    reactant1 = 
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
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-660, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 215,
    reactant1 = 
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
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (56000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (9420, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (881780000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (22260, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 217,
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
            A = (3.8426e+19, 'cm^3/(mol*s)'),
            n = -1.4,
            Ea = (104390, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.0, '[C]=O': 1.9, '[Ar]': 0.0},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 218,
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
            A = (6160000000000000.0, 'cm^6/(mol^2*s)'),
            n = -0.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.0, '[C]=O': 1.9, '[Ar]': 0.0},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 219,
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
        arrheniusLow = Arrhenius(
            A = (2.9532e+18, 'cm^6/(mol^2*s)'),
            n = -1,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 12.0, '[H][H]': 2.5, '[He]': 0.75, '[C]=O': 1.9, '[Ar]': 0.75},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 220,
    reactant1 = 
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.4502e+28, 'cm^3/(mol*s)'),
            n = -3.322,
            Ea = (120800, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'O=C=O': 3.8, 'O': 0.0, '[H][H]': 3.0, '[He]': 0.22, '[O][O]': 1.5, 'N#N': 2.0, '[C]=O': 1.9, '[Ar]': 0.36},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 221,
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
            A = (4650000000000.0, 'cm^3/(mol*s)'),
            n = 0.44,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.37e+20, 'cm^6/(mol^2*s)'),
            n = -1.72,
            Ea = (525, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (30, 'K'),
        T1 = (90000, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'O=C=O': 2.02, 'O': 12.36, '[H][H]': 1.08, '[He]': 0.57, '[O][O]': 0.54, '[C]=O': 1.08, '[Ar]': 0.39},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 222,
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
            A = (1982000000000.0, 's^-1'),
            n = 0.9,
            Ea = (48750, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.4676e+24, 'cm^3/(mol*s)'),
            n = -2.3,
            Ea = (48750, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.58,
        T3 = (30, 'K'),
        T1 = (90000, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'OO': 7.7, 'O=C=O': 1.6, 'O': 7.5, '[H][H]': 3.7, '[He]': 0.65, '[O][O]': 1.2, 'N#N': 1.5, '[C]=O': 2.8},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 223,
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
            A = (51912000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (2430, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.0376e+21, 'cm^6/(mol^2*s)'),
            n = -2.1,
            Ea = (5500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12.0, '[Ar]': 0.87},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 224,
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
            A = (5.0592e+17, 'cm^3/(mol*s)'),
            n = -1.2,
            Ea = (17734, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 9.55, 'C=O': 2.5, '[He]': 0.95, '[C]=O': 1.5, '[Ar]': 1.02},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 225,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (51659000000000.0, 'cm^3/(mol*s)'),
            n = 0.15,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.447e+22, 'cm^6/(mol^2*s)'),
            n = -1.6,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.514,
        T3 = (152, 'K'),
        T1 = (22850, 'K'),
        T2 = (10350, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 226,
    reactant1 = 
"""
CH_(Q)
multiplicity 4
1 C U3 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
HCCO
multiplicity 2
1 C U0 L0 E0  {2,T} {4,S}
2 C U0 L0 E0  {1,T} {3,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1020000000000000.0, 'cm^3/(mol*s)'),
            n = -0.4,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.26e+24, 'cm^6/(mol^2*s)'),
            n = -2.5,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.4,
        T3 = (30, 'K'),
        T1 = (90000, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 227,
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
        arrheniusHigh = Arrhenius(
            A = (21300000000000.0, 'cm^3/(mol*s)'),
            n = 0.32,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.39e+34, 'cm^6/(mol^2*s)'),
            n = -5.04,
            Ea = (7400, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.405,
        T3 = (258, 'K'),
        T1 = (2811, 'K'),
        T2 = (9908, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 228,
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
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 229,
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (308390000000000.0, 'cm^3/(mol*s)'),
            n = -0.033,
            Ea = (-142, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.947e+34, 'cm^6/(mol^2*s)'),
            n = -5.533,
            Ea = (6128, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.782,
        T3 = (271, 'K'),
        T1 = (2755, 'K'),
        T2 = (6570, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 230,
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(37000000000000.0, 's^-1'), n=0, Ea=(71976, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (4.4e+38, 'cm^3/(mol*s)'),
            n = -6.1,
            Ea = (94000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.932,
        T3 = (197, 'K'),
        T1 = (1540, 'K'),
        T2 = (10300, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 231,
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
            A = (124490000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.6787e+24, 'cm^6/(mol^2*s)'),
            n = -2.17,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.124,
        T3 = (1801, 'K'),
        T1 = (33.1, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 232,
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
            A = (3.3647e+18, 'cm^3/(mol*s)'),
            n = -1.43,
            Ea = (1330, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (4.824e+36, 'cm^6/(mol^2*s)'),
            n = -5.92,
            Ea = (3140, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.412,
        T3 = (195, 'K'),
        T1 = (5900, 'K'),
        T2 = (6394, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 233,
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
            A = (2.12e+16, 'cm^3/(mol*s)'),
            n = -0.97,
            Ea = (620, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.77e+50, 'cm^6/(mol^2*s)'),
            n = -9.67,
            Ea = (6220, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5325,
        T3 = (151, 'K'),
        T1 = (1038, 'K'),
        T2 = (4970, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 234,
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
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(68000000000000.0, 's^-1'), n=0, Ea=(26154, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (1.87e+25, 'cm^3/(mol*s)'),
            n = -3,
            Ea = (24300, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.5,
        T3 = (1413, 'K'),
        T1 = (1413, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 235,
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
        T3 = (30, 'K'),
        T1 = (90000, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 236,
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
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (280000000000000.0, 's^-1'),
            n = -0.73,
            Ea = (32820, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.02e+33, 'cm^3/(mol*s)'),
            n = -5.39,
            Ea = (36200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.96,
        T3 = (67.6, 'K'),
        T1 = (1855, 'K'),
        T2 = (7543, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 237,
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
            A = (1060000000000.0, 'cm^3/(mol*s)'),
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
        T3 = (30, 'K'),
        T1 = (90000, 'K'),
        T2 = (90000, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 238,
    reactant1 = 
"""
C2H
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 C U1 L0 E0  {1,T}
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
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (22500000000000.0, 'cm^3/(mol*s)'),
            n = 0.32,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
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
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 239,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
H2CC_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U2 L0 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (800000000000000.0, 's^-1'),
            n = -0.52,
            Ea = (50750, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2450000000000000.0, 'cm^3/(mol*s)'),
            n = -0.64,
            Ea = (49700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 240,
    reactant1 = 
"""
C2H2
multiplicity 1
1 C U0 L0 E0  {2,T} {3,S}
2 C U0 L0 E0  {1,T} {4,S}
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
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (524080000.0, 'cm^3/(mol*s)'),
            n = 1.64,
            Ea = (2096, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.434e+27, 'cm^6/(mol^2*s)'),
            n = -3.38,
            Ea = (847, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.215,
        T3 = (10.7, 'K'),
        T1 = (1043, 'K'),
        T2 = (2341, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 241,
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
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
        alpha = 0.591,
        T3 = (275, 'K'),
        T1 = (1226, 'K'),
        T2 = (5185, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 242,
    reactant1 = 
"""
C2H3
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U1 L0 E0  {1,D} {5,S}
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
C2H4
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (38800000000000.0, 'cm^3/(mol*s)'),
            n = 0.2,
            Ea = (0, 'cal/mol'),
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
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 243,
    reactant1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH2CO
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1430000000000000.0, 's^-1'),
            n = -0.15,
            Ea = (45606, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.44e+29, 'cm^3/(mol*s)'),
            n = -3.79,
            Ea = (43577, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.796,
        T3 = (100, 'K'),
        T1 = (50000, 'K'),
        T2 = (34200, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[H][H]': 2.0, '[C]=O': 1.5, 'C=C': 3.0, 'C#C': 3.0},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 244,
    reactant1 = 
"""
CH2CHO
multiplicity 2
1 C U0 L0 E0  {2,D} {4,S} {5,S}
2 C U0 L0 E0  {1,D} {3,S} {6,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (2930000000000.0, 's^-1'),
            n = 0.29,
            Ea = (40326, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.34e+27, 'cm^3/(mol*s)'),
            n = -3.18,
            Ea = (33445, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.211,
        T3 = (199, 'K'),
        T1 = (2032, 'K'),
        T2 = (111700, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[H][H]': 2.0, '[C]=O': 1.5, 'C=C': 3.0, 'C#C': 3.0},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 245,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1070000000000.0, 's^-1'),
            n = 0.63,
            Ea = (16895, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (5.65e+18, 'cm^3/(mol*s)'),
            n = -0.97,
            Ea = (14585, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.36,
        T3 = (122, 'K'),
        T1 = (50000, 'K'),
        T2 = (16940, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[H][H]': 2.0, '[C]=O': 1.5, 'C=C': 3.0, 'C#C': 3.0},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 246,
    reactant1 = 
"""
CH3CO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (96000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (3.85e+44, 'cm^6/(mol^2*s)'),
            n = -8.569,
            Ea = (5500, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1,
        T3 = (2900, 'K'),
        T1 = (2900, 'K'),
        T2 = (5132, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[H][H]': 2.0, '[C]=O': 1.5, 'C=C': 3.0, 'C#C': 3.0},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 247,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
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
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(5.44e+21, 's^-1'), n=-1.74, Ea=(86364, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (2.29e+58, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95922, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.92,
        T3 = (50000, 'K'),
        T1 = (10, 'K'),
        T2 = (8200, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[H][H]': 2.0, '[C]=O': 1.5, 'C=C': 3.0, 'C#C': 3.0},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 248,
    reactant1 = 
"""
CH3CHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.18e+22, 's^-1'), n=-1.74, Ea=(86364, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (9.15e+58, 'cm^3/(mol*s)'),
            n = -11.3,
            Ea = (95922, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.92,
        T3 = (50000, 'K'),
        T1 = (10, 'K'),
        T2 = (8200, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[H][H]': 2.0, '[C]=O': 1.5, 'C=C': 3.0, 'C#C': 3.0},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 249,
    reactant1 = 
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
    product1 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2CC_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U2 L0 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (8000000000000.0, 's^-1'),
            n = 0.44,
            Ea = (86770, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(3.71e+16, 'cm^3/(mol*s)'), n=0, Ea=(67816, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.735,
        T3 = (180, 'K'),
        T1 = (1035, 'K'),
        T2 = (5417, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 250,
    reactant1 = 
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
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (719250000.0, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1355, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.5225e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 1.569,
        T3 = (-9147, 'K'),
        T1 = (299, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 251,
    reactant1 = 
"""
C2H5
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
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
        efficiencies = {'C': 2.0, 'CO': 3.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, 'C=O': 2.5, '[He]': 0.7, '[C]=O': 1.5, '[Ar]': 0.7},
        comment = 'Reaction and kinetics from ERC-FoundationFuelv0.9.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

