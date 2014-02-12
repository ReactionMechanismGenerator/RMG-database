#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/TS_training"
shortDesc = u"Distances used to train group additivity values for TS geometries"
longDesc = u"""
Put interatomic distances for reactions to use as a training set for fitting
group additivity values in this file.
"""
recommended = True

# recipe(actions=[
#     ['CHANGE_BOND', '*1', '-1', '*2'],
#     ['FORM_BOND', '*1', 'S', '*3'],
#     ['GAIN_RADICAL', '*2', '1'],
#     ['LOSE_RADICAL', '*3', '1'],
# ])

entry(
    index = 1,
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2 *2 C 1 {1,S}
3 *3 H 0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.34016', 'd13': '2.29179', 'd23': '2.97297'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 C 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.36006', 'd13': '2.34603', 'd23': '3.08317'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D} {3,S}
3    C 0 {2,S}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 1 {1,S} {3,S}
3 *1 C 0 {2,S} {4,S}
4 *3 C 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.36221', 'd13': '2.34488', 'd23': '3.08163'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3    C 0 {2,S}
4 *2 C 0 {2,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S} {5,S}
3    C 0 {2,S}
4 *3 C 0 {2,S}
5 *2 C 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.37248', 'd13': '2.31062', 'd23': '2.88000'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,D}
3    C 0 {2,S}
4 *1 C 0 {2,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 C 1 {2,S} {4,S} {5,S}
4    C 0 {3,S}
5    C 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.37248', 'd13': '2.31062', 'd23': '2.88000'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 O 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.23467', 'd13': '2.24113', 'd23': '2.80911'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
1 *2 C 0 {2,D}
2 *1 O 0 {1,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 C 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.25974', 'd13': '1.95615', 'd23': '2.81003'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 S 0 {1,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 C 0 {1,S} {3,S}
3 *2 S 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.63224', 'd13': '2.73871', 'd23': '3.65010'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S}
3 *3 C 0 {2,S}
4 *2 O 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.24443', 'd13': '2.17044', 'd23': '2.68356'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,D}
3 *1 O 0 {2,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 C 1 {2,S} {4,S}
4    C 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.26829', 'd13': '1.91478', 'd23': '2.77240'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,S} {4,D}
3    C 0 {2,S}
4 *1 O 0 {2,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 C 1 {2,S} {4,S} {5,S}
4    C 0 {3,S}
5    C 0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.27681', 'd13': '1.89043', 'd23': '2.75326'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3    C 0 {2,S}
4 *2 O 0 {2,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S} {5,S}
3 *3 C 0 {2,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.25449', 'd13': '2.13715', 'd23': '2.59901'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,D}
3    C 0 {2,S}
4 *2 S 0 {2,D}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,S} {4,S} {5,S}
3 *3 C 0 {2,S}
4    C 0 {2,S}
5 *2 S 1 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': '1.66891', 'd13': '2.49399', 'd23': '3.17189'},
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
        ("Tue Jan 15 11:01:59 2014","Pierre Bhoorasingh <bhoorasingh.p@husky.neu.edu>","action","""Estimated and optimized in G09"""),
    ],
)
