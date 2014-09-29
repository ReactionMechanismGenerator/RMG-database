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
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0 
""",
    product1 = """
multiplicity 2
1 *1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *2 C u1 p0 c0  {1,S} {6,S} {7,S}
3 *3 H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.97297', 'd12': '1.34016', 'd13': '2.29179'},
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
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2  *3 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *2 C u1 p0 c0  {1,S} {9,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': '3.08317', 'd12': '1.36006', 'd13': '2.34603'},
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
1    C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *2 C u0 p0 c0  {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0  {2,D} {8,S} {9,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {3,S}
9    H u0 p0 c0  {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2  *3 C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0  {4,S} {10,S} {11,S} {12,S}
4  *2 C u1 p0 c0  {1,S} {3,S} {13,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '3.08163', 'd12': '1.36221', 'd13': '2.34488'},
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
1     C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {3,S} {8,S} {9,S} {10,S}
3  *1 C u0 p0 c0  {1,S} {2,S} {4,D}
4  *2 C u0 p0 c0  {3,D} {11,S} {12,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *3 C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5  *2 C u1 p0 c0  {1,S} {15,S} {16,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.88000', 'd12': '1.37248', 'd13': '2.31062'},
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
1     C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {3,S} {8,S} {9,S} {10,S}
3  *2 C u0 p0 c0  {1,S} {2,S} {4,D}
4  *1 C u0 p0 c0  {3,D} {11,S} {12,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {5,S} {6,S} {7,S}
2  *3 C u0 p0 c0  {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {5,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0  {5,S} {14,S} {15,S} {16,S}
5  *2 C u1 p0 c0  {1,S} {3,S} {4,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.88000', 'd12': '1.37248', 'd13': '2.31062'},
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
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 O u0 p2 c0  {1,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0  {1,S} {3,S} {7,S} {8,S}
3 *2 O u1 p2 c0  {2,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.80911', 'd12': '1.23467', 'd13': '2.24113'},
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
1 *2 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *1 O u0 p2 c0  {1,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2 *2 C u1 p0 c0  {3,S} {7,S} {8,S}
3 *1 O u0 p2 c0  {1,S} {2,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.81003', 'd12': '1.25974', 'd13': '1.95615'},
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
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 S u0 p2 c0  {1,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0  {1,S} {3,S} {7,S} {8,S}
3 *2 S u1 p2 c0  {2,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {2,S}
""",
    distances = DistanceData(
        distances = {'d23': '3.65010', 'd12': '1.63224', 'd13': '2.73871'},
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
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0  {1,S} {6,D} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *2 O u0 p2 c0  {2,D}
7    H u0 p0 c0  {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *3 C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *2 O u1 p2 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.68356', 'd12': '1.24443', 'd13': '2.17044'},
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
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *2 C u0 p0 c0  {1,S} {6,D} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *1 O u0 p2 c0  {2,D}
7    H u0 p0 c0  {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2  *3 C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
3  *2 C u1 p0 c0  {1,S} {4,S} {11,S}
4  *1 O u0 p2 c0  {2,S} {3,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.77240', 'd12': '1.26829', 'd13': '1.91478'},
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
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *2 C u0 p0 c0  {1,S} {2,S} {10,D}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10 *1 O u0 p2 c0  {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {4,S} {6,S} {7,S} {8,S}
2     C u0 p0 c0  {4,S} {9,S} {10,S} {11,S}
3  *3 C u0 p0 c0  {5,S} {12,S} {13,S} {14,S}
4  *2 C u1 p0 c0  {1,S} {2,S} {5,S}
5  *1 O u0 p2 c0  {3,S} {4,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.75326', 'd12': '1.27681', 'd13': '1.89043'},
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
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *1 C u0 p0 c0  {1,S} {2,S} {10,D}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10 *2 O u0 p2 c0  {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *3 C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5  *2 O u1 p2 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '2.59901', 'd12': '1.25449', 'd13': '2.13715'},
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
1     C u0 p0 c0  {2,S} {5,S} {6,S} {7,S}
2  *1 C u0 p0 c0  {1,S} {3,S} {4,D}
3     C u0 p0 c0  {2,S} {8,S} {9,S} {10,S}
4  *2 S u0 p2 c0  {2,D}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {3,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {6,S} {7,S} {8,S}
2  *1 C u0 p0 c0  {1,S} {3,S} {4,S} {5,S}
3  *3 C u0 p0 c0  {2,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  *2 S u1 p2 c0  {2,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': '3.17189', 'd12': '1.66891', 'd13': '2.49399'},
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
    index = 14,
    reactant1 = """
1 *2 C u0 p0 c0  {2,T} {3,S}
2 *1 C u0 p0 c0  {1,T} {4,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1 *3 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0  {1,S} {3,D} {7,S}
3 *2 C u1 p0 c0  {2,D} {8,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.071072, 'd12': 1.227205, 'd13': 2.339809},
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
1 *3 H u1 p0 c0 
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,D}
2    O u0 p2 c0  {1,D}
3 *2 O u0 p2 c0  {1,D}
""",
    product1 = """
multiplicity 2
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2    O u0 p2 c0  {1,D}
3 *2 O u1 p2 c0  {1,S}
4 *3 H u0 p0 c0  {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.132938, 'd12': 1.188381, 'd13': 1.594929},
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
1 *2 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *1 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    C u0 p0 c0  {1,S} {5,S} {6,S} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  *1 C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *2 C u1 p0 c0  {2,S} {12,S} {13,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.090076, 'd12': 1.362405, 'd13': 2.319306},
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
1    C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0  {1,S} {3,D} {7,S}
3 *2 C u0 p0 c0  {2,D} {8,S} {9,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {3,S}
9    H u0 p0 c0  {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2  *3 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *2 C u1 p0 c0  {1,S} {12,S} {13,S}
5     H u0 p0 c0  {1,S}
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
        distances = {'d23': 2.968669, 'd12': 1.36588, 'd13': 2.319554},
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
1 *1 C u0 p0 c0  {2,S} {3,S} {4,D}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4 *2 O u0 p2 c0  {1,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    C u0 p0 c0  {1,S} {5,S} {6,S} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3  *1 C u0 p0 c0  {1,S} {6,S} {10,S} {11,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6  *2 O u1 p2 c0  {3,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.804239, 'd12': 1.237281, 'd13': 2.216714},
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
1    H u0 p0 c0  {2,S}
2    O u0 p2 c0  {1,S} {3,S}
3 *3 C u1 p0 c0  {2,S} {4,S} {5,S}
4    H u0 p0 c0  {3,S}
5    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2  *3 C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3  *2 C u1 p0 c0  {1,S} {9,S} {10,S}
4     O u0 p2 c0  {2,S} {11,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.038853, 'd12': 1.364709, 'd13': 2.301401},
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
1    C u0 p0 c0  {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0  {1,D} {5,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 O u0 p2 c0  {1,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1 *1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *3 C u0 p0 c0  {1,S} {3,D} {7,S}
3    C u0 p0 c0  {2,D} {8,S} {9,S}
4 *2 O u1 p2 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {3,S}
9    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.867875, 'd12': 1.229678, 'd13': 2.298227},
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
1    C u0 p0 c0  {2,D} {3,S} {4,S}
2    C u0 p0 c0  {1,D} {5,S} {6,S}
3 *1 C u0 p0 c0  {1,S} {7,D} {8,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
7 *2 O u0 p2 c0  {3,D}
8    H u0 p0 c0  {3,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0 
""",
    product1 = """
multiplicity 2
1 *1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0  {1,S} {3,D} {7,S}
3    C u0 p0 c0  {2,D} {8,S} {9,S}
4 *2 O u1 p2 c0  {1,S}
5 *3 H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {3,S}
9    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.374435, 'd12': 1.233028, 'd13': 1.830001},
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
1    H u0 p0 c0  {2,S}
2 *1 C u0 p0 c0  {1,S} {3,T}
3 *2 C u0 p0 c0  {2,T} {4,S}
4    C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
5    H u0 p0 c0  {4,S}
6    H u0 p0 c0  {4,S}
7    H u0 p0 c0  {4,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
3  *1 C u0 p0 c0  {1,S} {4,D} {11,S}
4  *2 C u1 p0 c0  {2,S} {3,D}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.061247, 'd12': 1.228925, 'd13': 2.33573},
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
1     C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0  {1,S} {9,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 O u0 p2 c0  {1,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2  *3 C u0 p0 c0  {1,S} {3,S} {7,S} {8,S}
3  *1 C u0 p0 c0  {2,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9  *2 O u1 p2 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.800561, 'd12': 1.23818, 'd13': 2.216011},
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
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0  {1,S} {2,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {6,S}
2  *1 C u0 p0 c0  {1,S} {5,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5  *2 C u1 p0 c0  {2,S} {15,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.065754, 'd12': 1.365325, 'd13': 2.28955},
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
1     C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0  {1,S} {9,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {8,S} {9,S}
2     C u0 p0 c0  {1,S} {4,S} {6,S} {7,S}
3  *1 C u0 p0 c0  {1,S} {5,S} {10,S} {11,S}
4     C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  *2 C u1 p0 c0  {3,S} {15,S} {16,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.102136, 'd12': 1.364658, 'd13': 2.29863},
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
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0  {1,S} {2,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,T} {3,S}
2 *2 C u0 p0 c0  {1,T} {4,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4  *1 C u0 p0 c0  {1,S} {5,D} {13,S}
5  *2 C u1 p0 c0  {4,D} {14,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.086017, 'd12': 1.230931, 'd13': 2.312927},
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
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0  {1,S} {6,S} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {2,S}
""",
    reactant2 = """
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *2 C u0 p0 c0  {1,S} {6,D} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *1 O u0 p2 c0  {2,D}
7    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {4,S} {11,S} {12,S} {13,S}
4  *2 C u1 p0 c0  {3,S} {5,S} {14,S}
5  *1 O u0 p2 c0  {1,S} {4,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.801926, 'd12': 1.269238, 'd13': 1.93391},
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
1    C u0 p0 c0  {2,D} {3,S} {4,S}
2 *3 C u1 p0 c0  {1,D} {5,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
""",
    reactant2 = """
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0  {1,S} {6,D} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *2 O u0 p2 c0  {2,D}
7    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3  *3 C u0 p0 c0  {1,S} {4,D} {10,S}
4     C u0 p0 c0  {3,D} {11,S} {12,S}
5  *2 O u1 p2 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.711281, 'd12': 1.239306, 'd13': 2.214891},
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
1    C u0 p0 c0  {2,D} {3,S} {4,S}
2    C u0 p0 c0  {1,D} {5,S} {6,S}
3 *3 C u1 p0 c0  {1,S} {7,S} {8,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {3,S}
8    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2  *1 C u0 p0 c0  {1,S} {4,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {5,D} {10,S}
4  *2 C u1 p0 c0  {2,S} {11,S} {12,S}
5     C u0 p0 c0  {3,D} {13,S} {14,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {5,S}
14    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.941341, 'd12': 1.378152, 'd13': 2.156614},
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
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    reactant2 = """
1     C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
3  *1 C u0 p0 c0  {1,S} {4,D} {11,S}
4  *2 C u0 p0 c0  {2,S} {3,D} {12,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3  *3 C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0  {5,S} {13,S} {14,S} {15,S}
5  *2 C u1 p0 c0  {1,S} {4,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.97021, 'd12': 1.36751, 'd13': 2.321362},
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
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0  {1,S} {6,D} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *2 O u0 p2 c0  {2,D}
7    H u0 p0 c0  {2,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0  {1,S} {6,S} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2  *1 C u0 p0 c0  {1,S} {4,S} {5,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  *2 O u1 p2 c0  {2,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.663537, 'd12': 1.249064, 'd13': 2.137617},
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
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    reactant2 = """
1     C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *1 C u0 p0 c0  {1,S} {9,D} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9  *2 O u0 p2 c0  {3,D}
10    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2  *1 C u0 p0 c0  {1,S} {4,S} {5,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *3 C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  *2 O u1 p2 c0  {2,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.668259, 'd12': 1.245783, 'd13': 2.157034},
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
1     C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *3 C u1 p0 c0  {2,S} {12,S} {13,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {9,S} {10,S}
2  *3 C u0 p0 c0  {1,S} {4,S} {11,S} {12,S}
3     C u0 p0 c0  {1,S} {5,S} {7,S} {8,S}
4  *1 C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5     C u0 p0 c0  {3,S} {15,S} {16,S} {17,S}
6  *2 C u1 p0 c0  {4,S} {18,S} {19,S}
7     H u0 p0 c0  {3,S}
8     H u0 p0 c0  {3,S}
9     H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.071189, 'd12': 1.363694, 'd13': 2.313189},
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
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0  {1,S} {6,S} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {2,S}
""",
    reactant2 = """
1     C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2  *2 C u0 p0 c0  {1,S} {3,D} {7,S}
3  *1 C u0 p0 c0  {2,D} {8,S} {9,S}
4     O u0 p2 c0  {1,S} {10,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {3,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {4,S} {7,S} {8,S}
2  *1 C u0 p0 c0  {1,S} {5,S} {9,S} {10,S}
3     C u0 p0 c0  {5,S} {6,S} {11,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5  *2 C u1 p0 c0  {2,S} {3,S} {16,S}
6     O u0 p2 c0  {3,S} {17,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.083738, 'd12': 1.363391, 'd13': 2.332089},
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
1    C u0 p0 c0  {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0  {1,S} {5,S} {6,S}
3    C u0 p0 c0  {1,D} {7,S} {8,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {3,S}
8    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1    C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *2 C u0 p0 c0  {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0  {2,D} {8,S} {9,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {3,S}
9    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {4,S} {7,S} {8,S}
2  *3 C u0 p0 c0  {1,S} {5,S} {9,S} {10,S}
3     C u0 p0 c0  {4,S} {11,S} {12,S} {13,S}
4  *2 C u1 p0 c0  {1,S} {3,S} {14,S}
5     C u0 p0 c0  {2,S} {6,D} {15,S}
6     C u0 p0 c0  {5,D} {16,S} {17,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.962181, 'd12': 1.380982, 'd13': 2.154138},
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
1    C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *2 C u0 p0 c0  {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0  {2,D} {8,S} {9,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {3,S}
9    H u0 p0 c0  {3,S}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0  {1,S} {9,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3  *1 C u0 p0 c0  {1,S} {6,S} {11,S} {12,S}
4     C u0 p0 c0  {2,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {6,S} {16,S} {17,S} {18,S}
6  *2 C u1 p0 c0  {3,S} {5,S} {19,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.077102, 'd12': 1.366757, 'd13': 2.306282},
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
1     C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0  {4,S} {10,S} {11,S} {12,S}
4  *1 C u0 p0 c0  {1,S} {3,S} {13,D}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13 *2 O u0 p2 c0  {4,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0  {1,S} {5,S} {7,S} {8,S}
3  *3 C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0  {2,S} {15,S} {16,S} {17,S}
6  *2 O u1 p2 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.593958, 'd12': 1.255272, 'd13': 2.129003},
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
1     H u0 p0 c0  {2,S}
2     C u0 p0 c0  {1,S} {3,S} {4,D}
3     H u0 p0 c0  {2,S}
4     C u0 p0 c0  {2,D} {5,S} {6,S}
5     C u0 p0 c0  {4,S} {7,S} {8,S} {9,S}
6     H u0 p0 c0  {4,S}
7     H u0 p0 c0  {5,S}
8  *3 C u1 p0 c0  {5,S} {10,S} {11,S}
9     H u0 p0 c0  {5,S}
10    H u0 p0 c0  {8,S}
11    H u0 p0 c0  {8,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3  *1 C u0 p0 c0  {1,S} {5,S} {11,S} {12,S}
4     C u0 p0 c0  {2,S} {6,D} {13,S}
5  *2 C u1 p0 c0  {3,S} {14,S} {15,S}
6     C u0 p0 c0  {4,D} {16,S} {17,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {5,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.075197, 'd12': 1.361772, 'd13': 2.324172},
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
1     H u0 p0 c0  {2,S}
2     C u0 p0 c0  {1,S} {3,S} {4,S} {5,S}
3     H u0 p0 c0  {2,S}
4  *2 C u0 p0 c0  {2,S} {6,S} {7,D}
5     H u0 p0 c0  {2,S}
6     C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
7  *1 C u0 p0 c0  {4,D} {11,S} {12,S}
8     H u0 p0 c0  {6,S}
9     H u0 p0 c0  {6,S}
10    H u0 p0 c0  {6,S}
11    C u0 p0 c0  {7,S} {13,S} {14,S} {15,S}
12    H u0 p0 c0  {7,S}
13    H u0 p0 c0  {11,S}
14    H u0 p0 c0  {11,S}
15    H u0 p0 c0  {11,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {6,S} {7,S}
2  *3 C u0 p0 c0  {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0  {6,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0  {6,S} {17,S} {18,S} {19,S}
6  *2 C u1 p0 c0  {1,S} {4,S} {5,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.98811, 'd12': 1.373115, 'd13': 2.336523},
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
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0  {1,S} {6,S} {7,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {2,S}
7 *2 O u0 p2 c0  {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0  {1,S} {2,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {6,S}
2  *1 C u0 p0 c0  {1,S} {5,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0  {2,S} {15,S} {16,S} {17,S}
6     H u0 p0 c0  {1,S}
7  *2 O u1 p2 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.634861, 'd12': 1.256416, 'd13': 2.093432},
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
1     C u0 p0 c0  {4,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {4,S} {11,S} {12,S} {13,S}
4  *3 C u1 p0 c0  {1,S} {2,S} {3,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0  {1,S} {15,S} {16,S} {17,S}
6  *2 C u1 p0 c0  {2,S} {18,S} {19,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.066737, 'd12': 1.368086, 'd13': 2.265947},
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
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0  {1,S} {6,S} {7,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {2,S}
7 *2 O u0 p2 c0  {2,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *3 C u1 p0 c0  {1,S} {9,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3  *1 C u0 p0 c0  {1,S} {5,S} {6,S} {11,S}
4     C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0  {3,S} {15,S} {16,S} {17,S}
6  *2 O u1 p2 c0  {3,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.689679, 'd12': 1.247542, 'd13': 2.145617},
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
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    reactant2 = """
1     C u0 p0 c0  {2,S} {3,S} {5,S} {6,S}
2     C u0 p0 c0  {1,S} {4,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *1 C u0 p0 c0  {2,S} {12,D} {13,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12 *2 O u0 p2 c0  {4,D}
13    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2     C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3  *1 C u0 p0 c0  {1,S} {5,S} {6,S} {11,S}
4     C u0 p0 c0  {2,S} {12,S} {13,S} {14,S}
5  *3 C u0 p0 c0  {3,S} {15,S} {16,S} {17,S}
6  *2 O u1 p2 c0  {3,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.683927, 'd12': 1.245478, 'd13': 2.174495},
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
1     H u0 p0 c0  {2,S}
2     O u0 p2 c0  {1,S} {3,S}
3     C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
4     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
5     H u0 p0 c0  {3,S}
6     H u0 p0 c0  {3,S}
7  *3 C u1 p0 c0  {4,S} {10,S} {11,S}
8     H u0 p0 c0  {4,S}
9     H u0 p0 c0  {4,S}
10    H u0 p0 c0  {7,S}
11    H u0 p0 c0  {7,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 O u0 p2 c0  {1,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {7,S} {8,S}
2  *3 C u0 p0 c0  {1,S} {4,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {5,S} {11,S} {12,S}
4  *1 C u0 p0 c0  {2,S} {6,S} {13,S} {14,S}
5     O u0 p2 c0  {3,S} {15,S}
6  *2 O u1 p2 c0  {4,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.781465, 'd12': 1.238741, 'd13': 2.195651},
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
    index = 45,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {4,S} {6,S}
2     C u0 p0 c0  {1,S} {5,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5  *3 C u1 p0 c0  {2,S} {15,S} {16,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,S} {6,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {2,S}
6    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {5,S} {6,S} {8,S}
2     C u0 p0 c0  {1,S} {3,S} {9,S} {10,S}
3  *3 C u0 p0 c0  {2,S} {4,S} {11,S} {12,S}
4  *1 C u0 p0 c0  {3,S} {7,S} {13,S} {14,S}
5     C u0 p0 c0  {1,S} {15,S} {16,S} {17,S}
6     C u0 p0 c0  {1,S} {18,S} {19,S} {20,S}
7  *2 C u1 p0 c0  {4,S} {21,S} {22,S}
8     H u0 p0 c0  {1,S}
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
21    H u0 p0 c0  {7,S}
22    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.096972, 'd12': 1.364974, 'd13': 2.296433},
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
    index = 46,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {4,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {4,S} {11,S} {12,S} {13,S}
4  *3 C u1 p0 c0  {1,S} {2,S} {3,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1    C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *2 C u0 p0 c0  {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0  {2,D} {8,S} {9,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {3,S}
9    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2  *1 C u0 p0 c0  {1,S} {7,S} {8,S} {9,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {7,S} {19,S} {20,S} {21,S}
7  *2 C u1 p0 c0  {2,S} {6,S} {22,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
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
""",
    distances = DistanceData(
        distances = {'d23': 3.080852, 'd12': 1.370822, 'd13': 2.262773},
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
    index = 47,
    reactant1 = """
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *1 C u0 p0 c0  {1,S} {2,S} {10,D}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10 *2 O u0 p2 c0  {3,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0  {1,S} {2,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {8,S}
2  *1 C u0 p0 c0  {1,S} {5,S} {6,S} {7,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4     C u0 p0 c0  {1,S} {12,S} {13,S} {14,S}
5     C u0 p0 c0  {2,S} {15,S} {16,S} {17,S}
6     C u0 p0 c0  {2,S} {18,S} {19,S} {20,S}
7  *2 O u1 p2 c0  {2,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {5,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {6,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.576373, 'd12': 1.269519, 'd13': 2.053658},
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
    index = 48,
    reactant1 = """
1     H u0 p0 c0  {2,S}
2     O u0 p2 c0  {1,S} {3,S}
3     O u0 p2 c0  {2,S} {4,S}
4     C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
5     H u0 p0 c0  {4,S}
6     H u0 p0 c0  {4,S}
7  *1 C u0 p0 c0  {4,S} {8,S} {9,D}
8     C u0 p0 c0  {7,S} {10,S} {11,S} {12,S}
9  *2 C u0 p0 c0  {7,D} {13,S} {14,S}
10    H u0 p0 c0  {8,S}
11    H u0 p0 c0  {8,S}
12    H u0 p0 c0  {8,S}
13    H u0 p0 c0  {9,S}
14    H u0 p0 c0  {9,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {8,S} {9,S}
3  *3 C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5  *2 C u1 p0 c0  {1,S} {16,S} {17,S}
6     O u0 p2 c0  {2,S} {7,S}
7     O u0 p2 c0  {6,S} {18,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.91241, 'd12': 1.37073, 'd13': 2.319262},
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
    index = 49,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0  {1,S} {2,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1     C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {4,S} {8,S} {9,S} {10,S}
3  *1 C u0 p0 c0  {1,S} {4,D} {11,S}
4  *2 C u0 p0 c0  {2,S} {3,D} {12,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {8,S}
2  *1 C u0 p0 c0  {1,S} {5,S} {7,S} {9,S}
3     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
4     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
5     C u0 p0 c0  {2,S} {10,S} {11,S} {12,S}
6     C u0 p0 c0  {7,S} {19,S} {20,S} {21,S}
7  *2 C u1 p0 c0  {2,S} {6,S} {22,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {5,S}
11    H u0 p0 c0  {5,S}
12    H u0 p0 c0  {5,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.9951, 'd12': 1.378853, 'd13': 2.268596},
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
    index = 50,
    reactant1 = """
1     H u0 p0 c0  {2,S}
2     C u0 p0 c0  {1,S} {3,B} {4,B}
3     C u0 p0 c0  {2,B} {5,B} {6,S}
4     C u0 p0 c0  {2,B} {7,B} {8,S}
5     C u0 p0 c0  {3,B} {9,S} {10,B}
6     H u0 p0 c0  {3,S}
7     C u0 p0 c0  {4,B} {10,B} {11,S}
8     H u0 p0 c0  {4,S}
9  *1 C u0 p0 c0  {5,S} {12,D} {13,S}
10    C u0 p0 c0  {5,B} {7,B} {14,S}
11    H u0 p0 c0  {7,S}
12 *2 O u0 p2 c0  {9,D}
13    H u0 p0 c0  {9,S}
14    H u0 p0 c0  {10,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0 
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {8,S} {9,S} {10,S}
2     C u0 p0 c0  {1,S} {3,B} {4,B}
3     C u0 p0 c0  {2,B} {6,B} {11,S}
4     C u0 p0 c0  {2,B} {7,B} {12,S}
5     C u0 p0 c0  {6,B} {7,B} {13,S}
6     C u0 p0 c0  {3,B} {5,B} {14,S}
7     C u0 p0 c0  {4,B} {5,B} {15,S}
8  *2 O u1 p2 c0  {1,S}
9  *3 H u0 p0 c0  {1,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {4,S}
13    H u0 p0 c0  {5,S}
14    H u0 p0 c0  {6,S}
15    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.390271, 'd12': 1.232439, 'd13': 1.825219},
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
    index = 51,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {5,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0  {5,S} {14,S} {15,S} {16,S}
5  *3 C u1 p0 c0  {1,S} {3,S} {4,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
""",
    reactant2 = """
1     C u0 p0 c0  {3,S} {5,S} {6,S} {7,S}
2     C u0 p0 c0  {3,S} {8,S} {9,S} {10,S}
3  *2 C u0 p0 c0  {1,S} {2,S} {4,D}
4  *1 C u0 p0 c0  {3,D} {11,S} {12,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {4,S}
12    H u0 p0 c0  {4,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {10,S} {11,S}
3  *1 C u0 p0 c0  {1,S} {9,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {17,S} {18,S} {19,S}
5     C u0 p0 c0  {1,S} {20,S} {21,S} {22,S}
6     C u0 p0 c0  {2,S} {14,S} {15,S} {16,S}
7     C u0 p0 c0  {9,S} {23,S} {24,S} {25,S}
8     C u0 p0 c0  {9,S} {26,S} {27,S} {28,S}
9  *2 C u1 p0 c0  {3,S} {7,S} {8,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {2,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {6,S}
15    H u0 p0 c0  {6,S}
16    H u0 p0 c0  {6,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {4,S}
19    H u0 p0 c0  {4,S}
20    H u0 p0 c0  {5,S}
21    H u0 p0 c0  {5,S}
22    H u0 p0 c0  {5,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {7,S}
25    H u0 p0 c0  {7,S}
26    H u0 p0 c0  {8,S}
27    H u0 p0 c0  {8,S}
28    H u0 p0 c0  {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.098256, 'd12': 1.375812, 'd13': 2.252006},
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
    index = 52,
    reactant1 = """
multiplicity 2
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0  {1,S} {6,S} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {2,S}
7    H u0 p0 c0  {2,S}
""",
    reactant2 = """
1     C u0 p0 c0  {2,S} {3,S} {8,S} {9,S}
2     C u0 p0 c0  {1,S} {4,S} {10,S} {11,S}
3     C u0 p0 c0  {1,S} {5,S} {12,S} {13,S}
4     C u0 p0 c0  {2,S} {6,S} {14,S} {15,S}
5     C u0 p0 c0  {3,S} {16,S} {17,S} {18,S}
6  *2 C u0 p0 c0  {4,S} {7,D} {19,S}
7  *1 C u0 p0 c0  {6,D} {20,S} {21,S}
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
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {6,S}
20    H u0 p0 c0  {7,S}
21    H u0 p0 c0  {7,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {10,S} {11,S}
2     C u0 p0 c0  {1,S} {5,S} {12,S} {13,S}
3     C u0 p0 c0  {1,S} {7,S} {14,S} {15,S}
4  *3 C u0 p0 c0  {6,S} {8,S} {16,S} {17,S}
5     C u0 p0 c0  {2,S} {9,S} {18,S} {19,S}
6  *1 C u0 p0 c0  {4,S} {9,S} {20,S} {21,S}
7     C u0 p0 c0  {3,S} {22,S} {23,S} {24,S}
8     C u0 p0 c0  {4,S} {25,S} {26,S} {27,S}
9  *2 C u1 p0 c0  {5,S} {6,S} {28,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {4,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    H u0 p0 c0  {7,S}
23    H u0 p0 c0  {7,S}
24    H u0 p0 c0  {7,S}
25    H u0 p0 c0  {8,S}
26    H u0 p0 c0  {8,S}
27    H u0 p0 c0  {8,S}
28    H u0 p0 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 3.088237, 'd12': 1.365838, 'd13': 2.312608},
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
    index = 53,
    reactant1 = """
1     H u0 p0 c0  {2,S}
2     C u0 p0 c0  {1,S} {3,B} {4,B}
3     C u0 p0 c0  {2,B} {5,B} {6,S}
4     C u0 p0 c0  {2,B} {7,S} {8,B}
5     C u0 p0 c0  {3,B} {9,B} {10,S}
6     H u0 p0 c0  {3,S}
7     H u0 p0 c0  {4,S}
8     C u0 p0 c0  {4,B} {9,B} {11,S}
9     C u0 p0 c0  {5,B} {8,B} {12,S}
10 *1 C u0 p0 c0  {5,S} {13,D} {14,S}
11    H u0 p0 c0  {8,S}
12    C u0 p0 c0  {9,S} {13,S} {15,S} {16,S}
13 *2 C u0 p0 c0  {10,D} {12,S} {17,S}
14    H u0 p0 c0  {10,S}
15    H u0 p0 c0  {12,S}
16    H u0 p0 c0  {12,S}
17    H u0 p0 c0  {13,S}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {3,S} {4,S} {6,S} {11,S}
2     C u0 p0 c0  {5,S} {6,S} {12,S} {13,S}
3  *3 C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
4     C u0 p0 c0  {1,S} {5,B} {8,B}
5     C u0 p0 c0  {2,S} {4,B} {7,B}
6  *2 C u1 p0 c0  {1,S} {2,S} {17,S}
7     C u0 p0 c0  {5,B} {9,B} {18,S}
8     C u0 p0 c0  {4,B} {10,B} {19,S}
9     C u0 p0 c0  {7,B} {10,B} {20,S}
10    C u0 p0 c0  {8,B} {9,B} {21,S}
11    H u0 p0 c0  {1,S}
12    H u0 p0 c0  {2,S}
13    H u0 p0 c0  {2,S}
14    H u0 p0 c0  {3,S}
15    H u0 p0 c0  {3,S}
16    H u0 p0 c0  {3,S}
17    H u0 p0 c0  {6,S}
18    H u0 p0 c0  {7,S}
19    H u0 p0 c0  {8,S}
20    H u0 p0 c0  {9,S}
21    H u0 p0 c0  {10,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.992441, 'd12': 1.380921, 'd13': 2.288699},
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
    index = 54,
    reactant1 = """
1 *1 C u0 p0 c0  {2,D} {3,D}
2 *2 O u0 p2 c0  {1,D}
3    O u0 p2 c0  {1,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2    C u0 p0 c0  {3,D} {7,S} {8,S}
3 *3 C u1 p0 c0  {1,S} {2,D}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {2,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {5,S} {6,S} {7,S}
2  *3 C u0 p0 c0  {1,S} {3,S} {4,D}
3  *1 C u0 p0 c0  {2,S} {8,S} {9,D}
4     C u0 p0 c0  {2,D} {10,S} {11,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {1,S}
8  *2 O u1 p2 c0  {3,S}
9     O u0 p2 c0  {3,D}
10    H u0 p0 c0  {4,S}
11    H u0 p0 c0  {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.53821, 'd12': 1.2026, 'd13': 1.91836},
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
    index = 55,
    reactant1 = """
1    C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *1 C u0 p0 c0  {1,S} {3,D} {7,S}
3 *2 C u0 p0 c0  {2,D} {8,D}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    O u0 p2 c0  {3,D}
""",
    reactant2 = """
multiplicity 2
1 *3 C u1 p0 c0  {2,S} {3,S} {4,S}
2    H u0 p0 c0  {1,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3  *3 C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *2 C u1 p0 c0  {1,S} {12,D}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    O u0 p2 c0  {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 3.04755, 'd12': 1.35006, 'd13': 2.31921},
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
    index = 56,
    reactant1 = """
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *2 C u0 p0 c0  {1,S} {6,D} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *1 O u0 p2 c0  {2,D}
7    H u0 p0 c0  {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0 
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *2 C u1 p0 c0  {1,S} {3,S} {7,S}
3 *1 O u0 p2 c0  {2,S} {8,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8 *3 H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.43994, 'd12': 1.2402, 'd13': 1.56652},
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
    index = 57,
    reactant1 = """
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0  {1,S} {6,D} {7,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *2 O u0 p2 c0  {2,D}
7    H u0 p0 c0  {2,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0 
""",
    product1 = """
multiplicity 2
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *1 C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6 *2 O u1 p2 c0  {2,S}
7    H u0 p0 c0  {2,S}
8 *3 H u0 p0 c0  {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.38755, 'd12': 1.22869, 'd13': 1.87202},
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
    index = 58,
    reactant1 = """
1 *2 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *1 O u0 p2 c0  {1,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    reactant2 = """
multiplicity 2
1 *3 H u1 p0 c0 
""",
    product1 = """
multiplicity 2
1 *2 C u1 p0 c0  {2,S} {3,S} {4,S}
2 *1 O u0 p2 c0  {1,S} {5,S}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5 *3 H u0 p0 c0  {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.49332, 'd12': 1.23441, 'd13': 1.60353},
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
    index = 59,
    reactant1 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 C u0 p0 c0  {1,D} {5,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    O u0 p2 c0  {2,D}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 p0 c0  {1,S} {6,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    O u0 p2 c0  {2,D}
""",
    product1 = """
multiplicity 2
1  *1 C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *3 C u0 p0 c0  {1,S} {2,S} {10,D}
4  *2 C u1 p0 c0  {1,S} {11,D}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    O u0 p2 c0  {3,D}
11    O u0 p2 c0  {4,D}
""",
    distances = DistanceData(
        distances = {'d23': 2.91791, 'd12': 1.35838, 'd13': 2.14987},
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
    index = 60,
    reactant1 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 O u0 p2 c0  {1,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    reactant2 = """
multiplicity 2
1    C u0 p0 c0  {2,S} {3,D} {4,S}
2 *3 C u1 p0 c0  {1,S} {5,D}
3    O u0 p2 c0  {1,D}
4    H u0 p0 c0  {1,S}
5    O u0 p2 c0  {2,D}
""",
    product1 = """
multiplicity 2
1 *1 C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *3 C u0 p0 c0  {1,S} {3,S} {7,D}
3    C u0 p0 c0  {2,S} {8,D} {9,S}
4 *2 O u1 p2 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    O u0 p2 c0  {2,D}
8    O u0 p2 c0  {3,D}
9    H u0 p0 c0  {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.50122, 'd12': 1.25705, 'd13': 2.01672},
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
    index = 61,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {4,S} {5,S}
2     C u0 p0 c0  {1,S} {6,S} {7,S} {8,S}
3     C u0 p0 c0  {1,S} {9,S} {10,S} {11,S}
4  *3 C u1 p0 c0  {1,S} {12,D}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {2,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {3,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    O u0 p2 c0  {4,D}
""",
    reactant2 = """
1    C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *2 C u0 p0 c0  {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0  {2,D} {8,S} {9,S}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    H u0 p0 c0  {3,S}
9    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {6,S} {8,S}
2  *1 C u0 p0 c0  {6,S} {7,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0  {1,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0  {7,S} {17,S} {18,S} {19,S}
6  *3 C u0 p0 c0  {1,S} {2,S} {20,D}
7  *2 C u1 p0 c0  {2,S} {5,S} {21,S}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19    H u0 p0 c0  {5,S}
20    O u0 p2 c0  {6,D}
21    H u0 p0 c0  {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.92592, 'd12': 1.37116, 'd13': 2.22085},
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
    index = 62,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0  {1,S} {2,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
""",
    reactant2 = """
1     C u0 p0 c0  {2,S} {3,S} {4,S} {7,S}
2     C u0 p0 c0  {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
4  *1 C u0 p0 c0  {1,S} {5,S} {14,D}
5     O u0 p2 c0  {4,S} {6,S}
6     O u0 p2 c0  {5,S} {15,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14 *2 O u0 p2 c0  {4,D}
15    H u0 p0 c0  {6,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {3,S} {4,S} {5,S} {10,S}
2     C u0 p0 c0  {3,S} {6,S} {7,S} {11,S}
3  *1 C u0 p0 c0  {1,S} {2,S} {8,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {1,S} {16,S} {17,S} {18,S}
6     C u0 p0 c0  {2,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0  {2,S} {22,S} {23,S} {24,S}
8     O u0 p2 c0  {3,S} {9,S}
9     O u0 p2 c0  {8,S} {25,S}
10    H u0 p0 c0  {1,S}
11    H u0 p0 c0  {2,S}
12 *2 O u1 p2 c0  {3,S}
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
24    H u0 p0 c0  {7,S}
25    H u0 p0 c0  {9,S}
""",
    distances = DistanceData(
        distances = {'d23': 2.55429, 'd12': 1.26044, 'd13': 1.95909},
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
    index = 63,
    reactant1 = """
multiplicity 2
1     C u0 p0 c0  {2,S} {3,S} {5,S} {7,S}
2     C u0 p0 c0  {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0  {6,S} {14,S} {15,S} {16,S}
5     C u0 p0 c0  {1,S} {6,S} {17,D}
6  *3 C u1 p0 c0  {4,S} {5,S} {18,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    O u0 p2 c0  {5,D}
18    H u0 p0 c0  {6,S}
""",
    reactant2 = """
1 *1 C u0 p0 c0  {2,D} {3,S} {4,S}
2 *2 O u0 p2 c0  {1,D}
3    H u0 p0 c0  {1,S}
4    H u0 p0 c0  {1,S}
""",
    product1 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {7,S} {8,S}
2  *3 C u0 p0 c0  {5,S} {6,S} {7,S} {9,S}
3     C u0 p0 c0  {1,S} {10,S} {11,S} {12,S}
4     C u0 p0 c0  {1,S} {13,S} {14,S} {15,S}
5     C u0 p0 c0  {2,S} {16,S} {17,S} {18,S}
6  *1 C u0 p0 c0  {2,S} {19,S} {20,S} {21,S}
7     C u0 p0 c0  {1,S} {2,S} {22,D}
8     H u0 p0 c0  {1,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {4,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {5,S}
17    H u0 p0 c0  {5,S}
18    H u0 p0 c0  {5,S}
19 *2 O u1 p2 c0  {6,S}
20    H u0 p0 c0  {6,S}
21    H u0 p0 c0  {6,S}
22    O u0 p2 c0  {7,D}
""",
    distances = DistanceData(
        distances = {'d23': 2.61231, 'd12': 1.25737, 'd13': 2.04394},
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
    index = 64,
    reactant1 = """
1    C u0 p0 c0  {2,S} {4,S} {5,S} {6,S}
2 *2 C u0 p0 c0  {1,S} {3,D} {7,S}
3 *1 C u0 p0 c0  {2,D} {8,D}
4    H u0 p0 c0  {1,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
7    H u0 p0 c0  {2,S}
8    O u0 p2 c0  {3,D}
""",
    reactant2 = """
multiplicity 2
1     C u0 p0 c0  {3,S} {4,S} {5,S} {6,S}
2     C u0 p0 c0  {3,S} {7,S} {8,S} {9,S}
3  *3 C u1 p0 c0  {1,S} {2,S} {10,S}
4     H u0 p0 c0  {1,S}
5     H u0 p0 c0  {1,S}
6     H u0 p0 c0  {1,S}
7     H u0 p0 c0  {2,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {3,S}
""",
    product1 = """
multiplicity 2
1  *3 C u0 p0 c0  {2,S} {3,S} {5,S} {7,S}
2     C u0 p0 c0  {1,S} {8,S} {9,S} {10,S}
3     C u0 p0 c0  {1,S} {11,S} {12,S} {13,S}
4     C u0 p0 c0  {6,S} {14,S} {15,S} {16,S}
5  *1 C u0 p0 c0  {1,S} {6,S} {18,D}
6  *2 C u1 p0 c0  {4,S} {5,S} {17,S}
7     H u0 p0 c0  {1,S}
8     H u0 p0 c0  {2,S}
9     H u0 p0 c0  {2,S}
10    H u0 p0 c0  {2,S}
11    H u0 p0 c0  {3,S}
12    H u0 p0 c0  {3,S}
13    H u0 p0 c0  {3,S}
14    H u0 p0 c0  {4,S}
15    H u0 p0 c0  {4,S}
16    H u0 p0 c0  {4,S}
17    H u0 p0 c0  {6,S}
18    O u0 p2 c0  {5,D}
""",
    distances = DistanceData(
        distances = {'d23': 2.85131, 'd12': 1.33675, 'd13': 2.18368},
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

