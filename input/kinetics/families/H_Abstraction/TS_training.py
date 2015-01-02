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
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.40773504244', 'd12': '0.895297060023', 'd13': '2.30303210246'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 2,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
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
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.35892133446', 'd12': '0.930299051641', 'd13': '2.28893519078'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 3,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.20216645606', 'd12': '0.907894558278', 'd13': '2.10402794429'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 4,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 *2 H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.21988501633', 'd12': '1.15309849454', 'd13': '2.37290946709'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 5,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
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
1 *3 H u1 p0 c0
""",
    product2 = """
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {3,S} {6,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.46347894682', 'd12': '0.862862296846', 'd13': '2.32579722591'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 6,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1    O u0 p2 c0 {2,S} {4,S}
2 *1 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.06757172779', 'd12': '1.11574127633', 'd13': '2.1796554827'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 7,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
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
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
        distances = {'d23': '0.926273983824', 'd12': '1.36413844572', 'd13': '2.29011119802'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 8,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
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
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.08060600298', 'd12': '1.23289966705', 'd13': '2.31166939106'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 9,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *3 O u1 p2 c0 {2,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    O u0 p2 c0 {1,S} {3,S}
3 *1 O u0 p2 c0 {2,S} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.04828664688', 'd12': '1.17928080736', 'd13': '2.22345150147'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 10,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
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
1 *3 H u1 p0 c0
""",
    product2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': '1.19436701782', 'd12': '1.23398956601', 'd13': '2.42765010692'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 11,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
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
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
        distances = {'d23': '0.856116451331', 'd12': '1.47813602871', 'd13': '2.33353250223'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 12,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
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
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
        distances = {'d23': '0.890380160538', 'd12': '1.41348718108', 'd13': '2.3037243324'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 13,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  *1 C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *3 C u1 p0 c0 {2,S} {12,S} {13,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.929233924724', 'd12': '1.36327979666', 'd13': '2.29221727048'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 14,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
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
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
        distances = {'d23': '0.857297575577', 'd12': '1.47462637073', 'd13': '2.33091998893'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 15,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  *3 C u1 p0 c0 {1,S} {3,S} {13,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  *2 H u0 p0 c0 {2,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.30720965209', 'd12': '0.974384887201', 'd13': '2.28142288545'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 16,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  *1 C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     O u0 p2 c0 {2,S} {12,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     O u0 p2 c0 {2,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.929232557334', 'd12': '1.36776843715', 'd13': '2.2968743381'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 17,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1 *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {3,S} {7,D} {8,S}
3    O u0 p2 c0 {1,S} {2,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {3,S} {5,S} {6,S}
2    C u0 p0 c0 {3,S} {4,D} {7,S}
3    O u0 p2 c0 {1,S} {2,S}
4    O u0 p2 c0 {2,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.955049619099', 'd12': '1.32911528045', 'd13': '2.28383585417'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 18,
    reactant1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {4,D} {11,S}
4  *3 C u1 p0 c0 {2,S} {3,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {4,D} {12,S}
4  *1 C u0 p0 c0 {2,S} {3,D} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11 *2 H u0 p0 c0 {4,S}
12    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.41659613444', 'd12': '0.887625561499', 'd13': '2.30400248858'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 19,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  *1 C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5     O u0 p2 c0 {3,S} {15,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12 *2 H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  *3 C u1 p0 c0 {2,S} {12,S} {13,S}
5     O u0 p2 c0 {3,S} {14,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.929562714059', 'd12': '1.35777238782', 'd13': '2.28701840306'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 20,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5     O u0 p2 c0 {1,S} {15,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *3 C u1 p0 c0 {1,S} {12,S} {13,S}
5     O u0 p2 c0 {1,S} {14,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.923478017904', 'd12': '1.36923344491', 'd13': '2.29270714272'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 21,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  *1 C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {5,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  *3 C u1 p0 c0 {2,S} {15,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.927276316146', 'd12': '1.36286435818', 'd13': '2.28958345535'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 22,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  *1 C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6     H u0 p0 c0 {1,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  *3 C u1 p0 c0 {1,S} {4,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.970596361047', 'd12': '1.31339574095', 'd13': '2.28396108373'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 23,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3     C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4     C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  *3 C u1 p0 c0 {2,S} {4,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.976300411313', 'd12': '1.30507883057', 'd13': '2.28125066263'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 24,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  *3 C u1 p0 c0 {1,S} {15,S} {16,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.919883004244', 'd12': '1.37805888248', 'd13': '2.29790558097'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 25,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  *1 C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  *3 C u1 p0 c0 {1,S} {15,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.92744513748', 'd12': '1.37106798486', 'd13': '2.29850984591'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 26,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
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
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
        distances = {'d23': '0.850034093713', 'd12': '1.4930819397', 'd13': '2.34311603157'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 27,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {5,B} {8,S}
3     C u0 p0 c0 {1,B} {6,B} {9,S}
4     C u0 p0 c0 {5,B} {6,B} {10,S}
5     C u0 p0 c0 {2,B} {4,B} {11,S}
6     C u0 p0 c0 {3,B} {4,B} {12,S}
7  *1 O u0 p2 c0 {1,S} {13,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13 *2 H u0 p0 c0 {7,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {5,B} {8,S}
3     C u0 p0 c0 {1,B} {6,B} {9,S}
4     C u0 p0 c0 {5,B} {6,B} {10,S}
5     C u0 p0 c0 {2,B} {4,B} {11,S}
6     C u0 p0 c0 {3,B} {4,B} {12,S}
7  *3 O u1 p2 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.08657681722', 'd12': '1.08110686108', 'd13': '2.16027024006'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 28,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  *1 C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0 {1,S} {4,B} {5,B}
4     C u0 p0 c0 {3,B} {7,B} {14,S}
5     C u0 p0 c0 {3,B} {8,B} {15,S}
6     C u0 p0 c0 {7,B} {8,B} {16,S}
7     C u0 p0 c0 {4,B} {6,B} {17,S}
8     C u0 p0 c0 {5,B} {6,B} {18,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {1,S}
11 *2 H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {6,S}
17    H u0 p0 c0 {7,S}
18    H u0 p0 c0 {8,S}
""",
    product1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2     C u0 p0 c0 {1,S} {3,B} {4,B}
3     C u0 p0 c0 {2,B} {6,B} {11,S}
4     C u0 p0 c0 {2,B} {7,B} {12,S}
5     C u0 p0 c0 {6,B} {7,B} {13,S}
6     C u0 p0 c0 {3,B} {5,B} {14,S}
7     C u0 p0 c0 {4,B} {5,B} {15,S}
8  *3 C u1 p0 c0 {1,S} {16,S} {17,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
15    H u0 p0 c0 {7,S}
16    H u0 p0 c0 {8,S}
17    H u0 p0 c0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.923728822558', 'd12': '1.36787122418', 'd13': '2.29107401551'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""
""",
)

entry(
    index = 29,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.37890', 'd12': '1.33014', 'd13': '2.70895'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 30,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.44233', 'd12': '1.28923', 'd13': '2.73121'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 31,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.30536', 'd12': '1.20569', 'd13': '2.51006'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 32,
    reactant1 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
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
1    O u0 p2 c0 {2,S} {4,S}
2 *1 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
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
        distances = {'d23': '1.14362', 'd12': '1.40355', 'd13': '2.54716'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 33,
    reactant1 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
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
1    O u0 p2 c0 {2,S} {4,S}
2 *1 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
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
        distances = {'d23': '1.22242', 'd12': '1.32319', 'd13': '2.54544'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 34,
    reactant1 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
1    O u0 p2 c0 {2,S} {4,S}
2 *1 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
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
        distances = {'d23': '1.10392', 'd12': '1.27899', 'd13': '2.34834'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 35,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.37951', 'd12': '1.32326', 'd13': '2.70269'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 36,
    reactant1 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1    O u0 p2 c0 {2,S} {4,S}
2 *3 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
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
        distances = {'d23': '1.15831', 'd12': '1.38612', 'd13': '2.54409'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 37,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {3,S} {6,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.31192', 'd12': '1.37209', 'd13': '2.68374'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 38,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3     C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  *1 C u0 p0 c0 {1,S} {3,S} {5,S} {12,S}
5  *2 H u0 p0 c0 {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  *3 C u1 p0 c0 {2,S} {3,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.39021', 'd12': '1.31082', 'd13': '2.70089'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 39,
    reactant1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {3,S}
3    O u0 p2 c0 {1,S} {2,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {3,S}
3    O u0 p2 c0 {1,S} {2,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.35719', 'd12': '1.33957', 'd13': '2.69461'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 40,
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
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {3,S}
3    O u0 p2 c0 {1,S} {2,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {3,S}
3    O u0 p2 c0 {1,S} {2,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.32993', 'd12': '1.37733', 'd13': '2.70362'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 41,
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
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {2,S}
4 *2 H u0 p0 c0 {1,S}
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
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {6,S}
3    O u0 p2 c0 {1,S} {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.33663', 'd12': '1.36697', 'd13': '2.70329'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 42,
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
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
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
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 *3 C u1 p0 c0 {1,S} {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.30692', 'd12': '1.38471', 'd13': '2.69157'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 43,
    reactant1 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
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
1 *1 O u0 p2 c0 {2,S} {3,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.39456', 'd12': '1.18856', 'd13': '2.58134'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 44,
    reactant1 = """
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
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
1 *1 O u0 p2 c0 {2,S} {3,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.32977', 'd12': '1.05831', 'd13': '2.28959'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""
""",
)

entry(
    index = 45,
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
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.895297060023', 'd12': '1.40773504244', 'd13': '2.30303210246'},
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
    index = 46,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
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
        distances = {'d23': '0.930299051641', 'd12': '1.35892133446', 'd13': '2.28893519078'},
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
    index = 47,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.907894558278', 'd12': '1.20216645606', 'd13': '2.10402794429'},
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
    index = 48,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1 *1 C u0 p0 c0 {2,S} {3,D} {4,S}
2 *2 H u0 p0 c0 {1,S}
3    O u0 p2 c0 {1,D}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,D} {3,S}
2    O u0 p2 c0 {1,D}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.15309849454', 'd12': '1.21988501633', 'd13': '2.37290946709'},
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
    index = 49,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {3,S} {6,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
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
        distances = {'d23': '0.862862296846', 'd12': '1.46347894682', 'd13': '2.32579722591'},
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
    index = 50,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1    O u0 p2 c0 {2,S} {4,S}
2 *1 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.11574127633', 'd12': '1.06757172779', 'd13': '2.1796554827'},
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
    index = 51,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
1 *3 H u1 p0 c0
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
        distances = {'d23': '1.36413844572', 'd12': '0.926273983824', 'd13': '2.29011119802'},
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
    index = 52,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
multiplicity 2
1 *3 H u1 p0 c0
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
        distances = {'d23': '1.23289966705', 'd12': '1.08060600298', 'd13': '2.31166939106'},
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
    index = 53,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2    O u0 p2 c0 {1,S} {3,S}
3 *1 O u0 p2 c0 {2,S} {7,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {3,S}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *3 O u1 p2 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.17928080736', 'd12': '1.04828664688', 'd13': '2.22345150147'},
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
    index = 54,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,S} {6,S} {7,D}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6 *2 H u0 p0 c0 {2,S}
7    O u0 p2 c0 {2,D}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.23398956601', 'd12': '1.19436701782', 'd13': '2.42765010692'},
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
    index = 55,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
1 *3 H u1 p0 c0
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
        distances = {'d23': '1.47813602871', 'd12': '0.856116451331', 'd13': '2.33353250223'},
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
    index = 56,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
1 *3 H u1 p0 c0
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
        distances = {'d23': '1.41348718108', 'd12': '0.890380160538', 'd13': '2.3037243324'},
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
    index = 57,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *3 C u1 p0 c0 {2,S} {12,S} {13,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  *1 C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.36327979666', 'd12': '0.929233924724', 'd13': '2.29221727048'},
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
    index = 58,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': '1.47462637073', 'd12': '0.857297575577', 'd13': '2.33091998893'},
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
    index = 59,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {5,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  *2 H u0 p0 c0 {2,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {4,S} {10,S} {11,S} {12,S}
4  *3 C u1 p0 c0 {1,S} {3,S} {13,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.974384887201', 'd12': '1.30720965209', 'd13': '2.28142288545'},
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
    index = 60,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  *3 C u1 p0 c0 {1,S} {9,S} {10,S}
4     O u0 p2 c0 {2,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  *1 C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     O u0 p2 c0 {2,S} {12,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.36776843715', 'd12': '0.929232557334', 'd13': '2.2968743381'},
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
    index = 61,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {3,S} {5,S} {6,S}
2    C u0 p0 c0 {3,S} {4,D} {7,S}
3    O u0 p2 c0 {1,S} {2,S}
4    O u0 p2 c0 {2,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1 *1 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0 {3,S} {7,D} {8,S}
3    O u0 p2 c0 {1,S} {2,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    O u0 p2 c0 {2,D}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.32911528045', 'd12': '0.955049619099', 'd13': '2.28383585417'},
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
    index = 62,
    reactant1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    reactant2 = """
1     C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {4,D} {12,S}
4  *1 C u0 p0 c0 {2,S} {3,D} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11 *2 H u0 p0 c0 {4,S}
12    H u0 p0 c0 {3,S}
""",
    product1 = """
1 *2 H u0 p0 c0 {2,S}
2 *1 H u0 p0 c0 {1,S}
""",
    product2 = """
multiplicity 2
1     C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0 {1,S} {4,D} {11,S}
4  *3 C u1 p0 c0 {2,S} {3,D}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {2,S}
11    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': '0.887625561499', 'd12': '1.41659613444', 'd13': '2.30400248858'},
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
    index = 63,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  *3 C u1 p0 c0 {2,S} {12,S} {13,S}
5     O u0 p2 c0 {3,S} {14,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  *1 C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5     O u0 p2 c0 {3,S} {15,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12 *2 H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.35777238782', 'd12': '0.929562714059', 'd13': '2.28701840306'},
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
    index = 64,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4  *3 C u1 p0 c0 {1,S} {12,S} {13,S}
5     O u0 p2 c0 {1,S} {14,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5     O u0 p2 c0 {1,S} {15,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.36923344491', 'd12': '0.923478017904', 'd13': '2.29270714272'},
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
    index = 65,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  *3 C u1 p0 c0 {2,S} {15,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {1,S} {13,S} {14,S} {15,S}
5  *1 C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {5,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.36286435818', 'd12': '0.927276316146', 'd13': '2.28958345535'},
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
    index = 66,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  *3 C u1 p0 c0 {1,S} {4,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  *1 C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6     H u0 p0 c0 {1,S}
7  *2 H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.31339574095', 'd12': '0.970596361047', 'd13': '2.28396108373'},
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
    index = 67,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
3     C u0 p0 c0 {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0 {5,S} {13,S} {14,S} {15,S}
5  *3 C u1 p0 c0 {2,S} {4,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {3,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {4,S}
16    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  *1 C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3     C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4     C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0 {3,S} {15,S} {16,S} {17,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {1,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.30507883057', 'd12': '0.976300411313', 'd13': '2.28125066263'},
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
    index = 68,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5  *3 C u1 p0 c0 {1,S} {15,S} {16,S}
6     H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0 {1,S} {15,S} {16,S} {17,S}
6  *2 H u0 p0 c0 {2,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.37805888248', 'd12': '0.919883004244', 'd13': '2.29790558097'},
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
    index = 69,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {2,S} {12,S} {13,S} {14,S}
5  *3 C u1 p0 c0 {1,S} {15,S} {16,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
3  *1 C u0 p0 c0 {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0 {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9  *2 H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {4,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {5,S}
17    H u0 p0 c0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.37106798486', 'd12': '0.92744513748', 'd13': '2.29850984591'},
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
    index = 70,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
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
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
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
    distances = DistanceData(
        distances = {'d23': '1.4930819397', 'd12': '0.850034093713', 'd13': '2.34311603157'},
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
    index = 71,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {5,B} {8,S}
3     C u0 p0 c0 {1,B} {6,B} {9,S}
4     C u0 p0 c0 {5,B} {6,B} {10,S}
5     C u0 p0 c0 {2,B} {4,B} {11,S}
6     C u0 p0 c0 {3,B} {4,B} {12,S}
7  *3 O u1 p2 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,B} {3,B} {7,S}
2     C u0 p0 c0 {1,B} {5,B} {8,S}
3     C u0 p0 c0 {1,B} {6,B} {9,S}
4     C u0 p0 c0 {5,B} {6,B} {10,S}
5     C u0 p0 c0 {2,B} {4,B} {11,S}
6     C u0 p0 c0 {3,B} {4,B} {12,S}
7  *1 O u0 p2 c0 {1,S} {13,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11    H u0 p0 c0 {5,S}
12    H u0 p0 c0 {6,S}
13 *2 H u0 p0 c0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.08110686108', 'd12': '1.08657681722', 'd13': '2.16027024006'},
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
    index = 72,
    reactant1 = """
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {8,S} {9,S} {10,S}
2     C u0 p0 c0 {1,S} {3,B} {4,B}
3     C u0 p0 c0 {2,B} {6,B} {11,S}
4     C u0 p0 c0 {2,B} {7,B} {12,S}
5     C u0 p0 c0 {6,B} {7,B} {13,S}
6     C u0 p0 c0 {3,B} {5,B} {14,S}
7     C u0 p0 c0 {4,B} {5,B} {15,S}
8  *3 C u1 p0 c0 {1,S} {16,S} {17,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {1,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
13    H u0 p0 c0 {5,S}
14    H u0 p0 c0 {6,S}
15    H u0 p0 c0 {7,S}
16    H u0 p0 c0 {8,S}
17    H u0 p0 c0 {8,S}
""",
    product1 = """
multiplicity 2
1 *3 H u1 p0 c0
""",
    product2 = """
1     C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  *1 C u0 p0 c0 {1,S} {11,S} {12,S} {13,S}
3     C u0 p0 c0 {1,S} {4,B} {5,B}
4     C u0 p0 c0 {3,B} {7,B} {14,S}
5     C u0 p0 c0 {3,B} {8,B} {15,S}
6     C u0 p0 c0 {7,B} {8,B} {16,S}
7     C u0 p0 c0 {4,B} {6,B} {17,S}
8     C u0 p0 c0 {5,B} {6,B} {18,S}
9     H u0 p0 c0 {1,S}
10    H u0 p0 c0 {1,S}
11 *2 H u0 p0 c0 {2,S}
12    H u0 p0 c0 {2,S}
13    H u0 p0 c0 {2,S}
14    H u0 p0 c0 {4,S}
15    H u0 p0 c0 {5,S}
16    H u0 p0 c0 {6,S}
17    H u0 p0 c0 {7,S}
18    H u0 p0 c0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.36787122418', 'd12': '0.923728822558', 'd13': '2.29107401551'},
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
    index = 73,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.33014', 'd12': '1.37890', 'd13': '2.70895'},
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
    index = 74,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.28923', 'd12': '1.44233', 'd13': '2.73121'},
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
    index = 75,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.20569', 'd12': '1.30536', 'd13': '2.51006'},
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
    index = 76,
    reactant1 = """
1    O u0 p2 c0 {2,S} {4,S}
2 *1 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
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
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
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
        distances = {'d23': '1.40355', 'd12': '1.14362', 'd13': '2.54716'},
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
    index = 77,
    reactant1 = """
1    O u0 p2 c0 {2,S} {4,S}
2 *1 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
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
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
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
        distances = {'d23': '1.32319', 'd12': '1.22242', 'd13': '2.54544'},
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
    index = 78,
    reactant1 = """
1    O u0 p2 c0 {2,S} {4,S}
2 *1 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
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
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.27899', 'd12': '1.10392', 'd13': '2.34834'},
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
    index = 79,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.32326', 'd12': '1.37951', 'd13': '2.70269'},
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
    index = 80,
    reactant1 = """
1    O u0 p2 c0 {2,S} {4,S}
2 *3 O u0 p2 c0 {1,S} {3,S}
3 *2 H u0 p0 c0 {2,S}
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
multiplicity 2
1    O u0 p2 c0 {2,S} {3,S}
2 *3 O u1 p2 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    product2 = """
1    C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.38612', 'd12': '1.15831', 'd13': '2.54409'},
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
    index = 81,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
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
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1    C u0 p0 c0 {2,D} {4,S} {5,S}
2 *1 C u0 p0 c0 {1,D} {3,S} {6,S}
3 *2 H u0 p0 c0 {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.37209', 'd12': '1.31192', 'd13': '2.68374'},
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
    index = 82,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  *3 C u1 p0 c0 {2,S} {3,S} {11,S}
5     H u0 p0 c0 {1,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {4,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1     C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2     C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3     C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  *1 C u0 p0 c0 {1,S} {3,S} {5,S} {12,S}
5  *2 H u0 p0 c0 {4,S}
6     H u0 p0 c0 {1,S}
7     H u0 p0 c0 {1,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {3,S}
11    H u0 p0 c0 {3,S}
12    H u0 p0 c0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.31082', 'd12': '1.39021', 'd13': '2.70089'},
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
    index = 83,
    reactant1 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {3,S}
3    O u0 p2 c0 {1,S} {2,S}
4    H u0 p0 c0 {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
""",
    product2 = """
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {3,S}
3    O u0 p2 c0 {1,S} {2,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.33957', 'd12': '1.35719', 'd13': '2.69461'},
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
    index = 84,
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
1 *3 C u1 p0 c0 {2,S} {3,S} {4,S}
2    O u0 p2 c0 {1,S} {3,S}
3    O u0 p2 c0 {1,S} {2,S}
4    H u0 p0 c0 {1,S}
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
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    O u0 p2 c0 {1,S} {3,S}
3    O u0 p2 c0 {1,S} {2,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.37733', 'd12': '1.32993', 'd13': '2.70362'},
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
    index = 85,
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
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0 {1,S} {3,S} {6,S}
3    O u0 p2 c0 {1,S} {2,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
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
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    O u0 p2 c0 {1,S} {2,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.36697', 'd12': '1.33663', 'd13': '2.70329'},
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
    index = 86,
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
1    C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 *3 C u1 p0 c0 {1,S} {2,S} {8,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
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
1 *1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2    C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3    C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4 *2 H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {2,S}
8    H u0 p0 c0 {3,S}
9    H u0 p0 c0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': '1.38471', 'd12': '1.30692', 'd13': '2.69157'},
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
    index = 87,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.18856', 'd12': '1.39456', 'd13': '2.58134'},
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

entry(
    index = 88,
    reactant1 = """
1 *1 O u0 p2 c0 {2,S} {3,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
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
multiplicity 2
1 *3 O u1 p2 c0 {2,S}
2    H u0 p0 c0 {1,S}
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
        distances = {'d23': '1.05831', 'd12': '1.32977', 'd13': '2.28959'},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 44""",
    longDesc = 
u"""
""",
)

