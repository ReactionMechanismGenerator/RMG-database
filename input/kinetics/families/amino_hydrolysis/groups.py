#!/usr/bin/env python
# encoding: utf-8

name = "amino_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amine groups:
R1C(OH)CNR2 + H2O <=> R1C=O + CNHR2 
atom labels:
R1C[*1](O[*2]H[*3])C[*4]NR2 + H2O[*5] <=> R1C[*1]=O[*2] + C[*4]NHR2 +H[*3] + H2O
"""

template(reactants=["amino", "H2O"], products=["aldehyde", "imine", "H2O"], ownReverse=False)

reverse = "aldehyde_and_imine_to_amino"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*2', 1, '*3'],
    ['FORM_BOND', '*3', 1, '*5'],
    ['BREAK_BOND', '*1', 1, '*4'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*5'],

])

entry(
    index=0,
    label="amino",
    group=
"""
1     R ux px cx {2,S} 
2     N u0 p1 c0 {1,S} {3,S} {7,S}
3  *4 C u0 p0 c0 {2,S} {4,S} {8,S} {9,S}
4  *1 C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
5     R ux px cx {4,S} 
6  *2 O u0 p2 c0 {4,S} {11,S}
7     H u0 p0 c0 {2,S}
8     H u0 p0 c0 {3,S}
9     H u0 p0 c0 {3,S}
10    H u0 p0 c0 {4,S}
11 *3 H u0 p0 c0 {6,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="H2O",
    group=
"""
1  *5 O u0 p2 c0 {2,S} {3,S}
2     H u0 p0 c0 {1,S}
3     H u0 p0 c0 {1,S}
""",
    kinetics=None,
)


tree(
"""
L1: amino
L1: H2O
"""
)

