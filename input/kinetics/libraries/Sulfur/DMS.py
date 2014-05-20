#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DMS"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    reactant1 = 
"""
CS2H2(2)
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HJ
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
CS2H(2)J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
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
        A = (17400, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (5.87, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H2(2)
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CS2H(2)J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
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
        A = (0.000155, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.73, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H2(2)
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HSJ
multiplicity 2
1 S U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CS2H(2)J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2S
multiplicity 1
1 S U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (156, 'cm^3/(mol*s)'),
        n = 3.53,
        Ea = (8.32, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H2(2)
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3SJ
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CS2H(2)J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH3SH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (22.9, 'cm^3/(mol*s)'),
        n = 3.69,
        Ea = (11.61, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH3SSCH2J
multiplicity 2
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U1 L0 E0  {4,S} {8,S} {9,S}
3 S U0 L2 E0  {1,S} {4,S}
4 S U0 L2 E0  {2,S} {3,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3SCH2SJ
multiplicity 2
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U0 L0 E0  {3,S} {4,S} {8,S} {9,S}
3 S U0 L2 E0  {1,S} {2,S}
4 S U1 L2 E0  {2,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (313000000000.0, 's^-1'),
        n = 0.22,
        Ea = (31.93, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH2S
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3SJ
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3SSCH2J
multiplicity 2
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U1 L0 E0  {4,S} {8,S} {9,S}
3 S U0 L2 E0  {1,S} {4,S}
4 S U0 L2 E0  {2,S} {3,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25500, 'cm^3/(mol*s)'),
        n = 2.77,
        Ea = (-2.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH2S
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3SJ
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3SCH2SJ
multiplicity 2
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U0 L0 E0  {3,S} {4,S} {8,S} {9,S}
3 S U0 L2 E0  {1,S} {2,S}
4 S U1 L2 E0  {2,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.79,
        Ea = (-2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH3CH2SSCH2J
multiplicity 2
1  C U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2  C U0 L0 E0  {1,S} {8,S} {9,S} {10,S}
3  C U1 L0 E0  {5,S} {11,S} {12,S}
4  S U0 L2 E0  {1,S} {5,S}
5  S U0 L2 E0  {3,S} {4,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {2,S}
11 H U0 L0 E0  {3,S}
12 H U0 L0 E0  {3,S}
""",
    product1 = 
"""
CH3CH2SCH2SJ
multiplicity 2
1  C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {1,S} {7,S} {8,S} {9,S}
3  C U0 L0 E0  {4,S} {10,S} {11,S} {12,S}
4  S U0 L2 E0  {1,S} {3,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 S U1 L2 E0  {3,S}
11 H U0 L0 E0  {3,S}
12 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (313000000000.0, 's^-1'),
        n = 0.22,
        Ea = (31.93, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH2S
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3CH2SJ
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 S U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3CH2SSCH2J
multiplicity 2
1  C U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2  C U0 L0 E0  {1,S} {8,S} {9,S} {10,S}
3  C U1 L0 E0  {5,S} {11,S} {12,S}
4  S U0 L2 E0  {1,S} {5,S}
5  S U0 L2 E0  {3,S} {4,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {2,S}
11 H U0 L0 E0  {3,S}
12 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25500, 'cm^3/(mol*s)'),
        n = 2.77,
        Ea = (-2.31, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH2S
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3CH2SJ
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 S U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
CH3CH2SCH2SJ
multiplicity 2
1  C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {1,S} {7,S} {8,S} {9,S}
3  C U0 L0 E0  {4,S} {10,S} {11,S} {12,S}
4  S U0 L2 E0  {1,S} {3,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 S U1 L2 E0  {3,S}
11 H U0 L0 E0  {3,S}
12 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.79,
        Ea = (-2.27, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H2(2)
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3SSCH2J
multiplicity 2
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U1 L0 E0  {4,S} {8,S} {9,S}
3 S U0 L2 E0  {1,S} {4,S}
4 S U0 L2 E0  {2,S} {3,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3120, 'cm^3/(mol*s)'),
        n = 2.72,
        Ea = (7.28, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H2(2)
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CH3SCH2SJ
multiplicity 2
1 C U0 L0 E0  {3,S} {5,S} {6,S} {7,S}
2 C U0 L0 E0  {3,S} {4,S} {8,S} {9,S}
3 S U0 L2 E0  {1,S} {2,S}
4 S U1 L2 E0  {2,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {1,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6180, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (-1.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H2(2)
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
C2H5J
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
CH3CH2SSCH2J
multiplicity 2
1  C U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2  C U0 L0 E0  {1,S} {8,S} {9,S} {10,S}
3  C U1 L0 E0  {5,S} {11,S} {12,S}
4  S U0 L2 E0  {1,S} {5,S}
5  S U0 L2 E0  {3,S} {4,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {1,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 H U0 L0 E0  {2,S}
11 H U0 L0 E0  {3,S}
12 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3120, 'cm^3/(mol*s)'),
        n = 2.72,
        Ea = (7.28, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H2(2)
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
C2H5J
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
CH3CH2SCH2SJ
multiplicity 2
1  C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2  C U0 L0 E0  {1,S} {7,S} {8,S} {9,S}
3  C U0 L0 E0  {4,S} {10,S} {11,S} {12,S}
4  S U0 L2 E0  {1,S} {3,S}
5  H U0 L0 E0  {1,S}
6  H U0 L0 E0  {1,S}
7  H U0 L0 E0  {2,S}
8  H U0 L0 E0  {2,S}
9  H U0 L0 E0  {2,S}
10 S U1 L2 E0  {3,S}
11 H U0 L0 E0  {3,S}
12 H U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6180, 'cm^3/(mol*s)'),
        n = 2.57,
        Ea = (-1.16, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H2JJ_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U1 L2 E0  {1,S}
3 S U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CS2H2(2)
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20800000000.0, 's^-1'),
        n = 1,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H(2)J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 S U0 L2 E0  {1,S} {3,S}
3 S U0 L2 E0  {1,S} {2,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CS2H(1)J
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 S U1 L2 E0  {1,S}
3 S U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (20800000000.0, 's^-1'),
        n = 1,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H2JJ_(T)
multiplicity 3
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U1 L2 E0  {1,S}
3 S U1 L2 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HJ
multiplicity 2
1 H U1 L0 E0 
""",
    product2 = 
"""
CS2H(1)J
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 S U1 L2 E0  {1,S}
3 S U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3190000000.0, 's^-1'),
        n = 1.55,
        Ea = (36.55, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CS2H(1)J
multiplicity 2
1 C U0 L0 E0  {2,S} {3,D} {4,S}
2 S U1 L2 E0  {1,S}
3 S U0 L2 E0  {1,D}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
CS2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 S U0 L2 E0  {1,D}
3 S U0 L2 E0  {1,D}
""",
    product2 = 
"""
HJ
multiplicity 2
1 H U1 L0 E0 
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (252000000.0, 's^-1'),
        n = 1.74,
        Ea = (30.56, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH2S
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HJ
multiplicity 2
1 H U1 L0 E0 
""",
    product1 = 
"""
HCSJ
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 S U0 L2 E0  {1,D}
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
        A = (95000, 'cm^3/(mol*s)'),
        n = 2.72,
        Ea = (3.68, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH2S
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCSJ
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 S U0 L2 E0  {1,D}
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
        A = (0.0033, 'cm^3/(mol*s)'),
        n = 4.85,
        Ea = (3.8, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH2S
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
HSJ
multiplicity 2
1 S U1 L2 E0  {2,S}
2 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCSJ
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
H2S
multiplicity 1
1 S U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (127, 'cm^3/(mol*s)'),
        n = 3.7,
        Ea = (1.93, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
CH2S
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    reactant2 = 
"""
CH3SJ
multiplicity 2
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U1 L2 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
""",
    product1 = 
"""
HCSJ
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH3SH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 S U0 L2 E0  {1,S} {6,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.49, 'cm^3/(mol*s)'),
        n = 3.96,
        Ea = (5.36, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
C2H3S2(1)J
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 S U0 L2 E0  {1,S} {2,S}
4 S U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
HCSJ
multiplicity 2
1 C U1 L0 E0  {2,D} {3,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
""",
    product2 = 
"""
CH2S
multiplicity 1
1 C U0 L0 E0  {2,D} {3,S} {4,S}
2 S U0 L2 E0  {1,D}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (852000000000000.0, 's^-1'),
        n = -0.05,
        Ea = (36.87, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
C2H3S2(1)J
multiplicity 2
1 C U1 L0 E0  {3,S} {5,S} {6,S}
2 C U0 L0 E0  {3,S} {4,D} {7,S}
3 S U0 L2 E0  {1,S} {2,S}
4 S U0 L2 E0  {2,D}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 H U0 L0 E0  {2,S}
""",
    product1 = 
"""
C2H3S2(2)J
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 S U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 S U0 L2 E0  {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e-21, 's^-1'),
        n = 9.96,
        Ea = (19.14, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
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
C2H3S2(2)J
multiplicity 2
1 C U0 L0 E0  {2,S} {4,S} {5,S} {6,S}
2 S U0 L2 E0  {1,S} {3,S}
3 C U1 L0 E0  {2,S} {7,D}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {1,S}
7 S U0 L2 E0  {3,D}
""",
    product1 = 
"""
CS2
multiplicity 1
1 C U0 L0 E0  {2,D} {3,D}
2 S U0 L2 E0  {1,D}
3 S U0 L2 E0  {1,D}
""",
    product2 = 
"""
CH3J
multiplicity 2
1 C U1 L0 E0  {2,S} {3,S} {4,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
4 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2220000000000.0, 's^-1'),
        n = 0.67,
        Ea = (10.64, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\DMS.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

