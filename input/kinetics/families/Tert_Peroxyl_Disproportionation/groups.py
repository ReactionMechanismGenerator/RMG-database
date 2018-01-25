#!/usr/bin/env python
# encoding: utf-8

name = "Tert_Peroxyl_Disproportionation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["R3COO_rad", "R3COO_rad"], products=["R3CO_rad", "R3CO_rad", "O2"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['GAIN_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "R3COO_rad",
    group = 
"""
1    C   u0 {2,S} {4,S} {5,S} {6,S}
2 *1 O   u0 {1,S} {3,S}
3 *2 O   u1 {2,S}
4    R!H u0 {1,S}
5    R!H u0 {1,S}
6    R!H u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "R/ringOO_rad",
    group =
"""
1    C   u0 {2,S} {4,S} {8,S} {10,S}
2 *1 O   u0 {1,S} {3,S}
3 *2 O   u1 {2,S}
4    R!H u0 {1,S} {5,S}
5    R!H u0 {4,S} {6,S}
6    R!H u0 {5,S} {7,S}
7    R!H u0 {6,S} {8,S}
8    R!H u0 {1,S} {7,S}
10   R!H u0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: R3COO_rad
    L2: R/ringOO_rad
"""
)
