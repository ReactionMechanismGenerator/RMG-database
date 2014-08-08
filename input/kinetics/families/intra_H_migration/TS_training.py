#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/TS_training"
shortDesc = u"Distances used to train group additivity values for TS geometries"
longDesc = u"""
Put interatomic distances for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

entry(
    index = 1,
    reactant1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *2 C 0 {2,S} {4,S} {5,S}
4 *1 C 1 {3,S}
5 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *1 C 1 {2,S} {4,S}
4 *2 C 0 {3,S} {5,S}
5 *3 H 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.49221', 'd13': '1.30285', 'd23': '1.30172'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1 *1 C 1 {2,S}
2 *2 C 0 {1,S} {3,S} {6,S} {7,S}
3    C 0 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    C 0 {4,S} {6,S}
6    C 0 {2,S} {5,S}
7 *3 H 0 {2,S}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {7,S}
2 *1 C 1 {1,S} {3,S} {6,S}
3    C 0 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    C 0 {4,S} {6,S}
6    C 0 {2,S} {5,S}
7 *3 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.48516', 'd13': '1.31517', 'd23': '1.29485'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1 *1 C 1 {2,S}
2 *4 C 0 {1,S} {3,S}
3 *2 C 0 {2,S} {4,S} {6,S}
4    C 0 {3,S} {5,S}
5    C 0 {4,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {6,S}
2 *4 C 0 {1,S} {3,S}
3 *1 C 1 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    C 0 {4,S}
6 *3 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.22164', 'd13': '1.41346', 'd23': '1.40190'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *1 C 1 {2,S} {4,S}
4 *4 O 0 {3,S} {5,S}
5 *2 O 0 {4,S} {6,S}
6 *3 H 0 {5,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *2 C 0 {2,S} {4,S} {6,S}
4 *4 O 0 {3,S} {5,S}
5 *1 O 1 {4,S}
6 *3 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.03811', 'd13': '1.33202', 'd23': '1.28316'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *2 C 0 {3,S} {5,S} {8,S}
5 *5 C 0 {4,S} {6,S}
6 *4 C 0 {5,S} {7,S}
7 *1 C 1 {6,S}
8 *3 H 0 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *1 C 1 {3,S} {5,S}
5 *4 C 0 {4,S} {6,S}
6 *5 C 0 {5,S} {7,S}
7 *2 C 0 {6,S} {8,S}
8 *3 H 0 {7,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.52790', 'd13': '1.39272', 'd23': '1.36152'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {6,S}
3 *5 C 0 {2,S} {4,S}
4 *4 C 0 {3,S} {5,S}
5 *1 O 1 {4,S}
6 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S} {3,S}
3 *4 C 0 {2,S} {4,S}
4 *5 C 0 {3,S} {5,S}
5 *2 O 0 {4,S} {6,S}
6 *3 H 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.36998', 'd13': '1.29626', 'd23': '1.27828'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S} {8,S}
3    C 0 {2,S}
4 *5 C 0 {2,S} {5,S}
5    C 0 {4,S} {6,S}
6 *4 C 0 {5,S} {7,S}
7 *1 O 1 {6,S}
8 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S} {3,S} {4,S}
3    C 0 {2,S}
4 *4 C 0 {2,S} {5,S}
5    C 0 {4,S} {6,S}
6 *5 C 0 {5,S} {7,S}
7 *2 O 0 {6,S} {8,S}
8 *3 H 0 {7,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.50266', 'd13': '1.31554', 'd23': '1.24586'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1 *2 C 0 {2,S} {9,S}
2 *5 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {8,S}
4 *4 C 0 {3,S} {5,S}
5 *1 C 1 {4,S} {6,S}
6    C 0 {5,S} {7,S}
7    C 0 {6,S} {8,S}
8    C 0 {3,S} {7,S}
9 *3 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 1 {2,S}
2 *4 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {8,S}
4 *5 C 0 {3,S} {5,S}
5 *2 C 0 {4,S} {6,S} {9,S}
6    C 0 {5,S} {7,S}
7    C 0 {6,S} {8,S}
8    C 0 {3,S} {7,S}
9 *3 H 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.64783', 'd13': '1.38878', 'd23': '1.33168'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S} {3,S} {4,S}
3    C 0 {2,S}
4 *4 C 0 {2,S} {5,S}
5    C 0 {4,S} {6,S}
6    C 0 {5,S} {7,S}
7 *5 O 0 {6,S} {8,S}
8 *2 O 0 {7,S} {9,S}
9 *3 H 0 {8,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,S} {9,S}
3    C 0 {2,S}
4 *5 C 0 {2,S} {5,S}
5    C 0 {4,S} {6,S}
6    C 0 {5,S} {7,S}
7 *4 O 0 {6,S} {8,S}
8 *1 O 1 {7,S}
9 *3 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.51644', 'd13': '1.34348', 'd23': '1.19533'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1 *2 C 0 {2,S} {9,S}
2 *5 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {8,S}
4    C 0 {3,S} {5,S}
5 *4 C 0 {4,S} {6,S}
6 *1 C 1 {5,S} {7,S}
7    C 0 {6,S} {8,S}
8    C 0 {3,S} {7,S}
9 *3 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 1 {2,S}
2 *4 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {8,S}
4    C 0 {3,S} {5,S}
5 *5 C 0 {4,S} {6,S}
6 *2 C 0 {5,S} {7,S} {9,S}
7    C 0 {6,S} {8,S}
8    C 0 {3,S} {7,S}
9 *3 H 0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.65192', 'd13': '1.32587', 'd23': '1.37209'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1 *1 C 1 {2,S}
2 *4 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    C 0 {4,S} {6,S}
6 *5 C 0 {5,S} {7,S}
7 *2 O 0 {6,S} {8,S}
8 *3 H 0 {7,S}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {8,S}
2 *5 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    C 0 {4,S} {6,S}
6 *4 C 0 {5,S} {7,S}
7 *1 O 1 {6,S}
8 *3 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.50531', 'd13': '1.27498', 'd23': '1.24532'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1 *1 C 1 {2,S}
2 *4 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    C 0 {4,S} {6,S}
6 *5 O 0 {5,S} {7,S}
7 *2 O 0 {6,S} {8,S}
8 *3 H 0 {7,S}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {8,S}
2 *5 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4    C 0 {3,S} {5,S}
5    C 0 {4,S} {6,S}
6 *4 O 0 {5,S} {7,S}
7 *1 O 1 {6,S}
8 *3 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '2.53680', 'd13': '1.40019', 'd23': '1.14855'},
        method = 'B3LYP/6-31+G(d,p)',
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
    reactant1 = 
"""
1    H 0 0 {3,S}
2    H 0 0 {3,S}
3 *2 C 0 0 {1,S} {2,S} {4,S} {5,S}
4 *3 H 0 0 {3,S}
5 *1 O 1 2 {3,S}
""",
    product1 = 
"""
1 *1 C 1 0 {2,S} {4,S} {5,S}
2 *2 O 0 2 {1,S} {3,S}
3 *3 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.38927, 'd13': 1.203442, 'd23': 1.276283},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    reactant1 = 
"""
1     C 0 0 {3,S} {4,S} {5,S} {8,S}
2     H 0 0 {8,S}
3     H 0 0 {1,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {10,S}
7     H 0 0 {10,S}
8  *2 C 0 0 {1,S} {2,S} {9,S} {10,S}
9  *3 H 0 0 {8,S}
10 *1 C 1 0 {6,S} {7,S} {8,S}
""",
    product1 = 
"""
1  *1 C 1 0 {2,S} {3,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *2 C 0 0 {1,S} {4,S} {9,S} {10,S}
4  *3 H 0 0 {3,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.492365, 'd13': 1.30311, 'd23': 1.30064},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    reactant1 = 
"""
1     C 0 0 {2,S} {3,S} {4,S} {11,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     H 0 0 {1,S}
4     H 0 0 {1,S}
5     H 0 0 {11,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {13,S}
10    H 0 0 {13,S}
11 *2 C 0 0 {1,S} {5,S} {12,S} {13,S}
12 *3 H 0 0 {11,S}
13 *1 C 1 0 {9,S} {10,S} {11,S}
""",
    product1 = 
"""
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 1 0 {1,S} {4,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 C 0 0 {2,S} {5,S} {12,S} {13,S}
5  *3 H 0 0 {4,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.492204, 'd13': 1.302794, 'd23': 1.301687},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    reactant1 = 
"""
1     C 0 0 {2,D} {6,S} {9,S}
2     C 0 0 {1,D} {7,S} {8,S}
3     H 0 0 {11,S}
4     H 0 0 {11,S}
5     H 0 0 {9,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 C 0 0 {1,S} {5,S} {10,S} {11,S}
10 *3 H 0 0 {9,S}
11 *1 C 1 0 {3,S} {4,S} {9,S}
""",
    product1 = 
"""
1  *2 C 0 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 1 0 {1,S} {4,S} {8,S}
3  *3 H 0 0 {1,S}
4     C 0 0 {2,S} {5,D} {9,S}
5     C 0 0 {4,D} {10,S} {11,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
11    H 0 0 {5,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.489543, 'd13': 1.365329, 'd23': 1.256171},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    reactant1 = 
"""
1     C 0 0 {3,S} {4,S} {5,S} {11,S}
2     C 0 0 {6,S} {7,S} {8,S} {11,S}
3     H 0 0 {1,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {13,S}
10    H 0 0 {13,S}
11 *2 C 0 0 {1,S} {2,S} {12,S} {13,S}
12 *3 H 0 0 {11,S}
13 *1 C 1 0 {9,S} {10,S} {11,S}
""",
    product1 = 
"""
1  *1 C 1 0 {2,S} {3,S} {4,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 C 0 0 {1,S} {5,S} {12,S} {13,S}
5  *3 H 0 0 {4,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.493897, 'd13': 1.308689, 'd23': 1.302738},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    reactant1 = 
"""
1     C 0 0 {2,S} {4,S} {5,S} {14,S}
2     C 0 0 {1,S} {3,S} {6,S} {7,S}
3     C 0 0 {2,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {14,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {16,S}
13    H 0 0 {16,S}
14 *2 C 0 0 {1,S} {8,S} {15,S} {16,S}
15 *3 H 0 0 {14,S}
16 *1 C 1 0 {12,S} {13,S} {14,S}
""",
    product1 = 
"""
1     C 0 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 0 {1,S} {4,S} {9,S} {10,S}
3  *1 C 1 0 {1,S} {5,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *2 C 0 0 {3,S} {6,S} {15,S} {16,S}
6  *3 H 0 0 {5,S}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.49488, 'd13': 1.303078, 'd23': 1.297544},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    reactant1 = 
"""
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {13,S}
3     C 0 0 {1,S} {4,S} {9,S} {10,S}
4     O 0 2 {3,S} {12,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {13,S}
12    H 0 0 {4,S}
13 *2 C 0 0 {2,S} {11,S} {14,S} {15,S}
14 *3 H 0 0 {13,S}
15 *1 O 1 2 {13,S}
""",
    product1 = 
"""
1     C 0 0 {2,S} {3,S} {8,S} {9,S}
2     C 0 0 {1,S} {4,S} {10,S} {11,S}
3     C 0 0 {1,S} {5,S} {12,S} {13,S}
4  *1 C 1 0 {2,S} {6,S} {14,S}
5     O 0 2 {3,S} {15,S}
6  *2 O 0 2 {4,S} {7,S}
7  *3 H 0 0 {6,S}
8     H 0 0 {1,S}
9     H 0 0 {1,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.39608, 'd13': 1.208513, 'd23': 1.27819},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    reactant1 = 
"""
1     C 0 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 0 {1,S} {4,S} {9,S} {10,S}
3     C 0 0 {1,S} {5,S} {11,S} {12,S}
4     C 0 0 {2,S} {13,S} {14,S} {25,S}
5     C 0 0 {3,S} {16,S} {17,S} {18,S}
6     C 0 0 {19,S} {20,S} {21,S} {23,S}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {23,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
18    H 0 0 {5,S}
19    H 0 0 {6,S}
20    H 0 0 {6,S}
21    H 0 0 {6,S}
22    H 0 0 {25,S}
23 *2 C 0 0 {6,S} {15,S} {24,S} {25,S}
24 *3 H 0 0 {23,S}
25 *1 C 1 0 {4,S} {22,S} {23,S}
""",
    product1 = 
"""
1     C 0 0 {2,S} {3,S} {10,S} {11,S}
2     C 0 0 {1,S} {4,S} {12,S} {13,S}
3     C 0 0 {1,S} {6,S} {14,S} {15,S}
4     C 0 0 {2,S} {8,S} {16,S} {17,S}
5  *1 C 1 0 {7,S} {8,S} {18,S}
6     C 0 0 {3,S} {19,S} {20,S} {21,S}
7     C 0 0 {5,S} {22,S} {23,S} {24,S}
8  *2 C 0 0 {4,S} {5,S} {9,S} {25,S}
9  *3 H 0 0 {8,S}
10    H 0 0 {1,S}
11    H 0 0 {1,S}
12    H 0 0 {2,S}
13    H 0 0 {2,S}
14    H 0 0 {3,S}
15    H 0 0 {3,S}
16    H 0 0 {4,S}
17    H 0 0 {4,S}
18    H 0 0 {5,S}
19    H 0 0 {6,S}
20    H 0 0 {6,S}
21    H 0 0 {6,S}
22    H 0 0 {7,S}
23    H 0 0 {7,S}
24    H 0 0 {7,S}
25    H 0 0 {8,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 1.495163, 'd13': 1.305369, 'd23': 1.305005},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    reactant1 = 
"""
1     C 0 0 {2,B} {5,S} {13,B}
2     C 0 0 {1,B} {3,B} {6,S}
3     C 0 0 {2,B} {4,B} {8,S}
4     C 0 0 {3,B} {9,S} {15,B}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {14,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {11,S}
11 *2 C 0 0 {10,S} {12,S} {14,D}
12 *3 H 0 0 {11,S}
13 *4 C 0 0 {1,B} {14,S} {15,B}
14 *5 C 0 0 {7,S} {11,D} {13,S}
15 *1 C 1 0 {4,B} {13,B}
""",
    product1 = 
"""
1  *4 C 0 0 {2,B} {4,S} {8,B}
2     C 0 0 {1,B} {3,B} {10,S}
3     C 0 0 {2,B} {5,B} {11,S}
4  *5 C 0 0 {1,S} {7,D} {12,S}
5     C 0 0 {3,B} {6,B} {13,S}
6     C 0 0 {5,B} {8,B} {14,S}
7  *1 C 1 0 {4,D} {15,S}
8  *2 C 0 0 {1,B} {6,B} {9,S}
9  *3 H 0 0 {8,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {6,S}
15    H 0 0 {7,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': 2.451028, 'd13': 1.385279, 'd23': 1.387024},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""

""",
)

