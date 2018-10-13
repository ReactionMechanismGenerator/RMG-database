#!/usr/bin/env python
# encoding: utf-8

name = "1,3_NH3_elimination/groups"
shortDesc = u""
longDesc = u"""
This family describes reactions on a singlet PES of the sort:

RHRNH2 <=> R=R + NH3

where a terminal NH2 group and an H atom on an adjacent N are eliminated as NH3, leaving a multiple bond.

atom labeling:
*1 - the eliminated N
*2 - next R in the chain
*3 - last R in the chain
*4 - the eliminated H from R *3
"""

template(reactants=["RHRNH2"], products=["RR", "NH3"], ownReverse=False)

reverse = "1,3_NH3_addition"

reversible = True

recipe(actions=[
    ['FORM_BOND', '*1', 1, '*4'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*2', 1, '*3'],
])

entry(
    index = 1,
    label = "RHRNH2",
    group =
"""
1 *1 N   u0 p1 c0 {2,S} {5,S} {6,S}
2 *2 R!H u0 px c0 {1,S} {3,[S,D]}
3 *3 R!H u0 px c0 {2,[S,D]} {4,S}
4 *4 H   u0 p0 c0 {3,S}
5    H   u0 p0 c0 {1,S}
6    H   u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "NHNNH2",
    group =
"""
1 *1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 *2 N u0 p1 c0 {1,S} {3,[S,D]}
3 *3 N u0 p1 c0 {2,[S,D]} {4,S}
4 *4 H u0 p0 c0 {3,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "NNHNNH2",
    group =
"""
1 *1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 *2 N u0 p1 c0 {1,S} {3,S}
3 *3 N u0 p1 c0 {2,S} {4,S} {7,S}
4 *4 H u0 p0 c0 {3,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    N ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "NHDNNH2",
    group =
"""
1 *1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 *2 N u0 p1 c0 {1,S} {3,D}
3 *3 N u0 p1 c0 {2,D} {4,S}
4 *4 H u0 p0 c0 {3,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "CHCNH2",
    group =
"""
1 *1 N u0 p1 c0 {2,S} {5,S} {6,S}
2 *2 C u0 p0 c0 {1,S} {3,S}
3 *3 C u0 p0 c0 {2,S} {4,S}
4 *4 H u0 p0 c0 {3,S}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: RHRNH2
    L2: NHNNH2
        L3: NNHNNH2
        L3: NHDNNH2
    L2: CHCNH2
"""
)
