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
1    H 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *2 H 0 {2,S}
5    H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    H 0 {2,S}
4    H 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.3393741359,
        'd23' : 1.33935268564,
        'd13' : 2.67872682077,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""
M06-2X/6-31+G(d,p) calculations w/ tight, int=ultrafine options
""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
1    H 0 {2,S}
2    C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *1 C 0 {2,S} {6,S} {7,S} {8,S}
5    H 0 {2,S}
6    H 0 {4,S}
7    H 0 {4,S}
8 *2 H 0 {4,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    C 0 {2,S} {5,S} {6,S} {7,S}
4    H 0 {2,S}
5    H 0 {3,S}
6    H 0 {3,S}
7    H 0 {3,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.30821129476,
        'd23' : 1.37712245821,
        'd13' : 2.68276888272,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6     H 0 {4,S}
7  *1 C 0 {4,S} {9,S} {10,S} {11,S}
8     H 0 {4,S}
9     H 0 {7,S}
10    H 0 {7,S}
11 *2 H 0 {7,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {5,S} {6,S} {7,S}
5     H 0 {4,S}
6     C 0 {4,S} {8,S} {9,S} {10,S}
7     H 0 {4,S}
8     H 0 {6,S}
9     H 0 {6,S}
10    H 0 {6,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.31063324722,
        'd23' : 1.37920181409,
        'd13' : 2.68792471359,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6     H 0 {4,S}
7     C 0 {4,S} {9,S} {10,S} {11,S}
8     H 0 {4,S}
9     H 0 {7,S}
10    H 0 {7,S}
11 *1 C 0 {7,S} {12,S} {13,S} {14,S}
12    H 0 {11,S}
13    H 0 {11,S}
14 *2 H 0 {11,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     C 0 {2,S} {5,S} {6,S} {7,S}
4     H 0 {2,S}
5     H 0 {3,S}
6     C 0 {3,S} {8,S} {9,S} {10,S}
7     H 0 {3,S}
8     C 0 {6,S} {11,S} {12,S} {13,S}
9     H 0 {6,S}
10    H 0 {6,S}
11    H 0 {8,S}
12    H 0 {8,S}
13    H 0 {8,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.31200348227,
        'd23' : 1.37931646413,
        'd13' : 2.69070299055,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6  *1 C 0 {4,S} {9,S} {10,S} {11,S}
7     H 0 {4,S}
8     C 0 {4,S} {12,S} {13,S} {14,S}
9     H 0 {6,S}
10    H 0 {6,S}
11 *2 H 0 {6,S}
12    H 0 {8,S}
13    H 0 {8,S}
14    H 0 {8,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *1 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     C 0 {4,S} {11,S} {12,S} {13,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
11    H 0 {7,S}
12    H 0 {7,S}
13    H 0 {7,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.31597367556,
        'd23' : 1.37992230669,
        'd13' : 2.69552023665,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6 *1 C 0 {3,S} {7,S} {8,S} {9,S}
7    H 0 {6,S}
8    H 0 {6,S}
9 *2 H 0 {6,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4 *3 C 1 {3,S} {7,S} {8,S}
5    H 0 {3,S}
6    H 0 {3,S}
7    H 0 {4,S}
8    H 0 {4,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.32103245203,
        'd23' : 1.35951459954,
        'd13' : 2.67705175771,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
1    H 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *2 H 0 {2,S}
5    H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    H 0 {2,S}
4    H 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {8,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
8 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.37713399973,
        'd23' : 1.30819156289,
        'd13' : 2.68278131422,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
1    H 0 {2,S}
2    C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *1 C 0 {2,S} {6,S} {7,S} {8,S}
5    H 0 {2,S}
6    H 0 {4,S}
7    H 0 {4,S}
8 *2 H 0 {4,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    C 0 {2,S} {5,S} {6,S} {7,S}
4    H 0 {2,S}
5    H 0 {3,S}
6    H 0 {3,S}
7    H 0 {3,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {8,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
8 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.34454885366,
        'd23' : 1.34468432402,
        'd13' : 2.68491023469,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6     H 0 {4,S}
7  *1 C 0 {4,S} {9,S} {10,S} {11,S}
8     H 0 {4,S}
9     H 0 {7,S}
10    H 0 {7,S}
11 *2 H 0 {7,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     H 0 {4,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {8,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
8 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.34592645405,
        'd23' : 1.34540756838,
        'd13' : 2.68976068861,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6     H 0 {4,S}
7     C 0 {4,S} {9,S} {10,S} {11,S}
8     H 0 {4,S}
9     H 0 {7,S}
10    H 0 {7,S}
11 *1 C 0 {7,S} {12,S} {13,S} {14,S}
12    H 0 {11,S}
13    H 0 {11,S}
14 *2 H 0 {11,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     C 0 {2,S} {5,S} {6,S} {7,S}
4     H 0 {2,S}
5     C 0 {3,S} {8,S} {9,S} {10,S}
6     H 0 {3,S}
7     H 0 {3,S}
8     H 0 {5,S}
9     C 0 {5,S} {11,S} {12,S} {13,S}
10    H 0 {5,S}
11    H 0 {9,S}
12    H 0 {9,S}
13    H 0 {9,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {8,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
8 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.34734208010,
        'd23' : 1.34638652623,
        'd13' : 2.69267562849,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6  *1 C 0 {4,S} {9,S} {10,S} {11,S}
7     H 0 {4,S}
8     C 0 {4,S} {12,S} {13,S} {14,S}
9     H 0 {6,S}
10    H 0 {6,S}
11 *2 H 0 {6,S}
12    H 0 {8,S}
13    H 0 {8,S}
14    H 0 {8,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {5,S} {6,S} {7,S}
5     H 0 {4,S}
6     C 0 {4,S} {8,S} {9,S} {10,S}
7     C 0 {4,S} {11,S} {12,S} {13,S}
8     H 0 {6,S}
9     H 0 {6,S}
10    H 0 {6,S}
11    H 0 {7,S}
12    H 0 {7,S}
13    H 0 {7,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {8,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
8 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.34764127963,
        'd23' : 1.34162534895,
        'd13' : 2.68778427670,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6 *1 C 0 {3,S} {7,S} {8,S} {9,S}
7    H 0 {6,S}
8    H 0 {6,S}
9 *2 H 0 {6,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5 *3 C 1 {3,S} {7,S} {8,S}
6    H 0 {3,S}
7    H 0 {5,S}
8    H 0 {5,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {8,S}
2    C 0 {1,S} {5,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {2,S}
8 *2 H 0 {1,S}
""",
    distances = {
        'd12' : 1.35801928986,
        'd23' : 1.32864318762,
        'd13' : 2.68078750257,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
1    H 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *2 H 0 {2,S}
5    H 0 {2,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     C 0 {1,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     H 0 {4,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    H 0 {2,S}
4    H 0 {2,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {11,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
11 *2 H 0 {2,S}
""",
    distances = {
        'd12' : 1.37914883843,
        'd23' : 1.31063441583,
        'd13' : 2.68787275261,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
1    H 0 {2,S}
2    C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *1 C 0 {2,S} {6,S} {7,S} {8,S}
5    H 0 {2,S}
6    H 0 {4,S}
7    H 0 {4,S}
8 *2 H 0 {4,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     C 0 {1,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     H 0 {4,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    H 0 {2,S}
4    C 0 {2,S} {5,S} {6,S} {7,S}
5    H 0 {4,S}
6    H 0 {4,S}
7    H 0 {4,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {11,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
11 *2 H 0 {2,S}
""",
    distances = {
        'd12' : 1.34541799426,
        'd23' : 1.34597083831,
        'd13' : 2.68979141822,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 15,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6     H 0 {4,S}
7  *1 C 0 {4,S} {9,S} {10,S} {11,S}
8     H 0 {4,S}
9     H 0 {7,S}
10    H 0 {7,S}
11 *2 H 0 {7,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     C 0 {1,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     H 0 {4,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {5,S} {6,S} {7,S}
5     H 0 {4,S}
6     C 0 {4,S} {8,S} {9,S} {10,S}
7     H 0 {4,S}
8     H 0 {6,S}
9     H 0 {6,S}
10    H 0 {6,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {11,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
11 *2 H 0 {2,S}
""",
    distances = {
        'd12' : 1.34276693940,
        'd23' : 1.34762633132,
        'd13' : 2.68875565708,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6  *1 C 0 {4,S} {9,S} {10,S} {11,S}
7     H 0 {4,S}
8     C 0 {4,S} {12,S} {13,S} {14,S}
9     H 0 {6,S}
10    H 0 {6,S}
11 *2 H 0 {6,S}
12    H 0 {8,S}
13    H 0 {8,S}
14    H 0 {8,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     C 0 {1,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     H 0 {4,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     C 0 {4,S} {11,S} {12,S} {13,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
11    H 0 {7,S}
12    H 0 {7,S}
13    H 0 {7,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {11,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
11 *2 H 0 {2,S}
""",
    distances = {
        'd12' : 1.34656921583,
        'd23' : 1.34394599296,
        'd13' : 2.68905921144,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 18,
    reactant1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6 *1 C 0 {3,S} {7,S} {8,S} {9,S}
7    H 0 {6,S}
8    H 0 {6,S}
9 *2 H 0 {6,S}
""",
    reactant2 = 
"""
1  *3 C 1 {2,S} {3,S} {4,S}
2     H 0 {1,S}
3     H 0 {1,S}
4     C 0 {1,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     H 0 {4,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4 *3 C 1 {3,S} {7,S} {8,S}
5    H 0 {3,S}
6    H 0 {3,S}
7    H 0 {4,S}
8    H 0 {4,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {11,S}
3     C 0 {1,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
11 *2 H 0 {2,S}
""",
    distances = {
        'd12' : 1.35242499306,
        'd23' : 1.34612283019,
        'd13' : 2.69841510129,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
1    H 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *2 H 0 {2,S}
5    H 0 {2,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {8,S} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {4,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    H 0 {2,S}
4    H 0 {2,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5  *2 H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = {
        'd12' : 1.40716757820,
        'd23' : 1.28550527301,
        'd13' : 2.68933612152,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
1    H 0 {2,S}
2    C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *1 C 0 {2,S} {6,S} {7,S} {8,S}
5    H 0 {2,S}
6    H 0 {4,S}
7    H 0 {4,S}
8 *2 H 0 {4,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {8,S} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {4,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    C 0 {2,S} {5,S} {6,S} {7,S}
4    H 0 {2,S}
5    H 0 {3,S}
6    H 0 {3,S}
7    H 0 {3,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5  *2 H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = {
        'd12' : 1.37352706397,
        'd23' : 1.32070123588,
        'd13' : 2.68865422259,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6     H 0 {4,S}
7  *1 C 0 {4,S} {9,S} {10,S} {11,S}
8     H 0 {4,S}
9     H 0 {7,S}
10    H 0 {7,S}
11 *2 H 0 {7,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {8,S} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {4,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     H 0 {4,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5  *2 H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = {
        'd12' : 1.37534926838,
        'd23' : 1.31645349828,
        'd13' : 2.68924761910,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6     H 0 {4,S}
7     C 0 {4,S} {9,S} {10,S} {11,S}
8     H 0 {4,S}
9     H 0 {7,S}
10    H 0 {7,S}
11 *1 C 0 {7,S} {12,S} {13,S} {14,S}
12    H 0 {11,S}
13    H 0 {11,S}
14 *2 H 0 {11,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {8,S} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {4,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     C 0 {2,S} {5,S} {6,S} {7,S}
4     H 0 {2,S}
5     C 0 {3,S} {8,S} {9,S} {10,S}
6     H 0 {3,S}
7     H 0 {3,S}
8     C 0 {5,S} {11,S} {12,S} {13,S}
9     H 0 {5,S}
10    H 0 {5,S}
11    H 0 {8,S}
12    H 0 {8,S}
13    H 0 {8,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5  *2 H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = {
        'd12' : 1.37067593134,
        'd23' : 1.31924962137,
        'd13' : 2.68744916354,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6  *1 C 0 {4,S} {9,S} {10,S} {11,S}
7     H 0 {4,S}
8     C 0 {4,S} {12,S} {13,S} {14,S}
9     H 0 {6,S}
10    H 0 {6,S}
11 *2 H 0 {6,S}
12    H 0 {8,S}
13    H 0 {8,S}
14    H 0 {8,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {8,S} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {4,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product1 = 
"""
1     H 0 {2,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {5,S} {6,S} {7,S}
5     C 0 {4,S} {8,S} {9,S} {10,S}
6     H 0 {4,S}
7     C 0 {4,S} {11,S} {12,S} {13,S}
8     H 0 {5,S}
9     H 0 {5,S}
10    H 0 {5,S}
11    H 0 {7,S}
12    H 0 {7,S}
13    H 0 {7,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5  *2 H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = {
        'd12' : 1.37729313657,
        'd23' : 1.31606569056,
        'd13' : 2.69319121592,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6 *1 C 0 {3,S} {7,S} {8,S} {9,S}
7    H 0 {6,S}
8    H 0 {6,S}
9 *2 H 0 {6,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {5,S} {6,S} {7,S}
2  *3 C 1 {1,S} {3,S} {4,S}
3     H 0 {2,S}
4     C 0 {2,S} {8,S} {9,S} {10,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {4,S}
9     H 0 {4,S}
10    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5 *3 C 1 {3,S} {7,S} {8,S}
6    H 0 {3,S}
7    H 0 {5,S}
8    H 0 {5,S}
""",
    product2 = 
"""
1  *1 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5  *2 H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = {
        'd12' : 1.38731570737,
        'd23' : 1.30207330006,
        'd13' : 2.68718303364,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
1    H 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *2 H 0 {2,S}
5    H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S} {5,S}
5    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3 *1 C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5 *2 H 0 {3,S}
6    H 0 {3,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
""",
    distances = {
        'd12' : 1.42490792824,
        'd23' : 1.28503916731,
        'd13' : 2.70582358565,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 26,
    reactant1 = 
"""
1    H 0 {2,S}
2    C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4 *1 C 0 {2,S} {6,S} {7,S} {8,S}
5    H 0 {2,S}
6    H 0 {4,S}
7    H 0 {4,S}
8 *2 H 0 {4,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S} {5,S}
5    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3 *1 C 0 {2,S} {4,S} {5,S} {6,S}
4 *2 H 0 {3,S}
5    H 0 {3,S}
6    H 0 {3,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 {1,S} {6,S} {7,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
""",
    distances = {
        'd12' : 1.38946362815,
        'd23' : 1.31635615242,
        'd13' : 2.68885330909,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 27,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6     H 0 {4,S}
7  *1 C 0 {4,S} {9,S} {10,S} {11,S}
8     H 0 {4,S}
9     H 0 {7,S}
10    H 0 {7,S}
11 *2 H 0 {7,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S} {5,S}
5    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3 *1 C 0 {2,S} {4,S} {5,S} {6,S}
4 *2 H 0 {3,S}
5    H 0 {3,S}
6    H 0 {3,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3  *3 C 1 {1,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
""",
    distances = {
        'd12' : 1.39480230036,
        'd23' : 1.31403057143,
        'd13' : 2.69680491933,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 28,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6     H 0 {4,S}
7     C 0 {4,S} {9,S} {10,S} {11,S}
8     H 0 {4,S}
9     H 0 {7,S}
10    H 0 {7,S}
11 *1 C 0 {7,S} {12,S} {13,S} {14,S}
12    H 0 {11,S}
13    H 0 {11,S}
14 *2 H 0 {11,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S} {5,S}
5    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3 *1 C 0 {2,S} {4,S} {5,S} {6,S}
4 *2 H 0 {3,S}
5    H 0 {3,S}
6    H 0 {3,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {5,S} {6,S}
2     C 0 {1,S} {4,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {2,S} {12,S} {13,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
""",
    distances = {
        'd12' : 1.39427571589,
        'd23' : 1.31945648860,
        'd13' : 2.69931215056,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 29,
    reactant1 = 
"""
1     H 0 {2,S}
2     C 0 {1,S} {3,S} {4,S} {5,S}
3     H 0 {2,S}
4     C 0 {2,S} {6,S} {7,S} {8,S}
5     H 0 {2,S}
6  *1 C 0 {4,S} {9,S} {10,S} {11,S}
7     H 0 {4,S}
8     C 0 {4,S} {12,S} {13,S} {14,S}
9     H 0 {6,S}
10    H 0 {6,S}
11 *2 H 0 {6,S}
12    H 0 {8,S}
13    H 0 {8,S}
14    H 0 {8,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S} {5,S}
5    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3 *1 C 0 {2,S} {4,S} {5,S} {6,S}
4 *2 H 0 {3,S}
5    H 0 {3,S}
6    H 0 {3,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *3 C 1 {1,S} {12,S} {13,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
""",
    distances = {
        'd12' : 1.39571486669,
        'd23' : 1.31301772418,
        'd13' : 2.70603863261,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 30,
    reactant1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6 *1 C 0 {3,S} {7,S} {8,S} {9,S}
7    H 0 {6,S}
8    H 0 {6,S}
9 *2 H 0 {6,S}
""",
    reactant2 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S} {5,S}
5    H 0 {4,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    O 0 {1,S} {3,S}
3 *1 C 0 {2,S} {4,S} {5,S} {6,S}
4 *2 H 0 {3,S}
5    H 0 {3,S}
6    H 0 {3,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 1 {1,S} {6,S} {7,S}
3    O 0 {1,S} {8,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {3,S}
""",
    distances = {
        'd12' : 1.40646608200,
        'd23' : 1.30692490313,
        'd13' : 2.70366151951,
    },
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jun 20 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)