#!/usr/bin/env python
# encoding: utf-8

name = "TEOS"
shortDesc = u""
longDesc = u"""

"""
entry(
    index        = 1,
    reactant1 = 
"""
Si(OC2H5)4
multiplicity 1
1  Si U0 L0 E0  {10,S} {11,S} {12,S} {13,S}
2  C  U0 L0 E0  {6,S} {10,S} {14,S} {15,S}
3  C  U0 L0 E0  {7,S} {11,S} {16,S} {17,S}
4  C  U0 L0 E0  {8,S} {12,S} {18,S} {19,S}
5  C  U0 L0 E0  {9,S} {13,S} {20,S} {21,S}
6  C  U0 L0 E0  {2,S} {22,S} {23,S} {24,S}
7  C  U0 L0 E0  {3,S} {25,S} {26,S} {27,S}
8  C  U0 L0 E0  {4,S} {28,S} {29,S} {30,S}
9  C  U0 L0 E0  {5,S} {31,S} {32,S} {33,S}
10 O  U0 L2 E0  {1,S} {2,S}
11 O  U0 L2 E0  {1,S} {3,S}
12 O  U0 L2 E0  {1,S} {4,S}
13 O  U0 L2 E0  {1,S} {5,S}
14 H  U0 L0 E0  {2,S}
15 H  U0 L0 E0  {2,S}
16 H  U0 L0 E0  {3,S}
17 H  U0 L0 E0  {3,S}
18 H  U0 L0 E0  {4,S}
19 H  U0 L0 E0  {4,S}
20 H  U0 L0 E0  {5,S}
21 H  U0 L0 E0  {5,S}
22 H  U0 L0 E0  {6,S}
23 H  U0 L0 E0  {6,S}
24 H  U0 L0 E0  {6,S}
25 H  U0 L0 E0  {7,S}
26 H  U0 L0 E0  {7,S}
27 H  U0 L0 E0  {7,S}
28 H  U0 L0 E0  {8,S}
29 H  U0 L0 E0  {8,S}
30 H  U0 L0 E0  {8,S}
31 H  U0 L0 E0  {9,S}
32 H  U0 L0 E0  {9,S}
33 H  U0 L0 E0  {9,S}
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
Si(OC2H5)3OH
multiplicity 1
1  Si U0 L0 E0  {8,S} {9,S} {10,S} {11,S}
2  C  U0 L0 E0  {5,S} {8,S} {12,S} {13,S}
3  C  U0 L0 E0  {6,S} {9,S} {14,S} {15,S}
4  C  U0 L0 E0  {7,S} {10,S} {16,S} {17,S}
5  C  U0 L0 E0  {2,S} {18,S} {19,S} {20,S}
6  C  U0 L0 E0  {3,S} {21,S} {22,S} {23,S}
7  C  U0 L0 E0  {4,S} {24,S} {25,S} {26,S}
8  O  U0 L2 E0  {1,S} {2,S}
9  O  U0 L2 E0  {1,S} {3,S}
10 O  U0 L2 E0  {1,S} {4,S}
11 O  U0 L2 E0  {1,S} {27,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {2,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {5,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {5,S}
21 H  U0 L0 E0  {6,S}
22 H  U0 L0 E0  {6,S}
23 H  U0 L0 E0  {6,S}
24 H  U0 L0 E0  {7,S}
25 H  U0 L0 E0  {7,S}
26 H  U0 L0 E0  {7,S}
27 H  U0 L0 E0  {11,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1995000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)4
multiplicity 1
1  Si U0 L0 E0  {10,S} {11,S} {12,S} {13,S}
2  C  U0 L0 E0  {6,S} {10,S} {14,S} {15,S}
3  C  U0 L0 E0  {7,S} {11,S} {16,S} {17,S}
4  C  U0 L0 E0  {8,S} {12,S} {18,S} {19,S}
5  C  U0 L0 E0  {9,S} {13,S} {20,S} {21,S}
6  C  U0 L0 E0  {2,S} {22,S} {23,S} {24,S}
7  C  U0 L0 E0  {3,S} {25,S} {26,S} {27,S}
8  C  U0 L0 E0  {4,S} {28,S} {29,S} {30,S}
9  C  U0 L0 E0  {5,S} {31,S} {32,S} {33,S}
10 O  U0 L2 E0  {1,S} {2,S}
11 O  U0 L2 E0  {1,S} {3,S}
12 O  U0 L2 E0  {1,S} {4,S}
13 O  U0 L2 E0  {1,S} {5,S}
14 H  U0 L0 E0  {2,S}
15 H  U0 L0 E0  {2,S}
16 H  U0 L0 E0  {3,S}
17 H  U0 L0 E0  {3,S}
18 H  U0 L0 E0  {4,S}
19 H  U0 L0 E0  {4,S}
20 H  U0 L0 E0  {5,S}
21 H  U0 L0 E0  {5,S}
22 H  U0 L0 E0  {6,S}
23 H  U0 L0 E0  {6,S}
24 H  U0 L0 E0  {6,S}
25 H  U0 L0 E0  {7,S}
26 H  U0 L0 E0  {7,S}
27 H  U0 L0 E0  {7,S}
28 H  U0 L0 E0  {8,S}
29 H  U0 L0 E0  {8,S}
30 H  U0 L0 E0  {8,S}
31 H  U0 L0 E0  {9,S}
32 H  U0 L0 E0  {9,S}
33 H  U0 L0 E0  {9,S}
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
CH2OSi(OC2H5)3
multiplicity 2
1  C  U0 L0 E0  {5,S} {13,S} {14,S} {15,S}
2  C  U0 L0 E0  {6,S} {16,S} {17,S} {18,S}
3  C  U0 L0 E0  {7,S} {19,S} {20,S} {21,S}
4  C  U1 L0 E0  {8,S} {22,S} {23,S}
5  C  U0 L0 E0  {1,S} {9,S} {24,S} {25,S}
6  C  U0 L0 E0  {2,S} {10,S} {26,S} {27,S}
7  C  U0 L0 E0  {3,S} {11,S} {28,S} {29,S}
8  O  U0 L2 E0  {4,S} {12,S}
9  O  U0 L2 E0  {5,S} {12,S}
10 O  U0 L2 E0  {6,S} {12,S}
11 O  U0 L2 E0  {7,S} {12,S}
12 Si U0 L0 E0  {8,S} {9,S} {10,S} {11,S}
13 H  U0 L0 E0  {1,S}
14 H  U0 L0 E0  {1,S}
15 H  U0 L0 E0  {1,S}
16 H  U0 L0 E0  {2,S}
17 H  U0 L0 E0  {2,S}
18 H  U0 L0 E0  {2,S}
19 H  U0 L0 E0  {3,S}
20 H  U0 L0 E0  {3,S}
21 H  U0 L0 E0  {3,S}
22 H  U0 L0 E0  {4,S}
23 H  U0 L0 E0  {4,S}
24 H  U0 L0 E0  {5,S}
25 H  U0 L0 E0  {5,S}
26 H  U0 L0 E0  {6,S}
27 H  U0 L0 E0  {6,S}
28 H  U0 L0 E0  {7,S}
29 H  U0 L0 E0  {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.981e+17, 's^-1'),
        n = 0,
        Ea = (86.037, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)3OH
multiplicity 1
1  Si U0 L0 E0  {8,S} {9,S} {10,S} {11,S}
2  C  U0 L0 E0  {5,S} {8,S} {12,S} {13,S}
3  C  U0 L0 E0  {6,S} {9,S} {14,S} {15,S}
4  C  U0 L0 E0  {7,S} {10,S} {16,S} {17,S}
5  C  U0 L0 E0  {2,S} {18,S} {19,S} {20,S}
6  C  U0 L0 E0  {3,S} {21,S} {22,S} {23,S}
7  C  U0 L0 E0  {4,S} {24,S} {25,S} {26,S}
8  O  U0 L2 E0  {1,S} {2,S}
9  O  U0 L2 E0  {1,S} {3,S}
10 O  U0 L2 E0  {1,S} {4,S}
11 O  U0 L2 E0  {1,S} {27,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {2,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {5,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {5,S}
21 H  U0 L0 E0  {6,S}
22 H  U0 L0 E0  {6,S}
23 H  U0 L0 E0  {6,S}
24 H  U0 L0 E0  {7,S}
25 H  U0 L0 E0  {7,S}
26 H  U0 L0 E0  {7,S}
27 H  U0 L0 E0  {11,S}
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
Si(OC2H5)2(OH)2
multiplicity 1
1  Si U0 L0 E0  {6,S} {7,S} {8,S} {9,S}
2  C  U0 L0 E0  {4,S} {6,S} {10,S} {11,S}
3  C  U0 L0 E0  {5,S} {7,S} {12,S} {13,S}
4  C  U0 L0 E0  {2,S} {14,S} {15,S} {16,S}
5  C  U0 L0 E0  {3,S} {17,S} {18,S} {19,S}
6  O  U0 L2 E0  {1,S} {2,S}
7  O  U0 L2 E0  {1,S} {3,S}
8  O  U0 L2 E0  {1,S} {20,S}
9  O  U0 L2 E0  {1,S} {21,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {4,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {5,S}
18 H  U0 L0 E0  {5,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {8,S}
21 H  U0 L0 E0  {9,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1585000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)3OH
multiplicity 1
1  Si U0 L0 E0  {8,S} {9,S} {10,S} {11,S}
2  C  U0 L0 E0  {5,S} {8,S} {12,S} {13,S}
3  C  U0 L0 E0  {6,S} {9,S} {14,S} {15,S}
4  C  U0 L0 E0  {7,S} {10,S} {16,S} {17,S}
5  C  U0 L0 E0  {2,S} {18,S} {19,S} {20,S}
6  C  U0 L0 E0  {3,S} {21,S} {22,S} {23,S}
7  C  U0 L0 E0  {4,S} {24,S} {25,S} {26,S}
8  O  U0 L2 E0  {1,S} {2,S}
9  O  U0 L2 E0  {1,S} {3,S}
10 O  U0 L2 E0  {1,S} {4,S}
11 O  U0 L2 E0  {1,S} {27,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {2,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {5,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {5,S}
21 H  U0 L0 E0  {6,S}
22 H  U0 L0 E0  {6,S}
23 H  U0 L0 E0  {6,S}
24 H  U0 L0 E0  {7,S}
25 H  U0 L0 E0  {7,S}
26 H  U0 L0 E0  {7,S}
27 H  U0 L0 E0  {11,S}
""",
    product1 = 
"""
C2H5OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
O_Si(OC2H5)2
multiplicity 1
1  C  U0 L0 E0  {3,S} {6,S} {8,S} {9,S}
2  C  U0 L0 E0  {4,S} {7,S} {10,S} {11,S}
3  C  U0 L0 E0  {1,S} {12,S} {13,S} {14,S}
4  C  U0 L0 E0  {2,S} {15,S} {16,S} {17,S}
5  Si U0 L0 E0  {6,S} {7,S} {18,D}
6  O  U0 L2 E0  {1,S} {5,S}
7  O  U0 L2 E0  {2,S} {5,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 O  U0 L2 E0  {5,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501200000000.0, 's^-1'),
        n = 0,
        Ea = (45.105, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)3OH
multiplicity 1
1  Si U0 L0 E0  {8,S} {9,S} {10,S} {11,S}
2  C  U0 L0 E0  {5,S} {8,S} {12,S} {13,S}
3  C  U0 L0 E0  {6,S} {9,S} {14,S} {15,S}
4  C  U0 L0 E0  {7,S} {10,S} {16,S} {17,S}
5  C  U0 L0 E0  {2,S} {18,S} {19,S} {20,S}
6  C  U0 L0 E0  {3,S} {21,S} {22,S} {23,S}
7  C  U0 L0 E0  {4,S} {24,S} {25,S} {26,S}
8  O  U0 L2 E0  {1,S} {2,S}
9  O  U0 L2 E0  {1,S} {3,S}
10 O  U0 L2 E0  {1,S} {4,S}
11 O  U0 L2 E0  {1,S} {27,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {2,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {5,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {5,S}
21 H  U0 L0 E0  {6,S}
22 H  U0 L0 E0  {6,S}
23 H  U0 L0 E0  {6,S}
24 H  U0 L0 E0  {7,S}
25 H  U0 L0 E0  {7,S}
26 H  U0 L0 E0  {7,S}
27 H  U0 L0 E0  {11,S}
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
CH2OSi(OC2H5)2OH
multiplicity 2
1  C  U0 L0 E0  {4,S} {11,S} {12,S} {13,S}
2  C  U0 L0 E0  {5,S} {14,S} {15,S} {16,S}
3  C  U1 L0 E0  {7,S} {17,S} {18,S}
4  C  U0 L0 E0  {1,S} {8,S} {19,S} {20,S}
5  C  U0 L0 E0  {2,S} {9,S} {21,S} {22,S}
6  O  U0 L2 E0  {10,S} {23,S}
7  O  U0 L2 E0  {3,S} {10,S}
8  O  U0 L2 E0  {4,S} {10,S}
9  O  U0 L2 E0  {5,S} {10,S}
10 Si U0 L0 E0  {6,S} {7,S} {8,S} {9,S}
11 H  U0 L0 E0  {1,S}
12 H  U0 L0 E0  {1,S}
13 H  U0 L0 E0  {1,S}
14 H  U0 L0 E0  {2,S}
15 H  U0 L0 E0  {2,S}
16 H  U0 L0 E0  {2,S}
17 H  U0 L0 E0  {3,S}
18 H  U0 L0 E0  {3,S}
19 H  U0 L0 E0  {4,S}
20 H  U0 L0 E0  {4,S}
21 H  U0 L0 E0  {5,S}
22 H  U0 L0 E0  {5,S}
23 H  U0 L0 E0  {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.162e+17, 's^-1'),
        n = 0,
        Ea = (86.037, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)2(OH)2
multiplicity 1
1  Si U0 L0 E0  {6,S} {7,S} {8,S} {9,S}
2  C  U0 L0 E0  {4,S} {6,S} {10,S} {11,S}
3  C  U0 L0 E0  {5,S} {7,S} {12,S} {13,S}
4  C  U0 L0 E0  {2,S} {14,S} {15,S} {16,S}
5  C  U0 L0 E0  {3,S} {17,S} {18,S} {19,S}
6  O  U0 L2 E0  {1,S} {2,S}
7  O  U0 L2 E0  {1,S} {3,S}
8  O  U0 L2 E0  {1,S} {20,S}
9  O  U0 L2 E0  {1,S} {21,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {4,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {5,S}
18 H  U0 L0 E0  {5,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {8,S}
21 H  U0 L0 E0  {9,S}
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
Si(OC2H5)(OH)3
multiplicity 1
1  C  U0 L0 E0  {3,S} {4,S} {8,S} {9,S}
2  Si U0 L0 E0  {4,S} {5,S} {6,S} {7,S}
3  C  U0 L0 E0  {1,S} {10,S} {11,S} {12,S}
4  O  U0 L2 E0  {1,S} {2,S}
5  O  U0 L2 E0  {2,S} {13,S}
6  O  U0 L2 E0  {2,S} {14,S}
7  O  U0 L2 E0  {2,S} {15,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {3,S}
11 H  U0 L0 E0  {3,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {5,S}
14 H  U0 L0 E0  {6,S}
15 H  U0 L0 E0  {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)2(OH)2
multiplicity 1
1  Si U0 L0 E0  {6,S} {7,S} {8,S} {9,S}
2  C  U0 L0 E0  {4,S} {6,S} {10,S} {11,S}
3  C  U0 L0 E0  {5,S} {7,S} {12,S} {13,S}
4  C  U0 L0 E0  {2,S} {14,S} {15,S} {16,S}
5  C  U0 L0 E0  {3,S} {17,S} {18,S} {19,S}
6  O  U0 L2 E0  {1,S} {2,S}
7  O  U0 L2 E0  {1,S} {3,S}
8  O  U0 L2 E0  {1,S} {20,S}
9  O  U0 L2 E0  {1,S} {21,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {4,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {5,S}
18 H  U0 L0 E0  {5,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {8,S}
21 H  U0 L0 E0  {9,S}
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
O_Si(OC2H5)2
multiplicity 1
1  C  U0 L0 E0  {3,S} {6,S} {8,S} {9,S}
2  C  U0 L0 E0  {4,S} {7,S} {10,S} {11,S}
3  C  U0 L0 E0  {1,S} {12,S} {13,S} {14,S}
4  C  U0 L0 E0  {2,S} {15,S} {16,S} {17,S}
5  Si U0 L0 E0  {6,S} {7,S} {18,D}
6  O  U0 L2 E0  {1,S} {5,S}
7  O  U0 L2 E0  {2,S} {5,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 O  U0 L2 E0  {5,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501200000000.0, 's^-1'),
        n = 0,
        Ea = (39.74, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)2(OH)2
multiplicity 1
1  Si U0 L0 E0  {6,S} {7,S} {8,S} {9,S}
2  C  U0 L0 E0  {4,S} {6,S} {10,S} {11,S}
3  C  U0 L0 E0  {5,S} {7,S} {12,S} {13,S}
4  C  U0 L0 E0  {2,S} {14,S} {15,S} {16,S}
5  C  U0 L0 E0  {3,S} {17,S} {18,S} {19,S}
6  O  U0 L2 E0  {1,S} {2,S}
7  O  U0 L2 E0  {1,S} {3,S}
8  O  U0 L2 E0  {1,S} {20,S}
9  O  U0 L2 E0  {1,S} {21,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {4,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {5,S}
18 H  U0 L0 E0  {5,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {8,S}
21 H  U0 L0 E0  {9,S}
""",
    product1 = 
"""
C2H5OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
O_Si(OC2H5)OH
multiplicity 1
1  C  U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2  C  U0 L0 E0  {1,S} {8,S} {9,S} {10,S}
3  Si U0 L0 E0  {4,S} {5,S} {11,D}
4  O  U0 L2 E0  {1,S} {3,S}
5  O  U0 L2 E0  {3,S} {12,S}
6  H  U0 L0 E0  {1,S}
7  H  U0 L0 E0  {1,S}
8  H  U0 L0 E0  {2,S}
9  H  U0 L0 E0  {2,S}
10 H  U0 L0 E0  {2,S}
11 O  U0 L2 E0  {3,D}
12 H  U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (631000000000.0, 's^-1'),
        n = 0,
        Ea = (45.105, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)2(OH)2
multiplicity 1
1  Si U0 L0 E0  {6,S} {7,S} {8,S} {9,S}
2  C  U0 L0 E0  {4,S} {6,S} {10,S} {11,S}
3  C  U0 L0 E0  {5,S} {7,S} {12,S} {13,S}
4  C  U0 L0 E0  {2,S} {14,S} {15,S} {16,S}
5  C  U0 L0 E0  {3,S} {17,S} {18,S} {19,S}
6  O  U0 L2 E0  {1,S} {2,S}
7  O  U0 L2 E0  {1,S} {3,S}
8  O  U0 L2 E0  {1,S} {20,S}
9  O  U0 L2 E0  {1,S} {21,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {4,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {5,S}
18 H  U0 L0 E0  {5,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {8,S}
21 H  U0 L0 E0  {9,S}
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
CH2OSi(OC2H5)(OH)2
multiplicity 2
1  C  U0 L0 E0  {3,S} {9,S} {10,S} {11,S}
2  C  U1 L0 E0  {6,S} {12,S} {13,S}
3  C  U0 L0 E0  {1,S} {7,S} {14,S} {15,S}
4  O  U0 L2 E0  {8,S} {16,S}
5  O  U0 L2 E0  {8,S} {17,S}
6  O  U0 L2 E0  {2,S} {8,S}
7  O  U0 L2 E0  {3,S} {8,S}
8  Si U0 L0 E0  {4,S} {5,S} {6,S} {7,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {1,S}
11 H  U0 L0 E0  {1,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {2,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e+17, 's^-1'),
        n = 0,
        Ea = (86.037, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)(OH)3
multiplicity 1
1  C  U0 L0 E0  {3,S} {4,S} {8,S} {9,S}
2  Si U0 L0 E0  {4,S} {5,S} {6,S} {7,S}
3  C  U0 L0 E0  {1,S} {10,S} {11,S} {12,S}
4  O  U0 L2 E0  {1,S} {2,S}
5  O  U0 L2 E0  {2,S} {13,S}
6  O  U0 L2 E0  {2,S} {14,S}
7  O  U0 L2 E0  {2,S} {15,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {3,S}
11 H  U0 L0 E0  {3,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {5,S}
14 H  U0 L0 E0  {6,S}
15 H  U0 L0 E0  {7,S}
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
Si(OH)4
multiplicity 1
1 O  U0 L2 E0  {5,S} {6,S}
2 O  U0 L2 E0  {5,S} {7,S}
3 O  U0 L2 E0  {5,S} {8,S}
4 O  U0 L2 E0  {5,S} {9,S}
5 Si U0 L0 E0  {1,S} {2,S} {3,S} {4,S}
6 H  U0 L0 E0  {1,S}
7 H  U0 L0 E0  {2,S}
8 H  U0 L0 E0  {3,S}
9 H  U0 L0 E0  {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (631000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)(OH)3
multiplicity 1
1  C  U0 L0 E0  {3,S} {4,S} {8,S} {9,S}
2  Si U0 L0 E0  {4,S} {5,S} {6,S} {7,S}
3  C  U0 L0 E0  {1,S} {10,S} {11,S} {12,S}
4  O  U0 L2 E0  {1,S} {2,S}
5  O  U0 L2 E0  {2,S} {13,S}
6  O  U0 L2 E0  {2,S} {14,S}
7  O  U0 L2 E0  {2,S} {15,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {3,S}
11 H  U0 L0 E0  {3,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {5,S}
14 H  U0 L0 E0  {6,S}
15 H  U0 L0 E0  {7,S}
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
O_Si(OC2H5)OH
multiplicity 1
1  C  U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2  C  U0 L0 E0  {1,S} {8,S} {9,S} {10,S}
3  Si U0 L0 E0  {4,S} {5,S} {11,D}
4  O  U0 L2 E0  {1,S} {3,S}
5  O  U0 L2 E0  {3,S} {12,S}
6  H  U0 L0 E0  {1,S}
7  H  U0 L0 E0  {1,S}
8  H  U0 L0 E0  {2,S}
9  H  U0 L0 E0  {2,S}
10 H  U0 L0 E0  {2,S}
11 O  U0 L2 E0  {3,D}
12 H  U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501200000000.0, 's^-1'),
        n = 0,
        Ea = (39.74, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)(OH)3
multiplicity 1
1  C  U0 L0 E0  {3,S} {4,S} {8,S} {9,S}
2  Si U0 L0 E0  {4,S} {5,S} {6,S} {7,S}
3  C  U0 L0 E0  {1,S} {10,S} {11,S} {12,S}
4  O  U0 L2 E0  {1,S} {2,S}
5  O  U0 L2 E0  {2,S} {13,S}
6  O  U0 L2 E0  {2,S} {14,S}
7  O  U0 L2 E0  {2,S} {15,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {3,S}
11 H  U0 L0 E0  {3,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {5,S}
14 H  U0 L0 E0  {6,S}
15 H  U0 L0 E0  {7,S}
""",
    product1 = 
"""
C2H5OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
O_Si(OH)2
multiplicity 1
1 Si U0 L0 E0  {2,S} {3,S} {4,D}
2 O  U0 L2 E0  {1,S} {5,S}
3 O  U0 L2 E0  {1,S} {6,S}
4 O  U0 L2 E0  {1,D}
5 H  U0 L0 E0  {2,S}
6 H  U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501200000000.0, 's^-1'),
        n = 0,
        Ea = (45.105, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
Si(OC2H5)(OH)3
multiplicity 1
1  C  U0 L0 E0  {3,S} {4,S} {8,S} {9,S}
2  Si U0 L0 E0  {4,S} {5,S} {6,S} {7,S}
3  C  U0 L0 E0  {1,S} {10,S} {11,S} {12,S}
4  O  U0 L2 E0  {1,S} {2,S}
5  O  U0 L2 E0  {2,S} {13,S}
6  O  U0 L2 E0  {2,S} {14,S}
7  O  U0 L2 E0  {2,S} {15,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {3,S}
11 H  U0 L0 E0  {3,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {5,S}
14 H  U0 L0 E0  {6,S}
15 H  U0 L0 E0  {7,S}
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
CH2OSi(OH)3
multiplicity 2
1  C  U1 L0 E0  {5,S} {7,S} {8,S}
2  O  U0 L2 E0  {6,S} {9,S}
3  O  U0 L2 E0  {6,S} {10,S}
4  O  U0 L2 E0  {6,S} {11,S}
5  O  U0 L2 E0  {1,S} {6,S}
6  Si U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
7  H  U0 L0 E0  {1,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {2,S}
10 H  U0 L0 E0  {3,S}
11 H  U0 L0 E0  {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+17, 's^-1'),
        n = 0,
        Ea = (86.037, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
O_Si(OC2H5)2
multiplicity 1
1  C  U0 L0 E0  {3,S} {6,S} {8,S} {9,S}
2  C  U0 L0 E0  {4,S} {7,S} {10,S} {11,S}
3  C  U0 L0 E0  {1,S} {12,S} {13,S} {14,S}
4  C  U0 L0 E0  {2,S} {15,S} {16,S} {17,S}
5  Si U0 L0 E0  {6,S} {7,S} {18,D}
6  O  U0 L2 E0  {1,S} {5,S}
7  O  U0 L2 E0  {2,S} {5,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 O  U0 L2 E0  {5,D}
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
O_Si(OC2H5)OH
multiplicity 1
1  C  U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2  C  U0 L0 E0  {1,S} {8,S} {9,S} {10,S}
3  Si U0 L0 E0  {4,S} {5,S} {11,D}
4  O  U0 L2 E0  {1,S} {3,S}
5  O  U0 L2 E0  {3,S} {12,S}
6  H  U0 L0 E0  {1,S}
7  H  U0 L0 E0  {1,S}
8  H  U0 L0 E0  {2,S}
9  H  U0 L0 E0  {2,S}
10 H  U0 L0 E0  {2,S}
11 O  U0 L2 E0  {3,D}
12 H  U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (10000000000000.0, 's^-1'),
                n = 0,
                Ea = (52.059, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (1000000000000000.0, 's^-1'),
                n = 0,
                Ea = (68.552, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from TEOS.',
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
O_Si(OC2H5)2
multiplicity 1
1  C  U0 L0 E0  {3,S} {6,S} {8,S} {9,S}
2  C  U0 L0 E0  {4,S} {7,S} {10,S} {11,S}
3  C  U0 L0 E0  {1,S} {12,S} {13,S} {14,S}
4  C  U0 L0 E0  {2,S} {15,S} {16,S} {17,S}
5  Si U0 L0 E0  {6,S} {7,S} {18,D}
6  O  U0 L2 E0  {1,S} {5,S}
7  O  U0 L2 E0  {2,S} {5,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {3,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 O  U0 L2 E0  {5,D}
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
CH2OSiO(OC2H5)
multiplicity 2
1  C  U0 L0 E0  {3,S} {8,S} {9,S} {10,S}
2  C  U1 L0 E0  {5,S} {11,S} {12,S}
3  C  U0 L0 E0  {1,S} {6,S} {13,S} {14,S}
4  O  U0 L2 E0  {7,D}
5  O  U0 L2 E0  {2,S} {7,S}
6  O  U0 L2 E0  {3,S} {7,S}
7  Si U0 L0 E0  {4,D} {5,S} {6,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {1,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e+17, 's^-1'),
        n = 0,
        Ea = (86.037, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
O_Si(OC2H5)OH
multiplicity 1
1  C  U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2  C  U0 L0 E0  {1,S} {8,S} {9,S} {10,S}
3  Si U0 L0 E0  {4,S} {5,S} {11,D}
4  O  U0 L2 E0  {1,S} {3,S}
5  O  U0 L2 E0  {3,S} {12,S}
6  H  U0 L0 E0  {1,S}
7  H  U0 L0 E0  {1,S}
8  H  U0 L0 E0  {2,S}
9  H  U0 L0 E0  {2,S}
10 H  U0 L0 E0  {2,S}
11 O  U0 L2 E0  {3,D}
12 H  U0 L0 E0  {5,S}
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
O_Si(OH)2
multiplicity 1
1 Si U0 L0 E0  {2,S} {3,S} {4,D}
2 O  U0 L2 E0  {1,S} {5,S}
3 O  U0 L2 E0  {1,S} {6,S}
4 O  U0 L2 E0  {1,D}
5 H  U0 L0 E0  {2,S}
6 H  U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(
                A = (5012000000000.0, 's^-1'),
                n = 0,
                Ea = (52.059, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
            Arrhenius(
                A = (501200000000000.0, 's^-1'),
                n = 0,
                Ea = (68.552, 'kcal/mol'),
                T0 = (1, 'K'),
            ),
        ],
        comment = 'Reaction and kinetics from TEOS.',
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
O_Si(OC2H5)OH
multiplicity 1
1  C  U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2  C  U0 L0 E0  {1,S} {8,S} {9,S} {10,S}
3  Si U0 L0 E0  {4,S} {5,S} {11,D}
4  O  U0 L2 E0  {1,S} {3,S}
5  O  U0 L2 E0  {3,S} {12,S}
6  H  U0 L0 E0  {1,S}
7  H  U0 L0 E0  {1,S}
8  H  U0 L0 E0  {2,S}
9  H  U0 L0 E0  {2,S}
10 H  U0 L0 E0  {2,S}
11 O  U0 L2 E0  {3,D}
12 H  U0 L0 E0  {5,S}
""",
    product1 = 
"""
C2H5OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
SiO2
multiplicity 1
1 O  U0 L2 E0  {3,D}
2 O  U0 L2 E0  {3,D}
3 Si U0 L0 E0  {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (158500000000.0, 's^-1'),
        n = 0,
        Ea = (47.092, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
O_Si(OC2H5)OH
multiplicity 1
1  C  U0 L0 E0  {2,S} {4,S} {6,S} {7,S}
2  C  U0 L0 E0  {1,S} {8,S} {9,S} {10,S}
3  Si U0 L0 E0  {4,S} {5,S} {11,D}
4  O  U0 L2 E0  {1,S} {3,S}
5  O  U0 L2 E0  {3,S} {12,S}
6  H  U0 L0 E0  {1,S}
7  H  U0 L0 E0  {1,S}
8  H  U0 L0 E0  {2,S}
9  H  U0 L0 E0  {2,S}
10 H  U0 L0 E0  {2,S}
11 O  U0 L2 E0  {3,D}
12 H  U0 L0 E0  {5,S}
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
CH2OSiO(OH)
multiplicity 2
1 C  U1 L0 E0  {4,S} {6,S} {7,S}
2 O  U0 L2 E0  {5,S} {8,S}
3 O  U0 L2 E0  {5,D}
4 O  U0 L2 E0  {1,S} {5,S}
5 Si U0 L0 E0  {2,S} {3,D} {4,S}
6 H  U0 L0 E0  {1,S}
7 H  U0 L0 E0  {1,S}
8 H  U0 L0 E0  {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+17, 's^-1'),
        n = 0,
        Ea = (86.037, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
CH3OSi(OC2H5)2(OC2H3)
multiplicity 1
1  Si U0 L0 E0  {9,S} {10,S} {11,S} {12,S}
2  C  U0 L0 E0  {4,S} {9,S} {13,S} {14,S}
3  C  U0 L0 E0  {5,S} {10,S} {15,S} {16,S}
4  C  U0 L0 E0  {2,S} {17,S} {18,S} {19,S}
5  C  U0 L0 E0  {3,S} {20,S} {21,S} {22,S}
6  C  U0 L0 E0  {11,S} {23,S} {24,S} {25,S}
7  C  U0 L0 E0  {8,D} {12,S} {26,S}
8  C  U0 L0 E0  {7,D} {27,S} {28,S}
9  O  U0 L2 E0  {1,S} {2,S}
10 O  U0 L2 E0  {1,S} {3,S}
11 O  U0 L2 E0  {1,S} {6,S}
12 O  U0 L2 E0  {1,S} {7,S}
13 H  U0 L0 E0  {2,S}
14 H  U0 L0 E0  {2,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {3,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {4,S}
19 H  U0 L0 E0  {4,S}
20 H  U0 L0 E0  {5,S}
21 H  U0 L0 E0  {5,S}
22 H  U0 L0 E0  {5,S}
23 H  U0 L0 E0  {6,S}
24 H  U0 L0 E0  {6,S}
25 H  U0 L0 E0  {6,S}
26 H  U0 L0 E0  {7,S}
27 H  U0 L0 E0  {8,S}
28 H  U0 L0 E0  {8,S}
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
CH3OSi(OC2H5)(OC2H3)OH
multiplicity 1
1  Si U0 L0 E0  {7,S} {8,S} {9,S} {10,S}
2  C  U0 L0 E0  {3,S} {7,S} {11,S} {12,S}
3  C  U0 L0 E0  {2,S} {13,S} {14,S} {15,S}
4  C  U0 L0 E0  {8,S} {16,S} {17,S} {18,S}
5  C  U0 L0 E0  {6,D} {9,S} {19,S}
6  C  U0 L0 E0  {5,D} {20,S} {21,S}
7  O  U0 L2 E0  {1,S} {2,S}
8  O  U0 L2 E0  {1,S} {4,S}
9  O  U0 L2 E0  {1,S} {5,S}
10 O  U0 L2 E0  {1,S} {22,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {4,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {6,S}
21 H  U0 L0 E0  {6,S}
22 H  U0 L0 E0  {10,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
CH3OSi(OC2H5)2(OC2H3)
multiplicity 1
1  Si U0 L0 E0  {9,S} {10,S} {11,S} {12,S}
2  C  U0 L0 E0  {4,S} {9,S} {13,S} {14,S}
3  C  U0 L0 E0  {5,S} {10,S} {15,S} {16,S}
4  C  U0 L0 E0  {2,S} {17,S} {18,S} {19,S}
5  C  U0 L0 E0  {3,S} {20,S} {21,S} {22,S}
6  C  U0 L0 E0  {11,S} {23,S} {24,S} {25,S}
7  C  U0 L0 E0  {8,D} {12,S} {26,S}
8  C  U0 L0 E0  {7,D} {27,S} {28,S}
9  O  U0 L2 E0  {1,S} {2,S}
10 O  U0 L2 E0  {1,S} {3,S}
11 O  U0 L2 E0  {1,S} {6,S}
12 O  U0 L2 E0  {1,S} {7,S}
13 H  U0 L0 E0  {2,S}
14 H  U0 L0 E0  {2,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {3,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {4,S}
19 H  U0 L0 E0  {4,S}
20 H  U0 L0 E0  {5,S}
21 H  U0 L0 E0  {5,S}
22 H  U0 L0 E0  {5,S}
23 H  U0 L0 E0  {6,S}
24 H  U0 L0 E0  {6,S}
25 H  U0 L0 E0  {6,S}
26 H  U0 L0 E0  {7,S}
27 H  U0 L0 E0  {8,S}
28 H  U0 L0 E0  {8,S}
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
CH2OSi(OC2H5)(OC2H3)(OCH3)
multiplicity 2
1  C  U0 L0 E0  {5,D} {12,S} {13,S}
2  C  U0 L0 E0  {6,S} {14,S} {15,S} {16,S}
3  C  U1 L0 E0  {7,S} {17,S} {18,S}
4  C  U0 L0 E0  {8,S} {19,S} {20,S} {21,S}
5  C  U0 L0 E0  {1,D} {9,S} {22,S}
6  C  U0 L0 E0  {2,S} {10,S} {23,S} {24,S}
7  O  U0 L2 E0  {3,S} {11,S}
8  O  U0 L2 E0  {4,S} {11,S}
9  O  U0 L2 E0  {5,S} {11,S}
10 O  U0 L2 E0  {6,S} {11,S}
11 Si U0 L0 E0  {7,S} {8,S} {9,S} {10,S}
12 H  U0 L0 E0  {1,S}
13 H  U0 L0 E0  {1,S}
14 H  U0 L0 E0  {2,S}
15 H  U0 L0 E0  {2,S}
16 H  U0 L0 E0  {2,S}
17 H  U0 L0 E0  {3,S}
18 H  U0 L0 E0  {3,S}
19 H  U0 L0 E0  {4,S}
20 H  U0 L0 E0  {4,S}
21 H  U0 L0 E0  {4,S}
22 H  U0 L0 E0  {5,S}
23 H  U0 L0 E0  {6,S}
24 H  U0 L0 E0  {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e+17, 's^-1'),
        n = 0,
        Ea = (86.037, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
CH3OSi(OC2H5)(OC2H3)OH
multiplicity 1
1  Si U0 L0 E0  {7,S} {8,S} {9,S} {10,S}
2  C  U0 L0 E0  {3,S} {7,S} {11,S} {12,S}
3  C  U0 L0 E0  {2,S} {13,S} {14,S} {15,S}
4  C  U0 L0 E0  {8,S} {16,S} {17,S} {18,S}
5  C  U0 L0 E0  {6,D} {9,S} {19,S}
6  C  U0 L0 E0  {5,D} {20,S} {21,S}
7  O  U0 L2 E0  {1,S} {2,S}
8  O  U0 L2 E0  {1,S} {4,S}
9  O  U0 L2 E0  {1,S} {5,S}
10 O  U0 L2 E0  {1,S} {22,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {4,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {6,S}
21 H  U0 L0 E0  {6,S}
22 H  U0 L0 E0  {10,S}
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
CH3OSi(OC2H3)(OH)2
multiplicity 1
1  C  U0 L0 E0  {3,D} {9,S} {10,S}
2  C  U0 L0 E0  {6,S} {11,S} {12,S} {13,S}
3  C  U0 L0 E0  {1,D} {7,S} {14,S}
4  O  U0 L2 E0  {8,S} {15,S}
5  O  U0 L2 E0  {8,S} {16,S}
6  O  U0 L2 E0  {2,S} {8,S}
7  O  U0 L2 E0  {3,S} {8,S}
8  Si U0 L0 E0  {4,S} {5,S} {6,S} {7,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {1,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {2,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {4,S}
16 H  U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501200000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
CH3OSi(OC2H5)(OC2H3)OH
multiplicity 1
1  Si U0 L0 E0  {7,S} {8,S} {9,S} {10,S}
2  C  U0 L0 E0  {3,S} {7,S} {11,S} {12,S}
3  C  U0 L0 E0  {2,S} {13,S} {14,S} {15,S}
4  C  U0 L0 E0  {8,S} {16,S} {17,S} {18,S}
5  C  U0 L0 E0  {6,D} {9,S} {19,S}
6  C  U0 L0 E0  {5,D} {20,S} {21,S}
7  O  U0 L2 E0  {1,S} {2,S}
8  O  U0 L2 E0  {1,S} {4,S}
9  O  U0 L2 E0  {1,S} {5,S}
10 O  U0 L2 E0  {1,S} {22,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {4,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {6,S}
21 H  U0 L0 E0  {6,S}
22 H  U0 L0 E0  {10,S}
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
CH2OSi(OCH3)(OC2H3)OH
multiplicity 2
1  C  U0 L0 E0  {4,D} {10,S} {11,S}
2  C  U1 L0 E0  {6,S} {12,S} {13,S}
3  C  U0 L0 E0  {7,S} {14,S} {15,S} {16,S}
4  C  U0 L0 E0  {1,D} {8,S} {17,S}
5  O  U0 L2 E0  {9,S} {18,S}
6  O  U0 L2 E0  {2,S} {9,S}
7  O  U0 L2 E0  {3,S} {9,S}
8  O  U0 L2 E0  {4,S} {9,S}
9  Si U0 L0 E0  {5,S} {6,S} {7,S} {8,S}
10 H  U0 L0 E0  {1,S}
11 H  U0 L0 E0  {1,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {2,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {3,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+17, 's^-1'),
        n = 0,
        Ea = (86.037, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
CH3OSi(OC2H5)(OC2H3)OH
multiplicity 1
1  Si U0 L0 E0  {7,S} {8,S} {9,S} {10,S}
2  C  U0 L0 E0  {3,S} {7,S} {11,S} {12,S}
3  C  U0 L0 E0  {2,S} {13,S} {14,S} {15,S}
4  C  U0 L0 E0  {8,S} {16,S} {17,S} {18,S}
5  C  U0 L0 E0  {6,D} {9,S} {19,S}
6  C  U0 L0 E0  {5,D} {20,S} {21,S}
7  O  U0 L2 E0  {1,S} {2,S}
8  O  U0 L2 E0  {1,S} {4,S}
9  O  U0 L2 E0  {1,S} {5,S}
10 O  U0 L2 E0  {1,S} {22,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {3,S}
14 H  U0 L0 E0  {3,S}
15 H  U0 L0 E0  {3,S}
16 H  U0 L0 E0  {4,S}
17 H  U0 L0 E0  {4,S}
18 H  U0 L0 E0  {4,S}
19 H  U0 L0 E0  {5,S}
20 H  U0 L0 E0  {6,S}
21 H  U0 L0 E0  {6,S}
22 H  U0 L0 E0  {10,S}
""",
    product1 = 
"""
C2H5OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
""",
    product2 = 
"""
CH3OSi(O)OC2H3
multiplicity 1
1  C  U0 L0 E0  {3,D} {8,S} {9,S}
2  C  U0 L0 E0  {5,S} {10,S} {11,S} {12,S}
3  C  U0 L0 E0  {1,D} {6,S} {13,S}
4  O  U0 L2 E0  {7,D}
5  O  U0 L2 E0  {2,S} {7,S}
6  O  U0 L2 E0  {3,S} {7,S}
7  Si U0 L0 E0  {4,D} {5,S} {6,S}
8  H  U0 L0 E0  {1,S}
9  H  U0 L0 E0  {1,S}
10 H  U0 L0 E0  {2,S}
11 H  U0 L0 E0  {2,S}
12 H  U0 L0 E0  {2,S}
13 H  U0 L0 E0  {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (158500000000.0, 's^-1'),
        n = 0,
        Ea = (45.105, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
C2H5OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
9 H U0 L0 E0  {3,S}
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
H2O
multiplicity 1
1 O U0 L2 E0  {2,S} {3,S}
2 H U0 L0 E0  {1,S}
3 H U0 L0 E0  {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63100000000000.0, 's^-1'),
        n = 0,
        Ea = (66.167, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
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
C2H5OH
multiplicity 1
1 C U0 L0 E0  {2,S} {3,S} {4,S} {5,S}
2 C U0 L0 E0  {1,S} {6,S} {7,S} {8,S}
3 O U0 L2 E0  {1,S} {9,S}
4 H U0 L0 E0  {1,S}
5 H U0 L0 E0  {1,S}
6 H U0 L0 E0  {2,S}
7 H U0 L0 E0  {2,S}
8 H U0 L0 E0  {2,S}
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
        A = (1e+16, 's^-1'),
        n = 0,
        Ea = (83.057, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'Reaction and kinetics from TEOS.',
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

