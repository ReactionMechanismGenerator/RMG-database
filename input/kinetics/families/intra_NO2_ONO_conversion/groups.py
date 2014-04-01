#!/usr/bin/env python
# encoding: utf-8

name = "intra_NO2_ONO_conversion/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RNO2"], products=["RONO"], ownReverse=False)

reverse = "intra_ONO_NO2_migration"

recipe(actions=[
    ['BREAK_BOND', '*1', 'S', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['LOSE_PAIR', '*3', '1'],
    ['GAIN_PAIR', '*2', '1'],
])

entry(
    index = 1,
    label = "RNO2",
    group = 
"""
1 *1 R   0 {2,S}
2 *2 N5d 0 {1,S} {3,S} {4,D}
3 *3 Os  0 {2,S}
4    Od  0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: RNO2
"""
)


