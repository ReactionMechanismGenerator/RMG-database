#!/usr/bin/env python
# encoding: utf-8

name = "alcohol_dehydrogenation/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase dehydrogenation of an alcohol group:
C(OH)C(H) <=> C=C + H2O

atom labels:

C[*1](O[*2]H)C[*3](H[*4]) <=> C[*1]=C[*3] + H[*4]O[*2]H
"""

template(reactants=["alcohol"], products=["CdC", "H2O"], ownReverse=False)

reverse = "water_add_double_bond"

reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['CHANGE_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index=0,
    label="alcohol",
    group=
"""
1 *1 C u0 p0 c0 {2,S} {3,S}
2 *2 O u0 p2 c0 {1,S} {5,S}
3 *3 C u0 p0 c0 {1,S} {4,S}
4 *4 H u0 p0 c0 {3,S}
5 H u0 p0 c0 {2,S}
""",
    kinetics=None,
)

tree(
"""
L1: alcohol
"""
)
