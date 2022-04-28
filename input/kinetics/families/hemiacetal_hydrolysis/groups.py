#!/usr/bin/env python
# encoding: utf-8

name = "hemiacetal_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes hydrolysis of a hemiacetal species (ester alcohol), R1C(OR2)OH.
The reaction is acid-catalyzed, the template here does not consider a pH effect.
R1C(OR2)OH <=> R1C=O + R2OH

atom labels:

R1_C[*1]_(O[*2]_R2)_O[*3]_H[*4] <=> R1_C[*1]_=O[*3] + R2_O[*2]_H[*4]

Some rate data is available here: https://doi.org/10.1021/ja00406a036
"""

template(reactants=["hemiacetal"], products=["ketone", "alcohol"], ownReverse=False)

reverse = "alcohol_addition_to_ketone"

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
    label="hemiacetal",
    group=
"""
1  *1 Cs u0 p0 c0 {2,S} {3,S} {4,S}
2  *3 O  u0 p2 c0 {1,S} {5,S}
3  *2 O  u0 p2 c0 {1,S}
4     H  u0 p0 c0 {1,S}
5  *4 H  u0 p0 c0 {2,S}
""",
    kinetics=None,
)

entry(
    index=1,
    label="Cs_hemiacetal",
    group=
"""
1  *1 Cs u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  *3 O  u0 p2 c0 {1,S} {5,S}
3  *2 O  u0 p2 c0 {1,S}
4     H  u0 p0 c0 {1,S}
5  *4 H  u0 p0 c0 {2,S}
6     Cs u0 p0 c0 {1,S}
""",
    kinetics=None,
)

entry(
    index=2,
    label="Cs_methanediol",
    group=
"""
1  *1 Cs u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  *3 O  u0 p2 c0 {1,S} {5,S}
3  *2 O  u0 p2 c0 {1,S} {7,S}
4     H  u0 p0 c0 {1,S}
5  *4 H  u0 p0 c0 {2,S}
6     Cs u0 p0 c0 {1,S}
7     H  u0 p0 c0 {3,S}
""",
    kinetics=None,
)

entry(
    index=3,
    label="Cbdt_hemiacetal",
    group=
"""
1  *1 Cs u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  *3 O  u0 p2 c0 {1,S} {5,S}
3  *2 O  u0 p2 c0 {1,S}
4     H  u0 p0 c0 {1,S}
5  *4 H  u0 p0 c0 {2,S}
6     [Cb,Cd,Ct] ux {1,S}
""",
    kinetics=None,
)

entry(
    index=4,
    label="Cbdt_methanediol",
    group=
"""
1  *1 Cs u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  *3 O  u0 p2 c0 {1,S} {5,S}
3  *2 O  u0 p2 c0 {1,S} {7,S}
4     H  u0 p0 c0 {1,S}
5  *4 H  u0 p0 c0 {2,S}
6     [Cb,Cd,Ct] ux {1,S}
7     H  u0 p0 c0 {3,S}
""",
    kinetics=None,
)

tree(
"""
L1: hemiacetal
    L2: Cs_hemiacetal
        L3: Cs_methanediol
    L2: Cbdt_hemiacetal
        L3: Cbdt_methanediol
"""
)
