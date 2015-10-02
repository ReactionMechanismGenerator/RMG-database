#!/usr/bin/env python
# encoding: utf-8

name = "Retroen/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["alkylaromatic"], products=["methylaromatic", "alkene"], ownReverse=False)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['BREAK_BOND', '*3', 'S', '*4'],
    ['FORM_BOND', '*1', 'S', '*4'],
    ['CHANGE_BOND', '*2', 1, '*3'],
])

entry(
    index = 1,
    label = "alkylaromatic",
    group = 
"""
1 *1  Cs u0 {2,S} {4,S} {11,S} {12,S}
2 *2  Cs u0 {1,S} {3,S} {13,S} {14,S}
3 *3  Cs u0 {2,S} {10,S} 
4     C  u0 {1,S} {5,D} {9,S}
5     C  u0 {4,D} {6,S}
6     C  u0 {5,S} {7,D}
7     C  u0 {6,D} {8,S}
8     C  u0 {7,S} {9,D}
9     C  u0 {4,S} {8,D}
10 *4 H  u0 {3,S}
11    H  u0 {1,S}
12    H  u0 {1,S}
13    H  u0 {2,S}
14    H  u0 {2,S}
""",
    kinetics = None,
)



tree(
"""
L1: alkylaromatic
"""
)
