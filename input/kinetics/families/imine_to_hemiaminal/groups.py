#!/usr/bin/env python
# encoding: utf-8

name = "imine_to_hemiaminal/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amine groups:
R=NR' + H2O <=> H + RN(OH)R'
atom labels:
RC[*1]=N[*2]R' + H[*4]O[*3]H <=>  RC[*1](OH[*3])N[*2](H[*4])R'
"""

template(reactants=["CdN", "H2O"], products=["CdNOH"], ownReverse=False)

reverse = "hydroxylamine_to_imine"

reversible = True

only_forward = True

recipe(actions=[
    ['CHANGE_BOND', '*1', -1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*4', 1, '*2'],
])

entry(
    index=0,
    label="CdN",
    group=
"""
1    R ux px cx {2,S} 
2 *1 C u0 p0 c0 {1,S} {3,D} {5,S}
3 *2 N u0 p1 c0 {2,D} {4,S}
4    R ux px cx {3,S}
5    H u0 p0 c0 {2,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="H2O",
    group=
"""
1 *3 O u0 p2 c0 {2,S} {3,S}
2 *4 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: CdN
L1: H2O
"""
)
