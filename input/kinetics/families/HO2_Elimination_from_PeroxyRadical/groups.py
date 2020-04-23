#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/groups"
shortDesc = u""
longDesc = u"""
Sulfur was added to this family, and is treated the same as oxygen.
Ideally we would like to branch this into a new family "HS2_Elimination_from_PerthiylRadical"
once relevant kinetic data is available
"""

template(reactants=["R2OO"], products=["R=R", "OOH"], ownReverse=False)

reverse = "HO2_concerted_addition"
reversible = True

only_forward = True

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*5'],
    ['BREAK_BOND', '*2', 1, '*3'],
    ['CHANGE_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*4', 1, '*5'],
    ['GAIN_RADICAL', '*3', '1'],
    ['LOSE_RADICAL', '*4', '1'],
])

entry(
    index = 0,
    label = "R2OO",
    group = 
"""
1 *2 [C,Si,N,S]   u0 {2,S} {3,S}
2 *1 [C,Si,O,S,N] u0 {1,S} {5,S}
3 *3 [O,S]        u0 {1,S} {4,S}
4 *4 [O,S]        u1 {3,S}
5 *5 H            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "R2OO_0H",
    group = 
"""
1 *2 C     u0 {2,S} {3,S}
2 *1 Cd    u0 {1,S} {5,S}
3 *3 [O,S] u0 {1,S} {4,S}
4 *4 [O,S] u1 {3,S}
5 *5 H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "R2OO_0H_2H",
    group = 
"""
1 *2 C     u0 {2,S} {3,S} {4,S} {5,S}
2 *1 Cd    u0 {1,S} {7,S}
3 *3 [O,S] u0 {1,S} {6,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *4 [O,S] u1 {3,S}
7 *5 H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "R2OO_O",
    group = 
"""
1 *2 C     u0 {2,S} {3,S}
2 *1 [O,S] u0 {1,S} {5,S}
3 *3 [O,S] u0 {1,S} {4,S}
4 *4 [O,S] u1 {3,S}
5 *5 H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R2OO_O_HNd",
    group = 
"""
1 *2 C     u0 {2,S} {3,S} {4,S} {5,S}
2 *1 [O,S] u0 {1,S} {7,S}
3 *3 [O,S] u0 {1,S} {6,S}
4    H     u0 {1,S}
5    C     u0 {1,S}
6 *4 [O,S] u1 {3,S}
7 *5 H     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R2OO_2H",
    group = 
"""
1 *1 C     u0 {2,S} {4,S} {5,S} {6,S}
2 *2 C     u0 {1,S} {3,S}
3 *3 [O,S] u0 {2,S} {7,S}
4 *5 H     u0 {1,S}
5    H     u0 {1,S}
6    H     u0 {1,S}
7 *4 [O,S] u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R2OO_2H_2H",
    group = 
"""
1 *2 C     u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S] u0 {1,S} {9,S}
4    H     u0 {1,S}
5    H     u0 {1,S}
6 *5 H     u0 {2,S}
7    H     u0 {2,S}
8    H     u0 {2,S}
9 *4 [O,S] u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R2OO_2H_HNd",
    group = 
"""
1 *2 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C        u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]    u0 {1,S} {9,S}
4    H        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
6 *5 H        u0 {2,S}
7    H        u0 {2,S}
8    H        u0 {2,S}
9 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "R2OO_2H_HDe",
    group = 
"""
1 *2 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C                u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]            u0 {1,S} {9,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6 *5 H                u0 {2,S}
7    H                u0 {2,S}
8    H                u0 {2,S}
9 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "R2OO_2H_HCd",
    group = 
"""
1  *2 C     u0 {2,S} {3,S} {4,S} {5,S}
2  *1 C     u0 {1,S} {6,S} {7,S} {8,S}
3  *3 [O,S] u0 {1,S} {9,S}
4     Cd    u0 {1,S} {10,D}
5     H     u0 {1,S}
6  *5 H     u0 {2,S}
7     H     u0 {2,S}
8     H     u0 {2,S}
9  *4 [O,S] u1 {3,S}
10    Cd    u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R2OO_2H_NdNd",
    group = 
"""
1 *2 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C        u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]    u0 {1,S} {9,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {1,S}
6 *5 H        u0 {2,S}
7    H        u0 {2,S}
8    H        u0 {2,S}
9 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "R2OO_2H_NdDe",
    group = 
"""
1 *2 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C                u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]            u0 {1,S} {9,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6 *5 H                u0 {2,S}
7    H                u0 {2,S}
8    H                u0 {2,S}
9 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "R2OO_2H_DeDe",
    group = 
"""
1 *2 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C                u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]            u0 {1,S} {9,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6 *5 H                u0 {2,S}
7    H                u0 {2,S}
8    H                u0 {2,S}
9 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "R2OO_HNd",
    group = 
"""
1 *1 C        u0 {2,S} {4,S} {5,S} {6,S}
2 *2 C        u0 {1,S} {3,S}
3 *3 [O,S]    u0 {2,S} {7,S}
4 *5 H        u0 {1,S}
5    H        u0 {1,S}
6    [Cs,O,S] u0 {1,S}
7 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R2OO_HNd_2H",
    group = 
"""
1 *2 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C        u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]    u0 {1,S} {9,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6 *5 H        u0 {2,S}
7    H        u0 {2,S}
8    [Cs,O,S] u0 {2,S}
9 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "R2OO_HNd_HNd",
    group = 
"""
1 *2 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C        u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]    u0 {1,S} {9,S}
4    H        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
6 *5 H        u0 {2,S}
7    H        u0 {2,S}
8    [Cs,O,S] u0 {2,S}
9 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "R2OO_HNd_HDe",
    group = 
"""
1 *2 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C                u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]            u0 {1,S} {9,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6 *5 H                u0 {2,S}
7    H                u0 {2,S}
8    [Cs,O,S]         u0 {2,S}
9 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "R2OO_HNd_NdNd",
    group = 
"""
1 *2 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C        u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]    u0 {1,S} {9,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {1,S}
6 *5 H        u0 {2,S}
7    H        u0 {2,S}
8    [Cs,O,S] u0 {2,S}
9 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "R2OO_HNd_NdDe",
    group = 
"""
1 *2 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C                u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]            u0 {1,S} {9,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6 *5 H                u0 {2,S}
7    H                u0 {2,S}
8    [Cs,O,S]         u0 {2,S}
9 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "R2OO_HNd_DeDe",
    group = 
"""
1 *2 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C                u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]            u0 {1,S} {9,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6 *5 H                u0 {2,S}
7    H                u0 {2,S}
8    [Cs,O,S]         u0 {2,S}
9 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "R2OO_HDe",
    group = 
"""
1 *1 C                u0 {2,S} {4,S} {5,S} {6,S}
2 *2 C                u0 {1,S} {3,S}
3 *3 [O,S]            u0 {2,S} {7,S}
4 *5 H                u0 {1,S}
5    H                u0 {1,S}
6    [Cd,Ct,Cb,CO,CS] u0 {1,S}
7 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "R2OO_HDe_2H",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    H                u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    H                u0 {2,S}
9    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "R2OO_HDe_HNd",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    H                u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    H                u0 {2,S}
9    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R2OO_HDe_HDe",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    H                u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    H                u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "R2OO_HDe_NdNd",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    H                u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    [Cs,O,S]         u0 {2,S}
9    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "R2OO_HDe_NdDe",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    H                u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    [Cs,O,S]         u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R2OO_HDe_DeDe",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    H                u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    [Cd,Ct,Cb,CO,CS] u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "R2OO_NdNd",
    group = 
"""
1 *1 C        u0 {2,S} {4,S} {5,S} {6,S}
2 *2 C        u0 {1,S} {3,S}
3 *3 [O,S]    u0 {2,S} {7,S}
4 *5 H        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
6    [Cs,O,S] u0 {1,S}
7 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "R2OO_NdNd_2H",
    group = 
"""
1 *2 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C        u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]    u0 {1,S} {9,S}
4    H        u0 {1,S}
5    H        u0 {1,S}
6 *5 H        u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    [Cs,O,S] u0 {2,S}
9 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "R2OO_NdNd_HNd",
    group = 
"""
1 *2 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C        u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]    u0 {1,S} {9,S}
4    H        u0 {1,S}
5    [Cs,O,S] u0 {1,S}
6 *5 H        u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    [Cs,O,S] u0 {2,S}
9 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "R2OO_NdNd_HDe",
    group = 
"""
1 *2 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C                u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]            u0 {1,S} {9,S}
4    H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6 *5 H                u0 {2,S}
7    [Cs,O,S]         u0 {2,S}
8    [Cs,O,S]         u0 {2,S}
9 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "R2OO_NdNd_NdNd",
    group = 
"""
1 *2 C        u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C        u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]    u0 {1,S} {9,S}
4    [Cs,O,S] u0 {1,S}
5    [Cs,O,S] u0 {1,S}
6 *5 H        u0 {2,S}
7    [Cs,O,S] u0 {2,S}
8    [Cs,O,S] u0 {2,S}
9 *4 [O,S]    u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "R2OO_NdNd_NdDe",
    group = 
"""
1 *2 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C                u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]            u0 {1,S} {9,S}
4    [Cs,O,S]         u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6 *5 H                u0 {2,S}
7    [Cs,O,S]         u0 {2,S}
8    [Cs,O,S]         u0 {2,S}
9 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "R2OO_NdNd_DeDe",
    group = 
"""
1 *2 C                u0 {2,S} {3,S} {4,S} {5,S}
2 *1 C                u0 {1,S} {6,S} {7,S} {8,S}
3 *3 [O,S]            u0 {1,S} {9,S}
4    [Cd,Ct,Cb,CO,CS] u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6 *5 H                u0 {2,S}
7    [Cs,O,S]         u0 {2,S}
8    [Cs,O,S]         u0 {2,S}
9 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "R2OO_NdDe",
    group = 
"""
1 *1 C                u0 {2,S} {4,S} {5,S} {6,S}
2 *2 C                u0 {1,S} {3,S}
3 *3 [O,S]            u0 {2,S} {7,S}
4 *5 H                u0 {1,S}
5    [Cs,O,S]         u0 {1,S}
6    [Cd,Ct,Cb,CO,CS] u0 {1,S}
7 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "R2OO_NdDe_2H",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cs,O,S]         u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    H                u0 {2,S}
9    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "R2OO_NdDe_HNd",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cs,O,S]         u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    H                u0 {2,S}
9    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "R2OO_NdDe_HDe",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cs,O,S]         u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    H                u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "R2OO_NdDe_NdNd",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cs,O,S]         u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    [Cs,O,S]         u0 {2,S}
9    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "R2OO_NdDe_NdDe",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cs,O,S]         u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    [Cs,O,S]         u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "R2OO_NdDe_DeDe",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cs,O,S]         u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    [Cd,Ct,Cb,CO,CS] u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "R2OO_DeDe",
    group = 
"""
1 *1 C                u0 {2,S} {4,S} {5,S} {6,S}
2 *2 C                u0 {1,S} {3,S}
3 *3 [O,S]            u0 {2,S} {7,S}
4 *5 H                u0 {1,S}
5    [Cd,Ct,Cb,CO,CS] u0 {1,S}
6    [Cd,Ct,Cb,CO,CS] u0 {1,S}
7 *4 [O,S]            u1 {3,S}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "R2OO_DeDe_2H",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cd,Ct,Cb,CO,CS] u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    H                u0 {2,S}
9    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "R2OO_DeDe_HNd",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cd,Ct,Cb,CO,CS] u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    H                u0 {2,S}
9    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "R2OO_DeDe_HDe",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cd,Ct,Cb,CO,CS] u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    H                u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "R2OO_DeDe_NdNd",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cd,Ct,Cb,CO,CS] u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    [Cs,O,S]         u0 {2,S}
9    [Cs,O,S]         u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "R2OO_DeDe_NdDe",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cd,Ct,Cb,CO,CS] u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    [Cs,O,S]         u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "R2OO_DeDe_DeDe",
    group = 
"""
1 *1 C                u0 {2,S} {5,S} {6,S} {7,S}
2 *2 C                u0 {1,S} {3,S} {8,S} {9,S}
3 *3 [O,S]            u0 {2,S} {4,S}
4 *4 [O,S]            u1 {3,S}
5 *5 H                u0 {1,S}
6    [Cd,Ct,Cb,CO,CS] u0 {1,S}
7    [Cd,Ct,Cb,CO,CS] u0 {1,S}
8    [Cd,Ct,Cb,CO,CS] u0 {2,S}
9    [Cd,Ct,Cb,CO,CS] u0 {2,S}
""",
    kinetics = None,
)

tree(
"""
L1: R2OO
    L2: R2OO_0H
        L3: R2OO_0H_2H
    L2: R2OO_O
        L3: R2OO_O_HNd
    L2: R2OO_2H
        L3: R2OO_2H_2H
        L3: R2OO_2H_HNd
        L3: R2OO_2H_HDe
            L4: R2OO_2H_HCd
        L3: R2OO_2H_NdNd
        L3: R2OO_2H_NdDe
        L3: R2OO_2H_DeDe
    L2: R2OO_HNd
        L3: R2OO_HNd_2H
        L3: R2OO_HNd_HNd
        L3: R2OO_HNd_HDe
        L3: R2OO_HNd_NdNd
        L3: R2OO_HNd_NdDe
        L3: R2OO_HNd_DeDe
    L2: R2OO_HDe
        L3: R2OO_HDe_2H
        L3: R2OO_HDe_HNd
        L3: R2OO_HDe_HDe
        L3: R2OO_HDe_NdNd
        L3: R2OO_HDe_NdDe
        L3: R2OO_HDe_DeDe
    L2: R2OO_NdNd
        L3: R2OO_NdNd_2H
        L3: R2OO_NdNd_HNd
        L3: R2OO_NdNd_HDe
        L3: R2OO_NdNd_NdNd
        L3: R2OO_NdNd_NdDe
        L3: R2OO_NdNd_DeDe
    L2: R2OO_NdDe
        L3: R2OO_NdDe_2H
        L3: R2OO_NdDe_HNd
        L3: R2OO_NdDe_HDe
        L3: R2OO_NdDe_NdNd
        L3: R2OO_NdDe_NdDe
        L3: R2OO_NdDe_DeDe
    L2: R2OO_DeDe
        L3: R2OO_DeDe_2H
        L3: R2OO_DeDe_HNd
        L3: R2OO_DeDe_HDe
        L3: R2OO_DeDe_NdNd
        L3: R2OO_DeDe_NdDe
        L3: R2OO_DeDe_DeDe
"""
)

