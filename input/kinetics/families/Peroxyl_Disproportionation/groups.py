#!/usr/bin/env python
# encoding: utf-8

name = "Peroxyl_Disproportionation/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Root"], products=["RO_rad", "RO_rad", "O2"], ownReverse=False)

reversible = "Reverse_Peroxyl_Disproportionation"
reversible = True

reactantNum = 2
productNum = 3

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['GAIN_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*3', '1'],
])

entry(
    index = 1,
    label = "Root",
    group =
"""
1    R u0 {2,S}
2 *1 O u0 {1,S} {3,S}
3 *2 O u1 {2,S}
4    R u0 {5,S}
5 *3 O u0 {4,S} {6,S}
6 *4 O u1 {5,S}
""",
    kinetics = None,
)
