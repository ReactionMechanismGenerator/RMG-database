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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1  *1 C U0 {2,S} {4,S} {7,S} {9,S}
2  *2 C U0 {1,S} {3,S} {11,S} {12,S}
3  *3 C U0 {2,S} {5,S} {6,S} {8,S}
4  *5 O U0 {1,S} {5,S}
5  *4 O U0 {3,S} {4,S}
6     O U0 {3,S} {10,S}
7     R U0 {1,S}
8     R U0 {3,S}
9  *6 H U0 {1,S}
10    H U0 {6,S}
11    H U0 {2,S}
12    H U0 {2,S}
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
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1    O U1 {2,S}
2 *1 O U0 {1,S} {3,S}
3 *2 O U0 {2,S} {4,S}
4    O U1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

