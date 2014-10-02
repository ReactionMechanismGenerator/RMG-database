#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Si2S_R_H", "Y_H"], products=["Y_Si2S_R_H2"], ownReverse=False)

reverse = "Silylene_Elimination"

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*3'],
    ['LOSE_PAIR', '*3', '1'],
])

entry(
    index = 1,
    label = "Si2S_R_H",
    group = 
"""
1 *3 Si u0 p1 c0 {2,S} {3,S}
2    H  u0 p0 c0  {1,S}
3    R  u0 p0 c0  {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Y_H",
    group = "OR{H_H, Si_H}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "H_H",
    group = 
"""
1 *1 H u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "Si_H",
    group = """
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    R  u0  {1,S}
4    R  u0  {1,S}
5    R  u0  {1,S}
""",
    kinetics = None,
    shortDesc = u"""A silane""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "SiH2",
    group = 
"""
1 *3  Si u0 p1 c0 {2,S} {3,S}
2     H u0 p0 c0 {1,S}
3     H u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""silylene""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "SiH3_SiH",
    group = 
"""
1 *3  Si u0 p1 c0 {2,S} {3,S}
2     H u0 p0 c0 {1,S}
3     Si u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4     H u0 p0 c0 {3,S}
5     H u0 p0 c0 {3,S}
6     H u0 p0 c0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""disilylene""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "Si2H5_SiH",
    group = 
"""
1 *3  Si u0 p1 c0 {2,S} {3,S}
2     H u0 p0 c0 {1,S}
3     Si u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4     H u0 p0 c0 {3,S}
5     H u0 p0 c0 {3,S}
6     Si u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7     H u0 p0 c0 {6,S}
8     H u0 p0 c0 {6,S}
9     H u0 p0 c0 {6,S}
""",
    kinetics = None,
    shortDesc = u"""trisilylene""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "SiH4",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""Silane""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "Si2H6",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    Si u0 p0 c0 {1,S} {6,S} (7,S} {8,S}
6    H u0 p0 c0 {5,S}
7    H u0 p0 c0 {5,S}
8    H u0 p0 c0 {5,S}
""",
    kinetics = None,
    shortDesc = u"""Disilane""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Si3H8",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    Si u0 p0 c0 {1,S} {6,S} (7,S} {8,S}
6    H u0 p0 c0 {5,S}
7    H u0 p0 c0 {5,S}
8    Si u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
9    H u0 p0 c0 {8,S}
10   H u0 p0 c0 {8,S}
11   H u0 p0 c0 {8,S}
""",
    kinetics = None,
    shortDesc = u"""Trisilane""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: Si2S_R_H
	L2: SiH2
	L2: SiH3_SiH
	L2: Si2H5_SiH

L1: Y_H
	L2: H_H
	L2: Si_H
		L3: SiH4
		L3: Si2H6
		L3: Si3H8
"""
)

