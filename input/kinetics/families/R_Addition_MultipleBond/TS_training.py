#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/TS_training"
shortDesc = u"TS geometries found at M06-2X/6-311+G(2df,2p)"
longDesc = u"""
Put interatomic distances for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

entry(
    index = 1,
    reactant1 = """
1 *2 C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
multiplicity 2
1 *2 C u1 p0 c0 {2,S} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *3 H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.2096, 'd12': 1.32763, 'd13': 1.7757},
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
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *3 C u1 p0 c0 {1,S} {12,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    O u0 p2 c0 {4,D}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *2 C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  *1 C u0 p0 c0 {6,S} {7,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0 {7,S} {17,S} {18,S} {19,S}
6  *3 C u0 p0 c0 {1,S} {2,S} {20,D}
7  *2 C u1 p0 c0 {2,S} {5,S} {21,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {5,S}
20    O u0 p2 c0 {6,D}
21    H u0 p0 c0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.90401, 'd12': 1.35796, 'd13': 2.18876},
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
1     C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4     C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5  *1 C u0 p0 c0 {4,S} {6,S} {7,D}
6     C u0 p0 c0 {1,S} {5,S} {18,D}
7  *2 C u0 p0 c0 {5,D} {19,S} {20,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    O u0 p2 c0 {6,D}
19    H u0 p0 c0 {7,S}
20    H u0 p0 c0 {7,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  *1 C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7  *2 C u1 p0 c0 {2,S} {20,S} {21,S}
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
        distances = {'d23': 2.54564, 'd12': 1.34507, 'd13': 1.892},
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
1     C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5  *1 C u0 p0 c0 {4,S} {6,S} {7,D}
6     C u0 p0 c0 {1,S} {5,S} {19,D}
7  *2 C u0 p0 c0 {5,D} {20,S} {21,S}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {22,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    O u0 p2 c0 {6,D}
20    H u0 p0 c0 {7,S}
21    H u0 p0 c0 {7,S}
22    H u0 p0 c0 {9,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  *1 C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6     C u0 p0 c0 {1,S} {2,S} {20,D}
7  *2 C u1 p0 c0 {2,S} {21,S} {22,S}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
10 *3 H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {5,S}
20    O u0 p2 c0 {6,D}
21    H u0 p0 c0 {7,S}
22    H u0 p0 c0 {7,S}
23    H u0 p0 c0 {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.53897, 'd12': 1.34908, 'd13': 1.865},
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
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *1 C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10 *2 O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,D} {4,S}
3     C u0 p0 c0 {2,D} {8,S} {9,S}
4  *3 C u1 p0 c0 {2,S} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4     C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5     C u0 p0 c0 {4,S} {6,S} {7,D}
6  *3 C u0 p0 c0 {1,S} {5,S} {18,D}
7     C u0 p0 c0 {5,D} {19,S} {20,S}
8  *2 O u1 p2 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    O u0 p2 c0 {6,D}
19    H u0 p0 c0 {7,S}
20    H u0 p0 c0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.58254, 'd12': 1.25663, 'd13': 1.98921},
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
1     C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0 {1,S} {6,S} {17,D}
6  *3 C u1 p0 c0 {4,S} {5,S} {18,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    O u0 p2 c0 {5,D}
18    H u0 p0 c0 {6,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2 *2 O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  *3 C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6  *1 C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0 {1,S} {2,S} {22,D}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19 *2 O u1 p2 c0 {6,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    O u0 p2 c0 {7,D}
""",
    distances = DistanceData(
        distances = {'d23': 2.56593, 'd12': 1.24008, 'd13': 2.0208},
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
1     C u0 p0 c0 {2,S} {3,S} {6,S} {8,S}
2     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4     C u0 p0 c0 {5,S} {15,S} {16,S} {17,S}
5     C u0 p0 c0 {4,S} {6,S} {7,D}
6  *2 C u0 p0 c0 {1,S} {5,S} {18,D}
7     C u0 p0 c0 {5,D} {19,S} {20,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18 *1 O u0 p2 c0 {6,D}
19    H u0 p0 c0 {7,S}
20    H u0 p0 c0 {7,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {5,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0 {4,S} {6,S} {7,D}
6  *2 C u1 p0 c0 {1,S} {5,S} {8,S}
7     C u0 p0 c0 {5,D} {19,S} {20,S}
8  *1 O u0 p2 c0 {6,S} {21,S}
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
        distances = {'d23': 2.37117, 'd12': 1.23113, 'd13': 1.59687},
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
1     C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {5,S} {14,D}
5  *1 C u0 p0 c0 {4,S} {6,D} {15,S}
6  *2 C u0 p0 c0 {5,D} {16,S} {17,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    O u0 p2 c0 {4,D}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {6,S}
17    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  *1 C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  *3 C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7  *2 C u1 p0 c0 {2,S} {20,S} {21,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
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
        distances = {'d23': 2.96305, 'd12': 1.35483, 'd13': 2.26063},
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
1     C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3  *2 C u0 p0 c0 {1,S} {2,S} {4,D}
4  *1 C u0 p0 c0 {3,D} {11,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {3,D} {7,S} {8,S}
3 *3 C u1 p0 c0 {1,S} {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
2     C u0 p0 c0 {4,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0 {5,S} {14,S} {15,S} {16,S}
4  *2 C u1 p0 c0 {1,S} {2,S} {6,S}
5  *3 C u0 p0 c0 {3,S} {6,S} {7,D}
6  *1 C u0 p0 c0 {4,S} {5,S} {17,D}
7     C u0 p0 c0 {5,D} {18,S} {19,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {3,S}
17    O u0 p2 c0 {6,D}
18    H u0 p0 c0 {7,S}
19    H u0 p0 c0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.85259, 'd12': 1.32476, 'd13': 2.18072},
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

