#!/usr/bin/env python
# encoding: utf-8

name = "2#_Oxidative_degradation_of_ethers_to_aldehyde/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase second oxidative degradation of ethers groups to alcohol and aldehyde:
RCOC(OOH)(H)R' => RCOH + HC(=O)R'
atom labels:
RCO[*1]C[*2](O[*3]O[*4]H[*5])R' => RCO[*1]H[*5] + HC[*2](=O[*3])R' +O*[*4]
"""

template(reactants=["Mid"], products=["alcohol", "acid", "O_radical"], ownReverse=False)

reverse = "noun"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['BREAK_BOND', '*4', 1, '*5'],
    ['FORM_BOND', '*1', 1, '*5'],
    ['CHANGE_BOND', '*2', 1, '*3'],
    ['GAIN_RADICAL', '*4', '2'],
])

entry(
    index=0,
    label="Mid",
    group=
"""
1     R ux px cx {2,S}
2     C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  *1 O u0 p2 c0 {2,S} {4,S}
4  *2 C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5     R ux px cx {4,S}
6  *3 O u0 p2 c0 {4,S} {7,S}
7  *4 O u0 p2 c0 {6,S} {11,S}
8     H u0 p0 c0 {2,S}
9     H u0 p0 c0 {2,S}
10    H u0 p0 c0 {4,S}
11 *5 H u0 p0 c0 {7,S}

""",
    kinetics=None,
)

tree(
"""
L1: Mid

"""
)
