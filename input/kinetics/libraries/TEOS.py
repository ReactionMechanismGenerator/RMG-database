#!/usr/bin/env python
# encoding: utf-8

name = "TEOS"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
Si(OC2H5)4
1  C  0 {5,S} {14,S} {15,S} {16,S}
2  C  0 {6,S} {17,S} {18,S} {19,S}
3  C  0 {7,S} {20,S} {21,S} {22,S}
4  C  0 {8,S} {23,S} {24,S} {25,S}
5  C  0 {1,S} {9,S} {26,S} {27,S}
6  C  0 {2,S} {10,S} {28,S} {29,S}
7  C  0 {3,S} {11,S} {30,S} {31,S}
8  C  0 {4,S} {12,S} {32,S} {33,S}
9  O  0 {5,S} {13,S}
10 O  0 {6,S} {13,S}
11 O  0 {7,S} {13,S}
12 O  0 {8,S} {13,S}
13 Si 0 {9,S} {10,S} {11,S} {12,S}
14 H  0 {1,S}
15 H  0 {1,S}
16 H  0 {1,S}
17 H  0 {2,S}
18 H  0 {2,S}
19 H  0 {2,S}
20 H  0 {3,S}
21 H  0 {3,S}
22 H  0 {3,S}
23 H  0 {4,S}
24 H  0 {4,S}
25 H  0 {4,S}
26 H  0 {5,S}
27 H  0 {5,S}
28 H  0 {6,S}
29 H  0 {6,S}
30 H  0 {7,S}
31 H  0 {7,S}
32 H  0 {8,S}
33 H  0 {8,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
Si(OC2H5)3OH
1  C  0 {4,S} {12,S} {13,S} {14,S}
2  C  0 {5,S} {15,S} {16,S} {17,S}
3  C  0 {6,S} {18,S} {19,S} {20,S}
4  C  0 {1,S} {8,S} {21,S} {22,S}
5  C  0 {2,S} {9,S} {23,S} {24,S}
6  C  0 {3,S} {10,S} {25,S} {26,S}
7  O  0 {11,S} {27,S}
8  O  0 {4,S} {11,S}
9  O  0 {5,S} {11,S}
10 O  0 {6,S} {11,S}
11 Si 0 {7,S} {8,S} {9,S} {10,S}
12 H  0 {1,S}
13 H  0 {1,S}
14 H  0 {1,S}
15 H  0 {2,S}
16 H  0 {2,S}
17 H  0 {2,S}
18 H  0 {3,S}
19 H  0 {3,S}
20 H  0 {3,S}
21 H  0 {4,S}
22 H  0 {4,S}
23 H  0 {5,S}
24 H  0 {5,S}
25 H  0 {6,S}
26 H  0 {6,S}
27 H  0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1995000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Reactions and modified Arrhenius parameters from:
J Herzler, JA Manion, W Tsang
"Single-Pulse Shock Tube Study of the Decomposition of Tetraethoxysilane and Related Compounds"
J. Phys. Chem. A 1997, 101, 5500-5508
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
Si(OC2H5)4
1  C  0 {5,S} {14,S} {15,S} {16,S}
2  C  0 {6,S} {17,S} {18,S} {19,S}
3  C  0 {7,S} {20,S} {21,S} {22,S}
4  C  0 {8,S} {23,S} {24,S} {25,S}
5  C  0 {1,S} {9,S} {26,S} {27,S}
6  C  0 {2,S} {10,S} {28,S} {29,S}
7  C  0 {3,S} {11,S} {30,S} {31,S}
8  C  0 {4,S} {12,S} {32,S} {33,S}
9  O  0 {5,S} {13,S}
10 O  0 {6,S} {13,S}
11 O  0 {7,S} {13,S}
12 O  0 {8,S} {13,S}
13 Si 0 {9,S} {10,S} {11,S} {12,S}
14 H  0 {1,S}
15 H  0 {1,S}
16 H  0 {1,S}
17 H  0 {2,S}
18 H  0 {2,S}
19 H  0 {2,S}
20 H  0 {3,S}
21 H  0 {3,S}
22 H  0 {3,S}
23 H  0 {4,S}
24 H  0 {4,S}
25 H  0 {4,S}
26 H  0 {5,S}
27 H  0 {5,S}
28 H  0 {6,S}
29 H  0 {6,S}
30 H  0 {7,S}
31 H  0 {7,S}
32 H  0 {8,S}
33 H  0 {8,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OSi(OC2H5)3
1  C  0 {5,S} {13,S} {14,S} {15,S}
2  C  0 {6,S} {16,S} {17,S} {18,S}
3  C  0 {7,S} {19,S} {20,S} {21,S}
4  C  1 {8,S} {22,S} {23,S}
5  C  0 {1,S} {9,S} {24,S} {25,S}
6  C  0 {2,S} {10,S} {26,S} {27,S}
7  C  0 {3,S} {11,S} {28,S} {29,S}
8  O  0 {4,S} {12,S}
9  O  0 {5,S} {12,S}
10 O  0 {6,S} {12,S}
11 O  0 {7,S} {12,S}
12 Si 0 {8,S} {9,S} {10,S} {11,S}
13 H  0 {1,S}
14 H  0 {1,S}
15 H  0 {1,S}
16 H  0 {2,S}
17 H  0 {2,S}
18 H  0 {2,S}
19 H  0 {3,S}
20 H  0 {3,S}
21 H  0 {3,S}
22 H  0 {4,S}
23 H  0 {4,S}
24 H  0 {5,S}
25 H  0 {5,S}
26 H  0 {6,S}
27 H  0 {6,S}
28 H  0 {7,S}
29 H  0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.981e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
Si(OC2H5)3OH
1  C  0 {4,S} {12,S} {13,S} {14,S}
2  C  0 {5,S} {15,S} {16,S} {17,S}
3  C  0 {6,S} {18,S} {19,S} {20,S}
4  C  0 {1,S} {8,S} {21,S} {22,S}
5  C  0 {2,S} {9,S} {23,S} {24,S}
6  C  0 {3,S} {10,S} {25,S} {26,S}
7  O  0 {11,S} {27,S}
8  O  0 {4,S} {11,S}
9  O  0 {5,S} {11,S}
10 O  0 {6,S} {11,S}
11 Si 0 {7,S} {8,S} {9,S} {10,S}
12 H  0 {1,S}
13 H  0 {1,S}
14 H  0 {1,S}
15 H  0 {2,S}
16 H  0 {2,S}
17 H  0 {2,S}
18 H  0 {3,S}
19 H  0 {3,S}
20 H  0 {3,S}
21 H  0 {4,S}
22 H  0 {4,S}
23 H  0 {5,S}
24 H  0 {5,S}
25 H  0 {6,S}
26 H  0 {6,S}
27 H  0 {7,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
Si(OC2H5)2(OH)2
1  C  0 {3,S} {10,S} {11,S} {12,S}
2  C  0 {4,S} {13,S} {14,S} {15,S}
3  C  0 {1,S} {7,S} {16,S} {17,S}
4  C  0 {2,S} {8,S} {18,S} {19,S}
5  O  0 {9,S} {20,S}
6  O  0 {9,S} {21,S}
7  O  0 {3,S} {9,S}
8  O  0 {4,S} {9,S}
9  Si 0 {5,S} {6,S} {7,S} {8,S}
10 H  0 {1,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {2,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {3,S}
17 H  0 {3,S}
18 H  0 {4,S}
19 H  0 {4,S}
20 H  0 {5,S}
21 H  0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1585000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
Si(OC2H5)3OH
1  C  0 {4,S} {12,S} {13,S} {14,S}
2  C  0 {5,S} {15,S} {16,S} {17,S}
3  C  0 {6,S} {18,S} {19,S} {20,S}
4  C  0 {1,S} {8,S} {21,S} {22,S}
5  C  0 {2,S} {9,S} {23,S} {24,S}
6  C  0 {3,S} {10,S} {25,S} {26,S}
7  O  0 {11,S} {27,S}
8  O  0 {4,S} {11,S}
9  O  0 {5,S} {11,S}
10 O  0 {6,S} {11,S}
11 Si 0 {7,S} {8,S} {9,S} {10,S}
12 H  0 {1,S}
13 H  0 {1,S}
14 H  0 {1,S}
15 H  0 {2,S}
16 H  0 {2,S}
17 H  0 {2,S}
18 H  0 {3,S}
19 H  0 {3,S}
20 H  0 {3,S}
21 H  0 {4,S}
22 H  0 {4,S}
23 H  0 {5,S}
24 H  0 {5,S}
25 H  0 {6,S}
26 H  0 {6,S}
27 H  0 {7,S}
""",
    product1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product2 = 
"""
O_Si(OC2H5)2
1  C  0 {3,S} {6,S} {9,S} {10,S}
2  C  0 {4,S} {7,S} {11,S} {12,S}
3  C  0 {1,S} {13,S} {14,S} {15,S}
4  C  0 {2,S} {16,S} {17,S} {18,S}
5  Si 0 {6,S} {7,S} {8,D}
6  O  0 {1,S} {5,S}
7  O  0 {2,S} {5,S}
8  O  0 {5,D}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {3,S}
15 H  0 {3,S}
16 H  0 {4,S}
17 H  0 {4,S}
18 H  0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(501200000000.0, 's^-1'), n=0, Ea=(45.105, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
Si(OC2H5)3OH
1  C  0 {4,S} {12,S} {13,S} {14,S}
2  C  0 {5,S} {15,S} {16,S} {17,S}
3  C  0 {6,S} {18,S} {19,S} {20,S}
4  C  0 {1,S} {8,S} {21,S} {22,S}
5  C  0 {2,S} {9,S} {23,S} {24,S}
6  C  0 {3,S} {10,S} {25,S} {26,S}
7  O  0 {11,S} {27,S}
8  O  0 {4,S} {11,S}
9  O  0 {5,S} {11,S}
10 O  0 {6,S} {11,S}
11 Si 0 {7,S} {8,S} {9,S} {10,S}
12 H  0 {1,S}
13 H  0 {1,S}
14 H  0 {1,S}
15 H  0 {2,S}
16 H  0 {2,S}
17 H  0 {2,S}
18 H  0 {3,S}
19 H  0 {3,S}
20 H  0 {3,S}
21 H  0 {4,S}
22 H  0 {4,S}
23 H  0 {5,S}
24 H  0 {5,S}
25 H  0 {6,S}
26 H  0 {6,S}
27 H  0 {7,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OSi(OC2H5)2OH
1  C  0 {4,S} {11,S} {12,S} {13,S}
2  C  0 {5,S} {14,S} {15,S} {16,S}
3  C  1 {7,S} {17,S} {18,S}
4  C  0 {1,S} {8,S} {19,S} {20,S}
5  C  0 {2,S} {9,S} {21,S} {22,S}
6  O  0 {10,S} {23,S}
7  O  0 {3,S} {10,S}
8  O  0 {4,S} {10,S}
9  O  0 {5,S} {10,S}
10 Si 0 {6,S} {7,S} {8,S} {9,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {1,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {2,S}
17 H  0 {3,S}
18 H  0 {3,S}
19 H  0 {4,S}
20 H  0 {4,S}
21 H  0 {5,S}
22 H  0 {5,S}
23 H  0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.162e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
Si(OC2H5)2(OH)2
1  C  0 {3,S} {10,S} {11,S} {12,S}
2  C  0 {4,S} {13,S} {14,S} {15,S}
3  C  0 {1,S} {7,S} {16,S} {17,S}
4  C  0 {2,S} {8,S} {18,S} {19,S}
5  O  0 {9,S} {20,S}
6  O  0 {9,S} {21,S}
7  O  0 {3,S} {9,S}
8  O  0 {4,S} {9,S}
9  Si 0 {5,S} {6,S} {7,S} {8,S}
10 H  0 {1,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {2,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {3,S}
17 H  0 {3,S}
18 H  0 {4,S}
19 H  0 {4,S}
20 H  0 {5,S}
21 H  0 {6,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
Si(OC2H5)(OH)3
1  C  0 {2,S} {8,S} {9,S} {10,S}
2  C  0 {1,S} {6,S} {11,S} {12,S}
3  O  0 {7,S} {13,S}
4  O  0 {7,S} {14,S}
5  O  0 {7,S} {15,S}
6  O  0 {2,S} {7,S}
7  Si 0 {3,S} {4,S} {5,S} {6,S}
8  H  0 {1,S}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {4,S}
15 H  0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
Si(OC2H5)2(OH)2
1  C  0 {3,S} {10,S} {11,S} {12,S}
2  C  0 {4,S} {13,S} {14,S} {15,S}
3  C  0 {1,S} {7,S} {16,S} {17,S}
4  C  0 {2,S} {8,S} {18,S} {19,S}
5  O  0 {9,S} {20,S}
6  O  0 {9,S} {21,S}
7  O  0 {3,S} {9,S}
8  O  0 {4,S} {9,S}
9  Si 0 {5,S} {6,S} {7,S} {8,S}
10 H  0 {1,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {2,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {3,S}
17 H  0 {3,S}
18 H  0 {4,S}
19 H  0 {4,S}
20 H  0 {5,S}
21 H  0 {6,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
O_Si(OC2H5)2
1  C  0 {3,S} {6,S} {9,S} {10,S}
2  C  0 {4,S} {7,S} {11,S} {12,S}
3  C  0 {1,S} {13,S} {14,S} {15,S}
4  C  0 {2,S} {16,S} {17,S} {18,S}
5  Si 0 {6,S} {7,S} {8,D}
6  O  0 {1,S} {5,S}
7  O  0 {2,S} {5,S}
8  O  0 {5,D}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {3,S}
15 H  0 {3,S}
16 H  0 {4,S}
17 H  0 {4,S}
18 H  0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(501200000000.0, 's^-1'), n=0, Ea=(39.74, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
Si(OC2H5)2(OH)2
1  C  0 {3,S} {10,S} {11,S} {12,S}
2  C  0 {4,S} {13,S} {14,S} {15,S}
3  C  0 {1,S} {7,S} {16,S} {17,S}
4  C  0 {2,S} {8,S} {18,S} {19,S}
5  O  0 {9,S} {20,S}
6  O  0 {9,S} {21,S}
7  O  0 {3,S} {9,S}
8  O  0 {4,S} {9,S}
9  Si 0 {5,S} {6,S} {7,S} {8,S}
10 H  0 {1,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {2,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {3,S}
17 H  0 {3,S}
18 H  0 {4,S}
19 H  0 {4,S}
20 H  0 {5,S}
21 H  0 {6,S}
""",
    product1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product2 = 
"""
O_Si(OC2H5)OH
1  C  0 {2,S} {4,S} {7,S} {8,S}
2  C  0 {1,S} {9,S} {10,S} {11,S}
3  Si 0 {4,S} {5,S} {6,D}
4  O  0 {1,S} {3,S}
5  O  0 {3,S} {12,S}
6  O  0 {3,D}
7  H  0 {1,S}
8  H  0 {1,S}
9  H  0 {2,S}
10 H  0 {2,S}
11 H  0 {2,S}
12 H  0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(631000000000.0, 's^-1'), n=0, Ea=(45.105, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
Si(OC2H5)2(OH)2
1  C  0 {3,S} {10,S} {11,S} {12,S}
2  C  0 {4,S} {13,S} {14,S} {15,S}
3  C  0 {1,S} {7,S} {16,S} {17,S}
4  C  0 {2,S} {8,S} {18,S} {19,S}
5  O  0 {9,S} {20,S}
6  O  0 {9,S} {21,S}
7  O  0 {3,S} {9,S}
8  O  0 {4,S} {9,S}
9  Si 0 {5,S} {6,S} {7,S} {8,S}
10 H  0 {1,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {2,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {3,S}
17 H  0 {3,S}
18 H  0 {4,S}
19 H  0 {4,S}
20 H  0 {5,S}
21 H  0 {6,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OSi(OC2H5)(OH)2
1  C  0 {3,S} {9,S} {10,S} {11,S}
2  C  1 {6,S} {12,S} {13,S}
3  C  0 {1,S} {7,S} {14,S} {15,S}
4  O  0 {8,S} {16,S}
5  O  0 {8,S} {17,S}
6  O  0 {2,S} {8,S}
7  O  0 {3,S} {8,S}
8  Si 0 {4,S} {5,S} {6,S} {7,S}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {1,S}
12 H  0 {2,S}
13 H  0 {2,S}
14 H  0 {3,S}
15 H  0 {3,S}
16 H  0 {4,S}
17 H  0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.995e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
Si(OC2H5)(OH)3
1  C  0 {2,S} {8,S} {9,S} {10,S}
2  C  0 {1,S} {6,S} {11,S} {12,S}
3  O  0 {7,S} {13,S}
4  O  0 {7,S} {14,S}
5  O  0 {7,S} {15,S}
6  O  0 {2,S} {7,S}
7  Si 0 {3,S} {4,S} {5,S} {6,S}
8  H  0 {1,S}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {4,S}
15 H  0 {5,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
Si(OH)4
1 O  0 {5,S} {6,S}
2 O  0 {5,S} {7,S}
3 O  0 {5,S} {8,S}
4 O  0 {5,S} {9,S}
5 Si 0 {1,S} {2,S} {3,S} {4,S}
6 H  0 {1,S}
7 H  0 {2,S}
8 H  0 {3,S}
9 H  0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (631000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
Si(OC2H5)(OH)3
1  C  0 {2,S} {8,S} {9,S} {10,S}
2  C  0 {1,S} {6,S} {11,S} {12,S}
3  O  0 {7,S} {13,S}
4  O  0 {7,S} {14,S}
5  O  0 {7,S} {15,S}
6  O  0 {2,S} {7,S}
7  Si 0 {3,S} {4,S} {5,S} {6,S}
8  H  0 {1,S}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {4,S}
15 H  0 {5,S}
""",
    product1 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    product2 = 
"""
O_Si(OC2H5)OH
1  C  0 {2,S} {4,S} {7,S} {8,S}
2  C  0 {1,S} {9,S} {10,S} {11,S}
3  Si 0 {4,S} {5,S} {6,D}
4  O  0 {1,S} {3,S}
5  O  0 {3,S} {12,S}
6  O  0 {3,D}
7  H  0 {1,S}
8  H  0 {1,S}
9  H  0 {2,S}
10 H  0 {2,S}
11 H  0 {2,S}
12 H  0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(501200000000.0, 's^-1'), n=0, Ea=(39.74, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
Si(OC2H5)(OH)3
1  C  0 {2,S} {8,S} {9,S} {10,S}
2  C  0 {1,S} {6,S} {11,S} {12,S}
3  O  0 {7,S} {13,S}
4  O  0 {7,S} {14,S}
5  O  0 {7,S} {15,S}
6  O  0 {2,S} {7,S}
7  Si 0 {3,S} {4,S} {5,S} {6,S}
8  H  0 {1,S}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {4,S}
15 H  0 {5,S}
""",
    product1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product2 = 
"""
O_Si(OH)2
1 Si 0 {2,S} {3,S} {4,D}
2 O  0 {1,S} {5,S}
3 O  0 {1,S} {6,S}
4 O  0 {1,D}
5 H  0 {2,S}
6 H  0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(501200000000.0, 's^-1'), n=0, Ea=(45.105, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
Si(OC2H5)(OH)3
1  C  0 {2,S} {8,S} {9,S} {10,S}
2  C  0 {1,S} {6,S} {11,S} {12,S}
3  O  0 {7,S} {13,S}
4  O  0 {7,S} {14,S}
5  O  0 {7,S} {15,S}
6  O  0 {2,S} {7,S}
7  Si 0 {3,S} {4,S} {5,S} {6,S}
8  H  0 {1,S}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {4,S}
15 H  0 {5,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OSi(OH)3
1  C  1 {5,S} {7,S} {8,S}
2  O  0 {6,S} {9,S}
3  O  0 {6,S} {10,S}
4  O  0 {6,S} {11,S}
5  O  0 {1,S} {6,S}
6  Si 0 {2,S} {3,S} {4,S} {5,S}
7  H  0 {1,S}
8  H  0 {1,S}
9  H  0 {2,S}
10 H  0 {3,S}
11 H  0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
O_Si(OC2H5)2
1  C  0 {3,S} {6,S} {9,S} {10,S}
2  C  0 {4,S} {7,S} {11,S} {12,S}
3  C  0 {1,S} {13,S} {14,S} {15,S}
4  C  0 {2,S} {16,S} {17,S} {18,S}
5  Si 0 {6,S} {7,S} {8,D}
6  O  0 {1,S} {5,S}
7  O  0 {2,S} {5,S}
8  O  0 {5,D}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {3,S}
15 H  0 {3,S}
16 H  0 {4,S}
17 H  0 {4,S}
18 H  0 {4,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
O_Si(OC2H5)OH
1  C  0 {2,S} {4,S} {7,S} {8,S}
2  C  0 {1,S} {9,S} {10,S} {11,S}
3  Si 0 {4,S} {5,S} {6,D}
4  O  0 {1,S} {3,S}
5  O  0 {3,S} {12,S}
6  O  0 {3,D}
7  H  0 {1,S}
8  H  0 {1,S}
9  H  0 {2,S}
10 H  0 {2,S}
11 H  0 {2,S}
12 H  0 {5,S}
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
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    reactant1 = 
"""
O_Si(OC2H5)2
1  C  0 {3,S} {6,S} {9,S} {10,S}
2  C  0 {4,S} {7,S} {11,S} {12,S}
3  C  0 {1,S} {13,S} {14,S} {15,S}
4  C  0 {2,S} {16,S} {17,S} {18,S}
5  Si 0 {6,S} {7,S} {8,D}
6  O  0 {1,S} {5,S}
7  O  0 {2,S} {5,S}
8  O  0 {5,D}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {3,S}
15 H  0 {3,S}
16 H  0 {4,S}
17 H  0 {4,S}
18 H  0 {4,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OSiO(OC2H5)
1  C  0 {3,S} {8,S} {9,S} {10,S}
2  C  1 {5,S} {11,S} {12,S}
3  C  0 {1,S} {6,S} {13,S} {14,S}
4  O  0 {7,D}
5  O  0 {2,S} {7,S}
6  O  0 {3,S} {7,S}
7  Si 0 {4,D} {5,S} {6,S}
8  H  0 {1,S}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
14 H  0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.995e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
O_Si(OC2H5)OH
1  C  0 {2,S} {4,S} {7,S} {8,S}
2  C  0 {1,S} {9,S} {10,S} {11,S}
3  Si 0 {4,S} {5,S} {6,D}
4  O  0 {1,S} {3,S}
5  O  0 {3,S} {12,S}
6  O  0 {3,D}
7  H  0 {1,S}
8  H  0 {1,S}
9  H  0 {2,S}
10 H  0 {2,S}
11 H  0 {2,S}
12 H  0 {5,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
O_Si(OH)2
1 Si 0 {2,S} {3,S} {4,D}
2 O  0 {1,S} {5,S}
3 O  0 {1,S} {6,S}
4 O  0 {1,D}
5 H  0 {2,S}
6 H  0 {3,S}
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
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
O_Si(OC2H5)OH
1  C  0 {2,S} {4,S} {7,S} {8,S}
2  C  0 {1,S} {9,S} {10,S} {11,S}
3  Si 0 {4,S} {5,S} {6,D}
4  O  0 {1,S} {3,S}
5  O  0 {3,S} {12,S}
6  O  0 {3,D}
7  H  0 {1,S}
8  H  0 {1,S}
9  H  0 {2,S}
10 H  0 {2,S}
11 H  0 {2,S}
12 H  0 {5,S}
""",
    product1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product2 = 
"""
SiO2
1 O  0 {3,D}
2 O  0 {3,D}
3 Si 0 {1,D} {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(158500000000.0, 's^-1'), n=0, Ea=(47.092, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
O_Si(OC2H5)OH
1  C  0 {2,S} {4,S} {7,S} {8,S}
2  C  0 {1,S} {9,S} {10,S} {11,S}
3  Si 0 {4,S} {5,S} {6,D}
4  O  0 {1,S} {3,S}
5  O  0 {3,S} {12,S}
6  O  0 {3,D}
7  H  0 {1,S}
8  H  0 {1,S}
9  H  0 {2,S}
10 H  0 {2,S}
11 H  0 {2,S}
12 H  0 {5,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OSiO(OH)
1 C  1 {4,S} {6,S} {7,S}
2 O  0 {5,S} {8,S}
3 O  0 {5,D}
4 O  0 {1,S} {5,S}
5 Si 0 {2,S} {3,D} {4,S}
6 H  0 {1,S}
7 H  0 {1,S}
8 H  0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
CH3OSi(OC2H5)2(OC2H3)
1  C  0 {5,D} {13,S} {14,S}
2  C  0 {6,S} {15,S} {16,S} {17,S}
3  C  0 {7,S} {18,S} {19,S} {20,S}
4  C  0 {8,S} {21,S} {22,S} {23,S}
5  C  0 {1,D} {9,S} {24,S}
6  C  0 {2,S} {10,S} {25,S} {26,S}
7  C  0 {3,S} {11,S} {27,S} {28,S}
8  O  0 {4,S} {12,S}
9  O  0 {5,S} {12,S}
10 O  0 {6,S} {12,S}
11 O  0 {7,S} {12,S}
12 Si 0 {8,S} {9,S} {10,S} {11,S}
13 H  0 {1,S}
14 H  0 {1,S}
15 H  0 {2,S}
16 H  0 {2,S}
17 H  0 {2,S}
18 H  0 {3,S}
19 H  0 {3,S}
20 H  0 {3,S}
21 H  0 {4,S}
22 H  0 {4,S}
23 H  0 {4,S}
24 H  0 {5,S}
25 H  0 {6,S}
26 H  0 {6,S}
27 H  0 {7,S}
28 H  0 {7,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH3OSi(OC2H5)(OC2H3)OH
1  C  0 {4,D} {11,S} {12,S}
2  C  0 {5,S} {13,S} {14,S} {15,S}
3  C  0 {7,S} {16,S} {17,S} {18,S}
4  C  0 {1,D} {8,S} {19,S}
5  C  0 {2,S} {9,S} {20,S} {21,S}
6  O  0 {10,S} {22,S}
7  O  0 {3,S} {10,S}
8  O  0 {4,S} {10,S}
9  O  0 {5,S} {10,S}
10 Si 0 {6,S} {7,S} {8,S} {9,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {2,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {3,S}
17 H  0 {3,S}
18 H  0 {3,S}
19 H  0 {4,S}
20 H  0 {5,S}
21 H  0 {5,S}
22 H  0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1000000000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2OSi(OC2H5)3 = CH3OSi(OC2H5)2(OC2H3) + H
CH2OSi(OC2H5)2OH = CH3OSi(OC2H5)(OC2H3)OH + H
CH2OSi(OC2H5)(OH)2 = CH3OSi(OC2H3)(OH)2 + H
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
CH3OSi(OC2H5)2(OC2H3)
1  C  0 {5,D} {13,S} {14,S}
2  C  0 {6,S} {15,S} {16,S} {17,S}
3  C  0 {7,S} {18,S} {19,S} {20,S}
4  C  0 {8,S} {21,S} {22,S} {23,S}
5  C  0 {1,D} {9,S} {24,S}
6  C  0 {2,S} {10,S} {25,S} {26,S}
7  C  0 {3,S} {11,S} {27,S} {28,S}
8  O  0 {4,S} {12,S}
9  O  0 {5,S} {12,S}
10 O  0 {6,S} {12,S}
11 O  0 {7,S} {12,S}
12 Si 0 {8,S} {9,S} {10,S} {11,S}
13 H  0 {1,S}
14 H  0 {1,S}
15 H  0 {2,S}
16 H  0 {2,S}
17 H  0 {2,S}
18 H  0 {3,S}
19 H  0 {3,S}
20 H  0 {3,S}
21 H  0 {4,S}
22 H  0 {4,S}
23 H  0 {4,S}
24 H  0 {5,S}
25 H  0 {6,S}
26 H  0 {6,S}
27 H  0 {7,S}
28 H  0 {7,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OSi(OC2H5)(OC2H3)(OCH3)
1  C  0 {5,D} {12,S} {13,S}
2  C  0 {6,S} {14,S} {15,S} {16,S}
3  C  1 {7,S} {17,S} {18,S}
4  C  0 {8,S} {19,S} {20,S} {21,S}
5  C  0 {1,D} {9,S} {22,S}
6  C  0 {2,S} {10,S} {23,S} {24,S}
7  O  0 {3,S} {11,S}
8  O  0 {4,S} {11,S}
9  O  0 {5,S} {11,S}
10 O  0 {6,S} {11,S}
11 Si 0 {7,S} {8,S} {9,S} {10,S}
12 H  0 {1,S}
13 H  0 {1,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {2,S}
17 H  0 {3,S}
18 H  0 {3,S}
19 H  0 {4,S}
20 H  0 {4,S}
21 H  0 {4,S}
22 H  0 {5,S}
23 H  0 {6,S}
24 H  0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.995e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
CH3OSi(OC2H5)(OC2H3)OH
1  C  0 {4,D} {11,S} {12,S}
2  C  0 {5,S} {13,S} {14,S} {15,S}
3  C  0 {7,S} {16,S} {17,S} {18,S}
4  C  0 {1,D} {8,S} {19,S}
5  C  0 {2,S} {9,S} {20,S} {21,S}
6  O  0 {10,S} {22,S}
7  O  0 {3,S} {10,S}
8  O  0 {4,S} {10,S}
9  O  0 {5,S} {10,S}
10 Si 0 {6,S} {7,S} {8,S} {9,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {2,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {3,S}
17 H  0 {3,S}
18 H  0 {3,S}
19 H  0 {4,S}
20 H  0 {5,S}
21 H  0 {5,S}
22 H  0 {6,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
CH3OSi(OC2H3)(OH)2
1  C  0 {3,D} {9,S} {10,S}
2  C  0 {6,S} {11,S} {12,S} {13,S}
3  C  0 {1,D} {7,S} {14,S}
4  O  0 {8,S} {15,S}
5  O  0 {8,S} {16,S}
6  O  0 {2,S} {8,S}
7  O  0 {3,S} {8,S}
8  Si 0 {4,S} {5,S} {6,S} {7,S}
9  H  0 {1,S}
10 H  0 {1,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {2,S}
14 H  0 {3,S}
15 H  0 {4,S}
16 H  0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501200000000000.0, 's^-1'),
        n = 0,
        Ea = (68.552, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2OSi(OC2H5)(OC2H3)(OCH3) = SI(OCH3)2(C2H3)2 + H
""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
CH3OSi(OC2H5)(OC2H3)OH
1  C  0 {4,D} {11,S} {12,S}
2  C  0 {5,S} {13,S} {14,S} {15,S}
3  C  0 {7,S} {16,S} {17,S} {18,S}
4  C  0 {1,D} {8,S} {19,S}
5  C  0 {2,S} {9,S} {20,S} {21,S}
6  O  0 {10,S} {22,S}
7  O  0 {3,S} {10,S}
8  O  0 {4,S} {10,S}
9  O  0 {5,S} {10,S}
10 Si 0 {6,S} {7,S} {8,S} {9,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {2,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {3,S}
17 H  0 {3,S}
18 H  0 {3,S}
19 H  0 {4,S}
20 H  0 {5,S}
21 H  0 {5,S}
22 H  0 {6,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OSi(OCH3)(OC2H3)OH
1  C  0 {4,D} {10,S} {11,S}
2  C  1 {6,S} {12,S} {13,S}
3  C  0 {7,S} {14,S} {15,S} {16,S}
4  C  0 {1,D} {8,S} {17,S}
5  O  0 {9,S} {18,S}
6  O  0 {2,S} {9,S}
7  O  0 {3,S} {9,S}
8  O  0 {4,S} {9,S}
9  Si 0 {5,S} {6,S} {7,S} {8,S}
10 H  0 {1,S}
11 H  0 {1,S}
12 H  0 {2,S}
13 H  0 {2,S}
14 H  0 {3,S}
15 H  0 {3,S}
16 H  0 {3,S}
17 H  0 {4,S}
18 H  0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+17, 's^-1'), n=0, Ea=(86.037, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
CH3OSi(OC2H5)(OC2H3)OH
1  C  0 {4,D} {11,S} {12,S}
2  C  0 {5,S} {13,S} {14,S} {15,S}
3  C  0 {7,S} {16,S} {17,S} {18,S}
4  C  0 {1,D} {8,S} {19,S}
5  C  0 {2,S} {9,S} {20,S} {21,S}
6  O  0 {10,S} {22,S}
7  O  0 {3,S} {10,S}
8  O  0 {4,S} {10,S}
9  O  0 {5,S} {10,S}
10 Si 0 {6,S} {7,S} {8,S} {9,S}
11 H  0 {1,S}
12 H  0 {1,S}
13 H  0 {2,S}
14 H  0 {2,S}
15 H  0 {2,S}
16 H  0 {3,S}
17 H  0 {3,S}
18 H  0 {3,S}
19 H  0 {4,S}
20 H  0 {5,S}
21 H  0 {5,S}
22 H  0 {6,S}
""",
    product1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product2 = 
"""
CH3OSi(O)OC2H3
1  C  0 {3,D} {8,S} {9,S}
2  C  0 {5,S} {10,S} {11,S} {12,S}
3  C  0 {1,D} {6,S} {13,S}
4  O  0 {7,D}
5  O  0 {2,S} {7,S}
6  O  0 {3,S} {7,S}
7  Si 0 {4,D} {5,S} {6,S}
8  H  0 {1,S}
9  H  0 {1,S}
10 H  0 {2,S}
11 H  0 {2,S}
12 H  0 {2,S}
13 H  0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(158500000000.0, 's^-1'), n=0, Ea=(45.105, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product1 = 
"""
C2H4
1 C 0 {2,D} {3,S} {4,S}
2 C 0 {1,D} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    product2 = 
"""
H2O
1 O 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (63100000000000.0, 's^-1'),
        n = 0,
        Ea = (66.167, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    reactant1 = 
"""
C2H5OH
1 C 0 {2,S} {4,S} {5,S} {6,S}
2 C 0 {1,S} {3,S} {7,S} {8,S}
3 O 0 {2,S} {9,S}
4 H 0 {1,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {2,S}
8 H 0 {2,S}
9 H 0 {3,S}
""",
    product1 = 
"""
CH3
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product2 = 
"""
CH2OH
1 C 1 {2,S} {3,S} {4,S}
2 O 0 {1,S} {5,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+16, 's^-1'), n=0, Ea=(83.057, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

