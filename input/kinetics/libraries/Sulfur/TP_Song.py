#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/TP_Song"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    reactant1 = 
"""
thiophene
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {6,S}
2 C U0 L0 E0  {1,S} {4,D} {7,S}
3 C U0 L0 E0  {1,D} {5,S} {8,S}
4 C U0 L0 E0  {2,D} {5,S} {9,S}
5 S U0 L2 E0  {3,S} {4,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {4,S}
""",
    product1 = 
"""
IM1_(S)
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2 C U0 L0 E0  {1,S} {3,D} {8,S}
3 C U0 L0 E0  {2,D} {5,S} {9,S}
4 C U2 L0 E0  {1,S} {5,S}
5 S U0 L2 E0  {3,S} {4,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (920000, 's^-1'),
        n = 0.52,
        Ea = (67.07, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.',
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
thiophene
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {6,S}
2 C U0 L0 E0  {1,S} {4,D} {7,S}
3 C U0 L0 E0  {1,D} {5,S} {8,S}
4 C U0 L0 E0  {2,D} {5,S} {9,S}
5 S U0 L2 E0  {3,S} {4,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {4,S}
""",
    product1 = 
"""
IM2
multiplicity 1
1 C U0 L0 E0  {2,S} {4,D} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 C U0 L0 E0  {4,D} {8,S} {9,S}
4 C U0 L0 E0  {1,D} {3,D}
5 H U0 L0 E0  {1,S}
6 S U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (367000, 's^-1'),
        n = 0.55,
        Ea = (74.79, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.',
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
thiophene
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {6,S}
2 C U0 L0 E0  {1,S} {4,D} {7,S}
3 C U0 L0 E0  {1,D} {5,S} {8,S}
4 C U0 L0 E0  {2,D} {5,S} {9,S}
5 S U0 L2 E0  {3,S} {4,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {4,S}
""",
    product1 = 
"""
IM4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {5,S} {6,S}
2 C U0 L0 E0  {1,S} {7,D} {8,S}
3 C U0 L0 E0  {1,S} {4,T}
4 C U0 L0 E0  {3,T} {9,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 S U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (184000, 's^-1'),
        n = 0.65,
        Ea = (86.88, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.\nthiophene = IM3        2.35E05    0.75    86.11    0.0    0.0    0.0',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
thiophene = IM3        2.35E05    0.75    86.11    0.0    0.0    0.0
""",
)

entry(
    index        = 4,
    reactant1 = 
"""
IM1_(S)
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2 C U0 L0 E0  {1,S} {3,D} {8,S}
3 C U0 L0 E0  {2,D} {5,S} {9,S}
4 C U2 L0 E0  {1,S} {5,S}
5 S U0 L2 E0  {3,S} {4,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
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
H2CCS
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 S U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (210000000000.0, 's^-1'),
        n = 0.99,
        Ea = (41.95, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.',
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
IM1_(S)
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2 C U0 L0 E0  {1,S} {3,D} {8,S}
3 C U0 L0 E0  {2,D} {5,S} {9,S}
4 C U2 L0 E0  {1,S} {5,S}
5 S U0 L2 E0  {3,S} {4,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
IM5_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {6,S} {7,S}
2 C U1 L0 E0  {1,S} {4,S} {8,S}
3 C U0 L0 E0  {1,S} {5,D} {9,S}
4 S U0 L2 E0  {2,S} {5,S}
5 C U1 L0 E0  {3,D} {4,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (345000000000.0, 's^-1'),
        n = 0.34,
        Ea = (27.75, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.',
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
IM5_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {6,S} {7,S}
2 C U1 L0 E0  {1,S} {4,S} {8,S}
3 C U0 L0 E0  {1,S} {5,D} {9,S}
4 S U0 L2 E0  {2,S} {5,S}
5 C U1 L0 E0  {3,D} {4,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
IM4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {5,S} {6,S}
2 C U0 L0 E0  {1,S} {7,D} {8,S}
3 C U0 L0 E0  {1,S} {4,T}
4 C U0 L0 E0  {3,T} {9,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 S U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31300000000000.0, 's^-1'),
        n = 0.86,
        Ea = (22.3, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.',
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
IM2
multiplicity 1
1 C U0 L0 E0  {2,S} {4,D} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 C U0 L0 E0  {4,D} {8,S} {9,S}
4 C U0 L0 E0  {1,D} {3,D}
5 H U0 L0 E0  {1,S}
6 S U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
IM6_(S)
multiplicity 1
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U0 L0 E0  {3,S} {4,D} {8,S}
3 C U2 L0 E0  {1,S} {2,S}
4 C U0 L0 E0  {2,D} {9,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 S U0 L2 E0  {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.73e+17, 's^-1'),
        n = 0.58,
        Ea = (61.23, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.\nIM2 = IM2a            3.15E12    -0.03    6.03    0.0    0.0    0.0',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
IM2 = IM2a            3.15E12    -0.03    6.03    0.0    0.0    0.0
""",
)

entry(
    index        = 8,
    reactant1 = 
"""
IM6_(S)
multiplicity 1
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U0 L0 E0  {3,S} {4,D} {8,S}
3 C U2 L0 E0  {1,S} {2,S}
4 C U0 L0 E0  {2,D} {9,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 S U0 L2 E0  {4,D}
""",
    product1 = 
"""
CS_(S)
multiplicity 1
1 C U2 L0 E0  {2,D}
2 S U0 L2 E0  {1,D}
""",
    product2 = 
"""
propyne
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {1,S} {3,T}
3 C U0 L0 E0  {2,T} {7,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7220000000000.0, 's^-1'),
        n = 0.37,
        Ea = (14.5, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.',
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
IM2
multiplicity 1
1 C U0 L0 E0  {2,S} {4,D} {5,S}
2 C U0 L0 E0  {1,S} {6,D} {7,S}
3 C U0 L0 E0  {4,D} {8,S} {9,S}
4 C U0 L0 E0  {1,D} {3,D}
5 H U0 L0 E0  {1,S}
6 S U0 L2 E0  {2,D}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {3,S}
9 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
IM7_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,D} {7,S} {8,S}
3 C U1 L0 E0  {1,S} {2,D}
4 C U1 L0 E0  {1,S} {9,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 S U0 L2 E0  {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (27900000000.0, 's^-1'),
        n = 0.64,
        Ea = (71.6, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.',
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
IM7_(T)
multiplicity 3
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,D} {7,S} {8,S}
3 C U1 L0 E0  {1,S} {2,D}
4 C U1 L0 E0  {1,S} {9,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 S U0 L2 E0  {4,D}
""",
    product1 = 
"""
CS_(S)
multiplicity 1
1 C U2 L0 E0  {2,D}
2 S U0 L2 E0  {1,D}
""",
    product2 = 
"""
propadiene
multiplicity 1
1 C U0 L0 E0  {3,D} {4,S} {5,S}
2 C U0 L0 E0  {3,D} {6,S} {7,S}
3 C U0 L0 E0  {1,D} {2,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32700000000000.0, 's^-1'),
        n = 0.22,
        Ea = (8.83, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.',
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
IM10_(S)
multiplicity 1
1 C U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2 C U0 L0 E0  {1,S} {3,D} {8,S}
3 C U0 L0 E0  {2,D} {5,S} {9,S}
4 S U0 L2 E0  {1,S} {5,S}
5 C U2 L0 E0  {3,S} {4,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
IM11
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {5,S}
2 C U0 L0 E0  {1,S} {4,D} {6,S}
3 C U0 L0 E0  {1,D} {7,S} {8,S}
4 C U0 L0 E0  {2,D} {9,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
9 S U0 L2 E0  {4,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2900000000000.0, 's^-1'),
        n = 0.29,
        Ea = (15.56, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.\nIM3 = IM8a            3.46E19    0.59    13.39    0.0    0.0    0.0\nIM8 = IM8a            2.34E12    -0.09    3.68    0.0    0.0    0.0\nIM8a = IM9            5.40E16    1.27    83.03    0.0    0.0    0.0\nBelow reaction not found with CBS-QB3, guessed (Ea from paper)\nIM9 = H2S + butadiyne    1.00E10    0.10    11.63    0.0    0.0    0.0\nIM3 = IM10            1.00E12    0.23    13.53    0.0    0.0    0.0',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
IM3 = IM8a            3.46E19    0.59    13.39    0.0    0.0    0.0
IM8 = IM8a            2.34E12    -0.09    3.68    0.0    0.0    0.0
IM8a = IM9            5.40E16    1.27    83.03    0.0    0.0    0.0
Below reaction not found with CBS-QB3, guessed (Ea from paper)
IM9 = H2S + butadiyne    1.00E10    0.10    11.63    0.0    0.0    0.0
IM3 = IM10            1.00E12    0.23    13.53    0.0    0.0    0.0
""",
)

entry(
    index        = 12,
    reactant1 = 
"""
IM11
multiplicity 1
1 C U0 L0 E0  {2,S} {3,D} {5,S}
2 C U0 L0 E0  {1,S} {4,D} {6,S}
3 C U0 L0 E0  {1,D} {7,S} {8,S}
4 C U0 L0 E0  {2,D} {9,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {3,S}
8 H U0 L0 E0  {3,S}
9 S U0 L2 E0  {4,D}
""",
    product1 = 
"""
C2H2jj_(S)
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U2 L0 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2CCS
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 C U0 L0 E0  {1,D} {5,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 S U0 L2 E0  {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (66300000000.0, 's^-1'),
        n = 0.98,
        Ea = (88.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.',
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
IM4
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {5,S} {6,S}
2 C U0 L0 E0  {1,S} {7,D} {8,S}
3 C U0 L0 E0  {1,S} {4,T}
4 C U0 L0 E0  {3,T} {9,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 S U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {4,S}
""",
    product1 = 
"""
IM8
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {7,S}
2 C U0 L0 E0  {1,D} {4,S} {6,S}
3 C U0 L0 E0  {1,S} {5,T}
4 S U0 L2 E0  {2,S} {8,S}
5 C U0 L0 E0  {3,T} {9,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {4,S}
9 H U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (258000000000.0, 's^-1'),
        n = 0.68,
        Ea = (45.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\TP_Song.\nIM4 = IM4a            1.24E12    0.02    2.07    0.0    0.0    0.0',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
IM4 = IM4a            1.24E12    0.02    2.07    0.0    0.0    0.0
""",
)

