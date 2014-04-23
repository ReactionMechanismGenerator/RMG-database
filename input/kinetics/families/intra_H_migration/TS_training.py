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
2 *3 C 0 {1,S} {3,S} {4,S}
3 *1 C 1 {2,S}
4 *2 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S} {3,S}
3 *3 C 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.30291', 'd13': '1.49239', 'd23': '1.30072'},
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
        ("Wed Apr 23 18:19:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 1 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *3 C 0 {3,S} {5,S}
5 *2 H 0 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *3 C 0 {1,S} {3,S} {5,S}
3    C 0 {2,S} {4,S}
4 *1 C 1 {3,S}
5 *2 H 0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.40022', 'd13': '2.22140', 'd23': '1.41340'},
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
        ("Wed Apr 23 18:19:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
1 *3 C 0 {2,S} {4,S}
2    O 0 {1,S} {3,S}
3 *1 O 1 {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 1 {2,S}
2    O 0 {1,S} {3,S}
3 *3 O 0 {2,S} {4,S}
4 *2 H 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.27013', 'd13': '2.02458', 'd23': '1.333666'},
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
        ("Wed Apr 23 18:19:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)
