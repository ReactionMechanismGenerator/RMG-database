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
    ['LOSE_RADICAL', '*3', '2'],
])

entry(
    index = 1,
    label = "Si2S_R_H",
    group = 
"""
1 *3 Si 2S {2,S} {3,S}
2    H  0  {1,S}
3    R  0  {1,S}
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
1 *1 H 0 {2,S}
2 *2 H 0 {1,S}
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
    group = 
"""
1 *1 Si 0 {2,S} {3,S} {4,S} {5,S}
2 *2 H 0 {1,S}
3    R 0 {1,S}
4    R 0 {1,S}
5    R 0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""A silane""",
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

