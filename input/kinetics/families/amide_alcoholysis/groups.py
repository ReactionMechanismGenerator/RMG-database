#!/usr/bin/env python
# encoding: utf-8

name = "amide_alcoholysis/groups"
shortDesc = ""
longDesc = """
This family describes alcoholysis of an amide species, R2C(=O)N(R3)R4.
The reaction can be acid/base-catalyzed, the template here does not consider a pH effect.
R1OH + R2C(=O)N(R3)R4  <=> R2C(=O)OR1 + HN(R3)R4

atom labels:

R1_O[*1]_H[*2] + R2_C[*3]_(=O)_N[*4]_(R3)_R4 <=> R2_C[*3]_(=O)_O[*1]_R1 + H[*2]_N[*4]_(R3)R4
"""

template(reactants=["Root"], products=["ester", "amine"], ownReverse=False)

reverse = "amine_ester_condensation"
reversible = True
reactantNum = 2
productNum = 2

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['BREAK_BOND', '*3', 1, '*4'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['FORM_BOND', '*2', 1, '*4'],
])

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 *3 C u0 p0 c0 {2,S} {4,S} {5,D}
2 *4 N u0 p1 c0 {1,S} {6,S} {7,S}
3 *1 O u0 p2 c0 {8,S} {9,S}
4    R ux {1,S}
5    O u0 p2 c0 {1,D}
6    R ux {2,S}
7    R ux {2,S}
8 *2 H u0 p0 c0 {3,S}
9    R ux {3,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "Root_6R->C",
    group = 
"""
1 *3 C u0 p0 c0 {2,S} {4,S} {5,D}
2 *4 N u0 p1 c0 {1,S} {6,S} {7,S}
3 *1 O u0 p2 c0 {8,S} {9,S}
4    C ux {1,S}
5    O u0 p2 c0 {1,D}
6    C ux {2,S}
7    H ux {2,S}
8 *2 H u0 p0 c0 {3,S}
9    H ux {3,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Root_6R->C_Ext-4R-R",
    group = 
"""
1  *3 C   u0 p0 c0 {2,S} {4,S} {5,D}
2  *4 N   u0 p1 c0 {1,S} {6,S} {7,S}
3  *1 O   u0 p2 c0 {8,S} {9,S}
4     C   ux r0 {1,S} {10,[S,D,T,B]}
5     O   u0 p2 c0 {1,D}
6     C   ux {2,S}
7     H   ux {2,S}
8  *2 H   u0 p0 c0 {3,S}
9     H   ux {3,S}
10    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Root_N-6R->C",
    group = 
"""
1 *3 C u0 p0 c0 {2,S} {4,S} {5,D}
2 *4 N u0 p1 c0 {1,S} {6,S} {7,S}
3 *1 O u0 p2 c0 {8,S} {9,S}
4    C ux {1,S}
5    O u0 p2 c0 {1,D}
6    H ux {2,S}
7    H ux {2,S}
8 *2 H u0 p0 c0 {3,S}
9    H ux {3,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Root_N-6R->C_4R-inRing",
    group = 
"""
1 *3 C u0 p0 c0 {2,S} {4,S} {5,D}
2 *4 N u0 p1 c0 {1,S} {6,S} {7,S}
3 *1 O u0 p2 c0 {8,S} {9,S}
4    C ux r1 {1,S}
5    O u0 p2 c0 {1,D}
6    H ux {2,S}
7    H ux {2,S}
8 *2 H u0 p0 c0 {3,S}
9    H ux {3,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Root_N-6R->C_N-4R-inRing",
    group = 
"""
1 *3 C u0 p0 c0 {2,S} {4,S} {5,D}
2 *4 N u0 p1 c0 {1,S} {6,S} {7,S}
3 *1 O u0 p2 c0 {8,S} {9,S}
4    C u0 r0 {1,S}
5    O u0 p2 c0 {1,D}
6    H u0 {2,S}
7    H u0 {2,S}
8 *2 H u0 p0 c0 {3,S}
9    H u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Root_N-6R->C_N-4R-inRing_Ext-4R-R",
    group = 
"""
1  *3 C u0 p0 c0 {2,S} {4,S} {5,D}
2  *4 N u0 p1 c0 {1,S} {6,S} {7,S}
3  *1 O u0 p2 c0 {8,S} {9,S}
4     C u0 r0 {1,S} {10,[S,D,T,B]}
5     O u0 p2 c0 {1,D}
6     H u0 {2,S}
7     H u0 {2,S}
8  *2 H u0 p0 c0 {3,S}
9     H u0 {3,S}
10    C ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Root_N-6R->C_N-4R-inRing_Ext-4R-R_Ext-10R!H-R_Ext-10R!H-R",
    group = 
"""
1  *3 C   u0 p0 c0 r0 {2,S} {4,S} {5,D}
2  *4 N   u0 p1 c0 r0 {1,S} {6,S} {7,S}
3  *1 O   u0 p2 c0 r0 {8,S} {9,S}
4     C   u0 r0 {1,S} {10,[S,D,T,B]}
5     O   u0 p2 c0 r0 {1,D}
6     H   u0 r0 {2,S}
7     H   u0 r0 {2,S}
8  *2 H   u0 p0 c0 r0 {3,S}
9     H   u0 r0 {3,S}
10    C   ux {4,[S,D,T,B]} {11,[S,D,T,B]} {12,[S,D,T,B]}
11    R!H ux {10,[S,D,T,B]}
12    R!H ux {10,[S,D,T,B]}
""",
    kinetics = None,
)

tree(
"""
L1: Root
    L2: Root_6R->C
        L3: Root_6R->C_Ext-4R-R
    L2: Root_N-6R->C
        L3: Root_N-6R->C_4R-inRing
        L3: Root_N-6R->C_N-4R-inRing
            L4: Root_N-6R->C_N-4R-inRing_Ext-4R-R
                L5: Root_N-6R->C_N-4R-inRing_Ext-4R-R_Ext-10R!H-R_Ext-10R!H-R
"""
)

