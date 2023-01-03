#!/usr/bin/env python
# encoding: utf-8

name = "imine_to_hemiaminal/groups"
shortDesc = u""
longDesc = u"""
This family describes solution-phase hydrolysis of imine groups:
C=NR + H2O <=> C(OH)N(R1)R2 + H2O 
atom labels:
RC[*1]=N[*2]R' + H[*4]O[*3]H <=>  RC[*1](OH[*3])N[*2](H[*4])R'
"""

template(reactants=["CdN", "H2O"], products=["hemiaminal"], ownReverse=False)

reverse = "condensation_to_imine"

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


entry(
    index=2,
    label="C11H15N",
    group=
"""
1  C u0 p0 c0 {2,D} {6,S} {13,S}
2  C u0 p0 c0 {1,D} {3,S} {14,S}
3  C u0 p0 c0 {2,S} {4,D} {15,S}
4  C u0 p0 c0 {3,D} {5,S} {16,S}
5  C u0 p0 c0 {4,S} {6,D} {17,S}
6  C u0 p0 c0 {1,S} {5,D} {7,S}
7  *1 C u0 p0 c0 {6,S} {8,D} {18,S}
8  *2 N u0 p1 c0 {7,D} {9,S}
9  C u0 p0 c0 {8,S} {10,S} {11,S} {12,S}
10 C u0 p0 c0 {9,S} {19,S} {20,S} {21,S}
11 C u0 p0 c0 {9,S} {22,S} {23,S} {24,S}
12 C u0 p0 c0 {9,S} {25,S} {26,S} {27,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {10,S}
20 H u0 p0 c0 {10,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {11,S}
23 H u0 p0 c0 {11,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {12,S}
""",
    kinetics=None,
)

entry(
    index=3,
    label="C11H14N_p_NO2",
    group=
"""
1  C u0 p0 c0 {2,S} {16,S} {17,S} {18,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  *2 N u0 p1 c0 {2,S} {4,D}
4  *1 C u0 p0 c0 {3,D} {5,S} {19,S}
5  C u0 p0 c0 {4,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,S} {20,S}
7  C u0 p0 c0 {6,S} {8,D} {21,S}
8  C u0 p0 c0 {7,D} {9,S} {12,S}
9  N u0 p0 c+1 {8,S} {10,D} {11,S}
10 O u0 p2 c0 {9,D}
11 O u0 p3 c-1 {9,S}
12 C u0 p0 c0 {8,S} {13,D} {22,S}
13 C u0 p0 c0 {5,S} {12,D} {23,S}
14 C u0 p0 c0 {2,S} {24,S} {25,S} {26,S}
15 C u0 p0 c0 {2,S} {27,S} {28,S} {29,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {1,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {12,S}
23 H u0 p0 c0 {13,S}
24 H u0 p0 c0 {14,S}
25 H u0 p0 c0 {14,S}
26 H u0 p0 c0 {14,S}
27 H u0 p0 c0 {15,S}
28 H u0 p0 c0 {15,S}
29 H u0 p0 c0 {15,S}
""",
    kinetics=None,
)

entry(
    index=4,
    label="C11H14N_m_Br",
    group=
"""
1  C  u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C  u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  *2 N  u0 p1 c0 {2,S} {4,D}
4  *1 C  u0 p0 c0 {3,D} {5,S} {17,S}
5  C  u0 p0 c0 {4,S} {6,D} {11,S}
6  C  u0 p0 c0 {5,D} {7,S} {18,S}
7  C  u0 p0 c0 {6,S} {8,S} {9,D}
8  Br u0 p3 c0 {7,S}
9  C  u0 p0 c0 {7,D} {10,S} {19,S}
10 C  u0 p0 c0 {9,S} {11,D} {20,S}
11 C  u0 p0 c0 {5,S} {10,D} {21,S}
12 C  u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
13 C  u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
14 H  u0 p0 c0 {1,S}
15 H  u0 p0 c0 {1,S}
16 H  u0 p0 c0 {1,S}
17 H  u0 p0 c0 {4,S}
18 H  u0 p0 c0 {6,S}
19 H  u0 p0 c0 {9,S}
20 H  u0 p0 c0 {10,S}
21 H  u0 p0 c0 {11,S}
22 H  u0 p0 c0 {12,S}
23 H  u0 p0 c0 {12,S}
24 H  u0 p0 c0 {12,S}
25 H  u0 p0 c0 {13,S}
26 H  u0 p0 c0 {13,S}
27 H  u0 p0 c0 {13,S}
""",
    kinetics=None,
)

entry(
    index=5,
    label="C11H14N_p_Cl",
    group=
"""
1  C  u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C  u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  *2 N  u0 p1 c0 {2,S} {4,D}
4  *1 C  u0 p0 c0 {3,D} {5,S} {17,S}
5  C  u0 p0 c0 {4,S} {6,D} {11,S}
6  C  u0 p0 c0 {5,D} {7,S} {18,S}
7  C  u0 p0 c0 {6,S} {8,D} {19,S}
8  C  u0 p0 c0 {7,D} {9,S} {10,S}
9  Cl u0 p3 c0 {8,S}
10 C  u0 p0 c0 {8,S} {11,D} {20,S}
11 C  u0 p0 c0 {5,S} {10,D} {21,S}
12 C  u0 p0 c0 {2,S} {22,S} {23,S} {24,S}
13 C  u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
14 H  u0 p0 c0 {1,S}
15 H  u0 p0 c0 {1,S}
16 H  u0 p0 c0 {1,S}
17 H  u0 p0 c0 {4,S}
18 H  u0 p0 c0 {6,S}
19 H  u0 p0 c0 {7,S}
20 H  u0 p0 c0 {10,S}
21 H  u0 p0 c0 {11,S}
22 H  u0 p0 c0 {12,S}
23 H  u0 p0 c0 {12,S}
24 H  u0 p0 c0 {12,S}
25 H  u0 p0 c0 {13,S}
26 H  u0 p0 c0 {13,S}
27 H  u0 p0 c0 {13,S}
""",
    kinetics=None,
)

entry(
    index=6,
    label="C11H14N_p_CH3",
    group=
"""
1  C u0 p0 c0 {2,S} {14,S} {15,S} {16,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  *2 N u0 p1 c0 {2,S} {4,D}
4  *1 C u0 p0 c0 {3,D} {5,S} {17,S}
5  C u0 p0 c0 {4,S} {6,D} {11,S}
6  C u0 p0 c0 {5,D} {7,S} {18,S}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u0 p0 c0 {7,D} {9,S} {10,S}
9  C u0 p0 c0 {8,S} {20,S} {21,S} {22,S}
10 C u0 p0 c0 {8,S} {11,D} {23,S}
11 C u0 p0 c0 {5,S} {10,D} {24,S}
12 C u0 p0 c0 {2,S} {25,S} {26,S} {27,S}
13 C u0 p0 c0 {2,S} {28,S} {29,S} {30,S}
14 H u0 p0 c0 {1,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {12,S}
27 H u0 p0 c0 {12,S}
28 H u0 p0 c0 {13,S}
29 H u0 p0 c0 {13,S}
30 H u0 p0 c0 {13,S}
""",
    kinetics=None,
)

entry(
    index=7,
    label="C11H14N_p_OCH3",
    group=
"""
1  C u0 p0 c0 {2,S} {15,S} {16,S} {17,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  *2 N u0 p1 c0 {2,S} {4,D}
4  *1 C u0 p0 c0 {3,D} {5,S} {18,S}
5  C u0 p0 c0 {4,S} {6,D} {12,S}
6  C u0 p0 c0 {5,D} {7,S} {19,S}
7  C u0 p0 c0 {6,S} {8,D} {20,S}
8  C u0 p0 c0 {7,D} {9,S} {11,S}
9  O u0 p2 c0 {8,S} {10,S}
10 C u0 p0 c0 {9,S} {21,S} {22,S} {23,S}
11 C u0 p0 c0 {8,S} {12,D} {24,S}
12 C u0 p0 c0 {5,S} {11,D} {25,S}
13 C u0 p0 c0 {2,S} {26,S} {27,S} {28,S}
14 C u0 p0 c0 {2,S} {29,S} {30,S} {31,S}
15 H u0 p0 c0 {1,S}
16 H u0 p0 c0 {1,S}
17 H u0 p0 c0 {1,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {10,S}
22 H u0 p0 c0 {10,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {11,S}
25 H u0 p0 c0 {12,S}
26 H u0 p0 c0 {13,S}
27 H u0 p0 c0 {13,S}
28 H u0 p0 c0 {13,S}
29 H u0 p0 c0 {14,S}
30 H u0 p0 c0 {14,S}
31 H u0 p0 c0 {14,S}
""",
    kinetics=None,
)


entry(
    index=8,
    label="oxidated_Sertraline",
    group=
"""
1  Cl u0 p3 c0 {2,S}
2  C  u0 p0 c0 {1,S} {3,D} {19,S}
3  C  u0 p0 c0 {2,D} {4,S} {21,S}
4  C  u0 p0 c0 {3,S} {5,D} {22,S}
5  C  u0 p0 c0 {4,D} {6,S} {18,S}
6  C  u0 p0 c0 {5,S} {7,S} {11,S} {23,S}
7  C  u0 p0 c0 {6,S} {8,D} {17,S}
8  C  u0 p0 c0 {7,D} {9,S} {14,S}
9  *1 C  u0 p0 c0 {8,S} {10,S} {12,D} 
10 C  u0 p0 c0 {9,S} {11,S} {24,S} {25,S}
11 C  u0 p0 c0 {6,S} {10,S} {26,S} {27,S}
12 *2 N  u0 p1 c0 {9,D} {13,S} 
13 C  u0 p0 c0 {12,S} {28,S} {29,S} {30,S}
14 C  u0 p0 c0 {8,S} {15,D} {31,S}
15 C  u0 p0 c0 {14,D} {16,S} {32,S}
16 C  u0 p0 c0 {15,S} {17,D} {33,S}
17 C  u0 p0 c0 {7,S} {16,D} {34,S}
18 C  u0 p0 c0 {5,S} {19,D} {35,S}
19 C  u0 p0 c0 {2,S} {18,D} {20,S}
20 Cl u0 p3 c0 {19,S}
21 H  u0 p0 c0 {3,S}
22 H  u0 p0 c0 {4,S}
23 H  u0 p0 c0 {6,S}
24 H  u0 p0 c0 {10,S}
25 H  u0 p0 c0 {10,S}
26 H  u0 p0 c0 {11,S}
27 H  u0 p0 c0 {11,S}
28 H  u0 p0 c0 {13,S}
29 H  u0 p0 c0 {13,S}
30 H  u0 p0 c0 {13,S}
31 H  u0 p0 c0 {14,S}
32 H  u0 p0 c0 {15,S}
33 H  u0 p0 c0 {16,S}
34 H  u0 p0 c0 {17,S}
35 H  u0 p0 c0 {18,S}
""",
    kinetics=None,
)

tree(
"""
L1: CdN
  L2: C11H15N
  L2: C11H14N_p_NO2
  L2: C11H14N_m_Br
  L2: C11H14N_p_Cl
  L2: C11H14N_p_CH3
  L2: C11H14N_p_OCH3
  L2: oxidated_Sertraline

L1: H2O
"""
)

