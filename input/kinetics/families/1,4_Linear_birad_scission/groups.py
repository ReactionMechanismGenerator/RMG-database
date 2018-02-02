#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Linear_birad_scission/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RJJ"], products=["ene1", "ene2"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*4', '1'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*2', 1, '*3'],
])

entry(
    index = 1,
    label = "RJJ",
    group = 
"""
1 *1 R!H u1 px c0 {2,[S,D]}
2 *2 R!H u0 px c0 {1,[S,D]} {3,S}
3 *3 R!H u0 px c0 {2,S} {4,[S,D]}
4 *4 R!H u1 px c0 {3,[S,D]}
""",
    kinetics = None,
)

tree(
"""
L1: RJJ
"""
)


forbidden(
    label = "N2O2a",
    group =
"""
multiplicity [3]
1 *3 O u0 p2 c0 {2,S} {3,S}
2 *2 N u0 p1 c0 {1,S} {4,D}
3 *4 O u1 p2 c0 {1,S}
4 *1 N u1 p1 c0 {2,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
N2O2 reacts in this family to form a singlet O2 (O=O)
See RMG-Py issue #1020
""",
)

forbidden(
    label = "N2O2b",
    group =
"""
multiplicity [3]
1 *2 O u0 p2 c0 {2,S} {3,S}
2 *3 N u0 p1 c0 {1,S} {4,D}
3 *1 O u1 p2 c0 {1,S}
4 *4 N u1 p1 c0 {2,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Same as above, inverse atom labeling
""",
)

