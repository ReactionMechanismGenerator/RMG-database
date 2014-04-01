#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step2/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["C1(R)(H)(O[OC3(OH)(R')]C2)"], products=["C1(R)(O)(C2)", "C3(OH)(O)(R')"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*6'],
    ['BREAK_BOND', '*4', 'S', '*5'],
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['CHANGE_BOND', '*3', '1', '*4'],
    ['CHANGE_BOND', '*1', '1', '*5'],
    ['FORM_BOND', '*2', 'S', '*6'],
])

entry(
    index = 1,
    label = "C1(R)(H)(O[OC3(OH)(R')]C2)",
    group = 
"""
1  *1 C 0 {2,S} {4,S} {7,S} {9,S}
2  *2 C 0 {1,S} {3,S} {11,S} {12,S}
3  *3 C 0 {2,S} {5,S} {6,S} {8,S}
4  *5 O 0 {1,S} {5,S}
5  *4 O 0 {3,S} {4,S}
6     O 0 {3,S} {10,S}
7     R 0 {1,S}
8     R 0 {3,S}
9  *6 H 0 {1,S}
10    H 0 {6,S}
11    H 0 {2,S}
12    H 0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: C1(R)(H)(O[OC3(OH)(R')]C2)
"""
)

forbidden(
    label = "O4",
    group = 
"""
1    O 1 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *2 O 0 {2,S} {4,S}
4    O 1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

