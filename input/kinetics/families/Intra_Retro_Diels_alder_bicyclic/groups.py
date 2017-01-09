#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Retro_Diels_alder_bicyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["cyclohexene"], products=["open"], ownReverse=False)

reverse = "ringopening"

recipe(actions=[
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['CHANGE_BOND', '*5', 1, '*6'],
    ['BREAK_BOND', '*1', 1, '*6'],
    ['BREAK_BOND', '*4', 1, '*5'],
])

entry(
    index = 1,
    label = "cyclohexene",
    group = "OR{cyclohexene_1inring, cyclohexene_2inring, cyclohexene_3inring, cyclohexene_4inring}",
    kinetics = None,
)

entry(
    index = 2,
    label = "cyclohexene_1inring",
    group = 
"""
1  *1 R!H u0 {6,S} {2,S} {8,S} {9,S}
2  *2 R!H u0 {1,S} {3,D}
3  *3 R!H u0 {2,D} {4,S}
4  *4 R!H u0 {3,S} {5,S} {7,S} {10,S}
5  *5 R!H u0 {4,S} {6,S} {7,S}
6  *6 R!H u0 {1,S} {5,S}
7     R!H u0 {4,S} {5,S}
8  *7 R   u0 {1,S}
9  *8 R   u0 {1,S}
10 *9 R   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "cyclohexene_2inring",
    group = 
"""
1 *1 R!H u0 {2,S} {6,S} {9,S} {10,S}
2 *2 R!H u0 {1,S} {3,D}
3 *3 R!H u0 {2,D} {4,S}
4 *4 R!H u0 {3,S} {5,S} {7,S} {11,S}
5 *5 R!H u0 {4,S} {6,S} {8,S}
6 *6 R!H u0 {1,S} {5,S}
7    R!H u0 {4,S} {8,[S,D]}
8    R!H u0 {5,S} {7,[S,D]}
9  *7 R  u0 {1,S}
10 *8 R  u0 {1,S}
11 *9 R  u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "cyclohexene_3inring",
    group = 
"""
1 *1 R!H u0 {2,S} {6,S} {10,S} {11,S}
2 *2 R!H u0 {1,S} {3,D}
3 *3 R!H u0 {2,D} {4,S}
4 *4 R!H u0 {3,S} {5,S} {7,S} {12,S}
5 *5 R!H u0 {4,S} {6,S} {9,S}
6 *6 R!H u0 {1,S} {5,S}
7    R!H u0 {4,S} {8,[S,D]}
8    R!H u0 {7,[S,D]} {9,[S,D]}
9    R!H u0 {5,S} {8,[S,D]}
10 *7 R u0 {1,S}
11 *8 R u0 {1,S}
12 *9 R u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "cyclohexene_4inring",
    group = 
"""
1  *1 R!H u0 {2,S} {6,S} {11,S} {12,S}
2  *2 R!H u0 {1,S} {3,D}
3  *3 R!H u0 {2,D} {4,S}
4  *4 R!H u0 {3,S} {5,S} {7,S} {13,S}
5  *5 R!H u0 {4,S} {6,S} {10,S}
6  *6 R!H u0 {1,S} {5,S}
7     R!H u0 {4,S} {8,[S,D]}
8     R!H u0 {7,[S,D]} {9,[S,D]}
9     R!H u0 {8,[S,D]} {10,[S,D]}
10    R!H u0 {5,S} {9,[S,D]}
11 *7 R u0 {1,S}
12 *8 R u0 {1,S}
13 *9 R u0 {4,S}
""",
    kinetics = None,
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
1     C u0 {2,S} {4,S} {5,S} {10,S}
2  *4 C u0 {1,S} {3,S} {16,S}
3  *3 C u0 {2,S} {6,S} {11,D}
4     H u0 {1,S}
5     H u0 {1,S}
6     H u0 {3,S}
7  *1 C u0 {8,S} {11,S} {12,S}
8  *6 C u0 {7,S} {9,S} {13,S}
9  *5 C u0 {8,S} {10,S} {14,S}
10    C u0 {1,S} {9,S} {11,S} {15,S}
11 *2 C u0 {3,D} {7,S} {10,S}
12    H u0 {7,S}
13    H u0 {8,S}
14    H u0 {9,S}
15    H u0 {10,S}
16    H u0 {2,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)


forbidden(
    label = "bicyclohepta13diene",
    group = 
"""
1  *3 R!H u0 {2,[D,T]} {4,S}
2  *2 R!H u0 {1,[D,T]} {3,S} {6,S}
3  *1 R!H u0 {2,S} {7,S}
4  *4 R!H u0 {1,S} {5,[D,T]}
5  *5 R!H u0 {4,[D,T]} {6,S} {7,S}
6  R!H u0 {5,S} {2,S}
7  *6 R!H u0 {5,S} {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)


forbidden(
    label = "bicyclohepta13diene_prod",
    group = 
"""
1  *3 R!H u0 {2,S} {4,[D,T]}
2  *2 R!H u0 {1,S} {3,[D,T]} {6,S}
3  *1 R!H u0 {2,[D,T]}
4  *4 R!H u0 {1,[D,T]} {5,S}
5  *5 R!H u0 {4,S} {6,S} {7,[D,T]}
6  R!H u0 {5,S} {2,S}
7  *6 R!H u0 {5,[D,T]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)



forbidden(
    label = "bicyclohepta13diene_rad",
    group = 
"""
1  *3 R!H u0 {2,[D,T]} {4,S}
2  *2 R!H u0 {1,[D,T]} {3,S} {6,S}
3  *1 R!H u0 {2,S} {7,S}
4  *4 R!H u0 {1,S} {5,[D,T]}
5  *5 R!H u0 {4,[D,T]} {6,S} {7,S}
6  R!H u1 {5,S} {2,S}
7  *6 R!H u0 {5,S} {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)


forbidden(
    label = "bicyclohepta13diene_rad_prod",
    group = 
"""
1  *3 R!H u0 {2,S} {4,[D,T]}
2  *2 R!H u0 {1,S} {3,[D,T]} {6,S}
3  *1 R!H u0 {2,[D,T]}
4  *4 R!H u0 {1,[D,T]} {5,S}
5  *5 R!H u0 {4,S} {6,S} {7,[D,T]}
6  R!H u1 {5,S} {2,S}
7  *6 R!H u0 {5,[D,T]} 
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)
