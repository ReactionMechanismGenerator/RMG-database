#!/usr/bin/env python
# encoding: utf-8

name = "ether_peroxide_decomposition/groups"
shortDesc = u""
longDesc = u"""
HOOR(H)OR' <=> HOR(=O) + R'OH
atom labels:
HO[*4]O[*3]R[*1](H[*2])O[*5]R' <=> HO[*4]R[*1](=O[*3]) + R'O[*5]H[*2]
"""

template(reactants=["ether_peroxide"], products=["carboxyl", "alcohol"], ownReverse=False)

reverse = "aldehide_and_alcohol_to_ether_peroxide"

reversible = True

recipe(actions=[
    ['BREAK_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*1', 1, '*5'],
    ['FORM_BOND', '*1', 1, '*4'],
    ['FORM_BOND', '*5', 1, '*2'],
    ['CHANGE_BOND', '*1', 1, '*3'],
])

entry(
    index=0,
    label="ether_peroxide",
    group=
"""
1 *4 O u0 p2 c0 {2,S} {6,S}
2 *3 O u0 p2 c0 {1,S} {3,S}
3 *1 C u0 p0 c0 {2,S} {4,S} {7,S}
4 *5 O u0 p2 c0 {3,S} {5,S}
5    C u0 p0 c0 {4,S}
6    H u0 p0 c0 {1,S}
7 *2 H u0 p0 c0 {3,S}
""",
    kinetics=None,
)

tree(
"""
L1: ether_peroxide
"""
)

