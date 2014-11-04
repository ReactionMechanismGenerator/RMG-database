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
    group = 
"""
1     C u0 {2,S} {4,S} {7,S} {9,S}
2     C u0 {1,S} {3,S} {11,S} {12,S}
3  *4 C u0 {2,S} {6,D} {8,S}
4     O u0 {1,S} {5,S}
5  *1 O u0 {4,S} {10,S}
6  *3 O u0 {3,D}
7     R u0 {1,S}
8     R u0 {3,S}
9     H u0 {1,S}
10 *2 H u0 {5,S}
11    H u0 {2,S}
12    H u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: RCH(OOH)CH2C(O)R'
"""
)

forbidden(
    label = "O4",
    group = 
"""
1    O u1 {2,S}
2 *1 O u0 {1,S} {3,S}
3 *2 O u0 {2,S} {4,S}
4    O u1 {3,S}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

