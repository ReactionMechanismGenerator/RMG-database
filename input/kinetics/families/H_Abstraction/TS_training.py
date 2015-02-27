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
1 *3 H u1 p0 c0
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.964372, 'd12': 1.29429, 'd13': 2.25818},
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
1 *1 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 3
1    C u0 p0 c0 {2,S} {3,T}
2 *3 C u2 p0 c0 {1,S} {4,S}
3    C u0 p0 c0 {1,T} {5,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39444, 'd12': 1.16089, 'd13': 2.53998},
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
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38856, 'd12': 1.16829, 'd13': 2.52734},
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
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4872, 'd12': 1.11714, 'd13': 2.58514},
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
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.70887, 'd12': 1.02548, 'd13': 2.71755},
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
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.43871, 'd12': 0.863963, 'd13': 2.30267},
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
1  *1 C u0 p0 c0 {2,B} {6,B} {7,S}
2     C u0 p0 c0 {1,B} {3,B} {8,S}
3     C u0 p0 c0 {2,B} {4,B} {9,S}
4     C u0 p0 c0 {3,B} {5,B} {10,S}
5     C u0 p0 c0 {4,B} {6,B} {11,S}
6     C u0 p0 c0 {1,B} {5,B} {12,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {8,S}
2     C u0 p0 c0 {1,B} {4,B} {7,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29764, 'd12': 1.20143, 'd13': 2.48234},
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
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41939, 'd12': 1.10118, 'd13': 2.51218},
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
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.46367, 'd12': 1.24081, 'd13': 2.69952},
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
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43987, 'd12': 1.23949, 'd13': 2.6721},
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
1 *1 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 3
1    C u0 p0 c0 {2,S} {3,T}
2 *3 C u2 p0 c0 {1,S} {4,S}
3    C u0 p0 c0 {1,T} {5,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43316, 'd12': 1.23879, 'd13': 2.66223},
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
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29485, 'd12': 1.23782, 'd13': 2.51432},
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
    index = 13,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49307, 'd12': 1.22823, 'd13': 2.71466},
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
    index = 14,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40599, 'd12': 1.17506, 'd13': 2.57332},
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
    index = 15,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44974, 'd12': 1.14303, 'd13': 2.5876},
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
    index = 16,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.04792, 'd12': 1.24169, 'd13': 2.28501},
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
    index = 17,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2818, 'd12': 1.26321, 'd13': 2.51752},
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
    index = 18,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42929, 'd12': 1.28937, 'd13': 2.71084},
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
    index = 19,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42317, 'd12': 1.27631, 'd13': 2.6899},
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
    index = 20,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39168, 'd12': 1.28653, 'd13': 2.67292},
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
    index = 21,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39143, 'd12': 1.31802, 'd13': 2.68772},
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
    index = 22,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.11664, 'd12': 1.21509, 'd13': 2.33131},
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
    index = 23,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.5609, 'd12': 1.14278, 'd13': 2.6537},
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
    index = 24,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30413, 'd12': 1.25253, 'd13': 2.53945},
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
    index = 25,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.45419, 'd12': 1.27154, 'd13': 2.71853},
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
    index = 26,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.45239, 'd12': 1.26587, 'd13': 2.71157},
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
    index = 27,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.41583, 'd12': 0.875435, 'd13': 2.28904},
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
    index = 28,
    reactant1 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30794, 'd12': 1.19826, 'd13': 2.48347},
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
    index = 29,
    reactant1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.64481, 'd12': 1.03948, 'd13': 2.65148},
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
    index = 30,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40308, 'd12': 1.1138, 'd13': 2.50659},
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
    index = 31,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33973, 'd12': 1.31116, 'd13': 2.64253},
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
    index = 32,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.51519, 'd12': 1.22123, 'd13': 2.7132},
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
    index = 33,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50467, 'd12': 1.21775, 'd13': 2.71729},
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
    index = 34,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.56363, 'd12': 1.2049, 'd13': 2.75678},
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
    index = 35,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {3,D} {4,S} {5,S}
2 *1 C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38273, 'd12': 1.30549, 'd13': 2.68461},
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
    index = 36,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42468, 'd12': 1.25087, 'd13': 2.66446},
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
    index = 37,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38408, 'd12': 1.31908, 'd13': 2.70098},
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
    index = 38,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,B} {6,B} {7,S}
2     C u0 p0 c0 {1,B} {3,B} {8,S}
3     C u0 p0 c0 {2,B} {4,B} {9,S}
4     C u0 p0 c0 {3,B} {5,B} {10,S}
5     C u0 p0 c0 {4,B} {6,B} {11,S}
6     C u0 p0 c0 {1,B} {5,B} {12,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {8,S}
2     C u0 p0 c0 {1,B} {4,B} {7,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.64103, 'd12': 1.13377, 'd13': 2.77186},
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
    index = 39,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.81579, 'd12': 1.12895, 'd13': 2.80635},
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
    index = 40,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.92436, 'd12': 1.11842, 'd13': 2.92561},
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
    index = 41,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.63784, 'd12': 1.1357, 'd13': 2.74708},
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
    index = 42,
    reactant1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.69229, 'd12': 1.03032, 'd13': 2.70779},
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
    index = 43,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40439, 'd12': 1.11246, 'd13': 2.50817},
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
    index = 44,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3329, 'd12': 1.31533, 'd13': 2.64119},
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
    index = 45,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.52719, 'd12': 1.21725, 'd13': 2.73396},
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
    index = 46,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.55054, 'd12': 1.21065, 'd13': 2.75365},
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
    index = 47,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42807, 'd12': 1.25311, 'd13': 2.68089},
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
    index = 48,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.6608, 'd12': 1.13352, 'd13': 2.782},
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
    index = 49,
    reactant1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.64509, 'd12': 1.04109, 'd13': 2.67214},
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
    index = 50,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36766, 'd12': 1.14267, 'd13': 2.50461},
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
    index = 51,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.37662, 'd12': 1.28554, 'd13': 2.65879},
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
    index = 52,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47766, 'd12': 1.23787, 'd13': 2.70705},
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
    index = 53,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.52564, 'd12': 1.22146, 'd13': 2.72915},
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
    index = 54,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39444, 'd12': 1.27301, 'd13': 2.66332},
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
    index = 55,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.89387, 'd12': 1.39367, 'd13': 2.28754},
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
    index = 56,
    reactant1 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34972, 'd12': 1.18721, 'd13': 2.53015},
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
    index = 57,
    reactant1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.57678, 'd12': 1.06293, 'd13': 2.63067},
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
    index = 58,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37511, 'd12': 1.2924, 'd13': 2.66748},
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
    index = 59,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.51722, 'd12': 1.22886, 'd13': 2.74275},
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
    index = 60,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33927, 'd12': 1.17376, 'd13': 2.50779},
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
    index = 61,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49143, 'd12': 1.24581, 'd13': 2.7249},
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
    index = 62,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36677, 'd12': 1.30866, 'd13': 2.66791},
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
    index = 63,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31076, 'd12': 1.20167, 'd13': 2.50733},
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
    index = 64,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43905, 'd12': 1.27756, 'd13': 2.70403},
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
    index = 65,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41101, 'd12': 1.28593, 'd13': 2.6921},
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
    index = 66,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33751, 'd12': 1.33117, 'd13': 2.66142},
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
    index = 67,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.83964, 'd12': 1.12062, 'd13': 2.84485},
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
    index = 68,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48294, 'd12': 1.238, 'd13': 2.72057},
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
    index = 69,
    reactant1 = """
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
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4568, 'd12': 1.25432, 'd13': 2.70702},
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
    index = 70,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33047, 'd12': 1.32017, 'd13': 2.63625},
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
    index = 71,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.36116, 'd12': 1.3004, 'd13': 2.65083},
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
    index = 72,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47886, 'd12': 1.23665, 'd13': 2.70715},
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
    index = 73,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.36623, 'd12': 1.29405, 'd13': 2.64922},
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
    index = 74,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40726, 'd12': 1.27435, 'd13': 2.67949},
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
    index = 75,
    reactant1 = """
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
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37471, 'd12': 1.30736, 'd13': 2.6748},
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
    index = 76,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40177, 'd12': 1.2989, 'd13': 2.69039},
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
    index = 77,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40281, 'd12': 1.27912, 'd13': 2.68031},
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
    index = 78,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4322, 'd12': 1.25852, 'd13': 2.68364},
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
    index = 79,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.51572, 'd12': 1.08374, 'd13': 2.58042},
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
    index = 80,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    C u0 p0 c0 {1,D} {4,D}
3    H u0 p0 c0 {1,S}
4    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.28541, 'd12': 1.20894, 'd13': 2.37828},
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
    index = 81,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36667, 'd12': 1.13828, 'd13': 2.43193},
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
    index = 82,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.46309, 'd12': 1.21615, 'd13': 2.67111},
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
    index = 83,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.5019, 'd12': 1.20339, 'd13': 2.68918},
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
    index = 84,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.56813, 'd12': 1.19207, 'd13': 2.72322},
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
    index = 85,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.54305, 'd12': 1.19879, 'd13': 2.70826},
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
    index = 86,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32292, 'd12': 1.30622, 'd13': 2.62821},
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
    index = 87,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37254, 'd12': 1.26828, 'd13': 2.63862},
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
    index = 88,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4223, 'd12': 1.23012, 'd13': 2.64379},
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
    index = 89,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 *2 H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.46132, 'd12': 1.13702, 'd13': 2.52224},
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
    index = 90,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4     C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
5     C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  *3 C u1 p0 c0 {4,S} {5,S} {7,S}
7     C u0 p0 c0 {1,S} {6,S} {21,D}
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
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {5,S}
20    H u0 p0 c0 {5,S}
21    O u0 p2 c0 {7,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0 {1,S} {2,S} {22,D}
8  *2 H u0 p0 c0 {1,S}
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
19    H u0 p0 c0 {6,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    O u0 p2 c0 {7,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34343, 'd12': 1.38352, 'd13': 2.70046},
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
    index = 91,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7  *3 C u1 p0 c0 {2,S} {20,S} {21,S}
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
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3  *1 C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0 {1,S} {2,S} {22,D}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12 *2 H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {6,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    O u0 p2 c0 {7,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44639, 'd12': 1.28896, 'd13': 2.71347},
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
    index = 92,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26913, 'd12': 1.27438, 'd13': 2.50503},
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
    index = 93,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39946, 'd12': 1.31001, 'd13': 2.69203},
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
    index = 94,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.51853, 'd12': 1.23244, 'd13': 2.7239},
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
    index = 95,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3732, 'd12': 1.35064, 'd13': 2.69115},
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
    index = 96,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43643, 'd12': 1.31218, 'd13': 2.70729},
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
    index = 97,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41139, 'd12': 1.32975, 'd13': 2.71528},
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
    index = 98,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47526, 'd12': 1.26216, 'd13': 2.72997},
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
    index = 99,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47729, 'd12': 1.2668, 'd13': 2.74286},
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
    index = 100,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41644, 'd12': 1.31562, 'd13': 2.69363},
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
    index = 101,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48263, 'd12': 1.12284, 'd13': 2.54708},
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
    index = 102,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50472, 'd12': 1.15063, 'd13': 2.57058},
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
    index = 103,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.45716, 'd12': 1.25056, 'd13': 2.68233},
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
    index = 104,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39238, 'd12': 1.32359, 'd13': 2.67219},
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
    index = 105,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40064, 'd12': 1.31014, 'd13': 2.68538},
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
    index = 106,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.46371, 'd12': 1.27727, 'd13': 2.70354},
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
    index = 107,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43159, 'd12': 1.3068, 'd13': 2.69787},
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
    index = 108,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44012, 'd12': 1.26318, 'd13': 2.67317},
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
    index = 109,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41572, 'd12': 1.28156, 'd13': 2.67526},
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
    index = 110,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41933, 'd12': 1.28625, 'd13': 2.70078},
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
    index = 111,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39091, 'd12': 1.3141, 'd13': 2.68879},
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
    index = 112,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36275, 'd12': 1.34136, 'd13': 2.67914},
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
    index = 113,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3  *1 C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0 {1,S} {2,S} {22,D}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10 *2 H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {6,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    O u0 p2 c0 {7,D}
""",
    reactant2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7  *3 C u1 p0 c0 {2,S} {20,S} {21,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    O u0 p2 c0 {6,D}
20    H u0 p0 c0 {7,S}
21    H u0 p0 c0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36244, 'd12': 1.304, 'd13': 2.65247},
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
    index = 114,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.37462, 'd12': 0.893488, 'd13': 2.2681},
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
    index = 115,
    reactant1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.62095, 'd12': 1.04106, 'd13': 2.65255},
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
    index = 116,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.51602, 'd12': 1.21541, 'd13': 2.72728},
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
    index = 117,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41049, 'd12': 1.26532, 'd13': 2.6758},
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
    index = 118,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 3
1    C u0 p0 c0 {2,T} {3,S}
2    C u0 p0 c0 {1,T} {4,S}
3 *3 C u2 p0 c0 {1,S} {5,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.71577, 'd12': 1.12253, 'd13': 2.83796},
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
    index = 119,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    product1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.18564, 'd12': 1.31451, 'd13': 2.5001},
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
    index = 120,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.46401, 'd12': 1.13544, 'd13': 2.54805},
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
    index = 121,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    product1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23278, 'd12': 1.28296, 'd13': 2.4907},
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
    index = 122,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39273, 'd12': 1.17282, 'd13': 2.56055},
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
    index = 123,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30097, 'd12': 1.05464, 'd13': 2.25495},
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
    index = 124,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32482, 'd12': 1.18908, 'd13': 2.50813},
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
    index = 125,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26753, 'd12': 1.0907, 'd13': 2.34208},
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
    index = 126,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33628, 'd12': 1.37417, 'd13': 2.67587},
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
    index = 127,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38, 'd12': 1.28916, 'd13': 2.66232},
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
    index = 128,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32124, 'd12': 1.37262, 'd13': 2.64429},
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
    index = 129,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47985, 'd12': 1.23639, 'd13': 2.68474},
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
    index = 130,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42761, 'd12': 1.28225, 'd13': 2.70662},
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
    index = 131,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37945, 'd12': 1.33156, 'd13': 2.68289},
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
    index = 132,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34423, 'd12': 1.20738, 'd13': 2.54626},
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
    index = 133,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39458, 'd12': 1.32327, 'd13': 2.69545},
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
    index = 134,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50198, 'd12': 1.23984, 'd13': 2.73677},
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
    index = 135,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44872, 'd12': 1.28502, 'd13': 2.69905},
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
    index = 136,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47083, 'd12': 1.25307, 'd13': 2.71417},
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
    index = 137,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42257, 'd12': 1.30437, 'd13': 2.69066},
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
    index = 138,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.46842, 'd12': 1.24444, 'd13': 2.69949},
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
    index = 139,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38892, 'd12': 1.28245, 'd13': 2.66834},
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
    index = 140,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2896, 'd12': 1.19204, 'd13': 2.477},
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
    index = 141,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43501, 'd12': 1.26947, 'd13': 2.68027},
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
    index = 142,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26004, 'd12': 1.23172, 'd13': 2.48996},
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
    index = 143,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35476, 'd12': 1.33091, 'd13': 2.68227},
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
    index = 144,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40708, 'd12': 1.30452, 'd13': 2.69633},
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
    index = 145,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38322, 'd12': 1.3046, 'd13': 2.68341},
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
    index = 146,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31493, 'd12': 1.21874, 'd13': 2.53143},
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
    index = 147,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25118, 'd12': 1.22278, 'd13': 2.46055},
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
    index = 148,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 3
1    C u0 p0 c0 {2,T} {3,S}
2    C u0 p0 c0 {1,T} {4,S}
3 *3 C u2 p0 c0 {1,S} {5,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35141, 'd12': 1.31744, 'd13': 2.65773},
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
    index = 149,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.87771, 'd12': 1.12539, 'd13': 2.78624},
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
    index = 150,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50082, 'd12': 1.19919, 'd13': 2.66425},
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
    index = 151,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38457, 'd12': 1.36, 'd13': 2.63632},
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
    index = 152,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37526, 'd12': 1.34617, 'd13': 2.66976},
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
    index = 153,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41971, 'd12': 1.28767, 'd13': 2.70294},
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
    index = 154,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38278, 'd12': 1.1862, 'd13': 2.54826},
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
    index = 155,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.69997, 'd12': 1.1331, 'd13': 2.81507},
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
    index = 156,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36612, 'd12': 1.26716, 'd13': 2.63108},
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
    index = 157,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.46034, 'd12': 1.28021, 'd13': 2.72254},
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
    index = 158,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39917, 'd12': 1.30263, 'd13': 2.69753},
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
    index = 159,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27793, 'd12': 1.19687, 'd13': 2.41073},
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
    index = 160,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38043, 'd12': 1.19469, 'd13': 2.54285},
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
    index = 161,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.988982, 'd12': 1.2835, 'd13': 2.2699},
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
    index = 162,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    product1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24337, 'd12': 1.26594, 'd13': 2.509},
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
    index = 163,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3371, 'd12': 1.33898, 'd13': 2.67345},
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
    index = 164,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.41884, 'd12': 1.29899, 'd13': 2.71053},
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
    index = 165,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38198, 'd12': 1.31509, 'd13': 2.69476},
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
    index = 166,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35777, 'd12': 1.38142, 'd13': 2.73419},
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
    index = 167,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.51077, 'd12': 1.23815, 'd13': 2.71907},
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
    index = 168,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.48187, 'd12': 1.26406, 'd13': 2.72247},
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
    index = 169,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37596, 'd12': 1.31358, 'd13': 2.67539},
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
    index = 170,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36561, 'd12': 1.34478, 'd13': 2.67719},
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
    index = 171,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.39001, 'd12': 1.36326, 'd13': 2.64477},
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
    index = 172,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41906, 'd12': 1.28374, 'd13': 2.68723},
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
    index = 173,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.47522, 'd12': 1.27669, 'd13': 2.73719},
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
    index = 174,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28001, 'd12': 1.23891, 'd13': 2.503},
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
    index = 175,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.41532, 'd12': 1.18584, 'd13': 2.57286},
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
    index = 176,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.62371, 'd12': 1.17982, 'd13': 2.78509},
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
    index = 177,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.42279, 'd12': 1.3191, 'd13': 2.72768},
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
    index = 178,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,D}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    O u0 p2 c0 {1,D}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.69131, 'd12': 1.13807, 'd13': 2.82491},
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
    index = 179,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41002, 'd12': 1.32077, 'd13': 2.72822},
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
    index = 180,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36251, 'd12': 1.36017, 'd13': 2.63431},
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
    index = 181,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.923854, 'd12': 1.3556, 'd13': 2.27781},
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
    index = 182,
    reactant1 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42871, 'd12': 1.16128, 'd13': 2.58129},
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
    index = 183,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33003, 'd12': 1.18051, 'd13': 2.502},
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
    index = 184,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48928, 'd12': 1.24657, 'd13': 2.72313},
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
    index = 185,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36484, 'd12': 1.30523, 'd13': 2.66293},
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
    index = 186,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.77031, 'd12': 1.12448, 'd13': 2.84901},
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
    index = 187,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40632, 'd12': 1.27848, 'd13': 2.67973},
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
    index = 188,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40141, 'd12': 1.2791, 'd13': 2.67322},
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
    index = 189,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44276, 'd12': 1.2938, 'd13': 2.71507},
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
    index = 190,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38918, 'd12': 1.31607, 'd13': 2.68893},
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
    index = 191,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35819, 'd12': 1.32896, 'd13': 2.67947},
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
    index = 192,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40589, 'd12': 1.30228, 'd13': 2.68903},
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
    index = 193,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.4566, 'd12': 1.29072, 'd13': 2.74355},
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
    index = 194,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34484, 'd12': 1.34625, 'd13': 2.6847},
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
    index = 195,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37018, 'd12': 1.31863, 'd13': 2.68547},
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
    index = 196,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 3
1    C u0 p0 c0 {2,D} {3,D}
2 *3 C u2 p0 c0 {1,D}
3    O u0 p2 c0 {1,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.42541, 'd12': 1.23814, 'd13': 2.5461},
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
    index = 197,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 3
1    C u0 p0 c0 {2,D} {3,D}
2 *3 C u2 p0 c0 {1,D}
3    O u0 p2 c0 {1,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.45282, 'd12': 1.22447, 'd13': 2.65518},
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
    index = 198,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 3
1    C u0 p0 c0 {2,D} {3,D}
2 *3 C u2 p0 c0 {1,D}
3    O u0 p2 c0 {1,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.45534, 'd12': 1.22851, 'd13': 2.66445},
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
    index = 199,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 3
1    C u0 p0 c0 {2,D} {3,D}
2 *3 C u2 p0 c0 {1,D}
3    O u0 p2 c0 {1,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.41193, 'd12': 1.25782, 'd13': 2.66063},
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
    index = 200,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.80501, 'd12': 1.12964, 'd13': 2.73886},
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
    index = 201,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40076, 'd12': 1.34446, 'd13': 2.64444},
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
    index = 202,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36887, 'd12': 1.29557, 'd13': 2.65918},
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
    index = 203,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.38361, 'd12': 1.32882, 'd13': 2.69912},
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
    index = 204,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.49058, 'd12': 1.2296, 'd13': 2.71452},
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
    index = 205,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36733, 'd12': 1.34518, 'd13': 2.70794},
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
    index = 206,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.47374, 'd12': 1.24093, 'd13': 2.70515},
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
    index = 207,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.44373, 'd12': 1.26608, 'd13': 2.70924},
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
    index = 208,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.3583, 'd12': 1.35377, 'd13': 2.67764},
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
    index = 209,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.36702, 'd12': 1.20098, 'd13': 2.55933},
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
    index = 210,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.39821, 'd12': 1.34864, 'd13': 2.74343},
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
    index = 211,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.92365, 'd12': 1.11369, 'd13': 3.02434},
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
    index = 212,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,D}
2    H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.38045, 'd12': 1.3605, 'd13': 2.71051},
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
    index = 213,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26977, 'd12': 1.28834, 'd13': 2.55114},
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
    index = 214,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38621, 'd12': 1.35154, 'd13': 2.72595},
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
    index = 215,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43828, 'd12': 1.31832, 'd13': 2.73038},
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
    index = 216,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.40546, 'd12': 1.30526, 'd13': 2.70487},
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
    index = 217,
    reactant1 = """
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
    reactant2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.47802, 'd12': 1.26354, 'd13': 2.73766},
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
    index = 218,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.51687, 'd12': 1.24541, 'd13': 2.75861},
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
    index = 219,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3858, 'd12': 1.39696, 'd13': 2.78275},
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
    index = 220,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.41741, 'd12': 1.32835, 'd13': 2.72713},
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
    index = 221,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.46084, 'd12': 1.28825, 'd13': 2.74272},
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
    index = 222,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.43639, 'd12': 1.29948, 'd13': 2.72285},
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
    index = 223,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.44902, 'd12': 1.30052, 'd13': 2.74595},
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
    index = 224,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.43782, 'd12': 0.86239, 'd13': 2.2983},
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
    index = 225,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.52486, 'd12': 1.20715, 'd13': 2.72106},
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
    index = 226,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42033, 'd12': 1.26356, 'd13': 2.67127},
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
    index = 227,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.45416, 'd12': 1.24194, 'd13': 2.68962},
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
    index = 228,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.934703, 'd12': 1.32577, 'd13': 2.25494},
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
    index = 229,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44101, 'd12': 1.25686, 'd13': 2.6938},
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
    index = 230,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41709, 'd12': 1.27452, 'd13': 2.68689},
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
    index = 231,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38363, 'd12': 1.30557, 'd13': 2.66673},
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
    index = 232,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40233, 'd12': 1.28694, 'd13': 2.66635},
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
    index = 233,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.44337, 'd12': 1.27972, 'd13': 2.70939},
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
    index = 234,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  *1 C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6     C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
7     C u0 p0 c0 {1,S} {2,S} {23,D}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {24,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17 *2 H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {5,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    H u0 p0 c0 {6,S}
23    O u0 p2 c0 {7,D}
24    H u0 p0 c0 {9,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6     C u0 p0 c0 {1,S} {2,S} {20,D}
7  *3 C u1 p0 c0 {2,S} {21,S} {22,S}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
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
22    H u0 p0 c0 {7,S}
23    H u0 p0 c0 {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.916182, 'd12': 1.36184, 'd13': 2.27416},
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
    index = 235,
    reactant1 = """
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
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {5,S} {14,D}
5     O u0 p2 c0 {4,S} {6,S}
6  *1 O u0 p2 c0 {5,S} {15,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    O u0 p2 c0 {4,D}
15 *2 H u0 p0 c0 {6,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {5,S} {13,D}
5     O u0 p2 c0 {4,S} {14,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    O u0 p2 c0 {4,D}
14 *3 O u1 p2 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30031, 'd12': 1.20349, 'd13': 2.49703},
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
    index = 236,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {5,S} {13,D}
5     O u0 p2 c0 {4,S} {14,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    O u0 p2 c0 {4,D}
14 *3 O u1 p2 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {5,S} {14,D}
5     O u0 p2 c0 {4,S} {6,S}
6  *1 O u0 p2 c0 {5,S} {15,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    O u0 p2 c0 {4,D}
15 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31034, 'd12': 1.24357, 'd13': 2.51754},
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
    index = 237,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47468, 'd12': 1.13391, 'd13': 2.58993},
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
    index = 238,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.02425, 'd12': 1.27258, 'd13': 2.29683},
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
    index = 239,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    product1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.38024, 'd12': 1.19795, 'd13': 2.57366},
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
    index = 240,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.56688, 'd12': 1.13826, 'd13': 2.68698},
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
    index = 241,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.39021, 'd12': 1.33334, 'd13': 2.71645},
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
    index = 242,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.38866, 'd12': 1.31592, 'd13': 2.68893},
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
    index = 243,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.47821, 'd12': 1.24309, 'd13': 2.70749},
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
    index = 244,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.45209, 'd12': 1.26427, 'd13': 2.70747},
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
    index = 245,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.38658, 'd12': 1.32269, 'd13': 2.70085},
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
    index = 246,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,D} {4,S}
2    H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.36693, 'd12': 1.3794, 'd13': 2.71184},
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
    index = 247,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.50228, 'd12': 1.22756, 'd13': 2.71548},
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
    index = 248,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3     C u0 p0 c0 {2,S} {5,S} {10,D}
4     C u0 p0 c0 {2,D} {11,S} {12,S}
5     O u0 p2 c0 {3,S} {6,S}
6  *1 O u0 p2 c0 {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {1,S}
10    O u0 p2 c0 {3,D}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
13 *2 H u0 p0 c0 {6,S}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3     C u0 p0 c0 {2,S} {5,S} {9,D}
4     C u0 p0 c0 {2,D} {10,S} {11,S}
5     O u0 p2 c0 {3,S} {12,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     O u0 p2 c0 {3,D}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
12 *3 O u1 p2 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.937577, 'd12': 1.17221, 'd13': 2.10708},
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
    index = 249,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3     C u0 p0 c0 {2,S} {5,S} {9,D}
4     C u0 p0 c0 {2,D} {10,S} {11,S}
5     O u0 p2 c0 {3,S} {12,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     O u0 p2 c0 {3,D}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
12 *3 O u1 p2 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3     C u0 p0 c0 {2,S} {5,S} {10,D}
4     C u0 p0 c0 {2,D} {11,S} {12,S}
5     O u0 p2 c0 {3,S} {6,S}
6  *1 O u0 p2 c0 {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {1,S}
10    O u0 p2 c0 {3,D}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
13 *2 H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.39989, 'd12': 1.20258, 'd13': 2.57887},
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
    index = 250,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.977884, 'd12': 1.29246, 'd13': 2.26945},
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
    index = 251,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    product1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24182, 'd12': 1.26772, 'd13': 2.50718},
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
    index = 252,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3975, 'd12': 1.17334, 'd13': 2.55818},
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
    index = 253,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35655, 'd12': 1.3314, 'd13': 2.68729},
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
    index = 254,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34695, 'd12': 1.33117, 'd13': 2.67376},
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
    index = 255,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39115, 'd12': 1.31181, 'd13': 2.6992},
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
    index = 256,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44434, 'd12': 1.25117, 'd13': 2.6909},
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
    index = 257,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38996, 'd12': 1.304, 'd13': 2.69336},
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
    index = 258,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36322, 'd12': 1.32744, 'd13': 2.67448},
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
    index = 259,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37871, 'd12': 1.33278, 'd13': 2.68099},
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
    index = 260,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39121, 'd12': 1.30451, 'd13': 2.69447},
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
    index = 261,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.43504, 'd12': 1.3104, 'd13': 2.73412},
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
    index = 262,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,D}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    O u0 p2 c0 {1,D}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34492, 'd12': 1.33375, 'd13': 2.6698},
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
    index = 263,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40806, 'd12': 1.24384, 'd13': 2.6519},
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
    index = 264,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35705, 'd12': 1.34429, 'd13': 2.69505},
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
    index = 265,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.7064, 'd12': 1.13451, 'd13': 2.82673},
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
    index = 266,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.39347, 'd12': 1.31947, 'd13': 2.70389},
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
    index = 267,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.42272, 'd12': 1.3159, 'd13': 2.7251},
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
    index = 268,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37193, 'd12': 1.30083, 'd13': 2.67241},
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
    index = 269,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2  *1 C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41027, 'd12': 1.28525, 'd13': 2.69021},
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
    index = 270,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37277, 'd12': 1.33035, 'd13': 2.69608},
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
    index = 271,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.04276, 'd12': 1.25278, 'd13': 2.2939},
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
    index = 272,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50747, 'd12': 1.22446, 'd13': 2.72203},
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
    index = 273,
    reactant1 = """
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
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48174, 'd12': 1.24194, 'd13': 2.71985},
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
    index = 274,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1    C u0 p0 c0 {3,D} {4,S} {5,S}
2 *1 C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41098, 'd12': 1.29177, 'd13': 2.69187},
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
    index = 275,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44527, 'd12': 1.25846, 'd13': 2.69783},
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
    index = 276,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50298, 'd12': 1.23044, 'd13': 2.73213},
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
    index = 277,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2  *1 C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49618, 'd12': 1.23344, 'd13': 2.72066},
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
    index = 278,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,D} {9,S}
3  *3 C u1 p0 c0 {1,S} {5,S} {10,S}
4     C u0 p0 c0 {2,D} {6,S} {12,S}
5     C u0 p0 c0 {3,S} {6,D} {13,S}
6     C u0 p0 c0 {4,S} {5,D} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.10827, 'd12': 1.22195, 'd13': 2.31786},
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
    index = 279,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49591, 'd12': 1.22334, 'd13': 2.70803},
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
    index = 280,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.925569, 'd12': 1.34474, 'd13': 2.26775},
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
    index = 281,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37475, 'd12': 1.17381, 'd13': 2.52182},
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
    index = 282,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48476, 'd12': 1.15346, 'd13': 2.61123},
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
    index = 283,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.55043, 'd12': 1.14956, 'd13': 2.63671},
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
    index = 284,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.51283, 'd12': 1.09601, 'd13': 2.5987},
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
    index = 285,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {10,S}
4     C u0 p0 c0 {3,S} {5,D} {11,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40169, 'd12': 1.17121, 'd13': 2.56276},
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
    index = 286,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,D} {9,S}
3  *3 C u1 p0 c0 {1,S} {5,S} {10,S}
4     C u0 p0 c0 {2,D} {6,S} {11,S}
5     C u0 p0 c0 {3,S} {6,D} {12,S}
6     C u0 p0 c0 {4,S} {5,D} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,D} {11,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3926, 'd12': 1.19836, 'd13': 2.58114},
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
    index = 287,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2  *1 C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33502, 'd12': 1.17101, 'd13': 2.4995},
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
    index = 288,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27831, 'd12': 1.2625, 'd13': 2.53577},
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
    index = 289,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31685, 'd12': 1.25002, 'd13': 2.55894},
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
    index = 290,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.45773, 'd12': 1.24326, 'd13': 2.69413},
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
    index = 291,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2  *1 C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35764, 'd12': 1.30619, 'd13': 2.65607},
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
    index = 292,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3  *1 C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32869, 'd12': 1.31915, 'd13': 2.6379},
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
    index = 293,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2  *1 C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39908, 'd12': 1.26785, 'd13': 2.66171},
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
    index = 294,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38457, 'd12': 1.28122, 'd13': 2.65101},
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
    index = 295,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38786, 'd12': 1.27479, 'd13': 2.65584},
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
    index = 296,
    reactant1 = """
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
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31616, 'd12': 1.34806, 'd13': 2.66402},
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
    index = 297,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40244, 'd12': 1.26407, 'd13': 2.6525},
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
    index = 298,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.40769, 'd12': 1.29046, 'd13': 2.69234},
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
    index = 299,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33775, 'd12': 1.31168, 'd13': 2.63523},
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
    index = 300,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41052, 'd12': 1.27788, 'd13': 2.68277},
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
    index = 301,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4522, 'd12': 1.26652, 'd13': 2.7145},
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
    index = 302,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49045, 'd12': 1.25108, 'd13': 2.73836},
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
    index = 303,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43051, 'd12': 1.26709, 'd13': 2.67652},
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
    index = 304,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.56756, 'd12': 1.19956, 'd13': 2.73629},
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
    index = 305,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39501, 'd12': 1.34171, 'd13': 2.71439},
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
    index = 306,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,D} {9,S}
3  *3 C u1 p0 c0 {1,S} {5,S} {10,S}
4     C u0 p0 c0 {2,D} {6,S} {12,S}
5     C u0 p0 c0 {3,S} {6,D} {13,S}
6     C u0 p0 c0 {4,S} {5,D} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40518, 'd12': 1.33317, 'd13': 2.67611},
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
    index = 307,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.46478, 'd12': 1.27675, 'd13': 2.71438},
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
    index = 308,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.46049, 'd12': 1.26293, 'd13': 2.72099},
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
    index = 309,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36954, 'd12': 1.19996, 'd13': 2.55492},
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
    index = 310,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44841, 'd12': 1.2915, 'd13': 2.72027},
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
    index = 311,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30771, 'd12': 1.3715, 'd13': 2.67317},
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
    index = 312,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22374, 'd12': 1.26262, 'd13': 2.47315},
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
    index = 313,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3  *1 C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29281, 'd12': 1.19167, 'd13': 2.46742},
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
    index = 314,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4035, 'd12': 1.3031, 'd13': 2.69908},
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
    index = 315,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38149, 'd12': 1.30426, 'd13': 2.67549},
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
    index = 316,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,D}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    O u0 p2 c0 {1,D}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4648, 'd12': 1.24191, 'd13': 2.69416},
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
    index = 317,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48985, 'd12': 1.2516, 'd13': 2.73592},
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
    index = 318,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.45256, 'd12': 1.25253, 'd13': 2.67681},
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
    index = 319,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,D}
2    H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.51785, 'd12': 1.23344, 'd13': 2.73543},
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
    index = 320,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.42103, 'd12': 1.30563, 'd13': 2.7049},
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
    index = 321,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39477, 'd12': 1.35345, 'd13': 2.73862},
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
    index = 322,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44654, 'd12': 1.31698, 'd13': 2.73633},
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
    index = 323,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  *1 C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7     H u0 p0 c0 {1,S}
8  *2 H u0 p0 c0 {2,S}
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
""",
    reactant2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0 {1,S} {6,S} {18,D}
6  *3 C u1 p0 c0 {4,S} {5,S} {17,S}
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
17    H u0 p0 c0 {6,S}
18    O u0 p2 c0 {5,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.44365, 'd12': 1.24477, 'd13': 2.68253},
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
    index = 324,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47071, 'd12': 1.25004, 'd13': 2.7138},
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
    index = 325,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36693, 'd12': 1.33069, 'd13': 2.69409},
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
    index = 326,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.04556, 'd12': 1.24931, 'd13': 2.28907},
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
    index = 327,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50989, 'd12': 1.1469, 'd13': 2.63461},
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
    index = 328,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44047, 'd12': 1.14943, 'd13': 2.58595},
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
    index = 329,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25759, 'd12': 1.27808, 'd13': 2.5216},
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
    index = 330,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39822, 'd12': 1.30388, 'd13': 2.69887},
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
    index = 331,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48659, 'd12': 1.23827, 'd13': 2.7203},
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
    index = 332,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50256, 'd12': 1.22245, 'd13': 2.71956},
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
    index = 333,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50503, 'd12': 1.22274, 'd13': 2.71493},
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
    index = 334,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47479, 'd12': 1.24181, 'd13': 2.71435},
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
    index = 335,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4227, 'd12': 1.28031, 'd13': 2.70008},
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
    index = 336,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40173, 'd12': 1.31124, 'd13': 2.68493},
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
    index = 337,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37804, 'd12': 1.36021, 'd13': 2.71526},
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
    index = 338,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39284, 'd12': 1.30218, 'd13': 2.68806},
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
    index = 339,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44471, 'd12': 1.26907, 'd13': 2.70983},
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
    index = 340,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.51223, 'd12': 1.1971, 'd13': 2.69609},
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
    index = 341,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.87803, 'd12': 1.12015, 'd13': 2.90963},
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
    index = 342,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50981, 'd12': 1.23495, 'd13': 2.73802},
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
    index = 343,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41701, 'd12': 1.31543, 'd13': 2.72946},
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
    index = 344,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.08669, 'd12': 1.22696, 'd13': 2.31365},
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
    index = 345,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    product1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35558, 'd12': 1.20524, 'd13': 2.56073},
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
    index = 346,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26548, 'd12': 1.29463, 'd13': 2.53967},
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
    index = 347,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.42982, 'd12': 1.28483, 'd13': 2.70766},
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
    index = 348,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49281, 'd12': 1.24783, 'd13': 2.73394},
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
    index = 349,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.47588, 'd12': 1.25929, 'd13': 2.72785},
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
    index = 350,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.45355, 'd12': 1.28719, 'd13': 2.71445},
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
    index = 351,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49597, 'd12': 1.24675, 'd13': 2.73547},
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
    index = 352,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35029, 'd12': 1.21167, 'd13': 2.55664},
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
    index = 353,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.41773, 'd12': 1.33141, 'd13': 2.73482},
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
    index = 354,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44527, 'd12': 1.27473, 'd13': 2.71553},
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
    index = 355,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.49166, 'd12': 1.2491, 'd13': 2.73256},
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
    index = 356,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48687, 'd12': 1.22726, 'd13': 2.69238},
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
    index = 357,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,D} {4,S}
2    H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44528, 'd12': 1.31716, 'd13': 2.70575},
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
    index = 358,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39346, 'd12': 1.32679, 'd13': 2.71818},
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
    index = 359,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27339, 'd12': 1.39771, 'd13': 2.67085},
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
    index = 360,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *1 C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11 *2 H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.50984, 'd12': 1.2163, 'd13': 2.71499},
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
    index = 361,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.850002, 'd12': 1.46973, 'd13': 2.31972},
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
    index = 362,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26358, 'd12': 1.22001, 'd13': 2.46578},
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
    index = 363,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.71724, 'd12': 1.02215, 'd13': 2.71885},
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
    index = 364,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *1 C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11 *2 H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43772, 'd12': 1.08854, 'd13': 2.51563},
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
    index = 365,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *1 C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11 *2 H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.45942, 'd12': 1.22673, 'd13': 2.6851},
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
    index = 366,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2893, 'd12': 1.36199, 'd13': 2.64125},
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
    index = 367,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.292, 'd12': 1.35669, 'd13': 2.63872},
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
    index = 368,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26716, 'd12': 1.39863, 'd13': 2.65954},
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
    index = 369,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *1 C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11 *2 H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.43377, 'd12': 1.25243, 'd13': 2.683},
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
    index = 370,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29429, 'd12': 0.964372, 'd13': 2.25818},
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
    index = 371,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 3
1    C u0 p0 c0 {2,S} {3,T}
2 *3 C u2 p0 c0 {1,S} {4,S}
3    C u0 p0 c0 {1,T} {5,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.16089, 'd12': 1.39444, 'd13': 2.53998},
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
    index = 372,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.16829, 'd12': 1.38856, 'd13': 2.52734},
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
    index = 373,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.11714, 'd12': 1.4872, 'd13': 2.58514},
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
    index = 374,
    reactant1 = """
1  *1 C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.02548, 'd12': 1.70887, 'd13': 2.71755},
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
    index = 375,
    reactant1 = """
1  *1 C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.863963, 'd12': 1.43871, 'd13': 2.30267},
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
    index = 376,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {8,S}
2     C u0 p0 c0 {1,B} {4,B} {7,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,B} {6,B} {7,S}
2     C u0 p0 c0 {1,B} {3,B} {8,S}
3     C u0 p0 c0 {2,B} {4,B} {9,S}
4     C u0 p0 c0 {3,B} {5,B} {10,S}
5     C u0 p0 c0 {4,B} {6,B} {11,S}
6     C u0 p0 c0 {1,B} {5,B} {12,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.20143, 'd12': 1.29764, 'd13': 2.48234},
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
    index = 377,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.10118, 'd12': 1.41939, 'd13': 2.51218},
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
    index = 378,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24081, 'd12': 1.46367, 'd13': 2.69952},
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
    index = 379,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23949, 'd12': 1.43987, 'd13': 2.6721},
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
    index = 380,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 3
1    C u0 p0 c0 {2,S} {3,T}
2 *3 C u2 p0 c0 {1,S} {4,S}
3    C u0 p0 c0 {1,T} {5,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23879, 'd12': 1.43316, 'd13': 2.66223},
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

entry(
    index = 381,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23782, 'd12': 1.29485, 'd13': 2.51432},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 382,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22823, 'd12': 1.49307, 'd13': 2.71466},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 383,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.17506, 'd12': 1.40599, 'd13': 2.57332},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 384,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.14303, 'd12': 1.44974, 'd13': 2.5876},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 385,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.24169, 'd12': 1.04792, 'd13': 2.28501},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 386,
    reactant1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26321, 'd12': 1.2818, 'd13': 2.51752},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 387,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28937, 'd12': 1.42929, 'd13': 2.71084},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 388,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27631, 'd12': 1.42317, 'd13': 2.6899},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 389,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28653, 'd12': 1.39168, 'd13': 2.67292},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 390,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31802, 'd12': 1.39143, 'd13': 2.68772},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 391,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.21509, 'd12': 1.11664, 'd13': 2.33131},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 392,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.14278, 'd12': 1.5609, 'd13': 2.6537},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 393,
    reactant1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25253, 'd12': 1.30413, 'd13': 2.53945},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 394,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27154, 'd12': 1.45419, 'd13': 2.71853},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 395,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26587, 'd12': 1.45239, 'd13': 2.71157},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 396,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.875435, 'd12': 1.41583, 'd13': 2.28904},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 397,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19826, 'd12': 1.30794, 'd13': 2.48347},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 398,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.03948, 'd12': 1.64481, 'd13': 2.65148},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 399,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.1138, 'd12': 1.40308, 'd13': 2.50659},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 400,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31116, 'd12': 1.33973, 'd13': 2.64253},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 401,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22123, 'd12': 1.51519, 'd13': 2.7132},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 402,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.21775, 'd12': 1.50467, 'd13': 2.71729},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 403,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2049, 'd12': 1.56363, 'd13': 2.75678},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 404,
    reactant1 = """
1    C u0 p0 c0 {3,D} {4,S} {5,S}
2 *1 C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30549, 'd12': 1.38273, 'd13': 2.68461},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 405,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25087, 'd12': 1.42468, 'd13': 2.66446},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 406,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31908, 'd12': 1.38408, 'd13': 2.70098},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 407,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {8,S}
2     C u0 p0 c0 {1,B} {4,B} {7,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,B} {6,B} {7,S}
2     C u0 p0 c0 {1,B} {3,B} {8,S}
3     C u0 p0 c0 {2,B} {4,B} {9,S}
4     C u0 p0 c0 {3,B} {5,B} {10,S}
5     C u0 p0 c0 {4,B} {6,B} {11,S}
6     C u0 p0 c0 {1,B} {5,B} {12,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.13377, 'd12': 1.64103, 'd13': 2.77186},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 408,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.12895, 'd12': 1.81579, 'd13': 2.80635},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 409,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.11842, 'd12': 1.92436, 'd13': 2.92561},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 410,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.1357, 'd12': 1.63784, 'd13': 2.74708},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 411,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.03032, 'd12': 1.69229, 'd13': 2.70779},
        method = "m062x/6-311+G(2df,2p)",
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
    index = 412,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.11246, 'd12': 1.40439, 'd13': 2.50817},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 43""",
    longDesc = 
u"""
""",
)

entry(
    index = 413,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31533, 'd12': 1.3329, 'd13': 2.64119},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 44""",
    longDesc = 
u"""
""",
)

entry(
    index = 414,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.21725, 'd12': 1.52719, 'd13': 2.73396},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 45""",
    longDesc = 
u"""
""",
)

entry(
    index = 415,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.21065, 'd12': 1.55054, 'd13': 2.75365},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 46""",
    longDesc = 
u"""
""",
)

entry(
    index = 416,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25311, 'd12': 1.42807, 'd13': 2.68089},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 47""",
    longDesc = 
u"""
""",
)

entry(
    index = 417,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.13352, 'd12': 1.6608, 'd13': 2.782},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 48""",
    longDesc = 
u"""
""",
)

entry(
    index = 418,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.04109, 'd12': 1.64509, 'd13': 2.67214},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 49""",
    longDesc = 
u"""
""",
)

entry(
    index = 419,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.14267, 'd12': 1.36766, 'd13': 2.50461},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 50""",
    longDesc = 
u"""
""",
)

entry(
    index = 420,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
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
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28554, 'd12': 1.37662, 'd13': 2.65879},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 51""",
    longDesc = 
u"""
""",
)

entry(
    index = 421,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.23787, 'd12': 1.47766, 'd13': 2.70705},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 52""",
    longDesc = 
u"""
""",
)

entry(
    index = 422,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.22146, 'd12': 1.52564, 'd13': 2.72915},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 53""",
    longDesc = 
u"""
""",
)

entry(
    index = 423,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.27301, 'd12': 1.39444, 'd13': 2.66332},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 54""",
    longDesc = 
u"""
""",
)

entry(
    index = 424,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
1 *3 H u1 p0 c0
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39367, 'd12': 0.89387, 'd13': 2.28754},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 55""",
    longDesc = 
u"""
""",
)

entry(
    index = 425,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
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
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.18721, 'd12': 1.34972, 'd13': 2.53015},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 56""",
    longDesc = 
u"""
""",
)

entry(
    index = 426,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.06293, 'd12': 1.57678, 'd13': 2.63067},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 57""",
    longDesc = 
u"""
""",
)

entry(
    index = 427,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *1 C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12 *2 H u0 p0 c0 {6,S}
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
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2924, 'd12': 1.37511, 'd13': 2.66748},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 58""",
    longDesc = 
u"""
""",
)

entry(
    index = 428,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22886, 'd12': 1.51722, 'd13': 2.74275},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 59""",
    longDesc = 
u"""
""",
)

entry(
    index = 429,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.17376, 'd12': 1.33927, 'd13': 2.50779},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 60""",
    longDesc = 
u"""
""",
)

entry(
    index = 430,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24581, 'd12': 1.49143, 'd13': 2.7249},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 61""",
    longDesc = 
u"""
""",
)

entry(
    index = 431,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30866, 'd12': 1.36677, 'd13': 2.66791},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 62""",
    longDesc = 
u"""
""",
)

entry(
    index = 432,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.20167, 'd12': 1.31076, 'd13': 2.50733},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 63""",
    longDesc = 
u"""
""",
)

entry(
    index = 433,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {10,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27756, 'd12': 1.43905, 'd13': 2.70403},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 64""",
    longDesc = 
u"""
""",
)

entry(
    index = 434,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28593, 'd12': 1.41101, 'd13': 2.6921},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 65""",
    longDesc = 
u"""
""",
)

entry(
    index = 435,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33117, 'd12': 1.33751, 'd13': 2.66142},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 66""",
    longDesc = 
u"""
""",
)

entry(
    index = 436,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.12062, 'd12': 1.83964, 'd13': 2.84485},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 67""",
    longDesc = 
u"""
""",
)

entry(
    index = 437,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.238, 'd12': 1.48294, 'd13': 2.72057},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 68""",
    longDesc = 
u"""
""",
)

entry(
    index = 438,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
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
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25432, 'd12': 1.4568, 'd13': 2.70702},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 69""",
    longDesc = 
u"""
""",
)

entry(
    index = 439,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32017, 'd12': 1.33047, 'd13': 2.63625},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 70""",
    longDesc = 
u"""
""",
)

entry(
    index = 440,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3004, 'd12': 1.36116, 'd13': 2.65083},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 71""",
    longDesc = 
u"""
""",
)

entry(
    index = 441,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23665, 'd12': 1.47886, 'd13': 2.70715},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 72""",
    longDesc = 
u"""
""",
)

entry(
    index = 442,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29405, 'd12': 1.36623, 'd13': 2.64922},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 73""",
    longDesc = 
u"""
""",
)

entry(
    index = 443,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27435, 'd12': 1.40726, 'd13': 2.67949},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 74""",
    longDesc = 
u"""
""",
)

entry(
    index = 444,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
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
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30736, 'd12': 1.37471, 'd13': 2.6748},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 75""",
    longDesc = 
u"""
""",
)

entry(
    index = 445,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2989, 'd12': 1.40177, 'd13': 2.69039},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 76""",
    longDesc = 
u"""
""",
)

entry(
    index = 446,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27912, 'd12': 1.40281, 'd13': 2.68031},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 77""",
    longDesc = 
u"""
""",
)

entry(
    index = 447,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25852, 'd12': 1.4322, 'd13': 2.68364},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 78""",
    longDesc = 
u"""
""",
)

entry(
    index = 448,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.08374, 'd12': 1.51572, 'd13': 2.58042},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 79""",
    longDesc = 
u"""
""",
)

entry(
    index = 449,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    C u0 p0 c0 {1,D} {4,D}
3    H u0 p0 c0 {1,S}
4    O u0 p2 c0 {2,D}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.20894, 'd12': 1.28541, 'd13': 2.37828},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 80""",
    longDesc = 
u"""
""",
)

entry(
    index = 450,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.13828, 'd12': 1.36667, 'd13': 2.43193},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 81""",
    longDesc = 
u"""
""",
)

entry(
    index = 451,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.21615, 'd12': 1.46309, 'd13': 2.67111},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 82""",
    longDesc = 
u"""
""",
)

entry(
    index = 452,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.20339, 'd12': 1.5019, 'd13': 2.68918},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 83""",
    longDesc = 
u"""
""",
)

entry(
    index = 453,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19207, 'd12': 1.56813, 'd13': 2.72322},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 84""",
    longDesc = 
u"""
""",
)

entry(
    index = 454,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19879, 'd12': 1.54305, 'd13': 2.70826},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 85""",
    longDesc = 
u"""
""",
)

entry(
    index = 455,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
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
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30622, 'd12': 1.32292, 'd13': 2.62821},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 86""",
    longDesc = 
u"""
""",
)

entry(
    index = 456,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26828, 'd12': 1.37254, 'd13': 2.63862},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 87""",
    longDesc = 
u"""
""",
)

entry(
    index = 457,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23012, 'd12': 1.4223, 'd13': 2.64379},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 88""",
    longDesc = 
u"""
""",
)

entry(
    index = 458,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 *2 H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.13702, 'd12': 1.46132, 'd13': 2.52224},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 89""",
    longDesc = 
u"""
""",
)

entry(
    index = 459,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0 {1,S} {2,S} {22,D}
8  *2 H u0 p0 c0 {1,S}
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
19    H u0 p0 c0 {6,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    O u0 p2 c0 {7,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
3     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
4     C u0 p0 c0 {6,S} {15,S} {16,S} {17,S}
5     C u0 p0 c0 {6,S} {18,S} {19,S} {20,S}
6  *3 C u1 p0 c0 {4,S} {5,S} {7,S}
7     C u0 p0 c0 {1,S} {6,S} {21,D}
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
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {5,S}
20    H u0 p0 c0 {5,S}
21    O u0 p2 c0 {7,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.38352, 'd12': 1.34343, 'd13': 2.70046},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 90""",
    longDesc = 
u"""
""",
)

entry(
    index = 460,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3  *1 C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0 {1,S} {2,S} {22,D}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12 *2 H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {6,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    O u0 p2 c0 {7,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7  *3 C u1 p0 c0 {2,S} {20,S} {21,S}
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
        distances = {'d23': 1.28896, 'd12': 1.44639, 'd13': 2.71347},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 91""",
    longDesc = 
u"""
""",
)

entry(
    index = 461,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27438, 'd12': 1.26913, 'd13': 2.50503},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 92""",
    longDesc = 
u"""
""",
)

entry(
    index = 462,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31001, 'd12': 1.39946, 'd13': 2.69203},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 93""",
    longDesc = 
u"""
""",
)

entry(
    index = 463,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23244, 'd12': 1.51853, 'd13': 2.7239},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 94""",
    longDesc = 
u"""
""",
)

entry(
    index = 464,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35064, 'd12': 1.3732, 'd13': 2.69115},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 95""",
    longDesc = 
u"""
""",
)

entry(
    index = 465,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31218, 'd12': 1.43643, 'd13': 2.70729},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 96""",
    longDesc = 
u"""
""",
)

entry(
    index = 466,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32975, 'd12': 1.41139, 'd13': 2.71528},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 97""",
    longDesc = 
u"""
""",
)

entry(
    index = 467,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.26216, 'd12': 1.47526, 'd13': 2.72997},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 98""",
    longDesc = 
u"""
""",
)

entry(
    index = 468,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2668, 'd12': 1.47729, 'd13': 2.74286},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 99""",
    longDesc = 
u"""
""",
)

entry(
    index = 469,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31562, 'd12': 1.41644, 'd13': 2.69363},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 100""",
    longDesc = 
u"""
""",
)

entry(
    index = 470,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.12284, 'd12': 1.48263, 'd13': 2.54708},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 101""",
    longDesc = 
u"""
""",
)

entry(
    index = 471,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.15063, 'd12': 1.50472, 'd13': 2.57058},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 102""",
    longDesc = 
u"""
""",
)

entry(
    index = 472,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25056, 'd12': 1.45716, 'd13': 2.68233},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 103""",
    longDesc = 
u"""
""",
)

entry(
    index = 473,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32359, 'd12': 1.39238, 'd13': 2.67219},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 104""",
    longDesc = 
u"""
""",
)

entry(
    index = 474,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31014, 'd12': 1.40064, 'd13': 2.68538},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 105""",
    longDesc = 
u"""
""",
)

entry(
    index = 475,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27727, 'd12': 1.46371, 'd13': 2.70354},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 106""",
    longDesc = 
u"""
""",
)

entry(
    index = 476,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3068, 'd12': 1.43159, 'd13': 2.69787},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 107""",
    longDesc = 
u"""
""",
)

entry(
    index = 477,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26318, 'd12': 1.44012, 'd13': 2.67317},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 108""",
    longDesc = 
u"""
""",
)

entry(
    index = 478,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.28156, 'd12': 1.41572, 'd13': 2.67526},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 109""",
    longDesc = 
u"""
""",
)

entry(
    index = 479,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28625, 'd12': 1.41933, 'd13': 2.70078},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 110""",
    longDesc = 
u"""
""",
)

entry(
    index = 480,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3141, 'd12': 1.39091, 'd13': 2.68879},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 111""",
    longDesc = 
u"""
""",
)

entry(
    index = 481,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34136, 'd12': 1.36275, 'd13': 2.67914},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 112""",
    longDesc = 
u"""
""",
)

entry(
    index = 482,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0 {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0 {2,S} {10,S} {11,S} {12,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7  *3 C u1 p0 c0 {2,S} {20,S} {21,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {5,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {3,S}
15    H u0 p0 c0 {3,S}
16    H u0 p0 c0 {4,S}
17    H u0 p0 c0 {4,S}
18    H u0 p0 c0 {4,S}
19    O u0 p2 c0 {6,D}
20    H u0 p0 c0 {7,S}
21    H u0 p0 c0 {7,S}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {9,S}
3  *1 C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {2,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0 {1,S} {2,S} {22,D}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10 *2 H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {6,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    O u0 p2 c0 {7,D}
""",
    product2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.304, 'd12': 1.36244, 'd13': 2.65247},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 113""",
    longDesc = 
u"""
""",
)

entry(
    index = 483,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.893488, 'd12': 1.37462, 'd13': 2.2681},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 114""",
    longDesc = 
u"""
""",
)

entry(
    index = 484,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.04106, 'd12': 1.62095, 'd13': 2.65255},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 115""",
    longDesc = 
u"""
""",
)

entry(
    index = 485,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.21541, 'd12': 1.51602, 'd13': 2.72728},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 116""",
    longDesc = 
u"""
""",
)

entry(
    index = 486,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26532, 'd12': 1.41049, 'd13': 2.6758},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 117""",
    longDesc = 
u"""
""",
)

entry(
    index = 487,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 3
1    C u0 p0 c0 {2,T} {3,S}
2    C u0 p0 c0 {1,T} {4,S}
3 *3 C u2 p0 c0 {1,S} {5,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.12253, 'd12': 1.71577, 'd13': 2.83796},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 118""",
    longDesc = 
u"""
""",
)

entry(
    index = 488,
    reactant1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.31451, 'd12': 1.18564, 'd13': 2.5001},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 119""",
    longDesc = 
u"""
""",
)

entry(
    index = 489,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.13544, 'd12': 1.46401, 'd13': 2.54805},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 120""",
    longDesc = 
u"""
""",
)

entry(
    index = 490,
    reactant1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.28296, 'd12': 1.23278, 'd13': 2.4907},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 121""",
    longDesc = 
u"""
""",
)

entry(
    index = 491,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.17282, 'd12': 1.39273, 'd13': 2.56055},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 122""",
    longDesc = 
u"""
""",
)

entry(
    index = 492,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.05464, 'd12': 1.30097, 'd13': 2.25495},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 123""",
    longDesc = 
u"""
""",
)

entry(
    index = 493,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.18908, 'd12': 1.32482, 'd13': 2.50813},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 124""",
    longDesc = 
u"""
""",
)

entry(
    index = 494,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.0907, 'd12': 1.26753, 'd13': 2.34208},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 125""",
    longDesc = 
u"""
""",
)

entry(
    index = 495,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37417, 'd12': 1.33628, 'd13': 2.67587},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 126""",
    longDesc = 
u"""
""",
)

entry(
    index = 496,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28916, 'd12': 1.38, 'd13': 2.66232},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 127""",
    longDesc = 
u"""
""",
)

entry(
    index = 497,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.37262, 'd12': 1.32124, 'd13': 2.64429},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 128""",
    longDesc = 
u"""
""",
)

entry(
    index = 498,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23639, 'd12': 1.47985, 'd13': 2.68474},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 129""",
    longDesc = 
u"""
""",
)

entry(
    index = 499,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28225, 'd12': 1.42761, 'd13': 2.70662},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 130""",
    longDesc = 
u"""
""",
)

entry(
    index = 500,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33156, 'd12': 1.37945, 'd13': 2.68289},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 131""",
    longDesc = 
u"""
""",
)

entry(
    index = 501,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.20738, 'd12': 1.34423, 'd13': 2.54626},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 132""",
    longDesc = 
u"""
""",
)

entry(
    index = 502,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32327, 'd12': 1.39458, 'd13': 2.69545},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 133""",
    longDesc = 
u"""
""",
)

entry(
    index = 503,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23984, 'd12': 1.50198, 'd13': 2.73677},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 134""",
    longDesc = 
u"""
""",
)

entry(
    index = 504,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28502, 'd12': 1.44872, 'd13': 2.69905},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 135""",
    longDesc = 
u"""
""",
)

entry(
    index = 505,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25307, 'd12': 1.47083, 'd13': 2.71417},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 136""",
    longDesc = 
u"""
""",
)

entry(
    index = 506,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {5,S} {9,S}
4     C u0 p0 c0 {2,S} {5,D} {10,S}
5     C u0 p0 c0 {3,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9  *2 H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30437, 'd12': 1.42257, 'd13': 2.69066},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 137""",
    longDesc = 
u"""
""",
)

entry(
    index = 507,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24444, 'd12': 1.46842, 'd13': 2.69949},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 138""",
    longDesc = 
u"""
""",
)

entry(
    index = 508,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28245, 'd12': 1.38892, 'd13': 2.66834},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 139""",
    longDesc = 
u"""
""",
)

entry(
    index = 509,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19204, 'd12': 1.2896, 'd13': 2.477},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 140""",
    longDesc = 
u"""
""",
)

entry(
    index = 510,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.26947, 'd12': 1.43501, 'd13': 2.68027},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 141""",
    longDesc = 
u"""
""",
)

entry(
    index = 511,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.23172, 'd12': 1.26004, 'd13': 2.48996},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 142""",
    longDesc = 
u"""
""",
)

entry(
    index = 512,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33091, 'd12': 1.35476, 'd13': 2.68227},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 143""",
    longDesc = 
u"""
""",
)

entry(
    index = 513,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30452, 'd12': 1.40708, 'd13': 2.69633},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 144""",
    longDesc = 
u"""
""",
)

entry(
    index = 514,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3046, 'd12': 1.38322, 'd13': 2.68341},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 145""",
    longDesc = 
u"""
""",
)

entry(
    index = 515,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.21874, 'd12': 1.31493, 'd13': 2.53143},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 146""",
    longDesc = 
u"""
""",
)

entry(
    index = 516,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22278, 'd12': 1.25118, 'd13': 2.46055},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 147""",
    longDesc = 
u"""
""",
)

entry(
    index = 517,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 3
1    C u0 p0 c0 {2,T} {3,S}
2    C u0 p0 c0 {1,T} {4,S}
3 *3 C u2 p0 c0 {1,S} {5,S}
4    H u0 p0 c0 {2,S}
5    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31744, 'd12': 1.35141, 'd13': 2.65773},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 148""",
    longDesc = 
u"""
""",
)

entry(
    index = 518,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.12539, 'd12': 1.87771, 'd13': 2.78624},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 149""",
    longDesc = 
u"""
""",
)

entry(
    index = 519,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19919, 'd12': 1.50082, 'd13': 2.66425},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 150""",
    longDesc = 
u"""
""",
)

entry(
    index = 520,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36, 'd12': 1.38457, 'd13': 2.63632},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 151""",
    longDesc = 
u"""
""",
)

entry(
    index = 521,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34617, 'd12': 1.37526, 'd13': 2.66976},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 152""",
    longDesc = 
u"""
""",
)

entry(
    index = 522,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28767, 'd12': 1.41971, 'd13': 2.70294},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 153""",
    longDesc = 
u"""
""",
)

entry(
    index = 523,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.1862, 'd12': 1.38278, 'd13': 2.54826},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 154""",
    longDesc = 
u"""
""",
)

entry(
    index = 524,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.1331, 'd12': 1.69997, 'd13': 2.81507},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 155""",
    longDesc = 
u"""
""",
)

entry(
    index = 525,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26716, 'd12': 1.36612, 'd13': 2.63108},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 156""",
    longDesc = 
u"""
""",
)

entry(
    index = 526,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28021, 'd12': 1.46034, 'd13': 2.72254},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 157""",
    longDesc = 
u"""
""",
)

entry(
    index = 527,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30263, 'd12': 1.39917, 'd13': 2.69753},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 158""",
    longDesc = 
u"""
""",
)

entry(
    index = 528,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19687, 'd12': 1.27793, 'd13': 2.41073},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 159""",
    longDesc = 
u"""
""",
)

entry(
    index = 529,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19469, 'd12': 1.38043, 'd13': 2.54285},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 160""",
    longDesc = 
u"""
""",
)

entry(
    index = 530,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.2835, 'd12': 0.988982, 'd13': 2.2699},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 161""",
    longDesc = 
u"""
""",
)

entry(
    index = 531,
    reactant1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.26594, 'd12': 1.24337, 'd13': 2.509},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 162""",
    longDesc = 
u"""
""",
)

entry(
    index = 532,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33898, 'd12': 1.3371, 'd13': 2.67345},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 163""",
    longDesc = 
u"""
""",
)

entry(
    index = 533,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29899, 'd12': 1.41884, 'd13': 2.71053},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 164""",
    longDesc = 
u"""
""",
)

entry(
    index = 534,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31509, 'd12': 1.38198, 'd13': 2.69476},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 165""",
    longDesc = 
u"""
""",
)

entry(
    index = 535,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38142, 'd12': 1.35777, 'd13': 2.73419},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 166""",
    longDesc = 
u"""
""",
)

entry(
    index = 536,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23815, 'd12': 1.51077, 'd13': 2.71907},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 167""",
    longDesc = 
u"""
""",
)

entry(
    index = 537,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.26406, 'd12': 1.48187, 'd13': 2.72247},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 168""",
    longDesc = 
u"""
""",
)

entry(
    index = 538,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31358, 'd12': 1.37596, 'd13': 2.67539},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 169""",
    longDesc = 
u"""
""",
)

entry(
    index = 539,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34478, 'd12': 1.36561, 'd13': 2.67719},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 170""",
    longDesc = 
u"""
""",
)

entry(
    index = 540,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36326, 'd12': 1.39001, 'd13': 2.64477},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 171""",
    longDesc = 
u"""
""",
)

entry(
    index = 541,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28374, 'd12': 1.41906, 'd13': 2.68723},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 172""",
    longDesc = 
u"""
""",
)

entry(
    index = 542,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27669, 'd12': 1.47522, 'd13': 2.73719},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 173""",
    longDesc = 
u"""
""",
)

entry(
    index = 543,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23891, 'd12': 1.28001, 'd13': 2.503},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 174""",
    longDesc = 
u"""
""",
)

entry(
    index = 544,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.18584, 'd12': 1.41532, 'd13': 2.57286},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 175""",
    longDesc = 
u"""
""",
)

entry(
    index = 545,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.17982, 'd12': 1.62371, 'd13': 2.78509},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 176""",
    longDesc = 
u"""
""",
)

entry(
    index = 546,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3191, 'd12': 1.42279, 'd13': 2.72768},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 177""",
    longDesc = 
u"""
""",
)

entry(
    index = 547,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,D}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    O u0 p2 c0 {1,D}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.13807, 'd12': 1.69131, 'd13': 2.82491},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 178""",
    longDesc = 
u"""
""",
)

entry(
    index = 548,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32077, 'd12': 1.41002, 'd13': 2.72822},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 179""",
    longDesc = 
u"""
""",
)

entry(
    index = 549,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36017, 'd12': 1.36251, 'd13': 2.63431},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 180""",
    longDesc = 
u"""
""",
)

entry(
    index = 550,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3556, 'd12': 0.923854, 'd13': 2.27781},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 181""",
    longDesc = 
u"""
""",
)

entry(
    index = 551,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.16128, 'd12': 1.42871, 'd13': 2.58129},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 182""",
    longDesc = 
u"""
""",
)

entry(
    index = 552,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.18051, 'd12': 1.33003, 'd13': 2.502},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 183""",
    longDesc = 
u"""
""",
)

entry(
    index = 553,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24657, 'd12': 1.48928, 'd13': 2.72313},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 184""",
    longDesc = 
u"""
""",
)

entry(
    index = 554,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30523, 'd12': 1.36484, 'd13': 2.66293},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 185""",
    longDesc = 
u"""
""",
)

entry(
    index = 555,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.12448, 'd12': 1.77031, 'd13': 2.84901},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 186""",
    longDesc = 
u"""
""",
)

entry(
    index = 556,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27848, 'd12': 1.40632, 'd13': 2.67973},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 187""",
    longDesc = 
u"""
""",
)

entry(
    index = 557,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2791, 'd12': 1.40141, 'd13': 2.67322},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 188""",
    longDesc = 
u"""
""",
)

entry(
    index = 558,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2938, 'd12': 1.44276, 'd13': 2.71507},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 189""",
    longDesc = 
u"""
""",
)

entry(
    index = 559,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31607, 'd12': 1.38918, 'd13': 2.68893},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 190""",
    longDesc = 
u"""
""",
)

entry(
    index = 560,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32896, 'd12': 1.35819, 'd13': 2.67947},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 191""",
    longDesc = 
u"""
""",
)

entry(
    index = 561,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30228, 'd12': 1.40589, 'd13': 2.68903},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 192""",
    longDesc = 
u"""
""",
)

entry(
    index = 562,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29072, 'd12': 1.4566, 'd13': 2.74355},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 193""",
    longDesc = 
u"""
""",
)

entry(
    index = 563,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34625, 'd12': 1.34484, 'd13': 2.6847},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 194""",
    longDesc = 
u"""
""",
)

entry(
    index = 564,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31863, 'd12': 1.37018, 'd13': 2.68547},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 195""",
    longDesc = 
u"""
""",
)

entry(
    index = 565,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 3
1    C u0 p0 c0 {2,D} {3,D}
2 *3 C u2 p0 c0 {1,D}
3    O u0 p2 c0 {1,D}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23814, 'd12': 1.42541, 'd13': 2.5461},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 196""",
    longDesc = 
u"""
""",
)

entry(
    index = 566,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 3
1    C u0 p0 c0 {2,D} {3,D}
2 *3 C u2 p0 c0 {1,D}
3    O u0 p2 c0 {1,D}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22447, 'd12': 1.45282, 'd13': 2.65518},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 197""",
    longDesc = 
u"""
""",
)

entry(
    index = 567,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 3
1    C u0 p0 c0 {2,D} {3,D}
2 *3 C u2 p0 c0 {1,D}
3    O u0 p2 c0 {1,D}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22851, 'd12': 1.45534, 'd13': 2.66445},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 198""",
    longDesc = 
u"""
""",
)

entry(
    index = 568,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 3
1    C u0 p0 c0 {2,D} {3,D}
2 *3 C u2 p0 c0 {1,D}
3    O u0 p2 c0 {1,D}
""",
    product1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25782, 'd12': 1.41193, 'd13': 2.66063},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 199""",
    longDesc = 
u"""
""",
)

entry(
    index = 569,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.12964, 'd12': 1.80501, 'd13': 2.73886},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 200""",
    longDesc = 
u"""
""",
)

entry(
    index = 570,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34446, 'd12': 1.40076, 'd13': 2.64444},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 201""",
    longDesc = 
u"""
""",
)

entry(
    index = 571,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29557, 'd12': 1.36887, 'd13': 2.65918},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 202""",
    longDesc = 
u"""
""",
)

entry(
    index = 572,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32882, 'd12': 1.38361, 'd13': 2.69912},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 203""",
    longDesc = 
u"""
""",
)

entry(
    index = 573,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2296, 'd12': 1.49058, 'd13': 2.71452},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 204""",
    longDesc = 
u"""
""",
)

entry(
    index = 574,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34518, 'd12': 1.36733, 'd13': 2.70794},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 205""",
    longDesc = 
u"""
""",
)

entry(
    index = 575,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24093, 'd12': 1.47374, 'd13': 2.70515},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 206""",
    longDesc = 
u"""
""",
)

entry(
    index = 576,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26608, 'd12': 1.44373, 'd13': 2.70924},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 207""",
    longDesc = 
u"""
""",
)

entry(
    index = 577,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35377, 'd12': 1.3583, 'd13': 2.67764},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 208""",
    longDesc = 
u"""
""",
)

entry(
    index = 578,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.20098, 'd12': 1.36702, 'd13': 2.55933},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 209""",
    longDesc = 
u"""
""",
)

entry(
    index = 579,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34864, 'd12': 1.39821, 'd13': 2.74343},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 210""",
    longDesc = 
u"""
""",
)

entry(
    index = 580,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.11369, 'd12': 1.92365, 'd13': 3.02434},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 211""",
    longDesc = 
u"""
""",
)

entry(
    index = 581,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,D}
2    H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3605, 'd12': 1.38045, 'd13': 2.71051},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 212""",
    longDesc = 
u"""
""",
)

entry(
    index = 582,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.28834, 'd12': 1.26977, 'd13': 2.55114},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 213""",
    longDesc = 
u"""
""",
)

entry(
    index = 583,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.35154, 'd12': 1.38621, 'd13': 2.72595},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 214""",
    longDesc = 
u"""
""",
)

entry(
    index = 584,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {6,D}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *3 C u1 p0 c0 {2,S} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {1,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.31832, 'd12': 1.43828, 'd13': 2.73038},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 215""",
    longDesc = 
u"""
""",
)

entry(
    index = 585,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30526, 'd12': 1.40546, 'd13': 2.70487},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 216""",
    longDesc = 
u"""
""",
)

entry(
    index = 586,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
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
    product2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26354, 'd12': 1.47802, 'd13': 2.73766},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 217""",
    longDesc = 
u"""
""",
)

entry(
    index = 587,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24541, 'd12': 1.51687, 'd13': 2.75861},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 218""",
    longDesc = 
u"""
""",
)

entry(
    index = 588,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.39696, 'd12': 1.3858, 'd13': 2.78275},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 219""",
    longDesc = 
u"""
""",
)

entry(
    index = 589,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32835, 'd12': 1.41741, 'd13': 2.72713},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 220""",
    longDesc = 
u"""
""",
)

entry(
    index = 590,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28825, 'd12': 1.46084, 'd13': 2.74272},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 221""",
    longDesc = 
u"""
""",
)

entry(
    index = 591,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29948, 'd12': 1.43639, 'd13': 2.72285},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 222""",
    longDesc = 
u"""
""",
)

entry(
    index = 592,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30052, 'd12': 1.44902, 'd13': 2.74595},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 223""",
    longDesc = 
u"""
""",
)

entry(
    index = 593,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.86239, 'd12': 1.43782, 'd13': 2.2983},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 224""",
    longDesc = 
u"""
""",
)

entry(
    index = 594,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.20715, 'd12': 1.52486, 'd13': 2.72106},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 225""",
    longDesc = 
u"""
""",
)

entry(
    index = 595,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26356, 'd12': 1.42033, 'd13': 2.67127},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 226""",
    longDesc = 
u"""
""",
)

entry(
    index = 596,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24194, 'd12': 1.45416, 'd13': 2.68962},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 227""",
    longDesc = 
u"""
""",
)

entry(
    index = 597,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32577, 'd12': 0.934703, 'd13': 2.25494},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 228""",
    longDesc = 
u"""
""",
)

entry(
    index = 598,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {3,S} {5,S} {6,D}
3  *3 C u1 p0 c0 {1,S} {2,S} {9,S}
4     C u0 p0 c0 {1,S} {5,D} {10,S}
5     C u0 p0 c0 {2,S} {4,D} {11,S}
6     C u0 p0 c0 {2,D} {12,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,S} {6,D}
4     C u0 p0 c0 {2,S} {5,D} {11,S}
5     C u0 p0 c0 {3,S} {4,D} {12,S}
6     C u0 p0 c0 {3,D} {13,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25686, 'd12': 1.44101, 'd13': 2.6938},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 229""",
    longDesc = 
u"""
""",
)

entry(
    index = 599,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27452, 'd12': 1.41709, 'd13': 2.68689},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 230""",
    longDesc = 
u"""
""",
)

entry(
    index = 600,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30557, 'd12': 1.38363, 'd13': 2.66673},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 231""",
    longDesc = 
u"""
""",
)

entry(
    index = 601,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28694, 'd12': 1.40233, 'd13': 2.66635},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 232""",
    longDesc = 
u"""
""",
)

entry(
    index = 602,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27972, 'd12': 1.44337, 'd13': 2.70939},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 233""",
    longDesc = 
u"""
""",
)

entry(
    index = 603,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6     C u0 p0 c0 {1,S} {2,S} {20,D}
7  *3 C u1 p0 c0 {2,S} {21,S} {22,S}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {23,S}
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
22    H u0 p0 c0 {7,S}
23    H u0 p0 c0 {9,S}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {5,S} {6,S} {7,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {14,S} {15,S} {16,S}
5  *1 C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
6     C u0 p0 c0 {2,S} {20,S} {21,S} {22,S}
7     C u0 p0 c0 {1,S} {2,S} {23,D}
8     O u0 p2 c0 {1,S} {9,S}
9     O u0 p2 c0 {8,S} {24,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {4,S}
17 *2 H u0 p0 c0 {5,S}
18    H u0 p0 c0 {5,S}
19    H u0 p0 c0 {5,S}
20    H u0 p0 c0 {6,S}
21    H u0 p0 c0 {6,S}
22    H u0 p0 c0 {6,S}
23    O u0 p2 c0 {7,D}
24    H u0 p0 c0 {9,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.36184, 'd12': 0.916182, 'd13': 2.27416},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 234""",
    longDesc = 
u"""
""",
)

entry(
    index = 604,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {5,S} {13,D}
5     O u0 p2 c0 {4,S} {14,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    O u0 p2 c0 {4,D}
14 *3 O u1 p2 c0 {5,S}
""",
    product1 = """
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
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {5,S} {14,D}
5     O u0 p2 c0 {4,S} {6,S}
6  *1 O u0 p2 c0 {5,S} {15,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    O u0 p2 c0 {4,D}
15 *2 H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.20349, 'd12': 1.30031, 'd13': 2.49703},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 235""",
    longDesc = 
u"""
""",
)

entry(
    index = 605,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {1,S} {5,S} {14,D}
5     O u0 p2 c0 {4,S} {6,S}
6  *1 O u0 p2 c0 {5,S} {15,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {3,S}
14    O u0 p2 c0 {4,D}
15 *2 H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {5,S} {13,D}
5     O u0 p2 c0 {4,S} {14,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    O u0 p2 c0 {4,D}
14 *3 O u1 p2 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24357, 'd12': 1.31034, 'd13': 2.51754},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 236""",
    longDesc = 
u"""
""",
)

entry(
    index = 606,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.13391, 'd12': 1.47468, 'd13': 2.58993},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 237""",
    longDesc = 
u"""
""",
)

entry(
    index = 607,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.27258, 'd12': 1.02425, 'd13': 2.29683},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 238""",
    longDesc = 
u"""
""",
)

entry(
    index = 608,
    reactant1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.19795, 'd12': 1.38024, 'd13': 2.57366},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 239""",
    longDesc = 
u"""
""",
)

entry(
    index = 609,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.13826, 'd12': 1.56688, 'd13': 2.68698},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 240""",
    longDesc = 
u"""
""",
)

entry(
    index = 610,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33334, 'd12': 1.39021, 'd13': 2.71645},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 241""",
    longDesc = 
u"""
""",
)

entry(
    index = 611,
    reactant1 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31592, 'd12': 1.38866, 'd13': 2.68893},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 242""",
    longDesc = 
u"""
""",
)

entry(
    index = 612,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24309, 'd12': 1.47821, 'd13': 2.70749},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 243""",
    longDesc = 
u"""
""",
)

entry(
    index = 613,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.26427, 'd12': 1.45209, 'd13': 2.70747},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 244""",
    longDesc = 
u"""
""",
)

entry(
    index = 614,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32269, 'd12': 1.38658, 'd13': 2.70085},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 245""",
    longDesc = 
u"""
""",
)

entry(
    index = 615,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,D} {4,S}
2    H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3794, 'd12': 1.36693, 'd13': 2.71184},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 246""",
    longDesc = 
u"""
""",
)

entry(
    index = 616,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3  *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4     C u0 p0 c0 {2,D} {10,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    O u0 p2 c0 {4,D}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {3,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {2,S} {4,D}
4     C u0 p0 c0 {3,D} {11,D}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    O u0 p2 c0 {4,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22756, 'd12': 1.50228, 'd13': 2.71548},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 247""",
    longDesc = 
u"""
""",
)

entry(
    index = 617,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3     C u0 p0 c0 {2,S} {5,S} {9,D}
4     C u0 p0 c0 {2,D} {10,S} {11,S}
5     O u0 p2 c0 {3,S} {12,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     O u0 p2 c0 {3,D}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
12 *3 O u1 p2 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3     C u0 p0 c0 {2,S} {5,S} {10,D}
4     C u0 p0 c0 {2,D} {11,S} {12,S}
5     O u0 p2 c0 {3,S} {6,S}
6  *1 O u0 p2 c0 {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {1,S}
10    O u0 p2 c0 {3,D}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
13 *2 H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.17221, 'd12': 0.937577, 'd13': 2.10708},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 248""",
    longDesc = 
u"""
""",
)

entry(
    index = 618,
    reactant1 = """
1     C u0 p0 c0 {2,S} {7,S} {8,S} {9,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3     C u0 p0 c0 {2,S} {5,S} {10,D}
4     C u0 p0 c0 {2,D} {11,S} {12,S}
5     O u0 p2 c0 {3,S} {6,S}
6  *1 O u0 p2 c0 {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {1,S}
10    O u0 p2 c0 {3,D}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
13 *2 H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {4,D}
3     C u0 p0 c0 {2,S} {5,S} {9,D}
4     C u0 p0 c0 {2,D} {10,S} {11,S}
5     O u0 p2 c0 {3,S} {12,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     O u0 p2 c0 {3,D}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
12 *3 O u1 p2 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.20258, 'd12': 1.39989, 'd13': 2.57887},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 249""",
    longDesc = 
u"""
""",
)

entry(
    index = 619,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.29246, 'd12': 0.977884, 'd13': 2.26945},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 250""",
    longDesc = 
u"""
""",
)

entry(
    index = 620,
    reactant1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.26772, 'd12': 1.24182, 'd13': 2.50718},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 251""",
    longDesc = 
u"""
""",
)

entry(
    index = 621,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.17334, 'd12': 1.3975, 'd13': 2.55818},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 252""",
    longDesc = 
u"""
""",
)

entry(
    index = 622,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3314, 'd12': 1.35655, 'd13': 2.68729},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 253""",
    longDesc = 
u"""
""",
)

entry(
    index = 623,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33117, 'd12': 1.34695, 'd13': 2.67376},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 254""",
    longDesc = 
u"""
""",
)

entry(
    index = 624,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31181, 'd12': 1.39115, 'd13': 2.6992},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 255""",
    longDesc = 
u"""
""",
)

entry(
    index = 625,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25117, 'd12': 1.44434, 'd13': 2.6909},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 256""",
    longDesc = 
u"""
""",
)

entry(
    index = 626,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.304, 'd12': 1.38996, 'd13': 2.69336},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 257""",
    longDesc = 
u"""
""",
)

entry(
    index = 627,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32744, 'd12': 1.36322, 'd13': 2.67448},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 258""",
    longDesc = 
u"""
""",
)

entry(
    index = 628,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33278, 'd12': 1.37871, 'd13': 2.68099},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 259""",
    longDesc = 
u"""
""",
)

entry(
    index = 629,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30451, 'd12': 1.39121, 'd13': 2.69447},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 260""",
    longDesc = 
u"""
""",
)

entry(
    index = 630,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3104, 'd12': 1.43504, 'd13': 2.73412},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 261""",
    longDesc = 
u"""
""",
)

entry(
    index = 631,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,D}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    O u0 p2 c0 {1,D}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33375, 'd12': 1.34492, 'd13': 2.6698},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 262""",
    longDesc = 
u"""
""",
)

entry(
    index = 632,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24384, 'd12': 1.40806, 'd13': 2.6519},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 263""",
    longDesc = 
u"""
""",
)

entry(
    index = 633,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34429, 'd12': 1.35705, 'd13': 2.69505},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 264""",
    longDesc = 
u"""
""",
)

entry(
    index = 634,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.13451, 'd12': 1.7064, 'd13': 2.82673},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 265""",
    longDesc = 
u"""
""",
)

entry(
    index = 635,
    reactant1 = """
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  *1 C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.31947, 'd12': 1.39347, 'd13': 2.70389},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 266""",
    longDesc = 
u"""
""",
)

entry(
    index = 636,
    reactant1 = """
1  *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {2,S} {10,D}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    O u0 p2 c0 {3,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,D}
3 *3 C u1 p0 c0 {2,S} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3159, 'd12': 1.42272, 'd13': 2.7251},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 267""",
    longDesc = 
u"""
""",
)

entry(
    index = 637,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
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
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30083, 'd12': 1.37193, 'd13': 2.67241},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 268""",
    longDesc = 
u"""
""",
)

entry(
    index = 638,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2  *1 C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28525, 'd12': 1.41027, 'd13': 2.69021},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 269""",
    longDesc = 
u"""
""",
)

entry(
    index = 639,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33035, 'd12': 1.37277, 'd13': 2.69608},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 270""",
    longDesc = 
u"""
""",
)

entry(
    index = 640,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25278, 'd12': 1.04276, 'd13': 2.2939},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 271""",
    longDesc = 
u"""
""",
)

entry(
    index = 641,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22446, 'd12': 1.50747, 'd13': 2.72203},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 272""",
    longDesc = 
u"""
""",
)

entry(
    index = 642,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
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
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24194, 'd12': 1.48174, 'd13': 2.71985},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 273""",
    longDesc = 
u"""
""",
)

entry(
    index = 643,
    reactant1 = """
1    C u0 p0 c0 {3,D} {4,S} {5,S}
2 *1 C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29177, 'd12': 1.41098, 'd13': 2.69187},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 274""",
    longDesc = 
u"""
""",
)

entry(
    index = 644,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,D} {3,S}
3    C u0 p0 c0 {2,S} {4,T}
4    C u0 p0 c0 {3,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {4,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25846, 'd12': 1.44527, 'd13': 2.69783},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 275""",
    longDesc = 
u"""
""",
)

entry(
    index = 645,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23044, 'd12': 1.50298, 'd13': 2.73213},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 276""",
    longDesc = 
u"""
""",
)

entry(
    index = 646,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2  *1 C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23344, 'd12': 1.49618, 'd13': 2.72066},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 277""",
    longDesc = 
u"""
""",
)

entry(
    index = 647,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,D} {9,S}
3  *3 C u1 p0 c0 {1,S} {5,S} {10,S}
4     C u0 p0 c0 {2,D} {6,S} {12,S}
5     C u0 p0 c0 {3,S} {6,D} {13,S}
6     C u0 p0 c0 {4,S} {5,D} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22195, 'd12': 1.10827, 'd13': 2.31786},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 278""",
    longDesc = 
u"""
""",
)

entry(
    index = 648,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22334, 'd12': 1.49591, 'd13': 2.70803},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 279""",
    longDesc = 
u"""
""",
)

entry(
    index = 649,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.34474, 'd12': 0.925569, 'd13': 2.26775},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 280""",
    longDesc = 
u"""
""",
)

entry(
    index = 650,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.17381, 'd12': 1.37475, 'd13': 2.52182},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 281""",
    longDesc = 
u"""
""",
)

entry(
    index = 651,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.15346, 'd12': 1.48476, 'd13': 2.61123},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 282""",
    longDesc = 
u"""
""",
)

entry(
    index = 652,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.14956, 'd12': 1.55043, 'd13': 2.63671},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 283""",
    longDesc = 
u"""
""",
)

entry(
    index = 653,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.09601, 'd12': 1.51283, 'd13': 2.5987},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 284""",
    longDesc = 
u"""
""",
)

entry(
    index = 654,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {10,S}
4     C u0 p0 c0 {3,S} {5,D} {11,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.17121, 'd12': 1.40169, 'd13': 2.56276},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 285""",
    longDesc = 
u"""
""",
)

entry(
    index = 655,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {5,D} {11,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,D} {9,S}
3  *3 C u1 p0 c0 {1,S} {5,S} {10,S}
4     C u0 p0 c0 {2,D} {6,S} {11,S}
5     C u0 p0 c0 {3,S} {6,D} {12,S}
6     C u0 p0 c0 {4,S} {5,D} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19836, 'd12': 1.3926, 'd13': 2.58114},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 286""",
    longDesc = 
u"""
""",
)

entry(
    index = 656,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2  *1 C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.17101, 'd12': 1.33502, 'd13': 2.4995},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 287""",
    longDesc = 
u"""
""",
)

entry(
    index = 657,
    reactant1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2625, 'd12': 1.27831, 'd13': 2.53577},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 288""",
    longDesc = 
u"""
""",
)

entry(
    index = 658,
    reactant1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25002, 'd12': 1.31685, 'd13': 2.55894},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 289""",
    longDesc = 
u"""
""",
)

entry(
    index = 659,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24326, 'd12': 1.45773, 'd13': 2.69413},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 290""",
    longDesc = 
u"""
""",
)

entry(
    index = 660,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2  *1 C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30619, 'd12': 1.35764, 'd13': 2.65607},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 291""",
    longDesc = 
u"""
""",
)

entry(
    index = 661,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3  *1 C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3  *1 C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31915, 'd12': 1.32869, 'd13': 2.6379},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 292""",
    longDesc = 
u"""
""",
)

entry(
    index = 662,
    reactant1 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2  *1 C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6     C u0 p0 c0 {4,B} {5,B} {12,S}
7     H u0 p0 c0 {1,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {4,B} {8,S}
3     C u0 p0 c0 {1,B} {5,B} {9,S}
4     C u0 p0 c0 {2,B} {6,B} {10,S}
5     C u0 p0 c0 {3,B} {6,B} {11,S}
6  *3 C u1 p0 c0 {4,B} {5,B}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26785, 'd12': 1.39908, 'd13': 2.66171},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 293""",
    longDesc = 
u"""
""",
)

entry(
    index = 663,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28122, 'd12': 1.38457, 'd13': 2.65101},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 294""",
    longDesc = 
u"""
""",
)

entry(
    index = 664,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27479, 'd12': 1.38786, 'd13': 2.65584},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 295""",
    longDesc = 
u"""
""",
)

entry(
    index = 665,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
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
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34806, 'd12': 1.31616, 'd13': 2.66402},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 296""",
    longDesc = 
u"""
""",
)

entry(
    index = 666,
    reactant1 = """
1    C u0 p0 c0 {2,D} {3,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {4,T}
4    C u0 p0 c0 {3,T} {8,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,T}
3 *3 C u1 p0 c0 {1,D} {6,S}
4    C u0 p0 c0 {2,T} {7,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
7    H u0 p0 c0 {4,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26407, 'd12': 1.40244, 'd13': 2.6525},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 297""",
    longDesc = 
u"""
""",
)

entry(
    index = 667,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    C u0 p0 c0 {1,D} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    O u0 p2 c0 {3,D}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29046, 'd12': 1.40769, 'd13': 2.69234},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 298""",
    longDesc = 
u"""
""",
)

entry(
    index = 668,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31168, 'd12': 1.33775, 'd13': 2.63523},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 299""",
    longDesc = 
u"""
""",
)

entry(
    index = 669,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27788, 'd12': 1.41052, 'd13': 2.68277},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 300""",
    longDesc = 
u"""
""",
)

entry(
    index = 670,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26652, 'd12': 1.4522, 'd13': 2.7145},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 301""",
    longDesc = 
u"""
""",
)

entry(
    index = 671,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25108, 'd12': 1.49045, 'd13': 2.73836},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 302""",
    longDesc = 
u"""
""",
)

entry(
    index = 672,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *2 H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26709, 'd12': 1.43051, 'd13': 2.67652},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 303""",
    longDesc = 
u"""
""",
)

entry(
    index = 673,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19956, 'd12': 1.56756, 'd13': 2.73629},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 304""",
    longDesc = 
u"""
""",
)

entry(
    index = 674,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34171, 'd12': 1.39501, 'd13': 2.71439},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 305""",
    longDesc = 
u"""
""",
)

entry(
    index = 675,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {4,D} {9,S}
3  *3 C u1 p0 c0 {1,S} {5,S} {10,S}
4     C u0 p0 c0 {2,D} {6,S} {12,S}
5     C u0 p0 c0 {3,S} {6,D} {13,S}
6     C u0 p0 c0 {4,S} {5,D} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33317, 'd12': 1.40518, 'd13': 2.67611},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 306""",
    longDesc = 
u"""
""",
)

entry(
    index = 676,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27675, 'd12': 1.46478, 'd13': 2.71438},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 307""",
    longDesc = 
u"""
""",
)

entry(
    index = 677,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26293, 'd12': 1.46049, 'd13': 2.72099},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 308""",
    longDesc = 
u"""
""",
)

entry(
    index = 678,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19996, 'd12': 1.36954, 'd13': 2.55492},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 309""",
    longDesc = 
u"""
""",
)

entry(
    index = 679,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {11,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {6,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2915, 'd12': 1.44841, 'd13': 2.72027},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 310""",
    longDesc = 
u"""
""",
)

entry(
    index = 680,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3715, 'd12': 1.30771, 'd13': 2.67317},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 311""",
    longDesc = 
u"""
""",
)

entry(
    index = 681,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26262, 'd12': 1.22374, 'd13': 2.47315},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 312""",
    longDesc = 
u"""
""",
)

entry(
    index = 682,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3  *1 C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7  *2 H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19167, 'd12': 1.29281, 'd13': 2.46742},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 313""",
    longDesc = 
u"""
""",
)

entry(
    index = 683,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,D} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {5,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *3 C u1 p0 c0 {3,S} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product2 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.3031, 'd12': 1.4035, 'd13': 2.69908},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 314""",
    longDesc = 
u"""
""",
)

entry(
    index = 684,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    C u0 p0 c0 {1,S} {5,D} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30426, 'd12': 1.38149, 'd13': 2.67549},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 315""",
    longDesc = 
u"""
""",
)

entry(
    index = 685,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,D}
2 *3 C u1 p0 c0 {1,S} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    O u0 p2 c0 {1,D}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,D} {7,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24191, 'd12': 1.4648, 'd13': 2.69416},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 316""",
    longDesc = 
u"""
""",
)

entry(
    index = 686,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2516, 'd12': 1.48985, 'd13': 2.73592},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 317""",
    longDesc = 
u"""
""",
)

entry(
    index = 687,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25253, 'd12': 1.45256, 'd13': 2.67681},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 318""",
    longDesc = 
u"""
""",
)

entry(
    index = 688,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4  *1 C u0 p0 c0 {2,D} {9,S} {10,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10 *2 H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,D}
2    H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,D} {5,S}
2    C u0 p0 c0 {1,S} {4,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4 *3 C u1 p0 c0 {2,D} {9,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {4,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    O u0 p2 c0 {1,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23344, 'd12': 1.51785, 'd13': 2.73543},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 319""",
    longDesc = 
u"""
""",
)

entry(
    index = 689,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    product2 = """
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3 *1 C u0 p0 c0 {1,S} {5,D} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {3,D}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30563, 'd12': 1.42103, 'd13': 2.7049},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 320""",
    longDesc = 
u"""
""",
)

entry(
    index = 690,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,D} {3,S} {8,S}
2     C u0 p0 c0 {1,D} {4,S} {6,S}
3     C u0 p0 c0 {1,S} {5,D} {7,S}
4  *3 C u1 p0 c0 {2,S} {9,S} {10,S}
5     C u0 p0 c0 {3,D} {11,S} {12,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,D} {9,S}
3     C u0 p0 c0 {2,D} {4,S} {11,S}
4     C u0 p0 c0 {3,S} {5,D} {10,S}
5     C u0 p0 c0 {4,D} {12,S} {13,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.35345, 'd12': 1.39477, 'd13': 2.73862},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 321""",
    longDesc = 
u"""
""",
)

entry(
    index = 691,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,D} {4,S}
2 *1 C u0 p0 c0 {1,S} {5,D} {6,S}
3    C u0 p0 c0 {1,D} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
6 *2 H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *3 C u1 p0 c0 {1,S} {4,S} {9,S}
3     C u0 p0 c0 {1,S} {5,D} {10,S}
4     C u0 p0 c0 {2,S} {6,D} {11,S}
5     C u0 p0 c0 {3,D} {6,S} {12,S}
6     C u0 p0 c0 {4,D} {5,S} {13,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {5,S}
13    H u0 p0 c0 {6,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2     C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3     C u0 p0 c0 {2,S} {5,D} {11,S}
4     C u0 p0 c0 {1,S} {6,D} {12,S}
5     C u0 p0 c0 {3,D} {6,S} {13,S}
6     C u0 p0 c0 {4,D} {5,S} {14,S}
7  *2 H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.31698, 'd12': 1.44654, 'd13': 2.73633},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 322""",
    longDesc = 
u"""
""",
)

entry(
    index = 692,
    reactant1 = """
multiplicity 2
1 *1 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {7,S}
2     C u0 p0 c0 {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0 {6,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0 {1,S} {6,S} {18,D}
6  *3 C u1 p0 c0 {4,S} {5,S} {17,S}
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
17    H u0 p0 c0 {6,S}
18    O u0 p2 c0 {5,D}
""",
    product1 = """
1     C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  *1 C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0 {1,S} {2,S} {19,D}
7     H u0 p0 c0 {1,S}
8  *2 H u0 p0 c0 {2,S}
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
""",
    product2 = """
multiplicity 3
1 *3 C u2 p0 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24477, 'd12': 1.44365, 'd13': 2.68253},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 323""",
    longDesc = 
u"""
""",
)

entry(
    index = 693,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25004, 'd12': 1.47071, 'd13': 2.7138},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 324""",
    longDesc = 
u"""
""",
)

entry(
    index = 694,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33069, 'd12': 1.36693, 'd13': 2.69409},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 325""",
    longDesc = 
u"""
""",
)

entry(
    index = 695,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.24931, 'd12': 1.04556, 'd13': 2.28907},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 326""",
    longDesc = 
u"""
""",
)

entry(
    index = 696,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.1469, 'd12': 1.50989, 'd13': 2.63461},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 327""",
    longDesc = 
u"""
""",
)

entry(
    index = 697,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.14943, 'd12': 1.44047, 'd13': 2.58595},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 328""",
    longDesc = 
u"""
""",
)

entry(
    index = 698,
    reactant1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27808, 'd12': 1.25759, 'd13': 2.5216},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 329""",
    longDesc = 
u"""
""",
)

entry(
    index = 699,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30388, 'd12': 1.39822, 'd13': 2.69887},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 330""",
    longDesc = 
u"""
""",
)

entry(
    index = 700,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,D} {5,S}
2     C u0 p0 c0 {1,S} {4,D} {6,S}
3     C u0 p0 c0 {1,D} {7,S} {8,S}
4     C u0 p0 c0 {2,D} {9,S} {10,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {3,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {6,S} {7,S}
3    C u0 p0 c0 {4,D} {8,S} {9,S}
4 *3 C u1 p0 c0 {1,S} {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23827, 'd12': 1.48659, 'd13': 2.7203},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 331""",
    longDesc = 
u"""
""",
)

entry(
    index = 701,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22245, 'd12': 1.50256, 'd13': 2.71956},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 332""",
    longDesc = 
u"""
""",
)

entry(
    index = 702,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22274, 'd12': 1.50503, 'd13': 2.71493},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 333""",
    longDesc = 
u"""
""",
)

entry(
    index = 703,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.24181, 'd12': 1.47479, 'd13': 2.71435},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 334""",
    longDesc = 
u"""
""",
)

entry(
    index = 704,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28031, 'd12': 1.4227, 'd13': 2.70008},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 335""",
    longDesc = 
u"""
""",
)

entry(
    index = 705,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31124, 'd12': 1.40173, 'd13': 2.68493},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 336""",
    longDesc = 
u"""
""",
)

entry(
    index = 706,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.36021, 'd12': 1.37804, 'd13': 2.71526},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 337""",
    longDesc = 
u"""
""",
)

entry(
    index = 707,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30218, 'd12': 1.39284, 'd13': 2.68806},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 338""",
    longDesc = 
u"""
""",
)

entry(
    index = 708,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26907, 'd12': 1.44471, 'd13': 2.70983},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 339""",
    longDesc = 
u"""
""",
)

entry(
    index = 709,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.1971, 'd12': 1.51223, 'd13': 2.69609},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 340""",
    longDesc = 
u"""
""",
)

entry(
    index = 710,
    reactant1 = """
1    C u0 p0 c0 {2,T} {3,S}
2 *1 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,T} {3,S}
2 *3 C u1 p0 c0 {1,T}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.12015, 'd12': 1.87803, 'd13': 2.90963},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 341""",
    longDesc = 
u"""
""",
)

entry(
    index = 711,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.23495, 'd12': 1.50981, 'd13': 2.73802},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 342""",
    longDesc = 
u"""
""",
)

entry(
    index = 712,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31543, 'd12': 1.41701, 'd13': 2.72946},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 343""",
    longDesc = 
u"""
""",
)

entry(
    index = 713,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.22696, 'd12': 1.08669, 'd13': 2.31365},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 344""",
    longDesc = 
u"""
""",
)

entry(
    index = 714,
    reactant1 = """
multiplicity 2
1 *1 O u1 p2 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 3
1 *3 O u2 p2 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.20524, 'd12': 1.35558, 'd13': 2.56073},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 345""",
    longDesc = 
u"""
""",
)

entry(
    index = 715,
    reactant1 = """
1    O u0 p2 c0 {2,S} {3,S}
2 *1 O u0 p2 c0 {1,S} {4,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.29463, 'd12': 1.26548, 'd13': 2.53967},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 346""",
    longDesc = 
u"""
""",
)

entry(
    index = 716,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {1,S}
7    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,T}
3    C u0 p0 c0 {2,T} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28483, 'd12': 1.42982, 'd13': 2.70766},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 347""",
    longDesc = 
u"""
""",
)

entry(
    index = 717,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8  *2 H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24783, 'd12': 1.49281, 'd13': 2.73394},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 348""",
    longDesc = 
u"""
""",
)

entry(
    index = 718,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5  *2 H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0 {1,S} {2,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25929, 'd12': 1.47588, 'd13': 2.72785},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 349""",
    longDesc = 
u"""
""",
)

entry(
    index = 719,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {7,S}
3    O u0 p2 c0 {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.28719, 'd12': 1.45355, 'd13': 2.71445},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 350""",
    longDesc = 
u"""
""",
)

entry(
    index = 720,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8 *2 H u0 p0 c0 {2,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24675, 'd12': 1.49597, 'd13': 2.73547},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 351""",
    longDesc = 
u"""
""",
)

entry(
    index = 721,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3 *1 O u0 p2 c0 {1,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *3 O u1 p2 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.21167, 'd12': 1.35029, 'd13': 2.55664},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 352""",
    longDesc = 
u"""
""",
)

entry(
    index = 722,
    reactant1 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,D} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
7 *2 H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.33141, 'd12': 1.41773, 'd13': 2.73482},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 353""",
    longDesc = 
u"""
""",
)

entry(
    index = 723,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,D}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,D} {6,S}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.27473, 'd12': 1.44527, 'd13': 2.71553},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 354""",
    longDesc = 
u"""
""",
)

entry(
    index = 724,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5 *2 H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {6,S} {7,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2491, 'd12': 1.49166, 'd13': 2.73256},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 355""",
    longDesc = 
u"""
""",
)

entry(
    index = 725,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,D}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    O u0 p2 c0 {2,D}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {4,S}
2    C u0 p0 c0 {1,D} {3,D}
3    O u0 p2 c0 {2,D}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22726, 'd12': 1.48687, 'd13': 2.69238},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 356""",
    longDesc = 
u"""
""",
)

entry(
    index = 726,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,D} {4,S}
2    H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
4 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.31716, 'd12': 1.44528, 'd13': 2.70575},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 357""",
    longDesc = 
u"""
""",
)

entry(
    index = 727,
    reactant1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {4,D} {10,S}
4     C u0 p0 c0 {3,D} {11,S} {12,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
12    H u0 p0 c0 {4,S}
""",
    reactant2 = """
multiplicity 2
1  *3 C u1 p0 c0 {2,S} {3,S} {6,S}
2     C u0 p0 c0 {1,S} {4,D} {7,S}
3     C u0 p0 c0 {1,S} {5,D} {8,S}
4     C u0 p0 c0 {2,D} {5,S} {9,S}
5     C u0 p0 c0 {3,D} {4,S} {10,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {4,S}
10    H u0 p0 c0 {5,S}
""",
    product1 = """
1  *1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6  *2 H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2  *3 C u1 p0 c0 {1,S} {3,S} {8,S}
3     C u0 p0 c0 {2,S} {4,D} {9,S}
4     C u0 p0 c0 {3,D} {10,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32679, 'd12': 1.39346, 'd13': 2.71818},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 358""",
    longDesc = 
u"""
""",
)

entry(
    index = 728,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.39771, 'd12': 1.27339, 'd13': 2.67085},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 359""",
    longDesc = 
u"""
""",
)

entry(
    index = 729,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *1 C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11 *2 H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0 {1,S} {7,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.2163, 'd12': 1.50984, 'd13': 2.71499},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 360""",
    longDesc = 
u"""
""",
)

entry(
    index = 730,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    distances = DistanceData(
        distances = {'d23': 1.46973, 'd12': 0.850002, 'd13': 2.31972},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 361""",
    longDesc = 
u"""
""",
)

entry(
    index = 731,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22001, 'd12': 1.26358, 'd13': 2.46578},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 362""",
    longDesc = 
u"""
""",
)

entry(
    index = 732,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 3
1 *3 O u1 p2 c0 {2,S}
2    O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
multiplicity 2
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u1 p2 c0 {1,S}
3 *2 H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.02215, 'd12': 1.71724, 'd13': 2.71885},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 363""",
    longDesc = 
u"""
""",
)

entry(
    index = 733,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *1 C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11 *2 H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3 *3 O u1 p2 c0 {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2    O u0 p2 c0 {1,S} {4,S}
3 *2 H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.08854, 'd12': 1.43772, 'd13': 2.51563},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 364""",
    longDesc = 
u"""
""",
)

entry(
    index = 734,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *1 C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11 *2 H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2    C u0 p0 c0 {1,D} {3,D}
3 *3 C u1 p0 c0 {2,D} {6,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {3,D} {4,S} {5,S}
2    C u0 p0 c0 {3,D} {6,S} {7,S}
3    C u0 p0 c0 {1,D} {2,D}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.22673, 'd12': 1.45942, 'd13': 2.6851},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 365""",
    longDesc = 
u"""
""",
)

entry(
    index = 735,
    reactant1 = """
1 *1 C u0 p0 c0 {2,D} {3,S} {4,S}
2    C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0 {1,D} {5,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.36199, 'd12': 1.2893, 'd13': 2.64125},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 366""",
    longDesc = 
u"""
""",
)

entry(
    index = 736,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9 *2 H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {1,S} {3,D} {7,S}
3 *3 C u1 p0 c0 {2,D} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.35669, 'd12': 1.292, 'd13': 2.63872},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 367""",
    longDesc = 
u"""
""",
)

entry(
    index = 737,
    reactant1 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,D} {7,S}
3    C u0 p0 c0 {2,D} {8,S} {9,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4  *1 C u0 p0 c0 {2,D} {5,S} {10,S}
5     C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10 *2 H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': 1.39863, 'd12': 1.26716, 'd13': 2.65954},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 368""",
    longDesc = 
u"""
""",
)

entry(
    index = 738,
    reactant1 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *1 C u0 p0 c0 {3,D} {4,S} {11,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11 *2 H u0 p0 c0 {5,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,D} {8,S}
3     C u0 p0 c0 {1,S} {5,D} {9,S}
4     C u0 p0 c0 {2,D} {5,S} {10,S}
5  *3 C u1 p0 c0 {3,D} {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     H u0 p0 c0 {1,S}
5     H u0 p0 c0 {1,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25243, 'd12': 1.43377, 'd13': 2.683},
        method = "m062x/6-311+G(2df,2p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 369""",
    longDesc = 
u"""
""",
)

