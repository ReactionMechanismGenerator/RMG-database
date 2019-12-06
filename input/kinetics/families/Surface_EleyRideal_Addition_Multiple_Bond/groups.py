#!/usr/bin/env python
# encoding: utf-8

name = "Surface_EleyRideal_Addition_Multiple_Bond/groups"
shortDesc = u""
longDesc = u"""
Eeley Rideal reaction with a gas phase double, triple, or quadruple bonded species with a species (most likely hydrogen) directly bonded to the surface.

 *2    *4=*3         *3-*4-*2
  |          ---->    |
~*1~ +              ~*1~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2) * (mol/m3)
so k should be in (m3/mol/s).

This is from Theoretical Investigation of the Mechanisms for Olefinic Hydrogenation on
Pt(110) and Pt(111) Surfaces
Vincent Maurice & Christian Minot, J. Phys. Chem. 1990, 94, 8579-8588

and inspired by Ethylene Dimerization and Oligomerization to 1-Butene and Higher Olefins with Chromium-Promoted Cobalt on Carbon Catalyst by Xu et al. Doi:10.1021/acscatal.7b03205

"""

template(reactants=["Adsorbate1", "Gas"], products=["Adsorbate2"], ownReverse=False)

reverse = "Surface_EleyRideal_Deletion_Multiple_Bond"

reactantNum=2
productNum=1

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['CHANGE_BOND', '*3', -1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbate1",
    group =
"""
1 *1 X  ux px cx {2,S}
2 *2 R  ux px cx {1,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="Gas",
    group =
"""
1 *3 R!H ux px cx {2,[D,T,Q]}
2 *4 R!H ux px cx {1,[D,T,Q]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label="*H",
    group =
"""
1 *1 X u0 p0 c0 {2,S}
2 *2 H u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label="*C",
    group =
"""
1 *1 X u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label="R=R",
    group =
"""
1 *3 R!H ux px cx {2,D}
2 *4 R!H ux px cx {1,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label="R#R",
    group =
"""
1 *3 R!H ux px cx {2,T}
2 *4 R!H ux px cx {1,T}
""",
    kinetics = None,
)

entry(
    index = 7,
    label="C=C",
    group =
"""
1 *3 C u0 p0 c0 {2,D}
2 *4 C u0 p0 c0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 8,
    label="C#C",
    group =
"""
1 *3 C u0 p0 c0 {2,T}
2 *4 C u0 p0 c0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 9,
    label="*C2",
    group =
"""
1 *1 X u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3    H u0 p0 c0 {2,S}
4    H u0 p0 c0 {2,S}
5    C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
6    H u0 p0 c0 {5,S}
7    H u0 p0 c0 {5,S}
8    H u0 p0 c0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label="*C4",
    group =
"""
1 *1 X u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3    H u0 p0 c0 {2,S}
4    H u0 p0 c0 {2,S}
5    C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
6    C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7    C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
8    H u0 p0 c0 {5,S}
9    H u0 p0 c0 {5,S}
10   H u0 p0 c0 {6,S}
11   H u0 p0 c0 {6,S}
12   H u0 p0 c0 {7,S}
13   H u0 p0 c0 {7,S}
14   H u0 p0 c0 {7,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label="*C6",
    group =
"""
1 *1 X u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3    H u0 p0 c0 {2,S}
4    H u0 p0 c0 {2,S}
5    C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
6    C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7    C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
8    H u0 p0 c0 {5,S}
9    H u0 p0 c0 {5,S}
10   H u0 p0 c0 {6,S}
11   H u0 p0 c0 {6,S}
12   H u0 p0 c0 {7,S}
13   H u0 p0 c0 {7,S}
14   C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
15   C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
16   H u0 p0 c0 {14,S}
17   H u0 p0 c0 {14,S}
18   H u0 p0 c0 {15,S}
19   H u0 p0 c0 {15,S}
20   H u0 p0 c0 {15,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label="*C8",
    group =
"""
1 *1 X u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3    H u0 p0 c0 {2,S}
4    H u0 p0 c0 {2,S}
5    C u0 p0 c0 {2,S} {6,S} {8,S} {9,S}
6    C u0 p0 c0 {5,S} {7,S} {10,S} {11,S}
7    C u0 p0 c0 {6,S} {12,S} {13,S} {14,S}
8    H u0 p0 c0 {5,S}
9    H u0 p0 c0 {5,S}
10   H u0 p0 c0 {6,S}
11   H u0 p0 c0 {6,S}
12   H u0 p0 c0 {7,S}
13   H u0 p0 c0 {7,S}
14   C u0 p0 c0 {7,S} {15,S} {16,S} {17,S}
15   C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
16   H u0 p0 c0 {14,S}
17   H u0 p0 c0 {14,S}
18   H u0 p0 c0 {15,S}
19   H u0 p0 c0 {15,S}
20   C u0 p0 c0 {15,S} {21,S} {22,S} {23,S}
21   C u0 p0 c0 {20,S} {24,S} {25,S} {26,S}
22   H u0 p0 c0 {20,S}
23   H u0 p0 c0 {20,S}
24   H u0 p0 c0 {21,S}
25   H u0 p0 c0 {21,S}
26   H u0 p0 c0 {21,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label="CH2=CH2",
    group =
"""
1 *3 C u0 p0 c0 {2,D} {3,S} {4,S}
2 *4 C u0 p0 c0 {1,D} {5,S} {6,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {1,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label="HC#CH",
    group =
"""
1 *3 C u0 p0 c0 {2,T} {3,S}
2 *4 C u0 p0 c0 {1,T} {4,S}
3    H u0 p0 c0 {1,S}
4    H u0 p0 c0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate1
    L2: *H
    L2: *C
        L3: *C2
        L3: *C4
        L3: *C6
        L3: *C8
L1: Gas
    L2: R=R
        L3: C=C
            L4: CH2=CH2
    L2: R#R
        L3: C#C
            L4: HC#CH
"""
)
