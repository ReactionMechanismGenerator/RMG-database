#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Rn"], products=["RnCycle"], ownReverse=False)

reverse = "Ring_Open_Exo_Cycli_Radical"

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*3', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 1,
    label = "Rn",
    group = "OR{R4, R5, R6, R7plus}",
    kinetics = None,
)

entry(
    index = 2,
    label = "multiplebond_intra",
    group = 
"""
1 *2 [Cd,Ct,CO,N]     u0 {2,[D,T]}
2 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {1,[D,T]}
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
    label = "R4",
    group = 
"""
1 *1 R!H              u1 {2,[S,D,T,B]}
2 *4 R!H              ux {1,[S,D,T,B]} {3,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "R4_S",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 R!H            u0 {1,S} {3,S}
3 *2 [Cd,Ct,CO]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,S2d,Cdd] u0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "R4_S_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "R4_S_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 Ct  u0 {2,S} {4,T}
4 *3 Ct  u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "R4_S_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 CO  u0 {2,S} {4,D}
4 *3 Od  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "R4_D",
    group = 
"""
1 *1 Cd             u1 {2,D}
2 *4 Cd             u0 {1,D} {3,S}
3 *2 [Cd,Ct,CO]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,S2d,Cdd] u0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "R4_D_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "R4_D_T",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *2 Ct u0 {2,S} {4,T}
4 *3 Ct u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "R4_D_CO",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *2 CO u0 {2,S} {4,D}
4 *3 Od u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "R4_T",
    group = 
"""
1 *1 Ct             u1 {2,T}
2 *4 Ct             u0 {1,T} {3,S}
3 *2 [Cd,Ct,CO]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,S2d,Cdd] u0 {3,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "R4_T_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "R4_T_T",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T} {3,S}
3 *2 Ct u0 {2,S} {4,T}
4 *3 Ct u0 {3,T}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "R4_T_CO",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T} {3,S}
3 *2 CO u0 {2,S} {4,D}
4 *3 Od u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "R5",
    group = 
"""
1 *1 R!H                 u1 {2,[S,D,T,B]}
2 *4 R!H                 ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H                 ux {2,[S,D,T,B]} {4,S}
4 *2 [Cd,Ct,CO,N]        u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "R5_SS",
    group = 
"""
1 *1 R!H              u1 {2,S}
2 *4 R!H              u0 {1,S} {3,S}
3 *5 R!H              u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R5_SS_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "R5_SS_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "R5_SS_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 Od  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "R5_SM",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 [Cd,Ct,Cb]     u0 {1,S} {3,[B,T,D]}
3 *5 [Cd,Ct,Cb]     u0 {2,[B,T,D]} {4,S}
4 *2 [Cd,Ct,CO,N]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "R5_SD",
    group = 
"""
1 *1 R!H              u1 {2,S}
2 *4 Cd               u0 {1,S} {3,D}
3 *5 Cd               u0 {2,D} {4,S}
4 *2 [Cd,Ct,CO,N]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "R5_SD_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 Cd       u0 {1,S} {3,D}
3 *5 Cd       u0 {2,D} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "R5_SD_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "R5_SD_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 Od  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "R5_DS",
    group = 
"""
1 *1 Cd               u1 {2,D}
2 *4 Cd               u0 {1,D} {3,S}
3 *5 R!H              u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "R5_DS_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "R5_DS_T",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "R5_DS_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 Od  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "R5_ST",
    group = 
"""
1 *1 R!H              u1 {2,S}
2 *4 Ct               u0 {1,S} {3,T}
3 *5 Ct               u0 {2,T} {4,S}
4 *2 [Cd,Ct,CO,N]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "R5_ST_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 Ct       u0 {1,S} {3,T}
3 *5 Ct       u0 {2,T} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "R5_ST_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "R5_ST_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 Od  u0 {4,D}
""",
    kinetics = None,
)


entry(
    index = 31,
    label = "R5_MS",
    group = 
"""
1 *1 [Cd,Ct,Cb]     u1 {2,[B,T,D]}
2 *4 [Cd,Ct,Cb]     u0 {1,[B,T,D]} {3,S}
3 *5 R!H            u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "R5_TS",
    group = 
"""
1 *1 Ct               u1 {2,T}
2 *4 Ct               u0 {1,T} {3,S}
3 *5 R!H              u0 {2,S} {4,S}
4 *2 [Cd,Ct,CO,N]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "R5_TS_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *5 R!H      u0 {2,S} {4,S}
4 *2 Cd       u0 {3,S} {5,D}
5 *3 [Cd,Cdd] u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "R5_TS_T",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 Ct  u0 {3,S} {5,T}
5 *3 Ct  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "R5_TS_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 CO  u0 {3,S} {5,D}
5 *3 Od  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "R5_MM",
    group = 
"""
1 *1 Cd             u1 {2,[B,D]}
2 *4 [Cdd,Cbf]      u0 {1,[B,D]} {3,[B,D]}
3 *5 [Cb,Cd]        u0 {2,[B,D]} {4,S}
4 *2 [Cd,Ct,CO,N]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "R6",
    group = 
"""
1 *1 R!H                 u1 {2,[S,D,T,B]}
2 *4 R!H                 ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H                 ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H                 ux {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,N]        u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "R6_RSR",
    group = 
"""
1 *1 R!H              u1 {2,[S,D,T,B]}
2 *4 R!H              u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H              u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H              u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,N]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "R6_SSR",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 R!H            u0 {1,S} {3,S}
3 *6 R!H            u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H            u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "R6_SSS",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 R!H            u0 {1,S} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *5 R!H            u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "R6_SSS_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "R6_SSS_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 {4,S} {6,T}
6 *3 Ct  u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "R6_SSS_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 {4,S} {6,D}
6 *3 Od  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "R6_SSM",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 R!H            u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb]     u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]     u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "R6_SSM_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "R6_SSM_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "R6_SSM_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 Od         u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "R6_MSR",
    group = 
"""
1 *1 [Cd,Ct,Cb]     u1 {2,[D,T,B]}
2 *4 [Cd,Ct,Cb]     u0 {1,[D,T,B]} {3,S}
3 *6 R!H            u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H            u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO,N]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "R6_DSR",
    group = 
"""
1 *1 Cd             u1 {2,D}
2 *4 Cd             u0 {1,D} {3,S}
3 *6 R!H            u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H            u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "R6_DSS",
    group = 
"""
1 *1 Cd             u1 {2,D}
2 *4 Cd             u0 {1,D} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *5 R!H            u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "R6_DSS_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "R6_DSS_T",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 {4,S} {6,T}
6 *3 Ct  u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "R6_DSS_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 {4,S} {6,D}
6 *3 Od  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "R6_DSM",
    group = 
"""
1 *1 Cd             u1 {2,D}
2 *4 Cd             u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb]     u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]     u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "R6_DSM_D",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "R6_DSM_T",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "R6_DSM_CO",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 Od         u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "R6_TSR",
    group = 
"""
1 *1 Ct             u1 {2,T}
2 *4 Ct             u0 {1,T} {3,S}
3 *6 R!H            u0 {2,S} {4,[S,D,T,B]}
4 *5 R!H            u0 {3,[S,D,T,B]} {5,S}
5 *2 [Cd,Ct,CO]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "R6_TSS",
    group = 
"""
1 *1 Ct             u1 {2,T}
2 *4 Ct             u0 {1,T} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *5 R!H            u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "R6_TSS_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *5 R!H      u0 {3,S} {5,S}
5 *2 Cd       u0 {4,S} {6,D}
6 *3 [Cd,Cdd] u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "R6_TSS_T",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 Ct  u0 {4,S} {6,T}
6 *3 Ct  u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "R6_TSS_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 CO  u0 {4,S} {6,D}
6 *3 Od  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "R6_TSM",
    group = 
"""
1 *1 Ct             u1 {2,T}
2 *4 Ct             u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb]     u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb]     u0 {3,[D,T,B]} {5,S}
5 *2 [Cd,Ct,CO]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "R6_TSM_D",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "R6_TSM_T",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "R6_TSM_CO",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *5 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 Od         u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "R6_SMS",
    group = 
"""
1 *1 R!H              u1 {2,S}
2 *4 [Cd,Ct,Cb]       u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb]       u0 {2,[D,T,B]} {4,S}
4 *5 R!H              u0 {3,S} {5,S}
5 *2 [Cd,Ct,CO,N]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "R6_SMS_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 Cd         u0 {4,S} {6,D}
6 *3 [Cd,Cdd]   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "R6_SMS_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 Ct         u0 {4,S} {6,T}
6 *3 Ct         u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "R6_SMS_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *5 R!H        u0 {3,S} {5,S}
5 *2 CO         u0 {4,S} {6,D}
6 *3 Od         u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "R6_SMM",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 [Cd,Cb]        u0 {1,S} {3,[D,B]}
3 *6 [Cdd,Cbf]      u0 {2,[D,B]} {4,[D,B]}
4 *5 [Cd,Cb]        u0 {3,[D,B]} {5,S}
5 *2 [Cd,Ct,CO,N]     u0 {4,S} {6,[D,T]}
6 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "R7plus",
    group = "OR{R7, R8, R9}",
    kinetics = None,
)

entry(
    index = 100,
    label = "R7",
    group = 
"""
1 *1 R!H              u1 {2,[S,D,T,B]}
2 *4 R!H              ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H              ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H              ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H              ux {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO,N]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "R7_RSSR",
    group = 
"""
1 *1 R!H              u1 {2,[S,D,T,B]}
2 *4 R!H              u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H              u0 {2,S} {4,S}
4 *7 R!H              u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H              u0 {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO,N]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "R7_SSSR",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 R!H            u0 {1,S} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 R!H            u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H            u0 {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "R7_SSSS",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 R!H            u0 {1,S} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 R!H            u0 {3,S} {5,S}
5 *5 R!H            u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "R7_SSSS_D",
    group = 
"""
1 *1 R!H      u1 {2,S}
2 *4 R!H      u0 {1,S} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *7 R!H      u0 {3,S} {5,S}
5 *5 R!H      u0 {4,S} {6,S}
6 *2 Cd       u0 {5,S} {7,D}
7 *3 [Cd,Cdd] u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "R7_SSSS_T",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 Ct  u0 {5,S} {7,T}
7 *3 Ct  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "R7_SSSS_CO",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 CO  u0 {5,S} {7,D}
7 *3 Od  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "R7_SSSM",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 R!H            u0 {1,S} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb]     u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb]     u0 {4,[D,T,B]} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "R7_SSSM_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 Cd         u0 {5,S} {7,D}
7 *3 [Cd,Cdd]   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "R7_SSSM_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 Ct         u0 {5,S} {7,T}
7 *3 Ct         u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "R7_SSSM_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 CO         u0 {5,S} {7,D}
7 *3 Od         u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "R7_MSSR",
    group = 
"""
1 *1 [Cd,Ct,Cb]     u1 {2,[D,B,T]}
2 *4 [Cd,Ct,Cb]     u0 {1,[D,B,T]} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 R!H            u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H            u0 {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO,N]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "R7_DSSR",
    group = 
"""
1 *1 Cd             u1 {2,D}
2 *4 Cd             u0 {1,D} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 R!H            u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H            u0 {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "R7_DSSS",
    group = 
"""
1 *1 Cd             u1 {2,D}
2 *4 Cd             u0 {1,D} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 R!H            u0 {3,S} {5,S}
5 *5 R!H            u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "R7_DSSS_D",
    group = 
"""
1 *1 Cd       u1 {2,D}
2 *4 Cd       u0 {1,D} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *7 R!H      u0 {3,S} {5,S}
5 *5 R!H      u0 {4,S} {6,S}
6 *2 Cd       u0 {5,S} {7,D}
7 *3 [Cd,Cdd] u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "R7_DSSS_T",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 Ct  u0 {5,S} {7,T}
7 *3 Ct  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "R7_DSSS_CO",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 CO  u0 {5,S} {7,D}
7 *3 Od  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "R7_DSSM",
    group = 
"""
1 *1 Cd             u1 {2,D}
2 *4 Cd             u0 {1,D} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb]     u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb]     u0 {4,[D,T,B]} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "R7_DSSM_D",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 Cd         u0 {5,S} {7,D}
7 *3 [Cd,Cdd]   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "R7_DSSM_T",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 Ct         u0 {5,S} {7,T}
7 *3 Ct         u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "R7_DSSM_CO",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 CO         u0 {5,S} {7,D}
7 *3 Od         u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "R7_TSSR",
    group = 
"""
1 *1 Ct             u1 {2,T}
2 *4 Ct             u0 {1,T} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 R!H            u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H            u0 {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "R7_TSSS",
    group = 
"""
1 *1 Ct             u1 {2,T}
2 *4 Ct             u0 {1,T} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 R!H            u0 {3,S} {5,S}
5 *5 R!H            u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "R7_TSSS_D",
    group = 
"""
1 *1 Ct       u1 {2,T}
2 *4 Ct       u0 {1,T} {3,S}
3 *6 R!H      u0 {2,S} {4,S}
4 *7 R!H      u0 {3,S} {5,S}
5 *5 R!H      u0 {4,S} {6,S}
6 *2 Cd       u0 {5,S} {7,D}
7 *3 [Cd,Cdd] u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "R7_TSSS_T",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 Ct  u0 {5,S} {7,T}
7 *3 Ct  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "R7_TSSS_CO",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 CO  u0 {5,S} {7,D}
7 *3 Od  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "R7_TSSM",
    group = 
"""
1 *1 Ct             u1 {2,T}
2 *4 Ct             u0 {1,T} {3,S}
3 *6 R!H            u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb]     u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb]     u0 {4,[D,T,B]} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "R7_TSSM_D",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 Cd         u0 {5,S} {7,D}
7 *3 [Cd,Cdd]   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "R7_TSSM_T",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 Ct         u0 {5,S} {7,T}
7 *3 Ct         u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "R7_TSSM_CO",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 R!H        u0 {2,S} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 CO         u0 {5,S} {7,D}
7 *3 Od         u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "R7_RSMS",
    group = 
"""
1 *1 R!H              u1 {2,[S,D,T,B]}
2 *4 R!H              u0 {1,[S,D,T,B]} {3,S}
3 *6 [Cd,Ct,Cb]       u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb]       u0 {3,[D,T,B]} {5,S}
5 *5 R!H              u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO,N]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "R7_SSMS",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 R!H            u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb]     u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb]     u0 {3,[D,T,B]} {5,S}
5 *5 R!H            u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "R7_SSMS_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 Cd         u0 {5,S} {7,D}
7 *3 [Cd,Cdd]   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "R7_SSMS_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 Ct         u0 {5,S} {7,T}
7 *3 Ct         u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "R7_SSMS_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 R!H        u0 {1,S} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 CO         u0 {5,S} {7,D}
7 *3 Od         u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "R7_MSMS",
    group = 
"""
1 *1 [Cd,Ct,Cb]     u1 {2,[B,T,D]}
2 *4 [Cd,Ct,Cb]     u0 {1,[B,T,D]} {3,S}
3 *6 [Cd,Ct,Cb]     u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb]     u0 {3,[D,T,B]} {5,S}
5 *5 R!H            u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO,N]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "R7_DSMS",
    group = 
"""
1 *1 Cd             u1 {2,D}
2 *4 Cd             u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb]     u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb]     u0 {3,[D,T,B]} {5,S}
5 *5 R!H            u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "R7_DSMS_D",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 Cd         u0 {5,S} {7,D}
7 *3 [Cd,Cdd]   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "R7_DSMS_T",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 Ct         u0 {5,S} {7,T}
7 *3 Ct         u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "R7_DSMS_CO",
    group = 
"""
1 *1 Cd         u1 {2,D}
2 *4 Cd         u0 {1,D} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 CO         u0 {5,S} {7,D}
7 *3 Od         u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "R7_TSMS",
    group = 
"""
1 *1 Ct             u1 {2,T}
2 *4 Ct             u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb]     u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb]     u0 {3,[D,T,B]} {5,S}
5 *5 R!H            u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "R7_TSMS_D",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 Cd         u0 {5,S} {7,D}
7 *3 [Cd,Cdd]   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "R7_TSMS_T",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 Ct         u0 {5,S} {7,T}
7 *3 Ct         u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "R7_TSMS_CO",
    group = 
"""
1 *1 Ct         u1 {2,T}
2 *4 Ct         u0 {1,T} {3,S}
3 *6 [Cd,Ct,Cb] u0 {2,S} {4,[D,T,B]}
4 *7 [Cd,Ct,Cb] u0 {3,[D,T,B]} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 CO         u0 {5,S} {7,D}
7 *3 Od         u0 {6,D}
""",
    kinetics = None,
)


entry(
    index = 155,
    label = "R7_SMSR",
    group = 
"""
1 *1 R!H              u1 {2,S}
2 *4 [Cd,Ct,Cb]       u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb]       u0 {2,[D,T,B]} {4,S}
4 *7 R!H              u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H              u0 {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO,N]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "R7_SMSS",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 [Cd,Ct,Cb]     u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb]     u0 {2,[D,T,B]} {4,S}
4 *7 R!H            u0 {3,S} {5,S}
5 *5 R!H            u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "R7_SMSS_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *7 R!H        u0 {3,S} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 Cd         u0 {5,S} {7,D}
7 *3 [Cd,Cdd]   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "R7_SMSS_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *7 R!H        u0 {3,S} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 Ct         u0 {5,S} {7,T}
7 *3 Ct         u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "R7_SMSS_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *7 R!H        u0 {3,S} {5,S}
5 *5 R!H        u0 {4,S} {6,S}
6 *2 CO         u0 {5,S} {7,D}
7 *3 Od         u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "R7_SMSM",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 [Cd,Ct,Cb]     u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb]     u0 {2,[D,T,B]} {4,S}
4 *7 [Cd,Ct,Cb]     u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb]     u0 {4,[D,T,B]} {6,S}
6 *2 [Cd,Ct,CO]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "R7_SMSM_D",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 Cd         u0 {5,S} {7,D}
7 *3 [Cd,Cdd]   u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "R7_SMSM_T",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 Ct         u0 {5,S} {7,T}
7 *3 Ct         u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "R7_SMSM_CO",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *6 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *7 [Cd,Ct,Cb] u0 {3,S} {5,[D,T,B]}
5 *5 [Cd,Ct,Cb] u0 {4,[D,T,B]} {6,S}
6 *2 CO         u0 {5,S} {7,D}
7 *3 Od         u0 {6,D}
""",
    kinetics = None,
)


entry(
    index = 130,
    label = "R7_MMSR",
    group = 
"""
1 *1 [Cb,Cd]        u1 {2,[B,D]}
2 *4 [Cbf,Cdd]      u0 {1,[B,D]} {3,[B,D]}
3 *6 [Cb,Cd]        u0 {2,[B,D]} {4,S}
4 *7 R!H            u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H            u0 {4,[S,D,T,B]} {6,S}
6 *2 [Cd,Ct,CO,N]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "R7_RSMM",
    group = 
"""
1 *1 R!H            u1 {2,[S,D,T,B]}
2 *4 R!H            u0 {1,[S,D,T,B]} {3,S}
3 *6 [Cb,Cd]        u0 {2,S} {4,[D,B]}
4 *7 [Cbf,Cdd]      u0 {3,[D,B]} {5,[D,B]}
5 *5 [Cb,Cd]        u0 {4,[D,B]} {6,S}
6 *2 [Cd,Ct,CO,N]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "R7_SMMS",
    group = 
"""
1 *1 R!H            u1 {2,S}
2 *4 [Cb,Cd]        u0 {1,S} {3,[D,B]}
3 *6 [Cbf,Cdd]      u0 {2,[D,B]} {4,[D,B]}
4 *7 [Cb,Cd]        u0 {3,[D,B]} {5,S}
5 *5 R!H            u0 {4,S} {6,S}
6 *2 [Cd,Ct,CO,N]     u0 {5,S} {7,[D,T]}
7 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {6,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "R8",
    group = 
"""
1 *1 R!H           u1 {2,[S,D,T,B]}
2 *4 R!H           ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H           ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H           ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H           ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H           ux {5,[S,D,T,B]} {7,S}
7 *2 [Cd,Ct,CO,N]   u0 {6,S} {8,[D,T]}
8 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {7,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "R9",
    group = 
"""
1 *1 R!H           u1 {2,[S,D,T,B]}
2 *4 R!H           ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H           ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H           ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H           ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *9 R!H           ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *5 R!H           ux {6,[S,D,T,B]} {8,S}
8 *2 [Cd,Ct,CO,N]     u0 {7,S} {9,[D,T]}
9 *3 [Cd,Ct,Od,S2d,Cdd,N] u0 {8,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "doublebond_intra",
    group = 
"""
1 *2 Cd       u0 {2,D}
2 *3 [Cd,Cdd] u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "doublebond_intra_2H",
    group = 
"""
1 *2 Cd u0 {2,D}
2 *3 Cd u0 {1,D} {3,S} {4,S}
3    H  u0 {2,S}
4    H  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "doublebond_intra_2H_pri",
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
    index = 197,
    label = "doublebond_intra_2H_secNd",
    group = 
"""
1 *2 Cd     u0 {2,D} {3,S}
2 *3 Cd     u0 {1,D} {4,S} {5,S}
3    [Cs,O] u0 {1,S}
4    H      u0 {2,S}
5    H      u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "doublebond_intra_2H_secDe",
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
    index = 199,
    label = "doublebond_intra_HNd",
    group = 
"""
1 *2 Cd     u0 {2,D}
2 *3 Cd     u0 {1,D} {3,S} {4,S}
3    H      u0 {2,S}
4    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "doublebond_intra_HNd_pri",
    group = 
"""
1 *2 Cd     u0 {2,D} {3,S}
2 *3 Cd     u0 {1,D} {4,S} {5,S}
3    H      u0 {1,S}
4    H      u0 {2,S}
5    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "doublebond_intra_HNd_secNd",
    group = 
"""
1 *2 Cd     u0 {2,D} {3,S}
2 *3 Cd     u0 {1,D} {4,S} {5,S}
3    [Cs,O] u0 {1,S}
4    H      u0 {2,S}
5    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "doublebond_intra_HNd_secDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    H             u0 {2,S}
5    [Cs,O]        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "doublebond_intra_HDe",
    group = 
"""
1 *2 Cd            u0 {2,D}
2 *3 Cd            u0 {1,D} {3,S} {4,S}
3    H             u0 {2,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "doublebond_intra_HDe_pri",
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
    index = 205,
    label = "doublebond_intra_HCd_pri",
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
    index = 206,
    label = "doublebond_intra_HCt_pri",
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
    index = 207,
    label = "doublebond_intra_HDe_secNd",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cs,O]        u0 {1,S}
4    H             u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "doublebond_intra_HDe_secDe",
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
    index = 209,
    label = "doublebond_intra_NdNd",
    group = 
"""
1 *2 Cd     u0 {2,D}
2 *3 Cd     u0 {1,D} {3,S} {4,S}
3    [Cs,O] u0 {2,S}
4    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "doublebond_intra_NdNd_pri",
    group = 
"""
1 *2 Cd     u0 {2,D} {3,S}
2 *3 Cd     u0 {1,D} {4,S} {5,S}
3    H      u0 {1,S}
4    [Cs,O] u0 {2,S}
5    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "doublebond_intra_NdNd_secNd",
    group = 
"""
1 *2 Cd     u0 {2,D} {3,S}
2 *3 Cd     u0 {1,D} {4,S} {5,S}
3    [Cs,O] u0 {1,S}
4    [Cs,O] u0 {2,S}
5    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "doublebond_intra_NdNd_secDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cs,O]        u0 {2,S}
5    [Cs,O]        u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "doublebond_intra_NdDe",
    group = 
"""
1 *2 Cd            u0 {2,D}
2 *3 Cd            u0 {1,D} {3,S} {4,S}
3    [Cs,O]        u0 {2,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "doublebond_intra_NdDe_pri",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    H             u0 {1,S}
4    [Cs,O]        u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "doublebond_intra_NdCd_pri",
    group = 
"""
1 *2 Cd     u0 {2,D} {3,S}
2 *3 Cd     u0 {1,D} {4,S} {5,S}
3    H      u0 {1,S}
4    [Cs,O] u0 {2,S}
5    Cd     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "doublebond_intra_NdCt_pri",
    group = 
"""
1 *2 Cd     u0 {2,D} {3,S}
2 *3 Cd     u0 {1,D} {4,S} {5,S}
3    H      u0 {1,S}
4    [Cs,O] u0 {2,S}
5    Ct     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "doublebond_intra_NdDe_secNd",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cs,O]        u0 {1,S}
4    [Cs,O]        u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "doublebond_intra_NdDe_secDe",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
4    [Cs,O]        u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "doublebond_intra_DeDe",
    group = 
"""
1 *2 Cd            u0 {2,D}
2 *3 Cd            u0 {1,D} {3,S} {4,S}
3    [Cd,Ct,Cb,CO] u0 {2,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "doublebond_intra_DeDe_pri",
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
    index = 217,
    label = "doublebond_intra_DeDe_secNd",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    [Cs,O]        u0 {1,S}
4    [Cd,Ct,Cb,CO] u0 {2,S}
5    [Cd,Ct,Cb,CO] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "doublebond_intra_DeDe_secDe",
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
    index = 219,
    label = "triplebond_intra",
    group = 
"""
1 *2 Ct u0 {2,T}
2 *3 Ct u0 {1,T}
""",
    kinetics = None,
)

entry(
    index = 220,
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
    index = 221,
    label = "triplebond_intra_Nd",
    group = 
"""
1 *2 Ct     u0 {2,T}
2 *3 Ct     u0 {1,T} {3,S}
3    [Cs,O] u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 222,
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
    index = 223,
    label = "carbonylbond_intra",
    group = 
"""
1 *2 CO u0 {2,D}
2 *3 Od u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "carbonylbond_intra_H",
    group = 
"""
1 *2 CO u0 {2,D} {3,S}
2 *3 Od u0 {1,D}
3    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "carbonylbond_intra_Nd",
    group = 
"""
1 *2 CO     u0 {2,D} {3,S}
2 *3 Od     u0 {1,D}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "carbonylbond_intra_De",
    group = 
"""
1 *2 CO            u0 {2,D} {3,S}
2 *3 Od            u0 {1,D}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "radadd_intra_cs",
    group = 
"""
1 *1 Cs u1
""",
    kinetics = None,
)

entry(
    index = 228,
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
    index = 229,
    label = "radadd_intra_csHNd",
    group = 
"""
1 *1 Cs     u1 {2,S} {3,S}
2    H      u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 230,
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
    index = 235,
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
    index = 236,
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
    index = 237,
    label = "radadd_intra_csNdNd",
    group = 
"""
1 *1 Cs     u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 232,
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
    index = 239,
    label = "radadd_intra_csNdCd",
    group = 
"""
1 *1 Cs     u1 {2,S} {3,S}
2    [Cs,O] u0 {1,S}
3    Cd     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "radadd_intra_csNdCt",
    group = 
"""
1 *1 Cs     u1 {2,S} {3,S}
2    [Cs,O] u0 {1,S}
3    Ct     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 241,
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
    index = 234,
    label = "radadd_intra_O",
    group = 
"""
1 *1 O u1
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "radadd_intra_Cb",
    group = 
"""
1 *1 Cb u1
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "radadd_intra_cdsingle",
    group = 
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "radadd_intra_cdsingleH",
    group = 
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 238,
    label = "radadd_intra_cdsingleNd",
    group = 
"""
1 *1 Cd     u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "radadd_intra_cdsingleDe",
    group = 
"""
1 *1 Cd            u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "radadd_intra_cddouble",
    group = 
"""
1 *1 Cd u1 {2,D}
2    Cd u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "radadd_intra_CO",
    group = 
"""
1 *1 CO u1 {2,D}
2    O  u0 {1,D}
""",
    kinetics = None,
)

entry(
    index = 242,
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
    L2: R4
        L3: R4_S
            L4: R4_S_D
            L4: R4_S_T
            L4: R4_S_CO
        L3: R4_D
            L4: R4_D_D
            L4: R4_D_T
            L4: R4_D_CO
        L3: R4_T
            L4: R4_T_D
            L4: R4_T_T
            L4: R4_T_CO
    L2: R5
        L3: R5_SS
            L4: R5_SS_D
            L4: R5_SS_T
            L4: R5_SS_CO
        L3: R5_SM
            L4: R5_SD
                L5: R5_SD_D
                L5: R5_SD_T
                L5: R5_SD_CO
            L4: R5_ST
                L5: R5_ST_D
                L5: R5_ST_T
                L5: R5_ST_CO
        L3: R5_MS
            L4: R5_DS
                L5: R5_DS_D
                L5: R5_DS_T
                L5: R5_DS_CO
            L4: R5_TS
                L5: R5_TS_D
                L5: R5_TS_T
                L5: R5_TS_CO
        L3: R5_MM
    L2: R6
        L3: R6_RSR
            L4: R6_SSR
                L5: R6_SSS
                    L6: R6_SSS_D
                    L6: R6_SSS_T
                    L6: R6_SSS_CO
                L5: R6_SSM
                    L6: R6_SSM_D
                    L6: R6_SSM_T
                    L6: R6_SSM_CO
            L4: R6_MSR
                L5: R6_DSR
                    L6: R6_DSS
                        L7: R6_DSS_D
                        L7: R6_DSS_T
                        L7: R6_DSS_CO
                    L6: R6_DSM
                        L7: R6_DSM_D
                        L7: R6_DSM_T
                        L7: R6_DSM_CO
                L5: R6_TSR
                    L6: R6_TSS
                        L7: R6_TSS_D
                        L7: R6_TSS_T
                        L7: R6_TSS_CO
                    L6: R6_TSM
                        L7: R6_TSM_D
                        L7: R6_TSM_T
                        L7: R6_TSM_CO
        L3: R6_SMS
            L4: R6_SMS_D
            L4: R6_SMS_T
            L4: R6_SMS_CO
        L3: R6_SMM
    L2: R7plus
        L3: R7
            L4: R7_RSSR
                L5: R7_SSSR
                    L6: R7_SSSS
                        L7: R7_SSSS_D
                        L7: R7_SSSS_T
                        L7: R7_SSSS_CO
                    L6: R7_SSSM
                        L7: R7_SSSM_D
                        L7: R7_SSSM_T
                        L7: R7_SSSM_CO
                L5: R7_MSSR
                    L6: R7_DSSR
                        L7: R7_DSSS
                            L8: R7_DSSS_D
                            L8: R7_DSSS_T
                            L8: R7_DSSS_CO
                        L7: R7_DSSM
                            L8: R7_DSSM_D
                            L8: R7_DSSM_T
                            L8: R7_DSSM_CO
                    L6: R7_TSSR
                        L7: R7_TSSS
                            L8: R7_TSSS_D
                            L8: R7_TSSS_T
                            L8: R7_TSSS_CO
                        L7: R7_TSSM
                            L8: R7_TSSM_D
                            L8: R7_TSSM_T
                            L8: R7_TSSM_CO
            L4: R7_RSMS
                L5: R7_SSMS
                    L6: R7_SSMS_D
                    L6: R7_SSMS_T
                    L6: R7_SSMS_CO
                L5: R7_MSMS
                    L6: R7_DSMS
                        L7: R7_DSMS_D
                        L7: R7_DSMS_T
                        L7: R7_DSMS_CO
                    L6: R7_TSMS
                        L7: R7_TSMS_D
                        L7: R7_TSMS_T
                        L7: R7_TSMS_CO
            L4: R7_SMSR
                L5: R7_SMSS
                    L6: R7_SMSS_D
                    L6: R7_SMSS_T
                    L6: R7_SMSS_CO
                L5: R7_SMSM
                    L6: R7_SMSM_D
                    L6: R7_SMSM_T
                    L6: R7_SMSM_CO
            L4: R7_MMSR
            L4: R7_RSMM
            L4: R7_SMMS
        L3: R8
        L3: R9
L1: multiplebond_intra
    L2: doublebond_intra
        L3: doublebond_intra_2H
            L4: doublebond_intra_2H_pri
            L4: doublebond_intra_2H_secNd
            L4: doublebond_intra_2H_secDe
        L3: doublebond_intra_HNd
            L4: doublebond_intra_HNd_pri
            L4: doublebond_intra_HNd_secNd
            L4: doublebond_intra_HNd_secDe
        L3: doublebond_intra_HDe
            L4: doublebond_intra_HDe_pri
                L5: doublebond_intra_HCd_pri
                L5: doublebond_intra_HCt_pri
            L4: doublebond_intra_HDe_secNd
            L4: doublebond_intra_HDe_secDe
        L3: doublebond_intra_NdNd
            L4: doublebond_intra_NdNd_pri
            L4: doublebond_intra_NdNd_secNd
            L4: doublebond_intra_NdNd_secDe
        L3: doublebond_intra_NdDe
            L4: doublebond_intra_NdDe_pri
                L5: doublebond_intra_NdCd_pri
                L5: doublebond_intra_NdCt_pri
            L4: doublebond_intra_NdDe_secNd
            L4: doublebond_intra_NdDe_secDe
        L3: doublebond_intra_DeDe
            L4: doublebond_intra_DeDe_pri
            L4: doublebond_intra_DeDe_secNd
            L4: doublebond_intra_DeDe_secDe
    L2: triplebond_intra
        L3: triplebond_intra_H
        L3: triplebond_intra_Nd
        L3: triplebond_intra_De
    L2: carbonylbond_intra
        L3: carbonylbond_intra_H
        L3: carbonylbond_intra_Nd
        L3: carbonylbond_intra_De
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
    label = "bond21",
    group = 
"""
1 *2 R!H u0 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "cdd2",
    group = 
"""
1 *2 Cdd u0
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

