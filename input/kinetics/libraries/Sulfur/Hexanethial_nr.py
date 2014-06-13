#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/Hexanethial_nr"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    reactant1 = 
"""
C6H12SHOH
1  C 0 0 {2,S} {9,S} {10,S} {11,S}
2  C 0 0 {1,S} {3,S} {12,S} {13,S}
3  C 0 0 {2,S} {4,S} {14,S} {15,S}
4  C 0 0 {3,S} {5,S} {16,S} {17,S}
5  C 0 0 {4,S} {6,S} {18,S} {19,S}
6  C 0 0 {5,S} {7,S} {8,S} {20,S}
7  S 0 2 {6,S} {21,S}
8  O 0 2 {6,S} {22,S}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {1,S}
12 H 0 0 {2,S}
13 H 0 0 {2,S}
14 H 0 0 {3,S}
15 H 0 0 {3,S}
16 H 0 0 {4,S}
17 H 0 0 {4,S}
18 H 0 0 {5,S}
19 H 0 0 {5,S}
20 H 0 0 {6,S}
21 H 0 0 {7,S}
22 H 0 0 {8,S}
""",
    product1 = 
"""
C6H12O
1  C 0 0 {2,S} {3,S} {9,S} {10,S}
2  C 0 0 {1,S} {4,S} {11,S} {12,S}
3  C 0 0 {1,S} {5,S} {7,S} {8,S}
4  C 0 0 {2,S} {6,S} {13,S} {14,S}
5  C 0 0 {3,S} {15,S} {16,S} {17,S}
6  C 0 0 {4,S} {18,D} {19,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {2,S}
12 H 0 0 {2,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
16 H 0 0 {5,S}
17 H 0 0 {5,S}
18 O 0 2 {6,D}
19 H 0 0 {6,S}
""",
    product2 = 
"""
H2S
1 S 0 2 {2,S} {3,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (343000000000000.0, 's^-1'),
        n = -0.41,
        Ea = (44.42, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Hexanethial_nr.\nFirst one should be 36.30 kcal/mol, second 44.42 kcal/mol\nC6H12O + H2S = C6H12SHOH    6.13E+01    2.77    36.30    0.0    0.0    0.0',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
First one should be 36.30 kcal/mol, second 44.42 kcal/mol
C6H12O + H2S = C6H12SHOH    6.13E+01    2.77    36.30    0.0    0.0    0.0
""",
)

entry(
    index = 2,
    reactant1 = 
"""
C5H11COHS
1  C 0 0 {2,S} {9,S} {10,S} {11,S}
2  C 0 0 {1,S} {3,S} {12,S} {13,S}
3  C 0 0 {2,S} {4,S} {14,S} {15,S}
4  C 0 0 {3,S} {5,S} {16,S} {17,S}
5  C 0 0 {4,S} {6,S} {18,S} {19,S}
6  C 0 0 {5,S} {7,D} {8,S}
7  S 0 2 {6,D}
8  O 0 2 {6,S} {20,S}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {1,S}
12 H 0 0 {2,S}
13 H 0 0 {2,S}
14 H 0 0 {3,S}
15 H 0 0 {3,S}
16 H 0 0 {4,S}
17 H 0 0 {4,S}
18 H 0 0 {5,S}
19 H 0 0 {5,S}
20 H 0 0 {8,S}
""",
    product1 = 
"""
C5H11COSH
1  C 0 0 {2,S} {9,S} {10,S} {11,S}
2  C 0 0 {1,S} {3,S} {12,S} {13,S}
3  C 0 0 {2,S} {4,S} {14,S} {15,S}
4  C 0 0 {3,S} {5,S} {16,S} {17,S}
5  C 0 0 {4,S} {6,S} {18,S} {19,S}
6  C 0 0 {5,S} {7,S} {8,D}
7  S 0 2 {6,S} {20,S}
8  O 0 2 {6,D}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {1,S}
12 H 0 0 {2,S}
13 H 0 0 {2,S}
14 H 0 0 {3,S}
15 H 0 0 {3,S}
16 H 0 0 {4,S}
17 H 0 0 {4,S}
18 H 0 0 {5,S}
19 H 0 0 {5,S}
20 H 0 0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5100000000000.0, 's^-1'),
        n = 0.13,
        Ea = (28.48, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Hexanethial_nr.\nCorrect value of next reaction is in R_Addition_MultipleBond\nC5H11COHS + HJ = C5H11CJOHSH    1.18E+09    1.15    -0.06    0.0    0.0    0.0',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Correct value of next reaction is in R_Addition_MultipleBond
C5H11COHS + HJ = C5H11CJOHSH    1.18E+09    1.15    -0.06    0.0    0.0    0.0
""",
)

entry(
    index = 3,
    reactant1 = 
"""
C5H11J
1  C 0 0 {2,S} {3,S} {8,S} {9,S}
2  C 0 0 {1,S} {4,S} {6,S} {7,S}
3  C 0 0 {1,S} {5,S} {10,S} {11,S}
4  C 0 0 {2,S} {12,S} {13,S} {14,S}
5  C 1 0 {3,S} {15,S} {16,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
16 H 0 0 {5,S}
""",
    reactant2 = 
"""
COS
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 S 0 2 {1,D}
""",
    product1 = 
"""
C5H11COSJ
1  C 0 0 {2,S} {9,S} {10,S} {11,S}
2  C 0 0 {1,S} {3,S} {12,S} {13,S}
3  C 0 0 {2,S} {4,S} {14,S} {15,S}
4  C 0 0 {3,S} {5,S} {16,S} {17,S}
5  C 0 0 {4,S} {6,S} {18,S} {19,S}
6  C 0 0 {5,S} {7,S} {8,D}
7  S 1 2 {6,S}
8  O 0 2 {6,D}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {1,S}
12 H 0 0 {2,S}
13 H 0 0 {2,S}
14 H 0 0 {3,S}
15 H 0 0 {3,S}
16 H 0 0 {4,S}
17 H 0 0 {4,S}
18 H 0 0 {5,S}
19 H 0 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (603000, 'cm^3/(mol*s)'),
        n = 1.83,
        Ea = (11.84, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Hexanethial_nr.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    reactant1 = 
"""
CHOHS
1 C 0 0 {2,S} {3,D} {4,S}
2 O 0 2 {1,S} {5,S}
3 S 0 2 {1,D}
4 H 0 0 {1,S}
5 H 0 0 {2,S}
""",
    reactant2 = 
"""
C5H11J
1  C 0 0 {2,S} {3,S} {8,S} {9,S}
2  C 0 0 {1,S} {4,S} {6,S} {7,S}
3  C 0 0 {1,S} {5,S} {10,S} {11,S}
4  C 0 0 {2,S} {12,S} {13,S} {14,S}
5  C 1 0 {3,S} {15,S} {16,S}
6  H 0 0 {2,S}
7  H 0 0 {2,S}
8  H 0 0 {1,S}
9  H 0 0 {1,S}
10 H 0 0 {3,S}
11 H 0 0 {3,S}
12 H 0 0 {4,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
16 H 0 0 {5,S}
""",
    product1 = 
"""
C6H12OHSJ
1  C 0 0 {2,S} {4,S} {10,S} {11,S}
2  C 0 0 {1,S} {3,S} {12,S} {13,S}
3  C 0 0 {2,S} {5,S} {14,S} {15,S}
4  C 0 0 {1,S} {6,S} {8,S} {9,S}
5  C 0 0 {3,S} {7,S} {16,S} {17,S}
6  C 0 0 {4,S} {18,S} {19,S} {20,S}
7  O 0 2 {5,S} {21,S}
8  H 0 0 {4,S}
9  H 0 0 {4,S}
10 H 0 0 {1,S}
11 H 0 0 {1,S}
12 H 0 0 {2,S}
13 H 0 0 {2,S}
14 H 0 0 {3,S}
15 H 0 0 {3,S}
16 S 1 2 {5,S}
17 H 0 0 {5,S}
18 H 0 0 {6,S}
19 H 0 0 {6,S}
20 H 0 0 {6,S}
21 H 0 0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (774, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (3.56, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Hexanethial_nr.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    reactant1 = 
"""
C4H9CHJCHOHSH
1  C 0 0 {2,S} {3,S} {11,S} {12,S}
2  C 0 0 {1,S} {5,S} {9,S} {10,S}
3  C 0 0 {1,S} {6,S} {13,S} {14,S}
4  C 0 0 {6,S} {7,S} {8,S} {15,S}
5  C 0 0 {2,S} {16,S} {17,S} {18,S}
6  C 1 0 {3,S} {4,S} {19,S}
7  S 0 2 {4,S} {20,S}
8  O 0 2 {4,S} {21,S}
9  H 0 0 {2,S}
10 H 0 0 {2,S}
11 H 0 0 {1,S}
12 H 0 0 {1,S}
13 H 0 0 {3,S}
14 H 0 0 {3,S}
15 H 0 0 {4,S}
16 H 0 0 {5,S}
17 H 0 0 {5,S}
18 H 0 0 {5,S}
19 H 0 0 {6,S}
20 H 0 0 {7,S}
21 H 0 0 {8,S}
""",
    product1 = 
"""
SH
1 S 1 2 {2,S}
2 H 0 0 {1,S}
""",
    product2 = 
"""
hexen-1-ol
1  C 0 0 {2,S} {3,S} {10,S} {11,S}
2  C 0 0 {1,S} {4,S} {8,S} {9,S}
3  C 0 0 {1,S} {5,S} {12,S} {13,S}
4  C 0 0 {2,S} {14,S} {15,S} {16,S}
5  C 0 0 {3,S} {6,D} {17,S}
6  C 0 0 {5,D} {7,S} {18,S}
7  O 0 2 {6,S} {19,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {1,S}
11 H 0 0 {1,S}
12 H 0 0 {3,S}
13 H 0 0 {3,S}
14 H 0 0 {4,S}
15 H 0 0 {4,S}
16 H 0 0 {4,S}
17 H 0 0 {5,S}
18 H 0 0 {6,S}
19 H 0 0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2010000000000.0, 's^-1'),
        n = 0.13,
        Ea = (4.99, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Hexanethial_nr.\nreverse of next reaction is in R_Addition_MultipleBond library:',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
reverse of next reaction is in R_Addition_MultipleBond library:
""",
)

entry(
    index = 6,
    reactant1 = 
"""
hexen-1-ol
1  C 0 0 {2,S} {3,S} {10,S} {11,S}
2  C 0 0 {1,S} {4,S} {8,S} {9,S}
3  C 0 0 {1,S} {5,S} {12,S} {13,S}
4  C 0 0 {2,S} {14,S} {15,S} {16,S}
5  C 0 0 {3,S} {6,D} {17,S}
6  C 0 0 {5,D} {7,S} {18,S}
7  O 0 2 {6,S} {19,S}
8  H 0 0 {2,S}
9  H 0 0 {2,S}
10 H 0 0 {1,S}
11 H 0 0 {1,S}
12 H 0 0 {3,S}
13 H 0 0 {3,S}
14 H 0 0 {4,S}
15 H 0 0 {4,S}
16 H 0 0 {4,S}
17 H 0 0 {5,S}
18 H 0 0 {6,S}
19 H 0 0 {7,S}
""",
    product1 = 
"""
C6H12O
1  C 0 0 {2,S} {3,S} {9,S} {10,S}
2  C 0 0 {1,S} {4,S} {11,S} {12,S}
3  C 0 0 {1,S} {5,S} {7,S} {8,S}
4  C 0 0 {2,S} {6,S} {13,S} {14,S}
5  C 0 0 {3,S} {15,S} {16,S} {17,S}
6  C 0 0 {4,S} {18,D} {19,S}
7  H 0 0 {3,S}
8  H 0 0 {3,S}
9  H 0 0 {1,S}
10 H 0 0 {1,S}
11 H 0 0 {2,S}
12 H 0 0 {2,S}
13 H 0 0 {4,S}
14 H 0 0 {4,S}
15 H 0 0 {5,S}
16 H 0 0 {5,S}
17 H 0 0 {5,S}
18 O 0 2 {6,D}
19 H 0 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.32e-33, 's^-1'),
        n = 12.94,
        Ea = (31.33, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Hexanethial_nr.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    reactant1 = 
"""
CO
1 C 0 1 {2,T}
2 O 0 1 {1,T}
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
CO2
1 C 0 0 {2,D} {3,D}
2 O 0 2 {1,D}
3 O 0 2 {1,D}
""",
    product2 = 
"""
H2
1 H 0 0 {2,S}
2 H 0 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5000, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from Sulfur\\Hexanethial_nr.\nApprox water gas shift reaction',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Approx water gas shift reaction
""",
)

