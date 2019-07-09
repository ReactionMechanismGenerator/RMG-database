#!/usr/bin/env python
# encoding: utf-8

name = "Baeyer-Villiger_step2_cat/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["criegee", "acid"], products=["ester", "alcohol", "acid2"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*5', 1, '*6'],
    ['BREAK_BOND', '*9', 1, '*10'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['CHANGE_BOND', '*7', -1, '*8'],
    ['CHANGE_BOND', '*7', 1, '*9'],
    ['FORM_BOND', '*2', 1, '*5'],
    ['FORM_BOND', '*4', 1, '*8'],
    ['FORM_BOND', '*6', 1, '*10'],
])

entry(
    index = 1,
    label = "criegee",
    group =
"""
1 *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2 *2 [C,H] u0 {1,S}
3    [C,H] u0 {1,S}
4 *3 O     u0 {1,S} {8,S}
5 *5 O     u0 {1,S} {6,S}
6 *6 O     u0 {5,S} {7,S}
7    R     u0 {6,S}
8 *4 H     u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "acid",
    group =
"""
1     R u0 {2,S}
2 *7  C u0 {1,S} {3,D} {4,S}
3 *8  O u0 {2,D}
4 *9  O u0 {2,S} {5,S}
5 *10 H u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "6_membered_ring",
    group =
"""
1  *1 C     u0 {2,S} {3,S} {7,S} {8,S}
2  *2 [C,H] u0 {1,S} {4,[S,D,T,B]}
3     [C,H] u0 {1,S} {6,[S,D,T,B]}
4     R!H   u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H   u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H   u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
7  *3 O     u0 {1,S} {11,S}
8  *5 O     u0 {1,S} {9,S}
9  *6 O     u0 {8,S} {10,S}
10    R     u0 {9,S}
11 *4 H     u0 {7,S}
""",
    kinetics = None,
)

tree(
"""
L1: criegee
    L2: 6_membered_ring
L1: acid
"""
)

forbidden(
    label = "peracid_criegee",
    group =
"""
1  *1 C     u0 {2,S} {3,S} {4,S} {5,S}
2  *2 [C,H] u0 {1,S}
3     [C,H] u0 {1,S}
4  *3 O     u0 {1,S} {10,S}
5  *5 O     u0 {1,S} {6,S}
6  *6 O     u0 {5,S} {7,S}
7     C     u0 {6,S} {8,D} {9,S}
8     O     u0 {7,D}
9     R     u0 {7,S}
10 *4 H     u0 {4,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
This structure should react via Baeyer-Villiger_step2
""",
)

