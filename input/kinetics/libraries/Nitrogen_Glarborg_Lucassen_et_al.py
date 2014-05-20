#!/usr/bin/env python
# encoding: utf-8

name = "Nitrogen_Glarborg_Lucassen_et_al"
shortDesc = u""
longDesc = u"""
Arnas Lucassen, Kuiwen Zhang, Julia Warkentin, Kai Moshammer, Peter Glarborg, Paul Marshall, Katharina Kohse-Höinghaus
Fuel-nitrogen conversion in the combustion of small amines using dimethylamine and ethylamine as biomass-related model fuels
Combustion and Flame 159 (2012) 2254–2279
"""
entry(
    index        = 1,
    reactant1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (24000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (107260, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
        A = (560000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5464, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
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
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9706, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
        A = (400000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5196, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
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
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6348, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
        A = (8000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
        A = (1500000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9170, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (5494, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7143, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
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
        A = (1.1e+45, 's^-1'),
        n = -10.24,
        Ea = (47817, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+22, 'cm^3/(mol*s)'),
        n = -3.09,
        Ea = (6756, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2702, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-626, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
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
        A = (1.6e+36, 's^-1'),
        n = -7.92,
        Ea = (36342, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
        A = (720000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
        A = (500000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
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
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (7322, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
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
        A = (300000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6130, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
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
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4630, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
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
        A = (220000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5404, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NH_(S)
multiplicity 1
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1700000.0, 'cm^3/(mol*s)'),
        n = 2.08,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
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
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-89, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
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
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (457, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
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
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (7123, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
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
        A = (530000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9687, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (4441, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6090, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+29, 's^-1'),
        n = -6.03,
        Ea = (29894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
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
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
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
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
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
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
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
                A = (2.1e+17, 'cm^3/(mol*s)'),
                n = -1.68,
                Ea = (318, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1200000.0, 'cm^3/(mol*s)'),
                n = 2,
                Ea = (-1192, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5961, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
NH_(S)
multiplicity 1
1 N U2 L1 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    reactant2 = 
"""
N_(Q)
multiplicity 4
1 N U3 L1 E0 
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
N2
multiplicity 1
1 N U0 L1 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.7e+25, 's^-1'),
        n = -5.2,
        Ea = (21986, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
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
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
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
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
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
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
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
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
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
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
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
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
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
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
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
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
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
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
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
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2e+67, 's^-1'),
        n = -15.944,
        Ea = (99348, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (17000000000000.0, 'cm^3/(mol*s)'),
        n = 0.22,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54000000000000.0, 'cm^3/(mol*s)'),
        n = 0.16,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (12000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (5100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (26000000.0, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (2830, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
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
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (94000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (5460, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (6800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1275, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
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
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6348, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (1600000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (14000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
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
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
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
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (447, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (12000, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (15750, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (8200, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (10750, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (220, 'cm^3/(mol*s)'),
        n = 3.18,
        Ea = (9620, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (730, 'cm^3/(mol*s)'),
        n = 2.99,
        Ea = (7950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
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
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
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
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (220, 'cm^3/(mol*s)'),
        n = 3.18,
        Ea = (9620, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (730, 'cm^3/(mol*s)'),
        n = 2.99,
        Ea = (7950, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7140, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (120000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (3955, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
        A = (1800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (96000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    product1 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.7e+16, 'cm^3/(mol*s)'),
        n = -1.63,
        Ea = (3418, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
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
        A = (60000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CH2NH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,S} {7,S}
3 N U0 L1 E0  {1,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
        n = -0.32,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.1e+45, 's^-1'),
        n = -10.24,
        Ea = (47817, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
        A = (490000000.0, 'cm^3/(mol*s)'),
        n = 1.7,
        Ea = (588, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.4e+16, 'cm^3/(mol*s)'),
        n = -0.891,
        Ea = (2903, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.7e+21, 'cm^3/(mol*s)'),
        n = -3.02,
        Ea = (2845, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
        A = (25000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
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
    product3 = 
"""
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (24000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
HO2
multiplicity 2
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.7e+20, 'cm^3/(mol*s)'),
        n = -3.02,
        Ea = (2504, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    product1 = 
"""
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
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
        A = (120000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-769, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
        A = (19000000000.0, 's^-1'),
        n = 0,
        Ea = (23500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+36, 's^-1'),
        n = -7.92,
        Ea = (36342, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
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
CH2NH2
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1400000000000.0, 'cm^3/(mol*s)'),
        n = 0.701,
        Ea = (346, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
        A = (720000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
        A = (500000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
        A = (3600000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CH2NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (240, 'cm^3/(mol*s)'),
        n = 3.63,
        Ea = (11266, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
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
        A = (240, 'cm^3/(mol*s)'),
        n = 3.63,
        Ea = (11266, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9700, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (3900000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (1494, 'cal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (62000000000000.0, 'cm^3/(mol*s)'),
                n = 0,
                Ea = (6855, 'cal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6348, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (0.13, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
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
        A = (0.13, 'cm^3/(mol*s)'),
        n = 4.2,
        Ea = (-860, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (447, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (60000000.0, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (16630, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
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
    kinetics = Arrhenius(
        A = (60000000.0, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (16630, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10274, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5300000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (10274, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7143, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5e+18, 's^-1'),
        n = -2.4965,
        Ea = (67995, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (58000000000000.0, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (-125, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        A = (47000000000000.0, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (1900000000000.0, 'cm^3/(mol*s)'),
        n = 0.4,
        Ea = (5359, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
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
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (7322, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        A = (1.8e+18, 'cm^3/(mol*s)'),
        n = -1.9,
        Ea = (2975, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (37000000000000.0, 'cm^3/(mol*s)'),
        n = -0.2,
        Ea = (3556, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
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
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4630, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        A = (240000000000.0, 'cm^3/(mol*s)'),
        n = 0.3,
        Ea = (-1000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        n = -0.6,
        Ea = (800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
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
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-89, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        A = (3.9e-07, 'cm^3/(mol*s)'),
        n = 5.8,
        Ea = (2200, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
        A = (25, 'cm^3/(mol*s)'),
        n = 3.15,
        Ea = (5727, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
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
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (7123, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHNH_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U1 L1 E0  {2,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (4441, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
C2H2
multiplicity 1
1 H U0 L0 E0  {2,S}
2 C U0 L0 E0  {1,S} {3,T}
3 C U0 L0 E0  {2,T} {4,S}
4 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.8e-18, 'cm^3/(mol*s)'),
        n = 8.31,
        Ea = (7430, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (45000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
OCHCHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (45000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
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
CH2CO_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 C U1 L0 E0  {1,S} {5,D}
5 O U0 L2 E0  {4,D}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
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
OCHCHO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 O U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.7e+17, 'cm^3/(mol*s)'),
        n = -1.757,
        Ea = (11067, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.5e+18, 's^-1'),
        n = -2.52,
        Ea = (33000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.7e+25, 's^-1'),
        n = -5.2,
        Ea = (24000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (21000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (12000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (160000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (53000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1900000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
        A = (53000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CNH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-1113, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (9900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CHN_(T)
multiplicity 3
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
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
CH2CHN_(T)
multiplicity 3
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
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
CH2CHN_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
        A = (44000000000000.0, 'cm^3/(mol*s)'),
        n = -0.3485,
        Ea = (-727, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CHN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 N U1 L1 E0  {2,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-1152, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9706, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6348, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
HCCO
multiplicity 2
1 H U0 L0 E0  {2,S}
2 C U0 L0 E0  {1,S} {3,T}
3 C U0 L0 E0  {2,T} {4,S}
4 O U1 L2 E0  {3,S}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (14000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (1900, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
        A = (2000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7143, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25000000000000.0, 's^-1'),
        n = 0,
        Ea = (70300, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (33000000000.0, 'cm^3/(mol*s)'),
        n = 0.851,
        Ea = (2840, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
        A = (30000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
        A = (240000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (7322, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1350, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
        A = (20000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (10000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
        A = (170000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (4630, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1013, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (670000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1013, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
        A = (10000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (3000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
        A = (1200000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-89, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
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
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (7123, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CNH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 N U0 L1 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (4441, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(T)
multiplicity 3
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(T)
multiplicity 3
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(T)
multiplicity 3
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CHN_(T)
multiplicity 3
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
""",
    product1 = 
"""
c-C2H3N
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {3,S} {5,S}
3 N U0 L1 E0  {1,S} {2,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 's^-1'),
        n = 0,
        Ea = (4000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
""",
    product1 = 
"""
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 's^-1'),
        n = 0,
        Ea = (8000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product3 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CHN_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    product3 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
c-C2H3N
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {3,S} {5,S}
3 N U0 L1 E0  {1,S} {2,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (47000000000000.0, 's^-1'),
        n = 0,
        Ea = (41500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
c-C2H3N
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {3,S} {5,S}
3 N U0 L1 E0  {1,S} {2,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9800000000.0, 'cm^3/(mol*s)'),
        n = 1.212,
        Ea = (1969, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
c-C2H3N
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {3,S} {5,S}
3 N U0 L1 E0  {1,S} {2,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CHNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 N U1 L1 E0  {1,S} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (11000000000.0, 'cm^3/(mol*s)'),
        n = 1.229,
        Ea = (2422, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
c-C2H3N
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {3,S} {5,S}
3 N U0 L1 E0  {1,S} {2,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
c-C2H3N
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {3,S} {5,S}
3 N U0 L1 E0  {1,S} {2,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
C2H3
multiplicity 2
1 H U0 L0 E0  {2,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U0 L0 E0  {2,D} {4,S} {5,S}
4 H U0 L0 E0  {3,S}
5 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
NO
multiplicity 2
1 N U1 L1 E0  {2,D}
2 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
c-C2H3N
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {3,S} {5,S}
3 N U0 L1 E0  {1,S} {2,S} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {3,S}
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    product2 = 
"""
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    product1 = 
"""
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (790000000000000.0, 's^-1'),
        n = 0,
        Ea = (94940, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
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
        A = (44000000000.0, 'cm^3/(mol*s)'),
        n = 0.8,
        Ea = (6800, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
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
        A = (2800000000000000.0, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (20030, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
        A = (60000, 'cm^3/(mol*s)'),
        n = 3.01,
        Ea = (8522, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6000000000.0, 'cm^3/(mol*s)'),
        n = 1.8,
        Ea = (8130, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
        A = (470000000.0, 'cm^3/(mol*s)'),
        n = 1.18,
        Ea = (14360, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
        A = (20000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
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
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
        A = (5000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (7000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3CN_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 N U1 L1 E0  {2,D}
""",
    reactant2 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
""",
    product2 = 
"""
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1300000000000.0, 'cm^3/(mol*s)'),
        n = 0.64,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 216,
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
CN
multiplicity 2
1 C U1 L0 E0  {2,T}
2 N U0 L1 E0  {1,T}
""",
    product1 = 
"""
CH2CN
multiplicity 2
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 N U1 L1 E0  {2,D}
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
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (150000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (100000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
HCNH
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 N U0 L1 E0  {1,D} {4,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4900000000000.0, 'cm^3/(mol*s)'),
        n = -0.142,
        Ea = (1150, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
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
        A = (160000000000.0, 'cm^3/(mol*s)'),
        n = -0.02,
        Ea = (1020, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CHCNH
multiplicity 2
1 C U0 L0 E0  {2,D} {3,D}
2 C U1 L0 E0  {1,D} {4,S}
3 N U0 L1 E0  {1,D} {5,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {3,S}
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
HNC
multiplicity 1
1 N U0 L0 E+1 {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 C U0 L1 E-1 {1,T}
""",
    product2 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    product3 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (220, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (3540, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U0 L2 E0  {2,D}
""",
    product1 = 
"""
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(1.4e+16, 'cm^3/(mol*s)'), n=0, Ea=(72900, 'cal/mol'), T0=(1, 'K')),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U0 L2 E0  {2,D}
""",
    product1 = 
"""
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
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
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (4600000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (64200, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
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
        A = (13000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6955, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
HCO
multiplicity 2
1 C U1 L0 E0  {2,S} {3,D}
2 H U0 L0 E0  {1,S}
3 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (19100, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
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
        A = (400000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5196, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
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
        A = (8000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
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
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
        A = (700000, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (9000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U0 L2 E0  {2,D}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2000000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (5000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
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
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
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
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
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
HNCO
multiplicity 1
1 N U0 L1 E0  {2,D} {3,S}
2 C U0 L0 E0  {1,D} {4,D}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {2,D}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (560000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5464, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
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
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (9706, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (6100000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (556, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
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
        A = (3000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (556, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
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
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
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
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
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
        A = (19000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
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
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
        A = (1500000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9170, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
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
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
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
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8842, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (5494, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (7143, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH2NH_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 N U1 L1 E0  {1,S} {5,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.8e+43, 's^-1'),
        n = -10.302,
        Ea = (37459, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.9e+44, 's^-1'),
        n = -10.314,
        Ea = (46803, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
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
        A = (480000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
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
        A = (330000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-894, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (40000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
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
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
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
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-1192, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 252,
    reactant1 = 
"""
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH3NH
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U1 L1 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2702, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 253,
    reactant1 = 
"""
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
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
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
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
        A = (1600000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-626, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 254,
    reactant1 = 
"""
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1600000000000000.0, 's^-1'),
        n = -7.544,
        Ea = (38425, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 255,
    reactant1 = 
"""
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
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
        A = (3200000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 256,
    reactant1 = 
"""
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
O_(T)
multiplicity 3
1 O U2 L2 E0 
""",
    product1 = 
"""
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
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
        A = (50000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 257,
    reactant1 = 
"""
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
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
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
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
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 258,
    reactant1 = 
"""
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
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
CH3NO
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 O U0 L2 E0  {2,D}
""",
    product2 = 
"""
CH3O
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U1 L2 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000.0, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (6000, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 259,
    reactant1 = 
"""
CH3NCH3
multiplicity 2
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
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
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
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
        A = (6000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 260,
    reactant1 = 
"""
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
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
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (58000000000000.0, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (-125, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 261,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
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
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
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
        A = (560000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5464, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 262,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
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
CH3NCH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        A = (300000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6130, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 263,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
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
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
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
        A = (400000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5196, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 264,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
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
CH3NCH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        A = (220000000.0, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (5404, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 265,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
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
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
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
        A = (8000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 266,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
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
CH3NCH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        A = (2400000.0, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (457, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 267,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
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
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
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
    kinetics = Arrhenius(
        A = (1500000.0, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9170, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 268,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
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
CH3NCH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
        A = (530000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (9687, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 269,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (5494, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 270,
    reactant1 = 
"""
CH3NCH2_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {3,S} {7,S} {8,S}
3 N U1 L1 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    reactant2 = 
"""
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NCH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1800000.0, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (6090, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 271,
    reactant1 = 
"""
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3NCH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.3e+45, 's^-1'),
        n = -10.068,
        Ea = (66111, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 272,
    reactant1 = 
"""
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 273,
    reactant1 = 
"""
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
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
CH2O
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 O U0 L2 E0  {1,D}
""",
    product2 = 
"""
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (30000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 274,
    reactant1 = 
"""
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
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
H2CN
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,D}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 N U1 L1 E0  {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 275,
    reactant1 = 
"""
CH3NCH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
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
HCN
multiplicity 1
1 C U0 L0 E0  {2,S} {3,T}
2 H U0 L0 E0  {1,S}
3 N U0 L1 E0  {1,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8100000000000000.0, 's^-1'),
        n = -2.375,
        Ea = (14942, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 276,
    reactant1 = 
"""
CH3NCH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {7,S}
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
CH2NCH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U1 L0 E0  {3,S} {6,S} {7,S}
3 N U0 L1 E0  {1,D} {2,S}
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
        A = (20000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 277,
    reactant1 = 
"""
CH3NCH
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {7,S}
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
CH3
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
NCO
multiplicity 2
1 C U0 L0 E0  {2,T} {3,S}
2 N U0 L1 E0  {1,T}
3 O U1 L2 E0  {1,S}
""",
    product3 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (70000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 278,
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3NH2
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 N U0 L1 E0  {1,S} {6,S} {7,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (7200000000000.0, 'cm^3/(mol*s)'),
            n = 0.42,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -3.85,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 279,
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3CH2NH2
multiplicity 1
1  C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2  C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3  N U0 L1 E0  {1,S} {9,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {2,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {3,S}
10 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (7200000000000.0, 'cm^3/(mol*s)'),
            n = 0.42,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2.2e+30, 'cm^6/(mol^2*s)'),
            n = -3.85,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 280,
    reactant1 = 
"""
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3CHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U1 L0 E0  {1,S} {3,S} {7,S}
3 N U0 L1 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (1400000000.0, 'cm^3/(mol*s)'),
            n = 1.463,
            Ea = (1355, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (2e+39, 'cm^6/(mol^2*s)'),
            n = -6.642,
            Ea = (5769, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = -0.569,
        T3 = (299, 'K'),
        T1 = (9147, 'K'),
        T2 = (152.4, 'K'),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 281,
    reactant1 = 
"""
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (39000000000000.0, 'cm^3/(mol*s)'),
            n = 0.2,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(2.1e+24, 'cm^6/(mol^2*s)'), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 282,
    reactant1 = 
"""
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
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
CH2CHNH2_(T)
multiplicity 3
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,S} {6,S}
3 N U0 L1 E0  {1,S} {7,S} {8,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (39000000000000.0, 'cm^3/(mol*s)'),
            n = 0.2,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(A=(2.1e+24, 'cm^6/(mol^2*s)'), n=-1.3, Ea=(0, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.5,
        T3 = (1e-30, 'K'),
        T1 = (1e+30, 'K'),
        T2 = (1e+30, 'K'),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 283,
    reactant1 = 
"""
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CHCHNH2
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 N U0 L1 E0  {1,S} {5,S} {6,S}
3 C U1 L0 E0  {1,D} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (17000000000.0, 'cm^3/(mol*s)'),
            n = 1.266,
            Ea = (2709, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.3e+31, 'cm^6/(mol^2*s)'),
            n = -4.664,
            Ea = (3780, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7878,
        T3 = (-10212, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'O=C=O': 3.0, 'O': 5.0},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 284,
    reactant1 = 
"""
CHCNH2_(T)
multiplicity 3
1 N U0 L1 E0  {2,S} {4,S} {5,S}
2 C U1 L0 E0  {1,S} {3,D}
3 C U1 L0 E0  {2,D} {6,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH2CNH2
multiplicity 2
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 N U0 L1 E0  {3,S} {6,S} {7,S}
3 C U1 L0 E0  {1,D} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (17000000000.0, 'cm^3/(mol*s)'),
            n = 1.266,
            Ea = (2709, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (6.3e+31, 'cm^6/(mol^2*s)'),
            n = -4.664,
            Ea = (3780, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        alpha = 0.7878,
        T3 = (-10212, 'K'),
        T1 = (1e+30, 'K'),
        efficiencies = {'[H][H]': 2.0, '[C]=O': 2.0, 'O=C=O': 3.0, 'O': 5.0},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 285,
    reactant1 = 
"""
CH2CHN_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
""",
    product1 = 
"""
CH2CHN_(T)
multiplicity 3
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 N U2 L1 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (10000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (0, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'[H]': 0.0},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 286,
    reactant1 = 
"""
H2NCHO
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U0 L0 E0  {1,S} {5,S} {6,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {2,S}
6 O U0 L2 E0  {2,D}
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
NH3
multiplicity 1
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(
            A = (100000000000000.0, 's^-1'),
            n = 0,
            Ea = (75514, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        arrheniusLow = Arrhenius(
            A = (830000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (49084, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 287,
    reactant1 = 
"""
H2NCO
multiplicity 2
1 N U0 L1 E0  {2,S} {3,S} {4,S}
2 C U1 L0 E0  {1,S} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 O U0 L2 E0  {2,D}
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
NH2
multiplicity 2
1 N U1 L1 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(5900000000000.0, 's^-1'), n=0, Ea=(25000, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(
            A = (100000000000000.0, 'cm^3/(mol*s)'),
            n = 0,
            Ea = (21700, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index        = 288,
    reactant1 = 
"""
CH3NHCH2
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 N U0 L1 E0  {1,S} {3,S} {7,S}
3 C U1 L0 E0  {2,S} {8,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    reactant2 = 
"""
H
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CH3NHCH3
multiplicity 1
1  C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {3,S} {7,S} {8,S} {9,S}
3  N U0 L1 E0  {1,S} {2,S} {10,S}
4  H U0 L0 E0  {1,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(
            A = (5.2e+17, 'cm^3/(mol*s)'),
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
        alpha = 0.8422,
        T3 = (125, 'K'),
        T1 = (2219, 'K'),
        T2 = (6882, 'K'),
        efficiencies = {},
        comment = 'Reaction and kinetics from Nitrogen_Glarborg_Lucassen_et_al.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

