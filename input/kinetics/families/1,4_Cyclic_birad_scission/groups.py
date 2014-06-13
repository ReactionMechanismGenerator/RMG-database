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
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 2,
    label = "R5JJ",
    group = 
"""
1 *1 R 1 {2,{S,D}} {5,S}
2 *2 R 0 {1,{S,D}} {3,S}
3 *3 R 0 {2,S} {4,{S,D}}
4 *4 R 1 {3,{S,D}} {5,S}
5    R 0 {1,S} {4,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 3,
    label = "R6JJ",
    group = 
"""
1 *1 R 1 {2,{S,D}} {5,S}
2 *2 R 0 {1,{S,D}} {3,S}
3 *3 R 0 {2,S} {4,{S,D}}
4 *4 R 1 {3,{S,D}} {6,S}
5    R 0 {1,S} {6,S}
6    R 0 {4,S} {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

entry(
    index = 4,
    label = "R7JJ",
    group = 
"""
1 *1 R 1 {2,{S,D}} {5,S}
2 *2 R 0 {1,{S,D}} {3,S}
3 *3 R 0 {2,S} {4,{S,D}}
4 *4 R 1 {3,{S,D}} {7,S}
5    R 0 {1,S} {6,S}
6    R 0 {5,S} {7,S}
7    R 0 {4,S} {6,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Feb 10 21:39:02 2014","Connie Gao <connieg@mit.edu>","action","""Connie Gao <connieg@mit.edu> added this entry by importing the old RMG database."""),
    ],
)

tree(
"""
L1: RJJ
    L2: R5JJ
    L2: R6JJ
    L2: R7JJ
"""
)

