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

entry(
    index = 1,
    label = "Rn",
    group = "OR{Rnx_cyclics, R4, R5, R6, R7plus}",
    kinetics = None,
)

entry(
    index = 2,
    label = "multiplebond_intra",
    group = 
"""
1 *2 [Cd,Ct,CO,N]     u0 {2,[D,T]}
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
    label = "R4",
    group = 
"""
1 *1 R!H              u1 {2,[S,D,T,B]}
2 *4 R!H              ux {1,[S,D,T,B]} {3,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]}
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
4 *3 [Cd,Ct,Od,Sd,Cdd] u0 {3,[D,T]}
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
4 *3 [Cd,Ct,Od,Sd,Cdd] u0 {3,[D,T]}
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
4 *3 [Cd,Ct,Od,Sd,Cdd] u0 {3,[D,T]}
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
4 *2 [Cd,Ct,CO,N,CS]        u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
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
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
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
4 *2 [Cd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
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
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
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
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
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
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
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
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
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
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
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
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
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
6 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {5,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "R7plus",
    group = "OR{R7, R8, R9, R10, R11}",
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
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
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
7 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {6,[D,T]}
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
8 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {7,[D,T]}
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
9 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {8,[D,T]}
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
    index = 342,
    label = "doublebond_intra_HDe_secDe_benzene",
    group = 
"""
1 *2 Cd            u0 {2,D} {3,S}
2 *3 Cd            u0 {1,D} {4,S} {5,S}
3    Cd            u0 {1,S} {6,D}
4    H             u0 {2,S}
5    Cd            u0 {2,S} {7,D}
6    Cd            u0 {3,D} {7,S}
7    Cd            u0 {6,S} {5,D}
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
    index = 378,
    label = "doublebond_intra_DeDe_pri_cyc6",
    group = 
"""
1 *2 Cd  u0 {2,D} {3,S}
2 *3 Cd  u0 {1,D} {4,S} {5,S}
3    H   u0 {1,S}
4    Cd  u0 {2,S} {6,D}
5    Cd  u0 {2,S} {8,S} {9,D}
6    Cd  u0 {4,D} {7,S}
7    Cd  u0 {6,S} {8,D}
8    Cd  u0 {7,D} {5,S}
9    Cd  u0 {5,D}
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
    index = 344,
    label = "radadd_intra_csHCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
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
    index = 342,
    label = "radadd_intra_cdsingleDe_cb",
    group = 
"""
1 *1 Cd            u1 {2,S}
2    Cb		   u0 {1,S}
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

entry(
    index = 251,
    label = "R10",
    group =
"""
1 *1 R!H           u1 {2,[S,D,T,B]}
2 *4 R!H           ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H           ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H           ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H           ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *9 R!H           ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *10 R!H          ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *5 R!H           ux {7,[S,D,T,B]} {9,S}
9 *2 [Cd,Ct,CO,N]     u0 {8,S} {10,[D,T]}
10 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {9,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "R11",
    group = 
"""
1 *1 R!H           u1 {2,[S,D,T,B]}
2 *4 R!H           ux {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H           ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H           ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H           ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *9 R!H           ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *10 R!H          ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *11 R!H          ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *5 R!H           ux {8,[S,D,T,B]} {10,S}
10 *2 [Cd,Ct,CO,N]     u0 {9,S} {11,[D,T]}
11 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {10,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "Rnx_cyclics",
    group = "OR{Rnxc3, Rnxc4, Rnxc5, Rnxc6, Rnxc7, Rnxc8}",
    kinetics = None,
)

entry(
    index = 290,
    label = "Rnxc3",
    group = "OR{Rn4c3_alpha, Rn3c3_alpha, Rn2c3_alpha, Rn1c3_alpha}",
    kinetics = None,
)

entry(
    index = 254,
    label = "Rn4c3_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {3,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {1,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "Rn3c3_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {3,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {1,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "Rn2c3_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {3,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *5 R!H ux {2,[S,D,T,B]} {1,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "Rn1c3_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {3,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {1,[S,D,T,B]} {4,[S,D,T,B]}
4 *1 R!H u1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "Rnxc4",
    group = "OR{Rnxc4_alpha, Rnxc4_beta}",
    kinetics = None,
)

entry(
    index = 259,
    label = "Rnxc4_alpha",
    group = "OR{Rn4c4_alpha, Rn3c4_alpha, Rn2c4_alpha, Rn1c4_alpha}",
    kinetics = None,
)

entry(
    index = 260,
    label = "Rn4c4_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H ux {3,[S,D,T,B]} {1,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "Rn3c4_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H ux {3,[S,D,T,B]} {1,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "Rn2c4_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H ux {3,[S,D,T,B]} {1,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "Rn1c4_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {1,[S,D,T,B]} {5,[S,D,T,B]}
5 *1 R!H u1 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "Rnxc4_beta",
    group = "OR{Rn3c4_beta, Rn2c4_beta, Rn1c4_beta}",
    kinetics = None,
)

entry(
    index = 265,
    label = "Rn3c4_beta",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *7 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
4 *5 R!H ux {3,[S,D,T,B]} {1,[S,D,T,B]}
5 *6 R!H ux {3,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "Rn2c4_beta",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *6 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
4 *5 R!H ux {3,[S,D,T,B]} {1,[S,D,T,B]}
5 *4 R!H ux {3,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "Rn1c4_beta",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {4,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {5,[S,D,T,B]}
4 *5 R!H ux {3,[S,D,T,B]} {1,[S,D,T,B]}
5 *1 R!H u1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "Rnxc5",
    group = "OR{Rnxc5_alpha, Rnxc5_beta_long, Rnxc5_beta_short}",
    kinetics = None,
)

entry(
    index = 269,
    label = "Rnxc5_alpha",
    group = "OR{Rn4c5_alpha, Rn3c5_alpha, Rn2c5_alpha, Rn1c5_alpha}",
    kinetics = None,
)

entry(
    index = 270,
    label = "Rn4c5_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *7 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "Rn3c5_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "Rn2c5_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "Rn1c5_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 377,
    label = "Rn1c5_alpha_benzene",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,S}
3    Cb  u0 {2,S} {4,B}
4    Cb  u0 {3,B} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]} {6,[S,D,T,B]}
6 *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "Rnxc5_beta_long",
    group = "OR{Rn3c5_beta_long, Rn2c5_beta_long, Rn1c5_beta_long}",
    kinetics = None,
)

entry(
    index = 275,
    label = "Rn3c5_beta_long",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *7 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *8 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *6 R!H ux {3,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "Rn2c5_beta_long",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *6 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *4 R!H ux {3,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "Rn1c5_beta_long",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {6,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *1 R!H u1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 278,
    label = "Rnxc5_beta_short",
    group = "OR{Rn3c5_beta_short, Rn2c5_beta_short, Rn1c5_beta_short}",
    kinetics = None,
)

entry(
    index = 279,
    label = "Rn3c5_beta_short",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *6 R!H ux {4,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "Rn2c5_beta_short",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *4 R!H ux {4,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "Rn1c5_beta_short",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {6,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *1 R!H u1 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "Rnxc6",
    group = "OR{Rnxc6_alpha, Rnxc6_beta_long, Rnxc6_beta_short, Rnxc6_gamma}",
    kinetics = None,
)

entry(
    index = 283,
    label = "Rnxc6_alpha",
    group = "OR{Rn4c6_alpha, Rn3c6_alpha, Rn2c6_alpha, Rn1c6_alpha}",
    kinetics = None,
)

entry(
    index = 284,
    label = "Rn4c6_alpha",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]}
7  *7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "Rn4c6_alpha_benzene",
    group = 
"""
1  *2 C u0 {2,D} {6,S}
2  *3 C u0 {1,D} {3,S}
3     C u0 {2,S} {4,D}
4     C u0 {3,D} {5,S}
5     C u0 {4,S} {6,D}
6  *5 C u0 {5,D} {1,S} {7,[S,D,T,B]}
7  *7 C u0 {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6 C u0 {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 C u0 {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 C u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "Rn4c6_alpha_benzene_Cdchain",
    group = 
"""
1  *2 C u0 {2,D} {6,S}
2  *3 C u0 {1,D} {3,S}
3     C u0 {2,S} {4,D}
4     C u0 {3,D} {5,S}
5     C u0 {4,S} {6,D}
6  *5 C u0 {5,D} {1,S} {7,S}
7  *7 C u0 {6,S} {8,D}
8  *6 C u0 {7,D} {9,S}
9  *4 C u0 {8,S} {10,D}
10 *1 C u1 {9,D}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "Rn3c6_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]}
7 *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)
entry(
    index = 286,
    label = "Rn2c6_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "Rn1c6_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *4 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]}
7 *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "Rnxc6_beta_long",
    group = "OR{Rn3c6_beta_long, Rn2c6_beta_long, Rn1c6_beta_long}",
    kinetics = None,
)

entry(
    index = 289,
    label = "Rn3c6_beta_long",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *7 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *8 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *9 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *6 R!H ux {3,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "Rn2c6_beta_long",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *6 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *4 R!H ux {3,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "Rn1c6_beta_long",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {7,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *1 R!H u1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "Rnxc6_beta_short",
    group = "OR{Rn3c6_beta_short, Rn2c6_beta_short, Rn1c6_beta_short}",
    kinetics = None,
)

entry(
    index = 294,
    label = "Rn3c6_beta_short",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *6 R!H ux {5,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "Rn2c6_beta_short",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *4 R!H ux {5,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "Rn1c6_beta_short",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "Rnxc6_gamma",
    group = "OR{Rn2c6_gamma, Rn1c6_gamma}",
    kinetics = None,
)

entry(
    index = 298,
    label = "Rn2c6_gamma",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
5 *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *4 R!H ux {4,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "Rn1c6_gamma",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {7,[S,D,T,B]}
5 *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]}
7 *1 R!H u1 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "Rnxc7",
    group = "OR{Rnxc7_alpha, Rnxc7_beta_long, Rnxc7_beta_short, Rnxc7_gamma_long, Rnxc7_gamma_short}",
    kinetics = None,
)

entry(
    index = 301,
    label = "Rnxc7_alpha",
    group = "OR{Rn4c7_alpha, Rn3c7_alpha, Rn2c7_alpha, Rn1c7_alpha}",
    kinetics = None,
)

entry(
    index = 302,
    label = "Rn4c7_alpha",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]} {8,[S,D,T,B]}
8  *7 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *6 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4 R!H ux {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1 R!H u1 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "Rn3c7_alpha",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]} {8,[S,D,T,B]}
8  *6 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "Rn2c7_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "Rn1c7_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *4 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]} {8,[S,D,T,B]}
8 *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "Rnxc7_beta_long",
    group = "OR{Rn3c7_beta_long, Rn2c7_beta_long, Rn1c7_beta_long}",
    kinetics = None,
)

entry(
    index = 307,
    label = "Rn3c7_beta_long",
    group = 
"""
1  *2  R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3  R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3  *7  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4  *8  R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *10 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5  R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *6  R!H ux {3,[S,D,T,B]} {9,[S,D,T,B]}
9  *4  R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "Rn2c7_beta_long",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3  *6 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4  *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *4 R!H ux {3,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "Rn1c7_beta_long",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3  *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {8,[S,D,T,B]}
4  *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *1 R!H u1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "Rnxc7_beta_short",
    group = "OR{Rn3c7_beta_short, Rn2c7_beta_short, Rn1c7_beta_short}",
    kinetics = None,
)

entry(
    index = 311,
    label = "Rn3c7_beta_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *6 R!H ux {6,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "Rn2c7_beta_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *4 R!H ux {6,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "Rn1c7_beta_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "Rnxc7_gamma_long",
    group = "OR{Rn2c7_gamma_long, Rn1c7_gamma_long}",
    kinetics = None,
)

entry(
    index = 315,
    label = "Rn2c7_gamma_long",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {8,[S,D,T,B]}
5  *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *4 R!H ux {4,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "Rn1c7_gamma_long",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {8,[S,D,T,B]}
5  *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *1 R!H u1 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "Rnxc7_gamma_short",
    group = "OR{Rn2c7_gamma_short, Rn1c7_gamma_short}",
    kinetics = None,
)

entry(
    index = 318,
    label = "Rn2c7_gamma_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
6  *7 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *4 R!H ux {5,[S,D,T,B]} {9,[S,D,T,B]}
9  *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "Rn1c7_gamma_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {7,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]} {8,[S,D,T,B]}
6  *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *5 R!H ux {6,[S,D,T,B]} {1,[S,D,T,B]}
8  *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "Rn4c8_alpha",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]} {9,[S,D,T,B]}
9  *7 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *6 R!H ux {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *4 R!H ux {10,[S,D,T,B]} {12,[S,D,T,B]}
12 *1 R!H u1 {11,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "Rnxc8",
    group = "OR{Rnxc8_alpha, Rnxc8_beta_long, Rnxc8_beta_short, Rnxc8_gamma_long, Rnxc8_gamma_short, Rnxc8_epsilon}",
    kinetics = None,
)

entry(
    index = 322,
    label = "Rnxc8_alpha",
    group = "OR{Rn4c8_alpha, Rn3c8_alpha, Rn2c8_alpha, Rn1c8_alpha}",
    kinetics = None,
)

entry(
    index = 323,
    label = "Rn3c8_alpha",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]} {9,[S,D,T,B]}
9  *6 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *4 R!H ux {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1 R!H u1 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "Rn2c8_alpha",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7     R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "Rn1c8_alpha",
    group = 
"""
1 *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5    R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "Rnxc8_beta_long",
    group = "OR{Rn3c8_beta_long, Rn2c8_beta_long, Rn1c8_beta_long}",
    kinetics = None,
)

entry(
    index = 327,
    label = "Rn3c8_beta_long",
    group = 
"""
1  *2  R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3  R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3  *7  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4  *8  R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *9  R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *10 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *11 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5  R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *6  R!H ux {3,[S,D,T,B]} {10,[S,D,T,B]}
10 *4  R!H ux {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1  R!H u1 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "Rn2c8_beta_long",
    group = 
"""
1  *2  R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3  R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3  *6  R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4  *7  R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *8  R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *9  R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *10 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5  R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *4  R!H ux {3,[S,D,T,B]} {10,[S,D,T,B]}
10 *1  R!H u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "Rn1c8_beta_long",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3  *4 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {9,[S,D,T,B]}
4  *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *9 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "Rnxc8_beta_short",
    group = "OR{Rn3c8_beta_short, Rn2c8_beta_short, Rn1c8_beta_short}",
    kinetics = None,
)

entry(
    index = 331,
    label = "Rn3c8_beta_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]} {9,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *6 R!H ux {7,[S,D,T,B]} {10,[S,D,T,B]}
10 *4 R!H ux {9,[S,D,T,B]} {11,[S,D,T,B]}
11 *1 R!H u1 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "Rn2c8_beta_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]} {9,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *4 R!H ux {7,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "Rn1c8_beta_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6     R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *4 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]} {9,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "Rnxc8_gamma_long",
    group = "OR{Rn2c8_gamma_long, Rn1c8_gamma_long}",
    kinetics = None,
)

entry(
    index = 335,
    label = "Rn2c8_gamma_long",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5  *7 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *8 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *9 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *4 R!H ux {4,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)
entry(
    index = 336,
    label = "Rn1c8_gamma_long",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4  *4 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {9,[S,D,T,B]}
5  *6 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *7 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *8 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "Rnxc8_gamma_short",
    group = "OR{Rn2c8_gamma_short, Rn1c8_gamma_short}",
    kinetics = None,
)

entry(
    index = 338,
    label = "Rn2c8_gamma_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
7  *7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *4 R!H ux {6,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "Rn1c8_gamma_short",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *4 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]} {9,[S,D,T,B]}
7  *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "Rnxc8_epsilon",
    group = "OR{Rn1c8_epsilon}",
    kinetics = None,
)

entry(
    index = 341,
    label = "Rn1c8_epsilon",
    group = 
"""
1  *2 R!H u0 {2,[D,T]} {8,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5  *4 R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]} {9,[S,D,T,B]}
6  *6 R!H ux {5,[S,D,T,B]} {7,[S,D,T,B]}
7  *7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *5 R!H ux {7,[S,D,T,B]} {1,[S,D,T,B]}
9  *1 R!H u1 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "Rn3c6b_alpha",
    group = 
"""
1 *2 C u0 {2,D} {6,S}
2 *3 C u0 {1,D} {3,S}
3    C ux {2,S} {4,D}
4    C ux {3,D} {5,S}
5    C ux {4,S} {6,D}
6 *5 C ux {5,D} {1,S} {7,[S,D,T,B]}
7 *6 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8 *4 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "Rn3(RSS)c6b_alpha",
    group = 
"""
1 *2 C u0 {2,D} {6,S}
2 *3 C u0 {1,D} {3,S}
3    C ux {2,S} {4,D}
4    C ux {3,D} {5,S}
5    C ux {4,S} {6,D}
6 *5 C ux {5,D} {1,S} {7,S}
7 *6 R!H ux {6,S} {8,S}
8 *4 R!H ux {7,S} {9,[S,D,T,B]}
9 *1 R!H u1 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "R4_intra_6_member_ring",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {6,[S,D,T]}
2 *4 R!H              ux {1,[S,D,T]} {3,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {5,[S,D,T]}
5    R!H              ux {4,[S,D,T]} {6,[S,D,T,B]}
6    R!H              ux {5,[S,D,T,B]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "R4_intra_6_member_ring_S",
    group =
"""
1 *1 R!H              u1 {2,S} {6,[S,D,T]}
2 *4 R!H              ux {1,S} {3,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {5,[S,D,T]}
5    R!H              ux {4,[S,D,T]} {6,[S,D,T,B]}
6    R!H              ux {5,[S,D,T,B]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "R4_intra_6_member_ring_S_D",
    group =
"""
1 *1 R!H              u1 {2,S} {6,[S,D,T]}
2 *4 R!H              ux {1,S} {3,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {5,[S,D,T]}
5    R!H              ux {4,[S,D,T]} {6,[S,D,T,B]}
6    R!H              ux {5,[S,D,T,B]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "R4_intra_6_member_ring_S_D_2H",
    group =
"""
1 *1 R!H              u1 {2,S} {6,[S,D,T]}
2 *4 R!H              u0 {1,S} {3,S} {7,S} {8,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {5,[S,D,T]}
5    R!H              ux {4,[S,D,T]} {6,[S,D,T,B]}
6    R!H              ux {5,[S,D,T,B]} {1,[S,D,T]}
7    H                u0 {2,S}
8    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 379,
    label = "2-hydro-nathphalene",
    group =
"""
1 *1 C                u1 {2,S} {6,S}
2 *4 C                u0 {1,S} {3,S} {7,S} {8,S}
3 *2 Cd		      u0 {2,S} {4,D}
4 *3 Cd               u0 {3,D} {5,S}
5    Cb               u0 {4,S} {6,B}
6    Cb               u0 {5,B} {1,S}
7    H                u0 {2,S}
8    H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "R4_intra_6_member_ring_S_D_2R!H",
    group =
"""
1 *1 R!H              u1 {2,S} {6,[S,D,T]}
2 *4 R!H              u0 {1,S} {3,S} {7,S} {8,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {5,[S,D,T]}
5    R!H              ux {4,[S,D,T]} {6,[S,D,T,B]}
6    R!H              ux {5,[S,D,T,B]} {1,[S,D,T]}
7    R!H                u0 {2,S}
8    R!H                u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "R4_intra_6_member_ring_S_D_H_R!H",
    group =
"""
1 *1 R!H              u1 {2,S} {6,[S,D,T]}
2 *4 R!H              u0 {1,S} {3,S} {7,S} {8,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {5,[S,D,T]}
5    R!H              ux {4,[S,D,T]} {6,[S,D,T,B]}
6    R!H              ux {5,[S,D,T,B]} {1,[S,D,T]}
7    H                u0 {2,S}
8    R!H              u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "R5_intra_7_member_ring",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {7,[S,D,T]}
2 *4 R!H              ux {1,[S,D,T]} {5,[S,D,T]}
3 *2 [Cd,Ct,CO,N]     u0 {5,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {6,[S,D,T]}
5 *5 R!H              ux {2,[S,D,T]} {3,S}
6    R!H              ux {4,[S,D,T]} {7,[S,D,T]}
7    R!H              ux {6,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "R5_intra_7_member_ring_SS",
    group =
"""
1 *1 R!H              u1 {2,S} {7,[S,D,T]}
2 *4 R!H              ux {1,S} {5,S}
3 *2 [Cd,Ct,CO,N]     u0 {5,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {6,[S,D,T]}
5 *5 R!H              ux {2,S} {3,S}
6    R!H              ux {4,[S,D,T]} {7,[S,D,T]}
7    R!H              ux {6,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "R5_intra_7_member_ring_SS_D",
    group =
"""
1 *1 R!H              u1 {2,S} {7,[S,D,T]}
2 *4 R!H              ux {1,S} {5,S}
3 *2 [Cd,Ct,CO,N]     u0 {5,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {6,[S,D,T]}
5 *5 R!H              ux {2,S} {3,S}
6    R!H              ux {4,[S,D,T]} {7,[S,D,T]}
7    R!H              ux {6,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "R6_intra_10_member_ring",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {10,[S,D,T]}
2 *4 R!H              ux {1,[S,D,T]} {5,[S,D,T]}
3 *2 [Cd,Ct,CO,N]     u0 {6,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {7,[S,D,T]}
5 *6 R!H              ux {2,[S,D,T]} {6,[S,D,T]}
6 *5 R!H              ux {5,[S,D,T]} {3,S}
7    R!H              ux {4,[S,D,T]} {8,[S,D,T]}
8    R!H              ux {7,[S,D,T]} {9,[S,D,T]}
9    R!H              ux {8,[S,D,T]} {10,[S,D,T]}
10   R!H              ux {9,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "R6_intra_10_member_ring_SSD",
    group =
"""
1 *1 R!H              u1 {2,S} {10,[S,D,T]}
2 *4 R!H              ux {1,S} {5,S}
3 *2 [Cd,Ct,CO,N]     u0 {6,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {7,[S,D,T]}
5 *6 R!H              ux {2,S} {6,D}
6 *5 R!H              ux {5,D} {3,S}
7    R!H              ux {4,[S,D,T]} {8,[S,D,T]}
8    R!H              ux {7,[S,D,T]} {9,[S,D,T]}
9    R!H              ux {8,[S,D,T]} {10,[S,D,T]}
10   R!H              ux {9,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "R6_intra_10_member_ring_SSD_D",
    group =
"""
1 *1 R!H              u1 {2,S} {10,[S,D,T]}
2 *4 R!H              ux {1,S} {5,S}
3 *2 [Cd,Ct,CO,N]     u0 {6,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {7,[S,D,T]}
5 *6 R!H              ux {2,S} {6,D}
6 *5 R!H              ux {5,D} {3,S}
7    R!H              ux {4,[S,D,T]} {8,[S,D,T]}
8    R!H              ux {7,[S,D,T]} {9,[S,D,T]}
9    R!H              ux {8,[S,D,T]} {10,[S,D,T]}
10   R!H              ux {9,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "R7_intra_10_member_ring",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {10,[S,D,T]}
2 *4 R!H              ux {1,[S,D,T]} {5,[S,D,T]}
3 *2 [Cd,Ct,CO,N]     u0 {7,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {8,[S,D,T]}
5 *6 R!H              ux {2,[S,D,T]} {6,[S,D,T]}
6 *7 R!H              ux {5,[S,D,T]} {7,[S,D,T]}
7 *5 R!H              ux {6,[S,D,T]} {3,S}
8    R!H              ux {4,[S,D,T]} {9,[S,D,T]}
9    R!H              ux {8,[S,D,T]} {10,[S,D,T]}
10   R!H              ux {9,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 356,
    label = "R7_intra_10_member_ring_SDSD",
    group =
"""
1 *1 R!H              u1 {2,S} {10,[S,D,T]}
2 *4 R!H              ux {1,S} {5,D}
3 *2 [Cd,Ct,CO,N]     u0 {7,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {8,[S,D,T]}
5 *6 R!H              ux {2,D} {6,S}
6 *7 R!H              ux {5,S} {7,D}
7 *5 R!H              ux {6,D} {3,S}
8    R!H              ux {4,[S,D,T]} {9,[S,D,T]}
9    R!H              ux {8,[S,D,T]} {10,[S,D,T]}
10   R!H              ux {9,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 357,
    label = "R7_intra_10_member_ring_SDSD_D",
    group =
"""
1 *1 R!H              u1 {2,S} {10,[S,D,T]}
2 *4 R!H              ux {1,S} {5,D}
3 *2 [Cd,Ct,CO,N]     u0 {7,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {8,[S,D,T]}
5 *6 R!H              ux {2,D} {6,S}
6 *7 R!H              ux {5,S} {7,D}
7 *5 R!H              ux {6,D} {3,S}
8    R!H              ux {4,[S,D,T]} {9,[S,D,T]}
9    R!H              ux {8,[S,D,T]} {10,[S,D,T]}
10   R!H              ux {9,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 358,
    label = "Rn4(SDSD)c6_alpha",
    group =
"""
1  *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]} {7,D}
7  *7 R!H ux {6,D} {8,S}
8  *6 R!H ux {7,S} {9,D}
9  *4 R!H ux {8,D} {10,S}
10 *1 R!H u1 {9,S}
""",
    kinetics = None,
)

entry(
    index = 359,
    label = "R8_SDSDS",
    group =
"""
1 *1 R!H           u1 {2,S}
2 *4 R!H           ux {1,S} {3,D}
3 *6 R!H           ux {2,D} {4,S}
4 *7 R!H           ux {3,S} {5,D}
5 *8 R!H           ux {4,D} {6,S}
6 *5 R!H           ux {5,S} {7,S}
7 *2 [Cd,Ct,CO,N]   u0 {6,S} {8,[D,T]}
8 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {7,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 360,
    label = "R8_intra_10_member_ring",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {10,[S,D,T]}
2 *4 R!H              ux {1,[S,D,T]} {5,[S,D,T]}
3 *2 [Cd,Ct,CO,N]     u0 {8,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {9,[S,D,T]}
5 *6 R!H              ux {2,[S,D,T]} {6,[S,D,T]}
6 *7 R!H              ux {5,[S,D,T]} {7,[S,D,T]}
7 *8 R!H              ux {6,[S,D,T]} {8,[S,D,T]}
8 *5 R!H              ux {7,[S,D,T]} {3,S}
9    R!H              ux {4,[S,D,T]} {10,[S,D,T]}
10   R!H              ux {9,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 361,
    label = "R8_intra_10_member_ring_SSDSD",
    group =
"""
1 *1 R!H              u1 {2,S} {10,[S,D,T]}
2 *4 R!H              ux {1,S} {5,S}
3 *2 [Cd,Ct,CO,N]     u0 {8,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {9,[S,D,T]}
5 *6 R!H              ux {2,S} {6,D}
6 *7 R!H              ux {5,D} {7,S}
7 *8 R!H              ux {6,S} {8,D}
8 *5 R!H              ux {7,D} {3,S}
9    R!H              ux {4,[S,D,T]} {10,[S,D,T]}
10   R!H              ux {9,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 362,
    label = "R8_intra_10_member_ring_SSDSD_D",
    group =
"""
1 *1 R!H              u1 {2,S} {10,[S,D,T]}
2 *4 R!H              ux {1,S} {5,S}
3 *2 [Cd,Ct,CO,N]     u0 {8,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {9,[S,D,T]}
5 *6 R!H              ux {2,S} {6,D}
6 *7 R!H              ux {5,D} {7,S}
7 *8 R!H              ux {6,S} {8,D}
8 *5 R!H              ux {7,D} {3,S}
9    R!H              ux {4,[S,D,T]} {10,[S,D,T]}
10   R!H              ux {9,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 363,
    label = "R4_intra_7_member_ring",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {7,[S,D,T]}
2 *4 R!H              ux {1,[S,D,T]} {3,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {5,[S,D,T]}
5    R!H              ux {4,[S,D,T]} {6,[S,D,T]}
6    R!H              ux {5,[S,D,T]} {7,[S,D,T]}
7    R!H              ux {6,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 364,
    label = "R4_intra_7_member_ring_S",
    group =
"""
1 *1 R!H              u1 {2,S} {7,[S,D,T]}
2 *4 R!H              ux {1,S} {3,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {5,[S,D,T]}
5    R!H              ux {4,[S,D,T]} {6,[S,D,T]}
6    R!H              ux {5,[S,D,T]} {7,[S,D,T]}
7    R!H              ux {6,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 365,
    label = "R4_intra_7_member_ring_S_D",
    group =
"""
1 *1 R!H              u1 {2,S} {7,[S,D,T]}
2 *4 R!H              ux {1,S} {3,S}
3 *2 [Cd,Ct,CO,N]     u0 {2,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {5,[S,D,T]}
5    R!H              ux {4,[S,D,T]} {6,[S,D,T]}
6    R!H              ux {5,[S,D,T]} {7,[S,D,T]}
7    R!H              ux {6,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 366,
    label = "Rn3(SDS)c6b_alpha",
    group =
"""
1 *2 C u0 {2,D} {6,S}
2 *3 C u0 {1,D} {3,S}
3    C ux {2,S} {4,D}
4    C ux {3,D} {5,S}
5    C ux {4,S} {6,D}
6 *5 C ux {5,D} {1,S} {7,S}
7 *6 R!H ux {6,S} {8,D}
8 *4 R!H ux {7,D} {9,S}
9 *1 R!H u1 {8,S}
""",
    kinetics = None,
)

entry(
    index = 367,
    label = "Rn4(looped)c6_alpha",
    group =
"""
1  *2 R!H u0 {2,[D,T]} {6,[S,D,T,B]}
2  *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3     R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4     R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5     R!H ux {4,[S,D,T,B]} {6,[S,D,T,B]}
6  *5 R!H ux {5,[S,D,T,B]} {1,[S,D,T,B]} {7,[S,D,T,B]} {10,[S,D,T,B]}
7  *7 R!H ux {6,[S,D,T,B]} {8,[S,D,T,B]}
8  *6 R!H ux {7,[S,D,T,B]} {9,[S,D,T,B]}
9  *4 R!H ux {8,[S,D,T,B]} {10,[S,D,T,B]}
10 *1 R!H u1 {9,[S,D,T,B]} {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 368,
    label = "Rn2(SS)c5_alpha",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]} {6,S}
6 *4 R!H ux {5,S} {7,S}
7 *1 R!H u1 {6,S}
""",
    kinetics = None,
)

entry(
    index = 369,
    label = "R6_intra_7_member_ring",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {7,[S,D,T]}
2 *4 R!H              ux {1,[S,D,T]} {5,[S,D,T]}
3 *2 [Cd,Ct,CO,N]     u0 {6,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {7,[S,D,T]}
5 *6 R!H              ux {2,[S,D,T]} {6,[S,D,T]}
6 *5 R!H              ux {5,[S,D,T]} {3,S}
7    R!H              ux {4,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 370,
    label = "R6_intra_7_member_ring_SSD",
    group =
"""
1 *1 R!H              u1 {2,S} {7,[S,D,T]}
2 *4 R!H              ux {1,S} {5,S}
3 *2 [Cd,Ct,CO,N]     u0 {6,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {7,[S,D,T]}
5 *6 R!H              ux {2,S} {6,D}
6 *5 R!H              ux {5,D} {3,S}
7    R!H              ux {4,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 371,
    label = "R6_intra_7_member_ring_SSD_D",
    group =
"""
1 *1 R!H              u1 {2,S} {7,[S,D,T]}
2 *4 R!H              ux {1,S} {5,S}
3 *2 [Cd,Ct,CO,N]     u0 {6,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {7,[S,D,T]}
5 *6 R!H              ux {2,S} {6,D}
6 *5 R!H              ux {5,D} {3,S}
7    R!H              ux {4,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 372,
    label = "Rn2(SS)c5_beta_long",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3 *6 R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]} {6,S}
4 *7 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *4 R!H ux {3,S} {7,S}
7 *1 R!H u1 {6,S}
""",
    kinetics = None,
)

entry(
    index = 373,
    label = "Rn2(SS)c5_beta_short",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *6 R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]} {6,S}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]}
6 *4 R!H ux {4,S} {7,S}
7 *1 R!H u1 {6,S}
""",
    kinetics = None,
)

entry(
    index = 374,
    label = "R7_intra_7_member_ring",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {4,[S,D,T]}
2 *4 R!H              ux {1,[S,D,T]} {5,[S,D,T]}
3 *2 [Cd,Ct,CO,N]     u0 {7,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {1,[S,D,T]}
5 *6 R!H              ux {2,[S,D,T]} {6,[S,D,T]}
6 *7 R!H              ux {5,[S,D,T]} {7,[S,D,T]}
7 *5 R!H              ux {6,[S,D,T]} {3,S}
""",
    kinetics = None,
)

entry(
    index = 375,
    label = "R7_intra_7_member_ring_SDSD",
    group =
"""
1 *1 R!H              u1 {2,S} {4,[S,D,T]}
2 *4 R!H              ux {1,S} {5,D}
3 *2 [Cd,Ct,CO,N]     u0 {7,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {1,[S,D,T]}
5 *6 R!H              ux {2,D} {6,S}
6 *7 R!H              ux {5,S} {7,D}
7 *5 R!H              ux {6,D} {3,S}
""",
    kinetics = None,
)

entry(
    index = 376,
    label = "R7_intra_7_member_ring_SDSD_D",
    group =
"""
1 *1 R!H              u1 {2,S} {4,[S,D,T]}
2 *4 R!H              ux {1,S} {5,D}
3 *2 [Cd,Ct,CO,N]     u0 {7,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {1,[S,D,T]}
5 *6 R!H              ux {2,D} {6,S}
6 *7 R!H              ux {5,S} {7,D}
7 *5 R!H              ux {6,D} {3,S}
""",
    kinetics = None,
)

entry(
    index = 368,
    label = "Rn2(DS)c5_alpha",
    group =
"""
1 *2 R!H u0 {2,[D,T]} {5,[S,D,T,B]}
2 *3 R!H u0 {1,[D,T]} {3,[S,D,T,B]}
3    R!H ux {2,[S,D,T,B]} {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H ux {4,[S,D,T,B]} {1,[S,D,T,B]} {6,S}
6 *4 R!H ux {5,S} {7,D}
7 *1 R!H u1 {6,D}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "R5_intra_7_member_ring_SD",
    group =
"""
1 *1 R!H              u1 {2,S} {7,[S,D,T]}
2 *4 R!H              ux {1,S} {5,D}
3 *2 [Cd,Ct,CO,N]     u0 {5,S} {4,[D,T]}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,[D,T]} {6,[S,D,T]}
5 *5 R!H              ux {2,D} {3,S}
6    R!H              ux {4,[S,D,T]} {7,[S,D,T]}
7    R!H              ux {6,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "R5_intra_7_member_ring_SD_D",
    group =
"""
1 *1 R!H              u1 {2,S} {7,[S,D,T]}
2 *4 R!H              ux {1,S} {5,D}
3 *2 [Cd,Ct,CO,N]     u0 {5,S} {4,D}
4 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {3,D} {6,[S,D,T]}
5 *5 R!H              ux {2,D} {3,S}
6    R!H              ux {4,[S,D,T]} {7,[S,D,T]}
7    R!H              ux {6,[S,D,T]} {1,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "Rn1c6b_alpha",
    group =
"""
1 *2 R!H u0 {2,D} {6,S}
2 *3 R!H u0 {1,D} {3,S}
3    R!H ux {2,S} {4,D}
4    R!H ux {3,D} {5,S}
5    R!H ux {4,S} {6,D}
6 *4 R!H ux {5,D} {1,S} {7,S}
7 *1 R!H u1 {6,S}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "radadd_intra_cd_Cs",
    group =
"""
1 *1 Cd     u1 {2,S}
2    Cs     u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "R4_S_(Cd)_D",
    group =
"""
1 *1 R!H      u1 {2,S}
2 *4 Cd       u0 {1,S} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "R5_SB",
    group =
"""
1 *1 R!H                 u1 {2,S}
2 *4 Cb                  u0 {1,S} {3,B}
3 *5 Cb                  u0 {2,B} {4,S}
4 *2 [Cd,Ct,CO,N,CS]     u0 {3,S} {5,[D,T]}
5 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {4,[D,T]}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "Rn4(SDSS)c6_alpha_benzene",
    group =
"""
1  *2 C u0 {2,D} {6,S}
2  *3 C u0 {1,D} {3,S}
3     C u0 {2,S} {4,D}
4     C u0 {3,D} {5,S}
5     C u0 {4,S} {6,D}
6  *5 C u0 {5,D} {1,S} {7,S}
7  *7 C u0 {6,S} {8,S}
8  *6 C u0 {7,S} {9,D}
9  *4 C u0 {8,D} {10,S}
10 *1 C u1 {9,S}
""",
    kinetics = None,
)

entry(
    index = 380,
    label = "R6_intra_6_member_ring",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {4,[S,D,T]}
2 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {1,[S,D,T]} {3,[D,T]}
3 *2 [Cd,Ct,CO,N]     u0 {2,[D,T]} {6,S}
4 *4 R!H              ux {5,[S,D,T,B]} {1,[S,D,T]}
5 *6 R!H              ux {4,[S,D,T,B]} {6,[S,D,T]}
6 *5 R!H              ux {3,S} {5,[S,D,T]}
""",
    kinetics = None,
)

entry(
    index = 381,
    label = "R6_intra_6_member_ring_SBS",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {4,S}
2 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {1,[S,D,T]} {3,[D,T]}
3 *2 [Cd,Ct,CO,N]     u0 {2,[D,T]} {6,S}
4 *4 R!H              ux {5,B} {1,S}
5 *6 R!H              ux {4,B} {6,S}
6 *5 R!H              ux {3,S} {5,S} 
""",
    kinetics = None,
)

entry(
    index = 382,
    label = "R6_intra_6_member_ring_SBS_D",
    group =
"""
1 *1 R!H              u1 {2,[S,D,T]} {4,S}
2 *3 [Cd,Ct,Od,Sd,Cdd,N] u0 {1,[S,D,T]} {3,D}
3 *2 [Cd,Ct,CO,N]     u0 {2,D} {6,S}
4 *4 R!H              ux {5,B} {1,S}
5 *6 R!H              ux {4,B} {6,S}
6 *5 R!H              ux {3,S} {5,S} 
""",
    kinetics = None,
)

entry(
    index = 383,
    label = "R4_S_(Cm)_D",
    group =
"""
1 *1 R!H      u1 {2,S}
2 *4 [Cd,CO]  u0 {1,S} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 384,
    label = "R4_S_(CO)_D",
    group =
"""
1 *1 R!H      u1 {2,S}
2 *4 CO       u0 {1,S} {3,S}
3 *2 Cd       u0 {2,S} {4,D}
4 *3 [Cd,Cdd] u0 {3,D}
""",
    kinetics = None,
)

tree(
"""
L1: Rn
    L2: Rnx_cyclics
        L3: Rnxc3
            L4: Rn4c3_alpha
            L4: Rn3c3_alpha
            L4: Rn2c3_alpha
            L4: Rn1c3_alpha
        L3: Rnxc4
            L4: Rnxc4_alpha
                L5: Rn4c4_alpha
                L5: Rn3c4_alpha
                L5: Rn2c4_alpha
                L5: Rn1c4_alpha
            L4: Rnxc4_beta
                L5: Rn3c4_beta
                L5: Rn2c4_beta
                L5: Rn1c4_beta
        L3: Rnxc5
            L4: Rnxc5_alpha
                L5: Rn4c5_alpha
                L5: Rn3c5_alpha
                L5: Rn2c5_alpha
                    L6: Rn2(SS)c5_alpha
                    L6: Rn2(DS)c5_alpha
                L5: Rn1c5_alpha
		    L6: Rn1c5_alpha_benzene
            L4: Rnxc5_beta_long
                L5: Rn3c5_beta_long
                L5: Rn2c5_beta_long
                    L6: Rn2(SS)c5_beta_long
                L5: Rn1c5_beta_long
            L4: Rnxc5_beta_short
                L5: Rn3c5_beta_short
                L5: Rn2c5_beta_short
                    L6: Rn2(SS)c5_beta_short
                L5: Rn1c5_beta_short
        L3: Rnxc6
            L4: Rnxc6_alpha
                L5: Rn4c6_alpha
                    L6: Rn4c6_alpha_benzene
                        L7: Rn4c6_alpha_benzene_Cdchain
                        L7: Rn4(SDSS)c6_alpha_benzene
                    L6: Rn4(SDSD)c6_alpha
                    L6: Rn4(looped)c6_alpha
                L5: Rn3c6_alpha
                    L6:Rn3c6b_alpha
                        L7: Rn3(RSS)c6b_alpha
                        L7: Rn3(SDS)c6b_alpha
                L5: Rn2c6_alpha
                L5: Rn1c6_alpha
                    L6: Rn1c6b_alpha
            L4: Rnxc6_beta_long
                L5: Rn3c6_beta_long
                L5: Rn2c6_beta_long
                L5: Rn1c6_beta_long
            L4: Rnxc6_beta_short
                L5: Rn3c6_beta_short
                L5: Rn2c6_beta_short
                L5: Rn1c6_beta_short
            L4: Rnxc6_gamma
                L5: Rn2c6_gamma
                L5: Rn1c6_gamma
        L3: Rnxc7
            L4: Rnxc7_alpha
                L5: Rn4c7_alpha
                L5: Rn3c7_alpha
                L5: Rn2c7_alpha
                L5: Rn1c7_alpha
            L4: Rnxc7_beta_long
                L5: Rn3c7_beta_long
                L5: Rn2c7_beta_long
                L5: Rn1c7_beta_long
            L4: Rnxc7_beta_short
                L5: Rn3c7_beta_short
                L5: Rn2c7_beta_short
                L5: Rn1c7_beta_short
            L4: Rnxc7_gamma_long
                L5: Rn2c7_gamma_long
                L5: Rn1c7_gamma_long
            L4: Rnxc7_gamma_short
                L5: Rn2c7_gamma_short
                L5: Rn1c7_gamma_short
        L3: Rnxc8
            L4: Rnxc8_alpha
                L5: Rn4c8_alpha
                L5: Rn3c8_alpha
                L5: Rn2c8_alpha
                L5: Rn1c8_alpha
            L4: Rnxc8_beta_long
                L5: Rn3c8_beta_long
                L5: Rn2c8_beta_long
                L5: Rn1c8_beta_long
            L4: Rnxc8_beta_short
                L5: Rn3c8_beta_short
                L5: Rn2c8_beta_short
                L5: Rn1c8_beta_short
            L4: Rnxc8_gamma_long
                L5: Rn2c8_gamma_long
                L5: Rn1c8_gamma_long
            L4: Rnxc8_gamma_short
                L5: Rn2c8_gamma_short
                L5: Rn1c8_gamma_short
            L4: Rnxc8_epsilon
                L5: Rn1c8_epsilon
    L2: R4
        L3: R4_intra_6_member_ring
            L4: R4_intra_6_member_ring_S
                L5: R4_intra_6_member_ring_S_D
                    L6: R4_intra_6_member_ring_S_D_2H
			L7: 2-hydro-nathphalene
                    L6: R4_intra_6_member_ring_S_D_2R!H
                    L6: R4_intra_6_member_ring_S_D_H_R!H
        L3: R4_intra_7_member_ring
            L4: R4_intra_7_member_ring_S
                L5: R4_intra_7_member_ring_S_D
        L3: R4_S
            L4: R4_S_D
                L5: R4_S_(Cm)_D
                    L6: R4_S_(Cd)_D
                    L6: R4_S_(CO)_D
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
        L3: R5_intra_7_member_ring
            L4: R5_intra_7_member_ring_SS
                L5: R5_intra_7_member_ring_SS_D
            L4: R5_intra_7_member_ring_SD
                L5: R5_intra_7_member_ring_SD_D
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
            L4: R5_SB
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
        L3: R6_intra_10_member_ring
            L4: R6_intra_10_member_ring_SSD
                L5: R6_intra_10_member_ring_SSD_D
        L3: R6_intra_7_member_ring
            L4: R6_intra_7_member_ring_SSD
                L5: R6_intra_7_member_ring_SSD_D
	L3: R6_intra_6_member_ring
	    L4: R6_intra_6_member_ring_SBS
		L5: R6_intra_6_member_ring_SBS_D
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
            L4: R7_intra_10_member_ring
                L5: R7_intra_10_member_ring_SDSD
                    L6: R7_intra_10_member_ring_SDSD_D
            L4: R7_intra_7_member_ring
                L5: R7_intra_7_member_ring_SDSD
                    L6: R7_intra_7_member_ring_SDSD_D
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
            L4: R8_intra_10_member_ring
                L5: R8_intra_10_member_ring_SSDSD
                    L6: R8_intra_10_member_ring_SSDSD_D
            L4: R8_SDSDS
        L3: R9
        L3: R10
        L3: R11
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
		L5:doublebond_intra_HDe_secDe_benzene 
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
		L5: doublebond_intra_DeDe_pri_cyc6
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
	    L4: radadd_intra_csHCb
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
            L4: radadd_intra_cd_Cs
        L3: radadd_intra_cdsingleDe
	        L4:radadd_intra_cdsingleDe_cb
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

####################
#Forbid a carbon radical 2 carbons away from a phenyl side group from adding to either the meta- or para- position
forbidden(
    label = "beta_C_rad_to_meta_phenyl_res1",
    group =
"""
1 *4 C u0 {2,S} {3,[S,D,T]}
2 *6 C u0 {1,S} {4,D} {5,S}
3 *1 C u1 {1,[S,D,T]}
4 *5 C u0 {2,D} {7,S}
5    C u0 {2,S} {8,D}
6 *3 C u0 {7,D} {8,S}
7 *2 C u0 {4,S} {6,D}
8    C u0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a carbon radical 2 carbons away from a phenyl side group from adding to the meta-position
because the TS would be far too strained. Resonance form 1.
""",
)

forbidden(
    label = "beta_C_rad_to_meta_phenyl_res2",
    group =
"""
1 *4 C u0 {2,S} {3,[S,D,T]}
2 *6 C u0 {1,S} {4,S} {5,D}
3 *1 C u1 {1,[S,D,T]}
4 *3 C u0 {2,S} {7,D}
5 *7 C u0 {2,D} {8,S}
6 *5 C u0 {7,S} {8,D}
7 *2 C u0 {4,D} {6,S}
8 *8 C u0 {5,S} {6,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a carbon radical 2 carbons away from a phenyl side group from adding to the meta-position
because the TS would be far too strained. Resonance form 2.
""",
)

forbidden(
    label = "beta_C_rad_para_phenyl",
    group =
"""
1 *4 C u0 {2,S} {3,[S,D,T]}
2 *6 C u0 {1,S} {4,D} {5,S}
3 *1 C u1 {1,[S,D,T]}
4    C u0 {2,D} {7,S}
5 *7 C u0 {2,S} {8,D}
6 *2 C u0 {7,D} {8,S}
7 *3 C u0 {4,S} {6,D}
8 *5 C u0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a carbon radical 2 carbons away from a phenyl side group from adding to the para-position
because the TS would be far too strained.
""",
)
###################

####################
#Forbid a carbon radical 1 carbon away from a phenyl side group (benzylic position) from adding to either the meta- or para- position
forbidden(
    label = "alpha_C_rad_to_meta_phenyl_res1",
    group =
"""
1 *1 C u1 {2,S}
2 *4 C u0 {1,S} {3,D} {4,S}
3 *5 C u0 {2,D} {6,S}
4    C u0 {2,S} {7,D}
5 *3 C u0 {6,D} {7,S}
6 *2 C u0 {3,S} {5,D}
7    C u0 {4,D} {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a carbon radical 1 carbons away from a phenyl side group (benzylic position) from adding to the meta-position
because the TS would be far too strained. Resonance form 1.
""",
)

forbidden(
    label = "alpha_C_rad_to_meta_phenyl_res2",
    group =
"""
1 *1 C u1 {2,S}
2 *4 C u0 {1,S} {3,S} {4,D}
3 *3 C u0 {2,S} {6,D}
4 *6 C u0 {2,D} {7,S}
5 *5 C u0 {6,S} {7,D}
6 *2 C u0 {3,D} {5,S}
7 *7 C u0 {4,S} {5,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a carbon radical 1 carbons away from a phenyl side group (benzylic position) from adding to the meta-position
because the TS would be far too strained. Resonance form 2.
""",
)

forbidden(
    label = "alpha_C_rad_to_para_phenyl",
    group =
"""
1 *1 C u1 {2,S}
2 *4 C u0 {1,S} {3,S} {4,D}
3 *6 C u0 {2,S} {6,D}
4    C u0 {2,D} {7,S}
5 *2 C u0 {6,S} {7,D}
6 *5 C u0 {3,D} {5,S}
7 *3 C u0 {4,S} {5,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a carbon radical 1 carbons away from a phenyl side group (benzylic position) from adding to the para-position
because the TS would be far too strained.
""",
)
###################

####################
#Forbid a carbon radical 3 carbons away from a phenyl side group from adding to either the meta- or para- position
forbidden(
    label = "gamma_C_rad_to_meta_phenyl_res1",
    group =
"""
1 *6 C u0 {2,S} {3,[S,D,T]}
2 *7 C u0 {1,S} {4,D} {5,S}
3 *4 C u0 {1,[S,D,T]} {9,[S,D,T]}
4 *5 C u0 {2,D} {7,S}
5    C u0 {2,S} {8,D}
6 *3 C u0 {7,D} {8,S}
7 *2 C u0 {4,S} {6,D}
8    C u0 {5,D} {6,S}
9 *1 C u1 {3,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a carbon radical 3 carbons away from a phenyl side group from adding to the meta-position
because the TS would be far too strained. Resonance form 1.
""",
)

forbidden(
    label = "gamma_C_rad_to_meta_phenyl_res2",
    group =
"""
1 *6 C u0 {2,S} {3,[S,D,T]}
2 *7 C u0 {1,S} {4,S} {5,D}
3 *4 C u0 {1,[S,D,T]} {9,[S,D,T]}
4 *3 C u0 {2,S} {7,D}
5 *8 C u0 {2,D} {8,S}
6 *5 C u0 {7,S} {8,D}
7 *2 C u0 {4,D} {6,S}
8 *9 C u0 {5,S} {6,D}
9 *1 C u1 {3,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a carbon radical 3 carbons away from a phenyl side group from adding to the meta-position
because the TS would be far too strained. Resonance form 2.
""",
)

forbidden(
    label = "gamma_C_rad_to_para_phenyl",
    group =
"""
1 *6 C u0 {2,S} {3,[S,D,T]}
2 *7 C u0 {1,S} {4,S} {5,D}
3 *4 C u0 {1,[S,D,T]} {9,[S,D,T]}
4 *8 C u0 {2,S} {7,D}
5    C u0 {2,D} {8,S}
6 *2 C u0 {7,S} {8,D}
7 *5 C u0 {4,D} {6,S}
8 *3 C u0 {5,S} {6,D}
9 *1 C u1 {3,[S,D,T]}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a carbon radical 3 carbons away from a phenyl side group from adding to the para-position
because the TS would be far too strained.
""",
)
###################

###################
#Forbid phenyl radical from ring-closing on itself to make either a 3-5 or 4-4 membered bicyclic
forbidden(
    label = "Phenyl_self_3_5_ring_close_res1",
    group =
"""
1 *1 C u1 {2,D} {6,S}
2    C u0 {1,D} {3,S}
3 *2 C u0 {2,S} {4,D}
4 *3 C u0 {3,D} {5,S}
5    C u0 {4,S} {6,D}
6    C u0 {1,S} {5,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 3 and 5 membered ring. Resonance form 1.
""",
)

forbidden(
    label = "Phenyl_self_3_5_ring_close_res2",
    group =
"""
1 *1 C u1 {2,S} {6,D}
2 *3 C u0 {1,S} {3,D}
3 *2 C u0 {2,D} {4,S}
4    C u0 {3,S} {5,D}
5    C u0 {4,D} {6,S}
6    C u0 {1,D} {5,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 3 and 5 membered ring. Resonance form 2.
""",
)

forbidden(
    label = "Phenyl_self_4_4_ring_close_res1",
    group =
"""
1 *1 C u1 {2,D} {6,S}
2    C u0 {1,D} {3,S}
3 *3 C u0 {2,S} {4,D}
4 *2 C u0 {3,D} {5,S}
5    C u0 {4,S} {6,D}
6    C u0 {1,S} {5,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a phenyl radical from doing a ring closure on itself to form a fused 4 and 4 membered ring. Resonance form 1.
""",
)
###################
#Forbidden groups from C10H11 kinetic library
forbidden(
    label = "INDENYL_TO_INDENYLADD_res1",
    group =
"""
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 C u0 p0 c0 {1,D} {7,S}
4 *3 C u0 p0 c0 {2,S} {7,D}
5 C u0 p0 c0 {1,S} {9,D}
6 C u0 p0 c0 {2,D} {8,S}
7 *2 C u0 p0 c0 {3,S} {4,D}
8 *1 C u1 p0 c0 {6,S} {9,S}
9 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 5-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD_res2",
    group =
"""
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S}
4 C u0 p0 c0 {2,D} {7,S}
5 *3 C u0 p0 c0 {1,S} {9,D}
6 C u0 p0 c0 {2,S} {8,D}
7 *1 C u1 p0 c0 {3,S} {4,S}
8 C u0 p0 c0 {6,D} {9,S}
9 *2 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 5-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD2_res1",
    group =
"""
1 *3 C u0 p0 c0 {2,S} {3,S} {5,D}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 C u0 p0 c0 {2,S} {7,D}
5 *2 C u0 p0 c0 {1,D} {9,S}
6 C u0 p0 c0 {2,D} {8,S}
7 C u0 p0 c0 {3,S} {4,D}
8 C u0 p0 c0 {6,S} {9,D}
9 C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 3-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD2_res2",
    group =
"""
1 *3 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 *2 C u0 p0 c0 {1,D} {7,S}
4 C u0 p0 c0 {2,S} {7,D}
5 *1 C u1 p0 c0 {1,S} {9,S}
6 C u0 p0 c0 {2,D} {8,S}
7 C u0 p0 c0 {3,S} {4,D}
8 C u0 p0 c0 {6,S} {9,D}
9 C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 3-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD2_res3",
    group =
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 C u0 p0 c0 {2,S} {7,D}
5 *2 C u0 p0 c0 {1,S} {9,D}
6 C u0 p0 c0 {2,S} {8,D}
7 C u0 p0 c0 {3,S} {4,D}
8 C u0 p0 c0 {6,D} {9,S}
9 *3 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 3-membered ring tricyclic.
Resonance form 3.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD3_res1",
    group =
"""
1 C u0 p0 c0 {2,S} {3,S} {5,D}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 *2 C u0 p0 c0 {2,S} {7,D}
5 C u0 p0 c0 {1,D} {9,S}
6 C u0 p0 c0 {2,D} {8,S}
7 *3 C u0 p0 c0 {3,S} {4,D}
8 C u0 p0 c0 {6,S} {9,D}
9 C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,4, and 3-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD3_res2",
    group =
"""
1 C u0 p0 c0 {2,D} {3,S} {5,S}
2 C u0 p0 c0 {1,D} {4,S} {6,S}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 *2 C u0 p0 c0 {2,S} {7,D}
5 C u0 p0 c0 {1,S} {9,D}
6 C u0 p0 c0 {2,S} {8,D}
7 *3 C u0 p0 c0 {3,S} {4,D}
8 C u0 p0 c0 {6,D} {9,S}
9 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,4, and 3-membered ring tricyclic.
Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD3_res3",
    group =
"""
1 C u0 p0 c0 {2,B} {3,S} {5,B}
2 C u0 p0 c0 {1,B} {4,S} {6,B}
3 *1 C u1 p0 c0 {1,S} {7,S}
4 *2 C u0 p0 c0 {2,S} {7,D}
5 C u0 p0 c0 {1,B} {9,B}
6 C u0 p0 c0 {2,B} {8,B}
7 *3 C u0 p0 c0 {3,S} {4,D}
8 C u0 p0 c0 {6,B} {9,B}
9 C u0 p0 c0 {5,B} {8,B}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,4, and 3-membered ring tricyclic.
Resonance form3.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD4_res1",
    group =
"""
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,D}
3 C u0 p0 c0 {1,D} {7,S}
4 *3 C u0 p0 c0 {2,S} {7,D}
5 *1 C u1 p0 c0 {1,S} {9,S}
6 C u0 p0 c0 {2,D} {8,S}
7 *2 C u0 p0 c0 {3,S} {4,D}
8 C u0 p0 c0 {6,S} {9,D}
9 C u0 p0 c0 {5,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 4-membered ring tricyclic.
Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD4_res2",
    group =
"""
1 C u0 p0 c0 {2,S} {3,D} {5,S}
2 C u0 p0 c0 {1,S} {4,D} {6,S}
3 C u0 p0 c0 {1,D} {7,S}
4 C u0 p0 c0 {2,D} {7,S}
5 *2 C u0 p0 c0 {1,S} {9,D}
6 C u0 p0 c0 {2,S} {8,D}
7 *1 C u1 p0 c0 {3,S} {4,S}
8 C u0 p0 c0 {6,D} {9,S}
9 *3 C u0 p0 c0 {5,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from doing a ring closure to form a fused 6,5, and 4-membered ring tricyclic.
Resonance form 2.
""",
)

###################
#Forbidden groups from vinylCPD_H kinetic library

forbidden(
    label = "product45_to_product56",
    group =
"""
1 C u0 p0 c0 {2,S} {3,S} {5,S}
2 C u0 p0 c0 {1,S} {4,S} {6,S}
3 *3 C u0 p0 c0 {1,S} {4,D}
4 *2 C u0 p0 c0 {2,S} {3,D}
5 C u0 p0 c0 {1,S} {7,D}
6 *1 C u1 p0 c0 {2,S} {7,S}
7 C u0 p0 c0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid product45 in vinylCPD_H library from ring closing to form a fused 5, 4, and 3-membered ring tricyclic.
""",
)

forbidden(
    label = "product34_to_product57",
    group =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S}
2 C u0 p0 c0 {1,S} {3,S} {5,S}
3 *1 C u1 p0 c0 {1,S} {2,S}
4 *2 C u0 p0 c0 {1,S} {6,D}
5 C u0 p0 c0 {2,S} {7,D}
6 *3 C u0 p0 c0 {4,D} {7,S}
7 C u0 p0 c0 {5,D} {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid product34 in vinylCPD_H library from ring closing to form a fused 6, 3, and 3-membered ring tricyclic.
""",
)

###################
#Forbidden groups to enable Naphthalene formation from CPD'yl recombination

forbidden(
    label = "product1_strained_ringclose",
    group =
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S}
3 C u0 p0 c0 {1,S} {2,S} {7,S}
4 *2 C u0 p0 c0 {1,S} {9,D}
5 C u0 p0 c0 {1,S} {10,D}
6 C u0 p0 c0 {2,S} {8,D}
7 *1 C u1 p0 c0 {3,S} {8,S}
8 C u0 p0 c0 {6,D} {7,S}
9 *3 C u0 p0 c0 {4,D} {10,S}
10 C u0 p0 c0 {5,D} {9,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid product1 in naphthalene_H library from ring closing to form a highly-strained
fused 5, 4, 3, and 5-membered ring tetracyclic.

Badly estimated kinetics and thermo for this reaction would cause RMG to divert flux
to this reaction, instead of following the naphthalene-forming pathway.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD5_res1",
    group =
"""
1 C u0 {2,S} {4,S}
2 C u0 {1,S} {3,S} {7,D}
3 C u0 {2,S} {5,S} {6,D}
4 *2 C u0 {1,S} {5,D}
5 *3 C u0 {3,S} {4,D}
6 C u0 {3,D} {8,S}
7 C u0 {2,D} {9,S}
8 C u0 {6,S} {9,D}
9 *1 C u1 {7,S} {8,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from  ring-closing to form a highly strained tricyclic. Resonance form 1.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD5_res2",
    group =
"""
1 C u0 {2,S} {4,S}
2 C u0 {1,S} {3,B} {7,B}
3 C u0 {2,B} {5,S} {6,B}
4 *2 C u0 {1,S} {5,D}
5 *3 C u0 {3,S} {4,D}
6 C u0 {3,B} {8,B}
7 C u0 {2,B} {9,B}
8 C u0 {6,B} {9,B}
9 *1 C u1 {7,B} {8,B}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from  ring-closing to form a highly strained tricyclic. Resonance form 2.
""",
)

forbidden(
    label = "INDENYL_TO_INDENYLADD5_res3",
    group =
"""
1 C u0 {2,S} {4,S}
2 C u0 {1,S} {3,D} {7,S}
3 C u0 {2,D} {5,S} {6,S}
4 *2 C u0 {1,S} {5,D}
5 *3 C u0 {3,S} {4,D}
6 C u0 {3,S} {8,D}
7 C u0 {2,S} {9,D}
8 C u0 {6,D} {9,S}
9 *1 C u1 {7,D} {8,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid an indenyl radical from  ring-closing to form a highly strained tricyclic. Resonance form 3.
""",
)

forbidden(
    label = "phenyl_CPDyl_ring_close_dir_1",
    group =
"""
1 C u0 {2,S} {3,S} {4,D}
2 C u0 {1,S} {5,S} {6,D}
3 *1 C u1 {1,S} {7,S}
4 C u0 {1,D} {8,S}
5 C u0 {2,S} {9,D}
6 C u0 {2,D} {10,S}
7 C u0 {3,S} {8,D}
8 C u0 {4,S} {7,D}
9 C u0 {5,D} {11,S}
10 *3 C u0 {6,S} {11,D}
11 *2 C u0 {9,S} {10,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a phenyl-CPDyl radical connected by a single bond from undergoing a strained ring closure to  the para-position
of the phenyl ring. CPD'yl to phenyl direction.
""",
)

forbidden(
    label = "phenyl_CPDyl_ring_close_dir_2",
    group =
"""
1 C u0 {2,D} {3,S} {4,S}
2 C u0 {1,D} {5,S} {6,S}
3 *2 C u0 {1,S} {7,D}
4 C u0 {1,S} {8,D}
5 C u0 {2,S} {9,D}
6 C u0 {2,S} {10,D}
7 *3 C u0 {3,D} {8,S}
8 C u0 {4,D} {7,S}
9 C u0 {5,D} {11,S}
10  C u0 {6,D} {11,S}
11 *1 C u1 {9,S} {10,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Forbid a phenyl-CPDyl radical connected by a single bond from undergoing a strained ring closure to  the para-position
of the phenyl ring. Phenyl to CPD'yl direction.
""",
)

forbidden(
    label = "s2_4_5_diene_1_5_self_ring_close_res1",
    group =
"""
1  *1 C u1 p0 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  *2 C u0 p0 c0 {3,S} {5,D}
5  *3 C u0 p0 c0 {4,D} {6,S}
6  C u0 p0 c0 {3,S} {5,S} {7,S}
7  C u0 p0 c0 {1,S} {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a s2_4_5_diene_1_5 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure
from the tip of the 5-member ring to the corner of the 4. Resonance form 1.
""",
)

forbidden(
    label = "s2_4_5_diene_1_5_self_ring_close_res2",
    group =
"""
1  *1 C u1 p0 c0 {2,S} {7,S}
2  C u0 p0 c0 {1,S} {3,D}
3  C u0 p0 c0 {2,D} {4,S} {6,S}
4  *3 C u0 p0 c0 {3,S} {5,D}
5  *2 C u0 p0 c0 {4,D} {6,S}
6  C u0 p0 c0 {3,S} {5,S} {7,S}
7  C u0 p0 c0 {1,S} {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a s2_4_5_diene_1_5 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure
from the tip of the 5-member ring to the corner of the 4. Resonance form 2.
""",
)

forbidden(
    label = "s2_4_5_diene_1_5_self_ring_close_res3",
    group =
"""
1  *2 C u0 p0 c0 {2,D} {7,S}
2  *3 C u0 p0 c0 {1,D} {3,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {3,D} {5,S}
5  *1 C u1 p0 c0 {4,S} {6,S}
6  C u0 p0 c0 {3,S} {5,S} {7,S}
7  C u0 p0 c0 {1,S} {6,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a s2_4_5_diene_1_5 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure
from the tip of the 5-member ring to the corner of the 4. Resonance form 3.
""",
)

####################
#Forbid a carbon radical bonded to a cyclohexadiene side group from adding to the meta or para- position

forbidden(
    label = "s2_3_6_diene_0_2_self_ring_close_1_res_1",
    group =
"""
1  *1 C u1 {3,S} {8,S}
3  C u0 {1,S} {4,D} {8,S}
4  C u0 {3,D} {5,S}
5  *3 C u0 {4,S} {6,D}
6  *2 C u0 {5,D} {7,S}
7  C u0 {6,S} {8,S}
8  C u0 (1,S} {3,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a s2_3_6_diene_0_2 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure
from the tip of the 3-member ring to one of the far corners of the 6. Resonance form 1.
""",
)

forbidden(
    label = "s2_3_6_diene_0_2_self_ring_close_1_res_2",
    group =
"""
1  *2 C u0 {3,D} {8,S}
3  *3 C u0 {1,D} {4,S} {8,S}
4  C u0 {3,S} {5,D}
5  C u0 {4,D} {6,S}
6  *1 C u1 {5,S} {7,S}
7  C u0 {6,S} {8,S}
8  C u0 (1,S} {3,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a s2_3_6_diene_0_2 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure
from the tip of the 3-member ring to one of the far corners of the 6. Resonance form 2.
""",
)

forbidden(
    label = "s2_3_6_diene_0_2_self_ring_close_2_2",
    group =
"""
1  *1 C u1 {3,S} {8,S}
3  C u0 {1,S} {4,D} {8,S}
4  C u0 {3,D} {5,S}
5  *2 C u0 {4,S} {6,D}
6  *3 C u0 {5,D} {7,S}
7  C u0 {6,S} {8,S}
8  C u0 (1,S} {3,S} {7,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a s2_3_6_diene_0_2 bicyclic (using polycyclic.py nomenclature) from undergoing a highly strained self-ring closure
from the tip of the 3-member ring to one of the far corners of the 6.
""",
)

###################
#Forbidden groups for Naphthyl radical

forbidden(
    label = "1_naphthyl_7_add_res1",
    group =
"""
1 C u0 {2,B} {3,S} {4,B}
2 C u0 {1,B} {5,S} {10,B}
3 C u0 {1,S} {6,D}
4 C u0 {1,B} {8,B}
5 *3 C u0 {2,S} {7,D}
6 C u0 {3,D} {7,S}
7 *2 C u0 {5,D} {6,S}
8 C u0 {4,B} {9,B}
9 C u0 {8,B} {10,B}
10 *1 C u1 {2,B} {9,B}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 1.
""",
)

forbidden(
    label = "1_naphthyl_7_add_res2",
    group =
"""
1 C u0 {2,S} {3,S} {4,D}
2 C u0 {1,S} {5,S} {10,D}
3 C u0 {1,S} {6,D}
4 C u0 {1,D} {8,S}
5 *3 C u0 {2,S} {7,D}
6 C u0 {3,D} {7,S}
7 *2 C u0 {5,D} {6,S}
8 C u0 {4,S} {9,D}
9 C u0 {8,D} {10,S}
10 *1 C u1 {2,D} {9,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 2.
""",
)

forbidden(
    label = "1_naphthyl_7_add_res3",
    group =
"""
1 C u0 {2,D} {3,S} {4,S}
2 C u0 {1,D} {5,S} {10,S}
3 C u0 {1,S} {6,D}
4 C u0 {1,S} {8,D}
5 *3 C u0 {2,S} {7,D}
6 C u0 {3,D} {7,S}
7 *2 C u0 {5,D} {6,S}
8 C u0 {4,D} {9,S}
9 C u0 {8,S} {10,D}
10 *1 C u1 {2,S} {9,D}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 3.
""",
)

forbidden(
    label = "1_naphthyl_7_add_res4",
    group =
"""
1 C u0 {2,S} {3,S} {4,D}
2 C u0 {1,S} {5,S} {10,D}
3 C u0 {1,S} {6,D}
4 C u0 {1,D} {8,S}
5 *1 C u1 {2,S} {7,D}
6 C u0 {3,D} {7,S}
7 C u0 {5,D} {6,S}
8 *3 C u0 {4,S} {9,D}
9 *2 C u0 {8,D} {10,S}
10 C u0 {2,D} {9,S}
""",
    shortDesc = u"""""",
    longDesc =
u"""
Prevent a 1-naphthyl radical from attacking it's 7 site. Resonance form 4.
""",
)
