#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/TS_training"
shortDesc = u"Distances used to train group additivity values for TS geometries"
longDesc = u"""
Put interatomic distances for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

entry(
    index = 1,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  *2 C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *1 C u1 p0 c0  {2,S} {12,S} {13,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7  *3 H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3  *2 C u0 p0 c0  {4,S} {10,S} {11,S} {12,S}
4  *1 C u1 p0 c0  {1,S} {3,S} {13,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10 *3 H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.30172', 'd12': '1.49221', 'd13': '1.30285'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 2,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {5,S} {14,S} {15,S}
4     C u0 p0 c0  {2,S} {5,S} {10,S} {11,S}
5     C u0 p0 c0  {3,S} {4,S} {12,S} {13,S}
6  *1 C u1 p0 c0  {1,S} {16,S} {17,S}
7  *3 H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {5,S}
13    H u0 p0 c0  {5,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {6,S} {11,S} {12,S}
4     C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {6,S} {15,S} {16,S} {17,S}
6  *1 C u1 p0 c0  {3,S} {4,S} {5,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15 *3 H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.29485', 'd12': '1.48516', 'd13': '1.31517'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 3,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3  *4 C u0 p0 c0  {1,S} {5,S} {10,S} {11,S}
4     C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  *1 C u1 p0 c0  {3,S} {15,S} {16,S}
6  *3 H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
""",
    product1 = """
multiplicity 2
1  *4 C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {4,S} {5,S} {8,S} {9,S}
3  *2 C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0  {2,S} {13,S} {14,S} {15,S}
5  *1 C u1 p0 c0  {1,S} {2,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10 *3 H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.40190', 'd12': '2.22164', 'd13': '1.41346'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 4,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {8,S} {9,S} {10,S}
3  *1 C u1 p0 c0  {1,S} {4,S} {11,S}
4  *4 O u0 p2 c0  {3,S} {5,S}
5  *2 O u0 p2 c0  {4,S} {12,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12 *3 H u0 p0 c0  {5,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  *2 C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *4 O u0 p2 c0  {2,S} {12,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7  *3 H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12 *1 O u1 p2 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.28316', 'd12': '2.03811', 'd13': '1.33202'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 5,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {11,S} {12,S}
2  *2 C u0 p0 c0  {1,S} {3,S} {8,S} {13,S}
3  *5 C u0 p0 c0  {2,S} {5,S} {14,S} {15,S}
4     C u0 p0 c0  {1,S} {6,S} {9,S} {10,S}
5  *4 C u0 p0 c0  {3,S} {7,S} {16,S} {17,S}
6     C u0 p0 c0  {4,S} {18,S} {19,S} {20,S}
7  *1 C u1 p0 c0  {5,S} {21,S} {22,S}
8  *3 H u0 p0 c0  {2,S}
9     H u0 p0 c0  {4,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {1,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {5,S} {8,S} {9,S}
2  *5 C u0 p0 c0  {4,S} {6,S} {10,S} {11,S}
3     C u0 p0 c0  {1,S} {7,S} {12,S} {13,S}
4  *4 C u0 p0 c0  {2,S} {7,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {17,S} {18,S} {19,S}
6  *2 C u0 p0 c0  {2,S} {16,S} {20,S} {21,S}
7  *1 C u1 p0 c0  {3,S} {4,S} {22,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16 *3 H u0 p0 c0  {6,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.36152', 'd12': '2.52790', 'd13': '1.39272'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 6,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  *5 C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4  *4 C u0 p0 c0  {2,S} {9,S} {13,S} {14,S}
5  *3 H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9  *1 O u1 p2 c0  {4,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,S} {4,S} {6,S} {7,S}
2  *5 C u0 p0 c0  {1,S} {5,S} {8,S} {9,S}
3     C u0 p0 c0  {4,S} {10,S} {11,S} {12,S}
4  *1 C u1 p0 c0  {1,S} {3,S} {13,S}
5  *2 O u0 p2 c0  {2,S} {14,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14 *3 H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.27828', 'd12': '2.36998', 'd13': '1.29626'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 7,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {4,S} {5,S} {7,S}
2  *5 C u0 p0 c0  {1,S} {3,S} {8,S} {9,S}
3     C u0 p0 c0  {2,S} {6,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6  *4 C u0 p0 c0  {3,S} {12,S} {19,S} {20,S}
7  *3 H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12 *1 O u1 p2 c0  {6,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {8,S} {9,S}
2  *4 C u0 p0 c0  {1,S} {6,S} {10,S} {11,S}
3  *5 C u0 p0 c0  {1,S} {7,S} {12,S} {13,S}
4     C u0 p0 c0  {6,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0  {6,S} {17,S} {18,S} {19,S}
6  *1 C u1 p0 c0  {2,S} {4,S} {5,S}
7  *2 O u0 p2 c0  {3,S} {20,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20 *3 H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.24586', 'd12': '2.50266', 'd13': '1.31554'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 8,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {5,S} {9,S}
2     C u0 p0 c0  {1,S} {4,S} {14,S} {15,S}
3  *5 C u0 p0 c0  {1,S} {7,S} {10,S} {11,S}
4     C u0 p0 c0  {2,S} {6,S} {12,S} {13,S}
5  *4 C u0 p0 c0  {1,S} {8,S} {16,S} {17,S}
6     C u0 p0 c0  {4,S} {8,S} {18,S} {19,S}
7  *2 C u0 p0 c0  {3,S} {20,S} {21,S} {22,S}
8  *1 C u1 p0 c0  {5,S} {6,S} {23,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {2,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20 *3 H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {9,S}
2  *5 C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {6,S} {18,S} {19,S}
4  *2 C u0 p0 c0  {2,S} {5,S} {10,S} {13,S}
5     C u0 p0 c0  {4,S} {6,S} {14,S} {15,S}
6     C u0 p0 c0  {3,S} {5,S} {16,S} {17,S}
7  *4 C u0 p0 c0  {1,S} {8,S} {20,S} {21,S}
8  *1 C u1 p0 c0  {7,S} {22,S} {23,S}
9     H u0 p0 c0  {1,S}
10 *3 H u0 p0 c0  {4,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {5,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {8,S}
23    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.33168', 'd12': '2.64783', 'd13': '1.38878'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 9,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {9,S} {10,S}
2  *4 C u0 p0 c0  {1,S} {6,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {7,S} {13,S} {14,S}
4     C u0 p0 c0  {6,S} {15,S} {16,S} {17,S}
5     C u0 p0 c0  {6,S} {18,S} {19,S} {20,S}
6  *1 C u1 p0 c0  {2,S} {4,S} {5,S}
7  *5 O u0 p2 c0  {3,S} {8,S}
8  *2 O u0 p2 c0  {7,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21 *3 H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {5,S} {6,S} {8,S}
2  *5 C u0 p0 c0  {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0  {2,S} {4,S} {11,S} {12,S}
4     C u0 p0 c0  {3,S} {7,S} {13,S} {14,S}
5     C u0 p0 c0  {1,S} {15,S} {16,S} {17,S}
6     C u0 p0 c0  {1,S} {18,S} {19,S} {20,S}
7  *4 O u0 p2 c0  {4,S} {21,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21 *1 O u1 p2 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.19533', 'd12': '2.51644', 'd13': '1.34348'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 10,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {4,S} {9,S}
2     C u0 p0 c0  {1,S} {5,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {6,S} {14,S} {15,S}
4  *5 C u0 p0 c0  {1,S} {7,S} {10,S} {11,S}
5  *4 C u0 p0 c0  {2,S} {8,S} {16,S} {17,S}
6     C u0 p0 c0  {3,S} {8,S} {18,S} {19,S}
7  *2 C u0 p0 c0  {4,S} {20,S} {21,S} {22,S}
8  *1 C u1 p0 c0  {5,S} {6,S} {23,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20 *3 H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {9,S}
2     C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {6,S} {18,S} {19,S}
4  *5 C u0 p0 c0  {2,S} {5,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {4,S} {6,S} {10,S} {15,S}
6     C u0 p0 c0  {3,S} {5,S} {16,S} {17,S}
7  *4 C u0 p0 c0  {1,S} {8,S} {20,S} {21,S}
8  *1 C u1 p0 c0  {7,S} {22,S} {23,S}
9     H u0 p0 c0  {1,S}
10 *3 H u0 p0 c0  {5,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {8,S}
23    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.37209', 'd12': '2.65192', 'd13': '1.32587'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 11,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {10,S} {11,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {5,S} {12,S} {13,S}
4  *4 C u0 p0 c0  {2,S} {6,S} {14,S} {15,S}
5  *5 C u0 p0 c0  {3,S} {7,S} {16,S} {17,S}
6  *1 C u1 p0 c0  {4,S} {18,S} {19,S}
7  *2 O u0 p2 c0  {5,S} {20,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20 *3 H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {9,S} {10,S}
2     C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3  *5 C u0 p0 c0  {1,S} {5,S} {7,S} {8,S}
4     C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {3,S} {16,S} {17,S} {18,S}
6  *4 C u0 p0 c0  {4,S} {15,S} {19,S} {20,S}
7     H u0 p0 c0  {3,S}
8     H u0 p0 c0  {3,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15 *1 O u1 p2 c0  {6,S}
16 *3 H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.24532', 'd12': '2.50531', 'd13': '1.27498'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 12,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {8,S} {9,S}
2     C u0 p0 c0  {1,S} {4,S} {10,S} {11,S}
3  *4 C u0 p0 c0  {1,S} {5,S} {12,S} {13,S}
4     C u0 p0 c0  {2,S} {6,S} {14,S} {15,S}
5  *1 C u1 p0 c0  {3,S} {16,S} {17,S}
6  *5 O u0 p2 c0  {4,S} {7,S}
7  *2 O u0 p2 c0  {6,S} {18,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18 *3 H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {9,S} {10,S}
2     C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3  *5 C u0 p0 c0  {1,S} {5,S} {7,S} {8,S}
4     C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {3,S} {15,S} {16,S} {17,S}
6  *4 O u0 p2 c0  {4,S} {18,S}
7     H u0 p0 c0  {3,S}
8     H u0 p0 c0  {3,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15 *3 H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18 *1 O u1 p2 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.14855', 'd12': '2.53680', 'd13': '1.40019'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation.""",
    longDesc = 
u"""
""",
)

entry(
    index = 13,
    reactant1 = """
multiplicity 2
1 *2 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4 *3 H u0 p0 c0  {1,S}
5 *1 O u1 p2 c0  {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 *2 O u0 p2 c0  {1,S} {5,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5 *3 H u0 p0 c0  {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.276283, 'd12': 1.38927, 'd13': 1.203442},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 14,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *1 C u1 p0 c0  {1,S} {9,S} {10,S}
4     H u0 p0 c0  {1,S}
5  *3 H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2  *2 C u0 p0 c0  {3,S} {4,S} {8,S} {9,S}
3  *1 C u1 p0 c0  {1,S} {2,S} {10,S}
4  *3 H u0 p0 c0  {2,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30064, 'd12': 1.492365, 'd13': 1.30311},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 15,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0  {1,S} {4,D} {7,S}
3  *1 C u1 p0 c0  {1,S} {8,S} {9,S}
4     C u0 p0 c0  {2,D} {10,S} {11,S}
5     H u0 p0 c0  {1,S}
6  *3 H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {3,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {5,S} {6,S} {7,S}
2  *1 C u1 p0 c0  {1,S} {3,S} {8,S}
3     C u0 p0 c0  {2,S} {4,D} {9,S}
4     C u0 p0 c0  {3,D} {10,S} {11,S}
5  *3 H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.256171, 'd12': 1.489543, 'd13': 1.365329},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 16,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *1 C u1 p0 c0  {1,S} {12,S} {13,S}
5  *3 H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {4,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0  {4,S} {9,S} {10,S} {11,S}
3  *2 C u0 p0 c0  {4,S} {5,S} {12,S} {13,S}
4  *1 C u1 p0 c0  {1,S} {2,S} {3,S}
5  *3 H u0 p0 c0  {3,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.302738, 'd12': 1.493897, 'd13': 1.308689},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 17,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3  *2 C u0 p0 c0  {1,S} {5,S} {10,S} {11,S}
4     C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  *1 C u1 p0 c0  {3,S} {15,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11 *3 H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {5,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4  *2 C u0 p0 c0  {5,S} {13,S} {14,S} {15,S}
5  *1 C u1 p0 c0  {2,S} {4,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13 *3 H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.297544, 'd12': 1.49488, 'd13': 1.303078},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 18,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {5,S} {10,S} {11,S}
4  *2 C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5     O u0 p2 c0  {3,S} {15,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13 *3 H u0 p0 c0  {4,S}
14 *1 O u1 p2 c0  {4,S}
15    H u0 p0 c0  {5,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {5,S} {11,S} {12,S}
4  *1 C u1 p0 c0  {2,S} {6,S} {13,S}
5     O u0 p2 c0  {3,S} {14,S}
6  *2 O u0 p2 c0  {4,S} {15,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {5,S}
15 *3 H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27819, 'd12': 1.39608, 'd13': 1.208513},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 19,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {9,S} {10,S}
2     C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {6,S} {13,S} {14,S}
4     C u0 p0 c0  {2,S} {8,S} {15,S} {16,S}
5  *2 C u0 p0 c0  {7,S} {8,S} {17,S} {18,S}
6     C u0 p0 c0  {3,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0  {5,S} {22,S} {23,S} {24,S}
8  *1 C u1 p0 c0  {4,S} {5,S} {25,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {5,S}
18 *3 H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {7,S}
25    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {9,S} {10,S}
2     C u0 p0 c0  {1,S} {3,S} {11,S} {12,S}
3     C u0 p0 c0  {2,S} {5,S} {15,S} {16,S}
4     C u0 p0 c0  {1,S} {6,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {3,S} {8,S} {17,S} {18,S}
6     C u0 p0 c0  {4,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0  {8,S} {22,S} {23,S} {24,S}
8  *1 C u1 p0 c0  {5,S} {7,S} {25,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17 *3 H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {7,S}
25    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.305005, 'd12': 1.495163, 'd13': 1.305369},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 20,
    reactant1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,B} {5,S} {8,B}
2     C u0 p0 c0  {1,B} {3,B} {9,S}
3     C u0 p0 c0  {2,B} {4,B} {10,S}
4     C u0 p0 c0  {3,B} {6,B} {12,S}
5  *5 C u0 p0 c0  {1,S} {7,D} {11,S}
6     C u0 p0 c0  {4,B} {8,B} {13,S}
7  *2 C u0 p0 c0  {5,D} {14,S} {15,S}
8  *1 C u1 p0 c0  {1,B} {6,B}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {5,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {6,S}
14    H u0 p0 c0  {7,S}
15 *3 H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,B} {3,B} {7,S}
2     C u0 p0 c0  {1,B} {4,B} {10,S}
3  *2 C u0 p0 c0  {1,B} {6,B} {9,S}
4     C u0 p0 c0  {2,B} {5,B} {11,S}
5     C u0 p0 c0  {4,B} {6,B} {12,S}
6     C u0 p0 c0  {3,B} {5,B} {13,S}
7  *5 C u0 p0 c0  {1,S} {8,D} {14,S}
8  *1 C u1 p0 c0  {7,D} {15,S}
9  *3 H u0 p0 c0  {3,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {5,S}
13    H u0 p0 c0  {6,S}
14    H u0 p0 c0  {7,S}
15    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.387024, 'd12': 2.451028, 'd13': 1.385279},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 21,
    reactant1 = """
multiplicity 2
1 *2 C u0 p0 c0  {2,S} {3,D} {6,S}
2 *1 C u1 p0 c0  {1,S} {4,S} {5,S}
3    O u0 p2 c0  {1,D}
4    H u0 p0 c0  {2,S}
5    H u0 p0 c0  {2,S}
6 *3 H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1 *2 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 C u1 p0 c0  {1,S} {6,D}
3 *3 H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    O u0 p2 c0  {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.286564, 'd12': 1.399541, 'd13': 1.465925},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 22,
    reactant1 = """
multiplicity 2
1 *2 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0  {3,D} {7,S} {8,S}
3 *1 C u1 p0 c0  {1,S} {2,D}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *3 H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1 *2 C u0 p0 c0  {2,S} {3,D} {4,S}
2 *1 C u1 p0 c0  {1,S} {5,S} {6,S}
3    C u0 p0 c0  {1,D} {7,S} {8,S}
4 *3 H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {3,S}
8    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.337938, 'd12': 1.424615, 'd13': 1.299016},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 23,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {5,S} {11,S} {12,S}
4  *2 C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5     C u0 p0 c0  {3,S} {15,S} {16,S} {17,S}
6  *1 C u1 p0 c0  {4,S} {18,S} {19,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14 *3 H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {6,S} {11,S} {12,S}
4     C u0 p0 c0  {2,S} {13,S} {14,S} {15,S}
5  *2 C u0 p0 c0  {6,S} {16,S} {17,S} {18,S}
6  *1 C u1 p0 c0  {3,S} {5,S} {19,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16 *3 H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.300834, 'd12': 1.492938, 'd13': 1.302398},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 24,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {6,S} {8,S}
2  *2 C u0 p0 c0  {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {1,S} {2,S} {19,D}
7  *1 C u1 p0 c0  {2,S} {20,S} {21,S}
8     H u0 p0 c0  {1,S}
9  *3 H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    O u0 p2 c0  {6,D}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
4  *2 C u0 p0 c0  {6,S} {15,S} {18,S} {19,S}
5     C u0 p0 c0  {6,S} {16,S} {17,S} {20,S}
6  *1 C u1 p0 c0  {4,S} {5,S} {7,S}
7     C u0 p0 c0  {1,S} {6,S} {21,D}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15 *3 H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {5,S}
21    O u0 p2 c0  {7,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.24362, 'd12': 1.48173, 'd13': 1.37606},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 25,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {5,S} {10,S}
2  *5 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3  *6 C u0 p0 c0  {1,S} {2,S} {8,S} {9,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0  {1,S} {15,S} {16,S} {17,S}
6     C u0 p0 c0  {2,S} {20,S} {21,S} {22,S}
7  *2 C u0 p0 c0  {2,S} {18,S} {19,S} {23,S}
8     O u0 p2 c0  {3,S} {24,S}
9  *4 O u0 p2 c0  {3,S} {25,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {6,S}
23 *3 H u0 p0 c0  {7,S}
24    H u0 p0 c0  {8,S}
25 *1 O u1 p2 c0  {9,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {5,S} {11,S}
2  *4 C u0 p0 c0  {1,S} {3,S} {8,S} {9,S}
3  *5 C u0 p0 c0  {2,S} {6,S} {7,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {3,S} {19,S} {20,S} {21,S}
7  *1 C u1 p0 c0  {3,S} {22,S} {23,S}
8  *6 O u0 p2 c0  {2,S} {10,S}
9     O u0 p2 c0  {2,S} {24,S}
10 *2 O u0 p2 c0  {8,S} {25,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {9,S}
25 *3 H u0 p0 c0  {10,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4027, 'd12': 2.47997, 'd13': 1.14812},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 26,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {5,S} {10,S}
2  *5 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3  *4 C u0 p0 c0  {1,S} {2,S} {8,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {2,S} {21,S} {22,S} {23,S}
7  *2 C u0 p0 c0  {2,S} {19,S} {20,S} {24,S}
8     O u0 p2 c0  {3,S} {9,S}
9     O u0 p2 c0  {8,S} {25,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12 *1 O u1 p2 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {6,S}
23    H u0 p0 c0  {6,S}
24 *3 H u0 p0 c0  {7,S}
25    H u0 p0 c0  {9,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {5,S} {11,S}
2  *5 C u0 p0 c0  {1,S} {3,S} {8,S} {9,S}
3  *4 C u0 p0 c0  {2,S} {6,S} {7,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {3,S} {19,S} {20,S} {21,S}
7  *1 C u1 p0 c0  {3,S} {22,S} {23,S}
8     O u0 p2 c0  {2,S} {10,S}
9  *2 O u0 p2 c0  {2,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24 *3 H u0 p0 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28678, 'd12': 2.3547, 'd13': 1.28756},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 27,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {6,S} {8,S}
2  *2 C u0 p0 c0  {5,S} {6,S} {7,S} {10,S}
3     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0  {1,S} {11,S} {12,S} {19,S}
5     C u0 p0 c0  {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {1,S} {2,S} {20,D}
7  *1 C u1 p0 c0  {2,S} {21,S} {22,S}
8     O u0 p2 c0  {1,S} {9,S}
9     O u0 p2 c0  {8,S} {23,S}
10 *3 H u0 p0 c0  {2,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {4,S}
20    O u0 p2 c0  {6,D}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {9,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4  *2 C u0 p0 c0  {6,S} {16,S} {19,S} {20,S}
5     C u0 p0 c0  {6,S} {17,S} {18,S} {21,S}
6  *1 C u1 p0 c0  {4,S} {5,S} {7,S}
7     C u0 p0 c0  {1,S} {6,S} {22,D}
8     O u0 p2 c0  {1,S} {9,S}
9     O u0 p2 c0  {8,S} {23,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16 *3 H u0 p0 c0  {4,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {5,S}
22    O u0 p2 c0  {7,D}
23    H u0 p0 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23875, 'd12': 1.48045, 'd13': 1.38564},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 28,
    reactant1 = """
multiplicity 2
1  *6 C u0 p0 c0  {4,S} {5,S} {7,S} {9,S}
2  *2 C u0 p0 c0  {3,S} {6,S} {8,S} {11,S}
3  *5 C u0 p0 c0  {2,S} {7,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {1,S} {14,S} {15,S} {21,S}
6     C u0 p0 c0  {2,S} {19,S} {20,S} {22,S}
7  *7 C u0 p0 c0  {1,S} {3,S} {23,D}
8     O u0 p2 c0  {2,S} {10,S}
9  *4 O u0 p2 c0  {1,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11 *3 H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {5,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {6,S}
23    O u0 p2 c0  {7,D}
24 *1 O u1 p2 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    product1 = """
multiplicity 2
1  *5 C u0 p0 c0  {3,S} {4,S} {7,S} {8,S}
2  *6 C u0 p0 c0  {6,S} {7,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
4     C u0 p0 c0  {1,S} {17,S} {18,S} {19,S}
5     C u0 p0 c0  {6,S} {20,S} {21,S} {22,S}
6  *1 C u1 p0 c0  {2,S} {5,S} {9,S}
7  *4 C u0 p0 c0  {1,S} {2,S} {23,D}
8  *7 O u0 p2 c0  {1,S} {10,S}
9     O u0 p2 c0  {6,S} {11,S}
10 *2 O u0 p2 c0  {8,S} {25,S}
11    O u0 p2 c0  {9,S} {24,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {5,S}
23    O u0 p2 c0  {7,D}
24    H u0 p0 c0  {11,S}
25 *3 H u0 p0 c0  {10,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3435, 'd12': 2.48335, 'd13': 1.19085},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 29,
    reactant1 = """
multiplicity 2
1  *6 C u0 p0 c0  {4,S} {5,S} {7,S} {9,S}
2  *2 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3     C u0 p0 c0  {2,S} {8,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {1,S} {14,S} {15,S} {21,S}
6     C u0 p0 c0  {2,S} {19,S} {20,S} {22,S}
7  *5 C u0 p0 c0  {1,S} {2,S} {23,D}
8     O u0 p2 c0  {3,S} {10,S}
9  *4 O u0 p2 c0  {1,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11 *3 H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {5,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {6,S}
23    O u0 p2 c0  {7,D}
24 *1 O u1 p2 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    product1 = """
multiplicity 2
1  *4 C u0 p0 c0  {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0  {6,S} {9,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
4     C u0 p0 c0  {1,S} {17,S} {18,S} {19,S}
5     C u0 p0 c0  {6,S} {20,S} {21,S} {22,S}
6  *1 C u1 p0 c0  {2,S} {5,S} {7,S}
7  *5 C u0 p0 c0  {1,S} {6,S} {23,D}
8  *6 O u0 p2 c0  {1,S} {11,S}
9     O u0 p2 c0  {2,S} {10,S}
10    O u0 p2 c0  {9,S} {24,S}
11 *2 O u0 p2 c0  {8,S} {25,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {5,S}
23    O u0 p2 c0  {7,D}
24    H u0 p0 c0  {10,S}
25 *3 H u0 p0 c0  {11,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35819, 'd12': 2.46075, 'd13': 1.20035},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 30,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {4,S} {5,S} {7,S} {8,S}
2  *2 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3  *5 C u0 p0 c0  {2,S} {9,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {18,S} {19,S} {20,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {22,S}
6     C u0 p0 c0  {2,S} {14,S} {15,S} {21,S}
7     C u0 p0 c0  {1,S} {2,S} {23,D}
8     O u0 p2 c0  {1,S} {10,S}
9  *4 O u0 p2 c0  {3,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11 *3 H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {6,S}
15    H u0 p0 c0  {6,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {5,S}
23    O u0 p2 c0  {7,D}
24 *1 O u1 p2 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
3     C u0 p0 c0  {1,S} {17,S} {18,S} {19,S}
4  *4 C u0 p0 c0  {6,S} {9,S} {12,S} {13,S}
5     C u0 p0 c0  {6,S} {20,S} {21,S} {22,S}
6  *1 C u1 p0 c0  {4,S} {5,S} {7,S}
7     C u0 p0 c0  {1,S} {6,S} {23,D}
8     O u0 p2 c0  {1,S} {10,S}
9  *5 O u0 p2 c0  {4,S} {11,S}
10    O u0 p2 c0  {8,S} {24,S}
11 *2 O u0 p2 c0  {9,S} {25,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {2,S}
16    H u0 p0 c0  {2,S}
17    H u0 p0 c0  {3,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {5,S}
23    O u0 p2 c0  {7,D}
24    H u0 p0 c0  {10,S}
25 *3 H u0 p0 c0  {11,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37066, 'd12': 2.41589, 'd13': 1.24608},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 31,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {7,S} {8,S}
2  *5 C u0 p0 c0  {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0  {2,S} {19,S} {20,S} {21,S}
6  *2 C u0 p0 c0  {2,S} {17,S} {18,S} {22,S}
7     C u0 p0 c0  {1,S} {2,S} {23,D}
8     O u0 p2 c0  {1,S} {10,S}
9  *4 O u0 p2 c0  {2,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22 *3 H u0 p0 c0  {6,S}
23    O u0 p2 c0  {7,D}
24 *1 O u1 p2 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {6,S} {8,S}
2  *4 C u0 p0 c0  {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
4     C u0 p0 c0  {1,S} {15,S} {16,S} {17,S}
5     C u0 p0 c0  {2,S} {18,S} {19,S} {20,S}
6     C u0 p0 c0  {1,S} {2,S} {21,D}
7  *1 C u1 p0 c0  {2,S} {22,S} {23,S}
8     O u0 p2 c0  {1,S} {10,S}
9  *5 O u0 p2 c0  {2,S} {11,S}
10    O u0 p2 c0  {8,S} {24,S}
11 *2 O u0 p2 c0  {9,S} {25,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21    O u0 p2 c0  {6,D}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {10,S}
25 *3 H u0 p0 c0  {11,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42006, 'd12': 2.40999, 'd13': 1.1726},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 32,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {4,S} {5,S} {6,S} {10,S}
2  *4 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3     C u0 p0 c0  {2,S} {8,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {1,S} {14,S} {15,S} {19,S}
6  *5 C u0 p0 c0  {1,S} {2,S} {20,D}
7  *1 C u1 p0 c0  {2,S} {21,S} {22,S}
8     O u0 p2 c0  {3,S} {9,S}
9     O u0 p2 c0  {8,S} {23,S}
10 *3 H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {5,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {5,S}
20    O u0 p2 c0  {6,D}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {9,S}
""",
    product1 = """
multiplicity 2
1  *5 C u0 p0 c0  {2,S} {3,S} {7,S} {10,S}
2     C u0 p0 c0  {1,S} {8,S} {11,S} {12,S}
3  *2 C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0  {6,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {6,S} {19,S} {20,S} {21,S}
6  *1 C u1 p0 c0  {4,S} {5,S} {7,S}
7  *4 C u0 p0 c0  {1,S} {6,S} {22,D}
8     O u0 p2 c0  {2,S} {9,S}
9     O u0 p2 c0  {8,S} {23,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15 *3 H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22    O u0 p2 c0  {7,D}
23    H u0 p0 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34448, 'd12': 2.54737, 'd13': 1.40945},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 33,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {7,S} {8,S} {15,S}
2     H u0 p0 c0  {11,S}
3     H u0 p0 c0  {11,S}
4     H u0 p0 c0  {13,S}
5     H u0 p0 c0  {13,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     O u0 p2 c0  {18,D}
10    H u0 p0 c0  {19,S}
11    C u0 p0 c0  {2,S} {3,S} {12,S} {19,S}
12    H u0 p0 c0  {11,S}
13    C u0 p0 c0  {4,S} {5,S} {14,S} {15,S}
14    H u0 p0 c0  {13,S}
15 *2 C u0 p0 c0  {1,S} {13,S} {16,S} {18,S}
16 *3 H u0 p0 c0  {15,S}
17 *4 O u0 p2 c0  {19,S} {20,S}
18 *5 C u0 p0 c0  {9,D} {15,S} {19,S}
19 *6 C u0 p0 c0  {10,S} {11,S} {17,S} {18,S}
20 *1 O u1 p2 c0  {17,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {5,S} {6,S} {7,S} {19,S}
2     C u0 p0 c0  {8,S} {9,S} {10,S} {20,S}
3     C u0 p0 c0  {11,S} {12,S} {13,S} {20,S}
4     H u0 p0 c0  {19,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    O u0 p2 c0  {17,D}
15 *2 O u0 p2 c0  {16,S} {18,S}
16 *3 H u0 p0 c0  {15,S}
17 *5 C u0 p0 c0  {14,D} {19,S} {20,S}
18 *6 O u0 p2 c0  {15,S} {19,S}
19 *4 C u0 p0 c0  {1,S} {4,S} {17,S} {18,S}
20 *1 C u1 p0 c0  {2,S} {3,S} {17,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3516, 'd12': 2.47, 'd13': 1.2065},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 34,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {14,S}
4     C u0 p0 c0  {6,S} {17,S} {18,S} {19,S}
5  *2 C u0 p0 c0  {6,S} {15,S} {16,S} {20,S}
6  *5 C u0 p0 c0  {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0  {1,S} {6,D} {21,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20 *3 H u0 p0 c0  {5,S}
21 *1 O u1 p2 c0  {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {9,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0  {5,S} {16,S} {17,S} {18,S}
5  *4 C u0 p0 c0  {4,S} {6,D} {7,S}
6  *5 C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {5,S} {19,S} {20,S}
8  *2 O u0 p2 c0  {6,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21 *3 H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42329, 'd12': 2.44455, 'd13': 1.25908},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 35,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {7,S} {8,S} {21,S}
2     H u0 p0 c0  {12,S}
3     H u0 p0 c0  {12,S}
4     H u0 p0 c0  {10,S}
5     H u0 p0 c0  {10,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     O u0 p2 c0  {20,D}
10    C u0 p0 c0  {4,S} {5,S} {11,S} {21,S}
11    H u0 p0 c0  {10,S}
12    C u0 p0 c0  {2,S} {3,S} {13,S} {17,S}
13    H u0 p0 c0  {12,S}
14    O u0 p2 c0  {15,S} {16,S}
15    H u0 p0 c0  {14,S}
16    O u0 p2 c0  {14,S} {17,S}
17 *2 C u0 p0 c0  {12,S} {16,S} {18,S} {20,S}
18 *3 H u0 p0 c0  {17,S}
19 *4 O u0 p2 c0  {21,S} {22,S}
20 *5 C u0 p0 c0  {9,D} {17,S} {21,S}
21 *6 C u0 p0 c0  {1,S} {10,S} {19,S} {20,S}
22 *1 O u1 p2 c0  {19,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {7,S} {8,S} {21,S}
2     C u0 p0 c0  {9,S} {10,S} {11,S} {21,S}
3     C u0 p0 c0  {12,S} {13,S} {14,S} {22,S}
4     O u0 p2 c0  {5,S} {22,S}
5     O u0 p2 c0  {4,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    O u0 p2 c0  {19,D}
16    H u0 p0 c0  {5,S}
17 *2 O u0 p2 c0  {18,S} {20,S}
18 *3 H u0 p0 c0  {17,S}
19 *5 C u0 p0 c0  {15,D} {21,S} {22,S}
20 *6 O u0 p2 c0  {17,S} {21,S}
21 *4 C u0 p0 c0  {1,S} {2,S} {19,S} {20,S}
22 *1 C u1 p0 c0  {3,S} {4,S} {19,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33701, 'd12': 2.46273, 'd13': 1.20893},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 36,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {14,S}
4     C u0 p0 c0  {6,S} {17,S} {18,S} {19,S}
5     C u0 p0 c0  {6,S} {15,S} {16,S} {20,S}
6     C u0 p0 c0  {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0  {1,S} {6,D} {21,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {5,S}
21 *1 O u1 p2 c0  {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {9,S} {10,S} {11,S}
2     C u0 p0 c0  {6,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0  {5,S} {15,S} {16,S} {17,S}
4     C u0 p0 c0  {5,S} {18,S} {19,S} {20,S}
5     C u0 p0 c0  {3,S} {4,S} {7,D}
6  *1 C u1 p0 c0  {1,S} {2,S} {7,S}
7  *4 C u0 p0 c0  {5,D} {6,S} {8,S}
8  *2 O u0 p2 c0  {7,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {3,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {4,S}
21 *3 H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34765, 'd12': 2.11212, 'd13': 1.30528},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 37,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {6,S} {9,S}
2     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {15,S}
4     C u0 p0 c0  {5,S} {16,S} {17,S} {18,S}
5  *4 C u0 p0 c0  {4,S} {6,D} {7,S}
6  *5 C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {5,S} {19,S} {20,S}
8     O u0 p2 c0  {6,S} {21,S}
9  *3 H u0 p0 c0  {1,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {10,S} {11,S} {12,S}
2     C u0 p0 c0  {6,S} {13,S} {14,S} {15,S}
3  *2 C u0 p0 c0  {5,S} {9,S} {18,S} {19,S}
4     C u0 p0 c0  {5,S} {16,S} {17,S} {20,S}
5  *5 C u0 p0 c0  {3,S} {4,S} {7,D}
6  *1 C u1 p0 c0  {1,S} {2,S} {7,S}
7  *4 C u0 p0 c0  {5,D} {6,S} {8,S}
8     O u0 p2 c0  {7,S} {21,S}
9  *3 H u0 p0 c0  {3,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {1,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {2,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35287, 'd12': 2.53478, 'd13': 1.40511},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 38,
    reactant1 = """
multiplicity 2
1  *6 C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {15,S}
4     C u0 p0 c0  {6,S} {18,S} {19,S} {20,S}
5     C u0 p0 c0  {6,S} {16,S} {17,S} {21,S}
6     C u0 p0 c0  {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0  {1,S} {6,D} {22,S}
8  *5 O u0 p2 c0  {1,S} {9,S}
9  *2 O u0 p2 c0  {8,S} {23,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {5,S}
22 *1 O u1 p2 c0  {7,S}
23 *3 H u0 p0 c0  {9,S}
""",
    product1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0  {6,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {6,S} {19,S} {20,S} {21,S}
6     C u0 p0 c0  {4,S} {5,S} {7,D}
7  *6 C u0 p0 c0  {1,S} {6,D} {9,S}
8  *5 O u0 p2 c0  {1,S} {22,S}
9  *2 O u0 p2 c0  {7,S} {23,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22 *1 O u1 p2 c0  {8,S}
23 *3 H u0 p0 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29418, 'd12': 2.34294, 'd13': 1.1198},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 39,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {5,S} {6,S} {8,S}
2     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0  {4,S} {12,S} {13,S} {14,S}
4     C u0 p0 c0  {3,S} {5,S} {7,D}
5     C u0 p0 c0  {1,S} {4,S} {15,D}
6  *1 C u1 p0 c0  {1,S} {16,S} {17,S}
7     C u0 p0 c0  {4,D} {18,S} {19,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    O u0 p2 c0  {5,D}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {4,S} {8,S} {14,S} {15,S}
2     C u0 p0 c0  {4,S} {9,S} {10,S} {16,S}
3     C u0 p0 c0  {5,S} {11,S} {12,S} {13,S}
4  *1 C u1 p0 c0  {1,S} {2,S} {6,S}
5     C u0 p0 c0  {3,S} {6,S} {7,D}
6     C u0 p0 c0  {4,S} {5,S} {17,D}
7     C u0 p0 c0  {5,D} {18,S} {19,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {1,S}
15    H u0 p0 c0  {1,S}
16    H u0 p0 c0  {2,S}
17    O u0 p2 c0  {6,D}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24634, 'd12': 1.48422, 'd13': 1.37723},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 40,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {5,S} {8,S}
2     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {14,S}
4  *4 C u0 p0 c0  {5,S} {6,D} {7,S}
5  *5 C u0 p0 c0  {1,S} {4,S} {15,D}
6     C u0 p0 c0  {4,D} {18,S} {19,S}
7  *1 C u1 p0 c0  {4,S} {16,S} {17,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    O u0 p2 c0  {5,D}
16    H u0 p0 c0  {7,S}
17    H u0 p0 c0  {7,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
2     C u0 p0 c0  {4,S} {11,S} {12,S} {13,S}
3  *2 C u0 p0 c0  {5,S} {14,S} {15,S} {16,S}
4  *1 C u1 p0 c0  {1,S} {2,S} {6,S}
5  *5 C u0 p0 c0  {3,S} {6,S} {7,D}
6  *4 C u0 p0 c0  {4,S} {5,S} {17,D}
7     C u0 p0 c0  {5,D} {18,S} {19,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16 *3 H u0 p0 c0  {3,S}
17    O u0 p2 c0  {6,D}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34786, 'd12': 2.54909, 'd13': 1.3992},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 41,
    reactant1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,S} {5,S} {6,S} {8,S}
2     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
3  *2 C u0 p0 c0  {4,S} {12,S} {13,S} {14,S}
4  *5 C u0 p0 c0  {3,S} {5,S} {7,D}
5  *6 C u0 p0 c0  {1,S} {4,S} {15,D}
6  *1 C u1 p0 c0  {1,S} {16,S} {17,S}
7     C u0 p0 c0  {4,D} {18,S} {19,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14 *3 H u0 p0 c0  {3,S}
15    O u0 p2 c0  {5,D}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1  *6 C u0 p0 c0  {2,S} {3,S} {5,S} {8,S}
2  *2 C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {14,S}
4  *5 C u0 p0 c0  {5,S} {6,D} {7,S}
5  *4 C u0 p0 c0  {1,S} {4,S} {15,D}
6     C u0 p0 c0  {4,D} {18,S} {19,S}
7  *1 C u1 p0 c0  {4,S} {16,S} {17,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11 *3 H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    O u0 p2 c0  {5,D}
16    H u0 p0 c0  {7,S}
17    H u0 p0 c0  {7,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32527, 'd12': 2.60352, 'd13': 1.38289},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 42,
    reactant1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,S} {6,S} {7,S} {9,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {5,S} {15,S} {16,S} {17,S}
4  *2 C u0 p0 c0  {5,S} {13,S} {14,S} {18,S}
5  *5 C u0 p0 c0  {3,S} {4,S} {6,D}
6  *6 C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {1,S} {19,S} {20,S}
8     O u0 p2 c0  {6,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {3,S}
18 *3 H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1  *6 C u0 p0 c0  {2,S} {3,S} {6,S} {9,S}
2  *2 C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {15,S}
4     C u0 p0 c0  {5,S} {16,S} {17,S} {18,S}
5  *5 C u0 p0 c0  {4,S} {6,D} {7,S}
6  *4 C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {5,S} {19,S} {20,S}
8     O u0 p2 c0  {6,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12 *3 H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34151, 'd12': 2.6045, 'd13': 1.34645},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 43,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {6,S} {7,S} {9,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {5,S} {15,S} {16,S} {17,S}
4     C u0 p0 c0  {5,S} {13,S} {14,S} {18,S}
5     C u0 p0 c0  {3,S} {4,S} {6,D}
6     C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {1,S} {19,S} {20,S}
8     O u0 p2 c0  {6,S} {21,S}
9  *3 H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {3,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {5,S} {12,S} {13,S} {14,S}
2     C u0 p0 c0  {5,S} {15,S} {16,S} {17,S}
3  *2 C u0 p0 c0  {6,S} {9,S} {18,S} {19,S}
4     C u0 p0 c0  {6,S} {10,S} {11,S} {20,S}
5     C u0 p0 c0  {1,S} {2,S} {7,D}
6  *1 C u1 p0 c0  {3,S} {4,S} {7,S}
7     C u0 p0 c0  {5,D} {6,S} {8,S}
8     O u0 p2 c0  {7,S} {21,S}
9  *3 H u0 p0 c0  {3,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {1,S}
13    H u0 p0 c0  {1,S}
14    H u0 p0 c0  {1,S}
15    H u0 p0 c0  {2,S}
16    H u0 p0 c0  {2,S}
17    H u0 p0 c0  {2,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27782, 'd12': 1.49434, 'd13': 1.33593},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 44,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3  *2 C u0 p0 c0  {4,S} {10,S} {11,S} {12,S}
4  *1 C u1 p0 c0  {1,S} {3,S} {13,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10 *3 H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  *2 C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *1 C u1 p0 c0  {2,S} {12,S} {13,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7  *3 H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.49221', 'd12': '1.30172', 'd13': '1.30285'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 1""",
    longDesc = 
u"""
""",
)

entry(
    index = 45,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {6,S} {11,S} {12,S}
4     C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {6,S} {15,S} {16,S} {17,S}
6  *1 C u1 p0 c0  {3,S} {4,S} {5,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15 *3 H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {5,S} {14,S} {15,S}
4     C u0 p0 c0  {2,S} {5,S} {10,S} {11,S}
5     C u0 p0 c0  {3,S} {4,S} {12,S} {13,S}
6  *1 C u1 p0 c0  {1,S} {16,S} {17,S}
7  *3 H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {5,S}
13    H u0 p0 c0  {5,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.48516', 'd12': '1.29485', 'd13': '1.31517'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 2""",
    longDesc = 
u"""
""",
)

entry(
    index = 46,
    reactant1 = """
multiplicity 2
1  *4 C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {4,S} {5,S} {8,S} {9,S}
3  *2 C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0  {2,S} {13,S} {14,S} {15,S}
5  *1 C u1 p0 c0  {1,S} {2,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10 *3 H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3  *4 C u0 p0 c0  {1,S} {5,S} {10,S} {11,S}
4     C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  *1 C u1 p0 c0  {3,S} {15,S} {16,S}
6  *3 H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.22164', 'd12': '1.40190', 'd13': '1.41346'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 3""",
    longDesc = 
u"""
""",
)

entry(
    index = 47,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  *2 C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *4 O u0 p2 c0  {2,S} {12,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7  *3 H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12 *1 O u1 p2 c0  {4,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {8,S} {9,S} {10,S}
3  *1 C u1 p0 c0  {1,S} {4,S} {11,S}
4  *4 O u0 p2 c0  {3,S} {5,S}
5  *2 O u0 p2 c0  {4,S} {12,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12 *3 H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.03811', 'd12': '1.28316', 'd13': '1.33202'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 4""",
    longDesc = 
u"""
""",
)

entry(
    index = 48,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {5,S} {8,S} {9,S}
2  *5 C u0 p0 c0  {4,S} {6,S} {10,S} {11,S}
3     C u0 p0 c0  {1,S} {7,S} {12,S} {13,S}
4  *4 C u0 p0 c0  {2,S} {7,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {17,S} {18,S} {19,S}
6  *2 C u0 p0 c0  {2,S} {16,S} {20,S} {21,S}
7  *1 C u1 p0 c0  {3,S} {4,S} {22,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16 *3 H u0 p0 c0  {6,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {11,S} {12,S}
2  *2 C u0 p0 c0  {1,S} {3,S} {8,S} {13,S}
3  *5 C u0 p0 c0  {2,S} {5,S} {14,S} {15,S}
4     C u0 p0 c0  {1,S} {6,S} {9,S} {10,S}
5  *4 C u0 p0 c0  {3,S} {7,S} {16,S} {17,S}
6     C u0 p0 c0  {4,S} {18,S} {19,S} {20,S}
7  *1 C u1 p0 c0  {5,S} {21,S} {22,S}
8  *3 H u0 p0 c0  {2,S}
9     H u0 p0 c0  {4,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {1,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.52790', 'd12': '1.36152', 'd13': '1.39272'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 5""",
    longDesc = 
u"""
""",
)

entry(
    index = 49,
    reactant1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,S} {4,S} {6,S} {7,S}
2  *5 C u0 p0 c0  {1,S} {5,S} {8,S} {9,S}
3     C u0 p0 c0  {4,S} {10,S} {11,S} {12,S}
4  *1 C u1 p0 c0  {1,S} {3,S} {13,S}
5  *2 O u0 p2 c0  {2,S} {14,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14 *3 H u0 p0 c0  {5,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  *5 C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4  *4 C u0 p0 c0  {2,S} {9,S} {13,S} {14,S}
5  *3 H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9  *1 O u1 p2 c0  {4,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.36998', 'd12': '1.27828', 'd13': '1.29626'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 6""",
    longDesc = 
u"""
""",
)

entry(
    index = 50,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {8,S} {9,S}
2  *4 C u0 p0 c0  {1,S} {6,S} {10,S} {11,S}
3  *5 C u0 p0 c0  {1,S} {7,S} {12,S} {13,S}
4     C u0 p0 c0  {6,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0  {6,S} {17,S} {18,S} {19,S}
6  *1 C u1 p0 c0  {2,S} {4,S} {5,S}
7  *2 O u0 p2 c0  {3,S} {20,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20 *3 H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {4,S} {5,S} {7,S}
2  *5 C u0 p0 c0  {1,S} {3,S} {8,S} {9,S}
3     C u0 p0 c0  {2,S} {6,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6  *4 C u0 p0 c0  {3,S} {12,S} {19,S} {20,S}
7  *3 H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12 *1 O u1 p2 c0  {6,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.50266', 'd12': '1.24586', 'd13': '1.31554'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 7""",
    longDesc = 
u"""
""",
)

entry(
    index = 51,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {9,S}
2  *5 C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {6,S} {18,S} {19,S}
4  *2 C u0 p0 c0  {2,S} {5,S} {10,S} {13,S}
5     C u0 p0 c0  {4,S} {6,S} {14,S} {15,S}
6     C u0 p0 c0  {3,S} {5,S} {16,S} {17,S}
7  *4 C u0 p0 c0  {1,S} {8,S} {20,S} {21,S}
8  *1 C u1 p0 c0  {7,S} {22,S} {23,S}
9     H u0 p0 c0  {1,S}
10 *3 H u0 p0 c0  {4,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {5,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {8,S}
23    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {5,S} {9,S}
2     C u0 p0 c0  {1,S} {4,S} {14,S} {15,S}
3  *5 C u0 p0 c0  {1,S} {7,S} {10,S} {11,S}
4     C u0 p0 c0  {2,S} {6,S} {12,S} {13,S}
5  *4 C u0 p0 c0  {1,S} {8,S} {16,S} {17,S}
6     C u0 p0 c0  {4,S} {8,S} {18,S} {19,S}
7  *2 C u0 p0 c0  {3,S} {20,S} {21,S} {22,S}
8  *1 C u1 p0 c0  {5,S} {6,S} {23,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {2,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20 *3 H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.64783', 'd12': '1.33168', 'd13': '1.38878'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 8""",
    longDesc = 
u"""
""",
)

entry(
    index = 52,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {5,S} {6,S} {8,S}
2  *5 C u0 p0 c0  {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0  {2,S} {4,S} {11,S} {12,S}
4     C u0 p0 c0  {3,S} {7,S} {13,S} {14,S}
5     C u0 p0 c0  {1,S} {15,S} {16,S} {17,S}
6     C u0 p0 c0  {1,S} {18,S} {19,S} {20,S}
7  *4 O u0 p2 c0  {4,S} {21,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21 *1 O u1 p2 c0  {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {9,S} {10,S}
2  *4 C u0 p0 c0  {1,S} {6,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {7,S} {13,S} {14,S}
4     C u0 p0 c0  {6,S} {15,S} {16,S} {17,S}
5     C u0 p0 c0  {6,S} {18,S} {19,S} {20,S}
6  *1 C u1 p0 c0  {2,S} {4,S} {5,S}
7  *5 O u0 p2 c0  {3,S} {8,S}
8  *2 O u0 p2 c0  {7,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21 *3 H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.51644', 'd12': '1.19533', 'd13': '1.34348'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 9""",
    longDesc = 
u"""
""",
)

entry(
    index = 53,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {9,S}
2     C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {6,S} {18,S} {19,S}
4  *5 C u0 p0 c0  {2,S} {5,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {4,S} {6,S} {10,S} {15,S}
6     C u0 p0 c0  {3,S} {5,S} {16,S} {17,S}
7  *4 C u0 p0 c0  {1,S} {8,S} {20,S} {21,S}
8  *1 C u1 p0 c0  {7,S} {22,S} {23,S}
9     H u0 p0 c0  {1,S}
10 *3 H u0 p0 c0  {5,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {8,S}
23    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {4,S} {9,S}
2     C u0 p0 c0  {1,S} {5,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {6,S} {14,S} {15,S}
4  *5 C u0 p0 c0  {1,S} {7,S} {10,S} {11,S}
5  *4 C u0 p0 c0  {2,S} {8,S} {16,S} {17,S}
6     C u0 p0 c0  {3,S} {8,S} {18,S} {19,S}
7  *2 C u0 p0 c0  {4,S} {20,S} {21,S} {22,S}
8  *1 C u1 p0 c0  {5,S} {6,S} {23,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20 *3 H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.65192', 'd12': '1.37209', 'd13': '1.32587'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 10""",
    longDesc = 
u"""
""",
)

entry(
    index = 54,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {9,S} {10,S}
2     C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3  *5 C u0 p0 c0  {1,S} {5,S} {7,S} {8,S}
4     C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {3,S} {16,S} {17,S} {18,S}
6  *4 C u0 p0 c0  {4,S} {15,S} {19,S} {20,S}
7     H u0 p0 c0  {3,S}
8     H u0 p0 c0  {3,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15 *1 O u1 p2 c0  {6,S}
16 *3 H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {10,S} {11,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {5,S} {12,S} {13,S}
4  *4 C u0 p0 c0  {2,S} {6,S} {14,S} {15,S}
5  *5 C u0 p0 c0  {3,S} {7,S} {16,S} {17,S}
6  *1 C u1 p0 c0  {4,S} {18,S} {19,S}
7  *2 O u0 p2 c0  {5,S} {20,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20 *3 H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.50531', 'd12': '1.24532', 'd13': '1.27498'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 11""",
    longDesc = 
u"""
""",
)

entry(
    index = 55,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {9,S} {10,S}
2     C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3  *5 C u0 p0 c0  {1,S} {5,S} {7,S} {8,S}
4     C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {3,S} {15,S} {16,S} {17,S}
6  *4 O u0 p2 c0  {4,S} {18,S}
7     H u0 p0 c0  {3,S}
8     H u0 p0 c0  {3,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15 *3 H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18 *1 O u1 p2 c0  {6,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {8,S} {9,S}
2     C u0 p0 c0  {1,S} {4,S} {10,S} {11,S}
3  *4 C u0 p0 c0  {1,S} {5,S} {12,S} {13,S}
4     C u0 p0 c0  {2,S} {6,S} {14,S} {15,S}
5  *1 C u1 p0 c0  {3,S} {16,S} {17,S}
6  *5 O u0 p2 c0  {4,S} {7,S}
7  *2 O u0 p2 c0  {6,S} {18,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18 *3 H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.53680', 'd12': '1.14855', 'd13': '1.40019'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 12""",
    longDesc = 
u"""
""",
)

entry(
    index = 56,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0  {2,S} {3,S} {4,S}
2 *2 O u0 p2 c0  {1,S} {5,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5 *3 H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1 *2 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4 *3 H u0 p0 c0  {1,S}
5 *1 O u1 p2 c0  {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38927, 'd12': 1.276283, 'd13': 1.203442},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 13""",
    longDesc = 
u"""
""",
)

entry(
    index = 57,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2  *2 C u0 p0 c0  {3,S} {4,S} {8,S} {9,S}
3  *1 C u1 p0 c0  {1,S} {2,S} {10,S}
4  *3 H u0 p0 c0  {2,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *1 C u1 p0 c0  {1,S} {9,S} {10,S}
4     H u0 p0 c0  {1,S}
5  *3 H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.492365, 'd12': 1.30064, 'd13': 1.30311},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 14""",
    longDesc = 
u"""
""",
)

entry(
    index = 58,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {5,S} {6,S} {7,S}
2  *1 C u1 p0 c0  {1,S} {3,S} {8,S}
3     C u0 p0 c0  {2,S} {4,D} {9,S}
4     C u0 p0 c0  {3,D} {10,S} {11,S}
5  *3 H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0  {1,S} {4,D} {7,S}
3  *1 C u1 p0 c0  {1,S} {8,S} {9,S}
4     C u0 p0 c0  {2,D} {10,S} {11,S}
5     H u0 p0 c0  {1,S}
6  *3 H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {3,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.489543, 'd12': 1.256171, 'd13': 1.365329},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 15""",
    longDesc = 
u"""
""",
)

entry(
    index = 59,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {4,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0  {4,S} {9,S} {10,S} {11,S}
3  *2 C u0 p0 c0  {4,S} {5,S} {12,S} {13,S}
4  *1 C u1 p0 c0  {1,S} {2,S} {3,S}
5  *3 H u0 p0 c0  {3,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *1 C u1 p0 c0  {1,S} {12,S} {13,S}
5  *3 H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.493897, 'd12': 1.302738, 'd13': 1.308689},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 16""",
    longDesc = 
u"""
""",
)

entry(
    index = 60,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {5,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4  *2 C u0 p0 c0  {5,S} {13,S} {14,S} {15,S}
5  *1 C u1 p0 c0  {2,S} {4,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13 *3 H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3  *2 C u0 p0 c0  {1,S} {5,S} {10,S} {11,S}
4     C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  *1 C u1 p0 c0  {3,S} {15,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11 *3 H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49488, 'd12': 1.297544, 'd13': 1.303078},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 17""",
    longDesc = 
u"""
""",
)

entry(
    index = 61,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {5,S} {11,S} {12,S}
4  *1 C u1 p0 c0  {2,S} {6,S} {13,S}
5     O u0 p2 c0  {3,S} {14,S}
6  *2 O u0 p2 c0  {4,S} {15,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {5,S}
15 *3 H u0 p0 c0  {6,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {5,S} {10,S} {11,S}
4  *2 C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5     O u0 p2 c0  {3,S} {15,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13 *3 H u0 p0 c0  {4,S}
14 *1 O u1 p2 c0  {4,S}
15    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39608, 'd12': 1.27819, 'd13': 1.208513},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 18""",
    longDesc = 
u"""
""",
)

entry(
    index = 62,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {9,S} {10,S}
2     C u0 p0 c0  {1,S} {3,S} {11,S} {12,S}
3     C u0 p0 c0  {2,S} {5,S} {15,S} {16,S}
4     C u0 p0 c0  {1,S} {6,S} {13,S} {14,S}
5  *2 C u0 p0 c0  {3,S} {8,S} {17,S} {18,S}
6     C u0 p0 c0  {4,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0  {8,S} {22,S} {23,S} {24,S}
8  *1 C u1 p0 c0  {5,S} {7,S} {25,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17 *3 H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {7,S}
25    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {9,S} {10,S}
2     C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {6,S} {13,S} {14,S}
4     C u0 p0 c0  {2,S} {8,S} {15,S} {16,S}
5  *2 C u0 p0 c0  {7,S} {8,S} {17,S} {18,S}
6     C u0 p0 c0  {3,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0  {5,S} {22,S} {23,S} {24,S}
8  *1 C u1 p0 c0  {4,S} {5,S} {25,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {5,S}
18 *3 H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {7,S}
25    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.495163, 'd12': 1.305005, 'd13': 1.305369},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 19""",
    longDesc = 
u"""
""",
)

entry(
    index = 63,
    reactant1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,B} {3,B} {7,S}
2     C u0 p0 c0  {1,B} {4,B} {10,S}
3  *2 C u0 p0 c0  {1,B} {6,B} {9,S}
4     C u0 p0 c0  {2,B} {5,B} {11,S}
5     C u0 p0 c0  {4,B} {6,B} {12,S}
6     C u0 p0 c0  {3,B} {5,B} {13,S}
7  *5 C u0 p0 c0  {1,S} {8,D} {14,S}
8  *1 C u1 p0 c0  {7,D} {15,S}
9  *3 H u0 p0 c0  {3,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {5,S}
13    H u0 p0 c0  {6,S}
14    H u0 p0 c0  {7,S}
15    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,B} {5,S} {8,B}
2     C u0 p0 c0  {1,B} {3,B} {9,S}
3     C u0 p0 c0  {2,B} {4,B} {10,S}
4     C u0 p0 c0  {3,B} {6,B} {12,S}
5  *5 C u0 p0 c0  {1,S} {7,D} {11,S}
6     C u0 p0 c0  {4,B} {8,B} {13,S}
7  *2 C u0 p0 c0  {5,D} {14,S} {15,S}
8  *1 C u1 p0 c0  {1,B} {6,B}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {5,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {6,S}
14    H u0 p0 c0  {7,S}
15 *3 H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.451028, 'd12': 1.387024, 'd13': 1.385279},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 20""",
    longDesc = 
u"""
""",
)

entry(
    index = 64,
    reactant1 = """
multiplicity 2
1 *2 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 C u1 p0 c0  {1,S} {6,D}
3 *3 H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    O u0 p2 c0  {2,D}
""",
    product1 = """
multiplicity 2
1 *2 C u0 p0 c0  {2,S} {3,D} {6,S}
2 *1 C u1 p0 c0  {1,S} {4,S} {5,S}
3    O u0 p2 c0  {1,D}
4    H u0 p0 c0  {2,S}
5    H u0 p0 c0  {2,S}
6 *3 H u0 p0 c0  {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.399541, 'd12': 1.286564, 'd13': 1.465925},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 21""",
    longDesc = 
u"""
""",
)

entry(
    index = 65,
    reactant1 = """
multiplicity 2
1 *2 C u0 p0 c0  {2,S} {3,D} {4,S}
2 *1 C u1 p0 c0  {1,S} {5,S} {6,S}
3    C u0 p0 c0  {1,D} {7,S} {8,S}
4 *3 H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {3,S}
8    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1 *2 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0  {3,D} {7,S} {8,S}
3 *1 C u1 p0 c0  {1,S} {2,D}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *3 H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.424615, 'd12': 1.337938, 'd13': 1.299016},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 22""",
    longDesc = 
u"""
""",
)

entry(
    index = 66,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {6,S} {11,S} {12,S}
4     C u0 p0 c0  {2,S} {13,S} {14,S} {15,S}
5  *2 C u0 p0 c0  {6,S} {16,S} {17,S} {18,S}
6  *1 C u1 p0 c0  {3,S} {5,S} {19,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16 *3 H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {5,S} {11,S} {12,S}
4  *2 C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5     C u0 p0 c0  {3,S} {15,S} {16,S} {17,S}
6  *1 C u1 p0 c0  {4,S} {18,S} {19,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14 *3 H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.492938, 'd12': 1.300834, 'd13': 1.302398},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 23""",
    longDesc = 
u"""
""",
)

entry(
    index = 67,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
4  *2 C u0 p0 c0  {6,S} {15,S} {18,S} {19,S}
5     C u0 p0 c0  {6,S} {16,S} {17,S} {20,S}
6  *1 C u1 p0 c0  {4,S} {5,S} {7,S}
7     C u0 p0 c0  {1,S} {6,S} {21,D}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15 *3 H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {5,S}
21    O u0 p2 c0  {7,D}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {6,S} {8,S}
2  *2 C u0 p0 c0  {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {1,S} {2,S} {19,D}
7  *1 C u1 p0 c0  {2,S} {20,S} {21,S}
8     H u0 p0 c0  {1,S}
9  *3 H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    O u0 p2 c0  {6,D}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48173, 'd12': 1.24362, 'd13': 1.37606},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 24""",
    longDesc = 
u"""
""",
)

entry(
    index = 68,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {5,S} {11,S}
2  *4 C u0 p0 c0  {1,S} {3,S} {8,S} {9,S}
3  *5 C u0 p0 c0  {2,S} {6,S} {7,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {3,S} {19,S} {20,S} {21,S}
7  *1 C u1 p0 c0  {3,S} {22,S} {23,S}
8  *6 O u0 p2 c0  {2,S} {10,S}
9     O u0 p2 c0  {2,S} {24,S}
10 *2 O u0 p2 c0  {8,S} {25,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {9,S}
25 *3 H u0 p0 c0  {10,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {5,S} {10,S}
2  *5 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3  *6 C u0 p0 c0  {1,S} {2,S} {8,S} {9,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0  {1,S} {15,S} {16,S} {17,S}
6     C u0 p0 c0  {2,S} {20,S} {21,S} {22,S}
7  *2 C u0 p0 c0  {2,S} {18,S} {19,S} {23,S}
8     O u0 p2 c0  {3,S} {24,S}
9  *4 O u0 p2 c0  {3,S} {25,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {6,S}
23 *3 H u0 p0 c0  {7,S}
24    H u0 p0 c0  {8,S}
25 *1 O u1 p2 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.47997, 'd12': 1.4027, 'd13': 1.14812},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 25""",
    longDesc = 
u"""
""",
)

entry(
    index = 69,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {5,S} {11,S}
2  *5 C u0 p0 c0  {1,S} {3,S} {8,S} {9,S}
3  *4 C u0 p0 c0  {2,S} {6,S} {7,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {3,S} {19,S} {20,S} {21,S}
7  *1 C u1 p0 c0  {3,S} {22,S} {23,S}
8     O u0 p2 c0  {2,S} {10,S}
9  *2 O u0 p2 c0  {2,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24 *3 H u0 p0 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {5,S} {10,S}
2  *5 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3  *4 C u0 p0 c0  {1,S} {2,S} {8,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {2,S} {21,S} {22,S} {23,S}
7  *2 C u0 p0 c0  {2,S} {19,S} {20,S} {24,S}
8     O u0 p2 c0  {3,S} {9,S}
9     O u0 p2 c0  {8,S} {25,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12 *1 O u1 p2 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {6,S}
23    H u0 p0 c0  {6,S}
24 *3 H u0 p0 c0  {7,S}
25    H u0 p0 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.3547, 'd12': 1.28678, 'd13': 1.28756},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 26""",
    longDesc = 
u"""
""",
)

entry(
    index = 70,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4  *2 C u0 p0 c0  {6,S} {16,S} {19,S} {20,S}
5     C u0 p0 c0  {6,S} {17,S} {18,S} {21,S}
6  *1 C u1 p0 c0  {4,S} {5,S} {7,S}
7     C u0 p0 c0  {1,S} {6,S} {22,D}
8     O u0 p2 c0  {1,S} {9,S}
9     O u0 p2 c0  {8,S} {23,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16 *3 H u0 p0 c0  {4,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {5,S}
22    O u0 p2 c0  {7,D}
23    H u0 p0 c0  {9,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {6,S} {8,S}
2  *2 C u0 p0 c0  {5,S} {6,S} {7,S} {10,S}
3     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0  {1,S} {11,S} {12,S} {19,S}
5     C u0 p0 c0  {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {1,S} {2,S} {20,D}
7  *1 C u1 p0 c0  {2,S} {21,S} {22,S}
8     O u0 p2 c0  {1,S} {9,S}
9     O u0 p2 c0  {8,S} {23,S}
10 *3 H u0 p0 c0  {2,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {4,S}
20    O u0 p2 c0  {6,D}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48045, 'd12': 1.23875, 'd13': 1.38564},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 27""",
    longDesc = 
u"""
""",
)

entry(
    index = 71,
    reactant1 = """
multiplicity 2
1  *5 C u0 p0 c0  {3,S} {4,S} {7,S} {8,S}
2  *6 C u0 p0 c0  {6,S} {7,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
4     C u0 p0 c0  {1,S} {17,S} {18,S} {19,S}
5     C u0 p0 c0  {6,S} {20,S} {21,S} {22,S}
6  *1 C u1 p0 c0  {2,S} {5,S} {9,S}
7  *4 C u0 p0 c0  {1,S} {2,S} {23,D}
8  *7 O u0 p2 c0  {1,S} {10,S}
9     O u0 p2 c0  {6,S} {11,S}
10 *2 O u0 p2 c0  {8,S} {25,S}
11    O u0 p2 c0  {9,S} {24,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {5,S}
23    O u0 p2 c0  {7,D}
24    H u0 p0 c0  {11,S}
25 *3 H u0 p0 c0  {10,S}
""",
    product1 = """
multiplicity 2
1  *6 C u0 p0 c0  {4,S} {5,S} {7,S} {9,S}
2  *2 C u0 p0 c0  {3,S} {6,S} {8,S} {11,S}
3  *5 C u0 p0 c0  {2,S} {7,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {1,S} {14,S} {15,S} {21,S}
6     C u0 p0 c0  {2,S} {19,S} {20,S} {22,S}
7  *7 C u0 p0 c0  {1,S} {3,S} {23,D}
8     O u0 p2 c0  {2,S} {10,S}
9  *4 O u0 p2 c0  {1,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11 *3 H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {5,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {6,S}
23    O u0 p2 c0  {7,D}
24 *1 O u1 p2 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.48335, 'd12': 1.3435, 'd13': 1.19085},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 28""",
    longDesc = 
u"""
""",
)

entry(
    index = 72,
    reactant1 = """
multiplicity 2
1  *4 C u0 p0 c0  {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0  {6,S} {9,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
4     C u0 p0 c0  {1,S} {17,S} {18,S} {19,S}
5     C u0 p0 c0  {6,S} {20,S} {21,S} {22,S}
6  *1 C u1 p0 c0  {2,S} {5,S} {7,S}
7  *5 C u0 p0 c0  {1,S} {6,S} {23,D}
8  *6 O u0 p2 c0  {1,S} {11,S}
9     O u0 p2 c0  {2,S} {10,S}
10    O u0 p2 c0  {9,S} {24,S}
11 *2 O u0 p2 c0  {8,S} {25,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {5,S}
23    O u0 p2 c0  {7,D}
24    H u0 p0 c0  {10,S}
25 *3 H u0 p0 c0  {11,S}
""",
    product1 = """
multiplicity 2
1  *6 C u0 p0 c0  {4,S} {5,S} {7,S} {9,S}
2  *2 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3     C u0 p0 c0  {2,S} {8,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {1,S} {14,S} {15,S} {21,S}
6     C u0 p0 c0  {2,S} {19,S} {20,S} {22,S}
7  *5 C u0 p0 c0  {1,S} {2,S} {23,D}
8     O u0 p2 c0  {3,S} {10,S}
9  *4 O u0 p2 c0  {1,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11 *3 H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {5,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {6,S}
23    O u0 p2 c0  {7,D}
24 *1 O u1 p2 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.46075, 'd12': 1.35819, 'd13': 1.20035},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 29""",
    longDesc = 
u"""
""",
)

entry(
    index = 73,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
3     C u0 p0 c0  {1,S} {17,S} {18,S} {19,S}
4  *4 C u0 p0 c0  {6,S} {9,S} {12,S} {13,S}
5     C u0 p0 c0  {6,S} {20,S} {21,S} {22,S}
6  *1 C u1 p0 c0  {4,S} {5,S} {7,S}
7     C u0 p0 c0  {1,S} {6,S} {23,D}
8     O u0 p2 c0  {1,S} {10,S}
9  *5 O u0 p2 c0  {4,S} {11,S}
10    O u0 p2 c0  {8,S} {24,S}
11 *2 O u0 p2 c0  {9,S} {25,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {2,S}
16    H u0 p0 c0  {2,S}
17    H u0 p0 c0  {3,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {5,S}
23    O u0 p2 c0  {7,D}
24    H u0 p0 c0  {10,S}
25 *3 H u0 p0 c0  {11,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {4,S} {5,S} {7,S} {8,S}
2  *2 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3  *5 C u0 p0 c0  {2,S} {9,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {18,S} {19,S} {20,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {22,S}
6     C u0 p0 c0  {2,S} {14,S} {15,S} {21,S}
7     C u0 p0 c0  {1,S} {2,S} {23,D}
8     O u0 p2 c0  {1,S} {10,S}
9  *4 O u0 p2 c0  {3,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11 *3 H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {6,S}
15    H u0 p0 c0  {6,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {5,S}
23    O u0 p2 c0  {7,D}
24 *1 O u1 p2 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.41589, 'd12': 1.37066, 'd13': 1.24608},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 30""",
    longDesc = 
u"""
""",
)

entry(
    index = 74,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {6,S} {8,S}
2  *4 C u0 p0 c0  {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
4     C u0 p0 c0  {1,S} {15,S} {16,S} {17,S}
5     C u0 p0 c0  {2,S} {18,S} {19,S} {20,S}
6     C u0 p0 c0  {1,S} {2,S} {21,D}
7  *1 C u1 p0 c0  {2,S} {22,S} {23,S}
8     O u0 p2 c0  {1,S} {10,S}
9  *5 O u0 p2 c0  {2,S} {11,S}
10    O u0 p2 c0  {8,S} {24,S}
11 *2 O u0 p2 c0  {9,S} {25,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21    O u0 p2 c0  {6,D}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {10,S}
25 *3 H u0 p0 c0  {11,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {7,S} {8,S}
2  *5 C u0 p0 c0  {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0  {2,S} {19,S} {20,S} {21,S}
6  *2 C u0 p0 c0  {2,S} {17,S} {18,S} {22,S}
7     C u0 p0 c0  {1,S} {2,S} {23,D}
8     O u0 p2 c0  {1,S} {10,S}
9  *4 O u0 p2 c0  {2,S} {24,S}
10    O u0 p2 c0  {8,S} {25,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22 *3 H u0 p0 c0  {6,S}
23    O u0 p2 c0  {7,D}
24 *1 O u1 p2 c0  {9,S}
25    H u0 p0 c0  {10,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.40999, 'd12': 1.42006, 'd13': 1.1726},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 31""",
    longDesc = 
u"""
""",
)

entry(
    index = 75,
    reactant1 = """
multiplicity 2
1  *5 C u0 p0 c0  {2,S} {3,S} {7,S} {10,S}
2     C u0 p0 c0  {1,S} {8,S} {11,S} {12,S}
3  *2 C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0  {6,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {6,S} {19,S} {20,S} {21,S}
6  *1 C u1 p0 c0  {4,S} {5,S} {7,S}
7  *4 C u0 p0 c0  {1,S} {6,S} {22,D}
8     O u0 p2 c0  {2,S} {9,S}
9     O u0 p2 c0  {8,S} {23,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15 *3 H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22    O u0 p2 c0  {7,D}
23    H u0 p0 c0  {9,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {4,S} {5,S} {6,S} {10,S}
2  *4 C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3     C u0 p0 c0  {2,S} {8,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {1,S} {14,S} {15,S} {19,S}
6  *5 C u0 p0 c0  {1,S} {2,S} {20,D}
7  *1 C u1 p0 c0  {2,S} {21,S} {22,S}
8     O u0 p2 c0  {3,S} {9,S}
9     O u0 p2 c0  {8,S} {23,S}
10 *3 H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {5,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {5,S}
20    O u0 p2 c0  {6,D}
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.54737, 'd12': 1.34448, 'd13': 1.40945},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 32""",
    longDesc = 
u"""
""",
)

entry(
    index = 76,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {5,S} {6,S} {7,S} {19,S}
2     C u0 p0 c0  {8,S} {9,S} {10,S} {20,S}
3     C u0 p0 c0  {11,S} {12,S} {13,S} {20,S}
4     H u0 p0 c0  {19,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    O u0 p2 c0  {17,D}
15 *2 O u0 p2 c0  {16,S} {18,S}
16 *3 H u0 p0 c0  {15,S}
17 *5 C u0 p0 c0  {14,D} {19,S} {20,S}
18 *6 O u0 p2 c0  {15,S} {19,S}
19 *4 C u0 p0 c0  {1,S} {4,S} {17,S} {18,S}
20 *1 C u1 p0 c0  {2,S} {3,S} {17,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {7,S} {8,S} {15,S}
2     H u0 p0 c0  {11,S}
3     H u0 p0 c0  {11,S}
4     H u0 p0 c0  {13,S}
5     H u0 p0 c0  {13,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     O u0 p2 c0  {18,D}
10    H u0 p0 c0  {19,S}
11    C u0 p0 c0  {2,S} {3,S} {12,S} {19,S}
12    H u0 p0 c0  {11,S}
13    C u0 p0 c0  {4,S} {5,S} {14,S} {15,S}
14    H u0 p0 c0  {13,S}
15 *2 C u0 p0 c0  {1,S} {13,S} {16,S} {18,S}
16 *3 H u0 p0 c0  {15,S}
17 *4 O u0 p2 c0  {19,S} {20,S}
18 *5 C u0 p0 c0  {9,D} {15,S} {19,S}
19 *6 C u0 p0 c0  {10,S} {11,S} {17,S} {18,S}
20 *1 O u1 p2 c0  {17,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.47, 'd12': 1.3516, 'd13': 1.2065},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 33""",
    longDesc = 
u"""
""",
)

entry(
    index = 77,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {9,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0  {5,S} {16,S} {17,S} {18,S}
5  *4 C u0 p0 c0  {4,S} {6,D} {7,S}
6  *5 C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {5,S} {19,S} {20,S}
8  *2 O u0 p2 c0  {6,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21 *3 H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {14,S}
4     C u0 p0 c0  {6,S} {17,S} {18,S} {19,S}
5  *2 C u0 p0 c0  {6,S} {15,S} {16,S} {20,S}
6  *5 C u0 p0 c0  {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0  {1,S} {6,D} {21,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20 *3 H u0 p0 c0  {5,S}
21 *1 O u1 p2 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.44455, 'd12': 1.42329, 'd13': 1.25908},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 34""",
    longDesc = 
u"""
""",
)

entry(
    index = 78,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {7,S} {8,S} {21,S}
2     C u0 p0 c0  {9,S} {10,S} {11,S} {21,S}
3     C u0 p0 c0  {12,S} {13,S} {14,S} {22,S}
4     O u0 p2 c0  {5,S} {22,S}
5     O u0 p2 c0  {4,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    O u0 p2 c0  {19,D}
16    H u0 p0 c0  {5,S}
17 *2 O u0 p2 c0  {18,S} {20,S}
18 *3 H u0 p0 c0  {17,S}
19 *5 C u0 p0 c0  {15,D} {21,S} {22,S}
20 *6 O u0 p2 c0  {17,S} {21,S}
21 *4 C u0 p0 c0  {1,S} {2,S} {19,S} {20,S}
22 *1 C u1 p0 c0  {3,S} {4,S} {19,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {7,S} {8,S} {21,S}
2     H u0 p0 c0  {12,S}
3     H u0 p0 c0  {12,S}
4     H u0 p0 c0  {10,S}
5     H u0 p0 c0  {10,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     O u0 p2 c0  {20,D}
10    C u0 p0 c0  {4,S} {5,S} {11,S} {21,S}
11    H u0 p0 c0  {10,S}
12    C u0 p0 c0  {2,S} {3,S} {13,S} {17,S}
13    H u0 p0 c0  {12,S}
14    O u0 p2 c0  {15,S} {16,S}
15    H u0 p0 c0  {14,S}
16    O u0 p2 c0  {14,S} {17,S}
17 *2 C u0 p0 c0  {12,S} {16,S} {18,S} {20,S}
18 *3 H u0 p0 c0  {17,S}
19 *4 O u0 p2 c0  {21,S} {22,S}
20 *5 C u0 p0 c0  {9,D} {17,S} {21,S}
21 *6 C u0 p0 c0  {1,S} {10,S} {19,S} {20,S}
22 *1 O u1 p2 c0  {19,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.46273, 'd12': 1.33701, 'd13': 1.20893},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 35""",
    longDesc = 
u"""
""",
)

entry(
    index = 79,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {9,S} {10,S} {11,S}
2     C u0 p0 c0  {6,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0  {5,S} {15,S} {16,S} {17,S}
4     C u0 p0 c0  {5,S} {18,S} {19,S} {20,S}
5     C u0 p0 c0  {3,S} {4,S} {7,D}
6  *1 C u1 p0 c0  {1,S} {2,S} {7,S}
7  *4 C u0 p0 c0  {5,D} {6,S} {8,S}
8  *2 O u0 p2 c0  {7,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {3,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {4,S}
21 *3 H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {14,S}
4     C u0 p0 c0  {6,S} {17,S} {18,S} {19,S}
5     C u0 p0 c0  {6,S} {15,S} {16,S} {20,S}
6     C u0 p0 c0  {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0  {1,S} {6,D} {21,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {5,S}
21 *1 O u1 p2 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.11212, 'd12': 1.34765, 'd13': 1.30528},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 36""",
    longDesc = 
u"""
""",
)

entry(
    index = 80,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {6,S} {10,S} {11,S} {12,S}
2     C u0 p0 c0  {6,S} {13,S} {14,S} {15,S}
3  *2 C u0 p0 c0  {5,S} {9,S} {18,S} {19,S}
4     C u0 p0 c0  {5,S} {16,S} {17,S} {20,S}
5  *5 C u0 p0 c0  {3,S} {4,S} {7,D}
6  *1 C u1 p0 c0  {1,S} {2,S} {7,S}
7  *4 C u0 p0 c0  {5,D} {6,S} {8,S}
8     O u0 p2 c0  {7,S} {21,S}
9  *3 H u0 p0 c0  {3,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {1,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {2,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {6,S} {9,S}
2     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {15,S}
4     C u0 p0 c0  {5,S} {16,S} {17,S} {18,S}
5  *4 C u0 p0 c0  {4,S} {6,D} {7,S}
6  *5 C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {5,S} {19,S} {20,S}
8     O u0 p2 c0  {6,S} {21,S}
9  *3 H u0 p0 c0  {1,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.53478, 'd12': 1.35287, 'd13': 1.40511},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 37""",
    longDesc = 
u"""
""",
)

entry(
    index = 81,
    reactant1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0  {6,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {6,S} {19,S} {20,S} {21,S}
6     C u0 p0 c0  {4,S} {5,S} {7,D}
7  *6 C u0 p0 c0  {1,S} {6,D} {9,S}
8  *5 O u0 p2 c0  {1,S} {22,S}
9  *2 O u0 p2 c0  {7,S} {23,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22 *1 O u1 p2 c0  {8,S}
23 *3 H u0 p0 c0  {9,S}
""",
    product1 = """
multiplicity 2
1  *6 C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {15,S}
4     C u0 p0 c0  {6,S} {18,S} {19,S} {20,S}
5     C u0 p0 c0  {6,S} {16,S} {17,S} {21,S}
6     C u0 p0 c0  {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0  {1,S} {6,D} {22,S}
8  *5 O u0 p2 c0  {1,S} {9,S}
9  *2 O u0 p2 c0  {8,S} {23,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {5,S}
22 *1 O u1 p2 c0  {7,S}
23 *3 H u0 p0 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.34294, 'd12': 1.29418, 'd13': 1.1198},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 38""",
    longDesc = 
u"""
""",
)

entry(
    index = 82,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0  {4,S} {8,S} {14,S} {15,S}
2     C u0 p0 c0  {4,S} {9,S} {10,S} {16,S}
3     C u0 p0 c0  {5,S} {11,S} {12,S} {13,S}
4  *1 C u1 p0 c0  {1,S} {2,S} {6,S}
5     C u0 p0 c0  {3,S} {6,S} {7,D}
6     C u0 p0 c0  {4,S} {5,S} {17,D}
7     C u0 p0 c0  {5,D} {18,S} {19,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {1,S}
15    H u0 p0 c0  {1,S}
16    H u0 p0 c0  {2,S}
17    O u0 p2 c0  {6,D}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {5,S} {6,S} {8,S}
2     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0  {4,S} {12,S} {13,S} {14,S}
4     C u0 p0 c0  {3,S} {5,S} {7,D}
5     C u0 p0 c0  {1,S} {4,S} {15,D}
6  *1 C u1 p0 c0  {1,S} {16,S} {17,S}
7     C u0 p0 c0  {4,D} {18,S} {19,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    O u0 p2 c0  {5,D}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48422, 'd12': 1.24634, 'd13': 1.37723},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 39""",
    longDesc = 
u"""
""",
)

entry(
    index = 83,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
2     C u0 p0 c0  {4,S} {11,S} {12,S} {13,S}
3  *2 C u0 p0 c0  {5,S} {14,S} {15,S} {16,S}
4  *1 C u1 p0 c0  {1,S} {2,S} {6,S}
5  *5 C u0 p0 c0  {3,S} {6,S} {7,D}
6  *4 C u0 p0 c0  {4,S} {5,S} {17,D}
7     C u0 p0 c0  {5,D} {18,S} {19,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16 *3 H u0 p0 c0  {3,S}
17    O u0 p2 c0  {6,D}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {3,S} {5,S} {8,S}
2     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {14,S}
4  *4 C u0 p0 c0  {5,S} {6,D} {7,S}
5  *5 C u0 p0 c0  {1,S} {4,S} {15,D}
6     C u0 p0 c0  {4,D} {18,S} {19,S}
7  *1 C u1 p0 c0  {4,S} {16,S} {17,S}
8  *3 H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    O u0 p2 c0  {5,D}
16    H u0 p0 c0  {7,S}
17    H u0 p0 c0  {7,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.54909, 'd12': 1.34786, 'd13': 1.3992},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 40""",
    longDesc = 
u"""
""",
)

entry(
    index = 84,
    reactant1 = """
multiplicity 2
1  *6 C u0 p0 c0  {2,S} {3,S} {5,S} {8,S}
2  *2 C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {14,S}
4  *5 C u0 p0 c0  {5,S} {6,D} {7,S}
5  *4 C u0 p0 c0  {1,S} {4,S} {15,D}
6     C u0 p0 c0  {4,D} {18,S} {19,S}
7  *1 C u1 p0 c0  {4,S} {16,S} {17,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11 *3 H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    O u0 p2 c0  {5,D}
16    H u0 p0 c0  {7,S}
17    H u0 p0 c0  {7,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
""",
    product1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,S} {5,S} {6,S} {8,S}
2     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
3  *2 C u0 p0 c0  {4,S} {12,S} {13,S} {14,S}
4  *5 C u0 p0 c0  {3,S} {5,S} {7,D}
5  *6 C u0 p0 c0  {1,S} {4,S} {15,D}
6  *1 C u1 p0 c0  {1,S} {16,S} {17,S}
7     C u0 p0 c0  {4,D} {18,S} {19,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14 *3 H u0 p0 c0  {3,S}
15    O u0 p2 c0  {5,D}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.60352, 'd12': 1.32527, 'd13': 1.38289},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 41""",
    longDesc = 
u"""
""",
)

entry(
    index = 85,
    reactant1 = """
multiplicity 2
1  *6 C u0 p0 c0  {2,S} {3,S} {6,S} {9,S}
2  *2 C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {15,S}
4     C u0 p0 c0  {5,S} {16,S} {17,S} {18,S}
5  *5 C u0 p0 c0  {4,S} {6,D} {7,S}
6  *4 C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {5,S} {19,S} {20,S}
8     O u0 p2 c0  {6,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12 *3 H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {2,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1  *4 C u0 p0 c0  {2,S} {6,S} {7,S} {9,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {5,S} {15,S} {16,S} {17,S}
4  *2 C u0 p0 c0  {5,S} {13,S} {14,S} {18,S}
5  *5 C u0 p0 c0  {3,S} {4,S} {6,D}
6  *6 C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {1,S} {19,S} {20,S}
8     O u0 p2 c0  {6,S} {21,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {3,S}
18 *3 H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.6045, 'd12': 1.34151, 'd13': 1.34645},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 42""",
    longDesc = 
u"""
""",
)

entry(
    index = 86,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {5,S} {12,S} {13,S} {14,S}
2     C u0 p0 c0  {5,S} {15,S} {16,S} {17,S}
3  *2 C u0 p0 c0  {6,S} {9,S} {18,S} {19,S}
4     C u0 p0 c0  {6,S} {10,S} {11,S} {20,S}
5     C u0 p0 c0  {1,S} {2,S} {7,D}
6  *1 C u1 p0 c0  {3,S} {4,S} {7,S}
7     C u0 p0 c0  {5,D} {6,S} {8,S}
8     O u0 p2 c0  {7,S} {21,S}
9  *3 H u0 p0 c0  {3,S}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {1,S}
13    H u0 p0 c0  {1,S}
14    H u0 p0 c0  {1,S}
15    H u0 p0 c0  {2,S}
16    H u0 p0 c0  {2,S}
17    H u0 p0 c0  {2,S}
18    H u0 p0 c0  {3,S}
19    H u0 p0 c0  {3,S}
20    H u0 p0 c0  {4,S}
21    H u0 p0 c0  {8,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0  {2,S} {6,S} {7,S} {9,S}
2     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0  {5,S} {15,S} {16,S} {17,S}
4     C u0 p0 c0  {5,S} {13,S} {14,S} {18,S}
5     C u0 p0 c0  {3,S} {4,S} {6,D}
6     C u0 p0 c0  {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0  {1,S} {19,S} {20,S}
8     O u0 p2 c0  {6,S} {21,S}
9  *3 H u0 p0 c0  {1,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {3,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {7,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49434, 'd12': 1.27782, 'd13': 1.33593},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 43""",
    longDesc = 
u"""
""",
)

