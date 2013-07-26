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
    distances = DistanceData(
      distances = {'d12' : 1.30821129476, 'd23' : 1.37712245821, 'd13' : 2.68276888272},
    ),
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
    index = 2,
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
    distances = DistanceData(
      distances = {'d12' : 1.31063324722, 'd23' : 1.37920181409, 'd13' : 2.68792471359},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.31200348227, 'd23' : 1.37931646413, 'd13' : 2.69070299055},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.31597367556, 'd23' : 1.37992230669, 'd13' : 2.69552023665},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.32103245203, 'd23' : 1.35951459954, 'd13' : 2.67705175771},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.37713399973, 'd23' : 1.30819156289, 'd13' : 2.68278131422},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.34592645405, 'd23' : 1.34540756838, 'd13' : 2.68976068861},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.34734208010, 'd23' : 1.34638652623, 'd13' : 2.69267562849},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.34764127963, 'd23' : 1.34162534895, 'd13' : 2.68778427670},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.35801928986, 'd23' : 1.32864318762, 'd13' : 2.68078750257},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.37914883843, 'd23' : 1.31063441583, 'd13' : 2.68787275261},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.34541799426, 'd23' : 1.34597083831, 'd13' : 2.68979141822},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.34656921583, 'd23' : 1.34394599296, 'd13' : 2.68905921144},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.35242499306, 'd23' : 1.34612283019, 'd13' : 2.69841510129},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.40716757820, 'd23' : 1.28550527301, 'd13' : 2.68933612152},
    ),
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
    index = 16,
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
    distances = DistanceData(
      distances = {'d12' : 1.37352706397, 'd23' : 1.32070123588, 'd13' : 2.68865422259},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.37534926838, 'd23' : 1.31645349828, 'd13' : 2.68924761910},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.37067593134, 'd23' : 1.31924962137, 'd13' : 2.68744916354},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.37729313657, 'd23' : 1.31606569056, 'd13' : 2.69319121592},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.38731570737, 'd23' : 1.30207330006, 'd13' : 2.68718303364},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.42490792824, 'd23' : 1.28503916731, 'd13' : 2.70582358565},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.38946362815, 'd23' : 1.31635615242, 'd13' : 2.68885330909},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.39480230036, 'd23' : 1.31403057143, 'd13' : 2.69680491933},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.39427571589, 'd23' : 1.31945648860, 'd13' : 2.69931215056},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.39571486669, 'd23' : 1.31301772418, 'd13' : 2.70603863261},
    ),
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
    distances = DistanceData(
      distances = {'d12' : 1.40646608200, 'd23' : 1.30692490313, 'd13' : 2.70366151951},
    ),
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
1 *2 H 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6    H 0 {3,S}
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
2    C 0 {1,S} {3,S} {4,S} {5,S}
3 *3 O 1 {2,S}
4    H 0 {2,S}
5    H 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.22662146323, 'd23' : 1.26876032779, 'd13' : 2.48841133896},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jul 09 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 28,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6    C 0 {3,S} {7,S} {8,S} {9,S}
7    H 0 {6,S}
8    H 0 {6,S}
9    H 0 {6,S}
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
2 *1 C 0 {1,S} {3,S} {4,S} {5,S}
3 *2 H 0 {2,S}
4    H 0 {2,S}
5    H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,S} {7,S} {8,S}
3 *3 O 1 {2,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.23281655422, 'd23' : 1.26433589813, 'd13' : 2.49087111395},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jul 09 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 29,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6    C 0 {3,S} {7,S} {8,S} {9,S}
7    H 0 {6,S}
8    H 0 {6,S}
9    H 0 {6,S}
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
2    C 0 {1,S} {3,S} {4,S} {5,S}
3 *3 O 1 {2,S}
4    C 0 {2,S} {6,S} {7,S} {8,S}
5    H 0 {2,S}
6    H 0 {4,S}
7    H 0 {4,S}
8    H 0 {4,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.27491700423, 'd23' : 1.24043183457, 'd13' : 2.51130683348},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jul 09 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 30,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6    H 0 {3,S}
""",
    reactant2 = 
"""
1     C 0 {2,S} {4,S} {5,S} {6,S}
2  *3 C 1 {1,S} {3,S} {7,S}
3     C 0 {2,S} {8,S} {9,S} {10,S}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {3,S}
""",
    product1 = 
"""
1    H 0 {2,S}
2    C 0 {1,S} {3,S} {4,S} {5,S}
3    H 0 {2,S}
4    H 0 {2,S}
5 *1 O 1 {2,S}
""",
    product2 = 
"""
1  *3 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4  *2 H 0 {1,S}
5     H 0 {1,S}
6     H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.32301125928, 'd23' : 1.21339171256, 'd13' : 2.532136452},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jul 09 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 31,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S} {5,S} {6,S}
4    H 0 {3,S}
5    H 0 {3,S}
6    C 0 {3,S} {7,S} {8,S} {9,S}
7    H 0 {6,S}
8    H 0 {6,S}
9    H 0 {6,S}
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
2    C 0 {1,S} {3,S} {4,S} {5,S}
3 *3 O 1 {2,S}
4    C 0 {2,S} {6,S} {7,S} {8,S}
5    H 0 {2,S}
6    H 0 {4,S}
7    H 0 {4,S}
8    H 0 {4,S}
""",
    product2 = 
"""
1     C 0 {2,S} {3,S} {4,S} {5,S}
2  *1 C 0 {1,S} {6,S} {7,S} {8,S}
3     C 0 {1,S} {9,S} {10,S} {11,S}
4     H 0 {1,S}
5     H 0 {1,S}
6  *2 H 0 {2,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {3,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.28173528762, 'd23' : 1.23320782156, 'd13' : 2.51340049172},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Tue Jul 09 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations using the automatic transition state search algorithm."""),
    ],
)

entry(
    index = 32,
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S} {7,S} {8,S}
3 *2 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1    C 0 {2,S} {5,S} {6,S} {7,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    H 0 {2,S}
4    H 0 {2,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
""",
    product2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.36237396793244, 'd23' : 0.920939107487569, 'd13' : 2.28237150284523},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jul 10 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations manually conducted."""),
    ],
)

entry(
    index = 33,
    reactant1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *1 O 0 {1,S} {6,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1    C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 O 1 {1,S}
3    H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
""",
    product2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.23049946968701, 'd23' : 0.878798866066632, 'd13' : 2.09984939386138},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jul 10 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations manually conducted."""),
    ],
)

entry(
    index = 34,
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    O 0 {1,S} {6,S}
3 *2 H 0 {1,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    O 0 {1,S} {5,S}
5    H 0 {4,S}
""",
    product2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.30574576089681, 'd23' : 0.987751217361943, 'd13' : 2.29308108267021},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jul 10 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations manually conducted."""),
    ],
)

entry(
    index = 35,
    reactant1 = 
"""
1 *1 C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,S} {7,S} {8,S}
3    O 0 {2,S} {9,S}
4 *2 H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {2,S}
9    H 0 {3,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *3 C 1 {2,S} {3,S} {4,S}
2    H 0 {1,S}
3    H 0 {1,S}
4    C 0 {1,S} {5,S} {6,S} {7,S}
5    O 0 {4,S} {8,S}
6    H 0 {4,S}
7    H 0 {4,S}
8    H 0 {5,S}
""",
    product2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.36894227493346, 'd23' : 0.917222917125384, 'd13' : 2.28584480658683},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jul 10 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations manually conducted."""),
    ],
)

entry(
    index = 36,
    reactant1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2 *1 C 0 {1,S} {3,S} {7,S} {8,S}
3    O 0 {2,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7 *2 H 0 {2,S}
8    H 0 {2,S}
9    H 0 {3,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1    C 0 {2,S} {5,S} {6,S} {7,S}
2 *3 C 1 {1,S} {3,S} {4,S}
3    H 0 {2,S}
4    O 0 {2,S} {8,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {1,S}
8    H 0 {4,S}
""",
    product2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.28038915998223, 'd23' : 1.01536924697373, 'd13' : 2.29500967372689},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jul 10 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations manually conducted."""),
    ],
)

entry(
    index = 37,
    reactant1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,S} {7,S} {8,S}
3 *1 O 0 {2,S} {9,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {2,S}
9 *2 H 0 {3,S}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1    C 0 {2,S} {4,S} {5,S} {6,S}
2    C 0 {1,S} {3,S} {7,S} {8,S}
3 *3 O 1 {2,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {1,S}
7    H 0 {2,S}
8    H 0 {2,S}
""",
    product2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    distances = DistanceData(
      distances = {'d12' : 1.23254024331865, 'd23' : 0.879987818608872, 'd13' : 2.10329318462738},
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""M06-2X/6-31+G(d,p) calculations""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jul 10 12:04:58 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""pierrelb added this from calculations manually conducted."""),
    ],
)

entry(
    index = 38,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 O 1
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.36876181545', 'd13': '2.1612155077', 'd23': '0.812296043557'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:47 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 39,
    reactant1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
""",
    reactant2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '0.921546207259', 'd13': '2.28201823633', 'd23': '1.36160791194'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:47 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 40,
    reactant1 = 
"""
1    C 0 {2,S}
2 *3 O 1 {1,S}
""",
    reactant2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '0.878466949226', 'd13': '2.10041847117', 'd23': '1.23109428548'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:47 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 41,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 C 1 {1,S}
""",
    reactant2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '0.98778407539', 'd13': '1.30557736874', 'd23': '2.29297757456'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:47 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 42,
    reactant1 = 
"""
1 *3 C 1 {2,D}
2    C 0 {1,D}
""",
    reactant2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '0.870557845484', 'd13': '2.2993224283', 'd23': '1.43031240946'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:48 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 43,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 O 0 {1,S} {4,S}
4 *2 H 0 {3,S}
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
3 *3 O 1 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.23319401473', 'd13': '2.10364512661', 'd23': '0.879705648353'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:48 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 44,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    O 0 {1,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    O 0 {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.28001196708', 'd13': '2.29519902464', 'd23': '1.01602678611'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:49 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S}
3    O 0 {1,S}
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
2 *3 C 1 {1,S}
3    O 0 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.3695985205', 'd13': '2.28620680055', 'd23': '0.916948114925'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:49 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.36602382304', 'd13': '2.28513175685', 'd23': '0.92078848262'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:50 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {3,S}
3    C 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {3,S}
3 *3 C 1 {1,S} {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.41366938406', 'd13': '2.28737994166', 'd23': '0.87641002763'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:50 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2 *3 C 1 {1,S} {3,S}
3    O 0 {1,S} {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.36395734593', 'd13': '2.28294668685', 'd23': '0.921160996834'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:51 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.26872335796', 'd13': '2.28673375578', 'd23': '1.01896160848'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:51 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
1 *1 C 0 {3,S} {4,S}
2    C 0 {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2 *3 C 1 {3,S}
3    O 0 {1,S} {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.31062425836', 'd13': '2.29898153229', 'd23': '0.98999514929'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:51 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 51,
    reactant1 = 
"""
1 *3 C 1 {2,S} {3,S}
2    C 0 {1,S}
3    C 0 {1,S}
""",
    reactant2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '0.955159876503', 'd13': '2.27516596724', 'd23': '1.32155051423'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:52 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 52,
    reactant1 = 
"""
1    C 0 {2,S}
2    O 0 {1,S} {3,S}
3 *3 O 1 {2,S}
""",
    reactant2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.02407504738', 'd13': '2.13195529814', 'd23': '1.11101337387'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:52 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.44592668741', 'd13': '2.31224060659', 'd23': '0.866699918354'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:53 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.40281808323', 'd13': '2.29239043303', 'd23': '0.889901992254'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:54 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 55,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    O 0 {1,S}
5 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S} {4,S}
4    O 0 {3,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.25696584461', 'd13': '2.30205794469', 'd23': '1.04532238564'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:54 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 56,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {3,S} {4,S}
2    C 0 {3,S}
3    C 0 {1,S} {2,S} {5,D}
4 *2 H 0 {1,S}
5    O 0 {3,D}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2    C 0 {1,S} {3,S} {4,D}
3 *3 C 1 {2,S}
4    O 0 {2,D}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.29493056195', 'd13': '2.27249806075', 'd23': '0.978150838197'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:55 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 57,
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.36546577389', 'd13': '2.28311500994', 'd23': '0.918609178238'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:56 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 58,
    reactant1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S} {4,S}
3    C 0 {2,S}
4    C 0 {2,S}
""",
    reactant2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *3 H 1
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *1 C 0 {1,S} {5,S}
5 *2 H 0 {4,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '0.916017072113', 'd13': '2.28557228705', 'd23': '1.37128917033'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:59 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.32473135159', 'd13': '2.27628753225', 'd23': '0.953657026076'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:09 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 60,
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.3705654368', 'd13': '2.27924742614', 'd23': '0.911660449142'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:03 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 61,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {6,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5    C 0 {2,S}
6 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {5,S}
2    C 0 {1,S}
3    C 0 {5,S}
4    C 0 {5,S}
5 *3 C 1 {1,S} {3,S} {4,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.29067159232', 'd13': '2.28019861724', 'd23': '0.989683775661'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:11 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.38521629154', 'd13': '2.28865472312', 'd23': '0.904177754518'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:04 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 63,
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.3360762976', 'd13': '2.28081641878', 'd23': '0.944807825795'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:13 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 64,
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.36701470973', 'd13': '2.28295034526', 'd23': '0.917257030126'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:06 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 65,
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
5    C 0 {3,S}
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
4    C 0 {2,S}
5 *3 C 1 {3,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.36617069335', 'd13': '2.2845885535', 'd23': '0.920262865652'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:15 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 66,
    reactant1 = 
"""
1 *3 H 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {6,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4    C 0 {2,S}
5    C 0 {3,S}
6 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S} {5,S}
2    C 0 {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *3 C 1 {1,S} {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.32969490916', 'd13': '2.28108911894', 'd23': '0.953354903136'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:18 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 67,
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.38050595251', 'd13': '2.29098920012', 'd23': '0.911885694943'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:21 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 68,
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.37352301632', 'd13': '2.28503454644', 'd23': '0.913537647903'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:28 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 69,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '0.892814650986', 'd13': '2.29276767822', 'd23': '1.39995305363'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:32:46 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 70,
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.37937215782', 'd13': '2.29279020995', 'd23': '0.913652119097'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 20:33:24 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 71,
    reactant1 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,D}
2 *2 H 0 {1,S}
3    O 0 {1,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.48021', 'd13': '2.744', 'd23': '1.267'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:21:27 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 72,
    reactant1 = 
"""
1 *3 C 1 {2,D}
2    C 0 {1,D}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
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
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.304', 'd13': '2.667', 'd23': '1.366'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:21:28 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 73,
    reactant1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    O 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *3 O 1
""",
    product2 = 
"""
1    O 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.370', 'd13': '2.33824', 'd23': '1.04056932784'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:27 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 74,
    reactant1 = 
"""
1 *1 C 0 {2,D} {3,S}
2    O 0 {1,D}
3 *2 H 0 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *3 O 1 {1,S}
""",
    product1 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.201', 'd13': '1.367', 'd23': '2.537'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:27 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 75,
    reactant1 = 
"""
1 *2 H 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4    C 0 {3,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 O 1 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.224', 'd13': '2.494', 'd23': '1.274'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:27 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 76,
    reactant1 = 
"""
1    O 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3    C 0 {2,S}
4 *2 H 0 {2,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    C 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.272', 'd13': '2.712', 'd23': '1.443'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:28 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 77,
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    O 0 {1,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S} {3,S}
3    O 0 {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.14886959609', 'd13': '2.60572039885', 'd23': '1.53136943317'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:28 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 78,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 C 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 O 1 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.333', 'd13': '2.520', 'd23': '1.213'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:29 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 79,
    reactant1 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S}
2    O 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *3 C 1 {1,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S} {3,D}
2 *2 H 0 {1,S}
3    O 0 {1,D}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.4007256278', 'd13': '1.346', 'd23': '2.644'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:29 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 80,
    reactant1 = 
"""
1 *3 O 1 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3    O 0 {2,S} {4,S}
4    C 0 {3,S}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.39494', 'd13': '2.525', 'd23': '1.13285'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:30 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 81,
    reactant1 = 
"""
1    C 0 {2,S}
2 *3 O 1 {1,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *2 H 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.24091', 'd13': '2.50864801933', 'd23': '1.27440'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:30 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 82,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 C 1 {1,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.38952025866', 'd13': '2.689', 'd23': '1.31633'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:31 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 83,
    reactant1 = 
"""
1 *3 C 1 {2,D}
2    O 0 {1,D}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,D}
2 *2 H 0 {1,S}
3    O 0 {1,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.44599188466', 'd13': '2.720', 'd23': '1.29269'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:31 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 84,
    reactant1 = 
"""
1 *3 C 1
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
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.3109175145', 'd13': '2.68406', 'd23': '1.375'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:32 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 85,
    reactant1 = 
"""
1 *3 O 1
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
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.16833', 'd13': '1.427', 'd23': '1.42725'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:32 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 86,
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,D}
3 *2 H 0 {1,S}
4    O 0 {2,D}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,D}
3    O 0 {2,D}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.22694743487', 'd13': '2.46766755052', 'd23': '1.2743577649'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:33 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 87,
    reactant1 = 
"""
1 *3 O 1
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
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {3,S}
3 *3 C 1 {1,S} {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.17621185582', 'd13': '2.51378356933', 'd23': '1.35856038175'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:34 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 88,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S} {3,S}
2    C 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.32007', 'd13': '2.669', 'd23': '1.35753'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:34 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 89,
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S} {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2 *3 C 1 {1,S} {3,S}
3    O 0 {1,S} {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.17463471696', 'd13': '2.506476725', 'd23': '1.37819441443'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:34 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 90,
    reactant1 = 
"""
1 *3 O 1
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
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,D}
2 *3 C 1 {1,S}
3    C 0 {1,D}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.16169092984', 'd13': '2.59843421959', 'd23': '1.46191683065'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:35 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 91,
    reactant1 = 
"""
1 *3 C 1
""",
    reactant2 = 
"""
1 *1 C 0 {3,S} {4,S}
2    C 0 {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    O 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    product2 = 
"""
1 *1 C 0 {2,S}
2 *2 H 0 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.28724', 'd13': '2.715', 'd23': '1.43157'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:35 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 92,
    reactant1 = 
"""
1 *3 O 1
""",
    reactant2 = 
"""
1 *1 C 0 {3,S} {4,S}
2    C 0 {3,S}
3    O 0 {1,S} {2,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1 *1 O 0 {2,S}
2 *2 H 0 {1,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2 *3 C 1 {3,S}
3    O 0 {1,S} {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.19155777033', 'd13': '2.48273597758', 'd23': '1.3447797873'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:36 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 93,
    reactant1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S}
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
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.31861', 'd13': '2.689', 'd23': '1.37277'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:39 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 94,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 C 1 {1,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *2 H 0 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {3,S}
2    C 0 {3,S}
3 *3 C 1 {1,S} {2,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.36459', 'd13': '2.696', 'd23': '1.33990'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:40 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 95,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 C 1 {1,S}
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
1    O 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.39521', 'd13': '2.701', 'd23': '1.31478'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:23:41 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 96,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 C 1 {1,S}
""",
    reactant2 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *2 H 0 {1,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {4,S}
2    C 0 {4,S}
3    C 0 {4,S}
4 *3 C 1 {1,S} {2,S} {3,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.34491', 'd13': '2.695', 'd23': '1.36039'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:24:01 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 97,
    reactant1 = 
"""
1    O 0 {2,S}
2 *3 C 1 {1,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *2 H 0 {2,S}
""",
    product1 = 
"""
1    O 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 H 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2    C 0 {1,S}
3    C 0 {1,S}
4 *3 C 1 {1,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.39455', 'd13': '2.707', 'd23': '1.31571'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:24:02 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

entry(
    index = 98,
    reactant1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S}
3    C 0 {2,S}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,S} {4,S}
2 *1 C 0 {1,S} {5,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *2 H 0 {2,S}
""",
    product1 = 
"""
1 *3 C 1 {2,S}
2    C 0 {1,S} {3,S} {4,S}
3    C 0 {2,S}
4    C 0 {2,S}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,S}
4 *2 H 0 {3,S}
""",
    degeneracy = 1,
    distances = DistanceData(
        distances = {'d12': '1.30408', 'd13': '2.701', 'd23': '1.399'},
        method = 'M06-2X/6-31+G(d,p)',
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""M06-2X/6-31+G(d,p) calculation via group additive automatic TS estimator.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Jul 25 22:20:10 2013","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Found via direct estimation using automatic transition state generator"""),
    ],
)

