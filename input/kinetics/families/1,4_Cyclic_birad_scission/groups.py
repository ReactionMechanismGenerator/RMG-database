#!/usr/bin/env python
# encoding: utf-8

name = "1,4_Cyclic_birad_scission/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RJJ"], products=["diene"], ownReverse=False)

reverse = "none"

recipe(actions=[
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['LOSE_RADICAL', '*1', '1'],
    ['LOSE_RADICAL', '*4', '1'],
    ['CHANGE_BOND', '*1', '1', '*2'],
    ['CHANGE_BOND', '*3', '1', '*4'],
])

entry(
    index = 1,
    label = "RJJ",
    group = "OR{R5JJ, R6JJ, R7JJ}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "R5JJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R U1 {2,{S,D}} {5,S}
2 *2 R U0 {1,{S,D}} {3,S}
3 *3 R U0 {2,S} {4,{S,D}}
4 *4 R U1 {3,{S,D}} {5,S}
5    R U0 {1,S} {4,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "R6JJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R U1 {2,{S,D}} {5,S}
2 *2 R U0 {1,{S,D}} {3,S}
3 *3 R U0 {2,S} {4,{S,D}}
4 *4 R U1 {3,{S,D}} {6,S}
5    R U0 {1,S} {6,S}
6    R U0 {4,S} {5,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "R7JJ",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 R U1 {2,{S,D}} {5,S}
2 *2 R U0 {1,{S,D}} {3,S}
3 *3 R U0 {2,S} {4,{S,D}}
4 *4 R U1 {3,{S,D}} {7,S}
5    R U0 {1,S} {6,S}
6    R U0 {5,S} {7,S}
7    R U0 {4,S} {6,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: RJJ
    L2: R5JJ
    L2: R6JJ
    L2: R7JJ
"""
)

