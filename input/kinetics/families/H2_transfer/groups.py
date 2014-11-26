#!/usr/bin/env python
# encoding: utf-8

name = "H2_transfer/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RH2", "Si_pair"], products=["R", "Si_pair_H2"], ownReverse=True)

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['BREAK_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*4'],
    ['FORM_BOND', '*3', 'S', '*4'],
    ['GAIN_PAIR', '*1', 1],
    ['LOSE_PAIR', '*4', 1]])

entry(
    index = 1,
    label = "RH2",
    group = 
"""
1 *1 R!H u[0,2] p0 c0 {2,S} {3,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 2,
    label = "Si_pair",
    group = 
"""
1 *4 Si u[0,2] p1 c0
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "R-SiH2",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 H  u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "SiH4",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 H  u0 p0 c0 {1,S}
4    H  u0 p0 c0 {1,S}
5    H  u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R-SiH3",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 H  u0 p0 c0 {1,S}
4    H  u0 p0 c0 {1,S}
5    R!H ux px {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "Si2H6",
    group = 
"""
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3 *3 H  u0 p0 c0 {1,S}
4    H  u0 p0 c0 {1,S}
5    Si u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
6    H  u0 p0 c0 {5,S} 
7    H  u0 p0 c0 {5,S} 
8    H  u0 p0 c0 {5,S} 
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "SiH2-triplet",
    group = 
"""
1 *1 Si u2 p0 c0 {2,S} {3,S}
2 *2 H u0 p0 c0 {1,S}
3 *3 H u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""
""",
)

entry(
    index = 8,
    label = "Si_atom",
    group = 
"""
1 *4 Si u2 p1 c0
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "Y-SiH",
    group = 
"""
1 *4 Si u0 p1 c0 {2,S}
2    H u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "SiH2",
    group = 
"""
1 *4 Si u0 p1 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Si-SiH",
    group = 
"""
1 *4 Si u0 p1 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    Si ux px {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "H3SiSiH",
    group = 
"""
1 *4 Si u0 p1 c0 {2,S} {3,S}
2    H u0 p0 c0 {1,S}
3    Si u0 p0 c0 {1,S} {4,S} {5,S} {6,S}
4    H u0 p0 c0 {3,S}
5    H u0 p0 c0 {3,S}
6    H u0 p0 c0 {3,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: RH2
	L2: R-SiH2
		L3: SiH4
		L3: R-SiH3
			L4: Si2H6
	L2: SiH2-triplet

L1: Si_pair
	L2: Si_atom
	L2: Y-SiH
		L3: SiH2
		L3: Si-SiH
			L4: H3SiSiH
 
"""
)

