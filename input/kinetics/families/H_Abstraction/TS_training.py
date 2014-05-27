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
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
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
    history = [
        ('Thu Oct  3 16:15:59 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 2,
    reactant1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
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
    history = [
        ('Fri Oct  4 13:03:20 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 3,
    reactant1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
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
    history = [
        ('Thu Oct  3 19:11:41 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 4,
    reactant1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,D} {3,S}
2    O 0 2 {1,D}
3    H 0 0 {1,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,D} {4,S}
2 *2 H 0 0 {1,S}
3    O 0 2 {1,D}
4    H 0 0 {1,S}
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
    history = [
        ('Thu Oct  3 21:06:25 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 5,
    reactant1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    C 0 0 {2,D} {4,S} {5,S}
2 *1 C 0 0 {1,D} {3,S} {6,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
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
    history = [
        ('Fri Oct  4 14:36:06 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 6,
    reactant1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    O 0 2 {2,S} {4,S}
2 *1 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
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
    history = [
        ('Thu Oct  3 23:15:02 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 7,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
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
    history = [
        ('Sat Oct  5 07:17:14 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 8,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,D} {4,S}
2 *3 C 1 0 {1,S} {5,S} {6,S}
3    C 0 0 {1,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
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
    history = [
        ('Sat Oct  5 21:39:01 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 9,
    reactant1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *3 O 1 2 {2,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    O 0 2 {1,S} {3,S}
3 *1 O 0 2 {2,S} {7,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {3,S}
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
    history = [
        ('Sun Oct  6 05:11:10 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 10,
    reactant1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    O 0 2 {2,D}
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
    history = [
        ('Sun Oct  6 06:31:12 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 11,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3 *1 C 0 0 {2,D} {8,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8 *2 H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3 *3 C 1 0 {2,D} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
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
    history = [
        ('Sun Oct  6 08:26:17 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 12,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 0 {3,D} {7,S} {8,S}
3 *3 C 1 0 {1,S} {2,D}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
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
    history = [
        ('Sun Oct  6 10:45:23 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 13,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
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
    history = [
        ('Mon Oct  7 07:11:14 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 14,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,D} {5,S}
2     C 0 0 {1,S} {4,D} {6,S}
3  *1 C 0 0 {1,D} {7,S} {8,S}
4     C 0 0 {2,D} {9,S} {10,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7  *2 H 0 0 {3,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {4,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,D} {5,S}
2    C 0 0 {1,S} {4,D} {6,S}
3    C 0 0 {1,D} {7,S} {8,S}
4 *3 C 1 0 {2,D} {9,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
9    H 0 0 {4,S}
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
    history = [
        ('Mon Oct  7 12:18:12 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 15,
    reactant1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 0 {1,S} {3,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 0 0 {1,S} {4,S} {5,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {2,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
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
    history = [
        ('Tue Oct  8 10:23:39 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 16,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     O 0 2 {2,S} {12,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     O 0 2 {2,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
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
    history = [
        ('Thu Oct 10 22:36:03 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 17,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1 *1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,D} {8,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    O 0 2 {2,D}
8    H 0 0 {2,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {4,D} {7,S}
3    O 0 2 {1,S} {2,S}
4    O 0 2 {2,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
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
    history = [
        ('Fri Oct 11 00:52:04 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 18,
    reactant1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {4,D} {11,S}
4  *3 C 1 0 {2,S} {3,D}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {4,D} {12,S}
4  *1 C 0 0 {2,S} {3,D} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11 *2 H 0 0 {4,S}
12    H 0 0 {3,S}
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
    history = [
        ('Fri Oct 11 07:52:33 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 19,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4  *1 C 0 0 {2,S} {12,S} {13,S} {14,S}
5     O 0 2 {3,S} {15,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12 *2 H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     O 0 2 {3,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
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
    history = [
        ('Fri Oct 11 22:27:35 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 20,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     O 0 2 {1,S} {15,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     O 0 2 {1,S} {14,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
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
    history = [
        ('Sat Oct 12 13:28:20 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 21,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {1,S} {13,S} {14,S} {15,S}
5  *1 C 0 0 {2,S} {9,S} {16,S} {17,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {5,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 C 1 0 {2,S} {15,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
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
    history = [
        ('Sun Oct 13 02:56:15 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 22,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {6,S}
2  *1 C 0 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {2,S} {15,S} {16,S} {17,S}
6     H 0 0 {1,S}
7  *2 H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {5,S} {13,S} {14,S} {15,S}
5  *3 C 1 0 {1,S} {4,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
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
    history = [
        ('Sun Oct 13 18:16:24 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 23,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {7,S} {8,S}
2  *1 C 0 0 {1,S} {4,S} {6,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     C 0 0 {3,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {5,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {5,S} {13,S} {14,S} {15,S}
5  *3 C 1 0 {2,S} {4,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
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
    history = [
        ('Mon Oct 14 20:11:44 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 24,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {1,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 C 1 0 {1,S} {15,S} {16,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
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
    history = [
        ('Wed Oct 23 23:13:03 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 25,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 0 {1,S} {5,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {2,S} {15,S} {16,S} {17,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *3 C 1 0 {1,S} {15,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
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
    history = [
        ('Thu Oct 24 19:10:33 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 26,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1  *1 C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {4,B} {8,S}
3     C 0 0 {1,B} {5,B} {9,S}
4     C 0 0 {2,B} {6,B} {10,S}
5     C 0 0 {3,B} {6,B} {11,S}
6     C 0 0 {4,B} {5,B} {12,S}
7  *2 H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
12    H 0 0 {6,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {4,B} {8,S}
3     C 0 0 {1,B} {5,B} {9,S}
4     C 0 0 {2,B} {6,B} {10,S}
5     C 0 0 {3,B} {6,B} {11,S}
6  *3 C 1 0 {4,B} {5,B}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
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
    history = [
        ('Fri Oct 25 07:16:46 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 27,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {5,B} {8,S}
3     C 0 0 {1,B} {6,B} {9,S}
4     C 0 0 {5,B} {6,B} {10,S}
5     C 0 0 {2,B} {4,B} {11,S}
6     C 0 0 {3,B} {4,B} {12,S}
7  *1 O 0 2 {1,S} {13,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
12    H 0 0 {6,S}
13 *2 H 0 0 {7,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {5,B} {8,S}
3     C 0 0 {1,B} {6,B} {9,S}
4     C 0 0 {5,B} {6,B} {10,S}
5     C 0 0 {2,B} {4,B} {11,S}
6     C 0 0 {3,B} {4,B} {12,S}
7  *3 O 1 2 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
12    H 0 0 {6,S}
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
    history = [
        ('Fri Oct 25 21:17:19 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 28,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {9,S} {10,S}
2  *1 C 0 0 {1,S} {11,S} {12,S} {13,S}
3     C 0 0 {1,S} {4,B} {5,B}
4     C 0 0 {3,B} {7,B} {14,S}
5     C 0 0 {3,B} {8,B} {15,S}
6     C 0 0 {7,B} {8,B} {16,S}
7     C 0 0 {4,B} {6,B} {17,S}
8     C 0 0 {5,B} {6,B} {18,S}
9     H 0 0 {1,S}
10    H 0 0 {1,S}
11 *2 H 0 0 {2,S}
12    H 0 0 {2,S}
13    H 0 0 {2,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {6,S}
17    H 0 0 {7,S}
18    H 0 0 {8,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {8,S} {9,S} {10,S}
2     C 0 0 {1,S} {3,B} {4,B}
3     C 0 0 {2,B} {6,B} {11,S}
4     C 0 0 {2,B} {7,B} {12,S}
5     C 0 0 {6,B} {7,B} {13,S}
6     C 0 0 {3,B} {5,B} {14,S}
7     C 0 0 {4,B} {5,B} {15,S}
8  *3 C 1 0 {1,S} {16,S} {17,S}
9     H 0 0 {1,S}
10    H 0 0 {1,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {6,S}
15    H 0 0 {7,S}
16    H 0 0 {8,S}
17    H 0 0 {8,S}
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
    history = [
        ('Sun Oct 27 06:17:26 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 29,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    O 0 2 {1,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 30,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,S} {7,S}
3    O 0 2 {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 31,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *1 O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9 *2 H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *3 O 1 2 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 32,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {4,S}
2 *1 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    O 0 2 {1,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 33,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {4,S}
2 *1 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,S} {7,S}
3    O 0 2 {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 34,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *1 O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9 *2 H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {4,S}
2 *1 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *3 O 1 2 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 35,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 36,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1    O 0 2 {2,S} {4,S}
2 *3 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 37,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,D} {4,S} {5,S}
2 *1 C 0 0 {1,D} {3,S} {6,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 38,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {4,S} {6,S} {7,S}
2     C 0 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 0 {2,S} {4,S} {10,S} {11,S}
4  *1 C 0 0 {1,S} {3,S} {5,S} {12,S}
5  *2 H 0 0 {4,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {4,S} {9,S} {10,S}
4  *3 C 1 0 {2,S} {3,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 39,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {3,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    O 0 2 {1,S} {3,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 40,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {3,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    O 0 2 {1,S} {3,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 41,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {3,S} {6,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 42,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    C 0 0 {1,S} {2,S} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3 *3 C 1 0 {1,S} {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 43,
    reactant1 = """
1 *3 O 1 2 {2,S}
2    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    O 0 2 {1,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 44,
    reactant1 = """
1 *3 O 1 2 {2,S}
2    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *1 O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9 *2 H 0 0 {3,S}
""",
    product1 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *3 O 1 2 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 45,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1 *3 O 1 2 {2,S}
2    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.808251, 'd12': 1.407349, 'd13': 2.196944},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:30:51 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 46,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    O 0 2 {1,S} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    reactant2 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    product2 = """
1 *3 H 1 0
""",
    distances = DistanceData(
        distances = {'d23': 1.296176, 'd12': 1.002833, 'd13': 2.29898},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:37:06 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 47,
    reactant1 = """
1 *1 O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product1 = """
1    H 0 0 {2,S}
2 *3 O 1 2 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.216325, 'd12': 1.324475, 'd13': 2.537847},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:37:28 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 48,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *1 O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9 *2 H 0 0 {3,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *3 O 1 2 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.91111, 'd12': 1.201, 'd13': 2.10677},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:47:00 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 49,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,S} {7,S}
3    O 0 2 {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.060399, 'd12': 1.250952, 'd13': 2.311305},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:47:09 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 50,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    O 0 2 {1,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.926377, 'd12': 1.366101, 'd13': 2.29247},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:47:18 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 51,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *3 O 1 2 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.19983, 'd12': 1.310536, 'd13': 2.509181},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:58:37 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 52,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,D}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,D} {4,S}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
4 *2 H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.274424, 'd12': 1.486471, 'd13': 2.760463},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:46:21 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 53,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.126056, 'd12': 1.425793, 'd13': 2.55168},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:48:35 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 54,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    C 0 0 {1,S} {2,S} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3 *3 C 1 0 {1,S} {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.877258, 'd12': 1.430155, 'd13': 2.306828},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:01:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 55,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {3,S} {6,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.927201, 'd12': 1.366575, 'd13': 2.293246},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:57:37 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 56,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1 *1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {3,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {3,S} {7,S} {8,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.008692, 'd12': 1.297897, 'd13': 2.306541},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:03:08 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 57,
    reactant1 = """
1 *1 O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    product1 = """
1    H 0 0 {2,S}
2 *3 O 1 2 {1,S}
""",
    product2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *1 C 0 0 {1,D} {5,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6 *2 H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.235607, 'd12': 1.272333, 'd13': 2.495812},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:08:49 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 58,
    reactant1 = """
1 *1 O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    product1 = """
1    H 0 0 {2,S}
2 *3 O 1 2 {1,S}
""",
    product2 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.002539, 'd12': 1.591884, 'd13': 2.498974},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:07:51 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 59,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1 *3 O 1 2 {2,S}
2    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.162672, 'd12': 1.477049, 'd13': 2.638169},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:26:01 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 60,
    reactant1 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,D} {3,S} {4,S}
2    C 0 0 {1,D} {5,S} {6,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    O 0 2 {1,S} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.464952, 'd12': 1.262583, 'd13': 2.727535},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:34:53 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 61,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     O 0 2 {1,S} {12,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3  *3 C 1 0 {1,S} {2,S} {4,S}
4     O 0 2 {3,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.176607, 'd12': 1.193929, 'd13': 2.370363},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:52:18 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 62,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1  *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {5,D}
4  *2 H 0 0 {1,S}
5     O 0 2 {3,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 0 {1,S} {2,S} {4,D}
4    O 0 2 {3,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.012158, 'd12': 1.268907, 'd13': 2.279237},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:41:26 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 63,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *3 O 1 2 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.246208, 'd12': 1.275568, 'd13': 2.521678},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:02:57 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 64,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2  *1 C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {2,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *3 C 1 0 {1,S} {6,S} {7,S}
3     C 0 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.380732, 'd12': 1.32602, 'd13': 2.706495},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:29:49 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 65,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    C 0 0 {1,S} {3,S} {5,S} {6,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.363688, 'd12': 1.332471, 'd13': 2.695568},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:18:45 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 66,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,D} {6,S}
3    C 0 0 {2,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.470831, 'd12': 1.26608, 'd13': 2.736083},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:31:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 67,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {3,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {3,S} {7,S} {8,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.430905, 'd12': 1.302739, 'd13': 2.733224},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:40:03 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 68,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    reactant2 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7  *2 H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1 *3 H 1 0
""",
    distances = DistanceData(
        distances = {'d23': 1.371495, 'd12': 0.926853, 'd13': 2.298343},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 07:03:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 69,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,D} {3,S}
2    O 0 2 {1,D}
3    H 0 0 {1,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,D} {3,S} {4,S}
2    O 0 2 {1,D}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.317309, 'd12': 1.223801, 'd13': 2.535817},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:39:05 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 70,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {5,D}
4  *2 H 0 0 {1,S}
5     O 0 2 {3,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 0 {1,S} {2,S} {4,D}
4    O 0 2 {3,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.429246, 'd12': 1.284618, 'd13': 2.712247},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 07:59:34 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 71,
    reactant1 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33542, 'd12': 1.380621, 'd13': 2.716025},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:45:14 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 72,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *3 O 1 2 {2,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    O 0 2 {1,S} {3,S}
3 *1 O 0 2 {2,S} {7,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {3,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.149865, 'd12': 1.40219, 'd13': 2.551133},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 07:56:41 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 73,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.355809, 'd12': 1.356755, 'd13': 2.71208},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:35:43 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 74,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *3 O 1 2 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.289857, 'd12': 1.24964, 'd13': 2.539487},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:30:25 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 75,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *3 O 1 2 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.248587, 'd12': 1.276309, 'd13': 2.524895},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:28:00 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 76,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,D}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,D} {4,S}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
4 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.329108, 'd12': 1.421184, 'd13': 2.749792},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:39:14 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 77,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,D}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,D}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    O 0 2 {1,D}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.306486, 'd12': 1.449892, 'd13': 2.754254},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 09:03:31 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 78,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.185967, 'd12': 1.355088, 'd13': 2.540637},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:53:42 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 79,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.377889, 'd12': 1.328058, 'd13': 2.705697},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 10:13:30 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 80,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {2,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 0 {5,S} {11,S} {12,S} {13,S}
4     C 0 0 {5,S} {14,S} {15,S} {16,S}
5  *3 C 1 0 {1,S} {3,S} {4,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.065669, 'd12': 1.235549, 'd13': 2.301216},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 10:38:39 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 81,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 0 {1,S} {3,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.409141, 'd12': 1.307025, 'd13': 2.715605},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 10:36:33 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 82,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.381915, 'd12': 1.325846, 'd13': 2.707452},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 10:47:57 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 83,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,D} {6,S}
2     C 0 0 {1,S} {4,D} {7,S}
3  *1 C 0 0 {1,D} {5,S} {8,S}
4     C 0 0 {2,D} {9,S} {10,S}
5  *2 H 0 0 {3,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,D} {5,S}
2    C 0 0 {1,S} {4,D} {6,S}
3 *3 C 1 0 {1,D} {7,S}
4    C 0 0 {2,D} {8,S} {9,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {4,S}
9    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.299711, 'd12': 1.382945, 'd13': 2.682409},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 11:04:48 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 84,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4  *1 C 0 0 {2,S} {12,S} {13,S} {14,S}
5     C 0 0 {3,S} {15,S} {16,S} {17,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12 *2 H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *3 C 1 0 {3,S} {15,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.930376, 'd12': 1.362744, 'd13': 2.292827},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 11:42:17 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 85,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     C 0 0 {3,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {5,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {2,S} {13,S} {14,S} {15,S}
5  *3 C 1 0 {1,S} {2,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.968067, 'd12': 1.319334, 'd13': 2.286248},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 11:52:49 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 86,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,D} {4,S}
2 *3 C 1 0 {1,S} {5,S} {6,S}
3    C 0 0 {1,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4443, 'd12': 1.287947, 'd13': 2.732236},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 11:43:44 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 87,
    reactant1 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,D} {3,S} {4,S}
2    C 0 0 {1,D} {5,S} {6,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,D} {6,S}
3    C 0 0 {2,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.513197, 'd12': 1.235324, 'd13': 2.74749},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:00:22 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 88,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {4,D}
4     C 0 0 {3,D} {11,S} {12,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 0 {1,S} {3,S} {4,D}
3  *3 C 1 0 {2,S} {8,S} {9,S}
4     C 0 0 {2,D} {10,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.463225, 'd12': 1.272173, 'd13': 2.734469},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:24:08 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 89,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,S} {12,S} {13,S}
5     C 0 0 {3,S} {4,S} {14,S} {15,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
""",
    product1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    product2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {5,S} {9,S} {10,S}
4     C 0 0 {2,S} {5,S} {11,S} {12,S}
5     C 0 0 {3,S} {4,S} {13,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.994169, 'd12': 1.282451, 'd13': 2.276393},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:21:13 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 90,
    reactant1 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    O 1 2 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2    C 0 0 {1,D} {5,S} {6,S}
3 *3 C 1 0 {1,S} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.48516, 'd12': 1.131035, 'd13': 2.614105},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:05:12 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 91,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11 *2 H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38475, 'd12': 1.160095, 'd13': 2.544667},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:48:34 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 92,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,D}
3    O 0 2 {2,D}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,D} {7,S}
3    O 0 2 {2,D}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32645, 'd12': 1.222161, 'd13': 2.548529},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:11:32 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 93,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {1,S} {4,D} {10,S}
4     C 0 0 {3,D} {11,S} {12,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 0 {1,S} {3,S} {8,S}
3     C 0 0 {2,S} {4,D} {9,S}
4     C 0 0 {3,D} {10,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.493337, 'd12': 1.255489, 'd13': 2.74766},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 13:08:58 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 94,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2    C 0 0 {3,S} {5,D} {8,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    O 0 2 {2,D}
6    H 0 0 {1,S}
7    H 0 0 {1,S}
8    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {4,D} {7,S}
3    O 0 2 {1,S} {2,S}
4    O 0 2 {2,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.380239, 'd12': 1.321635, 'd13': 2.701664},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:58:11 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 95,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {5,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {2,S} {13,S} {14,S} {15,S}
5     O 0 2 {1,S} {2,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1  *3 C 1 0 {3,S} {5,S} {6,S}
2     C 0 0 {4,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     O 0 2 {1,S} {2,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.455335, 'd12': 1.287741, 'd13': 2.74237},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 14:38:08 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 96,
    reactant1 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    reactant2 = """
1  *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {5,D}
4  *2 H 0 0 {1,S}
5     O 0 2 {3,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,D} {3,S} {4,S}
2    C 0 0 {1,D} {5,S} {6,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
""",
    product2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 0 {1,S} {2,S} {4,D}
4    O 0 2 {3,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.464653, 'd12': 1.254446, 'd13': 2.717863},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 13:50:22 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 97,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11 *2 H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.353827, 'd12': 1.354599, 'd13': 2.708409},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 14:50:38 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 98,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    O 0 2 {2,D}
""",
    product2 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.331478, 'd12': 1.4283, 'd13': 2.756683},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 14:52:03 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 99,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,D} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.309076, 'd12': 1.457569, 'd13': 2.765122},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 14:51:10 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 100,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.352875, 'd12': 1.359062, 'd13': 2.711432},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:00:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 101,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.330919, 'd12': 1.229832, 'd13': 2.560671},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:05:43 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 102,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *3 O 1 2 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.246807, 'd12': 1.280576, 'd13': 2.526767},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:38:53 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 103,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,D}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,D} {4,S}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
4 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.30392, 'd12': 1.45327, 'd13': 2.755748},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:41:09 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 104,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.210177, 'd12': 1.332136, 'd13': 2.542273},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:37:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 105,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 0 {1,S} {3,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.188088, 'd12': 1.355607, 'd13': 2.543226},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 18:10:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 106,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {3,D} {7,S}
3     C 0 0 {2,D} {8,S} {9,S}
4     O 0 2 {1,S} {10,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,D} {5,S}
2 *3 C 1 0 {1,S} {4,S} {6,S}
3    C 0 0 {1,D} {7,S} {8,S}
4    O 0 2 {2,S} {9,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
9    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.483497, 'd12': 1.271122, 'd13': 2.75044},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 18:13:29 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 107,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,S} {12,S} {13,S}
5     C 0 0 {3,S} {4,S} {14,S} {15,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {5,S} {9,S} {10,S}
4     C 0 0 {2,S} {5,S} {11,S} {12,S}
5     C 0 0 {3,S} {4,S} {13,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.418941, 'd12': 1.291399, 'd13': 2.710328},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 20:18:23 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 108,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {1,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *3 C 1 0 {1,S} {6,S} {7,S}
3     C 0 0 {1,S} {8,S} {9,S} {10,S}
4     C 0 0 {1,S} {11,S} {12,S} {13,S}
5     C 0 0 {1,S} {14,S} {15,S} {16,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.376535, 'd12': 1.333048, 'd13': 2.708112},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 21:20:31 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 109,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2  *1 C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {4,S} {11,D}
4     O 0 2 {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8  *2 H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    O 0 2 {3,D}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,D}
3  *3 C 1 0 {4,S} {9,S} {10,S}
4     O 0 2 {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     O 0 2 {2,D}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.38536, 'd12': 1.318788, 'd13': 2.703903},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 20:36:48 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 110,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {4,S} {11,D}
4     O 0 2 {2,S} {3,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    O 0 2 {3,D}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {3,S} {4,S} {8,D}
3  *3 C 1 0 {2,S} {9,S} {10,S}
4     O 0 2 {1,S} {2,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     O 0 2 {2,D}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.403984, 'd12': 1.298579, 'd13': 2.702172},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 20:33:32 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 111,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,D} {10,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     O 0 2 {3,D}
10    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,S} {7,S}
3    C 0 0 {2,S} {8,D} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    O 0 2 {3,D}
9    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.453078, 'd12': 1.280278, 'd13': 2.731984},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 21:48:00 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 112,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,D} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     O 0 2 {3,D}
10    H 0 0 {3,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {7,S} {8,S}
3    C 0 0 {1,S} {6,D} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {3,D}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.343187, 'd12': 1.364407, 'd13': 2.707408},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 21:42:44 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 113,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1  *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {5,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {2,S} {13,S} {14,S} {15,S}
5     O 0 2 {1,S} {2,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1  *3 C 1 0 {3,S} {5,S} {6,S}
2     C 0 0 {4,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     O 0 2 {1,S} {2,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.421882, 'd12': 1.318758, 'd13': 2.74022},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 23:58:59 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 114,
    reactant1 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.384498, 'd12': 1.346259, 'd13': 2.730612},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 00:36:16 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 115,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *3 O 1 2 {2,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    O 0 2 {1,S} {3,S}
3 *1 O 0 2 {2,S} {7,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {3,S}
""",
    product2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.201517, 'd12': 1.34754, 'd13': 2.547347},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 23:45:19 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 116,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *3 O 1 2 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    O 0 2 {1,S} {3,S}
3 *1 O 0 2 {2,S} {7,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {3,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.152543, 'd12': 1.404984, 'd13': 2.557307},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 23:54:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 117,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7  *2 H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.356039, 'd12': 1.360934, 'd13': 2.716761},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 01:10:15 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 118,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,D} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.351842, 'd12': 1.408127, 'd13': 2.756651},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 00:30:38 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 119,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,D} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.307129, 'd12': 1.461382, 'd13': 2.768218},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 00:35:12 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 120,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {11,S} {12,S} {13,S}
4     C 0 0 {1,S} {14,S} {15,S} {16,S}
5     O 0 2 {1,S} {6,S}
6  *1 O 0 2 {5,S} {7,S}
7  *2 H 0 0 {6,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {4,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {1,S} {13,S} {14,S} {15,S}
5     O 0 2 {1,S} {6,S}
6  *3 O 1 2 {5,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.453162, 'd12': 1.113429, 'd13': 2.565773},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 01:22:15 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 121,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8  *2 H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,D} {6,S}
3    C 0 0 {2,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.44811, 'd12': 1.286944, 'd13': 2.734005},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 04:42:11 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 122,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,S} {12,S} {13,S}
5     C 0 0 {3,S} {4,S} {14,S} {15,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {5,S} {9,S} {10,S}
4     C 0 0 {2,S} {5,S} {11,S} {12,S}
5     C 0 0 {3,S} {4,S} {13,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.389466, 'd12': 1.322772, 'd13': 2.712125},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 04:39:04 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 123,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,S} {12,S} {13,S}
5     C 0 0 {3,S} {4,S} {14,S} {15,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    product2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {5,S} {9,S} {10,S}
4     C 0 0 {2,S} {5,S} {11,S} {12,S}
5     C 0 0 {3,S} {4,S} {13,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.195943, 'd12': 1.347002, 'd13': 2.542942},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 03:53:49 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 124,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {4,S} {6,S} {8,S} {9,S}
2     C 0 0 {5,S} {10,S} {11,S} {12,S}
3     C 0 0 {4,S} {5,S} {7,D}
4     O 0 2 {1,S} {3,S}
5     O 0 2 {2,S} {3,S}
6  *2 H 0 0 {1,S}
7     O 0 2 {3,D}
8     H 0 0 {1,S}
9     H 0 0 {1,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {2,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1  *3 C 1 0 {4,S} {7,S} {8,S}
2     C 0 0 {5,S} {9,S} {10,S} {11,S}
3     C 0 0 {4,S} {5,S} {6,D}
4     O 0 2 {1,S} {3,S}
5     O 0 2 {2,S} {3,S}
6     O 0 2 {3,D}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.382092, 'd12': 1.321991, 'd13': 2.703748},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 03:50:14 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 125,
    reactant1 = """
1    H 0 0 {2,S}
2 *3 O 1 2 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {4,B} {8,S}
3     C 0 0 {1,B} {5,B} {9,S}
4     C 0 0 {2,B} {6,B} {10,S}
5     C 0 0 {3,B} {6,B} {11,S}
6     C 0 0 {4,B} {5,B} {12,S}
7  *2 H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
12    H 0 0 {6,S}
""",
    product1 = """
1 *1 O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
""",
    product2 = """
1  *3 C 1 0 {2,B} {3,B}
2     C 0 0 {1,B} {4,B} {7,S}
3     C 0 0 {1,B} {5,B} {8,S}
4     C 0 0 {2,B} {6,B} {9,S}
5     C 0 0 {3,B} {6,B} {10,S}
6     C 0 0 {4,B} {5,B} {11,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
11    H 0 0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.259028, 'd12': 1.243519, 'd13': 2.490608},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 04:52:55 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 126,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,D} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7 *2 H 0 0 {2,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.405721, 'd12': 1.205245, 'd13': 2.603715},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 09:08:12 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 127,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,D} {7,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7    H 0 0 {2,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,D} {6,S}
3    O 0 2 {2,D}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.25767, 'd12': 1.278589, 'd13': 2.534594},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 09:28:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 128,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8  *2 H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.410864, 'd12': 1.321875, 'd13': 2.730185},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 10:59:27 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 129,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 0 {1,S} {4,S} {9,S} {10,S}
3     C 0 0 {1,S} {5,S} {11,S} {12,S}
4     C 0 0 {2,S} {6,S} {13,S} {14,S}
5     C 0 0 {3,S} {6,D} {15,S}
6     C 0 0 {4,S} {5,D} {16,S}
7  *2 H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {6,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product2 = """
1  *3 C 1 0 {2,S} {3,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {6,S} {12,S} {13,S}
5     C 0 0 {3,S} {6,D} {14,S}
6     C 0 0 {4,S} {5,D} {15,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.370231, 'd12': 1.341899, 'd13': 2.712072},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 11:43:26 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 130,
    reactant1 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {1,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    product1 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *3 C 1 0 {1,S} {6,S} {7,S}
3     C 0 0 {1,S} {8,S} {9,S} {10,S}
4     C 0 0 {1,S} {11,S} {12,S} {13,S}
5     C 0 0 {1,S} {14,S} {15,S} {16,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.33492, 'd12': 1.390728, 'd13': 2.723733},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 16:54:12 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 131,
    reactant1 = """
1    H 0 0 {2,S}
2 *3 C 1 0 {1,S} {3,S} {4,S}
3    C 0 0 {2,S} {5,S} {6,D}
4    H 0 0 {2,S}
5    H 0 0 {3,S}
6    C 0 0 {3,D} {7,S} {8,S}
7    H 0 0 {6,S}
8    H 0 0 {6,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,D} {8,S}
3     C 0 0 {1,S} {5,D} {9,S}
4     C 0 0 {2,D} {5,S} {10,S}
5     C 0 0 {3,D} {4,S} {11,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    product2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,D} {7,S}
3     C 0 0 {1,S} {5,D} {8,S}
4     C 0 0 {2,D} {5,S} {9,S}
5     C 0 0 {3,D} {4,S} {10,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.391177, 'd12': 1.337615, 'd13': 2.727653},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 13:43:36 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 132,
    reactant1 = """
1    H 0 0 {2,S}
2    C 0 0 {1,S} {3,T}
3    C 0 0 {2,T} {4,S}
4 *3 C 1 0 {3,S} {5,S} {6,S}
5    H 0 0 {4,S}
6    H 0 0 {4,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,D} {8,S}
3     C 0 0 {1,S} {5,D} {9,S}
4     C 0 0 {2,D} {5,S} {10,S}
5     C 0 0 {3,D} {4,S} {11,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
""",
    product1 = """
1    H 0 0 {2,S}
2    C 0 0 {1,S} {3,T}
3    C 0 0 {2,T} {4,S}
4 *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
5 *2 H 0 0 {4,S}
6    H 0 0 {4,S}
7    H 0 0 {4,S}
""",
    product2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,D} {7,S}
3     C 0 0 {1,S} {5,D} {8,S}
4     C 0 0 {2,D} {5,S} {9,S}
5     C 0 0 {3,D} {4,S} {10,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.415978, 'd12': 1.314561, 'd13': 2.730215},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 13:56:57 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 133,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {7,S} {8,S}
2  *1 C 0 0 {1,S} {4,S} {5,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {2,S} {6,D} {13,S}
5  *2 H 0 0 {2,S}
6     O 0 2 {4,D}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7  *2 H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2  *3 C 1 0 {1,S} {4,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,D} {12,S}
5     O 0 2 {4,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.454247, 'd12': 1.286158, 'd13': 2.739153},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 16:47:41 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 134,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {8,S}
2     C 0 0 {1,S} {9,S} {10,S} {11,S}
3     C 0 0 {1,S} {5,D} {12,S}
4     C 0 0 {1,S} {6,D} {13,S}
5     C 0 0 {3,D} {7,S} {15,S}
6     C 0 0 {4,D} {7,S} {16,S}
7     C 0 0 {5,S} {6,S} {14,D}
8  *2 H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    O 0 2 {7,D}
15    H 0 0 {5,S}
16    H 0 0 {6,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {8,S} {9,S} {10,S}
2  *3 C 1 0 {1,S} {3,S} {4,S}
3     C 0 0 {2,S} {5,D} {12,S}
4     C 0 0 {2,S} {6,D} {13,S}
5     C 0 0 {3,D} {7,S} {14,S}
6     C 0 0 {4,D} {7,S} {15,S}
7     C 0 0 {5,S} {6,S} {11,D}
8     H 0 0 {1,S}
9     H 0 0 {1,S}
10    H 0 0 {1,S}
11    O 0 2 {7,D}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.627066, 'd12': 1.210734, 'd13': 2.837081},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 18:59:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 135,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1  *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {5,D}
4  *2 H 0 0 {1,S}
5     O 0 2 {3,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    product2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 0 {1,S} {2,S} {4,D}
4    O 0 2 {3,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.254681, 'd12': 1.279753, 'd13': 2.532874},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 22:20:02 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 136,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    product2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.318814, 'd12': 1.251585, 'd13': 2.554427},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 22:58:02 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 137,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.245048, 'd12': 1.288264, 'd13': 2.531537},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 01:47:56 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 138,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1  *1 C 0 0 {8,S} {9,S} {10,S} {11,S}
2     C 0 0 {3,B} {4,B} {8,S}
3     C 0 0 {2,B} {6,B} {12,S}
4     C 0 0 {2,B} {7,B} {13,S}
5     C 0 0 {6,B} {7,B} {14,S}
6     C 0 0 {3,B} {5,B} {15,S}
7     C 0 0 {4,B} {5,B} {16,S}
8     O 0 2 {1,S} {2,S}
9  *2 H 0 0 {1,S}
10    H 0 0 {1,S}
11    H 0 0 {1,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {6,S}
16    H 0 0 {7,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,B} {3,B} {8,S}
2     C 0 0 {1,B} {5,B} {9,S}
3     C 0 0 {1,B} {6,B} {10,S}
4     C 0 0 {5,B} {6,B} {11,S}
5     C 0 0 {2,B} {4,B} {12,S}
6     C 0 0 {3,B} {4,B} {13,S}
7  *3 C 1 0 {8,S} {14,S} {15,S}
8     O 0 2 {1,S} {7,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {5,S}
13    H 0 0 {6,S}
14    H 0 0 {7,S}
15    H 0 0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4136, 'd12': 1.311451, 'd13': 2.724572},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 21:32:44 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 139,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    product2 = """
1     C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 0 {1,S} {3,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.286517, 'd12': 1.264185, 'd13': 2.546171},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 00:37:13 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 140,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.247176, 'd12': 1.284317, 'd13': 2.529051},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 01:45:03 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 141,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {1,S} {15,S} {16,S} {17,S}
6     C 0 0 {2,S} {18,S} {19,S} {20,S}
7     C 0 0 {2,S} {21,S} {22,S} {23,S}
8     C 0 0 {2,S} {24,S} {25,S} {26,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
18    H 0 0 {6,S}
19    H 0 0 {6,S}
20    H 0 0 {6,S}
21    H 0 0 {7,S}
22    H 0 0 {7,S}
23    H 0 0 {7,S}
24    H 0 0 {8,S}
25    H 0 0 {8,S}
26    H 0 0 {8,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     C 0 0 {1,S} {11,S} {12,S} {13,S}
5     C 0 0 {1,S} {14,S} {15,S} {16,S}
6     C 0 0 {2,S} {17,S} {18,S} {19,S}
7     C 0 0 {2,S} {20,S} {21,S} {22,S}
8     C 0 0 {2,S} {23,S} {24,S} {25,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {6,S}
18    H 0 0 {6,S}
19    H 0 0 {6,S}
20    H 0 0 {7,S}
21    H 0 0 {7,S}
22    H 0 0 {7,S}
23    H 0 0 {8,S}
24    H 0 0 {8,S}
25    H 0 0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.379587, 'd12': 1.333337, 'd13': 2.706613},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 08:06:55 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 142,
    reactant1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 0 {2,S}
4     H 0 0 {2,S}
5     C 0 0 {2,S} {6,S} {7,S} {8,S}
6     C 0 0 {5,S} {9,S} {10,S} {11,S}
7     C 0 0 {5,S} {12,S} {13,S} {14,S}
8     C 0 0 {5,S} {15,S} {16,S} {17,S}
9     H 0 0 {6,S}
10    O 0 2 {6,S} {18,S}
11    H 0 0 {6,S}
12    H 0 0 {7,S}
13    H 0 0 {7,S}
14    H 0 0 {7,S}
15    H 0 0 {8,S}
16    H 0 0 {8,S}
17    H 0 0 {8,S}
18 *3 O 1 2 {10,S}
""",
    reactant2 = """
1 *1 O 0 2 {2,S} {3,S}
2    O 1 2 {1,S}
3 *2 H 0 0 {1,S}
""",
    product1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 0 {2,S}
4     C 0 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 0 {2,S}
6     C 0 0 {4,S} {9,S} {10,S} {11,S}
7     C 0 0 {4,S} {12,S} {13,S} {14,S}
8     C 0 0 {4,S} {15,S} {16,S} {17,S}
9     H 0 0 {6,S}
10    H 0 0 {6,S}
11    H 0 0 {6,S}
12    H 0 0 {7,S}
13    H 0 0 {7,S}
14    H 0 0 {7,S}
15    O 0 2 {8,S} {18,S}
16    H 0 0 {8,S}
17    H 0 0 {8,S}
18 *1 O 0 2 {15,S} {19,S}
19 *2 H 0 0 {18,S}
""",
    product2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.345438, 'd12': 1.094942, 'd13': 2.436127},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 04:47:09 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 143,
    reactant1 = """
1     H 0 0 {2,S}
2     O 0 2 {1,S} {3,S}
3     C 0 0 {2,S} {4,S} {5,S} {6,S}
4     C 0 0 {3,S} {7,S} {8,S} {9,S}
5     C 0 0 {3,S} {10,S} {11,S} {12,S}
6     C 0 0 {3,S} {13,S} {14,S} {15,S}
7     H 0 0 {4,S}
8     H 0 0 {4,S}
9     H 0 0 {4,S}
10    O 0 2 {5,S} {16,S}
11    H 0 0 {5,S}
12    H 0 0 {5,S}
13    H 0 0 {6,S}
14    H 0 0 {6,S}
15    H 0 0 {6,S}
16 *3 O 1 2 {10,S}
""",
    reactant2 = """
1 *1 O 0 2 {2,S} {3,S}
2    O 1 2 {1,S}
3 *2 H 0 0 {1,S}
""",
    product1 = """
1     H 0 0 {2,S}
2     O 0 2 {1,S} {3,S}
3     C 0 0 {2,S} {4,S} {5,S} {6,S}
4     C 0 0 {3,S} {7,S} {8,S} {9,S}
5     C 0 0 {3,S} {10,S} {11,S} {12,S}
6     C 0 0 {3,S} {13,S} {14,S} {15,S}
7     O 0 2 {4,S} {16,S}
8     H 0 0 {4,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
11    H 0 0 {5,S}
12    H 0 0 {5,S}
13    H 0 0 {6,S}
14    H 0 0 {6,S}
15    H 0 0 {6,S}
16 *1 O 0 2 {7,S} {17,S}
17 *2 H 0 0 {16,S}
""",
    product2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.420877, 'd12': 1.060269, 'd13': 2.465326},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 06:24:58 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 144,
    reactant1 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    O 1 2 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {7,S} {9,S}
2     C 0 0 {1,S} {5,S} {10,S} {11,S}
3     C 0 0 {1,S} {6,S} {12,S} {13,S}
4     C 0 0 {5,S} {6,S} {14,S} {15,S}
5     C 0 0 {2,S} {4,S} {16,S} {17,S}
6     C 0 0 {3,S} {4,S} {18,S} {19,S}
7     O 0 2 {1,S} {8,S}
8  *3 O 1 2 {7,S}
9     H 0 0 {1,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
18    H 0 0 {6,S}
19    H 0 0 {6,S}
""",
    product1 = """
1  *2 H 0 0 {2,S}
2  *1 O 0 2 {1,S} {3,S}
3     O 0 2 {2,S} {4,S}
4     C 0 0 {3,S} {5,S} {6,S} {7,S}
5     H 0 0 {4,S}
6     C 0 0 {4,S} {8,S} {9,S} {10,S}
7     C 0 0 {4,S} {11,S} {12,S} {13,S}
8     H 0 0 {6,S}
9     C 0 0 {6,S} {14,S} {15,S} {16,S}
10    H 0 0 {6,S}
11    H 0 0 {7,S}
12    C 0 0 {7,S} {15,S} {17,S} {18,S}
13    H 0 0 {7,S}
14    H 0 0 {9,S}
15    C 0 0 {9,S} {12,S} {19,S} {20,S}
16    H 0 0 {9,S}
17    H 0 0 {12,S}
18    H 0 0 {12,S}
19    H 0 0 {15,S}
20    H 0 0 {15,S}
""",
    product2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.405068, 'd12': 1.066347, 'd13': 2.461135},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 16:45:44 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 145,
    reactant1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {3,S} {4,S} {5,S} {9,S}
2     C 0 0 {6,S} {7,S} {8,S} {10,S}
3  *1 C 0 0 {1,S} {11,S} {12,S} {13,S}
4     C 0 0 {1,S} {14,S} {15,S} {16,S}
5     C 0 0 {1,S} {17,S} {18,S} {19,S}
6     C 0 0 {2,S} {20,S} {21,S} {22,S}
7     C 0 0 {2,S} {23,S} {24,S} {25,S}
8     C 0 0 {2,S} {26,S} {27,S} {28,S}
9     O 0 2 {1,S} {10,S}
10    O 0 2 {2,S} {9,S}
11 *2 H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {4,S}
17    H 0 0 {5,S}
18    H 0 0 {5,S}
19    H 0 0 {5,S}
20    H 0 0 {6,S}
21    H 0 0 {6,S}
22    H 0 0 {6,S}
23    H 0 0 {7,S}
24    H 0 0 {7,S}
25    H 0 0 {7,S}
26    H 0 0 {8,S}
27    H 0 0 {8,S}
28    H 0 0 {8,S}
""",
    product1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {3,S} {4,S} {5,S} {9,S}
2     C 0 0 {6,S} {7,S} {8,S} {10,S}
3  *3 C 1 0 {1,S} {11,S} {12,S}
4     C 0 0 {1,S} {13,S} {14,S} {15,S}
5     C 0 0 {1,S} {16,S} {17,S} {18,S}
6     C 0 0 {2,S} {19,S} {20,S} {21,S}
7     C 0 0 {2,S} {22,S} {23,S} {24,S}
8     C 0 0 {2,S} {25,S} {26,S} {27,S}
9     O 0 2 {1,S} {10,S}
10    O 0 2 {2,S} {9,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
18    H 0 0 {5,S}
19    H 0 0 {6,S}
20    H 0 0 {6,S}
21    H 0 0 {6,S}
22    H 0 0 {7,S}
23    H 0 0 {7,S}
24    H 0 0 {7,S}
25    H 0 0 {8,S}
26    H 0 0 {8,S}
27    H 0 0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.362866, 'd12': 1.339148, 'd13': 2.70112},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 21:49:08 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 146,
    reactant1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,B} {4,B}
3  *3 C 1 0 {2,B} {5,B}
4     C 0 0 {2,B} {6,B} {7,S}
5     C 0 0 {3,B} {8,B} {9,S}
6     C 0 0 {4,B} {8,B} {10,S}
7     H 0 0 {4,S}
8     C 0 0 {5,B} {6,B} {11,S}
9     H 0 0 {5,S}
10    H 0 0 {6,S}
11    H 0 0 {8,S}
""",
    reactant2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,D} {8,S}
3     C 0 0 {1,S} {5,D} {9,S}
4     C 0 0 {2,D} {5,S} {10,S}
5     C 0 0 {3,D} {4,S} {11,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
""",
    product1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,B} {4,B}
3     C 0 0 {2,B} {5,B} {6,S}
4  *1 C 0 0 {2,B} {7,S} {8,B}
5     C 0 0 {3,B} {9,B} {10,S}
6     H 0 0 {3,S}
7  *2 H 0 0 {4,S}
8     C 0 0 {4,B} {9,B} {11,S}
9     C 0 0 {5,B} {8,B} {12,S}
10    H 0 0 {5,S}
11    H 0 0 {8,S}
12    H 0 0 {9,S}
""",
    product2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,D} {7,S}
3     C 0 0 {1,S} {5,D} {8,S}
4     C 0 0 {2,D} {5,S} {9,S}
5     C 0 0 {3,D} {4,S} {10,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.585963, 'd12': 1.207705, 'd13': 2.793668},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 18:50:21 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 147,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1  *1 C 0 0 {5,S} {7,S} {8,S} {9,S}
2     C 0 0 {5,S} {10,S} {11,S} {12,S}
3     C 0 0 {6,S} {13,S} {14,S} {15,S}
4     C 0 0 {6,S} {16,S} {17,S} {18,S}
5     C 0 0 {1,S} {2,S} {6,D}
6     C 0 0 {3,S} {4,S} {5,D}
7  *2 H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {1,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {2,S}
13    H 0 0 {3,S}
14    H 0 0 {3,S}
15    H 0 0 {3,S}
16    H 0 0 {4,S}
17    H 0 0 {4,S}
18    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    product2 = """
1  *3 C 1 0 {5,S} {7,S} {8,S}
2     C 0 0 {5,S} {9,S} {10,S} {11,S}
3     C 0 0 {6,S} {12,S} {13,S} {14,S}
4     C 0 0 {6,S} {15,S} {16,S} {17,S}
5     C 0 0 {1,S} {2,S} {6,D}
6     C 0 0 {3,S} {4,S} {5,D}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {3,S}
15    H 0 0 {4,S}
16    H 0 0 {4,S}
17    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.387594, 'd12': 1.217391, 'd13': 2.604205},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Sat May 24 09:29:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 148,
    reactant1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,B} {4,B}
3     C 0 0 {2,B} {5,S} {6,B}
4     C 0 0 {2,B} {7,S} {8,B}
5     H 0 0 {3,S}
6     C 0 0 {3,B} {9,S} {10,B}
7     H 0 0 {4,S}
8     C 0 0 {4,B} {10,B} {11,S}
9     C 0 0 {6,S} {12,S} {13,S} {14,S}
10    C 0 0 {6,B} {8,B} {15,S}
11    H 0 0 {8,S}
12    H 0 0 {9,S}
13    H 0 0 {9,S}
14    O 0 2 {9,S} {16,S}
15    H 0 0 {10,S}
16 *3 O 1 2 {14,S}
""",
    reactant2 = """
1 *1 O 0 2 {2,S} {3,S}
2    O 1 2 {1,S}
3 *2 H 0 0 {1,S}
""",
    product1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,B} {4,B}
3     C 0 0 {2,B} {5,S} {6,B}
4     C 0 0 {2,B} {7,S} {8,B}
5     H 0 0 {3,S}
6     C 0 0 {3,B} {9,B} {10,S}
7     H 0 0 {4,S}
8     C 0 0 {4,B} {9,B} {11,S}
9     C 0 0 {6,B} {8,B} {12,S}
10    C 0 0 {6,S} {13,S} {14,S} {15,S}
11    H 0 0 {8,S}
12    H 0 0 {9,S}
13    O 0 2 {10,S} {16,S}
14    H 0 0 {10,S}
15    H 0 0 {10,S}
16 *1 O 0 2 {13,S} {17,S}
17 *2 H 0 0 {16,S}
""",
    product2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.374965, 'd12': 1.076901, 'd13': 2.450556},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via group additive TS generator.""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 21:44:58 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 149,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
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
    history = [
        ('Thu Oct  3 16:15:59 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 150,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
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
    history = [
        ('Fri Oct  4 13:03:20 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 151,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
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
    history = [
        ('Thu Oct  3 19:11:41 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 152,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,D} {4,S}
2 *2 H 0 0 {1,S}
3    O 0 2 {1,D}
4    H 0 0 {1,S}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {2,D} {3,S}
2    O 0 2 {1,D}
3    H 0 0 {1,S}
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
    history = [
        ('Thu Oct  3 21:06:25 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 153,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    C 0 0 {2,D} {4,S} {5,S}
2 *1 C 0 0 {1,D} {3,S} {6,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
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
    history = [
        ('Fri Oct  4 14:36:06 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 154,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    O 0 2 {2,S} {4,S}
2 *1 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
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
    history = [
        ('Thu Oct  3 23:15:02 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 155,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
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
    history = [
        ('Sat Oct  5 07:17:14 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 156,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,D} {4,S}
2 *3 C 1 0 {1,S} {5,S} {6,S}
3    C 0 0 {1,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
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
    history = [
        ('Sat Oct  5 21:39:01 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 157,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    O 0 2 {1,S} {3,S}
3 *1 O 0 2 {2,S} {7,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {3,S}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *3 O 1 2 {2,S}
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
    history = [
        ('Sun Oct  6 05:11:10 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 158,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    O 0 2 {2,D}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
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
    history = [
        ('Sun Oct  6 06:31:12 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 159,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3 *3 C 1 0 {2,D} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3 *1 C 0 0 {2,D} {8,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8 *2 H 0 0 {3,S}
9    H 0 0 {3,S}
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
    history = [
        ('Sun Oct  6 08:26:17 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 160,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 0 {3,D} {7,S} {8,S}
3 *3 C 1 0 {1,S} {2,D}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
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
    history = [
        ('Sun Oct  6 10:45:23 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 161,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
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
    history = [
        ('Mon Oct  7 07:11:14 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 162,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,D} {5,S}
2    C 0 0 {1,S} {4,D} {6,S}
3    C 0 0 {1,D} {7,S} {8,S}
4 *3 C 1 0 {2,D} {9,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
9    H 0 0 {4,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,D} {5,S}
2     C 0 0 {1,S} {4,D} {6,S}
3  *1 C 0 0 {1,D} {7,S} {8,S}
4     C 0 0 {2,D} {9,S} {10,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7  *2 H 0 0 {3,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {4,S}
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
    history = [
        ('Mon Oct  7 12:18:12 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 163,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 0 0 {1,S} {4,S} {5,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {2,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 0 {1,S} {3,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
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
    history = [
        ('Tue Oct  8 10:23:39 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 164,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     O 0 2 {2,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     O 0 2 {2,S} {12,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
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
    history = [
        ('Thu Oct 10 22:36:03 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 165,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {4,D} {7,S}
3    O 0 2 {1,S} {2,S}
4    O 0 2 {2,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1 *1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,D} {8,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    O 0 2 {2,D}
8    H 0 0 {2,S}
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
    history = [
        ('Fri Oct 11 00:52:04 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 166,
    reactant1 = """
1 *3 H 1 0
""",
    reactant2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {4,D} {12,S}
4  *1 C 0 0 {2,S} {3,D} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11 *2 H 0 0 {4,S}
12    H 0 0 {3,S}
""",
    product1 = """
1 *2 H 0 0 {2,S}
2 *1 H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {4,D} {11,S}
4  *3 C 1 0 {2,S} {3,D}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
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
    history = [
        ('Fri Oct 11 07:52:33 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 167,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     O 0 2 {3,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4  *1 C 0 0 {2,S} {12,S} {13,S} {14,S}
5     O 0 2 {3,S} {15,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12 *2 H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
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
    history = [
        ('Fri Oct 11 22:27:35 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 168,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     O 0 2 {1,S} {14,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     O 0 2 {1,S} {15,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
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
    history = [
        ('Sat Oct 12 13:28:20 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 169,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 C 1 0 {2,S} {15,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {1,S} {13,S} {14,S} {15,S}
5  *1 C 0 0 {2,S} {9,S} {16,S} {17,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {5,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
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
    history = [
        ('Sun Oct 13 02:56:15 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 170,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {5,S} {13,S} {14,S} {15,S}
5  *3 C 1 0 {1,S} {4,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {6,S}
2  *1 C 0 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {2,S} {15,S} {16,S} {17,S}
6     H 0 0 {1,S}
7  *2 H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
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
    history = [
        ('Sun Oct 13 18:16:24 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 171,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {5,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {5,S} {13,S} {14,S} {15,S}
5  *3 C 1 0 {2,S} {4,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {7,S} {8,S}
2  *1 C 0 0 {1,S} {4,S} {6,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     C 0 0 {3,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
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
    history = [
        ('Mon Oct 14 20:11:44 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 172,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 C 1 0 {1,S} {15,S} {16,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {1,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
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
    history = [
        ('Wed Oct 23 23:13:03 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 173,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *3 C 1 0 {1,S} {15,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 0 {1,S} {5,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {2,S} {15,S} {16,S} {17,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
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
    history = [
        ('Thu Oct 24 19:10:33 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 174,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {4,B} {8,S}
3     C 0 0 {1,B} {5,B} {9,S}
4     C 0 0 {2,B} {6,B} {10,S}
5     C 0 0 {3,B} {6,B} {11,S}
6  *3 C 1 0 {4,B} {5,B}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1  *1 C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {4,B} {8,S}
3     C 0 0 {1,B} {5,B} {9,S}
4     C 0 0 {2,B} {6,B} {10,S}
5     C 0 0 {3,B} {6,B} {11,S}
6     C 0 0 {4,B} {5,B} {12,S}
7  *2 H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
12    H 0 0 {6,S}
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
    history = [
        ('Fri Oct 25 07:16:46 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 175,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {5,B} {8,S}
3     C 0 0 {1,B} {6,B} {9,S}
4     C 0 0 {5,B} {6,B} {10,S}
5     C 0 0 {2,B} {4,B} {11,S}
6     C 0 0 {3,B} {4,B} {12,S}
7  *3 O 1 2 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
12    H 0 0 {6,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {5,B} {8,S}
3     C 0 0 {1,B} {6,B} {9,S}
4     C 0 0 {5,B} {6,B} {10,S}
5     C 0 0 {2,B} {4,B} {11,S}
6     C 0 0 {3,B} {4,B} {12,S}
7  *1 O 0 2 {1,S} {13,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
12    H 0 0 {6,S}
13 *2 H 0 0 {7,S}
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
    history = [
        ('Fri Oct 25 21:17:19 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 176,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {8,S} {9,S} {10,S}
2     C 0 0 {1,S} {3,B} {4,B}
3     C 0 0 {2,B} {6,B} {11,S}
4     C 0 0 {2,B} {7,B} {12,S}
5     C 0 0 {6,B} {7,B} {13,S}
6     C 0 0 {3,B} {5,B} {14,S}
7     C 0 0 {4,B} {5,B} {15,S}
8  *3 C 1 0 {1,S} {16,S} {17,S}
9     H 0 0 {1,S}
10    H 0 0 {1,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {6,S}
15    H 0 0 {7,S}
16    H 0 0 {8,S}
17    H 0 0 {8,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {9,S} {10,S}
2  *1 C 0 0 {1,S} {11,S} {12,S} {13,S}
3     C 0 0 {1,S} {4,B} {5,B}
4     C 0 0 {3,B} {7,B} {14,S}
5     C 0 0 {3,B} {8,B} {15,S}
6     C 0 0 {7,B} {8,B} {16,S}
7     C 0 0 {4,B} {6,B} {17,S}
8     C 0 0 {5,B} {6,B} {18,S}
9     H 0 0 {1,S}
10    H 0 0 {1,S}
11 *2 H 0 0 {2,S}
12    H 0 0 {2,S}
13    H 0 0 {2,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {6,S}
17    H 0 0 {7,S}
18    H 0 0 {8,S}
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
    history = [
        ('Sun Oct 27 06:17:26 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via double-ended strategy using automatic transition state generator'),
    ],
)

entry(
    index = 177,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    O 0 2 {1,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 178,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,S} {7,S}
3    O 0 2 {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 179,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *3 O 1 2 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *1 O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9 *2 H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 180,
    reactant1 = """
1    O 0 2 {2,S} {4,S}
2 *1 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    O 0 2 {1,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 181,
    reactant1 = """
1    O 0 2 {2,S} {4,S}
2 *1 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,S} {7,S}
3    O 0 2 {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 182,
    reactant1 = """
1    O 0 2 {2,S} {4,S}
2 *1 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *3 O 1 2 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *1 O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9 *2 H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 183,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 184,
    reactant1 = """
1    O 0 2 {2,S} {4,S}
2 *3 O 0 2 {1,S} {3,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 185,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,D} {4,S} {5,S}
2 *1 C 0 0 {1,D} {3,S} {6,S}
3 *2 H 0 0 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 186,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {4,S} {9,S} {10,S}
4  *3 C 1 0 {2,S} {3,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {4,S} {6,S} {7,S}
2     C 0 0 {1,S} {3,S} {8,S} {9,S}
3     C 0 0 {2,S} {4,S} {10,S} {11,S}
4  *1 C 0 0 {1,S} {3,S} {5,S} {12,S}
5  *2 H 0 0 {4,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 187,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    O 0 2 {1,S} {3,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {3,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 188,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    O 0 2 {1,S} {3,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {3,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 189,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {3,S} {6,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 190,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3 *3 C 1 0 {1,S} {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    C 0 0 {1,S} {2,S} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 191,
    reactant1 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    O 0 2 {1,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *3 O 1 2 {2,S}
2    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 192,
    reactant1 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,S} {7,S} {8,S}
3 *3 O 1 2 {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1 *3 O 1 2 {2,S}
2    H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *1 O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9 *2 H 0 0 {3,S}
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
    history = [
        ('Sun Nov 17 1:40:36 2013', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', ' '),
    ],
)

entry(
    index = 193,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1 *3 O 1 2 {2,S}
2    H 0 0 {1,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.407349, 'd12': 0.808251, 'd13': 2.196944},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 45""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:30:51 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 194,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    reactant2 = """
1 *3 H 1 0
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    O 0 2 {1,S} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    product2 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.002833, 'd12': 1.296176, 'd13': 2.29898},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 46""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:37:06 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 195,
    reactant1 = """
1    H 0 0 {2,S}
2 *3 O 1 2 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    product1 = """
1 *1 O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
""",
    product2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.324475, 'd12': 1.216325, 'd13': 2.537847},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 47""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:37:28 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 196,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *3 O 1 2 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *1 O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9 *2 H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.201, 'd12': 0.91111, 'd13': 2.10677},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 48""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:47:00 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 197,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,S} {7,S}
3    O 0 2 {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.250952, 'd12': 1.060399, 'd13': 2.311305},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 49""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:47:09 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 198,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    O 0 2 {1,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3    O 0 2 {1,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.366101, 'd12': 0.926377, 'd13': 2.29247},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 50""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:47:18 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 199,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *3 O 1 2 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.310536, 'd12': 1.19983, 'd13': 2.509181},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 51""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:58:37 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 200,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,D} {4,S}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
4 *2 H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,D}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.486471, 'd12': 1.274424, 'd13': 2.760463},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 52""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:46:21 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 201,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.425793, 'd12': 1.126056, 'd13': 2.55168},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 53""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:48:35 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 202,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3 *3 C 1 0 {1,S} {2,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    C 0 0 {1,S} {2,S} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.430155, 'd12': 0.877258, 'd13': 2.306828},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 54""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:01:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 203,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {3,S} {6,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.366575, 'd12': 0.927201, 'd13': 2.293246},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 55""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 04:57:37 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 204,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {3,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {3,S} {7,S} {8,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1 *1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.297897, 'd12': 1.008692, 'd13': 2.306541},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 56""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:03:08 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 205,
    reactant1 = """
1    H 0 0 {2,S}
2 *3 O 1 2 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *1 C 0 0 {1,D} {5,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6 *2 H 0 0 {2,S}
""",
    product1 = """
1 *1 O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
""",
    product2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.272333, 'd12': 1.235607, 'd13': 2.495812},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 57""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:08:49 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 206,
    reactant1 = """
1    H 0 0 {2,S}
2 *3 O 1 2 {1,S}
""",
    reactant2 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    product1 = """
1 *1 O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
""",
    product2 = """
1    O 0 2 {2,S} {3,S}
2 *3 O 1 2 {1,S}
3    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.591884, 'd12': 1.002539, 'd13': 2.498974},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 58""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:07:51 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 207,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1 *3 O 1 2 {2,S}
2    H 0 0 {1,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.477049, 'd12': 1.162672, 'd13': 2.638169},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 59""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:26:01 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 208,
    reactant1 = """
1 *1 C 0 0 {2,D} {3,S} {4,S}
2    C 0 0 {1,D} {5,S} {6,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    O 0 2 {1,S} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    product1 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.262583, 'd12': 1.464952, 'd13': 2.727535},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 60""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:34:53 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 209,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3  *3 C 1 0 {1,S} {2,S} {4,S}
4     O 0 2 {3,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {4,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     O 0 2 {1,S} {12,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.193929, 'd12': 1.176607, 'd13': 2.370363},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 61""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:52:18 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 210,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 0 {1,S} {2,S} {4,D}
4    O 0 2 {3,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1  *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {5,D}
4  *2 H 0 0 {1,S}
5     O 0 2 {3,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.268907, 'd12': 1.012158, 'd13': 2.279237},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 62""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 05:41:26 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 211,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *3 O 1 2 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.275568, 'd12': 1.246208, 'd13': 2.521678},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 63""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:02:57 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 212,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *3 C 1 0 {1,S} {6,S} {7,S}
3     C 0 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2  *1 C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {2,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.32602, 'd12': 1.380732, 'd13': 2.706495},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 64""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:29:49 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 213,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    C 0 0 {1,S} {3,S} {5,S} {6,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,S} {6,S} {7,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.332471, 'd12': 1.363688, 'd13': 2.695568},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 65""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:18:45 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 214,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,D} {6,S}
3    C 0 0 {2,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.26608, 'd12': 1.470831, 'd13': 2.736083},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 66""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:31:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 215,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {3,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {3,S} {7,S} {8,S}
3    O 0 2 {1,S} {2,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1 *1 C 0 0 {3,S} {4,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.302739, 'd12': 1.430905, 'd13': 2.733224},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 67""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:40:03 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 216,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7  *2 H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1 *3 H 1 0
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product2 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 0.926853, 'd12': 1.371495, 'd13': 2.298343},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 68""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 07:03:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 217,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    reactant2 = """
1 *1 C 0 0 {2,D} {3,S} {4,S}
2    O 0 2 {1,D}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    product2 = """
1 *3 C 1 0 {2,D} {3,S}
2    O 0 2 {1,D}
3    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.223801, 'd12': 1.317309, 'd13': 2.535817},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 69""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 06:39:05 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 218,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 0 {1,S} {2,S} {4,D}
4    O 0 2 {3,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {5,D}
4  *2 H 0 0 {1,S}
5     O 0 2 {3,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.284618, 'd12': 1.429246, 'd13': 2.712247},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 70""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 07:59:34 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 219,
    reactant1 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.380621, 'd12': 1.33542, 'd13': 2.716025},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 71""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:45:14 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 220,
    reactant1 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    O 0 2 {1,S} {3,S}
3 *1 O 0 2 {2,S} {7,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {3,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *3 O 1 2 {2,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.40219, 'd12': 1.149865, 'd13': 2.551133},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 72""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 07:56:41 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 221,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.356755, 'd12': 1.355809, 'd13': 2.71208},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 73""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:35:43 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 222,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *3 O 1 2 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.24964, 'd12': 1.289857, 'd13': 2.539487},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 74""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:30:25 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 223,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *3 O 1 2 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.276309, 'd12': 1.248587, 'd13': 2.524895},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 75""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:28:00 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 224,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,D} {4,S}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
4 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,D}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.421184, 'd12': 1.329108, 'd13': 2.749792},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 76""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:39:14 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 225,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,D}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    O 0 2 {1,D}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,D}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.449892, 'd12': 1.306486, 'd13': 2.754254},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 77""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 09:03:31 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 226,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.355088, 'd12': 1.185967, 'd13': 2.540637},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 78""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 08:53:42 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 227,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.328058, 'd12': 1.377889, 'd13': 2.705697},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 79""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 10:13:30 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 228,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 0 {5,S} {11,S} {12,S} {13,S}
4     C 0 0 {5,S} {14,S} {15,S} {16,S}
5  *3 C 1 0 {1,S} {3,S} {4,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {4,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {6,S}
2     C 0 0 {1,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {2,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.235549, 'd12': 1.065669, 'd13': 2.301216},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 80""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 10:38:39 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 229,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 0 {1,S} {3,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.307025, 'd12': 1.409141, 'd13': 2.715605},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 81""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 10:36:33 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 230,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.325846, 'd12': 1.381915, 'd13': 2.707452},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 82""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 10:47:57 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 231,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,D} {5,S}
2    C 0 0 {1,S} {4,D} {6,S}
3 *3 C 1 0 {1,D} {7,S}
4    C 0 0 {2,D} {8,S} {9,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {4,S}
9    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,D} {6,S}
2     C 0 0 {1,S} {4,D} {7,S}
3  *1 C 0 0 {1,D} {5,S} {8,S}
4     C 0 0 {2,D} {9,S} {10,S}
5  *2 H 0 0 {3,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.382945, 'd12': 1.299711, 'd13': 2.682409},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 83""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 11:04:48 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 232,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *3 C 1 0 {3,S} {15,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4  *1 C 0 0 {2,S} {12,S} {13,S} {14,S}
5     C 0 0 {3,S} {15,S} {16,S} {17,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12 *2 H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.362744, 'd12': 0.930376, 'd13': 2.292827},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 84""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 11:42:17 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 233,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {5,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {2,S} {13,S} {14,S} {15,S}
5  *3 C 1 0 {1,S} {2,S} {16,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     C 0 0 {3,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.319334, 'd12': 0.968067, 'd13': 2.286248},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 85""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 11:52:49 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 234,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,D} {4,S}
2 *3 C 1 0 {1,S} {5,S} {6,S}
3    C 0 0 {1,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.287947, 'd12': 1.4443, 'd13': 2.732236},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 86""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 11:43:44 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 235,
    reactant1 = """
1 *1 C 0 0 {2,D} {3,S} {4,S}
2    C 0 0 {1,D} {5,S} {6,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,D} {6,S}
3    C 0 0 {2,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.235324, 'd12': 1.513197, 'd13': 2.74749},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 87""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:00:22 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 236,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 0 {1,S} {3,S} {4,D}
3  *3 C 1 0 {2,S} {8,S} {9,S}
4     C 0 0 {2,D} {10,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {4,D}
4     C 0 0 {3,D} {11,S} {12,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.272173, 'd12': 1.463225, 'd13': 2.734469},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 88""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:24:08 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 237,
    reactant1 = """
1 *1 H 0 0 {2,S}
2 *2 H 0 0 {1,S}
""",
    reactant2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {5,S} {9,S} {10,S}
4     C 0 0 {2,S} {5,S} {11,S} {12,S}
5     C 0 0 {3,S} {4,S} {13,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {5,S}
""",
    product1 = """
1 *3 H 1 0
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,S} {12,S} {13,S}
5     C 0 0 {3,S} {4,S} {14,S} {15,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.282451, 'd12': 0.994169, 'd13': 2.276393},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 89""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:21:13 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 238,
    reactant1 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    reactant2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    product1 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    O 1 2 {1,S}
""",
    product2 = """
1    C 0 0 {2,D} {3,S} {4,S}
2    C 0 0 {1,D} {5,S} {6,S}
3 *3 C 1 0 {1,S} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.131035, 'd12': 1.48516, 'd13': 2.614105},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 90""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:05:12 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 239,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11 *2 H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.160095, 'd12': 1.38475, 'd13': 2.544667},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 91""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:48:34 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 240,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 0 {1,S} {3,D} {7,S}
3    O 0 2 {2,D}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {2,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    product2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,D}
3    O 0 2 {2,D}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.222161, 'd12': 1.32645, 'd13': 2.548529},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 92""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:11:32 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 241,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 0 {1,S} {3,S} {8,S}
3     C 0 0 {2,S} {4,D} {9,S}
4     C 0 0 {3,D} {10,S} {11,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {1,S} {4,D} {10,S}
4     C 0 0 {3,D} {11,S} {12,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.255489, 'd12': 1.493337, 'd13': 2.74766},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 93""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 13:08:58 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 242,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {4,D} {7,S}
3    O 0 2 {1,S} {2,S}
4    O 0 2 {2,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1 *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2    C 0 0 {3,S} {5,D} {8,S}
3    O 0 2 {1,S} {2,S}
4 *2 H 0 0 {1,S}
5    O 0 2 {2,D}
6    H 0 0 {1,S}
7    H 0 0 {1,S}
8    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.321635, 'd12': 1.380239, 'd13': 2.701664},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 94""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 12:58:11 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 243,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1  *3 C 1 0 {3,S} {5,S} {6,S}
2     C 0 0 {4,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     O 0 2 {1,S} {2,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {5,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {2,S} {13,S} {14,S} {15,S}
5     O 0 2 {1,S} {2,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.287741, 'd12': 1.455335, 'd13': 2.74237},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 95""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 14:38:08 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 244,
    reactant1 = """
1 *1 C 0 0 {2,D} {3,S} {4,S}
2    C 0 0 {1,D} {5,S} {6,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {2,S}
6    H 0 0 {2,S}
""",
    reactant2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 0 {1,S} {2,S} {4,D}
4    O 0 2 {3,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    product1 = """
1    C 0 0 {2,D} {3,S} {4,S}
2 *3 C 1 0 {1,D} {5,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {2,S}
""",
    product2 = """
1  *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {5,D}
4  *2 H 0 0 {1,S}
5     O 0 2 {3,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.254446, 'd12': 1.464653, 'd13': 2.717863},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 96""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 13:50:22 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 245,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11 *2 H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.354599, 'd12': 1.353827, 'd13': 2.708409},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 97""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 14:50:38 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 246,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,S} {7,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
7    O 0 2 {2,D}
""",
    reactant2 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.4283, 'd12': 1.331478, 'd13': 2.756683},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 98""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 14:52:03 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 247,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,D} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.457569, 'd12': 1.309076, 'd13': 2.765122},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 99""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 14:51:10 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 248,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.359062, 'd12': 1.352875, 'd13': 2.711432},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 100""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:00:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 249,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.229832, 'd12': 1.330919, 'd13': 2.560671},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 101""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:05:43 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 250,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *3 O 1 2 {1,S}
5    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.280576, 'd12': 1.246807, 'd13': 2.526767},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 102""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:38:53 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 251,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,D} {4,S}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
4 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,D}
2    H 0 0 {1,S}
3    O 0 2 {1,D}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.45327, 'd12': 1.30392, 'd13': 2.755748},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 103""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:41:09 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 252,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.332136, 'd12': 1.210177, 'd13': 2.542273},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 104""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 16:37:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 253,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 0 {1,S} {3,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.355607, 'd12': 1.188088, 'd13': 2.543226},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 105""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 18:10:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 254,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,D} {5,S}
2 *3 C 1 0 {1,S} {4,S} {6,S}
3    C 0 0 {1,D} {7,S} {8,S}
4    O 0 2 {2,S} {9,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
9    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {3,D} {7,S}
3     C 0 0 {2,D} {8,S} {9,S}
4     O 0 2 {1,S} {10,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.271122, 'd12': 1.483497, 'd13': 2.75044},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 106""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 18:13:29 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 255,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {5,S} {9,S} {10,S}
4     C 0 0 {2,S} {5,S} {11,S} {12,S}
5     C 0 0 {3,S} {4,S} {13,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {5,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,S} {12,S} {13,S}
5     C 0 0 {3,S} {4,S} {14,S} {15,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.291399, 'd12': 1.418941, 'd13': 2.710328},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 107""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 20:18:23 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 256,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *3 C 1 0 {1,S} {6,S} {7,S}
3     C 0 0 {1,S} {8,S} {9,S} {10,S}
4     C 0 0 {1,S} {11,S} {12,S} {13,S}
5     C 0 0 {1,S} {14,S} {15,S} {16,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {1,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.333048, 'd12': 1.376535, 'd13': 2.708112},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 108""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 21:20:31 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 257,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {5,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,D}
3  *3 C 1 0 {4,S} {9,S} {10,S}
4     O 0 2 {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     O 0 2 {2,D}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {3,S} {5,S} {6,S} {7,S}
2  *1 C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {4,S} {11,D}
4     O 0 2 {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8  *2 H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    O 0 2 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.318788, 'd12': 1.38536, 'd13': 2.703903},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 109""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 20:36:48 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 258,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {3,S} {4,S} {8,D}
3  *3 C 1 0 {2,S} {9,S} {10,S}
4     O 0 2 {1,S} {2,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     O 0 2 {2,D}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {4,S} {11,D}
4     O 0 2 {2,S} {3,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    O 0 2 {3,D}
""",
    distances = DistanceData(
        distances = {'d23': 1.298579, 'd12': 1.403984, 'd13': 2.702172},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 110""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 20:33:32 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 259,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2 *3 C 1 0 {1,S} {3,S} {7,S}
3    C 0 0 {2,S} {8,D} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    O 0 2 {3,D}
9    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,D} {10,S}
4  *2 H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     O 0 2 {3,D}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.280278, 'd12': 1.453078, 'd13': 2.731984},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 111""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 21:48:00 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 260,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {7,S} {8,S}
3    C 0 0 {1,S} {6,D} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {3,D}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,D} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     O 0 2 {3,D}
10    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.364407, 'd12': 1.343187, 'd13': 2.707408},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 112""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 21:42:44 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 261,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1  *3 C 1 0 {3,S} {5,S} {6,S}
2     C 0 0 {4,S} {5,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     O 0 2 {1,S} {2,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1  *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {5,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {2,S} {13,S} {14,S} {15,S}
5     O 0 2 {1,S} {2,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.318758, 'd12': 1.421882, 'd13': 2.74022},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 113""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 23:58:59 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 262,
    reactant1 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    reactant2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    product1 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.346259, 'd12': 1.384498, 'd13': 2.730612},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 114""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 00:36:16 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 263,
    reactant1 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    O 0 2 {1,S} {3,S}
3 *1 O 0 2 {2,S} {7,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {3,S}
""",
    reactant2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *3 O 1 2 {2,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.34754, 'd12': 1.201517, 'd13': 2.547347},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 115""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 23:45:19 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 264,
    reactant1 = """
1    C 0 0 {2,S} {4,S} {5,S} {6,S}
2    O 0 2 {1,S} {3,S}
3 *1 O 0 2 {2,S} {7,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7 *2 H 0 0 {3,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 2 {1,S} {6,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *3 O 1 2 {2,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.404984, 'd12': 1.152543, 'd13': 2.557307},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 116""",
    longDesc = 
u"""
""",
    history = [
        ('Wed May 21 23:54:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 265,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7  *2 H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.360934, 'd12': 1.356039, 'd13': 2.716761},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 117""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 01:10:15 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 266,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,D} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.408127, 'd12': 1.351842, 'd13': 2.756651},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 118""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 00:30:38 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 267,
    reactant1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,D} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7 *2 H 0 0 {2,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.461382, 'd12': 1.307129, 'd13': 2.768218},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 119""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 00:35:12 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 268,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {1,S} {13,S} {14,S} {15,S}
5     O 0 2 {1,S} {6,S}
6  *3 O 1 2 {5,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {11,S} {12,S} {13,S}
4     C 0 0 {1,S} {14,S} {15,S} {16,S}
5     O 0 2 {1,S} {6,S}
6  *1 O 0 2 {5,S} {7,S}
7  *2 H 0 0 {6,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.113429, 'd12': 1.453162, 'd13': 2.565773},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 120""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 01:22:15 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 269,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8  *2 H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,D} {6,S}
3    C 0 0 {2,D} {7,S} {8,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {3,S}
8    H 0 0 {3,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.286944, 'd12': 1.44811, 'd13': 2.734005},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 121""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 04:42:11 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 270,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {5,S} {9,S} {10,S}
4     C 0 0 {2,S} {5,S} {11,S} {12,S}
5     C 0 0 {3,S} {4,S} {13,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {5,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,S} {12,S} {13,S}
5     C 0 0 {3,S} {4,S} {14,S} {15,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.322772, 'd12': 1.389466, 'd13': 2.712125},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 122""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 04:39:04 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 271,
    reactant1 = """
1    O 0 2 {2,S} {3,S}
2 *1 O 0 2 {1,S} {4,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {2,S}
""",
    reactant2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {5,S} {9,S} {10,S}
4     C 0 0 {2,S} {5,S} {11,S} {12,S}
5     C 0 0 {3,S} {4,S} {13,S} {14,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {5,S}
14    H 0 0 {5,S}
""",
    product1 = """
1    O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *3 O 1 2 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,S} {12,S} {13,S}
5     C 0 0 {3,S} {4,S} {14,S} {15,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.347002, 'd12': 1.195943, 'd13': 2.542942},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 123""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 03:53:49 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 272,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1  *3 C 1 0 {4,S} {7,S} {8,S}
2     C 0 0 {5,S} {9,S} {10,S} {11,S}
3     C 0 0 {4,S} {5,S} {6,D}
4     O 0 2 {1,S} {3,S}
5     O 0 2 {2,S} {3,S}
6     O 0 2 {3,D}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {4,S} {6,S} {8,S} {9,S}
2     C 0 0 {5,S} {10,S} {11,S} {12,S}
3     C 0 0 {4,S} {5,S} {7,D}
4     O 0 2 {1,S} {3,S}
5     O 0 2 {2,S} {3,S}
6  *2 H 0 0 {1,S}
7     O 0 2 {3,D}
8     H 0 0 {1,S}
9     H 0 0 {1,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.321991, 'd12': 1.382092, 'd13': 2.703748},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 124""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 03:50:14 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 273,
    reactant1 = """
1 *1 O 0 2 {2,S} {3,S}
2    H 0 0 {1,S}
3 *2 H 0 0 {1,S}
""",
    reactant2 = """
1  *3 C 1 0 {2,B} {3,B}
2     C 0 0 {1,B} {4,B} {7,S}
3     C 0 0 {1,B} {5,B} {8,S}
4     C 0 0 {2,B} {6,B} {9,S}
5     C 0 0 {3,B} {6,B} {10,S}
6     C 0 0 {4,B} {5,B} {11,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
11    H 0 0 {6,S}
""",
    product1 = """
1    H 0 0 {2,S}
2 *3 O 1 2 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,B} {3,B} {7,S}
2     C 0 0 {1,B} {4,B} {8,S}
3     C 0 0 {1,B} {5,B} {9,S}
4     C 0 0 {2,B} {6,B} {10,S}
5     C 0 0 {3,B} {6,B} {11,S}
6     C 0 0 {4,B} {5,B} {12,S}
7  *2 H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
12    H 0 0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.243519, 'd12': 1.259028, 'd13': 2.490608},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 125""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 04:52:55 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 274,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    reactant2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,D}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 0 {1,S} {6,D} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7 *2 H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.205245, 'd12': 1.405721, 'd13': 2.603715},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 126""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 09:08:12 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 275,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    reactant2 = """
1 *3 C 1 0 {2,S} {4,S} {5,S}
2    C 0 0 {1,S} {3,D} {6,S}
3    O 0 2 {2,D}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,D} {7,S}
3 *2 H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    O 0 2 {2,D}
7    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.278589, 'd12': 1.25767, 'd13': 2.534594},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 127""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 09:28:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 276,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8  *2 H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    reactant2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.321875, 'd12': 1.410864, 'd13': 2.730185},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 128""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 10:59:27 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 277,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 0 {1,S} {6,S} {7,S} {8,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
""",
    reactant2 = """
1  *3 C 1 0 {2,S} {3,S} {7,S}
2     C 0 0 {1,S} {4,S} {8,S} {9,S}
3     C 0 0 {1,S} {5,S} {10,S} {11,S}
4     C 0 0 {2,S} {6,S} {12,S} {13,S}
5     C 0 0 {3,S} {6,D} {14,S}
6     C 0 0 {4,S} {5,D} {15,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {6,S}
""",
    product1 = """
1    C 0 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 0 {1,S} {6,S} {7,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6    H 0 0 {2,S}
7    H 0 0 {2,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 0 {1,S} {4,S} {9,S} {10,S}
3     C 0 0 {1,S} {5,S} {11,S} {12,S}
4     C 0 0 {2,S} {6,S} {13,S} {14,S}
5     C 0 0 {3,S} {6,D} {15,S}
6     C 0 0 {4,S} {5,D} {16,S}
7  *2 H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.341899, 'd12': 1.370231, 'd13': 2.712072},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 129""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 11:43:26 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 278,
    reactant1 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *3 C 1 0 {1,S} {6,S} {7,S}
3     C 0 0 {1,S} {8,S} {9,S} {10,S}
4     C 0 0 {1,S} {11,S} {12,S} {13,S}
5     C 0 0 {1,S} {14,S} {15,S} {16,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
""",
    product1 = """
1     C 0 0 {3,S} {4,S} {5,S} {6,S}
2     C 0 0 {3,S} {7,S} {8,S} {9,S}
3  *3 C 1 0 {1,S} {2,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {1,S} {15,S} {16,S} {17,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.390728, 'd12': 1.33492, 'd13': 2.723733},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 130""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 16:54:12 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 279,
    reactant1 = """
1 *1 C 0 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 0 {1,S} {3,D} {7,S}
3    C 0 0 {2,D} {8,S} {9,S}
4    H 0 0 {1,S}
5    H 0 0 {1,S}
6 *2 H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {3,S}
9    H 0 0 {3,S}
""",
    reactant2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,D} {7,S}
3     C 0 0 {1,S} {5,D} {8,S}
4     C 0 0 {2,D} {5,S} {9,S}
5     C 0 0 {3,D} {4,S} {10,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
""",
    product1 = """
1    H 0 0 {2,S}
2 *3 C 1 0 {1,S} {3,S} {4,S}
3    C 0 0 {2,S} {5,S} {6,D}
4    H 0 0 {2,S}
5    H 0 0 {3,S}
6    C 0 0 {3,D} {7,S} {8,S}
7    H 0 0 {6,S}
8    H 0 0 {6,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,D} {8,S}
3     C 0 0 {1,S} {5,D} {9,S}
4     C 0 0 {2,D} {5,S} {10,S}
5     C 0 0 {3,D} {4,S} {11,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.337615, 'd12': 1.391177, 'd13': 2.727653},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 131""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 13:43:36 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 280,
    reactant1 = """
1    H 0 0 {2,S}
2    C 0 0 {1,S} {3,T}
3    C 0 0 {2,T} {4,S}
4 *1 C 0 0 {3,S} {5,S} {6,S} {7,S}
5 *2 H 0 0 {4,S}
6    H 0 0 {4,S}
7    H 0 0 {4,S}
""",
    reactant2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,D} {7,S}
3     C 0 0 {1,S} {5,D} {8,S}
4     C 0 0 {2,D} {5,S} {9,S}
5     C 0 0 {3,D} {4,S} {10,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
""",
    product1 = """
1    H 0 0 {2,S}
2    C 0 0 {1,S} {3,T}
3    C 0 0 {2,T} {4,S}
4 *3 C 1 0 {3,S} {5,S} {6,S}
5    H 0 0 {4,S}
6    H 0 0 {4,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,D} {8,S}
3     C 0 0 {1,S} {5,D} {9,S}
4     C 0 0 {2,D} {5,S} {10,S}
5     C 0 0 {3,D} {4,S} {11,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.314561, 'd12': 1.415978, 'd13': 2.730215},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 132""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 13:56:57 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 281,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7  *2 H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {6,S} {7,S}
2  *3 C 1 0 {1,S} {4,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {5,D} {12,S}
5     O 0 2 {4,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     H 0 0 {1,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {7,S} {8,S}
2  *1 C 0 0 {1,S} {4,S} {5,S} {9,S}
3     C 0 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 0 {2,S} {6,D} {13,S}
5  *2 H 0 0 {2,S}
6     O 0 2 {4,D}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.286158, 'd12': 1.454247, 'd13': 2.739153},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 133""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 16:47:41 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 282,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {8,S} {9,S} {10,S}
2  *3 C 1 0 {1,S} {3,S} {4,S}
3     C 0 0 {2,S} {5,D} {12,S}
4     C 0 0 {2,S} {6,D} {13,S}
5     C 0 0 {3,D} {7,S} {14,S}
6     C 0 0 {4,D} {7,S} {15,S}
7     C 0 0 {5,S} {6,S} {11,D}
8     H 0 0 {1,S}
9     H 0 0 {1,S}
10    H 0 0 {1,S}
11    O 0 2 {7,D}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {6,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {8,S}
2     C 0 0 {1,S} {9,S} {10,S} {11,S}
3     C 0 0 {1,S} {5,D} {12,S}
4     C 0 0 {1,S} {6,D} {13,S}
5     C 0 0 {3,D} {7,S} {15,S}
6     C 0 0 {4,D} {7,S} {16,S}
7     C 0 0 {5,S} {6,S} {14,D}
8  *2 H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    O 0 2 {7,D}
15    H 0 0 {5,S}
16    H 0 0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.210734, 'd12': 1.627066, 'd13': 2.837081},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 134""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 18:59:46 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 283,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    reactant2 = """
1 *3 C 1 0 {3,S} {5,S} {6,S}
2    C 0 0 {3,S} {7,S} {8,S} {9,S}
3    C 0 0 {1,S} {2,S} {4,D}
4    O 0 2 {3,D}
5    H 0 0 {1,S}
6    H 0 0 {1,S}
7    H 0 0 {2,S}
8    H 0 0 {2,S}
9    H 0 0 {2,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1  *1 C 0 0 {3,S} {4,S} {6,S} {7,S}
2     C 0 0 {3,S} {8,S} {9,S} {10,S}
3     C 0 0 {1,S} {2,S} {5,D}
4  *2 H 0 0 {1,S}
5     O 0 2 {3,D}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.279753, 'd12': 1.254681, 'd13': 2.532874},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 135""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 22:20:02 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 284,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    reactant2 = """
1     C 0 0 {4,S} {5,S} {6,S} {7,S}
2     C 0 0 {4,S} {8,S} {9,S} {10,S}
3     C 0 0 {4,S} {11,S} {12,S} {13,S}
4  *3 C 1 0 {1,S} {2,S} {3,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.251585, 'd12': 1.318814, 'd13': 2.554427},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 136""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 22:58:02 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 285,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {1,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6  *2 H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.288264, 'd12': 1.245048, 'd13': 2.531537},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 137""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 01:47:56 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 286,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4 *2 H 0 0 {1,S}
5    H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,B} {3,B} {8,S}
2     C 0 0 {1,B} {5,B} {9,S}
3     C 0 0 {1,B} {6,B} {10,S}
4     C 0 0 {5,B} {6,B} {11,S}
5     C 0 0 {2,B} {4,B} {12,S}
6     C 0 0 {3,B} {4,B} {13,S}
7  *3 C 1 0 {8,S} {14,S} {15,S}
8     O 0 2 {1,S} {7,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {5,S}
13    H 0 0 {6,S}
14    H 0 0 {7,S}
15    H 0 0 {7,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1  *1 C 0 0 {8,S} {9,S} {10,S} {11,S}
2     C 0 0 {3,B} {4,B} {8,S}
3     C 0 0 {2,B} {6,B} {12,S}
4     C 0 0 {2,B} {7,B} {13,S}
5     C 0 0 {6,B} {7,B} {14,S}
6     C 0 0 {3,B} {5,B} {15,S}
7     C 0 0 {4,B} {5,B} {16,S}
8     O 0 2 {1,S} {2,S}
9  *2 H 0 0 {1,S}
10    H 0 0 {1,S}
11    H 0 0 {1,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {6,S}
16    H 0 0 {7,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.311451, 'd12': 1.4136, 'd13': 2.724572},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 138""",
    longDesc = 
u"""
""",
    history = [
        ('Thu May 22 21:32:44 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 287,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {4,S} {5,S} {6,S}
2     C 0 0 {1,S} {7,S} {8,S} {9,S}
3     C 0 0 {4,S} {10,S} {11,S} {12,S}
4  *3 C 1 0 {1,S} {3,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {2,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5  *2 H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.264185, 'd12': 1.286517, 'd13': 2.546171},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 139""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 00:37:13 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 288,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 0 {2,S} {12,S} {13,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 0 {1,S} {4,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {2,S} {12,S} {13,S} {14,S}
5     H 0 0 {1,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.284317, 'd12': 1.247176, 'd13': 2.529051},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 140""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 01:45:03 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 289,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 0 {1,S} {9,S} {10,S}
4     C 0 0 {1,S} {11,S} {12,S} {13,S}
5     C 0 0 {1,S} {14,S} {15,S} {16,S}
6     C 0 0 {2,S} {17,S} {18,S} {19,S}
7     C 0 0 {2,S} {20,S} {21,S} {22,S}
8     C 0 0 {2,S} {23,S} {24,S} {25,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {4,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {5,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {6,S}
18    H 0 0 {6,S}
19    H 0 0 {6,S}
20    H 0 0 {7,S}
21    H 0 0 {7,S}
22    H 0 0 {7,S}
23    H 0 0 {8,S}
24    H 0 0 {8,S}
25    H 0 0 {8,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3  *1 C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5     C 0 0 {1,S} {15,S} {16,S} {17,S}
6     C 0 0 {2,S} {18,S} {19,S} {20,S}
7     C 0 0 {2,S} {21,S} {22,S} {23,S}
8     C 0 0 {2,S} {24,S} {25,S} {26,S}
9  *2 H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {5,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
18    H 0 0 {6,S}
19    H 0 0 {6,S}
20    H 0 0 {6,S}
21    H 0 0 {7,S}
22    H 0 0 {7,S}
23    H 0 0 {7,S}
24    H 0 0 {8,S}
25    H 0 0 {8,S}
26    H 0 0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.333337, 'd12': 1.379587, 'd13': 2.706613},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 141""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 08:06:55 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 290,
    reactant1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 0 {2,S}
4     C 0 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 0 {2,S}
6     C 0 0 {4,S} {9,S} {10,S} {11,S}
7     C 0 0 {4,S} {12,S} {13,S} {14,S}
8     C 0 0 {4,S} {15,S} {16,S} {17,S}
9     H 0 0 {6,S}
10    H 0 0 {6,S}
11    H 0 0 {6,S}
12    H 0 0 {7,S}
13    H 0 0 {7,S}
14    H 0 0 {7,S}
15    O 0 2 {8,S} {18,S}
16    H 0 0 {8,S}
17    H 0 0 {8,S}
18 *1 O 0 2 {15,S} {19,S}
19 *2 H 0 0 {18,S}
""",
    reactant2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    product1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 0 {2,S}
4     H 0 0 {2,S}
5     C 0 0 {2,S} {6,S} {7,S} {8,S}
6     C 0 0 {5,S} {9,S} {10,S} {11,S}
7     C 0 0 {5,S} {12,S} {13,S} {14,S}
8     C 0 0 {5,S} {15,S} {16,S} {17,S}
9     H 0 0 {6,S}
10    O 0 2 {6,S} {18,S}
11    H 0 0 {6,S}
12    H 0 0 {7,S}
13    H 0 0 {7,S}
14    H 0 0 {7,S}
15    H 0 0 {8,S}
16    H 0 0 {8,S}
17    H 0 0 {8,S}
18 *3 O 1 2 {10,S}
""",
    product2 = """
1 *1 O 0 2 {2,S} {3,S}
2    O 1 2 {1,S}
3 *2 H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.094942, 'd12': 1.345438, 'd13': 2.436127},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 142""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 04:47:09 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 291,
    reactant1 = """
1     H 0 0 {2,S}
2     O 0 2 {1,S} {3,S}
3     C 0 0 {2,S} {4,S} {5,S} {6,S}
4     C 0 0 {3,S} {7,S} {8,S} {9,S}
5     C 0 0 {3,S} {10,S} {11,S} {12,S}
6     C 0 0 {3,S} {13,S} {14,S} {15,S}
7     O 0 2 {4,S} {16,S}
8     H 0 0 {4,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
11    H 0 0 {5,S}
12    H 0 0 {5,S}
13    H 0 0 {6,S}
14    H 0 0 {6,S}
15    H 0 0 {6,S}
16 *1 O 0 2 {7,S} {17,S}
17 *2 H 0 0 {16,S}
""",
    reactant2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    product1 = """
1     H 0 0 {2,S}
2     O 0 2 {1,S} {3,S}
3     C 0 0 {2,S} {4,S} {5,S} {6,S}
4     C 0 0 {3,S} {7,S} {8,S} {9,S}
5     C 0 0 {3,S} {10,S} {11,S} {12,S}
6     C 0 0 {3,S} {13,S} {14,S} {15,S}
7     H 0 0 {4,S}
8     H 0 0 {4,S}
9     H 0 0 {4,S}
10    O 0 2 {5,S} {16,S}
11    H 0 0 {5,S}
12    H 0 0 {5,S}
13    H 0 0 {6,S}
14    H 0 0 {6,S}
15    H 0 0 {6,S}
16 *3 O 1 2 {10,S}
""",
    product2 = """
1 *1 O 0 2 {2,S} {3,S}
2    O 1 2 {1,S}
3 *2 H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.060269, 'd12': 1.420877, 'd13': 2.465326},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 143""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 06:24:58 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 292,
    reactant1 = """
1  *2 H 0 0 {2,S}
2  *1 O 0 2 {1,S} {3,S}
3     O 0 2 {2,S} {4,S}
4     C 0 0 {3,S} {5,S} {6,S} {7,S}
5     H 0 0 {4,S}
6     C 0 0 {4,S} {8,S} {9,S} {10,S}
7     C 0 0 {4,S} {11,S} {12,S} {13,S}
8     H 0 0 {6,S}
9     C 0 0 {6,S} {14,S} {15,S} {16,S}
10    H 0 0 {6,S}
11    H 0 0 {7,S}
12    C 0 0 {7,S} {15,S} {17,S} {18,S}
13    H 0 0 {7,S}
14    H 0 0 {9,S}
15    C 0 0 {9,S} {12,S} {19,S} {20,S}
16    H 0 0 {9,S}
17    H 0 0 {12,S}
18    H 0 0 {12,S}
19    H 0 0 {15,S}
20    H 0 0 {15,S}
""",
    reactant2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    product1 = """
1 *1 O 0 2 {2,S} {3,S}
2 *2 H 0 0 {1,S}
3    O 1 2 {1,S}
""",
    product2 = """
1     C 0 0 {2,S} {3,S} {7,S} {9,S}
2     C 0 0 {1,S} {5,S} {10,S} {11,S}
3     C 0 0 {1,S} {6,S} {12,S} {13,S}
4     C 0 0 {5,S} {6,S} {14,S} {15,S}
5     C 0 0 {2,S} {4,S} {16,S} {17,S}
6     C 0 0 {3,S} {4,S} {18,S} {19,S}
7     O 0 2 {1,S} {8,S}
8  *3 O 1 2 {7,S}
9     H 0 0 {1,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
18    H 0 0 {6,S}
19    H 0 0 {6,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.066347, 'd12': 1.405068, 'd13': 2.461135},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 144""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 16:45:44 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 293,
    reactant1 = """
1 *1 C 0 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
5 *2 H 0 0 {1,S}
""",
    reactant2 = """
1     C 0 0 {3,S} {4,S} {5,S} {9,S}
2     C 0 0 {6,S} {7,S} {8,S} {10,S}
3  *3 C 1 0 {1,S} {11,S} {12,S}
4     C 0 0 {1,S} {13,S} {14,S} {15,S}
5     C 0 0 {1,S} {16,S} {17,S} {18,S}
6     C 0 0 {2,S} {19,S} {20,S} {21,S}
7     C 0 0 {2,S} {22,S} {23,S} {24,S}
8     C 0 0 {2,S} {25,S} {26,S} {27,S}
9     O 0 2 {1,S} {10,S}
10    O 0 2 {2,S} {9,S}
11    H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {5,S}
17    H 0 0 {5,S}
18    H 0 0 {5,S}
19    H 0 0 {6,S}
20    H 0 0 {6,S}
21    H 0 0 {6,S}
22    H 0 0 {7,S}
23    H 0 0 {7,S}
24    H 0 0 {7,S}
25    H 0 0 {8,S}
26    H 0 0 {8,S}
27    H 0 0 {8,S}
""",
    product1 = """
1 *3 C 1 0 {2,S} {3,S} {4,S}
2    H 0 0 {1,S}
3    H 0 0 {1,S}
4    H 0 0 {1,S}
""",
    product2 = """
1     C 0 0 {3,S} {4,S} {5,S} {9,S}
2     C 0 0 {6,S} {7,S} {8,S} {10,S}
3  *1 C 0 0 {1,S} {11,S} {12,S} {13,S}
4     C 0 0 {1,S} {14,S} {15,S} {16,S}
5     C 0 0 {1,S} {17,S} {18,S} {19,S}
6     C 0 0 {2,S} {20,S} {21,S} {22,S}
7     C 0 0 {2,S} {23,S} {24,S} {25,S}
8     C 0 0 {2,S} {26,S} {27,S} {28,S}
9     O 0 2 {1,S} {10,S}
10    O 0 2 {2,S} {9,S}
11 *2 H 0 0 {3,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {4,S}
15    H 0 0 {4,S}
16    H 0 0 {4,S}
17    H 0 0 {5,S}
18    H 0 0 {5,S}
19    H 0 0 {5,S}
20    H 0 0 {6,S}
21    H 0 0 {6,S}
22    H 0 0 {6,S}
23    H 0 0 {7,S}
24    H 0 0 {7,S}
25    H 0 0 {7,S}
26    H 0 0 {8,S}
27    H 0 0 {8,S}
28    H 0 0 {8,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.339148, 'd12': 1.362866, 'd13': 2.70112},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 145""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 21:49:08 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 294,
    reactant1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,B} {4,B}
3     C 0 0 {2,B} {5,B} {6,S}
4  *1 C 0 0 {2,B} {7,S} {8,B}
5     C 0 0 {3,B} {9,B} {10,S}
6     H 0 0 {3,S}
7  *2 H 0 0 {4,S}
8     C 0 0 {4,B} {9,B} {11,S}
9     C 0 0 {5,B} {8,B} {12,S}
10    H 0 0 {5,S}
11    H 0 0 {8,S}
12    H 0 0 {9,S}
""",
    reactant2 = """
1  *3 C 1 0 {2,S} {3,S} {6,S}
2     C 0 0 {1,S} {4,D} {7,S}
3     C 0 0 {1,S} {5,D} {8,S}
4     C 0 0 {2,D} {5,S} {9,S}
5     C 0 0 {3,D} {4,S} {10,S}
6     H 0 0 {1,S}
7     H 0 0 {2,S}
8     H 0 0 {3,S}
9     H 0 0 {4,S}
10    H 0 0 {5,S}
""",
    product1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,B} {4,B}
3  *3 C 1 0 {2,B} {5,B}
4     C 0 0 {2,B} {6,B} {7,S}
5     C 0 0 {3,B} {8,B} {9,S}
6     C 0 0 {4,B} {8,B} {10,S}
7     H 0 0 {4,S}
8     C 0 0 {5,B} {6,B} {11,S}
9     H 0 0 {5,S}
10    H 0 0 {6,S}
11    H 0 0 {8,S}
""",
    product2 = """
1  *1 C 0 0 {2,S} {3,S} {6,S} {7,S}
2     C 0 0 {1,S} {4,D} {8,S}
3     C 0 0 {1,S} {5,D} {9,S}
4     C 0 0 {2,D} {5,S} {10,S}
5     C 0 0 {3,D} {4,S} {11,S}
6  *2 H 0 0 {1,S}
7     H 0 0 {1,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {4,S}
11    H 0 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.207705, 'd12': 1.585963, 'd13': 2.793668},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 146""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 18:50:21 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 295,
    reactant1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *1 O 0 2 {1,S} {15,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
15 *2 H 0 0 {5,S}
""",
    reactant2 = """
1  *3 C 1 0 {5,S} {7,S} {8,S}
2     C 0 0 {5,S} {9,S} {10,S} {11,S}
3     C 0 0 {6,S} {12,S} {13,S} {14,S}
4     C 0 0 {6,S} {15,S} {16,S} {17,S}
5     C 0 0 {1,S} {2,S} {6,D}
6     C 0 0 {3,S} {4,S} {5,D}
7     H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {2,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {3,S}
13    H 0 0 {3,S}
14    H 0 0 {3,S}
15    H 0 0 {4,S}
16    H 0 0 {4,S}
17    H 0 0 {4,S}
""",
    product1 = """
1     C 0 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 0 {1,S} {9,S} {10,S} {11,S}
4     C 0 0 {1,S} {12,S} {13,S} {14,S}
5  *3 O 1 2 {1,S}
6     H 0 0 {2,S}
7     H 0 0 {2,S}
8     H 0 0 {2,S}
9     H 0 0 {3,S}
10    H 0 0 {3,S}
11    H 0 0 {3,S}
12    H 0 0 {4,S}
13    H 0 0 {4,S}
14    H 0 0 {4,S}
""",
    product2 = """
1  *1 C 0 0 {5,S} {7,S} {8,S} {9,S}
2     C 0 0 {5,S} {10,S} {11,S} {12,S}
3     C 0 0 {6,S} {13,S} {14,S} {15,S}
4     C 0 0 {6,S} {16,S} {17,S} {18,S}
5     C 0 0 {1,S} {2,S} {6,D}
6     C 0 0 {3,S} {4,S} {5,D}
7  *2 H 0 0 {1,S}
8     H 0 0 {1,S}
9     H 0 0 {1,S}
10    H 0 0 {2,S}
11    H 0 0 {2,S}
12    H 0 0 {2,S}
13    H 0 0 {3,S}
14    H 0 0 {3,S}
15    H 0 0 {3,S}
16    H 0 0 {4,S}
17    H 0 0 {4,S}
18    H 0 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.217391, 'd12': 1.387594, 'd13': 2.604205},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 147""",
    longDesc = 
u"""
""",
    history = [
        ('Sat May 24 09:29:52 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

entry(
    index = 296,
    reactant1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,B} {4,B}
3     C 0 0 {2,B} {5,S} {6,B}
4     C 0 0 {2,B} {7,S} {8,B}
5     H 0 0 {3,S}
6     C 0 0 {3,B} {9,B} {10,S}
7     H 0 0 {4,S}
8     C 0 0 {4,B} {9,B} {11,S}
9     C 0 0 {6,B} {8,B} {12,S}
10    C 0 0 {6,S} {13,S} {14,S} {15,S}
11    H 0 0 {8,S}
12    H 0 0 {9,S}
13    O 0 2 {10,S} {16,S}
14    H 0 0 {10,S}
15    H 0 0 {10,S}
16 *1 O 0 2 {13,S} {17,S}
17 *2 H 0 0 {16,S}
""",
    reactant2 = """
1 *3 O 1 2 {2,S}
2    O 1 2 {1,S}
""",
    product1 = """
1     H 0 0 {2,S}
2     C 0 0 {1,S} {3,B} {4,B}
3     C 0 0 {2,B} {5,S} {6,B}
4     C 0 0 {2,B} {7,S} {8,B}
5     H 0 0 {3,S}
6     C 0 0 {3,B} {9,S} {10,B}
7     H 0 0 {4,S}
8     C 0 0 {4,B} {10,B} {11,S}
9     C 0 0 {6,S} {12,S} {13,S} {14,S}
10    C 0 0 {6,B} {8,B} {15,S}
11    H 0 0 {8,S}
12    H 0 0 {9,S}
13    H 0 0 {9,S}
14    O 0 2 {9,S} {16,S}
15    H 0 0 {10,S}
16 *3 O 1 2 {14,S}
""",
    product2 = """
1 *1 O 0 2 {2,S} {3,S}
2    O 1 2 {1,S}
3 *2 H 0 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d23': 1.076901, 'd12': 1.374965, 'd13': 2.450556},
        method = "B3LYP/6-31+G(d,p)",
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Reverse reaction for reaction index 148""",
    longDesc = 
u"""
""",
    history = [
        ('Fri May 23 21:44:58 2014', 'Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>', 'action', 'Found via group additive estimation by the automatic transition state generator'),
    ],
)

