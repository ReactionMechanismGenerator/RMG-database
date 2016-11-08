#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_Insertion/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Si2S", "Y_H"], products=["Y_Si2S_H"], ownReverse=False)

#reverse = "Silylene_Elimination"

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*3'],
    ['LOSE_PAIR', '*3', '1'],
])

entry(
    index = 1,
    label = "Si2S",
    group =
"""
1 *3 Si ux p1 c0
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
1 *1 Si ux p0 c0 {2,S}
2 *2 H  u0 p0 c0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 4,
    label = "SiH3_R",
    group = """
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4    H  u0 p0 c0 {1,S}
5    R  ux px {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 4,
    label = "SiH3_Si",
    group = """
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4    H  u0 p0 c0 {1,S}
5    Si  ux px {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 4,
    label = "SiH2_R2",
    group = """
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    H  u0 p0 c0 {1,S}
4    R  ux px {1,S}
5    R  ux px {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 4,
    label = "SiH_R3",
    group = """
1 *1 Si u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 p0 c0 {1,S}
3    R  ux px {1,S}
4    R  ux px {1,S}
5    R  ux px {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
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
    index = 5,
    label = "Si-Si-H",
    group =
"""
1 *3  Si u0 p1 c0 {2,S} {3,S}
2     H u0 p0 c0 {1,S}
3     Si ux px {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc =
u"""

""",
)

entry(
    index = 5,
    label = "Si-Si-Si",
    group =
"""
1 *3  Si u0 p1 c0 {2,S} {3,S}
2     Si ux px {1,S}
3     Si ux px {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
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



tree(
"""
L1: Si2S
	L2: SiH2
	L2: Si-Si-Si
	L2: Si-Si-H

L1: Y_H
	L2: H_H
	L2: Si_H
            L3: SiH3_R
		L4: SiH4
                L4: SiH3_Si
	    L3: SiH2_R2
            L3: SiH_R3
"""
)

forbidden(
    label = "Si_wrong_valence",
    group =
"""
1 *3  Si u0 p2 c0
""",
    shortDesc = u"""This violates Hund's rule for Silicon""",
    longDesc =
u"""

""",
)

forbidden(
    label = "silylene_as_si-h",
    group =
"""
1 *1  Si ux p1 c0 {2,S}
2 *2  H  u0 p0 c0 {1,S}
""",
    shortDesc = u"""We shouldn't be able to insert into an Si-H bond in a silylene.""",
    longDesc =
u"""

""",
)
