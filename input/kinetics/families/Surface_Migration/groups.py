#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Migration/groups"
shortDesc = u""
longDesc = u"""
Surface species migrating where it binds to the surface.

     *4              *4
      |               |
 *2--*3              *2--*3
  |         ---->         |
~*1~                    ~*1~

The rate, which should be in mol/m2/s,
will be given by k * (mol/m2)
so k should be in (1/s).

"""

template(reactants=["Adsorbate1"], products=["Adsorbate2"], ownReverse=False)

reverse = "Surface_Migration_Reverse"

reactantNum=1
productNum=1

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 1,
    label = "Adsorbate1",
    group =
"""
1 *1 X   ux px cx {2,S}
2 *2 R!H ux px cx {1,S} {3,[S,D]}
3 *3 R!H ux px cx {2,[S,D]} {4,S}
4 *4 R   ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label="*C",
    group =
"""
1 *1 X ux px cx {2,S}
2 *2 C ux px cx {1,S} {3,[S,D]}
3 *3 C ux px cx {2,[S,D]} {4,S}
4 *4 R ux px cx {3,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label="*nC4",
    group =
"""
1 *1 X u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 *4 H u0 p0 c0 {3,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
9    H u0 p0 c0 {8,S}
10   H u0 p0 c0 {8,S}
11   C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12   H u0 p0 c0 {11,S}
13   H u0 p0 c0 {11,S}
14   H u0 p0 c0 {11,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label="*nC6",
    group =
"""
1 *1 X u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 *4 H u0 p0 c0 {3,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
9    H u0 p0 c0 {8,S}
10   H u0 p0 c0 {8,S}
11   C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12   H u0 p0 c0 {11,S}
13   H u0 p0 c0 {11,S}
14   C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15   H u0 p0 c0 {14,S}
16   H u0 p0 c0 {14,S}
17   C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18   H u0 p0 c0 {17,S}
19   H u0 p0 c0 {17,S}
20   H u0 p0 c0 {17,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label="*nC8",
    group =
"""
1 *1 X u0 p0 c0 {2,S}
2 *2 C u0 p0 c0 {1,S} {3,S} {5,S} {6,S}
3 *3 C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
4 *4 H u0 p0 c0 {3,S}
5    H u0 p0 c0 {2,S}
6    H u0 p0 c0 {2,S}
7    H u0 p0 c0 {3,S}
8    C u0 p0 c0 {3,S} {9,S} {10,S} {11,S}
9    H u0 p0 c0 {8,S}
10   H u0 p0 c0 {8,S}
11   C u0 p0 c0 {8,S} {12,S} {13,S} {14,S}
12   H u0 p0 c0 {11,S}
13   H u0 p0 c0 {11,S}
14   C u0 p0 c0 {11,S} {15,S} {16,S} {17,S}
15   H u0 p0 c0 {14,S}
16   H u0 p0 c0 {14,S}
17   C u0 p0 c0 {14,S} {18,S} {19,S} {20,S}
18   H u0 p0 c0 {17,S}
19   H u0 p0 c0 {17,S}
20   C u0 p0 c0 {17,S} {21,S} {22,S} {23,S}
21   H u0 p0 c0 {20,S}
22   H u0 p0 c0 {20,S}
23   C u0 p0 c0 {20,S} {24,S} {25,S} {26,S}
24   H u0 p0 c0 {23,S}
25   H u0 p0 c0 {23,S}
26   H u0 p0 c0 {23,S}
""",
    kinetics = None,
)

tree(
"""
L1: Adsorbate1
    L2: *C
        L3: *nC4
        L3: *nC6
        L3: *nC8
"""
)
