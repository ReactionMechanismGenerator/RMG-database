#!/usr/bin/env python
# encoding: utf-8

name = "methanoate_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of methanoate_hydrolysis:
R1C(=O)OR2 + H2O <=> R1C(=O)OH + R2OH

atom labels:

R1_C_(=O)_O[*1]_R2[*2] + H[*3]_O[*4]_H <=> R1_C_(=O)_O[*1]_H[*3] + R2[*2]_O[*4]_H
"""

template(reactants=["methanoate", "H2O"], products=["carboxyl", "alcohol"], ownReverse=False)

reverse = "alcohol_addition_to_carboxyl"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index=0,
    label="methanoate",
    group=
"""
1    O u0 p2 c0 {2,D}
2    C u0 p0 c0 {1,D} {3,S}
3 *1 O u0 p2 c0 {2,S} {4,S}
4 *2 R ux px cx {3,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="H2O",
    group=
"""
1 *4 O u0 p2 c0 {2,S} {3,S}
2 *3 H u0 p0 c0 {1,S}
3    H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: methanoate
L1: H2O
"""
)
