#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DMS"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
CS2H2(2)
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HJ
1 H 1
""",
    product1 = 
"""
CS2H(2)J
1 S 0 {2,S} {3,S}
2 C 1 {1,S} {3,S} {4,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(17400, 'cm^3/(mol*s)'), n=2.9, Ea=(5.87, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
CS2H2(2)
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH3J
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CS2H(2)J
1 S 0 {2,S} {3,S}
2 C 1 {1,S} {3,S} {4,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000155, 'cm^3/(mol*s)'),
        n = 5.06,
        Ea = (4.73, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
CS2H2(2)
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
HSJ
1 S 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
CS2H(2)J
1 S 0 {2,S} {3,S}
2 C 1 {1,S} {3,S} {4,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
""",
    product2 = 
"""
H2S
1 S 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(156, 'cm^3/(mol*s)'), n=3.53, Ea=(8.32, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
CS2H2(2)
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH3SJ
1 S 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 H 0 {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CS2H(2)J
1 S 0 {2,S} {3,S}
2 C 1 {1,S} {3,S} {4,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
""",
    product2 = 
"""
CH3SH
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {4,S} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {2,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(22.9, 'cm^3/(mol*s)'), n=3.69, Ea=(11.61, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
CH3SSCH2J
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 {1,S} {3,S}
3 S 0 {2,S} {4,S}
4 C 1 {3,S} {8,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    product1 = 
"""
CH3SCH2SJ
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 S 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (313000000000.0, 's^-1'),
        n = 0.22,
        Ea = (31.93, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
CH2S
1 C 0 {2,D} {3,S} {4,S}
2 S 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3SJ
1 S 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 H 0 {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH3SSCH2J
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 {1,S} {3,S}
3 S 0 {2,S} {4,S}
4 C 1 {3,S} {8,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25500, 'cm^3/(mol*s)'),
        n = 2.77,
        Ea = (-2.31, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
CH2S
1 C 0 {2,D} {3,S} {4,S}
2 S 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3SJ
1 S 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 H 0 {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CH3SCH2SJ
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 S 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.79,
        Ea = (-2.27, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
CH3CH2SSCH2J
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  S 0 {2,S} {4,S}
4  S 0 {3,S} {5,S}
5  C 1 {4,S} {11,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {5,S}
12 H 0 {5,S}
""",
    product1 = 
"""
CH3CH2SCH2SJ
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  S 0 {2,S} {4,S}
4  C 0 {3,S} {5,S} {11,S} {12,S}
5  S 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {4,S}
12 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (313000000000.0, 's^-1'),
        n = 0.22,
        Ea = (31.93, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
CH2S
1 C 0 {2,D} {3,S} {4,S}
2 S 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3CH2SJ
1 S 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 C 0 {2,S} {6,S} {7,S} {8,S}
4 H 0 {2,S}
5 H 0 {2,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH3CH2SSCH2J
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  S 0 {2,S} {4,S}
4  S 0 {3,S} {5,S}
5  C 1 {4,S} {11,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {5,S}
12 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (25500, 'cm^3/(mol*s)'),
        n = 2.77,
        Ea = (-2.31, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
CH2S
1 C 0 {2,D} {3,S} {4,S}
2 S 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3CH2SJ
1 S 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 C 0 {2,S} {6,S} {7,S} {8,S}
4 H 0 {2,S}
5 H 0 {2,S}
6 H 0 {3,S}
7 H 0 {3,S}
8 H 0 {3,S}
""",
    product1 = 
"""
CH3CH2SCH2SJ
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  S 0 {2,S} {4,S}
4  C 0 {3,S} {5,S} {11,S} {12,S}
5  S 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {4,S}
12 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.79,
        Ea = (-2.27, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
CS2H2(2)
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH3J
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3SSCH2J
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 {1,S} {3,S}
3 S 0 {2,S} {4,S}
4 C 1 {3,S} {8,S} {9,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {4,S}
9 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3120, 'cm^3/(mol*s)'), n=2.72, Ea=(7.28, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
CS2H2(2)
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
CH3J
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
CH3SCH2SJ
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 {1,S} {3,S}
3 C 0 {2,S} {4,S} {8,S} {9,S}
4 S 1 {3,S}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
8 H 0 {3,S}
9 H 0 {3,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6180, 'cm^3/(mol*s)'), n=2.57, Ea=(-1.16, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
CS2H2(2)
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
C2H5J
1 C 1 {2,S} {3,S} {4,S}
2 C 0 {1,S} {5,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3CH2SSCH2J
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  S 0 {2,S} {4,S}
4  S 0 {3,S} {5,S}
5  C 1 {4,S} {11,S} {12,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {5,S}
12 H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3120, 'cm^3/(mol*s)'), n=2.72, Ea=(7.28, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
CS2H2(2)
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    reactant2 = 
"""
C2H5J
1 C 1 {2,S} {3,S} {4,S}
2 C 0 {1,S} {5,S} {6,S} {7,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {2,S}
6 H 0 {2,S}
7 H 0 {2,S}
""",
    product1 = 
"""
CH3CH2SCH2SJ
1  C 0 {2,S} {6,S} {7,S} {8,S}
2  C 0 {1,S} {3,S} {9,S} {10,S}
3  S 0 {2,S} {4,S}
4  C 0 {3,S} {5,S} {11,S} {12,S}
5  S 1 {4,S}
6  H 0 {1,S}
7  H 0 {1,S}
8  H 0 {1,S}
9  H 0 {2,S}
10 H 0 {2,S}
11 H 0 {4,S}
12 H 0 {4,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6180, 'cm^3/(mol*s)'), n=2.57, Ea=(-1.16, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 15,
    reactant1 = 
"""
CS2H2JJ
1 S 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 1 {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    product1 = 
"""
CS2H2(2)
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20800000000.0, 's^-1'), n=1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    reactant1 = 
"""
CS2H(2)J
1 S 0 {2,S} {3,S}
2 C 1 {1,S} {3,S} {4,S}
3 S 0 {1,S} {2,S}
4 H 0 {2,S}
""",
    product1 = 
"""
CS2H(1)J
1 S 1 {2,S}
2 C 0 {1,S} {3,D} {4,S}
3 S 0 {2,D}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20800000000.0, 's^-1'), n=1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
CS2H2JJ
1 S 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 S 1 {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    product1 = 
"""
HJ
1 H 1
""",
    product2 = 
"""
CS2H(1)J
1 S 1 {2,S}
2 C 0 {1,S} {3,D} {4,S}
3 S 0 {2,D}
4 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3190000000.0, 's^-1'), n=1.55, Ea=(36.55, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 18,
    reactant1 = 
"""
CS2H(1)J
1 S 1 {2,S}
2 C 0 {1,S} {3,D} {4,S}
3 S 0 {2,D}
4 H 0 {2,S}
""",
    product1 = 
"""
CS2
1 S 0 {2,D}
2 C 0 {1,D} {3,D}
3 S 0 {2,D}
""",
    product2 = 
"""
HJ
1 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(252000000.0, 's^-1'), n=1.74, Ea=(30.56, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
CH2S
1 C 0 {2,D} {3,S} {4,S}
2 S 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HJ
1 H 1
""",
    product1 = 
"""
HCSJ
1 C 1 {2,D} {3,S}
2 S 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
H2
1 H 0 {2,S}
2 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(95000, 'cm^3/(mol*s)'), n=2.72, Ea=(3.68, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
CH2S
1 C 0 {2,D} {3,S} {4,S}
2 S 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3J
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    product1 = 
"""
HCSJ
1 C 1 {2,D} {3,S}
2 S 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
CH4
1 C 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
5 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.0033, 'cm^3/(mol*s)'), n=4.85, Ea=(3.8, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
CH2S
1 C 0 {2,D} {3,S} {4,S}
2 S 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
HSJ
1 S 1 {2,S}
2 H 0 {1,S}
""",
    product1 = 
"""
HCSJ
1 C 1 {2,D} {3,S}
2 S 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
H2S
1 S 0 {2,S} {3,S}
2 H 0 {1,S}
3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(127, 'cm^3/(mol*s)'), n=3.7, Ea=(1.93, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
CH2S
1 C 0 {2,D} {3,S} {4,S}
2 S 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    reactant2 = 
"""
CH3SJ
1 S 1 {2,S}
2 C 0 {1,S} {3,S} {4,S} {5,S}
3 H 0 {2,S}
4 H 0 {2,S}
5 H 0 {2,S}
""",
    product1 = 
"""
HCSJ
1 C 1 {2,D} {3,S}
2 S 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
CH3SH
1 S 0 {2,S} {3,S}
2 C 0 {1,S} {4,S} {5,S} {6,S}
3 H 0 {1,S}
4 H 0 {2,S}
5 H 0 {2,S}
6 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.49, 'cm^3/(mol*s)'), n=3.96, Ea=(5.36, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
C2H3S2(1)J
1 C 1 {2,S} {5,S} {6,S}
2 S 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {7,S}
4 S 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product1 = 
"""
HCSJ
1 C 1 {2,D} {3,S}
2 S 0 {1,D}
3 H 0 {1,S}
""",
    product2 = 
"""
CH2S
1 C 0 {2,D} {3,S} {4,S}
2 S 0 {1,D}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (852000000000000.0, 's^-1'),
        n = -0.05,
        Ea = (36.87, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
C2H3S2(1)J
1 C 1 {2,S} {5,S} {6,S}
2 S 0 {1,S} {3,S}
3 C 0 {2,S} {4,D} {7,S}
4 S 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {3,S}
""",
    product1 = 
"""
C2H3S2(2)J
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 S 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.2e-21, 's^-1'), n=9.96, Ea=(19.14, 'kcal/mol'), T0=(1, 'K')),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
C2H3S2(2)J
1 C 0 {2,S} {5,S} {6,S} {7,S}
2 S 0 {1,S} {3,S}
3 C 1 {2,S} {4,D}
4 S 0 {3,D}
5 H 0 {1,S}
6 H 0 {1,S}
7 H 0 {1,S}
""",
    product1 = 
"""
CS2
1 S 0 {2,D}
2 C 0 {1,D} {3,D}
3 S 0 {2,D}
""",
    product2 = 
"""
CH3J
1 C 1 {2,S} {3,S} {4,S}
2 H 0 {1,S}
3 H 0 {1,S}
4 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2220000000000.0, 's^-1'),
        n = 0.67,
        Ea = (10.64, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Nov 15 16:45:30 2012","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

