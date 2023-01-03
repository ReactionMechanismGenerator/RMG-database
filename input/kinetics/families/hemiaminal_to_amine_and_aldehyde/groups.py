#!/usr/bin/env python
# encoding: utf-8

name = "hemiaminal_to_amine_and_aldehyde/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amine groups:
C=NR + H2O <=> C=O + RNH2
atom labels:
H[*5] + RC[*1](O[*3]H[*4])N[*2]R' <=> C[*1]_=O[*3] + R_N[*2]_H[*4]_H[*5]


this family needs a fix: where does H[*5] come from? if H3O+ or H2O, need to explicitly say so


"""

template(reactants=["hemiaminal"], products=["CdO", "NH2"], ownReverse=False)

reverse = "condensation_to_imine"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*5'],
])

entry(
    index=0,
    label="hemiaminal",
    group=
"""
1     R ux px cx {2,S}
2  *1 C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  *2 O u0 p2 c0 {2,S} {8,S}
4  *4 N u0 p1 c0 {2,S} {5,S} {6,S}
5     R ux px cx {4,S}
6     R ux px cx {4,S}
7     H u0 p0 c0 {2,S}
8  *3 H u0 p0 c0 {3,S}
""",
    kinetics=None,
)


tree(
"""
L1: hemiaminal
"""
)

