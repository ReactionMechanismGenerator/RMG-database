#!/usr/bin/env python
# encoding: utf-8

name = "intra_NO2_ONO_conversion/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["RNO2"], products=["RONO"], ownReverse=False)

reverse = "intra_ONO_NO2_migration"

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['LOSE_PAIR', '*3', '1'],
    ['GAIN_PAIR', '*2', '1'],
])

entry(
    index = 0,
    label = "RNO2",
    group = 
"""
1 *2 N5d u0 {2,S} {3,S} {4,D}
2 *1 R   u0 {1,S}
3 *3 Os  u0 {1,S}
4    Od  u0 {1,D}
""",
    kinetics = None,
)

tree(
"""
L1: RNO2
"""
)

