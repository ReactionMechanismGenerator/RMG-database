#!/usr/bin/env python
# encoding: utf-8

name = "Silylene_to_Silene/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["SiRHSiH"], products=["SiR=SiH2"], ownReverse=False)

recipe(actions=[
    ['LOSE_PAIR', '*1', '1'],
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['CHANGE_BOND', '*1', '1', '*2'],
])

entry(
    index = 1,
    label = "SiRHSiH",
    group = 
"""
1 *1 Si u0 p1 c0 {2,S} {4,S}
2 *2 Si u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3  H u0 p0 c0 {2,S}
4     R u0 p0 c0 {1,S}
5     R u0 p0 c0 {2,S}
6     R u0 p0 c0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)


tree(
"""
L1: SiRHSiH
"""
)

