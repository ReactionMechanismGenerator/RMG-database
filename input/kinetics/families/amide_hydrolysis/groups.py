#!/usr/bin/env python
# encoding: utf-8

name = "amide_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of amide groups:
R2C(=O)NR1 + H2O <=> R1C(=O)OH + HNR2
atom labels:
R2C[*1]_(=O)N[*2]_R1 + H[*4]_O[*3]_H <=> R1C[*1](=O)O[*3]H + H[*4]_N[*2]_R2
"""

template(reactants=["COdN", "H2O"], products=["COdOH", "HNR"], ownReverse=False)

reverse = "condensation_to_amide"

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
    label="COdN",
    group=
"""
1    R  ux px cx {2,S}
2 *1 C  u0 p0 c0 {1,S} {3,D} {4,S}
3    O  u0 p2 c0 {2,D}
4 *2 N  u0 p1 c0 {2,S} {5,S} {6,S}
5    R  ux px cx {4,S}
6    R  ux px cx {4,S}
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

entry(
    index=2,
    label="Diazepam_after_imine_hydrolysis",
    group=
"""
1     C  u0 p0 c0 {2,S} {6,D} {21,S}
2     C  u0 p0 c0 {1,S} {3,D} {22,S}
3     C  u0 p0 c0 {2,D} {4,S} {23,S}
4     C  u0 p0 c0 {3,S} {5,D} {24,S}
5     C  u0 p0 c0 {4,D} {6,S} {25,S}
6     C  u0 p0 c0 {1,D} {5,S} {7,S}
7     C  u0 p0 c0 {6,S} {34,D} {20,S}
8     N  u0 p1 c0 {9,S} {35,S} {36,S}
9     C  u0 p0 c0 {8,S} {10,S} {26,S} {27,S}
10 *1 C  u0 p0 c0 {9,S} {11,D} {12,S}
11    O  u0 p2 c0 {10,D}
12 *2 N  u0 p1 c0 {10,S} {13,S} {14,S}
13    C  u0 p0 c0 {12,S} {28,S} {29,S} {30,S}
14    C  u0 p0 c0 {12,S} {15,S} {20,D}
15    C  u0 p0 c0 {14,S} {16,D} {31,S}
16    C  u0 p0 c0 {15,D} {17,S} {32,S}
17    C  u0 p0 c0 {16,S} {18,S} {19,D}
18    Cl u0 p3 c0 {17,S}
19    C  u0 p0 c0 {17,D} {20,S} {33,S}
20    C  u0 p0 c0 {7,S} {14,D} {19,S}
21    H  u0 p0 c0 {1,S}
22    H  u0 p0 c0 {2,S}
23    H  u0 p0 c0 {3,S}
24    H  u0 p0 c0 {4,S}
25    H  u0 p0 c0 {5,S}
26    H  u0 p0 c0 {9,S}
27    H  u0 p0 c0 {9,S}
28    H  u0 p0 c0 {13,S}
29    H  u0 p0 c0 {13,S}
30    H  u0 p0 c0 {13,S}
31    H  u0 p0 c0 {15,S}
32    H  u0 p0 c0 {16,S}
33    H  u0 p0 c0 {19,S}
34    O  u0 p2 c0 {7,D}
35    H  u0 p0 c0 {8,S}
36    H  u0 p0 c0 {8,S}
""",
    kinetics=None,
)


tree(
"""
L1: COdN
  L2: Diazepam_after_imine_hydrolysis
L1: H2O
"""
)
