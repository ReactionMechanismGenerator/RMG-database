#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["RnCyclic"], ownReverse=False)

reverse = "Ring_Open_Endo_Cycli_Radical"

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*1', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 1,
    label = "Rn",
    group = "OR{R3, R4, R5, R6plus}",
    kinetics = None,
)

entry(
    index = 2,
    label = "multiplebond_intra",
    group = 
"""
1 *2 [Cd,Cdd,Ct,CO,N,CS] u0 {2,[D,T]}
2 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {1,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "radadd_intra",
    group = 
"""
1 *1 R!H u1
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "R3",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {1,S} {3,[D,T]}
3 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {2,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "R4",
    group = 
"""
1 *1 R!H                 u1 {2,[S,D,T,B]}
2 *4 R!H                 ux {1,[S,D,T,B]} {3,S}
3 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R4_S",
    group = 
"""
1 *1 R!H               u1 {2,S}
2 *4 R!H               u0 {1,S} {3,S}
3 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R4_D",
    group = 
"""
1 *1 R!H                u1 {2,D}
2 *4 Cd                u0 {1,D} {3,S}
3 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "R4_T",
    group = 
"""
1 *1 R!H                u1 {2,T}
2 *4 Ct                u0 {1,T} {3,S}
3 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "R5",
    group = 
"""
1 *1 R!H                 u1 {2,[S,D,T,B]}
2 *4 R!H                 ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H                 ux {2,[S,D,T,B]} {4,S}
4 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
""",
)

entry(
    index = 27,
    label = "R5_SS",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 R!H                 u0 {1,S} {3,S}
3 *5 R!H                 u0 {2,S} {4,S}
4 *2 [Cd,Cdd,Ct,CO,N,CS]        u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, single.
""",
)

entry(
    index = 30,
    label = "R5_SM",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 [Cd,Ct,Cb]          u0 {1,S} {3,[D,T,B]}
3 *5 [Cd,Ct,Cb]          u0 {2,[D,T,B]} {4,S}
4 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "R5_SD",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 Cd                  u0 {1,S} {3,D}
3 *5 Cd                  u0 {2,D} {4,S}
4 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then double. (The next is a single)
""",
)

entry(
    index = 39,
    label = "R5_ST",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 Ct                  u0 {1,S} {3,T}
3 *5 Ct                  u0 {2,T} {4,S}
4 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are single, then triple. (The next is a single)
""",
)

entry(
    index = 36,
    label = "R5_MS",
    group = 
"""
1 *1 R!H         u1 {2,[D,T,B]}
2 *4 [Cd,Ct,Cb]          u0 {1,[D,T,B]} {3,S}
3 *5 R!H                 u0 {2,S} {4,S}
4 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "R5_DS",
    group = 
"""
1 *1 R!H                  u1 {2,D}
2 *4 Cd                  u0 {1,D} {3,S}
3 *5 R!H                 u0 {2,S} {4,S}
4 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Cdd,Ct,Od,Sd,N] u0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are double, then single. (The next is a single)
""",
)

entry(
    index = 46,
    label = "R5_TS",
    group = 
"""
1 *1 R!H                  u1 {2,T}
2 *4 Ct                  u0 {1,T} {3,S}
3 *5 R!H                 u0 {2,S} {4,S}
4 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
    longDesc = 
u"""
The ring being formed has 5 atoms in.
Starting at the radical site, the first two bonds are triple, then single. (The next is a single)
""",
)

entry(
    index = 45,
    label = "R5_MM",
    group = 
"""
1 *1 R!H            u1 {2,[D,B]}
2 *4 [Cdd,Cbf]           u0 {1,[D,B]} {3,[D,B]}
3 *5 [Cd,Cb]             u0 {2,[D,B]} {4,S}
4 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "R6plus",
    group = "OR{R6, R7, R8, R9}",
    kinetics = None,
)

entry(
    index = 59,
    label = "R6",
    group = 
"""
1 *1 R!H                 u1 {2,[S,D,T,B]}
2 *4 R!H                 ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                 ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H                 ux {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "R6_RSR",
    group = 
"""
1 *1 R!H                 u1 {2,[S,D,T,B]}
2 *4 R!H                 u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H                 u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H                 u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "R6_SSR",
    group = 
"""
1 *1 R!H               u1 {2,S}
2 *4 R!H               u0 {1,S} {3,S}
3 *6 R!H               u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H               u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "R6_SSS",
    group = 
"""
1 *1 R!H               u1 {2,S}
2 *4 R!H               u0 {1,S} {3,S}
3 *6 R!H               u0 {2,S} {4,S}
4 *5 R!H               u0 {3,S} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "R6_SSM",
    group = 
"""
1 *1 R!H               u1 {2,S}
2 *4 R!H               u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb]        u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]        u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "R6_MSR",
    group = 
"""
1 *1 R!H       u1 {2,[D,T,B]}
2 *4 [Cd,Ct,Cb]        u0 {1,[D,T,B]} {3,S}
3 *6 R!H               u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H               u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "R6_DSR",
    group = 
"""
1 *1 R!H                u1 {2,D}
2 *4 Cd                u0 {1,D} {3,S}
3 *6 R!H               u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H               u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "R6_DSS",
    group = 
"""
1 *1 R!H                u1 {2,D}
2 *4 Cd                u0 {1,D} {3,S}
3 *6 R!H               u0 {2,S} {4,S}
4 *5 R!H               u0 {3,S} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]    u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "R6_DSM",
    group = 
"""
1 *1 R!H                u1 {2,D}
2 *4 Cd                u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb]        u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]        u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "R6_TSR",
    group = 
"""
1 *1 R!H                u1 {2,T}
2 *4 Ct                u0 {1,T} {3,S}
3 *6 R!H               u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H               u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "R6_TSS",
    group = 
"""
1 *1 R!H                u1 {2,T}
2 *4 Ct                u0 {1,T} {3,S}
3 *6 R!H               u0 {2,S} {4,S}
4 *5 R!H               u0 {3,S} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "R6_TSM",
    group = 
"""
1 *1 R!H                u1 {2,T}
2 *4 Ct                u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb]        u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]        u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "R6_SMS",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 [Cd,Ct,Cb]          u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb]          u0 {2,[D,T,B]} {4,S}
4 *5 R!H                 u0 {3,S} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS]    u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "R6_SMM",
    group = 
"""
1 *1 R!H           u1 {2,S}
2 *4 [Cd,Cb]       u0 {1,S} {3,[D,B]}
3 *6 [Cdd,Cbf]     u0 {2,[D,B]} {4,[D,B]}
4 *5 [Cd,Cb]       u0 {3,[D,B]} {5,S}
5 *2 [Cd,Cdd,Ct,CO,N,CS] u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "R7",
    group = 
"""
1 *1 R!H                 u1 {2,[S,D,T,B]}
2 *4 R!H                 ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                 ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                 ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H                 ux {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Cdd,Ct,CO,N,CS]    u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "R8",
    group = 
"""
1 *1 R!H                 u1 {2,[S,D,T,B]}
2 *4 R!H                 ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                 ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                 ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H                 ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H                 ux {5,[S,D,T,B]} {7,S}
7 *2 [Cd,Cdd,Ct,CO,N,CS]    u0 {6,S} {8,[D,T]}
8 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {7,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "R9",
    group = 
"""
1 *1 R!H                 u1 {2,[S,D,T,B]}
2 *4 R!H                 ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                 ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H                 ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H                 ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *9 R!H                 ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *5 R!H                 ux {6,[S,D,T,B]} {8,S}
8 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "R9_SSSSSD",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 R!H                 u0 {1,S} {3,S}
3 *6 R!H                 u0 {2,S} {4,S}
4 *7 R!H                 u0 {3,S} {5,S}
5 *8 R!H                 u0 {4,S} {6,S}
6 *9 R!H                 u0 {5,S} {7,D}
7 *5 R!H                 u0 {6,D} {8,S}
8 *2 [Cd,Cdd,Ct,CO,N,CS]     u0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "R9_SDSSSD",
    group = 
"""
1 *1 R!H                 u1 {2,S}
2 *4 R!H                 u0 {1,S} {3,D}
3 *6 R!H                 u0 {2,D} {4,S}
4 *7 R!H                 u0 {3,S} {5,S}
5 *8 R!H                 u0 {4,S} {6,S}
6 *9 R!H                 u0 {5,S} {7,D}
7 *5 R!H                 u0 {6,D} {8,S}
8 *2 [Cd,Cdd,Ct,CO,N,CS]    u0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "doublebond_intra",
    group = 
"""
1 *2 Cd       u0 {2,D}
2 *3 [Cd,Cdd] u0 {1,D}
""",
    kinetics = None,
    longDesc = 
u"""
Note that nodes below this currently do not match allenic type Cdd atoms for *3,
so this is the most specific group that will match such a molecule.
""",
)

entry(
    index = 115,
    label = "doublebond_intra_pri",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "doublebond_intra_pri_2H",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "doublebond_intra_pri_HNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    H        u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "doublebond_intra_pri_HDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    H             u0 {1,S}
4    H             u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "doublebond_intra_pri_HCd",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    Cd u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "doublebond_intra_pri_HCt",
    group = 
"""
1 *2 Cd u0 {2,D} {3,S}
2 *3 Cd u0 {1,D} {4,S} {5,S}
3    H  u0 {1,S}
4    H  u0 {2,S}
5    Ct u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "doublebond_intra_pri_NdNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "doublebond_intra_pri_NdDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    H             u0 {1,S}
4    [Cs,O,S]      u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "doublebond_intra_pri_NdCd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Cd       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "doublebond_intra_pri_NdCt",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    H        u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Ct       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "doublebond_intra_pri_DeDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    H             u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "doublebond_intra_secNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "doublebond_intra_secNd_2H",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    H        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "doublebond_intra_secNd_HNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "doublebond_intra_secNd_HDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cs,O,S]      u0 {1,S}
4    H             u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "doublebond_intra_secNd_HCd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    Cd       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "doublebond_intra_secNd_HCt",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    H        u0 {2,S}
5    Ct       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "doublebond_intra_secNd_NdNd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "doublebond_intra_secNd_NdDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cs,O,S]      u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "doublebond_intra_secNd_NdCd",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Cd       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "doublebond_intra_secNd_NdCt",
    group = 
"""
1 *2 Cd       u0 {2,D} {3,S}
2 *3 Cd       u0 {1,D} {4,S} {5,S}
3    [Cs,O,S] u0 {1,S}
4    [Cs,O,S] u0 {2,S}
5    Ct       u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "doublebond_intra_secNd_DeDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cs,O,S]      u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "doublebond_intra_secDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "doublebond_intra_secDe_2H",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {2,S}
5    H             u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "doublebond_intra_secDe_HNd",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {2,S}
5    [Cs,O,S]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "doublebond_intra_secDe_HDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "doublebond_intra_secDe_HCd",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {2,S}
5    Cd            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "doublebond_intra_secDe_HCt",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {2,S}
5    Ct            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "doublebond_intra_secDe_NdNd",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cs,O,S]      u0 {2,S}
5    [Cs,O,S]      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "doublebond_intra_secDe_NdDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cs,O,S]      u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "doublebond_intra_secDe_NdCd",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cs,O,S]      u0 {2,S}
5    Cd            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "doublebond_intra_secDe_NdCt",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cs,O,S]      u0 {2,S}
5    Ct            u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "doublebond_intra_secDe_DeDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "triplebond_intra",
    group = 
"""
1 *2 Ct u0 {2,T}
2 *3 Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "triplebond_intra_H",
    group = 
"""
1 *2 Ct u0 {2,T}
2 *3 Ct u0 {1,T} {3,S}
3    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "triplebond_intra_Nd",
    group = 
"""
1 *2 Ct       u0 {2,T}
2 *3 Ct       u0 {1,T} {3,S}
3    [Cs,O,S] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "triplebond_intra_De",
    group = 
"""
1 *2 Ct            u0 {2,T}
2 *3 Ct            u0 {1,T} {3,S}
3    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "carbonyl_intra",
    group = 
"""
1 *2 CO u0 {2,D}
2 *3 Od u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "carbonyl_intra_H",
    group = 
"""
1 *2 CO u0 {2,D} {3,S}
2 *3 Od u0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "carbonyl_intra_Nd",
    group = 
"""
1 *2 CO       u0 {2,D} {3,S}
2 *3 Od       u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "carbonyl_intra_De",
    group = 
"""
1 *2 CO            u0 {2,D} {3,S}
2 *3 Od            u0 {1,D}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "thiyl_intra",
    group = 
"""
1 *2 CS u0 {2,D}
2 *3 Sd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "thiyl_intra_H",
    group = 
"""
1 *2 CS u0 {2,D} {3,S}
2 *3 Sd u0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "thiyl_intra_Nd",
    group = 
"""
1 *2 CS       u0 {2,D} {3,S}
2 *3 Sd       u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "thiyl_intra_De",
    group = 
"""
1 *2 CS            u0 {2,D} {3,S}
2 *3 Sd            u0 {1,D}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "radadd_intra_cs",
    group = 
"""
1 *1 Cs u1
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "radadd_intra_cs2H",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "radadd_intra_csHNd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    H        u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "radadd_intra_csHDe",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "radadd_intra_csHCd",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "radadd_intra_csHCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "radadd_intra_csNdNd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "radadd_intra_csNdDe",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cs,O,S]      u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "radadd_intra_csNdCd",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    Cd       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "radadd_intra_csNdCt",
    group = 
"""
1 *1 Cs       u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    Ct       u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "radadd_intra_csDeDe",
    group = 
"""
1 *1 Cs            u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "radadd_intra_O",
    group = 
"""
1 *1 O u1
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "radadd_intra_S",
    group = 
"""
1 *1 S u1
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "radadd_intra_Cb",
    group = 
"""
1 *1 Cb u1
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "radadd_intra_cdsingle",
    group = 
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "radadd_intra_cdsingleH",
    group = 
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "radadd_intra_cdsingleNd",
    group = 
"""
1 *1 Cd       u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "radadd_intra_cdsingleDe",
    group = 
"""
1 *1 Cd            u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "radadd_intra_cddouble",
    group = 
"""
1 *1 Cd u1 {2,D}
2    Cd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "radadd_intra_CO",
    group = 
"""
1 *1 CO u1 {2,D}
2    O  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "radadd_intra_Ct",
    group = 
"""
1 *1 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    kinetics = None,
)

tree(
"""
L1: Rn
    L2: R3
    L2: R4
        L3: R4_S
        L3: R4_D
        L3: R4_T
    L2: R5
        L3: R5_SS
        L3: R5_SM
            L4: R5_SD
            L4: R5_ST
        L3: R5_MS
            L4: R5_DS
            L4: R5_TS
        L3: R5_MM
    L2: R6plus
        L3: R6
            L4: R6_RSR
                L5: R6_SSR
                    L6: R6_SSS
                    L6: R6_SSM
                L5: R6_MSR
                    L6: R6_DSR
                        L7: R6_DSS
                        L7: R6_DSM
                    L6: R6_TSR
                        L7: R6_TSS
                        L7: R6_TSM
            L4: R6_SMS
            L4: R6_SMM
        L3: R7
        L3: R8
        L3: R9
            L4: R9_SSSSSD
            L4: R9_SDSSSD
L1: multiplebond_intra
    L2: doublebond_intra
        L3: doublebond_intra_pri
            L4: doublebond_intra_pri_2H
            L4: doublebond_intra_pri_HNd
            L4: doublebond_intra_pri_HDe
                L5: doublebond_intra_pri_HCd
                L5: doublebond_intra_pri_HCt
            L4: doublebond_intra_pri_NdNd
            L4: doublebond_intra_pri_NdDe
                L5: doublebond_intra_pri_NdCd
                L5: doublebond_intra_pri_NdCt
            L4: doublebond_intra_pri_DeDe
        L3: doublebond_intra_secNd
            L4: doublebond_intra_secNd_2H
            L4: doublebond_intra_secNd_HNd
            L4: doublebond_intra_secNd_HDe
                L5: doublebond_intra_secNd_HCd
                L5: doublebond_intra_secNd_HCt
            L4: doublebond_intra_secNd_NdNd
            L4: doublebond_intra_secNd_NdDe
                L5: doublebond_intra_secNd_NdCd
                L5: doublebond_intra_secNd_NdCt
            L4: doublebond_intra_secNd_DeDe
        L3: doublebond_intra_secDe
            L4: doublebond_intra_secDe_2H
            L4: doublebond_intra_secDe_HNd
            L4: doublebond_intra_secDe_HDe
                L5: doublebond_intra_secDe_HCd
                L5: doublebond_intra_secDe_HCt
            L4: doublebond_intra_secDe_NdNd
            L4: doublebond_intra_secDe_NdDe
                L5: doublebond_intra_secDe_NdCd
                L5: doublebond_intra_secDe_NdCt
            L4: doublebond_intra_secDe_DeDe
    L2: triplebond_intra
        L3: triplebond_intra_H
        L3: triplebond_intra_Nd
        L3: triplebond_intra_De
    L2: carbonyl_intra
        L3: carbonyl_intra_H
        L3: carbonyl_intra_Nd
        L3: carbonyl_intra_De
    L2: thiyl_intra
        L3: thiyl_intra_H
        L3: thiyl_intra_Nd
        L3: thiyl_intra_De
L1: radadd_intra
    L2: radadd_intra_cs
        L3: radadd_intra_cs2H
        L3: radadd_intra_csHNd
        L3: radadd_intra_csHDe
            L4: radadd_intra_csHCd
            L4: radadd_intra_csHCt
        L3: radadd_intra_csNdNd
        L3: radadd_intra_csNdDe
            L4: radadd_intra_csNdCd
            L4: radadd_intra_csNdCt
        L3: radadd_intra_csDeDe
    L2: radadd_intra_O
    L2: radadd_intra_S
    L2: radadd_intra_Cb
    L2: radadd_intra_cdsingle
        L3: radadd_intra_cdsingleH
        L3: radadd_intra_cdsingleNd
        L3: radadd_intra_cdsingleDe
    L2: radadd_intra_cddouble
    L2: radadd_intra_CO
    L2: radadd_intra_Ct
"""
)

forbidden(
    label = "bond31",
    group = 
"""
1 *3 R!H u0 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "bond31rad",
    group = 
"""
1 *3 R!H u1 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

