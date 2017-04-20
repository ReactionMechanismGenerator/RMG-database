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
    index = 1,
    label = "RNO2",
    group = 
"""
1 *1 R   u0 {2,S}
2 *2 N5d u0 {1,S} {3,S} {4,D}
3 *3 Os  u0 {2,S}
4    Od  u0 {2,D}
""",
    kinetics = None,
)
 
entry(
    index = 2,
    label = "CH3NO2",
    group = 
"""
1 *1 Cs u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
2 *3 Os u0 p2 c0 {1,S} {3,S}
3 *2 N5d u0 p1 c0 {2,S} {4,D}
4    Od u0 p2 c0 {3,D}
5    H u0 p0 c0 {1,S}
6    H u0 p0 c0 {1,S}
7    H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

tree(
"""
L1: RNO2
	L2: CH3NO2
"""
)

