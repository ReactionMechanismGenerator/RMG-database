#!/usr/bin/env python
# encoding: utf-8

name = "Methylformate"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    reactant1 = 
"""
Mfmt
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
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
CH3OH
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 C U0 L0 E0  {1,S} {4,S} {5,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {2,S}
5 H U0 L0 E0  {2,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2128000000000.0, 's^-1'),
        n = 0.735,
        Ea = (68.628, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Mfmt
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
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
        A = (2158000000.0, 's^-1'),
        n = 1.28,
        Ea = (75.979, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Mfmt
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
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
        A = (453600000000.0, 's^-1'),
        n = 0.832,
        Ea = (83.612, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Mofml
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
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
CH3j
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2300000000.0, 's^-1'),
        n = 1.09,
        Ea = (14.9, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CO
multiplicity 1
1 C U0 L1 E-1 {2,T}
2 O U0 L1 E+1 {1,T}
""",
    reactant2 = 
"""
CH3Oj
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
Mofml
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1970000000.0, 'cm^3/(mol*s)'),
        n = 1.27,
        Ea = (5.81, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
HCjO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
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
Fmoml
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5030, 'cm^3/(mol*s)'),
        n = 2.48,
        Ea = (9.32, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Hj
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
Mfmt
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
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
Mofml
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (228000, 'cm^3/(mol*s)'),
        n = 2.5,
        Ea = (6.56, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
Hj
multiplicity 2
1 H U1 L0 E0 
""",
    reactant2 = 
"""
Mfmt
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
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
Fmoml
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (116000, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (7.62, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CH3j
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
Mfmt
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
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
Mofml
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 O U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.34, 'cm^3/(mol*s)'),
        n = 2.82,
        Ea = (6.81, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CH3j
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
Mfmt
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
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
Fmoml
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 O U0 L2 E0  {1,S} {2,S}
4 O U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.257, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (8.02, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CH3Oj
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 O U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HCjO
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 O U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
Mfmt
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
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
CH3j
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
OjCHO
multiplicity 2
1 O U1 L2 E0  {2,S}
2 C U0 L0 E0  {1,S} {3,D} {4,S}
3 O U0 L2 E0  {2,D}
4 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
Mfmt
multiplicity 1
1 C U0 L0 E0  {3,S} {4,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {7,D} {8,S}
3 O U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 O U0 L2 E0  {2,D}
8 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (18000000000000.0, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Methylformate.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

