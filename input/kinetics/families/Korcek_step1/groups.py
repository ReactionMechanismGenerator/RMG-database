#!/usr/bin/env python
# encoding: utf-8

name = "Korcek_step1/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RCH(OOH)CH2C(O)R'"], products=["cyclic_peroxide"], ownReverse=False)

reverse = "cyclic_peroxide_ringopening"

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['CHANGE_BOND', '*3', '-1', '*4'],
    ['FORM_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*4'],
])

entry(
    index = 1,
    label = "RCH(OOH)CH2C(O)R'",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1     C U0 {2,S} {4,S} {7,S} {9,S}
2     C U0 {1,S} {3,S} {11,S} {12,S}
3  *4 C U0 {2,S} {6,D} {8,S}
4     O U0 {1,S} {5,S}
5  *1 O U0 {4,S} {10,S}
6  *3 O U0 {3,D}
7     R U0 {1,S}
8     R U0 {3,S}
9     H U0 {1,S}
10 *2 H U0 {5,S}
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
L1: RCH(OOH)CH2C(O)R'
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

