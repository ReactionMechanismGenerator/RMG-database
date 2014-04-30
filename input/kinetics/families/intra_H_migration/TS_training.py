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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
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
    history = [
        ("Tue Apr 29 23:10:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""B3LYP/6-31+G(d,p) calculation in G09"""),
    ],
)

