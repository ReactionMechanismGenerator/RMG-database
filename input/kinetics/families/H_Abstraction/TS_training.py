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
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.895297060023', 'd13': '2.30303210246', 'd23': '1.40773504244'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct  3 16:15:59 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.930299051641', 'd13': '2.28893519078', 'd23': '1.35892133446'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct  4 13:03:20 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.907894558278', 'd13': '2.10402794429', 'd23': '1.20216645606'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct  3 19:11:41 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,D}
2 *2 H 0 {1,S}
3    O 0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.15309849454', 'd13': '2.37290946709', 'd23': '1.21988501633'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct  3 21:06:25 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,D}
2 *1 C 0 {1,D} {3,S}
3 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.862862296846', 'd13': '2.32579722591', 'd23': '1.46347894682'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct  4 14:36:06 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.11574127633', 'd13': '2.1796554827', 'd23': '1.06757172779'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct  3 23:15:02 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.36413844572', 'd13': '2.29011119802', 'd23': '0.926273983824'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sat Oct  5 07:17:14 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,D}
2 *3 C 1 {1,S}
3    C 0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.23289966705', 'd13': '2.31166939106', 'd23': '1.08060600298'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sat Oct  5 21:39:01 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    O 0 {1,S} {3,S}
3 *3 O 1 {2,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S}
2    O 0 {1,S} {3,S}
3 *1 O 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.17928080736', 'd13': '2.22345150147', 'd23': '1.04828664688'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct  6 05:11:10 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,D}
3    O 0 {2,D}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3 *2 H 0 {2,S}
4    O 0 {2,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.23398956601', 'd13': '2.42765010692', 'd23': '1.19436701782'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct  6 06:31:12 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3 *1 C 0 {2,D} {4,S}
4 *2 H 0 {3,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3 *3 C 1 {2,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.47813602871', 'd13': '2.33353250223', 'd23': '0.856116451331'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct  6 08:26:17 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D} {4,S}
3    C 0 {2,D}
4 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,D}
3 *3 C 1 {1,S} {2,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.41348718108', 'd13': '2.3037243324', 'd23': '0.890380160538'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct  6 10:45:23 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S}
4    C 0 {2,S}
5 *2 H 0 {3,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *3 C 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.36327979666', 'd13': '2.29221727048', 'd23': '0.929233924724'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Oct  7 07:11:14 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3 *1 C 0 {1,D} {5,S}
4    C 0 {2,D}
5 *2 H 0 {3,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3    C 0 {1,D}
4 *3 C 1 {2,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.47462637073', 'd13': '2.33091998893', 'd23': '0.857297575577'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Oct  7 12:18:12 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 15,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {3,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.974384887201', 'd13': '2.28142288545', 'd23': '1.30720965209'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Oct  8 10:23:39 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 16,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S}
4    O 0 {2,S}
5 *2 H 0 {3,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *3 C 1 {1,S}
4    O 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.36776843715', 'd13': '2.2968743381', 'd23': '0.929232557334'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct 10 22:36:03 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {3,S} {4,S}
2    C 0 {3,S} {5,D}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
5    O 0 {2,D}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {3,S}
2    C 0 {3,S} {4,D}
3    O 0 {1,S} {2,S}
4    O 0 {2,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.32911528045', 'd13': '2.28383585417', 'd23': '0.955049619099'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 11 00:52:04 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 18,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4 *3 C 1 {2,S} {3,D}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4 *1 C 0 {2,S} {3,D} {5,S}
5 *2 H 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.887625561499', 'd13': '2.30400248858', 'd23': '1.41659613444'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 11 07:52:33 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *1 C 0 {2,S} {6,S}
5    O 0 {3,S}
6 *2 H 0 {4,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *3 C 1 {2,S}
5    O 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.35777238782', 'd13': '2.28701840306', 'd23': '0.929562714059'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 11 22:27:35 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {1,S}
6 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5    O 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.36923344491', 'd13': '2.29270714272', 'd23': '0.923478017904'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sat Oct 12 13:28:20 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 C 0 {2,S} {6,S}
6 *2 H 0 {5,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *3 C 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.36286435818', 'd13': '2.28958345535', 'd23': '0.927276316146'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct 13 02:56:15 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {5,S}
5 *3 C 1 {1,S} {4,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.31339574095', 'd13': '2.28396108373', 'd23': '0.970596361047'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct 13 18:16:24 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {6,S}
3    C 0 {1,S} {5,S}
4    C 0 {2,S}
5    C 0 {3,S}
6 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {5,S}
5 *3 C 1 {2,S} {4,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.30507883057', 'd13': '2.28125066263', 'd23': '0.976300411313'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Oct 14 20:11:44 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *3 C 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.37805888248', 'd13': '2.29790558097', 'd23': '0.919883004244'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Oct 23 23:13:03 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 H 0 {3,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {5,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *3 C 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.37106798486', 'd13': '2.29850984591', 'd23': '0.92744513748'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct 24 19:10:33 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 26,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6    C 0 {4,B} {5,B}
7 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,B} {3,B}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6 *3 C 1 {4,B} {5,B}
""",
    distances = DistanceData(
        distances = {'d12': '1.4930819397', 'd13': '2.34311603157', 'd23': '0.850034093713'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 25 07:16:46 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 27,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {5,B}
3    C 0 {1,B} {6,B}
4    C 0 {5,B} {6,B}
5    C 0 {2,B} {4,B}
6    C 0 {3,B} {4,B}
7 *1 O 0 {1,S} {8,S}
8 *2 H 0 {7,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {5,B}
3    C 0 {1,B} {6,B}
4    C 0 {5,B} {6,B}
5    C 0 {2,B} {4,B}
6    C 0 {3,B} {4,B}
7 *3 O 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.08110686108', 'd13': '2.16027024006', 'd23': '1.08657681722'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 25 21:17:19 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 28,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {9,S}
3    C 0 {1,S} {4,B} {5,B}
4    C 0 {3,B} {7,B}
5    C 0 {3,B} {8,B}
6    C 0 {7,B} {8,B}
7    C 0 {4,B} {6,B}
8    C 0 {5,B} {6,B}
9 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {8,S}
2    C 0 {1,S} {3,B} {4,B}
3    C 0 {2,B} {6,B}
4    C 0 {2,B} {7,B}
5    C 0 {6,B} {7,B}
6    C 0 {3,B} {5,B}
7    C 0 {4,B} {5,B}
8 *3 C 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.36787122418', 'd13': '2.29107401551', 'd23': '0.923728822558'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct 27 06:17:26 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 29,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.33014', 'd13': '2.70895', 'd23': '1.37890'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 30,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3    O 0 {2,S}
4 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    O 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.28923', 'd13': '2.73121', 'd23': '1.44233'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 31,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *1 O 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *3 O 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.20569', 'd13': '2.51006', 'd23': '1.30536'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 32,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.40355', 'd13': '2.54716', 'd23': '1.14362'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 33,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3    O 0 {2,S}
4 *2 H 0 {2,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    O 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.32319', 'd13': '2.54544', 'd23': '1.22242'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 34,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *1 O 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *3 O 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.27899', 'd13': '2.34834', 'd23': '1.10392'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 35,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.32326', 'd13': '2.70269', 'd23': '1.37951'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 36,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.38612', 'd13': '2.54409', 'd23': '1.15831'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 37,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *1 C 0 {1,D} {3,S}
3 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.37209', 'd13': '2.68374', 'd23': '1.31192'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 38,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *1 C 0 {1,S} {3,S} {5,S}
5 *2 H 0 {4,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *3 C 1 {1,S} {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.31082', 'd13': '2.70089', 'd23': '1.39021'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 39,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    O 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S} {3,S}
2    O 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.33957', 'd13': '2.69461', 'd23': '1.35719'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 40,
    reactant1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    O 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S} {3,S}
2    O 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.37733', 'd13': '2.70362', 'd23': '1.32993'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 41,
    reactant1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    O 0 {1,S} {3,S}
3    C 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S} {3,S}
2    O 0 {1,S} {3,S}
3    C 0 {1,S} {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.36697', 'd13': '2.70329', 'd23': '1.33663'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 42,
    reactant1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {3,S}
3    C 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S} {3,S}
2    C 0 {1,S} {3,S}
3    C 0 {1,S} {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.38471', 'd13': '2.69157', 'd23': '1.30692'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 43,
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.18856', 'd13': '2.58134', 'd23': '1.39456'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 44,
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *1 O 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *3 O 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.05831', 'd13': '2.28959', 'd23': '1.32977'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 45,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1
""",
    distances = DistanceData(
        distances = {'d12': '1.40773504244', 'd13': '2.30303210246', 'd23': '0.895297060023'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct  3 16:15:59 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 46,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.35892133446', 'd13': '2.28893519078', 'd23': '0.930299051641'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct  4 13:03:20 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 47,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 O 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.20216645606', 'd13': '2.10402794429', 'd23': '0.907894558278'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct  3 19:11:41 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 48,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,D}
2 *2 H 0 {1,S}
3    O 0 {1,D}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.21988501633', 'd13': '2.37290946709', 'd23': '1.15309849454'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct  3 21:06:25 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 49,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *1 C 0 {1,D} {3,S}
3 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.46347894682', 'd13': '2.32579722591', 'd23': '0.862862296846'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct  4 14:36:06 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 50,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.06757172779', 'd13': '2.1796554827', 'd23': '1.11574127633'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct  3 23:15:02 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 51,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.926273983824', 'd13': '2.29011119802', 'd23': '1.36413844572'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sat Oct  5 07:17:14 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 52,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,D}
2 *3 C 1 {1,S}
3    C 0 {1,D}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,D}
3    C 0 {2,D}
4 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.08060600298', 'd13': '2.31166939106', 'd23': '1.23289966705'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sat Oct  5 21:39:01 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 53,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    O 0 {1,S} {3,S}
3 *1 O 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    O 0 {1,S} {3,S}
3 *3 O 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.04828664688', 'd13': '2.22345150147', 'd23': '1.17928080736'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct  6 05:11:10 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 54,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3 *2 H 0 {2,S}
4    O 0 {2,D}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,D}
3    O 0 {2,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.19436701782', 'd13': '2.42765010692', 'd23': '1.23398956601'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct  6 06:31:12 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 55,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3 *3 C 1 {2,D}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,D}
3 *1 C 0 {2,D} {4,S}
4 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.856116451331', 'd13': '2.33353250223', 'd23': '1.47813602871'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct  6 08:26:17 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 56,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {3,S}
2    C 0 {3,D}
3 *3 C 1 {1,S} {2,D}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D} {4,S}
3    C 0 {2,D}
4 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.890380160538', 'd13': '2.3037243324', 'd23': '1.41348718108'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct  6 10:45:23 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 57,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *3 C 1 {2,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S}
4    C 0 {2,S}
5 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.929233924724', 'd13': '2.29221727048', 'd23': '1.36327979666'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Oct  7 07:11:14 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 58,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3    C 0 {1,D}
4 *3 C 1 {2,D}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3 *1 C 0 {1,D} {5,S}
4    C 0 {2,D}
5 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.857297575577', 'd13': '2.33091998893', 'd23': '1.47462637073'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Oct  7 12:18:12 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 59,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.30720965209', 'd13': '2.28142288545', 'd23': '0.974384887201'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Oct  8 10:23:39 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 60,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *3 C 1 {1,S}
4    O 0 {2,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S}
4    O 0 {2,S}
5 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.929232557334', 'd13': '2.2968743381', 'd23': '1.36776843715'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct 10 22:36:03 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 61,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {3,S}
2    C 0 {3,S} {4,D}
3    O 0 {1,S} {2,S}
4    O 0 {2,D}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1 *1 C 0 {3,S} {4,S}
2    C 0 {3,S} {5,D}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
5    O 0 {2,D}
""",
    distances = DistanceData(
        distances = {'d12': '0.955049619099', 'd13': '2.28383585417', 'd23': '1.32911528045'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 11 00:52:04 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 62,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4 *1 C 0 {2,S} {3,D} {5,S}
5 *2 H 0 {4,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {4,S}
3    C 0 {1,S} {4,D}
4 *3 C 1 {2,S} {3,D}
""",
    distances = DistanceData(
        distances = {'d12': '1.41659613444', 'd13': '2.30400248858', 'd23': '0.887625561499'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 11 07:52:33 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 63,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *3 C 1 {2,S}
5    O 0 {3,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *1 C 0 {2,S} {6,S}
5    O 0 {3,S}
6 *2 H 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.929562714059', 'd13': '2.28701840306', 'd23': '1.35777238782'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 11 22:27:35 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 64,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
5    O 0 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    O 0 {1,S}
6 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.923478017904', 'd13': '2.29270714272', 'd23': '1.36923344491'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sat Oct 12 13:28:20 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 65,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *3 C 1 {2,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 C 0 {2,S} {6,S}
6 *2 H 0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.927276316146', 'd13': '2.28958345535', 'd23': '1.36286435818'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct 13 02:56:15 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 66,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {5,S}
5 *3 C 1 {1,S} {4,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.970596361047', 'd13': '2.28396108373', 'd23': '1.31339574095'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct 13 18:16:24 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 67,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {5,S}
5 *3 C 1 {2,S} {4,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {6,S}
3    C 0 {1,S} {5,S}
4    C 0 {2,S}
5    C 0 {3,S}
6 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.976300411313', 'd13': '2.28125066263', 'd23': '1.30507883057'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Oct 14 20:11:44 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 68,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *3 C 1 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.919883004244', 'd13': '2.29790558097', 'd23': '1.37805888248'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Oct 23 23:13:03 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 69,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {5,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *3 C 1 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {5,S}
3 *1 C 0 {1,S} {6,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.92744513748', 'd13': '2.29850984591', 'd23': '1.37106798486'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Oct 24 19:10:33 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 70,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,B} {3,B}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6 *3 C 1 {4,B} {5,B}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1 *1 C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6    C 0 {4,B} {5,B}
7 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.850034093713', 'd13': '2.34311603157', 'd23': '1.4930819397'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 25 07:16:46 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 71,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {5,B}
3    C 0 {1,B} {6,B}
4    C 0 {5,B} {6,B}
5    C 0 {2,B} {4,B}
6    C 0 {3,B} {4,B}
7 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {5,B}
3    C 0 {1,B} {6,B}
4    C 0 {5,B} {6,B}
5    C 0 {2,B} {4,B}
6    C 0 {3,B} {4,B}
7 *1 O 0 {1,S} {8,S}
8 *2 H 0 {7,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.08657681722', 'd13': '2.16027024006', 'd23': '1.08110686108'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Fri Oct 25 21:17:19 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 72,
    reactant1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {8,S}
2    C 0 {1,S} {3,B} {4,B}
3    C 0 {2,B} {6,B}
4    C 0 {2,B} {7,B}
5    C 0 {6,B} {7,B}
6    C 0 {3,B} {5,B}
7    C 0 {4,B} {5,B}
8 *3 C 1 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {9,S}
3    C 0 {1,S} {4,B} {5,B}
4    C 0 {3,B} {7,B}
5    C 0 {3,B} {8,B}
6    C 0 {7,B} {8,B}
7    C 0 {4,B} {6,B}
8    C 0 {5,B} {6,B}
9 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '0.923728822558', 'd13': '2.29107401551', 'd23': '1.36787122418'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation via double-ended TS generator.""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Oct 27 06:17:26 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via double-ended strategy using automatic transition state generator"""),
    ],
)

entry(
    index = 73,
    reactant1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1
""",
    product2 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
4 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.37890', 'd13': '2.70895', 'd23': '1.33014'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 74,
    reactant1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    O 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3    O 0 {2,S}
4 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.44233', 'd13': '2.73121', 'd23': '1.28923'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 75,
    reactant1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *3 O 1 {2,S}
""",
    product1 = 
"""
1 *3 C 1
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *1 O 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.30536', 'd13': '2.51006', 'd23': '1.20569'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 76,
    reactant1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
4 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.14362', 'd13': '2.54716', 'd23': '1.40355'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 77,
    reactant1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    O 0 {2,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3    O 0 {2,S}
4 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.22242', 'd13': '2.54544', 'd23': '1.32319'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 78,
    reactant1 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *3 O 1 {2,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *1 O 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.10392', 'd13': '2.34834', 'd23': '1.27899'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 79,
    reactant1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    product1 = 
"""
1 *3 C 1
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.37951', 'd13': '2.70269', 'd23': '1.32326'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 80,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.15831', 'd13': '2.54409', 'd23': '1.38612'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 81,
    reactant1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,D}
2 *3 C 1 {1,D}
""",
    product1 = 
"""
1 *3 C 1
""",
    product2 = 
"""
1    C 0 {2,D}
2 *1 C 0 {1,D} {3,S}
3 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.31192', 'd13': '2.68374', 'd23': '1.37209'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 82,
    reactant1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *3 C 1 {1,S} {3,S}
""",
    product1 = 
"""
1 *3 C 1
""",
    product2 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *1 C 0 {1,S} {3,S} {5,S}
5 *2 H 0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.39021', 'd13': '2.70089', 'd23': '1.31082'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 83,
    reactant1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S}
2    O 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
""",
    product1 = 
"""
1 *3 C 1
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    O 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.35719', 'd13': '2.69461', 'd23': '1.33957'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 84,
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S}
2    O 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    O 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.32993', 'd13': '2.70362', 'd23': '1.37733'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 85,
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S}
2    O 0 {1,S} {3,S}
3    C 0 {1,S} {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    O 0 {1,S} {3,S}
3    C 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.33663', 'd13': '2.70329', 'd23': '1.36697'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 86,
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S}
2    C 0 {1,S} {3,S}
3    C 0 {1,S} {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {3,S}
3    C 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.30692', 'd13': '2.69157', 'd23': '1.38471'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 87,
    reactant1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
""",
    product1 = 
"""
1 *3 O 1
""",
    product2 = 
"""
1 *1 C 0 {2,S} {4,S}
2    C 0 {1,S} {3,S}
3    O 0 {2,S}
4 *2 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.39456', 'd13': '2.58134', 'd23': '1.18856'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

entry(
    index = 88,
    reactant1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *3 O 1 {2,S}
""",
    product1 = 
"""
1 *3 O 1
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S}
3 *1 O 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.32977', 'd13': '2.28959', 'd23': '1.05831'},
        method = 'B3LYP/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""B3LYP/6-31+G(d,p) calculation""",
    longDesc = 
u"""

""",
    history = [
        ("Sun Nov 17 1:40:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action",""" """),
    ],
)

