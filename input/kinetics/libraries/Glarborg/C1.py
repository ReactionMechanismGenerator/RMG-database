#!/usr/bin/env python
# encoding: utf-8

name = "Glarborg/C1"
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
        A = (3600000000000000.0, 'cm^3/(mol*s)'),
        n = -0.41,
        Ea = (16600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant3 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
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
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+17, 'cm^6/(mol^2*s)'),
        n = -0.6,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    reactant3 = 
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+19, 'cm^6/(mol^2*s)'),
        n = -1,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (4300, 'cm^3/(mol*s)'),
        n = 2.7,
        Ea = (-1822, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (210000000.0, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (3449, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
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
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
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
        A = (740000, 'cm^3/(mol*s)'),
        n = 2.433,
        Ea = (53502, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (84000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-445, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (28900000000000.0, 'cm^3/(mol*s)', '*|/', 1.58),
        n = 0,
        Ea = (-497, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3580, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (1700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3760, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
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
        A = (9600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3970, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
                A = (1900000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (427, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(1.6e+18, 'cm^3/(mol*s)'), n=0, Ea=(29410, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (4700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (60500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17943, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
HOCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,D}
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
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
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
                A = (4600000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (-89, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(9500000.0, 'cm^3/(mol*s)'), n=2, Ea=(-89, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
HOCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,D}
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
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
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
HOCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {2,S}
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
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (990000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (410000000.0, 'cm^3/(mol*s)'),
        n = 1.47,
        Ea = (2444, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (420000000000.0, 'cm^3/(mol*s)'),
        n = 0.57,
        Ea = (2760, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (240000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (36461, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (78000000.0, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (-1055, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (41000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10206, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (32, 'cm^3/(mol*s)'),
        n = 3.36,
        Ea = (4310, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (110000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (110000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (3400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (27000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (4100, 'cm^3/(mol*s)'),
        n = 3.156,
        Ea = (8755, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (440000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (6577, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (1000000.0, 'cm^3/(mol*s)'),
        n = 2.182,
        Ea = (2506, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (47000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (21000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (4300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10030, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (43000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
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
        A = (90000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (72000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (69000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
O_(T)
multiplicity 3
1 O U2 L2 E0 
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (1100, 'cm^3/(mol*s)'),
        n = 3,
        Ea = (2780, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (3000000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (120000, 'cm^3/(mol*s)'),
        n = 2.228,
        Ea = (-3020, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0.2688,
        Ea = (-687.5, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (7500000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (28297, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (190000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9842, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (28000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (16055, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
    product3 = 
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (2.2e+22, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
    product3 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
    kinetics = Arrhenius(
        A = (2.6e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+21, 'cm^3/(mol*s)'),
        n = -3.3,
        Ea = (2867, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH2_(T)
multiplicity 3
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
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH2_(T)
multiplicity 3
1 C U2 L0 E0  {2,S} {3,S}
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
        A = (200000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
H
multiplicity 2
1 H U1 L0 E0 
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (11000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (2900000000.0, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (4491, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (510000000.0, 'cm^3/(mol*s)'),
        n = 1.24,
        Ea = (4491, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (21000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5305, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (3700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5305, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (150000000.0, 'cm^3/(mol*s)'),
        n = 1.4434,
        Ea = (113, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (27000000.0, 'cm^3/(mol*s)'),
        n = 1.4434,
        Ea = (113, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (46600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (54800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (66000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-693, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
                A = (72000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (3736, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(A=(2.9e+16, 'cm^3/(mol*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
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
        Ea = (5862, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (4800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (2400000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22, 'cm^3/(mol*s)'),
        n = 3.1,
        Ea = (16227, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (53000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (745, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (4600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (745, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (3800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
    kinetics = Arrhenius(
        A = (22000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1749, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (9.5e+25, 'cm^3/(mol*s)'),
        n = -4.93,
        Ea = (9080, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (130000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (15073, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 O U0 L2 E0  {1,D}
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
        A = (100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2981, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OOH
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product3 = 
"""
H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OOH
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3OO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
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
        A = (54000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OOH
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (12000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OOH
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
    product3 = 
"""
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4750, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OOH
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3OO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
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
        A = (8700000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (4750, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OOH
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
CH3OO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
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
        A = (1100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-437, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OOH
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        A = (720000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-258, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OOH
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 O U0 L2 E0  {2,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
CH3OO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
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
        Ea = (10206, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
        A = (16000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-445, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
        A = (2000000000000000.0, 'cm^3/(mol*s)'),
        n = -0.6,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (400000000000.0, 'cm^3/(mol*s)'),
        n = 0.6,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
CH3OOH
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
        A = (250000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1490, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
        A = (5100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1411, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
CH4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3OOH
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (21000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
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
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
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
CO2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 O U0 L2 E0  {1,D}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.18,
        Ea = (17940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
CH3OOH
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
        A = (41000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (10206, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
CH3OOH
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
        A = (300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
CH3OOH
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
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19400, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
CH3OO
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
    product3 = 
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
CH3OO
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
    product3 = 
"""
O2_(T)
multiplicity 3
1 O U1 L2 E0  {2,S}
2 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (200000000000.0, 'cm^3/(mol*s)'),
        n = -0.55,
        Ea = (-1600, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
CH3CH2O
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {1,S} {3,S} {7,S} {8,S}
3 O U1 L2 E0  {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1410, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
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
    product1 = 
"""
CH3OOH
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
        A = (19, 'cm^3/(mol*s)'),
        n = 3.64,
        Ea = (17100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(37000000000000.0, 's^-1'), n=0, Ea=(71969, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (5661000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (65849, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        efficiencies = {'[H][H]': 2.5, '[C]=O': 1.9, 'O=C=O': 3.8, 'O': 12.0},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
            A = (36000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (1.269e+41, 'cm^6/(mol^2*s)'),
            n = -7,
            Ea = (2762, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.62,
        T3 = (73, 'K'),
        T1 = (1180, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'O=C=O': 3.0, 'O': 5.0},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        efficiencies = {'C': 2.0, 'O=C=O': 2.0, 'CC': 3.0, 'O': 6.0, '[H][H]': 2.0, 'N#N': 1.0, '[C]=O': 1.5},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(7e+17, 'cm^6/(mol^2*s)'), n=-1, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0.0, 'O': 0.0, 'N#N': 0.0},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
H
multiplicity 2
1 H U1 L0 E0 
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
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(6.2e+16, 'cm^6/(mol^2*s)'), n=-0.6, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'O': 5.0},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
            A = (19000000000000.0, 'cm^6/(mol^2*s)'),
            n = 0,
            Ea = (-1788, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[O][O]': 1.5, 'O': 10.0, 'N#N': 1.5},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
OH
multiplicity 2
1 O U1 L2 E0  {2,S}
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(4.5e+22, 'cm^6/(mol^2*s)'), n=-2, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {'[H][H]': 0.73, 'O': 12.0, '[Ar]': 0.38},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
            A = (10000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H]': 0.0, 'O': 0.0, 'N#N': 0.0, '[Ar]': 0.0},
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
            ),
        ],
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
HOCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {2,S}
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
            ),
        ],
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
HOCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 O U0 L2 E0  {1,S} {4,S}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {2,S}
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
            ),
        ],
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OO
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U1 L2 E0  {2,S}
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
            ),
        ],
        comment = 'Reaction and kinetics from Glarborg\\C1.',
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
CH3OOH
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
    kinetics = PDepArrhenius(
        pressures = ([1, 10, 50, 1000], 'atm'),
        arrhenius = [
            Arrhenius(A=(2e+35, 's^-1'), n=-6.7, Ea=(47450, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.1e+28, 's^-1'), n=-4.15, Ea=(46190, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.8e+26, 's^-1'), n=-3.5, Ea=(46340, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(2.2e+17, 's^-1'), n=-0.42, Ea=(44622, 'cal/mol'), T0=(1, 'K')),
        ],
        comment = 'Reaction and kinetics from Glarborg\\C1.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

