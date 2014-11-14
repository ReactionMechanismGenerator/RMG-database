#!/usr/bin/env python
# encoding: utf-8

name = "H_shift_cyclopentadiene/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["cyclopentadiene"], products=["cyclopentadiene"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*6'],
    ['FORM_BOND', '*2', 'S', '*6'],
    ['CHANGE_BOND', '*2', '-1', '*3'],
    ['CHANGE_BOND', '*4', '-1', '*5'],
    ['CHANGE_BOND', '*1', '1', '*5'],
    ['CHANGE_BOND', '*4', '1', '*3'],
])

entry(
    index = 1,
    label = "cyclopentadiene",
    group = 
"""
1 *1 C u0 {2,S} {5,S} {6,S}
2 *2 C u0 {1,S} {3,D}
3 *3 C u0 {2,D} {4,S}
4 *4 C u0 {3,S} {5,D}
5 *5 C u0 {1,S} {4,D}
6 *6 H u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: cyclopentadiene
"""
)

