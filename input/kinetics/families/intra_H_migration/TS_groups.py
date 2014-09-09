#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/TS_groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "RnH",
    group = "OR{R2Hall, R3Hall, R4Hall, R5Hall, R6Hall, R7Hall}",
    distances = DistanceData(
        distances = {'d12': 1.92444, 'd13': 1.31733, 'd23': 1.29172},
        uncertainties = {'d12': 0.190471, 'd13': 0.052898, 'd23': 0.049569},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 21 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=185 label="R7H">, <Entry index=200 label="C_rad_out_2H">, <Entry index=219 label="O_H_out">]
[<Entry index=16 label="R3H_SS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=219 label="O_H_out">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
[<Entry index=56 label="R4H_BSD">, <Entry index=196 label="Cb_rad_out">, <Entry index=227 label="Cd_H_out_singleH">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 2,
    label = "Y_rad_out",
    group = 
"""
1 *1 R!H u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 3,
    label = "XH_out",
    group = 
"""
1 *2 R!H u0 {2,S}
2 *3 H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 4,
    label = "R2Hall",
    group = "OR{R2H}",
    distances = DistanceData(
        distances = {'d12': -0.408743, 'd13': -0.027862, 'd23': -0.012622},
        uncertainties = {'d12': 0.1955, 'd13': 0.030656, 'd23': 0.026451},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 10 distances.
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
""",
)

entry(
    index = 5,
    label = "R2H",
    group = 
"""
1 *1 R!H u1 {2,[S,D,B]}
2 *2 R!H u0 {1,[S,D,B]} {3,S}
3 *3 H   u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.408743, 'd13': -0.027862, 'd23': -0.012622},
        uncertainties = {'d12': 0.1955, 'd13': 0.030656, 'd23': 0.026451},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 10 distances.
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
""",
)

entry(
    index = 6,
    label = "R2H_S",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *2 R!H u0 {1,S} {3,S}
3 *3 H   u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.408743, 'd13': -0.027862, 'd23': -0.012622},
        uncertainties = {'d12': 0.1955, 'd13': 0.030656, 'd23': 0.026451},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 10 distances.
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
""",
)

entry(
    index = 7,
    label = "R2H_S_cy3",
    group = 
"""
1 *1 R!H u1 {2,S} {4,[S,D,B]}
2 *2 R!H u0 {1,S} {3,S} {4,[S,D,B]}
3 *3 H   u0 {2,S}
4    R!H u0 {1,[S,D,B]} {2,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 8,
    label = "R2H_S_cy4",
    group = 
"""
1 *1 R!H u1 {2,S} {5,[S,D,B]}
2 *2 R!H u0 {1,S} {3,S} {4,[S,D,B]}
3 *3 H   u0 {2,S}
4    R!H u0 {2,[S,D,B]} {5,[S,D,B]}
5    R!H u0 {1,[S,D,B]} {4,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 9,
    label = "R2H_S_cy5",
    group = 
"""
1 *1 R!H u1 {2,S} {6,[S,D,B]}
2 *2 R!H u0 {1,S} {3,S} {4,[S,D,B]}
3 *3 H   u0 {2,S}
4    R!H u0 {2,[S,D,B]} {5,[S,D,B]}
5    R!H u0 {4,[S,D,B]} {6,[S,D,B]}
6    R!H u0 {1,[S,D,B]} {5,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 10,
    label = "R2H_D",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *2 Cd u0 {1,D} {3,S}
3 *3 H  u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 11,
    label = "R2H_B",
    group = 
"""
1 *1 Cb u1 {2,B}
2 *2 Cb u0 {1,B} {3,S}
3 *3 H  u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 12,
    label = "R3Hall",
    group = 
"""
1 *1 R!H u1       {2,[S,D,T,B]}
2 *4 R!H u[0,1,2] {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *2 R!H u0       {2,[S,D,T,B]} {4,S}
4 *3 H   u0       {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.233073, 'd13': 0.056335, 'd23': 0.061697},
        uncertainties = {'d12': 3.14385, 'd13': 0.520728, 'd23': 0.36572},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=16 label="R3H_SS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 13,
    label = "R3HJ",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u1 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *2 R!H u0 {2,[S,D,T,B]} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 14,
    label = "R3H",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *2 R!H u0 {2,[S,D,T,B]} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.233073, 'd13': 0.056335, 'd23': 0.061697},
        uncertainties = {'d12': 3.14385, 'd13': 0.520728, 'd23': 0.36572},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=16 label="R3H_SS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 15,
    label = "R3H_SR",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,[S,D,T,B]}
3 *2 R!H u0 {2,[S,D,T,B]} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.233073, 'd13': 0.056335, 'd23': 0.061697},
        uncertainties = {'d12': 3.14385, 'd13': 0.520728, 'd23': 0.36572},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=16 label="R3H_SS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 16,
    label = "R3H_SS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.233073, 'd13': 0.056335, 'd23': 0.061697},
        uncertainties = {'d12': 3.14385, 'd13': 0.520728, 'd23': 0.36572},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=16 label="R3H_SS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 17,
    label = "R3H_SS_2Cd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,S}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 18,
    label = "R3H_SS_OOCs",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *2 Cs u0 {2,S} {4,S}
4 *3 H  u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 19,
    label = "R3H_SS_S",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ss  u0 {1,S} {3,S}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 20,
    label = "R3H_SS_12cy3",
    group = 
"""
1 *1 R!H u1 {2,S} {5,[S,D,B]}
2 *4 R!H u0 {1,S} {3,S} {5,[S,D,B]}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
5    R!H u0 {1,[S,D,B]} {2,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 21,
    label = "R3H_SS_23cy3",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S} {5,[S,D,B]}
3 *2 R!H u0 {2,S} {4,S} {5,[S,D,B]}
4 *3 H   u0 {3,S}
5    R!H u0 {2,[S,D,B]} {3,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 22,
    label = "R3H_SS_13cy4",
    group = 
"""
1 *1 R!H u1 {2,S} {5,[S,D,B]}
2 *4 R!H u0 {1,S} {3,S}
3 *2 R!H u0 {2,S} {4,S} {5,[S,D,B]}
4 *3 H   u0 {3,S}
5    R!H u0 {1,[S,D,B]} {3,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 23,
    label = "R3H_SS_12cy4",
    group = 
"""
1 *1 R!H u1 {2,S} {6,[S,D,B]}
2 *4 R!H u0 {1,S} {3,S} {5,[S,D,B]}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
5    R!H u0 {2,[S,D,B]} {6,[S,D,B]}
6    R!H u0 {1,[S,D,B]} {5,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 24,
    label = "R3H_SS_23cy4",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S} {6,[S,D,B]}
3 *2 R!H u0 {2,S} {4,S} {5,[S,D,B]}
4 *3 H   u0 {3,S}
5    R!H u0 {3,[S,D,B]} {6,[S,D,B]}
6    R!H u0 {2,[S,D,B]} {5,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 25,
    label = "R3H_SS_13cy5",
    group = 
"""
1 *1 R!H u1 {2,S} {6,[S,D,B]}
2 *4 R!H u0 {1,S} {3,S}
3 *2 R!H u0 {2,S} {4,S} {5,[S,D,B]}
4 *3 H   u0 {3,S}
5    R!H u0 {3,[S,D,B]} {6,[S,D,B]}
6    R!H u0 {1,[S,D,B]} {5,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 26,
    label = "R3H_SS_12cy5",
    group = 
"""
1 *1 R!H u1 {2,S} {7,[S,D,B]}
2 *4 R!H u0 {1,S} {3,S} {5,[S,D,B]}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
5    R!H u0 {2,[S,D,B]} {6,[S,D,B]}
6    R!H u0 {5,[S,D,B]} {7,[S,D,B]}
7    R!H u0 {1,[S,D,B]} {6,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 27,
    label = "R3H_SS_23cy5",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S} {7,[S,D,B]}
3 *2 R!H u0 {2,S} {4,S} {5,[S,D,B]}
4 *3 H   u0 {3,S}
5    R!H u0 {3,[S,D,B]} {6,[S,D,B]}
6    R!H u0 {5,[S,D,B]} {7,[S,D,B]}
7    R!H u0 {2,[S,D,B]} {6,[S,D,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 28,
    label = "R3H_SD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *2 Cd  u0 {2,D} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 29,
    label = "R3H_ST",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *2 Ct  u0 {2,T} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 30,
    label = "R3H_SB",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cb  u0 {1,S} {3,B}
3 *2 Cb  u0 {2,B} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 31,
    label = "R3H_MS",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H u0 {1,[D,T,B]} {3,S}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 32,
    label = "R3H_DS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 33,
    label = "R3H_TS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 34,
    label = "R3H_BS",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cb  u0 {1,B} {3,S}
3 *2 R!H u0 {2,S} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 35,
    label = "R3H_BB",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *2 Cb  u0 {2,B} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 36,
    label = "R4Hall",
    group = 
"""
1 *1 R!H u1       {2,[S,D,T,B]}
2 *4 R!H u[0,1,2] {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H u[0,1,2] {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *2 R!H u0       {3,[S,D,T,B]} {5,S}
5 *3 H   u0       {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.561336, 'd13': 0.042229, 'd23': 0.032928},
        uncertainties = {'d12': 0.235434, 'd13': 0.053942, 'd23': 0.121146},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=56 label="R4H_BSD">, <Entry index=196 label="Cb_rad_out">, <Entry index=227 label="Cd_H_out_singleH">]
""",
)

entry(
    index = 37,
    label = "R4HJ_1",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u1 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *2 R!H u0 {3,[S,D,T,B]} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 38,
    label = "R4HJ_2",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H u1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *2 R!H u0 {3,[S,D,T,B]} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 39,
    label = "R4H",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *5 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *2 R!H u0 {3,[S,D,T,B]} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.561336, 'd13': 0.042229, 'd23': 0.032928},
        uncertainties = {'d12': 0.235434, 'd13': 0.053942, 'd23': 0.121146},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=56 label="R4H_BSD">, <Entry index=196 label="Cb_rad_out">, <Entry index=227 label="Cd_H_out_singleH">]
""",
)

entry(
    index = 40,
    label = "R4H_RSR",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *5 R!H u0 {2,S} {4,[S,D,T,B]}
4 *2 R!H u0 {3,[S,D,T,B]} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.561336, 'd13': 0.042229, 'd23': 0.032928},
        uncertainties = {'d12': 0.235434, 'd13': 0.053942, 'd23': 0.121146},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=56 label="R4H_BSD">, <Entry index=196 label="Cb_rad_out">, <Entry index=227 label="Cd_H_out_singleH">]
""",
)

entry(
    index = 41,
    label = "R4H_RSS",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.588763, 'd13': 0.041829, 'd23': 0.028935},
        uncertainties = {'d12': 0.78183, 'd13': 0.093741, 'd23': 0.311438},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
""",
)

entry(
    index = 42,
    label = "R4H_SSS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.588763, 'd13': 0.041829, 'd23': 0.028935},
        uncertainties = {'d12': 0.78183, 'd13': 0.093741, 'd23': 0.311438},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
""",
)

entry(
    index = 43,
    label = "R4H_SSS_CsSCsCs",
    group = 
"""
1 *1 Cs u1 {2,S}
2 *4 Ss u0 {1,S} {3,S}
3 *5 Cs u0 {2,S} {4,S}
4 *2 Cs u0 {3,S} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 44,
    label = "R4H_SSS_CsCsSCs",
    group = 
"""
1 *1 Cs u1 {2,S}
2 *4 Cs u0 {1,S} {3,S}
3 *5 Ss u0 {2,S} {4,S}
4 *2 Cs u0 {3,S} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 45,
    label = "R4H_SSS_OOCsCs",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *5 Cs u0 {2,S} {4,S}
4 *2 Cs u0 {3,S} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 46,
    label = "R4H_SSS_OO(Cs/Cs)Cs",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *5 Cs u0 {2,S} {4,S} {6,S}
4 *2 Cs u0 {3,S} {5,S}
5 *3 H  u0 {4,S}
6    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 47,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *5 Cs u0 {2,S} {4,S} {6,S} {7,S}
4 *2 Cs u0 {3,S} {5,S}
5 *3 H  u0 {4,S}
6    Cs u0 {3,S}
7    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 48,
    label = "R4H_SSS_OOCsCd",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *5 Cs u0 {2,S} {4,S}
4 *2 Cd u0 {3,S} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 49,
    label = "R4H_DSS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 50,
    label = "R4H_TSS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 51,
    label = "R4H_BSS",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cb  u0 {1,B} {3,S}
3 *5 R!H u0 {2,S} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 52,
    label = "R4H_RSD",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *5 Cd  u0 {2,S} {4,D}
4 *2 Cd  u0 {3,D} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.456197, 'd13': 0.043763, 'd23': 0.048232},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=56 label="R4H_BSD">, <Entry index=196 label="Cb_rad_out">, <Entry index=227 label="Cd_H_out_singleH">]
""",
)

entry(
    index = 53,
    label = "R4H_SSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 Cd  u0 {2,S} {4,D}
4 *2 Cd  u0 {3,D} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 54,
    label = "R4H_DSD",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *2 Cd u0 {3,D} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 55,
    label = "R4H_TSD",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *2 Cd u0 {3,D} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 56,
    label = "R4H_BSD",
    group = 
"""
1 *1 Cb u1 {2,B}
2 *4 Cb u0 {1,B} {3,S}
3 *5 Cd u0 {2,S} {4,D}
4 *2 Cd u0 {3,D} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.456197, 'd13': 0.043763, 'd23': 0.048232},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=56 label="R4H_BSD">, <Entry index=196 label="Cb_rad_out">, <Entry index=227 label="Cd_H_out_singleH">]
""",
)

entry(
    index = 57,
    label = "R4H_RST",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *5 Ct  u0 {2,S} {4,T}
4 *2 Ct  u0 {3,T} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 58,
    label = "R4H_SST",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 Ct  u0 {2,S} {4,T}
4 *2 Ct  u0 {3,T} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 59,
    label = "R4H_DST",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Ct u0 {2,S} {4,T}
4 *2 Ct u0 {3,T} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 60,
    label = "R4H_TST",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T} {3,S}
3 *5 Ct u0 {2,S} {4,T}
4 *2 Ct u0 {3,T} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 61,
    label = "R4H_BST",
    group = 
"""
1 *1 Cb u1 {2,B}
2 *4 Cb u0 {1,B} {3,S}
3 *5 Ct u0 {2,S} {4,T}
4 *2 Ct u0 {3,T} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 62,
    label = "R4H_RSB",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *5 Cb  u0 {2,S} {4,B}
4 *2 Cb  u0 {3,B} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 63,
    label = "R4H_SSB",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *5 Cb  u0 {2,S} {4,B}
4 *2 Cb  u0 {3,B} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 64,
    label = "R4H_DSB",
    group = 
"""
1 *1 Cd u1 {2,D}
2 *4 Cd u0 {1,D} {3,S}
3 *5 Cb u0 {2,S} {4,B}
4 *2 Cb u0 {3,B} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 65,
    label = "R4H_TSB",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T} {3,S}
3 *5 Cb u0 {2,S} {4,B}
4 *2 Cb u0 {3,B} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 66,
    label = "R4H_BSB",
    group = 
"""
1 *1 Cb u1 {2,B}
2 *4 Cb u0 {1,B} {3,S}
3 *5 Cb u0 {2,S} {4,B}
4 *2 Cb u0 {3,B} {5,S}
5 *3 H  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 67,
    label = "R4H_SMS",
    group = 
"""
1 *1 R!H        u1 {2,S}
2 *4 [Cd,Ct,Cb] u0 {1,S} {3,[D,T,B]}
3 *5 [Cd,Ct,Cb] u0 {2,[D,T,B]} {4,S}
4 *2 R!H        u0 {3,S} {5,S}
5 *3 H          u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 68,
    label = "R4H_SDS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cd  u0 {1,S} {3,D}
3 *5 Cd  u0 {2,D} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 69,
    label = "R4H_STS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Ct  u0 {1,S} {3,T}
3 *5 Ct  u0 {2,T} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 70,
    label = "R4H_SBS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cb  u0 {1,S} {3,B}
3 *5 Cb  u0 {2,B} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 71,
    label = "R4H_SBB",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cb  u0 {1,S} {3,B}
3 *5 Cbf u0 {2,B} {4,B}
4 *2 Cb  u0 {3,B} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 72,
    label = "R4H_BBS",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *5 Cb  u0 {2,B} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 73,
    label = "R4H_BBB",
    group = 
"""
1  *1 Cb       u1 {2,B} {15,B}
2  *4 Cbf      u0 {1,B} {3,B} {12,B}
3  *5 Cbf      u0 {2,B} {4,B} {9,B}
4  *2 Cb       u0 {3,B} {5,S} {6,B}
5  *3 H        u0 {4,S}
6     [Cb,Cbf] u0 {4,B} {7,B}
7     [Cb,Cbf] u0 {6,B} {8,B}
8     [Cb,Cbf] u0 {7,B} {9,B}
9     Cbf      u0 {3,B} {8,B} {10,B}
10    [Cb,Cbf] u0 {9,B} {11,B}
11    [Cb,Cbf] u0 {10,B} {12,B}
12    Cbf      u0 {2,B} {11,B} {13,B}
13    [Cb,Cbf] u0 {12,B} {14,B}
14    [Cb,Cbf] u0 {13,B} {15,B}
15    [Cb,Cbf] u0 {1,B} {14,B}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 74,
    label = "R5Hall",
    group = 
"""
1 *1 R!H u1       {2,[S,D,T,B]}
2 *4 R!H u[0,1,2] {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u[0,1,2] {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H u[0,1,2] {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *2 R!H u0       {4,[S,D,T,B]} {6,S}
6 *3 H   u0       {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.652208, 'd13': 0.047659, 'd23': -0.009719},
        uncertainties = {'d12': 1.49107, 'd13': 0.46283, 'd23': 0.298937},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
""",
)

entry(
    index = 75,
    label = "R5HJ_1",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u1 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 76,
    label = "R5HJ_2",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 77,
    label = "R5HJ_3",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H u1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 78,
    label = "R5H",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *5 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.652208, 'd13': 0.047659, 'd23': -0.009719},
        uncertainties = {'d12': 1.49107, 'd13': 0.46283, 'd23': 0.298937},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
""",
)

entry(
    index = 79,
    label = "R5H_RSSR",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.652208, 'd13': 0.047659, 'd23': -0.009719},
        uncertainties = {'d12': 1.49107, 'd13': 0.46283, 'd23': 0.298937},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
""",
)

entry(
    index = 80,
    label = "R5H_SSSR",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.652208, 'd13': 0.047659, 'd23': -0.009719},
        uncertainties = {'d12': 1.49107, 'd13': 0.46283, 'd23': 0.298937},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
""",
)

entry(
    index = 81,
    label = "R5H_SSSS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.652208, 'd13': 0.047659, 'd23': -0.009719},
        uncertainties = {'d12': 1.49107, 'd13': 0.46283, 'd23': 0.298937},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
""",
)

entry(
    index = 82,
    label = "R5H_CCCC_O",
    group = 
"""
1 *1 O u1 {2,S}
2 *4 C u0 {1,S} {3,S}
3 *6 C u0 {2,S} {4,S}
4 *5 C u0 {3,S} {5,S}
5 *2 C u0 {4,S} {6,S}
6 *3 H u0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.647088, 'd13': 0.030304, 'd23': -0.031534},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
""",
)

entry(
    index = 83,
    label = "R5H_SSSS_CsCsCsSCs",
    group = 
"""
1 *1 Cs u1 {2,S}
2 *4 Cs u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S}
4 *5 Ss u0 {3,S} {5,S}
5 *2 Cs u0 {4,S} {6,S}
6 *3 H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 84,
    label = "R5H_SSSS_OOCCC",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S}
4 *5 Cs u0 {3,S} {5,S}
5 *2 Cs u0 {4,S} {6,S}
6 *3 H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 85,
    label = "R5H_SSSS_OO(Cs/Cs)Cs",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S} {7,S}
4 *5 Cs u0 {3,S} {5,S}
5 *2 Cs u0 {4,S} {6,S}
6 *3 H  u0 {5,S}
7    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 86,
    label = "R5H_SSSS_OO(Cs/Cs/Cs)Cs",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S} {7,S} {8,S}
4 *5 Cs u0 {3,S} {5,S}
5 *2 Cs u0 {4,S} {6,S}
6 *3 H  u0 {5,S}
7    Cs u0 {3,S}
8    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 87,
    label = "R5H_SSSS_OOCs(Cs/Cs)",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S}
4 *5 Cs u0 {3,S} {5,S} {7,S}
5 *2 Cs u0 {4,S} {6,S}
6 *3 H  u0 {5,S}
7    Cs u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 88,
    label = "R5H_SSSS_OOCs(Cs/Cs/Cs)",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S}
4 *5 Cs u0 {3,S} {5,S} {7,S} {8,S}
5 *2 Cs u0 {4,S} {6,S}
6 *3 H  u0 {5,S}
7    Cs u0 {4,S}
8    Cs u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 89,
    label = "R5H_SSSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Cd  u0 {3,S} {5,D}
5 *2 Cd  u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 90,
    label = "R5H_SSST",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Ct  u0 {3,S} {5,T}
5 *2 Ct  u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 91,
    label = "R5H_SSSB",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Cb  u0 {3,S} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 92,
    label = "R5H_DSSR",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 93,
    label = "R5H_DSSS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 94,
    label = "R5H_DSSD",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Cd  u0 {3,S} {5,D}
5 *2 Cd  u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 95,
    label = "R5H_DSST",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Ct  u0 {3,S} {5,T}
5 *2 Ct  u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 96,
    label = "R5H_DSSB",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Cb  u0 {3,S} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 97,
    label = "R5H_TSSR",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 98,
    label = "R5H_TSSS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 99,
    label = "R5H_TSSD",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Cd  u0 {3,S} {5,D}
5 *2 Cd  u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 100,
    label = "R5H_TSST",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Ct  u0 {3,S} {5,T}
5 *2 Ct  u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 101,
    label = "R5H_TSSB",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Cb  u0 {3,S} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 102,
    label = "R5H_BSSR",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cb  u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 103,
    label = "R5H_BSSS",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cb  u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 104,
    label = "R5H_BSSD",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cb  u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Cd  u0 {3,S} {5,D}
5 *2 Cd  u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 105,
    label = "R5H_BSST",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cb  u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Ct  u0 {3,S} {5,T}
5 *2 Ct  u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 106,
    label = "R5H_BSSB",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cb  u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *5 Cb  u0 {3,S} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 107,
    label = "R5H_RSMS",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H u0 {2,S} {4,[D,T,B]}
4 *5 R!H u0 {3,[D,T,B]} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 108,
    label = "R5H_SSMS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,[D,T,B]}
4 *5 R!H u0 {3,[D,T,B]} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 109,
    label = "R5H_DSMS",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,[D,T,B]}
4 *5 R!H u0 {3,[D,T,B]} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 110,
    label = "R5H_TSMS",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,[D,T,B]}
4 *5 R!H u0 {3,[D,T,B]} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 111,
    label = "R5H_BSMS",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cb  u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,[D,T,B]}
4 *5 R!H u0 {3,[D,T,B]} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 112,
    label = "R5H_SMSR",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,[D,T,B]}
3 *6 R!H u0 {2,[D,T,B]} {4,S}
4 *5 R!H u0 {3,S} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 113,
    label = "R5H_SMSS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,[D,T,B]}
3 *6 R!H u0 {2,[D,T,B]} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 114,
    label = "R5H_SMSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,[D,T,B]}
3 *6 R!H u0 {2,[D,T,B]} {4,S}
4 *5 Cd  u0 {3,S} {5,D}
5 *2 Cd  u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 115,
    label = "R5H_SMST",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,[D,T,B]}
3 *6 R!H u0 {2,[D,T,B]} {4,S}
4 *5 Ct  u0 {3,S} {5,T}
5 *2 Ct  u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 116,
    label = "R5H_SMSB",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,[D,T,B]}
3 *6 R!H u0 {2,[D,T,B]} {4,S}
4 *5 Cb  u0 {3,S} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 117,
    label = "R5H_BBSR",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cb  u0 {2,B} {4,S}
4 *5 R!H u0 {3,S} {5,[S,D,T,B]}
5 *2 R!H u0 {4,[S,D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 118,
    label = "R5H_BBSS",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cb  u0 {2,B} {4,S}
4 *5 R!H u0 {3,S} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 119,
    label = "R5H_BBSD",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cb  u0 {2,B} {4,S}
4 *5 Cd  u0 {3,S} {5,D}
5 *2 Cd  u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 120,
    label = "R5H_BBST",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cb  u0 {2,B} {4,S}
4 *5 Ct  u0 {3,S} {5,T}
5 *2 Ct  u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 121,
    label = "R5H_BBSB",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cb  u0 {2,B} {4,S}
4 *5 Cb  u0 {3,S} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 122,
    label = "R5H_RSBB",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *6 Cb  u0 {2,S} {4,B}
4 *5 Cbf u0 {3,B} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 123,
    label = "R5H_SSBB",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 Cb  u0 {2,S} {4,B}
4 *5 Cbf u0 {3,B} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 124,
    label = "R5H_DSBB",
    group = 
"""
1 *1 Cd  u1 {2,D}
2 *4 Cd  u0 {1,D} {3,S}
3 *6 Cb  u0 {2,S} {4,B}
4 *5 Cbf u0 {3,B} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 125,
    label = "R5H_TSBB",
    group = 
"""
1 *1 Ct  u1 {2,T}
2 *4 Ct  u0 {1,T} {3,S}
3 *6 Cb  u0 {2,S} {4,B}
4 *5 Cbf u0 {3,B} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 126,
    label = "R5H_BSBB",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cb  u0 {1,B} {3,S}
3 *6 Cb  u0 {2,S} {4,B}
4 *5 Cbf u0 {3,B} {5,B}
5 *2 Cb  u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 127,
    label = "R5H_SBBS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cb  u0 {1,S} {3,B}
3 *6 Cbf u0 {2,B} {4,B}
4 *5 Cb  u0 {3,B} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 128,
    label = "R5H_SBBB",
    group = 
"""
1  *1 R!H      u1 {2,S}
2  *4 Cb       u0 {1,S} {3,B} {16,B}
3  *6 Cbf      u0 {2,B} {4,B} {13,B}
4  *5 Cbf      u0 {3,B} {5,B} {10,B}
5  *2 Cb       u0 {4,B} {6,S} {7,B}
6  *3 H        u0 {5,S}
7     [Cb,Cbf] u0 {5,B} {8,B}
8     [Cb,Cbf] u0 {7,B} {9,B}
9     [Cb,Cbf] u0 {8,B} {10,B}
10    Cbf      u0 {4,B} {9,B} {11,B}
11    [Cb,Cbf] u0 {10,B} {12,B}
12    [Cb,Cbf] u0 {11,B} {13,B}
13    Cbf      u0 {3,B} {12,B} {14,B}
14    [Cb,Cbf] u0 {13,B} {15,B}
15    [Cb,Cbf] u0 {14,B} {16,B}
16    [Cb,Cbf] u0 {2,B} {15,B}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 129,
    label = "R5H_BBBS",
    group = 
"""
1  *1 Cb       u1 {2,B} {16,B}
2  *4 Cbf      u0 {1,B} {3,B} {13,B}
3  *6 Cbf      u0 {2,B} {4,B} {10,B}
4  *5 Cb       u0 {3,B} {5,S} {7,B}
5  *2 R!H      u0 {4,S} {6,S}
6  *3 H        u0 {5,S}
7     [Cb,Cbf] u0 {4,B} {8,B}
8     [Cb,Cbf] u0 {7,B} {9,B}
9     [Cb,Cbf] u0 {8,B} {10,B}
10    Cbf      u0 {3,B} {9,B} {11,B}
11    [Cb,Cbf] u0 {10,B} {12,B}
12    [Cb,Cbf] u0 {11,B} {13,B}
13    Cbf      u0 {2,B} {12,B} {14,B}
14    [Cb,Cbf] u0 {13,B} {15,B}
15    [Cb,Cbf] u0 {14,B} {16,B}
16    [Cb,Cbf] u0 {1,B} {15,B}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 130,
    label = "R5H_BBBB",
    group = 
"""
1  *1 Cb       u1 {2,B} {19,B}
2  *4 Cbf      u0 {1,B} {3,B} {16,B}
3  *6 Cbf      u0 {2,B} {4,B} {13,B}
4  *5 Cbf      u0 {3,B} {5,B} {10,B}
5  *2 Cb       u0 {4,B} {6,S} {7,B}
6  *3 H        u0 {5,S}
7     [Cb,Cbf] u0 {5,B} {8,B}
8     [Cb,Cbf] u0 {7,B} {9,B}
9     [Cb,Cbf] u0 {8,B} {10,B}
10    Cbf      u0 {4,B} {9,B} {11,B}
11    [Cb,Cbf] u0 {10,B} {12,B}
12    [Cb,Cbf] u0 {11,B} {13,B}
13    Cbf      u0 {3,B} {12,B} {14,B}
14    [Cb,Cbf] u0 {13,B} {15,B}
15    [Cb,Cbf] u0 {14,B} {16,B}
16    Cbf      u0 {2,B} {15,B} {17,B}
17    [Cb,Cbf] u0 {16,B} {18,B}
18    [Cb,Cbf] u0 {17,B} {19,B}
19    [Cb,Cbf] u0 {1,B} {18,B}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 131,
    label = "R6Hall",
    group = 
"""
1 *1 R!H u1       {2,[S,D,T,B]}
2 *4 R!H u[0,1,2] {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u[0,1,2] {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u[0,1,2] {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H u[0,1,2] {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *2 R!H u0       {5,[S,D,T,B]} {7,S}
7 *3 H   u0       {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.598515, 'd13': 0.004658, 'd23': 0.018291},
        uncertainties = {'d12': 1.68294, 'd13': 0.075653, 'd23': 0.372031},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 132,
    label = "R6HJ_1",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u1 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 133,
    label = "R6HJ_2",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 134,
    label = "R6HJ_3",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 135,
    label = "R6HJ_4",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 136,
    label = "R6H",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *5 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.598515, 'd13': 0.004658, 'd23': 0.018291},
        uncertainties = {'d12': 1.68294, 'd13': 0.075653, 'd23': 0.372031},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 137,
    label = "R6H_RSSSR",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.598515, 'd13': 0.004658, 'd23': 0.018291},
        uncertainties = {'d12': 1.68294, 'd13': 0.075653, 'd23': 0.372031},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 138,
    label = "R6H_SSSSR",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.598515, 'd13': 0.004658, 'd23': 0.018291},
        uncertainties = {'d12': 1.68294, 'd13': 0.075653, 'd23': 0.372031},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 139,
    label = "R6H_SSSSS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.598515, 'd13': 0.004658, 'd23': 0.018291},
        uncertainties = {'d12': 1.68294, 'd13': 0.075653, 'd23': 0.372031},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 140,
    label = "R6H_SSSSS_OO",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S}
4 *7 Cs u0 {3,S} {5,S}
5 *5 Cs u0 {4,S} {6,S}
6 *2 Cs u0 {5,S} {7,S}
7 *3 H  u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 141,
    label = "R6H_SSSSS_OO(Cs/Cs)Cs",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S} {8,S}
4 *7 Cs u0 {3,S} {5,S}
5 *5 Cs u0 {4,S} {6,S}
6 *2 Cs u0 {5,S} {7,S}
7 *3 H  u0 {6,S}
8    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 144,
    label = "R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs)",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S} {8,S}
4 *7 Cs u0 {3,S} {5,S}
5 *5 Cs u0 {4,S} {6,S}
6 *2 Cs u0 {5,S} {7,S} {9,S}
7 *3 H  u0 {6,S}
8    Cs u0 {3,S}
9    Cs u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 143,
    label = "R6H_SSSSS_OOCCC(Cs/Cs)",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S}
4 *7 Cs u0 {3,S} {5,S}
5 *5 Cs u0 {4,S} {6,S}
6 *2 Cs u0 {5,S} {7,S} {8,S}
7 *3 H  u0 {6,S}
8    Cs u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 144,
    label = "R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs)",
    group = 
"""
1 *1 Os u1 {2,S}
2 *4 Os u0 {1,S} {3,S}
3 *6 Cs u0 {2,S} {4,S} {8,S}
4 *7 Cs u0 {3,S} {5,S}
5 *5 Cs u0 {4,S} {6,S}
6 *2 Cs u0 {5,S} {7,S} {9,S}
7 *3 H  u0 {6,S}
8    Cs u0 {3,S}
9    Cs u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 145,
    label = "R6H_SSSSS_bicyclopentane",
    group = 
"""
1  *1 R!H u1 {2,S} {8,S}
2  *4 R!H u0 {1,S} {3,S}
3  *6 R!H u0 {2,S} {4,S} {9,S}
4  *7 R!H u0 {3,S} {5,S} {11,S}
5  *5 R!H u0 {4,S} {6,S}
6  *2 R!H u0 {5,S} {7,S} {10,S}
7  *3 H   u0 {6,S}
8     C   u0 {1,S} {9,S}
9     C   u0 {3,S} {8,S}
10    C   u0 {6,S} {11,D}
11    C   u0 {4,S} {10,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 146,
    label = "R6H_SSSSD",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 147,
    label = "R6H_SSSST",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 148,
    label = "R6H_SSSSB",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 149,
    label = "R6H_DSSSR",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 150,
    label = "R6H_DSSSS",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 151,
    label = "R6H_DSSSD",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 152,
    label = "R6H_DSSST",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 153,
    label = "R6H_DSSSB",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H u0 {1,D} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 154,
    label = "R6H_TSSSR",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 155,
    label = "R6H_TSSSS",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 156,
    label = "R6H_TSSSD",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 157,
    label = "R6H_TSSST",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 158,
    label = "R6H_TSSSB",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H u0 {1,T} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 159,
    label = "R6H_BSSSR",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 160,
    label = "R6H_BSSSS",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 161,
    label = "R6H_BSSSD",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 162,
    label = "R6H_BSSST",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 163,
    label = "R6H_BSSSB",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H u0 {1,B} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 164,
    label = "R6H_RSSMS",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H u0 {2,S} {4,S}
4 *7 R!H u0 {3,S} {5,[D,T,B]}
5 *5 R!H u0 {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 165,
    label = "R6H_RSMSR",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *6 R!H u0 {2,S} {4,[D,T,B]}
4 *7 R!H u0 {3,[D,T,B]} {5,S}
5 *5 R!H u0 {4,S} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 166,
    label = "R6H_SMSSR",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,[D,T,B]}
3 *6 R!H u0 {2,[D,T,B]} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 167,
    label = "R6H_SMSMS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H u0 {1,S} {3,[D,T,B]}
3 *6 R!H u0 {2,[D,T,B]} {4,S}
4 *7 R!H u0 {3,S} {5,[D,T,B]}
5 *5 R!H u0 {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 168,
    label = "R6H_BBSRS",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cb  u0 {2,B} {4,S}
4 *7 R!H u0 {3,S} {5,[S,D,T,B]}
5 *5 R!H u0 {4,[S,D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 169,
    label = "R6H_BBSSM",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cb  u0 {2,B} {4,S}
4 *7 R!H u0 {3,S} {5,S}
5 *5 R!H u0 {4,S} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 170,
    label = "R6H_BBSBB",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cb  u0 {2,B} {4,S}
4 *7 Cb  u0 {3,S} {5,B}
5 *5 Cbf u0 {4,B} {6,B}
6 *2 Cb  u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 171,
    label = "R6H_SBBSR",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cb  u0 {1,S} {3,B}
3 *6 Cbf u0 {2,B} {4,B}
4 *7 Cb  u0 {3,B} {5,S}
5 *5 R!H u0 {4,S} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 172,
    label = "R6H_RSBBS",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *6 Cb  u0 {2,S} {4,B}
4 *7 Cbf u0 {3,B} {5,B}
5 *5 Cb  u0 {4,B} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 173,
    label = "R6H_BBBSR",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cbf u0 {2,B} {4,B}
4 *7 Cb  u0 {3,B} {5,S}
5 *5 R!H u0 {4,S} {6,[S,D,T,B]}
6 *2 R!H u0 {5,[S,D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 174,
    label = "R6H_SBBBS",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cb  u0 {1,S} {3,B}
3 *6 Cbf u0 {2,B} {4,B}
4 *7 Cbf u0 {3,B} {5,B}
5 *5 Cb  u0 {4,B} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 175,
    label = "R6H_RSBBB",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,S}
3 *6 Cb  u0 {2,S} {4,B}
4 *7 Cbf u0 {3,B} {5,B}
5 *5 Cbf u0 {4,B} {6,B}
6 *2 Cb  u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 176,
    label = "R6H_SBBBB",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 Cb  u0 {1,S} {3,B}
3 *6 Cbf u0 {2,B} {4,B}
4 *7 Cbf u0 {3,B} {5,B}
5 *5 Cbf u0 {4,B} {6,B}
6 *2 Cb  u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 177,
    label = "R6H_BBBBS",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cbf u0 {2,B} {4,B}
4 *7 Cbf u0 {3,B} {5,B}
5 *5 Cb  u0 {4,B} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 178,
    label = "R6H_BBBBB",
    group = 
"""
1 *1 Cb  u1 {2,B}
2 *4 Cbf u0 {1,B} {3,B}
3 *6 Cbf u0 {2,B} {4,B}
4 *7 Cbf u0 {3,B} {5,B}
5 *5 Cbf u0 {4,B} {6,B}
6 *2 Cb  u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 179,
    label = "R7Hall",
    group = 
"""
1 *1 R!H u1       {2,[S,D,T,B]}
2 *4 R!H u[0,1,2] {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u[0,1,2] {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u[0,1,2] {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H u[0,1,2] {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H u[0,1,2] {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *2 R!H u0       {6,[S,D,T,B]} {8,S}
8 *3 H   u0       {7,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.570201, 'd13': 0.012145, 'd23': -0.069444},
        uncertainties = {'d12': 0.404351, 'd13': 1.12597, 'd23': 1.00358},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=185 label="R7H">, <Entry index=200 label="C_rad_out_2H">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 180,
    label = "R7HJ_1",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u1 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *2 R!H u0 {6,[S,D,T,B]} {8,S}
8 *3 H   u0 {7,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 181,
    label = "R7HJ_2",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u1 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *2 R!H u0 {6,[S,D,T,B]} {8,S}
8 *3 H   u0 {7,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 182,
    label = "R7HJ_3",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u1 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *2 R!H u0 {6,[S,D,T,B]} {8,S}
8 *3 H   u0 {7,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 183,
    label = "R7HJ_4",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H u1 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *2 R!H u0 {6,[S,D,T,B]} {8,S}
8 *3 H   u0 {7,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 184,
    label = "R7HJ_5",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *2 R!H u0 {6,[S,D,T,B]} {8,S}
8 *3 H   u0 {7,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 185,
    label = "R7H",
    group = 
"""
1 *1 R!H u1 {2,[S,D,T,B]}
2 *4 R!H u0 {1,[S,D,T,B]} {3,[S,D,T,B]}
3 *6 R!H u0 {2,[S,D,T,B]} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *2 R!H u0 {6,[S,D,T,B]} {8,S}
8 *3 H   u0 {7,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.570201, 'd13': 0.012145, 'd23': -0.069444},
        uncertainties = {'d12': 0.404351, 'd13': 1.12597, 'd23': 1.00358},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 2 distances.
[<Entry index=185 label="R7H">, <Entry index=200 label="C_rad_out_2H">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 186,
    label = "R7H_OOCs4",
    group = 
"""
1 *1 Os  u1 {2,S}
2 *4 Os  u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *2 R!H u0 {6,[S,D,T,B]} {8,S}
8 *3 H   u0 {7,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 187,
    label = "R7H_OOCCCC(Cs/Cs)",
    group = 
"""
1 *1 Os  u1 {2,S}
2 *4 Os  u0 {1,S} {3,S}
3 *6 R!H u0 {2,S} {4,[S,D,T,B]}
4 *7 R!H u0 {3,[S,D,T,B]} {5,[S,D,T,B]}
5 *8 R!H u0 {4,[S,D,T,B]} {6,[S,D,T,B]}
6 *5 R!H u0 {5,[S,D,T,B]} {7,[S,D,T,B]}
7 *2 R!H u0 {6,[S,D,T,B]} {8,S} {9,S}
8 *3 H   u0 {7,S}
9    Cs  u0 {7,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 188,
    label = "O_rad_out",
    group = 
"""
1 *1 O u1
""",
    distances = DistanceData(
        distances = {'d12': -0.050945, 'd13': -0.062432, 'd23': -0.035422},
        uncertainties = {'d12': 0.377658, 'd13': 0.084014, 'd23': 0.062469},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=231 label="Cs_H_out_2H">]
""",
)

entry(
    index = 189,
    label = "S_rad_out",
    group = 
"""
1 *1 S u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 190,
    label = "Cd_rad_out_double",
    group = 
"""
1 *1 Cd u1 {2,D}
2    Cd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 191,
    label = "Cd_rad_out_single",
    group = 
"""
1 *1 Cd u1 {2,S}
2    R  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 192,
    label = "Cd_rad_out_singleH",
    group = 
"""
1 *1 Cd u1 {2,S}
2    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 193,
    label = "Cd_rad_out_singleNd",
    group = 
"""
1 *1 Cd       u1 {2,S}
2    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 194,
    label = "Cd_rad_out_singleDe",
    group = 
"""
1 *1 Cd            u1 {2,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 195,
    label = "Ct_rad_out",
    group = 
"""
1 *1 Ct u1 {2,T}
2 *4 Ct u0 {1,T}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 196,
    label = "Cb_rad_out",
    group = 
"""
1 *1 Cb       u1 {2,B}
2 *4 [Cb,Cbf] u0 {1,B}
""",
    distances = DistanceData(
        distances = {'d12': 0.046926, 'd13': 0.016122, 'd23': 0.031381},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=56 label="R4H_BSD">, <Entry index=196 label="Cb_rad_out">, <Entry index=227 label="Cd_H_out_singleH">]
""",
)

entry(
    index = 197,
    label = "CO_rad_out",
    group = 
"""
1 *1 C u1 {2,D}
2    O u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 198,
    label = "C=S_rad_out",
    group = 
"""
1 *1 Cd u1 {2,D}
2    Sd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 199,
    label = "C_rad_out_single",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    R u0 {1,S}
3    R u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.013492, 'd13': 0.019185, 'd23': 0.009461},
        uncertainties = {'d12': 0.192464, 'd13': 0.056422, 'd23': 0.052652},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=185 label="R7H">, <Entry index=200 label="C_rad_out_2H">, <Entry index=219 label="O_H_out">]
[<Entry index=16 label="R3H_SS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=219 label="O_H_out">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 200,
    label = "C_rad_out_2H",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    H u0 {1,S}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.004022, 'd13': 0.021964, 'd23': 0.011264},
        uncertainties = {'d12': 0.142907, 'd13': 0.065511, 'd23': 0.060408},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 11 distances.
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=185 label="R7H">, <Entry index=200 label="C_rad_out_2H">, <Entry index=219 label="O_H_out">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
""",
)

entry(
    index = 201,
    label = "C_rad_out_1H",
    group = 
"""
1 *1 C   u1 {2,S} {3,S}
2    H   u0 {1,S}
3    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.061032, 'd13': 0.008225, 'd23': 0.020636},
        uncertainties = {'d12': 0.472167, 'd13': 0.078882, 'd23': 0.056635},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=16 label="R3H_SS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=219 label="O_H_out">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
""",
)

entry(
    index = 202,
    label = "C_rad_out_H/NonDeC",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.061032, 'd13': 0.008225, 'd23': 0.020636},
        uncertainties = {'d12': 0.472167, 'd13': 0.078882, 'd23': 0.056635},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=16 label="R3H_SS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=219 label="O_H_out">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
""",
)

entry(
    index = 203,
    label = "C_rad_out_H/NonDeO",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    H u0 {1,S}
3    O u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 204,
    label = "C_rad_out_H/NonDeS",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    H u0 {1,S}
3    S u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 205,
    label = "C_rad_out_H/OneDe",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 206,
    label = "C_rad_out_noH",
    group = 
"""
1 *1 C   u1 {2,S} {3,S}
2    R!H u0 {1,S}
3    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.069981, 'd13': 0.027874, 'd23': -0.079383},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 207,
    label = "C_rad_out_NonDe",
    group = 
"""
1 *1 C        u1 {2,S} {3,S}
2    [Cs,O,S] u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.069981, 'd13': 0.027874, 'd23': -0.079383},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 208,
    label = "C_rad_out_Cs2",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cs u0 {1,S}
3    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.069981, 'd13': 0.027874, 'd23': -0.079383},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 209,
    label = "C_rad_out_Cs2_cy3",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cs u0 {1,S} {3,S}
3    Cs u0 {1,S} {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 210,
    label = "C_rad_out_Cs2_cy4",
    group = 
"""
1 *1 C       u1 {2,S} {3,S}
2    Cs      u0 {1,S} {4,S}
3    Cs      u0 {1,S} {4,S}
4    [Cs,Cd] u0 {2,S} {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 211,
    label = "C_rad_out_Cs2_cy5",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    Cs            u0 {1,S} {4,S}
3    Cs            u0 {1,S} {5,S}
4    [Cs,Cd,Cb,Ct] u0 {2,S} {5,[S,D,T,B]}
5    [Cs,Cd,Cb,Ct] u0 {3,S} {4,[S,D,T,B]}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 212,
    label = "C_rad_out_NDMustO",
    group = 
"""
1 *1 C        u1 {2,S} {3,S}
2    O        u0 {1,S}
3    [Cs,O,S] u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 213,
    label = "C_rad_out_OneDe",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cs,O,S]      u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 214,
    label = "C_rad_out_OneDe/Cs",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    Cs            u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 215,
    label = "C_rad_out_OneDe/O",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    O             u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 216,
    label = "C_rad_out_OneDe/S",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    S             u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 217,
    label = "C_rad_out_TwoDe",
    group = 
"""
1 *1 C             u1 {2,S} {3,S}
2    [Cd,Ct,Cb,CO] u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 218,
    label = "CO_H_out",
    group = 
"""
1 *2 CO u0 {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 219,
    label = "O_H_out",
    group = 
"""
1 *2 O u0 {2,S}
2 *3 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.04651, 'd13': -0.011217, 'd23': -0.064501},
        uncertainties = {'d12': 0.477892, 'd13': 0.17786, 'd23': 0.162146},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 4 distances.
[<Entry index=16 label="R3H_SS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=219 label="O_H_out">]
[<Entry index=139 label="R6H_SSSSS">, <Entry index=208 label="C_rad_out_Cs2">, <Entry index=219 label="O_H_out">]
[<Entry index=185 label="R7H">, <Entry index=200 label="C_rad_out_2H">, <Entry index=219 label="O_H_out">]
""",
)

entry(
    index = 220,
    label = "Ct_H_out",
    group = 
"""
1 *2 Ct u0 {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 221,
    label = "Cb_H_out",
    group = 
"""
1 *2 Cb u0 {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 222,
    label = "S_H_out",
    group = 
"""
1 *2 S u0 {2,S}
2 *3 H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 223,
    label = "Cd_H_out_double",
    group = 
"""
1 *2 Cd     u0 {2,S} {3,D}
2 *3 H      u0 {1,S}
3    [Cd,O] u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 224,
    label = "Cd_H_out_doubleC",
    group = 
"""
1 *2 Cd u0 {2,S} {3,D}
2 *3 H  u0 {1,S}
3    Cd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 225,
    label = "Cd_H_out_doubleO",
    group = 
"""
1 *2 Cd u0 {2,S} {3,D}
2 *3 H  u0 {1,S}
3    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 226,
    label = "Cd_H_out_single",
    group = 
"""
1 *2 Cd u0 {2,S} {3,S}
2 *3 H  u0 {1,S}
3    R  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.070389, 'd13': 0.024183, 'd23': 0.047072},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=56 label="R4H_BSD">, <Entry index=196 label="Cb_rad_out">, <Entry index=227 label="Cd_H_out_singleH">]
""",
)

entry(
    index = 227,
    label = "Cd_H_out_singleH",
    group = 
"""
1 *2 Cd u0 {2,S} {3,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.070389, 'd13': 0.024183, 'd23': 0.047072},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=56 label="R4H_BSD">, <Entry index=196 label="Cb_rad_out">, <Entry index=227 label="Cd_H_out_singleH">]
""",
)

entry(
    index = 228,
    label = "Cd_H_out_singleNd",
    group = 
"""
1 *2 Cd     u0 {2,S} {3,S}
2 *3 H      u0 {1,S}
3    [Cs,O] u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 229,
    label = "Cd_H_out_singleDe",
    group = 
"""
1 *2 Cd            u0 {2,S} {3,S}
2 *3 H             u0 {1,S}
3    [Cd,Ct,Cb,CO] u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 230,
    label = "Cs_H_out",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    R  u0 {1,S}
4    R  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01797, 'd13': 0.002119, 'd23': 0.017136},
        uncertainties = {'d12': 0.171316, 'd13': 0.031284, 'd23': 0.027634},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 16 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
""",
)

entry(
    index = 231,
    label = "Cs_H_out_2H",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.117045, 'd13': -0.000867, 'd23': 0.039314},
        uncertainties = {'d12': 0.686449, 'd13': 0.085984, 'd23': 0.03788},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=139 label="R6H_SSSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=231 label="Cs_H_out_2H">]
[<Entry index=81 label="R5H_SSSS">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=231 label="Cs_H_out_2H">]
""",
)

entry(
    index = 232,
    label = "Cs_H_out_2H/NonDeC",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 233,
    label = "Cs_H_out_1H",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S}
2 *3 H   u0 {1,S}
3    R!H u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.062333, 'd13': 0.00468, 'd23': 0.012576},
        uncertainties = {'d12': 0.129148, 'd13': 0.02795, 'd23': 0.031651},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 10 distances.
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
""",
)

entry(
    index = 234,
    label = "Cs_H_out_H/NonDeC",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.055239, 'd13': -0.000499, 'd23': 0.01725},
        uncertainties = {'d12': 0.107463, 'd13': 0.030202, 'd23': 0.034208},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 9 distances.
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=42 label="R4H_SSS">, <Entry index=188 label="O_rad_out">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=202 label="C_rad_out_H/NonDeC">, <Entry index=234 label="Cs_H_out_H/NonDeC">]
""",
)

entry(
    index = 235,
    label = "Cs_H_out_H/(NonDeC/Cs)",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S} {5,S}
4    H  u0 {1,S}
5    Cs u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.030417, 'd13': 0.004217, 'd23': 0.025734},
        uncertainties = {'d12': 0.136107, 'd13': 0.040551, 'd23': 0.036033},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 6 distances.
[<Entry index=16 label="R3H_SS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=42 label="R4H_SSS">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
[<Entry index=6 label="R2H_S">, <Entry index=188 label="O_rad_out">, <Entry index=235 label="Cs_H_out_H/(NonDeC/Cs)">]
""",
)

entry(
    index = 237,
    label = "Cs_H_out_H/(NonDeC/Cs/Cs)",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S} {5,S} {6,S}
4    H  u0 {1,S}
5    Cs u0 {3,S}
6    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 238,
    label = "Cs_H_out_H/(NonDeC/Cs/Cs/Cs)",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S} {5,S} {6,S} {7,S}
4    H  u0 {1,S}
5    Cs u0 {3,S}
6    Cs u0 {3,S}
7    Cs u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 239,
    label = "Cs_H_out_H/(NonDeC/O)",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S} {5,S}
4    H  u0 {1,S}
5    O  u0 {3,S} {6,S}
6    H  u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 240,
    label = "Cs_H_out_H/NonDeO",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    O  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 241,
    label = "Cs_H_out_OOH/H",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S} {5,S}
5    O  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 242,
    label = "Cs_H_out_H/NonDeS",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    S  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 243,
    label = "Cs_H_out_H/OneDe",
    group = 
"""
1 *2 Cs            u0 {2,S} {3,S} {4,S}
2 *3 H             u0 {1,S}
3    [Cd,Ct,CS,CO] u0 {1,S}
4    H             u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.131499, 'd13': 0.055176, 'd23': -0.032992},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
""",
)

entry(
    index = 244,
    label = "Cs_H_out_H/Ct",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Ct u0 {1,S} {5,T}
4    H  u0 {1,S}
5    C  u0 {3,T} {6,S}
6    R  u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 245,
    label = "Cs_H_out_H/CO",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    CO u0 {1,S} {5,D} {6,S}
4    H  u0 {1,S}
5    O  u0 {3,D}
6    R  u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 246,
    label = "Cs_H_out_H/CS",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    CS u0 {1,S} {5,D} {6,S}
4    H  u0 {1,S}
5    S  u0 {3,D}
6    R  u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 247,
    label = "Cs_H_out_H/Cd",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd u0 {1,S} {5,D} {6,S}
4    H  u0 {1,S}
5    C  u0 {3,D} {7,S} {8,S}
6    R  u0 {3,S}
7    R  u0 {5,S}
8    R  u0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.131499, 'd13': 0.055176, 'd23': -0.032992},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=247 label="Cs_H_out_H/Cd">]
""",
)

entry(
    index = 248,
    label = "Cs_H_out_noH",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S} {4,S}
2 *3 H   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.06634, 'd13': -0.002174, 'd23': -7.1e-05},
        uncertainties = {'d12': 0.392727, 'd13': 0.099, 'd23': 0.074794},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
""",
)

entry(
    index = 249,
    label = "Cs_H_out_NonDe",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S}
2 *3 H      u0 {1,S}
3    [Cs,O] u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.06634, 'd13': -0.002174, 'd23': -7.1e-05},
        uncertainties = {'d12': 0.392727, 'd13': 0.099, 'd23': 0.074794},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
""",
)

entry(
    index = 250,
    label = "Cs_H_out_Cs2",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S}
4    Cs u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.06634, 'd13': -0.002174, 'd23': -7.1e-05},
        uncertainties = {'d12': 0.392727, 'd13': 0.099, 'd23': 0.074794},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 3 distances.
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=250 label="Cs_H_out_Cs2">]
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
[<Entry index=82 label="R5H_CCCC_O">, <Entry index=188 label="O_rad_out">, <Entry index=250 label="Cs_H_out_Cs2">]
""",
)

entry(
    index = 251,
    label = "Cs_H_out_Cs2_cy3",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S} {4,S}
4    Cs u0 {1,S} {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 252,
    label = "Cs_H_out_Cs2_cy4",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {1,S} {5,S}
5    Cs u0 {3,S} {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 253,
    label = "Cs_H_out_Cs2_cy5",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S} {5,S}
4    Cs u0 {1,S} {6,S}
5    Cs u0 {3,S} {6,S}
6    Cs u0 {4,S} {5,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.135882, 'd13': 0.005017, 'd23': 0.005687},
        uncertainties = {},
    ),
    shortDesc = u"""Group additive distances.""",
    longDesc = 
u"""
Fitted to 1 distances.
[<Entry index=6 label="R2H_S">, <Entry index=200 label="C_rad_out_2H">, <Entry index=253 label="Cs_H_out_Cs2_cy5">]
""",
)

entry(
    index = 254,
    label = "Cs_H_out_NDMustO",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S}
2 *3 H      u0 {1,S}
3    O      u0 {1,S}
4    [Cs,O] u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 255,
    label = "Cs_H_out_OneDe",
    group = "OR{Cs_H_out_Cd, Cs_H_out_Ct, Cs_H_out_CO, Cs_H_out_CS}",
    distances = DistanceData(distances={}),
)

entry(
    index = 256,
    label = "Cs_H_out_Ct",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S}
2 *3 H      u0 {1,S}
3    C      u0 {1,S} {5,T}
4    [Cs,O] u0 {1,S}
5    C      u0 {3,T} {6,S}
6    R      u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 257,
    label = "Cs_H_out_CO",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S}
2 *3 H      u0 {1,S}
3    C      u0 {1,S} {5,D} {6,S}
4    [Cs,O] u0 {1,S}
5    O      u0 {3,D}
6    R      u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 258,
    label = "Cs_H_out_CS",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S}
2 *3 H      u0 {1,S}
3    C      u0 {1,S} {5,D} {6,S}
4    [Cs,O] u0 {1,S}
5    S      u0 {3,D}
6    R      u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 259,
    label = "Cs_H_out_Cd",
    group = 
"""
1 *2 Cs     u0 {2,S} {3,S} {4,S}
2 *3 H      u0 {1,S}
3    C      u0 {1,S} {5,D} {6,S}
4    [Cs,O] u0 {1,S}
5    C      u0 {3,D} {7,S} {8,S}
6    R      u0 {3,S}
7    R      u0 {5,S}
8    R      u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 260,
    label = "Cs_H_out_TwoDe",
    group = "OR{Cs_H_out_CdCd, Cs_H_out_CdCt, Cs_H_out_CtCt}",
    distances = DistanceData(distances={}),
)

entry(
    index = 261,
    label = "Cs_H_out_CtCt",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    C  u0 {1,S} {5,T}
4    C  u0 {1,S} {7,T}
5    C  u0 {3,T} {6,S}
6    R  u0 {5,S}
7    C  u0 {4,T} {8,S}
8    R  u0 {7,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 262,
    label = "Cs_H_out_CdCt",
    group = 
"""
1  *2 Cs u0 {2,S} {3,S} {4,S}
2  *3 H  u0 {1,S}
3     C  u0 {1,S} {5,D} {9,S}
4     C  u0 {1,S} {7,T}
5     C  u0 {3,D} {6,S} {10,S}
6     R  u0 {5,S}
7     C  u0 {4,T} {8,S}
8     C  u0 {7,S}
9     R  u0 {3,S}
10    R  u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 263,
    label = "Cs_H_out_CdCd",
    group = 
"""
1  *2 Cs u0 {2,S} {3,S} {4,S}
2  *3 H  u0 {1,S}
3     C  u0 {1,S} {5,D} {9,S}
4     C  u0 {1,S} {7,D} {10,S}
5     C  u0 {3,D} {6,S} {11,S}
6     R  u0 {5,S}
7     C  u0 {4,D} {8,S} {12,S}
8     C  u0 {7,S}
9     R  u0 {3,S}
10    R  u0 {4,S}
11    R  u0 {5,S}
12    R  u0 {7,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 264,
    label = "Cs_H_out_OOH",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    R  u0 {1,S}
4    O  u0 {1,S} {5,S}
5    O  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 265,
    label = "Cs_H_out_OOH/Cs",
    group = 
"""
1 *2 Cs u0 {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs u0 {1,S}
4    O  u0 {1,S} {5,S}
5    O  u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

tree(
"""
L1: RnH
    L2: R2Hall
        L3: R2H
            L4: R2H_S
                L5: R2H_S_cy3
                L5: R2H_S_cy4
                L5: R2H_S_cy5
            L4: R2H_D
            L4: R2H_B
    L2: R3Hall
        L3: R3HJ
        L3: R3H
            L4: R3H_SR
                L5: R3H_SS
                    L6: R3H_SS_2Cd
                    L6: R3H_SS_OOCs
                    L6: R3H_SS_S
                    L6: R3H_SS_12cy3
                    L6: R3H_SS_23cy3
                    L6: R3H_SS_13cy4
                    L6: R3H_SS_12cy4
                    L6: R3H_SS_23cy4
                    L6: R3H_SS_13cy5
                    L6: R3H_SS_12cy5
                    L6: R3H_SS_23cy5
                L5: R3H_SD
                L5: R3H_ST
                L5: R3H_SB
            L4: R3H_MS
                L5: R3H_DS
                L5: R3H_TS
                L5: R3H_BS
            L4: R3H_BB
    L2: R4Hall
        L3: R4HJ_1
        L3: R4HJ_2
        L3: R4H
            L4: R4H_RSR
                L5: R4H_RSS
                    L6: R4H_SSS
                        L7: R4H_SSS_CsSCsCs
                        L7: R4H_SSS_CsCsSCs
                        L7: R4H_SSS_OOCsCs
                            L8: R4H_SSS_OO(Cs/Cs)Cs
                                L9: R4H_SSS_OO(Cs/Cs/Cs)Cs
                        L7: R4H_SSS_OOCsCd
                    L6: R4H_DSS
                    L6: R4H_TSS
                    L6: R4H_BSS
                L5: R4H_RSD
                    L6: R4H_SSD
                    L6: R4H_DSD
                    L6: R4H_TSD
                    L6: R4H_BSD
                L5: R4H_RST
                    L6: R4H_SST
                    L6: R4H_DST
                    L6: R4H_TST
                    L6: R4H_BST
                L5: R4H_RSB
                    L6: R4H_SSB
                    L6: R4H_DSB
                    L6: R4H_TSB
                    L6: R4H_BSB
            L4: R4H_SMS
                L5: R4H_SDS
                L5: R4H_STS
                L5: R4H_SBS
            L4: R4H_SBB
            L4: R4H_BBS
            L4: R4H_BBB
    L2: R5Hall
        L3: R5HJ_1
        L3: R5HJ_2
        L3: R5HJ_3
        L3: R5H
            L4: R5H_RSSR
                L5: R5H_SSSR
                    L6: R5H_SSSS
                        L7: R5H_CCCC_O
                        L7: R5H_SSSS_CsCsCsSCs
                        L7: R5H_SSSS_OOCCC
                            L8: R5H_SSSS_OO(Cs/Cs)Cs
                                L9: R5H_SSSS_OO(Cs/Cs/Cs)Cs
                            L8: R5H_SSSS_OOCs(Cs/Cs)
                                L9: R5H_SSSS_OOCs(Cs/Cs/Cs)
                    L6: R5H_SSSD
                    L6: R5H_SSST
                    L6: R5H_SSSB
                L5: R5H_DSSR
                    L6: R5H_DSSS
                    L6: R5H_DSSD
                    L6: R5H_DSST
                    L6: R5H_DSSB
                L5: R5H_TSSR
                    L6: R5H_TSSS
                    L6: R5H_TSSD
                    L6: R5H_TSST
                    L6: R5H_TSSB
                L5: R5H_BSSR
                    L6: R5H_BSSS
                    L6: R5H_BSSD
                    L6: R5H_BSST
                    L6: R5H_BSSB
            L4: R5H_RSMS
                L5: R5H_SSMS
                L5: R5H_DSMS
                L5: R5H_TSMS
                L5: R5H_BSMS
            L4: R5H_SMSR
                L5: R5H_SMSS
                L5: R5H_SMSD
                L5: R5H_SMST
                L5: R5H_SMSB
            L4: R5H_BBSR
                L5: R5H_BBSS
                L5: R5H_BBSD
                L5: R5H_BBST
                L5: R5H_BBSB
            L4: R5H_RSBB
                L5: R5H_SSBB
                L5: R5H_DSBB
                L5: R5H_TSBB
                L5: R5H_BSBB
            L4: R5H_SBBS
            L4: R5H_SBBB
            L4: R5H_BBBS
            L4: R5H_BBBB
    L2: R6Hall
        L3: R6HJ_1
        L3: R6HJ_2
        L3: R6HJ_3
        L3: R6HJ_4
        L3: R6H
            L4: R6H_RSSSR
                L5: R6H_SSSSR
                    L6: R6H_SSSSS
                        L7: R6H_SSSSS_OO
                            L8: R6H_SSSSS_OO(Cs/Cs)Cs
                                L9: R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs)
                            L8: R6H_SSSSS_OOCCC(Cs/Cs)
                                L9: R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs)
                        L7: R6H_SSSSS_bicyclopentane
                    L6: R6H_SSSSD
                    L6: R6H_SSSST
                    L6: R6H_SSSSB
                L5: R6H_DSSSR
                    L6: R6H_DSSSS
                    L6: R6H_DSSSD
                    L6: R6H_DSSST
                    L6: R6H_DSSSB
                L5: R6H_TSSSR
                    L6: R6H_TSSSS
                    L6: R6H_TSSSD
                    L6: R6H_TSSST
                    L6: R6H_TSSSB
                L5: R6H_BSSSR
                    L6: R6H_BSSSS
                    L6: R6H_BSSSD
                    L6: R6H_BSSST
                    L6: R6H_BSSSB
            L4: R6H_RSSMS
            L4: R6H_RSMSR
            L4: R6H_SMSSR
            L4: R6H_SMSMS
            L4: R6H_BBSRS
            L4: R6H_BBSSM
            L4: R6H_BBSBB
            L4: R6H_SBBSR
            L4: R6H_RSBBS
            L4: R6H_BBBSR
            L4: R6H_SBBBS
            L4: R6H_RSBBB
            L4: R6H_SBBBB
            L4: R6H_BBBBS
            L4: R6H_BBBBB
    L2: R7Hall
        L3: R7HJ_1
        L3: R7HJ_2
        L3: R7HJ_3
        L3: R7HJ_4
        L3: R7HJ_5
        L3: R7H
            L4: R7H_OOCs4
                L5: R7H_OOCCCC(Cs/Cs)
L1: Y_rad_out
    L2: O_rad_out
    L2: S_rad_out
    L2: Cd_rad_out_double
    L2: Cd_rad_out_single
        L3: Cd_rad_out_singleH
        L3: Cd_rad_out_singleNd
        L3: Cd_rad_out_singleDe
    L2: Ct_rad_out
    L2: Cb_rad_out
    L2: CO_rad_out
    L2: C=S_rad_out
    L2: C_rad_out_single
        L3: C_rad_out_2H
        L3: C_rad_out_1H
            L4: C_rad_out_H/NonDeC
            L4: C_rad_out_H/NonDeO
            L4: C_rad_out_H/NonDeS
            L4: C_rad_out_H/OneDe
        L3: C_rad_out_noH
            L4: C_rad_out_NonDe
                L5: C_rad_out_Cs2
                    L6: C_rad_out_Cs2_cy3
                    L6: C_rad_out_Cs2_cy4
                    L6: C_rad_out_Cs2_cy5
                L5: C_rad_out_NDMustO
            L4: C_rad_out_OneDe
                L5: C_rad_out_OneDe/Cs
                L5: C_rad_out_OneDe/O
                L5: C_rad_out_OneDe/S
            L4: C_rad_out_TwoDe
L1: XH_out
    L2: CO_H_out
    L2: O_H_out
    L2: Ct_H_out
    L2: Cb_H_out
    L2: S_H_out
    L2: Cd_H_out_double
        L3: Cd_H_out_doubleC
        L3: Cd_H_out_doubleO
    L2: Cd_H_out_single
        L3: Cd_H_out_singleH
        L3: Cd_H_out_singleNd
        L3: Cd_H_out_singleDe
    L2: Cs_H_out
        L3: Cs_H_out_2H
            L4: Cs_H_out_2H/NonDeC
        L3: Cs_H_out_1H
            L4: Cs_H_out_H/NonDeC
                L5: Cs_H_out_H/(NonDeC/Cs)
                    L6: Cs_H_out_H/(NonDeC/Cs/Cs)
                        L7: Cs_H_out_H/(NonDeC/Cs/Cs/Cs)
                L5: Cs_H_out_H/(NonDeC/O)
            L4: Cs_H_out_H/NonDeO
                L5: Cs_H_out_OOH/H
            L4: Cs_H_out_H/NonDeS
            L4: Cs_H_out_H/OneDe
                L5: Cs_H_out_H/Ct
                L5: Cs_H_out_H/CO
                L5: Cs_H_out_H/CS
                L5: Cs_H_out_H/Cd
        L3: Cs_H_out_noH
            L4: Cs_H_out_NonDe
                L5: Cs_H_out_Cs2
                    L6: Cs_H_out_Cs2_cy3
                    L6: Cs_H_out_Cs2_cy4
                    L6: Cs_H_out_Cs2_cy5
                L5: Cs_H_out_NDMustO
            L4: Cs_H_out_OneDe
                L5: Cs_H_out_Ct
                L5: Cs_H_out_CO
                L5: Cs_H_out_CS
                L5: Cs_H_out_Cd
            L4: Cs_H_out_TwoDe
                L5: Cs_H_out_CtCt
                L5: Cs_H_out_CdCt
                L5: Cs_H_out_CdCd
        L3: Cs_H_out_OOH
            L4: Cs_H_out_OOH/Cs
"""
)

