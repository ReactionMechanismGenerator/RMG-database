#!/usr/bin/env python
# encoding: utf-8

name = "TEOS"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    reactant1 = 
"""
Si(OC2H5)4
1     Si    0 {10,S} {11,S} {12,S} {13,S}
2     C     0 {6,S} {10,S}
3     C     0 {7,S} {11,S}
4     C     0 {8,S} {12,S}
5     C     0 {9,S} {13,S}
6     C     0 {2,S}
7     C     0 {3,S}
8     C     0 {4,S}
9     C     0 {5,S}
10    O     0 {1,S} {2,S}
11    O     0 {1,S} {3,S}
12    O     0 {1,S} {4,S}
13    O     0 {1,S} {5,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
Si(OC2H5)3OH
1     Si    0 {8,S} {9,S} {10,S} {11,S}
2     C     0 {5,S} {8,S}
3     C     0 {6,S} {9,S}
4     C     0 {7,S} {10,S}
5     C     0 {2,S}
6     C     0 {3,S}
7     C     0 {4,S}
8     O     0 {1,S} {2,S}
9     O     0 {1,S} {3,S}
10    O     0 {1,S} {4,S}
11    O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e+15,"s^-1"),
        n = 0,
        Ea = (68.552,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Reactions and modified Arrhenius parameters from:
J Herzler, JA Manion, W Tsang
"Single-Pulse Shock Tube Study of the Decomposition of Tetraethoxysilane and Related Compounds"
J. Phys. Chem. A 1997, 101, 5500-5508
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 2,
    reactant1 = 
"""
Si(OC2H5)4
1     Si    0 {10,S} {11,S} {12,S} {13,S}
2     C     0 {6,S} {10,S}
3     C     0 {7,S} {11,S}
4     C     0 {8,S} {12,S}
5     C     0 {9,S} {13,S}
6     C     0 {2,S}
7     C     0 {3,S}
8     C     0 {4,S}
9     C     0 {5,S}
10    O     0 {1,S} {2,S}
11    O     0 {1,S} {3,S}
12    O     0 {1,S} {4,S}
13    O     0 {1,S} {5,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2OSi(OC2H5)3
1     Si    0 {9,S} {10,S} {11,S} {12,S}
2     C     0 {5,S} {9,S}
3     C     0 {6,S} {10,S}
4     C     0 {7,S} {11,S}
5     C     0 {2,S}
6     C     0 {3,S}
7     C     0 {4,S}
8     C     1 {12,S}
9     O     0 {1,S} {2,S}
10    O     0 {1,S} {3,S}
11    O     0 {1,S} {4,S}
12    O     0 {1,S} {8,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.981e+17,"s^-1"),
        n = 0,
        Ea = (86.037,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 3,
    reactant1 = 
"""
Si(OC2H5)3OH
1     Si    0 {8,S} {9,S} {10,S} {11,S}
2     C     0 {5,S} {8,S}
3     C     0 {6,S} {9,S}
4     C     0 {7,S} {10,S}
5     C     0 {2,S}
6     C     0 {3,S}
7     C     0 {4,S}
8     O     0 {1,S} {2,S}
9     O     0 {1,S} {3,S}
10    O     0 {1,S} {4,S}
11    O     0 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
Si(OC2H5)2(OH)2
1     Si    0 {6,S} {7,S} {8,S} {9,S}
2     C     0 {4,S} {6,S}
3     C     0 {5,S} {7,S}
4     C     0 {2,S}
5     C     0 {3,S}
6     O     0 {1,S} {2,S}
7     O     0 {1,S} {3,S}
8     O     0 {1,S}
9     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.585e+15,"s^-1"),
        n = 0,
        Ea = (68.552,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 4,
    reactant1 = 
"""
Si(OC2H5)3OH
1     Si    0 {8,S} {9,S} {10,S} {11,S}
2     C     0 {5,S} {8,S}
3     C     0 {6,S} {9,S}
4     C     0 {7,S} {10,S}
5     C     0 {2,S}
6     C     0 {3,S}
7     C     0 {4,S}
8     O     0 {1,S} {2,S}
9     O     0 {1,S} {3,S}
10    O     0 {1,S} {4,S}
11    O     0 {1,S}
""",
    product1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
O_Si(OC2H5)2
1     C     0 {3,S} {6,S}
2     C     0 {4,S} {7,S}
3     C     0 {1,S}
4     C     0 {2,S}
5     Si    0 {6,S} {7,S} {8,D}
6     O     0 {1,S} {5,S}
7     O     0 {2,S} {5,S}
8     O     0 {5,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.012e+11,"s^-1"),
        n = 0,
        Ea = (45.105,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 5,
    reactant1 = 
"""
Si(OC2H5)3OH
1     Si    0 {8,S} {9,S} {10,S} {11,S}
2     C     0 {5,S} {8,S}
3     C     0 {6,S} {9,S}
4     C     0 {7,S} {10,S}
5     C     0 {2,S}
6     C     0 {3,S}
7     C     0 {4,S}
8     O     0 {1,S} {2,S}
9     O     0 {1,S} {3,S}
10    O     0 {1,S} {4,S}
11    O     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2OSi(OC2H5)2OH
1     Si    0 {7,S} {8,S} {9,S} {10,S}
2     C     0 {4,S} {7,S}
3     C     0 {5,S} {8,S}
4     C     0 {2,S}
5     C     0 {3,S}
6     C     1 {9,S}
7     O     0 {1,S} {2,S}
8     O     0 {1,S} {3,S}
9     O     0 {1,S} {6,S}
10    O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.162e+17,"s^-1"),
        n = 0,
        Ea = (86.037,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 6,
    reactant1 = 
"""
Si(OC2H5)2(OH)2
1     Si    0 {6,S} {7,S} {8,S} {9,S}
2     C     0 {4,S} {6,S}
3     C     0 {5,S} {7,S}
4     C     0 {2,S}
5     C     0 {3,S}
6     O     0 {1,S} {2,S}
7     O     0 {1,S} {3,S}
8     O     0 {1,S}
9     O     0 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
Si(OC2H5)(OH)3
1     C     0 {3,S} {4,S}
2     Si    0 {4,S} {5,S} {6,S} {7,S}
3     C     0 {1,S}
4     O     0 {1,S} {2,S}
5     O     0 {2,S}
6     O     0 {2,S}
7     O     0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (68.552,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 7,
    reactant1 = 
"""
Si(OC2H5)2(OH)2
1     Si    0 {6,S} {7,S} {8,S} {9,S}
2     C     0 {4,S} {6,S}
3     C     0 {5,S} {7,S}
4     C     0 {2,S}
5     C     0 {3,S}
6     O     0 {1,S} {2,S}
7     O     0 {1,S} {3,S}
8     O     0 {1,S}
9     O     0 {1,S}
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
O_Si(OC2H5)2
1     C     0 {3,S} {6,S}
2     C     0 {4,S} {7,S}
3     C     0 {1,S}
4     C     0 {2,S}
5     Si    0 {6,S} {7,S} {8,D}
6     O     0 {1,S} {5,S}
7     O     0 {2,S} {5,S}
8     O     0 {5,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.012e+11,"s^-1"),
        n = 0,
        Ea = (39.74,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8,
    reactant1 = 
"""
Si(OC2H5)2(OH)2
1     Si    0 {6,S} {7,S} {8,S} {9,S}
2     C     0 {4,S} {6,S}
3     C     0 {5,S} {7,S}
4     C     0 {2,S}
5     C     0 {3,S}
6     O     0 {1,S} {2,S}
7     O     0 {1,S} {3,S}
8     O     0 {1,S}
9     O     0 {1,S}
""",
    product1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
O_Si(OC2H5)OH
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     Si    0 {4,S} {5,S} {6,D}
4     O     0 {1,S} {3,S}
5     O     0 {3,S}
6     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+11,"s^-1"),
        n = 0,
        Ea = (45.105,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 9,
    reactant1 = 
"""
Si(OC2H5)2(OH)2
1     Si    0 {6,S} {7,S} {8,S} {9,S}
2     C     0 {4,S} {6,S}
3     C     0 {5,S} {7,S}
4     C     0 {2,S}
5     C     0 {3,S}
6     O     0 {1,S} {2,S}
7     O     0 {1,S} {3,S}
8     O     0 {1,S}
9     O     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2OSi(OC2H5)(OH)2
1     Si    0 {5,S} {6,S} {7,S} {8,S}
2     C     0 {3,S} {5,S}
3     C     0 {2,S}
4     C     1 {6,S}
5     O     0 {1,S} {2,S}
6     O     0 {1,S} {4,S}
7     O     0 {1,S}
8     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e+17,"s^-1"),
        n = 0,
        Ea = (86.037,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 10,
    reactant1 = 
"""
Si(OC2H5)(OH)3
1     C     0 {3,S} {4,S}
2     Si    0 {4,S} {5,S} {6,S} {7,S}
3     C     0 {1,S}
4     O     0 {1,S} {2,S}
5     O     0 {2,S}
6     O     0 {2,S}
7     O     0 {2,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
Si(OH)4
1     Si    0 {2,S} {3,S} {4,S} {5,S}
2     O     0 {1,S}
3     O     0 {1,S}
4     O     0 {1,S}
5     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (68.552,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 11,
    reactant1 = 
"""
Si(OC2H5)(OH)3
1     C     0 {3,S} {4,S}
2     Si    0 {4,S} {5,S} {6,S} {7,S}
3     C     0 {1,S}
4     O     0 {1,S} {2,S}
5     O     0 {2,S}
6     O     0 {2,S}
7     O     0 {2,S}
""",
    product1 = 
"""
H2O
1     O     0
""",
    product2 = 
"""
O_Si(OC2H5)OH
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     Si    0 {4,S} {5,S} {6,D}
4     O     0 {1,S} {3,S}
5     O     0 {3,S}
6     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.012e+11,"s^-1"),
        n = 0,
        Ea = (39.74,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 12,
    reactant1 = 
"""
Si(OC2H5)(OH)3
1     C     0 {3,S} {4,S}
2     Si    0 {4,S} {5,S} {6,S} {7,S}
3     C     0 {1,S}
4     O     0 {1,S} {2,S}
5     O     0 {2,S}
6     O     0 {2,S}
7     O     0 {2,S}
""",
    product1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
O_Si(OH)2
1     Si    0 {2,S} {3,S} {4,D}
2     O     0 {1,S}
3     O     0 {1,S}
4     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.012e+11,"s^-1"),
        n = 0,
        Ea = (45.105,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 13,
    reactant1 = 
"""
Si(OC2H5)(OH)3
1     C     0 {3,S} {4,S}
2     Si    0 {4,S} {5,S} {6,S} {7,S}
3     C     0 {1,S}
4     O     0 {1,S} {2,S}
5     O     0 {2,S}
6     O     0 {2,S}
7     O     0 {2,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2OSi(OH)3
1     Si    0 {3,S} {4,S} {5,S} {6,S}
2     C     1 {3,S}
3     O     0 {1,S} {2,S}
4     O     0 {1,S}
5     O     0 {1,S}
6     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+17,"s^-1"),
        n = 0,
        Ea = (86.037,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 14,
    reactant1 = 
"""
O_Si(OC2H5)2
1     C     0 {3,S} {6,S}
2     C     0 {4,S} {7,S}
3     C     0 {1,S}
4     C     0 {2,S}
5     Si    0 {6,S} {7,S} {8,D}
6     O     0 {1,S} {5,S}
7     O     0 {2,S} {5,S}
8     O     0 {5,D}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
O_Si(OC2H5)OH
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     Si    0 {4,S} {5,S} {6,D}
4     O     0 {1,S} {3,S}
5     O     0 {3,S}
6     O     0 {3,D}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1e+13,"s^-1"), n=0, Ea=(52.059,"kcal/mol"), T0=(1,"K")),
            Arrhenius(A=(1e+15,"s^-1"), n=0, Ea=(68.552,"kcal/mol"), T0=(1,"K"))
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 16,
    reactant1 = 
"""
O_Si(OC2H5)2
1     C     0 {3,S} {6,S}
2     C     0 {4,S} {7,S}
3     C     0 {1,S}
4     C     0 {2,S}
5     Si    0 {6,S} {7,S} {8,D}
6     O     0 {1,S} {5,S}
7     O     0 {2,S} {5,S}
8     O     0 {5,D}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2OSiO(OC2H5)
1     C     0 {2,S} {5,S}
2     C     0 {1,S}
3     Si    0 {5,S} {6,S} {7,D}
4     C     1 {6,S}
5     O     0 {1,S} {3,S}
6     O     0 {3,S} {4,S}
7     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e+17,"s^-1"),
        n = 0,
        Ea = (86.037,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 17,
    reactant1 = 
"""
O_Si(OC2H5)OH
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     Si    0 {4,S} {5,S} {6,D}
4     O     0 {1,S} {3,S}
5     O     0 {3,S}
6     O     0 {3,D}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
O_Si(OH)2
1     Si    0 {2,S} {3,S} {4,D}
2     O     0 {1,S}
3     O     0 {1,S}
4     O     0 {1,D}
""",
    degeneracy = 1,
    duplicate = True,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(5.012e+12,"s^-1"), n=0, Ea=(52.059,"kcal/mol"), T0=(1,"K")),
            Arrhenius(A=(5.012e+14,"s^-1"), n=0, Ea=(68.552,"kcal/mol"), T0=(1,"K"))
        ],
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 19,
    reactant1 = 
"""
O_Si(OC2H5)OH
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     Si    0 {4,S} {5,S} {6,D}
4     O     0 {1,S} {3,S}
5     O     0 {3,S}
6     O     0 {3,D}
""",
    product1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
SiO2
1     Si    0 {2,D} {3,D}
2     O     0 {1,D}
3     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.585e+11,"s^-1"),
        n = 0,
        Ea = (47.092,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 20,
    reactant1 = 
"""
O_Si(OC2H5)OH
1     C     0 {2,S} {4,S}
2     C     0 {1,S}
3     Si    0 {4,S} {5,S} {6,D}
4     O     0 {1,S} {3,S}
5     O     0 {3,S}
6     O     0 {3,D}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2OSiO(OH)
1     Si    0 {3,S} {4,S} {5,D}
2     C     1 {3,S}
3     O     0 {1,S} {2,S}
4     O     0 {1,S}
5     O     0 {1,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+17,"s^-1"),
        n = 0,
        Ea = (86.037,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 21,
    reactant1 = 
"""
CH3OSi(OC2H5)2(OC2H3)
1     Si    0 {9,S} {10,S} {11,S} {12,S}
2     C     0 {4,S} {9,S}
3     C     0 {5,S} {10,S}
4     C     0 {2,S}
5     C     0 {3,S}
6     C     0 {11,S}
7     C     0 {8,D} {12,S}
8     C     0 {7,D}
9     O     0 {1,S} {2,S}
10    O     0 {1,S} {3,S}
11    O     0 {1,S} {6,S}
12    O     0 {1,S} {7,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH3OSi(OC2H5)(OC2H3)OH
1     Si    0 {7,S} {8,S} {9,S} {10,S}
2     C     0 {3,S} {7,S}
3     C     0 {2,S}
4     C     0 {8,S}
5     C     0 {6,D} {9,S}
6     C     0 {5,D}
7     O     0 {1,S} {2,S}
8     O     0 {1,S} {4,S}
9     O     0 {1,S} {5,S}
10    O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (68.552,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2OSi(OC2H5)3 = CH3OSi(OC2H5)2(OC2H3) + H
CH2OSi(OC2H5)2OH = CH3OSi(OC2H5)(OC2H3)OH + H
CH2OSi(OC2H5)(OH)2 = CH3OSi(OC2H3)(OH)2 + H
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 22,
    reactant1 = 
"""
CH3OSi(OC2H5)2(OC2H3)
1     Si    0 {9,S} {10,S} {11,S} {12,S}
2     C     0 {4,S} {9,S}
3     C     0 {5,S} {10,S}
4     C     0 {2,S}
5     C     0 {3,S}
6     C     0 {11,S}
7     C     0 {8,D} {12,S}
8     C     0 {7,D}
9     O     0 {1,S} {2,S}
10    O     0 {1,S} {3,S}
11    O     0 {1,S} {6,S}
12    O     0 {1,S} {7,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2OSi(OC2H5)(OC2H3)(OCH3)
1     Si    0 {8,S} {9,S} {10,S} {11,S}
2     C     0 {3,S} {8,S}
3     C     0 {2,S}
4     C     0 {9,S}
5     C     0 {6,D} {10,S}
6     C     0 {5,D}
7     C     1 {11,S}
8     O     0 {1,S} {2,S}
9     O     0 {1,S} {4,S}
10    O     0 {1,S} {5,S}
11    O     0 {1,S} {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.995e+17,"s^-1"),
        n = 0,
        Ea = (86.037,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 23,
    reactant1 = 
"""
CH3OSi(OC2H5)(OC2H3)OH
1     Si    0 {7,S} {8,S} {9,S} {10,S}
2     C     0 {3,S} {7,S}
3     C     0 {2,S}
4     C     0 {8,S}
5     C     0 {6,D} {9,S}
6     C     0 {5,D}
7     O     0 {1,S} {2,S}
8     O     0 {1,S} {4,S}
9     O     0 {1,S} {5,S}
10    O     0 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
CH3OSi(OC2H3)(OH)2
1     Si    0 {5,S} {6,S} {7,S} {8,S}
2     C     0 {5,S}
3     C     0 {4,D} {6,S}
4     C     0 {3,D}
5     O     0 {1,S} {2,S}
6     O     0 {1,S} {3,S}
7     O     0 {1,S}
8     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.012e+14,"s^-1"),
        n = 0,
        Ea = (68.552,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
CH2OSi(OC2H5)(OC2H3)(OCH3) = SI(OCH3)2(C2H3)2 + H
""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 24,
    reactant1 = 
"""
CH3OSi(OC2H5)(OC2H3)OH
1     Si    0 {7,S} {8,S} {9,S} {10,S}
2     C     0 {3,S} {7,S}
3     C     0 {2,S}
4     C     0 {8,S}
5     C     0 {6,D} {9,S}
6     C     0 {5,D}
7     O     0 {1,S} {2,S}
8     O     0 {1,S} {4,S}
9     O     0 {1,S} {5,S}
10    O     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2OSi(OCH3)(OC2H3)OH
1     Si    0 {6,S} {7,S} {8,S} {9,S}
2     C     0 {6,S}
3     C     0 {4,D} {7,S}
4     C     0 {3,D}
5     C     1 {8,S}
6     O     0 {1,S} {2,S}
7     O     0 {1,S} {3,S}
8     O     0 {1,S} {5,S}
9     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+17,"s^-1"),
        n = 0,
        Ea = (86.037,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 25,
    reactant1 = 
"""
CH3OSi(OC2H5)(OC2H3)OH
1     Si    0 {7,S} {8,S} {9,S} {10,S}
2     C     0 {3,S} {7,S}
3     C     0 {2,S}
4     C     0 {8,S}
5     C     0 {6,D} {9,S}
6     C     0 {5,D}
7     O     0 {1,S} {2,S}
8     O     0 {1,S} {4,S}
9     O     0 {1,S} {5,S}
10    O     0 {1,S}
""",
    product1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product2 = 
"""
CH3OSi(O)OC2H3
1     C     0 {5,S}
2     C     0 {4,D} {6,S}
3     Si    0 {5,S} {6,S} {7,D}
4     C     0 {2,D}
5     O     0 {1,S} {3,S}
6     O     0 {2,S} {3,S}
7     O     0 {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.585e+11,"s^-1"),
        n = 0,
        Ea = (45.105,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 26,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product1 = 
"""
C2H4
1     C     0 {2,D}
2     C     0 {1,D}
""",
    product2 = 
"""
H2O
1     O     0
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+13,"s^-1"),
        n = 0,
        Ea = (66.167,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 27,
    reactant1 = 
"""
C2H5OH
1     C     0 {2,S} {3,S}
2     C     0 {1,S}
3     O     0 {1,S}
""",
    product1 = 
"""
CH3
1     C     1
""",
    product2 = 
"""
CH2OH
1     C     1 {2,S}
2     O     0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (83.057,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("2011-07-26","Richard West <rwest@mit.edu>","action","""Richard West <rwest@mit.edu> imported this entry from the old RMG database."""),
    ],
)

