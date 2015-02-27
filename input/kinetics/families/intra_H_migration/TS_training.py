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
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  *2 C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7  *1 C u1 p0 c0 {2,S} {20,S} {21,S}
8     H u0 p0 c0 {1,S}
9  *3 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    O u0 p2 c0 {6,D}
20    H u0 p0 c0 {7,S}
21    H u0 p0 c0 {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  *2 C u0 p0 c0 {6,S} {15,S} {18,S} {19,S}
5     C u0 p0 c0 {6,S} {16,S} {17,S} {20,S}
6  *1 C u1 p0 c0 {4,S} {5,S} {7,S}
7     C u0 p0 c0 {1,S} {6,S} {21,D}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15 *3 H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {4,S}
20    H u0 p0 c0 {5,S}
21    O u0 p2 c0 {7,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.22993, 'd12': 1.47388, 'd13': 1.37611},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 2,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {24,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {14,S} {15,S} {16,S} {23,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {20,S}
13    H u0 p0 c0 {20,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {23,S}
18    O u0 p2 c0 {19,S} {24,S}
19    H u0 p0 c0 {18,S}
20 *2 C u0 p0 c0 {12,S} {13,S} {21,S} {23,S}
21 *3 H u0 p0 c0 {20,S}
22 *4 O u0 p2 c0 {24,S} {25,S}
23 *5 C u0 p0 c0 {4,S} {17,S} {20,S} {24,S}
24 *6 C u0 p0 c0 {1,S} {18,S} {22,S} {23,S}
25 *1 O u1 p2 c0 {22,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {24,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {14,S} {15,S} {16,S} {22,S}
5     O u0 p2 c0 {19,S} {24,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {22,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {25,S}
18    H u0 p0 c0 {25,S}
19    H u0 p0 c0 {5,S}
20 *2 O u0 p2 c0 {21,S} {23,S}
21 *3 H u0 p0 c0 {20,S}
22 *5 C u0 p0 c0 {4,S} {7,S} {24,S} {25,S}
23 *6 O u0 p2 c0 {20,S} {24,S}
24 *4 C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
25 *1 C u1 p0 c0 {17,S} {18,S} {22,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34095, 'd12': 2.40177, 'd13': 1.18969},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 3,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  *2 C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {1,S} {11,S} {12,S} {19,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {20,D}
7  *1 C u1 p0 c0 {2,S} {21,S} {22,S}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
10 *3 H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {4,S}
20    O u0 p2 c0 {6,D}
21    H u0 p0 c0 {7,S}
22    H u0 p0 c0 {7,S}
23    H u0 p0 c0 {9,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  *2 C u0 p0 c0 {6,S} {16,S} {19,S} {20,S}
5     C u0 p0 c0 {6,S} {17,S} {18,S} {21,S}
6  *1 C u1 p0 c0 {4,S} {5,S} {7,S}
7     C u0 p0 c0 {1,S} {6,S} {22,D}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16 *3 H u0 p0 c0 {4,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {4,S}
20    H u0 p0 c0 {4,S}
21    H u0 p0 c0 {5,S}
22    O u0 p2 c0 {7,D}
23    H u0 p0 c0 {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23399, 'd12': 1.47608, 'd13': 1.37785},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 4,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {4,S} {5,S} {6,S} {17,S}
2     H u0 p0 c0 {15,S}
3     H u0 p0 c0 {15,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {13,S}
8     H u0 p0 c0 {13,S}
9     H u0 p0 c0 {19,S}
10    O u0 p2 c0 {20,D}
11    H u0 p0 c0 {19,S}
12    H u0 p0 c0 {21,S}
13    C u0 p0 c0 {7,S} {8,S} {14,S} {21,S}
14    H u0 p0 c0 {13,S}
15    C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
16    H u0 p0 c0 {15,S}
17 *2 C u0 p0 c0 {1,S} {15,S} {18,S} {20,S}
18 *3 H u0 p0 c0 {17,S}
19 *4 C u0 p0 c0 {9,S} {11,S} {21,S} {22,S}
20 *5 C u0 p0 c0 {10,D} {17,S} {21,S}
21 *6 C u0 p0 c0 {12,S} {13,S} {19,S} {20,S}
22 *1 O u1 p2 c0 {19,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {7,S} {8,S} {9,S} {21,S}
2     C u0 p0 c0 {10,S} {11,S} {12,S} {22,S}
3     C u0 p0 c0 {13,S} {14,S} {15,S} {22,S}
4     H u0 p0 c0 {21,S}
5     H u0 p0 c0 {20,S}
6     H u0 p0 c0 {20,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    O u0 p2 c0 {19,D}
17 *2 O u0 p2 c0 {18,S} {20,S}
18 *3 H u0 p0 c0 {17,S}
19 *5 C u0 p0 c0 {16,D} {21,S} {22,S}
20 *6 C u0 p0 c0 {5,S} {6,S} {17,S} {21,S}
21 *4 C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
22 *1 C u1 p0 c0 {2,S} {3,S} {19,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22207, 'd12': 2.47089, 'd13': 1.32293},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 5,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
2  *4 C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3     C u0 p0 c0 {2,S} {8,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0 {1,S} {14,S} {15,S} {19,S}
6  *5 C u0 p0 c0 {1,S} {2,S} {20,D}
7  *1 C u1 p0 c0 {2,S} {21,S} {22,S}
8     O u0 p2 c0 {3,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
10 *3 H u0 p0 c0 {1,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {5,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {5,S}
20    O u0 p2 c0 {6,D}
21    H u0 p0 c0 {7,S}
22    H u0 p0 c0 {7,S}
23    H u0 p0 c0 {9,S}
""",
    product1 = """
multiplicity 2
1  *5 C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2     C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
3  *2 C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  *1 C u1 p0 c0 {4,S} {5,S} {7,S}
7  *4 C u0 p0 c0 {1,S} {6,S} {22,D}
8     O u0 p2 c0 {2,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15 *3 H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {5,S}
20    H u0 p0 c0 {5,S}
21    H u0 p0 c0 {5,S}
22    O u0 p2 c0 {7,D}
23    H u0 p0 c0 {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33714, 'd12': 2.52814, 'd13': 1.4141},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 6,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {7,S} {8,S} {15,S}
2     H u0 p0 c0 {11,S}
3     H u0 p0 c0 {11,S}
4     H u0 p0 c0 {13,S}
5     H u0 p0 c0 {13,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     O u0 p2 c0 {18,D}
10    H u0 p0 c0 {19,S}
11    C u0 p0 c0 {2,S} {3,S} {12,S} {19,S}
12    H u0 p0 c0 {11,S}
13    C u0 p0 c0 {4,S} {5,S} {14,S} {15,S}
14    H u0 p0 c0 {13,S}
15 *2 C u0 p0 c0 {1,S} {13,S} {16,S} {18,S}
16 *3 H u0 p0 c0 {15,S}
17 *4 O u0 p2 c0 {19,S} {20,S}
18 *5 C u0 p0 c0 {9,D} {15,S} {19,S}
19 *6 C u0 p0 c0 {10,S} {11,S} {17,S} {18,S}
20 *1 O u1 p2 c0 {17,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {5,S} {6,S} {7,S} {19,S}
2     C u0 p0 c0 {8,S} {9,S} {10,S} {20,S}
3     C u0 p0 c0 {11,S} {12,S} {13,S} {20,S}
4     H u0 p0 c0 {19,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    O u0 p2 c0 {17,D}
15 *2 O u0 p2 c0 {16,S} {18,S}
16 *3 H u0 p0 c0 {15,S}
17 *5 C u0 p0 c0 {14,D} {19,S} {20,S}
18 *6 O u0 p2 c0 {15,S} {19,S}
19 *4 C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
20 *1 C u1 p0 c0 {2,S} {3,S} {17,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32583, 'd12': 2.43894, 'd13': 1.21819},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 7,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {14,S}
4     C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5  *2 C u0 p0 c0 {6,S} {15,S} {16,S} {20,S}
6  *5 C u0 p0 c0 {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0 {1,S} {6,D} {21,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {4,S}
20 *3 H u0 p0 c0 {5,S}
21 *1 O u1 p2 c0 {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  *4 C u0 p0 c0 {4,S} {6,D} {7,S}
6  *5 C u0 p0 c0 {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0 {5,S} {19,S} {20,S}
8  *2 O u0 p2 c0 {6,S} {21,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {7,S}
20    H u0 p0 c0 {7,S}
21 *3 H u0 p0 c0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40303, 'd12': 2.44145, 'd13': 1.27926},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 8,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {7,S} {8,S} {21,S}
2     H u0 p0 c0 {12,S}
3     H u0 p0 c0 {12,S}
4     H u0 p0 c0 {10,S}
5     H u0 p0 c0 {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     O u0 p2 c0 {20,D}
10    C u0 p0 c0 {4,S} {5,S} {11,S} {21,S}
11    H u0 p0 c0 {10,S}
12    C u0 p0 c0 {2,S} {3,S} {13,S} {17,S}
13    H u0 p0 c0 {12,S}
14    O u0 p2 c0 {15,S} {16,S}
15    H u0 p0 c0 {14,S}
16    O u0 p2 c0 {14,S} {17,S}
17 *2 C u0 p0 c0 {12,S} {16,S} {18,S} {20,S}
18 *3 H u0 p0 c0 {17,S}
19 *4 O u0 p2 c0 {21,S} {22,S}
20 *5 C u0 p0 c0 {9,D} {17,S} {21,S}
21 *6 C u0 p0 c0 {1,S} {10,S} {19,S} {20,S}
22 *1 O u1 p2 c0 {19,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {7,S} {8,S} {21,S}
2     C u0 p0 c0 {9,S} {10,S} {11,S} {21,S}
3     C u0 p0 c0 {12,S} {13,S} {14,S} {22,S}
4     O u0 p2 c0 {5,S} {22,S}
5     O u0 p2 c0 {4,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    O u0 p2 c0 {19,D}
16    H u0 p0 c0 {5,S}
17 *2 O u0 p2 c0 {18,S} {20,S}
18 *3 H u0 p0 c0 {17,S}
19 *5 C u0 p0 c0 {15,D} {21,S} {22,S}
20 *6 O u0 p2 c0 {17,S} {21,S}
21 *4 C u0 p0 c0 {1,S} {2,S} {19,S} {20,S}
22 *1 C u1 p0 c0 {3,S} {4,S} {19,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31841, 'd12': 2.43951, 'd13': 1.2456},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 9,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {14,S}
4     C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5     C u0 p0 c0 {6,S} {15,S} {16,S} {20,S}
6     C u0 p0 c0 {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0 {1,S} {6,D} {21,S}
8  *3 H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {4,S}
20    H u0 p0 c0 {5,S}
21 *1 O u1 p2 c0 {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
2     C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
4     C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5     C u0 p0 c0 {3,S} {4,S} {7,D}
6  *1 C u1 p0 c0 {1,S} {2,S} {7,S}
7  *4 C u0 p0 c0 {5,D} {6,S} {8,S}
8  *2 O u0 p2 c0 {7,S} {21,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {1,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {2,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {3,S}
17    H u0 p0 c0 {3,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {4,S}
20    H u0 p0 c0 {4,S}
21 *3 H u0 p0 c0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3316, 'd12': 2.0903, 'd13': 1.30383},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 10,
    reactant1 = """
multiplicity 2
1  *2 C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {15,S}
4     C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  *4 C u0 p0 c0 {4,S} {6,D} {7,S}
6  *5 C u0 p0 c0 {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0 {5,S} {19,S} {20,S}
8     O u0 p2 c0 {6,S} {21,S}
9  *3 H u0 p0 c0 {1,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {2,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {7,S}
20    H u0 p0 c0 {7,S}
21    H u0 p0 c0 {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
2     C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
3  *2 C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
4     C u0 p0 c0 {5,S} {16,S} {17,S} {20,S}
5  *5 C u0 p0 c0 {3,S} {4,S} {7,D}
6  *1 C u1 p0 c0 {1,S} {2,S} {7,S}
7  *4 C u0 p0 c0 {5,D} {6,S} {8,S}
8     O u0 p2 c0 {7,S} {21,S}
9  *3 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {1,S}
12    H u0 p0 c0 {1,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {2,S}
15    H u0 p0 c0 {2,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {3,S}
19    H u0 p0 c0 {3,S}
20    H u0 p0 c0 {4,S}
21    H u0 p0 c0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34718, 'd12': 2.51412, 'd13': 1.39637},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 11,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {4,S} {5,S} {6,S} {15,S}
2     H u0 p0 c0 {13,S}
3     H u0 p0 c0 {13,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     O u0 p2 c0 {18,D}
8     H u0 p0 c0 {19,S}
9     H u0 p0 c0 {19,S}
10    H u0 p0 c0 {11,S}
11    C u0 p0 c0 {10,S} {12,S} {17,D}
12    H u0 p0 c0 {11,S}
13    C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
14    H u0 p0 c0 {13,S}
15 *2 C u0 p0 c0 {1,S} {13,S} {16,S} {18,S}
16 *3 H u0 p0 c0 {15,S}
17 *4 C u0 p0 c0 {11,D} {18,S} {19,S}
18 *5 C u0 p0 c0 {7,D} {15,S} {17,S}
19 *1 C u1 p0 c0 {8,S} {9,S} {17,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {4,S} {5,S} {6,S} {19,S}
2     C u0 p0 c0 {7,S} {8,S} {9,S} {19,S}
3     C u0 p0 c0 {13,S} {14,S} {18,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {15,S}
11    H u0 p0 c0 {15,S}
12    O u0 p2 c0 {17,D}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15 *2 C u0 p0 c0 {10,S} {11,S} {16,S} {18,S}
16 *3 H u0 p0 c0 {15,S}
17 *4 C u0 p0 c0 {12,D} {18,S} {19,S}
18 *5 C u0 p0 c0 {3,D} {15,S} {17,S}
19 *1 C u1 p0 c0 {1,S} {2,S} {17,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34152, 'd12': 2.53021, 'd13': 1.3996},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-311+G(2df,2p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 12,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4  *2 C u0 p0 c0 {6,S} {15,S} {18,S} {19,S}
5     C u0 p0 c0 {6,S} {16,S} {17,S} {20,S}
6  *1 C u1 p0 c0 {4,S} {5,S} {7,S}
7     C u0 p0 c0 {1,S} {6,S} {21,D}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15 *3 H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {4,S}
20    H u0 p0 c0 {5,S}
21    O u0 p2 c0 {7,D}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  *2 C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7  *1 C u1 p0 c0 {2,S} {20,S} {21,S}
8     H u0 p0 c0 {1,S}
9  *3 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    O u0 p2 c0 {6,D}
20    H u0 p0 c0 {7,S}
21    H u0 p0 c0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47388, 'd12': 1.22993, 'd13': 1.37611},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 13,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {24,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {14,S} {15,S} {16,S} {22,S}
5     O u0 p2 c0 {19,S} {24,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {22,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {25,S}
18    H u0 p0 c0 {25,S}
19    H u0 p0 c0 {5,S}
20 *2 O u0 p2 c0 {21,S} {23,S}
21 *3 H u0 p0 c0 {20,S}
22 *5 C u0 p0 c0 {4,S} {7,S} {24,S} {25,S}
23 *6 O u0 p2 c0 {20,S} {24,S}
24 *4 C u0 p0 c0 {1,S} {5,S} {22,S} {23,S}
25 *1 C u1 p0 c0 {17,S} {18,S} {22,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {24,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {14,S} {15,S} {16,S} {23,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {20,S}
13    H u0 p0 c0 {20,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {23,S}
18    O u0 p2 c0 {19,S} {24,S}
19    H u0 p0 c0 {18,S}
20 *2 C u0 p0 c0 {12,S} {13,S} {21,S} {23,S}
21 *3 H u0 p0 c0 {20,S}
22 *4 O u0 p2 c0 {24,S} {25,S}
23 *5 C u0 p0 c0 {4,S} {17,S} {20,S} {24,S}
24 *6 C u0 p0 c0 {1,S} {18,S} {22,S} {23,S}
25 *1 O u1 p2 c0 {22,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.40177, 'd12': 1.34095, 'd13': 1.18969},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 14,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4  *2 C u0 p0 c0 {6,S} {16,S} {19,S} {20,S}
5     C u0 p0 c0 {6,S} {17,S} {18,S} {21,S}
6  *1 C u1 p0 c0 {4,S} {5,S} {7,S}
7     C u0 p0 c0 {1,S} {6,S} {22,D}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16 *3 H u0 p0 c0 {4,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {4,S}
20    H u0 p0 c0 {4,S}
21    H u0 p0 c0 {5,S}
22    O u0 p2 c0 {7,D}
23    H u0 p0 c0 {9,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  *2 C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {1,S} {11,S} {12,S} {19,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {20,D}
7  *1 C u1 p0 c0 {2,S} {21,S} {22,S}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
10 *3 H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {4,S}
20    O u0 p2 c0 {6,D}
21    H u0 p0 c0 {7,S}
22    H u0 p0 c0 {7,S}
23    H u0 p0 c0 {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47608, 'd12': 1.23399, 'd13': 1.37785},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 15,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {7,S} {8,S} {9,S} {21,S}
2     C u0 p0 c0 {10,S} {11,S} {12,S} {22,S}
3     C u0 p0 c0 {13,S} {14,S} {15,S} {22,S}
4     H u0 p0 c0 {21,S}
5     H u0 p0 c0 {20,S}
6     H u0 p0 c0 {20,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    O u0 p2 c0 {19,D}
17 *2 O u0 p2 c0 {18,S} {20,S}
18 *3 H u0 p0 c0 {17,S}
19 *5 C u0 p0 c0 {16,D} {21,S} {22,S}
20 *6 C u0 p0 c0 {5,S} {6,S} {17,S} {21,S}
21 *4 C u0 p0 c0 {1,S} {4,S} {19,S} {20,S}
22 *1 C u1 p0 c0 {2,S} {3,S} {19,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {4,S} {5,S} {6,S} {17,S}
2     H u0 p0 c0 {15,S}
3     H u0 p0 c0 {15,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {13,S}
8     H u0 p0 c0 {13,S}
9     H u0 p0 c0 {19,S}
10    O u0 p2 c0 {20,D}
11    H u0 p0 c0 {19,S}
12    H u0 p0 c0 {21,S}
13    C u0 p0 c0 {7,S} {8,S} {14,S} {21,S}
14    H u0 p0 c0 {13,S}
15    C u0 p0 c0 {2,S} {3,S} {16,S} {17,S}
16    H u0 p0 c0 {15,S}
17 *2 C u0 p0 c0 {1,S} {15,S} {18,S} {20,S}
18 *3 H u0 p0 c0 {17,S}
19 *4 C u0 p0 c0 {9,S} {11,S} {21,S} {22,S}
20 *5 C u0 p0 c0 {10,D} {17,S} {21,S}
21 *6 C u0 p0 c0 {12,S} {13,S} {19,S} {20,S}
22 *1 O u1 p2 c0 {19,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.47089, 'd12': 1.22207, 'd13': 1.32293},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 16,
    reactant1 = """
multiplicity 2
1  *5 C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2     C u0 p0 c0 {1,S} {8,S} {11,S} {12,S}
3  *2 C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {6,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0 {6,S} {19,S} {20,S} {21,S}
6  *1 C u1 p0 c0 {4,S} {5,S} {7,S}
7  *4 C u0 p0 c0 {1,S} {6,S} {22,D}
8     O u0 p2 c0 {2,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15 *3 H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {5,S}
20    H u0 p0 c0 {5,S}
21    H u0 p0 c0 {5,S}
22    O u0 p2 c0 {7,D}
23    H u0 p0 c0 {9,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0 {4,S} {5,S} {6,S} {10,S}
2  *4 C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3     C u0 p0 c0 {2,S} {8,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0 {1,S} {14,S} {15,S} {19,S}
6  *5 C u0 p0 c0 {1,S} {2,S} {20,D}
7  *1 C u1 p0 c0 {2,S} {21,S} {22,S}
8     O u0 p2 c0 {3,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
10 *3 H u0 p0 c0 {1,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {5,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {5,S}
20    O u0 p2 c0 {6,D}
21    H u0 p0 c0 {7,S}
22    H u0 p0 c0 {7,S}
23    H u0 p0 c0 {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.52814, 'd12': 1.33714, 'd13': 1.4141},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 17,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {5,S} {6,S} {7,S} {19,S}
2     C u0 p0 c0 {8,S} {9,S} {10,S} {20,S}
3     C u0 p0 c0 {11,S} {12,S} {13,S} {20,S}
4     H u0 p0 c0 {19,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    O u0 p2 c0 {17,D}
15 *2 O u0 p2 c0 {16,S} {18,S}
16 *3 H u0 p0 c0 {15,S}
17 *5 C u0 p0 c0 {14,D} {19,S} {20,S}
18 *6 O u0 p2 c0 {15,S} {19,S}
19 *4 C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
20 *1 C u1 p0 c0 {2,S} {3,S} {17,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {7,S} {8,S} {15,S}
2     H u0 p0 c0 {11,S}
3     H u0 p0 c0 {11,S}
4     H u0 p0 c0 {13,S}
5     H u0 p0 c0 {13,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     O u0 p2 c0 {18,D}
10    H u0 p0 c0 {19,S}
11    C u0 p0 c0 {2,S} {3,S} {12,S} {19,S}
12    H u0 p0 c0 {11,S}
13    C u0 p0 c0 {4,S} {5,S} {14,S} {15,S}
14    H u0 p0 c0 {13,S}
15 *2 C u0 p0 c0 {1,S} {13,S} {16,S} {18,S}
16 *3 H u0 p0 c0 {15,S}
17 *4 O u0 p2 c0 {19,S} {20,S}
18 *5 C u0 p0 c0 {9,D} {15,S} {19,S}
19 *6 C u0 p0 c0 {10,S} {11,S} {17,S} {18,S}
20 *1 O u1 p2 c0 {17,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.43894, 'd12': 1.32583, 'd13': 1.21819},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 18,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  *4 C u0 p0 c0 {4,S} {6,D} {7,S}
6  *5 C u0 p0 c0 {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0 {5,S} {19,S} {20,S}
8  *2 O u0 p2 c0 {6,S} {21,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {7,S}
20    H u0 p0 c0 {7,S}
21 *3 H u0 p0 c0 {8,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {14,S}
4     C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5  *2 C u0 p0 c0 {6,S} {15,S} {16,S} {20,S}
6  *5 C u0 p0 c0 {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0 {1,S} {6,D} {21,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {4,S}
20 *3 H u0 p0 c0 {5,S}
21 *1 O u1 p2 c0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.44145, 'd12': 1.40303, 'd13': 1.27926},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 19,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {7,S} {8,S} {21,S}
2     C u0 p0 c0 {9,S} {10,S} {11,S} {21,S}
3     C u0 p0 c0 {12,S} {13,S} {14,S} {22,S}
4     O u0 p2 c0 {5,S} {22,S}
5     O u0 p2 c0 {4,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    O u0 p2 c0 {19,D}
16    H u0 p0 c0 {5,S}
17 *2 O u0 p2 c0 {18,S} {20,S}
18 *3 H u0 p0 c0 {17,S}
19 *5 C u0 p0 c0 {15,D} {21,S} {22,S}
20 *6 O u0 p2 c0 {17,S} {21,S}
21 *4 C u0 p0 c0 {1,S} {2,S} {19,S} {20,S}
22 *1 C u1 p0 c0 {3,S} {4,S} {19,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {7,S} {8,S} {21,S}
2     H u0 p0 c0 {12,S}
3     H u0 p0 c0 {12,S}
4     H u0 p0 c0 {10,S}
5     H u0 p0 c0 {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     O u0 p2 c0 {20,D}
10    C u0 p0 c0 {4,S} {5,S} {11,S} {21,S}
11    H u0 p0 c0 {10,S}
12    C u0 p0 c0 {2,S} {3,S} {13,S} {17,S}
13    H u0 p0 c0 {12,S}
14    O u0 p2 c0 {15,S} {16,S}
15    H u0 p0 c0 {14,S}
16    O u0 p2 c0 {14,S} {17,S}
17 *2 C u0 p0 c0 {12,S} {16,S} {18,S} {20,S}
18 *3 H u0 p0 c0 {17,S}
19 *4 O u0 p2 c0 {21,S} {22,S}
20 *5 C u0 p0 c0 {9,D} {17,S} {21,S}
21 *6 C u0 p0 c0 {1,S} {10,S} {19,S} {20,S}
22 *1 O u1 p2 c0 {19,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.43951, 'd12': 1.31841, 'd13': 1.2456},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 20,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {9,S} {10,S} {11,S}
2     C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
4     C u0 p0 c0 {5,S} {18,S} {19,S} {20,S}
5     C u0 p0 c0 {3,S} {4,S} {7,D}
6  *1 C u1 p0 c0 {1,S} {2,S} {7,S}
7  *4 C u0 p0 c0 {5,D} {6,S} {8,S}
8  *2 O u0 p2 c0 {7,S} {21,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {1,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {2,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {3,S}
17    H u0 p0 c0 {3,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {4,S}
20    H u0 p0 c0 {4,S}
21 *3 H u0 p0 c0 {8,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {14,S}
4     C u0 p0 c0 {6,S} {17,S} {18,S} {19,S}
5     C u0 p0 c0 {6,S} {15,S} {16,S} {20,S}
6     C u0 p0 c0 {4,S} {5,S} {7,D}
7  *4 C u0 p0 c0 {1,S} {6,D} {21,S}
8  *3 H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {4,S}
20    H u0 p0 c0 {5,S}
21 *1 O u1 p2 c0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.0903, 'd12': 1.3316, 'd13': 1.30383},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 21,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {6,S} {10,S} {11,S} {12,S}
2     C u0 p0 c0 {6,S} {13,S} {14,S} {15,S}
3  *2 C u0 p0 c0 {5,S} {9,S} {18,S} {19,S}
4     C u0 p0 c0 {5,S} {16,S} {17,S} {20,S}
5  *5 C u0 p0 c0 {3,S} {4,S} {7,D}
6  *1 C u1 p0 c0 {1,S} {2,S} {7,S}
7  *4 C u0 p0 c0 {5,D} {6,S} {8,S}
8     O u0 p2 c0 {7,S} {21,S}
9  *3 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {1,S}
12    H u0 p0 c0 {1,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {2,S}
15    H u0 p0 c0 {2,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {3,S}
19    H u0 p0 c0 {3,S}
20    H u0 p0 c0 {4,S}
21    H u0 p0 c0 {8,S}
""",
    product1 = """
multiplicity 2
1  *2 C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {15,S}
4     C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  *4 C u0 p0 c0 {4,S} {6,D} {7,S}
6  *5 C u0 p0 c0 {1,S} {5,D} {8,S}
7  *1 C u1 p0 c0 {5,S} {19,S} {20,S}
8     O u0 p2 c0 {6,S} {21,S}
9  *3 H u0 p0 c0 {1,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {2,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    H u0 p0 c0 {7,S}
20    H u0 p0 c0 {7,S}
21    H u0 p0 c0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.51412, 'd12': 1.34718, 'd13': 1.39637},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 22,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {4,S} {5,S} {6,S} {19,S}
2     C u0 p0 c0 {7,S} {8,S} {9,S} {19,S}
3     C u0 p0 c0 {13,S} {14,S} {18,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {15,S}
11    H u0 p0 c0 {15,S}
12    O u0 p2 c0 {17,D}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15 *2 C u0 p0 c0 {10,S} {11,S} {16,S} {18,S}
16 *3 H u0 p0 c0 {15,S}
17 *4 C u0 p0 c0 {12,D} {18,S} {19,S}
18 *5 C u0 p0 c0 {3,D} {15,S} {17,S}
19 *1 C u1 p0 c0 {1,S} {2,S} {17,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {4,S} {5,S} {6,S} {15,S}
2     H u0 p0 c0 {13,S}
3     H u0 p0 c0 {13,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     O u0 p2 c0 {18,D}
8     H u0 p0 c0 {19,S}
9     H u0 p0 c0 {19,S}
10    H u0 p0 c0 {11,S}
11    C u0 p0 c0 {10,S} {12,S} {17,D}
12    H u0 p0 c0 {11,S}
13    C u0 p0 c0 {2,S} {3,S} {14,S} {15,S}
14    H u0 p0 c0 {13,S}
15 *2 C u0 p0 c0 {1,S} {13,S} {16,S} {18,S}
16 *3 H u0 p0 c0 {15,S}
17 *4 C u0 p0 c0 {11,D} {18,S} {19,S}
18 *5 C u0 p0 c0 {7,D} {15,S} {17,S}
19 *1 C u1 p0 c0 {8,S} {9,S} {17,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.53021, 'd12': 1.34152, 'd13': 1.3996},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 11""",
    longDesc = 
u"""
""",
)

