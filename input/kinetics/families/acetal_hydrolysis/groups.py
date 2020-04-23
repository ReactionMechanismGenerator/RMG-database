#!/usr/bin/env python
# encoding: utf-8

name = "acetal_hydrolysis/groups"
shortDesc = u""
longDesc = u"""
This family describes hydrolysis of an acetal species (two esters), R1C(OR2)OR3.
The reaction is acid-catalyzed, the template here does not consider a pH effect.
R1C(OR2)OR3 + H2O <=> R1C(OR2)OH + R3OH

atom labels:

R1_C_(O_R2)_O[*1]_R3[*2] + H[*3]_O[*4]_H <=> R1_C_(O_R2)_O[*1]_H[*3] + R3[*2]_O[*4]_H

Some rate data is available here: https://doi.org/10.1021/ja00406a036
"""

template(reactants=["acetal", "H2O"], products=["hemiacetal", "alcohol"], ownReverse=False)

reverse = "alcohol_hemiacetal_condensation"

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
    label="acetal",
    group=
"""
1     Cs u0 p0 c0 {2,S} {3,S} {4,S}
2  *1 O  u0 p2 c0 {1,S} {5,S}
3     O  u0 p2 c0 {1,S} {6,S}
4     H  u0 p0 c0 {1,S}
5  *2 R!H ux px cx {2,S}
6     R!H ux px cx {3,S}
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

entry(
    index=2,
    label="erythromycin_functional",
    group=
"""
1  C u0 p0 c0 {2,S} {17,S} {18,S} {19,S}
2  *2 C u0 p0 c0 {1,S} {3,S} {14,S} {20,S}
3  *1 O u0 p2 c0 {2,S} {4,S}
4  C u0 p0 c0 {3,S} {5,S} {12,S} {21,S}
5  O u0 p2 c0 {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,S} {22,S} {23,S}
7  C u0 p0 c0 {6,S} {8,S} {24,S} {25,S}
8  C u0 p0 c0 {7,S} {9,S} {12,S} {26,S}
9  N u0 p1 c0 {8,S} {10,S} {11,S}
10 C u0 p0 c0 {9,S} {27,S} {28,S} {29,S}
11 C u0 p0 c0 {9,S} {30,S} {31,S} {32,S}
12 C u0 p0 c0 {4,S} {8,S} {13,S} {33,S}
13 O u0 p2 c0 {12,S} {34,S}
14 C u0 p0 c0 {2,S} {15,S} {16,S} {35,S}
15 O u0 p2 c0 {14,S} {36,S}
16 C u0 p0 c0 {14,S} {37,S} {38,S} {39,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {1,S}
20 H u0 p0 c0 {2,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {10,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {10,S}
30 H u0 p0 c0 {11,S}
31 H u0 p0 c0 {11,S}
32 H u0 p0 c0 {11,S}
33 H u0 p0 c0 {12,S}
34 H u0 p0 c0 {13,S}
35 H u0 p0 c0 {14,S}
36 H u0 p0 c0 {15,S}
37 H u0 p0 c0 {16,S}
38 H u0 p0 c0 {16,S}
39 H u0 p0 c0 {16,S}

""",
    kinetics=None,
)

entry(
    index=3,
    label="Cbdt_acetal",
    group=
"""
1    Cs         u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2 *1 O          u0 p2 c0 {1,S} {5,S}
3    O          u0 p2 c0 {1,S} {6,S}
4    H          u0 p0 c0 {1,S}
5 *2 R!H        ux px cx {2,S}
6    R!H        ux px cx {3,S}
7    [Cb,Cd,Ct] ux px cx {1,S}
""",
    kinetics=None,
)

tree(
"""
L1: acetal
  L2: erythromycin_functional
  L2: Cbdt_acetal
L1: H2O
"""
)
