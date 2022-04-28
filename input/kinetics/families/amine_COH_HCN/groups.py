#!/usr/bin/env python
# encoding: utf-8

name = "amine_COH_HCN/groups"
shortDesc = u""
longDesc = u"""
This family describes a reaction between a secondary/tertiary amine with a COH branch and HCN (condensation),
producing an amine with a CC#N branch.
R1N(R2)COH + HC#N <=> R1N(R2)CCN + H2O

atom labels:

R1N(R2)_C[*1]_O[*2]_H + H[*3]_C[*4]_#N <=> R1N(R2)_C[*1]C_[*4]_#N + H[*3]_O[*2]_H
"""

template(reactants=["amine_COH", "HCN"], products=["hemiacetal", "alcohol"], ownReverse=False)

reverse = "amine_CCN_to_amine_OH"

reversible = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*4'],
    ['FORM_BOND', '*2', 1, '*3'],
])

entry(
    index=0,
    label="amine_COH",
    group=
"""
1    R!H u0 px c0 {2,S}
2    N   u0 p1 c0 {1,S} {3,S} {4,S}
3    R   u0 px c0 {2,S}
4 *1 C   u0 p0 c0 {2,S} {5,S} {6,S} {7,S}
5 *2 O   u0 p2 c0 {4,S} {8,S}
6    H   u0 p0 c0 {4,S}
7    H   u0 p0 c0 {4,S}
8    H   u0 p0 c0 {5,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="HCN",
    group=
"""
1 *4 C u0 p0 c0 {2,T} {3,S}
2    N u0 p1 c0 {1,T}
3 *3 H u0 p0 c0 {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: amine_COH
L1: HCN
"""
)
