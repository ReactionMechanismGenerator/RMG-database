#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Linear_birad_scission/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RJJ"], products=["ene1", "ene2"], ownReverse=False)

reverse = "none"

reversible = True
recipe(actions=[
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*4', '1'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*2', 1, '*3'],
])

entry(
    index = 0,
    label = "RJJ",
    group = 
"""
1 *1 R!H u1 c0 {2,[S,D]}
2 *2 R!H u0 c0 {1,[S,D]} {3,S}
3 *3 R!H u0 c0 {2,S} {4,[S,D]}
4 *4 R!H u1 c0 {3,[S,D]}
""",
    kinetics = None,
)

tree(
"""
L1: RJJ
"""
)

