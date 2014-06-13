#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Diels_alder/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["cyclohexene"], products=["open"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['CHANGE_BOND', '*1', '1', '*2'],
    ['CHANGE_BOND', '*3', '1', '*4'],
    ['CHANGE_BOND', '*2', '-1', '*3'],
    ['CHANGE_BOND', '*5', '1', '*6'],
    ['BREAK_BOND', '*1', 'S', '*6'],
    ['BREAK_BOND', '*4', 'S', '*5'],
])

entry(
    index = 1,
    label = "cyclohexene",
    group = "OR{cyclohexene_1inring, cyclohexene_2inring, cyclohexene_3inring, cyclohexene_4inring}",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "cyclohexene_1inring",
    group = 
"""
1 *1 R!H 0 {2,S} {6,S}
2 *2 R!H 0 {1,S} {3,D}
3 *3 R!H 0 {2,D} {4,S}
4 *4 R!H 0 {3,S} {5,S} {7,S}
5 *5 R!H 0 {4,S} {6,S} {7,S}
6 *6 R!H 0 {1,S} {5,S}
7    R!H 0 {4,S} {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "cyclohexene_2inring",
    group = 
"""
1 *1 R!H 0 {2,S} {6,S}
2 *2 R!H 0 {1,S} {3,D}
3 *3 R!H 0 {2,D} {4,S}
4 *4 R!H 0 {3,S} {5,S} {7,S}
5 *5 R!H 0 {4,S} {6,S} {8,S}
6 *6 R!H 0 {1,S} {5,S}
7    R!H 0 {4,S} {8,{S,D}}
8    R!H 0 {5,S} {7,{S,D}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "cyclohexene_3inring",
    group = 
"""
1 *1 R!H 0 {2,S} {6,S}
2 *2 R!H 0 {1,S} {3,D}
3 *3 R!H 0 {2,D} {4,S}
4 *4 R!H 0 {3,S} {5,S} {7,S}
5 *5 R!H 0 {4,S} {6,S} {9,S}
6 *6 R!H 0 {1,S} {5,S}
7    R!H 0 {4,S} {8,{S,D}}
8    R!H 0 {7,{S,D}} {9,{S,D}}
9    R!H 0 {5,S} {8,{S,D}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 5,
    label = "cyclohexene_4inring",
    group = 
"""
1  *1 R!H 0 {2,S} {6,S}
2  *2 R!H 0 {1,S} {3,D}
3  *3 R!H 0 {2,D} {4,S}
4  *4 R!H 0 {3,S} {5,S} {7,S}
5  *5 R!H 0 {4,S} {6,S} {10,S}
6  *6 R!H 0 {1,S} {5,S}
7     R!H 0 {4,S} {8,{S,D}}
8     R!H 0 {7,{S,D}} {9,{S,D}}
9     R!H 0 {8,{S,D}} {10,{S,D}}
10    R!H 0 {5,S} {9,{S,D}}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

tree(
"""
L1: cyclohexene
    L2: cyclohexene_1inring
    L2: cyclohexene_2inring
    L2: cyclohexene_3inring
    L2: cyclohexene_4inring
"""
)

forbidden(
    label = "two5rings",
    group = 
"""
1     C 0 {2,S} {4,S} {5,S} {10,S}
2  *4 C 0 {1,S} {3,S} {16,S}
3  *3 C 0 {2,S} {6,S} {11,D}
4     H 0 {1,S}
5     H 0 {1,S}
6     H 0 {3,S}
7  *1 C 0 {8,S} {11,S} {12,S}
8  *6 C 0 {7,S} {9,S} {13,S}
9  *5 C 0 {8,S} {10,S} {14,S}
10    C 0 {1,S} {9,S} {11,S} {15,S}
11 *2 C 0 {3,D} {7,S} {10,S}
12    H 0 {7,S}
13    H 0 {8,S}
14    H 0 {9,S}
15    H 0 {10,S}
16    H 0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
    ],
)

