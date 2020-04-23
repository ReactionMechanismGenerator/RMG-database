#!/usr/bin/env python
# encoding: utf-8

name = "1,2_NH3_elimination/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions on a singlet PES of the sort:

NNHNH2 <=> N=N + NH3

where a terminal NH2 group and an H atom on an adjacent N are eliminated as NH3, leaving a multiple bond.

atom labeling:
*1 - the eliminated N
*2 - N adjacent to N *1, has the eliminated H *4
*3 - N adjacent to N *2
*4 - the eliminated H from N *2
"""

template(reactants=["NNHNH2"], products=["NN", "NH3"], ownReverse=False)

reverse = "1,2_NH3_addition"

reversible = True

only_forward = True

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*2', 1, '*4'],
    ['GAIN_PAIR', '*2', '1'],
    ['LOSE_PAIR', '*3', '1'],
    ['CHANGE_BOND', '*2', 1, '*3'],
])

entry(
    index = 0,
    label = "NNHNH2",
    group =
"""
1 *1 N u0 p1     c0 {2,S} {5,S} {6,S}
2 *2 N u0 px     cx {1,S} {4,S} {3,[S,D]}
3 *3 N u0 p[1,2] cx {2,[S,D]}
4 *4 H u0 p0     c0 {2,S}
5    H u0 p0     c0 {1,S}
6    H u0 p0     c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "non_charged",
    group =
"""
1 *1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 *2 N u0 p1 c0 {1,S} {4,S} {3,S}
3 *3 N u0 p1 c0 {2,S}
4 *4 H u0 p0 c0 {2,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "non_charged4",
    group =
"""
1 *1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 *2 N u0 p1 c0 {1,S} {4,S} {3,S}
3 *3 N u0 p1 c0 {2,S} {7,S}
4 *4 H u0 p0 c0 {2,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    N ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "charged",
    group =
"""
1 *1 N u0 p1 c0  {2,S} {5,S} {6,S}
2 *2 N u0 p0 c+1 {1,S} {4,S} {3,[S,D]}
3 *3 N u0 p2 c-1 {2,[S,D]}
4 *4 H u0 p0 c0  {2,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "chargedS",
    group =
"""
1 *1 N u0 p1 c0  {2,S} {5,S} {6,S}
2 *2 N u0 p0 c+1 {1,S} {4,S} {3,S}
3 *3 N u0 p2 c-1 {2,S}
4 *4 H u0 p0 c0  {2,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "chargedD",
    group =
"""
1 *1 N u0 p1 c0  {2,S} {5,S} {6,S}
2 *2 N u0 p0 c+1 {1,S} {4,S} {3,D}
3 *3 N u0 p2 c-1 {2,D}
4 *4 H u0 p0 c0  {2,S}
5    H u0 p0 c0  {1,S}
6    H u0 p0 c0  {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: NNHNH2
    L2: non_charged
        L3: non_charged4
    L2: charged
        L3: chargedS
        L3: chargedD
"""
)
