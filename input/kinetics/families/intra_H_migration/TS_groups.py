#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/TS_groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "RnH",
    group = "OR{R2Hall, R2Hall, R3Hall, R4Hall, R5Hall, R6Hall, R7Hall}",
    distances = DistanceData(
        distances = {'d12': 1.68607, 'd13': 1.30701, 'd23': 1.68632},
        uncertainties = {'d12': 0.83158, 'd13': 0.093271, 'd23': 0.816009},
    ),
    shortDesc = u"""Fitted to 86 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=15 label="Cdj_out">, <Entry index=23 label="Cb_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=4 label="R2Hall">, <Entry index=27 label="Cdj_out_Cd">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=12 label="C_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=21 label="Cd_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=10 label="Cj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=17 label="Cbj_out">, <Entry index=21 label="Cd_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=9 label="R7Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
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
    label = "X_H_out",
    group = 
"""
1 *2 R!H ux {2,S}
2 *3 H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 4,
    label = "R2Hall",
    group = 
"""
1 *2 R!H u0 {2,[S,D,T,B]} {3,S}
2 *1 R!H u1 {1,[S,D,T,B]}
3 *3 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.292487, 'd13': -0.010846, 'd23': -0.281721},
        uncertainties = {'d12': 0.239553, 'd13': 0.090382, 'd23': 0.234623},
    ),
    shortDesc = u"""Fitted to 32 distances.
""",
    longDesc = 
u"""
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=12 label="C_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=21 label="Cd_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=4 label="R2Hall">, <Entry index=10 label="Cj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=27 label="Cdj_out_Cd">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 5,
    label = "R3Hall",
    group = 
"""
1 *4 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *2 R!H u0 {1,[S,D,T,B]} {4,S}
3 *1 R!H u1 {1,[S,D,T,B]}
4 *3 H   u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.053016, 'd13': 0.051722, 'd23': 0.081089},
        uncertainties = {'d12': 1.21326, 'd13': 0.055772, 'd23': 1.17354},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 6,
    label = "R4Hall",
    group = 
"""
1 *5 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *4 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
3 *2 R!H u0 {1,[S,D,T,B]} {5,S}
4 *1 R!H u1 {2,[S,D,T,B]}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.248769, 'd13': 0.022582, 'd23': 0.219285},
        uncertainties = {'d12': 0.803278, 'd13': 0.085499, 'd23': 0.794082},
    ),
    shortDesc = u"""Fitted to 20 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=15 label="Cdj_out">, <Entry index=23 label="Cb_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=17 label="Cbj_out">, <Entry index=21 label="Cd_H_out">]
""",
)

entry(
    index = 7,
    label = "R5Hall",
    group = 
"""
1 *6 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *5 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
3 *4 R!H ux {1,[S,D,T,B]} {5,[S,D,T,B]}
4 *2 R!H u0 {2,[S,D,T,B]} {6,S}
5 *1 R!H u1 {3,[S,D,T,B]}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.276387, 'd13': -0.02368, 'd23': 0.222369},
        uncertainties = {'d12': 1.06105, 'd13': 0.109201, 'd23': 1.0271},
    ),
    shortDesc = u"""Fitted to 18 distances.
""",
    longDesc = 
u"""
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 8,
    label = "R6Hall",
    group = 
"""
1 *7 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *6 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
3 *5 R!H ux {1,[S,D,T,B]} {5,[S,D,T,B]}
4 *4 R!H ux {2,[S,D,T,B]} {6,[S,D,T,B]}
5 *2 R!H u0 {3,[S,D,T,B]} {7,S}
6 *1 R!H u1 {4,[S,D,T,B]}
7 *3 H   u0 {5,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.232765, 'd13': -0.016807, 'd23': 0.288109},
        uncertainties = {'d12': 2.08011, 'd13': 0.189356, 'd23': 2.05129},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=8 label="R6Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 9,
    label = "R7Hall",
    group = 
"""
1 *7 R!H ux {2,[S,D,T,B]} {3,[S,D,T,B]}
2 *8 R!H ux {1,[S,D,T,B]} {4,[S,D,T,B]}
3 *6 R!H ux {1,[S,D,T,B]} {5,[S,D,T,B]}
4 *5 R!H ux {2,[S,D,T,B]} {6,[S,D,T,B]}
5 *4 R!H ux {3,[S,D,T,B]} {7,[S,D,T,B]}
6 *2 R!H u0 {4,[S,D,T,B]} {8,S}
7 *1 R!H u1 {5,[S,D,T,B]}
8 *3 H   u0 {6,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.06217, 'd13': 0.051123, 'd23': 0.253889},
        uncertainties = {'d12': 3.15857, 'd13': 0.256186, 'd23': 3.13824},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=9 label="R7Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 10,
    label = "Cj_out",
    group = 
"""
1 *1 C u1
""",
    distances = DistanceData(
        distances = {'d12': -0.072611, 'd13': 0.026008, 'd23': 0.040976},
        uncertainties = {'d12': 0.809385, 'd13': 0.089209, 'd23': 0.802072},
    ),
    shortDesc = u"""Fitted to 66 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=15 label="Cdj_out">, <Entry index=23 label="Cb_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=4 label="R2Hall">, <Entry index=27 label="Cdj_out_Cd">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=9 label="R7Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=12 label="C_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=21 label="Cd_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=10 label="Cj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=17 label="Cbj_out">, <Entry index=21 label="Cd_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
""",
)

entry(
    index = 14,
    label = "Csj_out",
    group = 
"""
1 *1 Cs u1
""",
    distances = DistanceData(
        distances = {'d12': -0.073527, 'd13': 0.023993, 'd23': 0.047117},
        uncertainties = {'d12': 0.832956, 'd13': 0.087133, 'd23': 0.827368},
    ),
    shortDesc = u"""Fitted to 62 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=9 label="R7Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=12 label="C_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=21 label="Cd_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 24,
    label = "Csj_out_2H",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 17 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=9 label="R7Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=31 label="Cs_H_out_1H">]
""",
)

entry(
    index = 35,
    label = "Csj_out_CHH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 17 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=9 label="R7Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=35 label="Csj_out_CHH">, <Entry index=31 label="Cs_H_out_1H">]
""",
)

entry(
    index = 36,
    label = "Csj_out_OHH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    O  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 25,
    label = "Csj_out_1H",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=5 label="R3Hall">, <Entry index=38 label="Csj_out_COH">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=5 label="R3Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 37,
    label = "Csj_out_CCH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="R6Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=5 label="R3Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=13 label="O_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=37 label="Csj_out_CCH">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 38,
    label = "Csj_out_COH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=5 label="R3Hall">, <Entry index=38 label="Csj_out_COH">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 39,
    label = "Csj_out_OOH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    O  u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 26,
    label = "Csj_out_noH",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 11 distances.
""",
    longDesc = 
u"""
[<Entry index=7 label="R5Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=41 label="Csj_out_CCO">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=13 label="O_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=41 label="Csj_out_CCO">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 43,
    label = "Csj_out_CCC",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="R6Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=43 label="Csj_out_CCC">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 41,
    label = "Csj_out_CCO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=7 label="R5Hall">, <Entry index=41 label="Csj_out_CCO">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=41 label="Csj_out_CCO">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 42,
    label = "Csj_out_COO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 43,
    label = "Csj_out_OOO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 15,
    label = "Cdj_out",
    group = 
"""
1 *1 Cd u1
""",
    distances = DistanceData(
        distances = {'d12': -0.212575, 'd13': 0.005083, 'd23': 0.099441},
        uncertainties = {'d12': 2.66728, 'd13': 0.083904, 'd23': 2.21333},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=15 label="Cdj_out">, <Entry index=23 label="Cb_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=27 label="Cdj_out_Cd">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 27,
    label = "Cdj_out_Cd",
    group = 
"""
1 *1 Cd       u1 {2,D}
2    [Cd,Cdd] ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.125385, 'd13': -0.021008, 'd23': -0.183569},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=4 label="R2Hall">, <Entry index=27 label="Cdj_out_Cd">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 44,
    label = "Cdj_out_CdOs",
    group = 
"""
1 *1 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    O        ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 45,
    label = "Cdj_out_CdCs",
    group = 
"""
1 *1 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    Cs       ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 28,
    label = "Cdj_out_Od",
    group = 
"""
1 *1 Cd u1 {2,D}
2    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 46,
    label = "Cdj_out_OdCs",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 47,
    label = "Cdj_out_OdOs",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 16,
    label = "Ctj_out",
    group = 
"""
1 *1 Ct u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 29,
    label = "Ctj_out_Ct",
    group = 
"""
1 *1 Ct u1 {2,T}
2    Ct ux {1,T}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 17,
    label = "Cbj_out",
    group = 
"""
1 *1 Cb u1
""",
    distances = DistanceData(
        distances = {'d12': 0.572242, 'd13': 0.055304, 'd23': -0.305995},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=17 label="Cbj_out">, <Entry index=21 label="Cd_H_out">]
""",
)

entry(
    index = 11,
    label = "Oj_out",
    group = 
"""
1 *1 O u1
""",
    distances = DistanceData(
        distances = {'d12': 0.213055, 'd13': -0.076312, 'd23': -0.120233},
        uncertainties = {'d12': 0.983225, 'd13': 0.115002, 'd23': 0.940121},
    ),
    shortDesc = u"""Fitted to 20 distances.
""",
    longDesc = 
u"""
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=8 label="R6Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
""",
)

entry(
    index = 18,
    label = "Oj_out_C",
    group = 
"""
1 *1 O u1 {2,S}
2    C ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=18 label="Oj_out_C">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=6 label="R4Hall">, <Entry index=18 label="Oj_out_C">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=9 label="R7Hall">, <Entry index=18 label="Oj_out_C">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=18 label="Oj_out_C">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=7 label="R5Hall">, <Entry index=18 label="Oj_out_C">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=18 label="Oj_out_C">, <Entry index=32 label="Cs_H_out_noH">]
""",
)

entry(
    index = 19,
    label = "Oj_out_O",
    group = 
"""
1 *1 O u1 {2,S}
2    O ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 11 distances.
""",
    longDesc = 
u"""
[<Entry index=7 label="R5Hall">, <Entry index=19 label="Oj_out_O">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=7 label="R5Hall">, <Entry index=19 label="Oj_out_O">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=19 label="Oj_out_O">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=19 label="Oj_out_O">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=5 label="R3Hall">, <Entry index=19 label="Oj_out_O">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=19 label="Oj_out_O">, <Entry index=13 label="O_H_out">]
[<Entry index=9 label="R7Hall">, <Entry index=19 label="Oj_out_O">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=19 label="Oj_out_O">, <Entry index=32 label="Cs_H_out_noH">]
""",
)

entry(
    index = 12,
    label = "C_H_out",
    group = 
"""
1 *2 C ux {2,S}
2 *3 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.044562, 'd13': 0.024698, 'd23': -0.073415},
        uncertainties = {'d12': 0.76875, 'd13': 0.089789, 'd23': 0.74434},
    ),
    shortDesc = u"""Fitted to 66 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=15 label="Cdj_out">, <Entry index=23 label="Cb_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=4 label="R2Hall">, <Entry index=27 label="Cdj_out_Cd">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=12 label="C_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=21 label="Cd_H_out">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=10 label="Cj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=17 label="Cbj_out">, <Entry index=21 label="Cd_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
""",
)

entry(
    index = 20,
    label = "Cs_H_out",
    group = 
"""
1 *2 Cs ux {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.049515, 'd13': 0.022446, 'd23': -0.075967},
        uncertainties = {'d12': 0.791714, 'd13': 0.087049, 'd23': 0.765955},
    ),
    shortDesc = u"""Fitted to 62 distances.
""",
    longDesc = 
u"""
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=4 label="R2Hall">, <Entry index=27 label="Cdj_out_Cd">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=10 label="Cj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
""",
)

entry(
    index = 30,
    label = "Cs_H_out_2H",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.053391, 'd13': 0.026591, 'd23': 0.053596},
        uncertainties = {'d12': 0.872478, 'd13': 0.097734, 'd23': 0.877979},
    ),
    shortDesc = u"""Fitted to 31 distances.
""",
    longDesc = 
u"""
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=27 label="Cdj_out_Cd">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=10 label="Cj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=30 label="Cs_H_out_2H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=30 label="Cs_H_out_2H">]
""",
)

entry(
    index = 31,
    label = "Cs_H_out_1H",
    group = 
"""
1 *2 Cs  ux {2,S} {3,S} {4,S}
2 *3 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.007735, 'd13': 0.012915, 'd23': -0.089783},
        uncertainties = {'d12': 0.847545, 'd13': 0.072818, 'd23': 0.835669},
    ),
    shortDesc = u"""Fitted to 14 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=4 label="R2Hall">, <Entry index=11 label="Oj_out">, <Entry index=31 label="Cs_H_out_1H">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=31 label="Cs_H_out_1H">]
""",
)

entry(
    index = 32,
    label = "Cs_H_out_noH",
    group = 
"""
1 *2 Cs  ux {2,S} {3,S} {4,S}
2 *3 H   u0 {1,S}
3    R!H u0 {1,S}
4    R!H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.293222, 'd13': 0.0228, 'd23': -0.32256},
        uncertainties = {'d12': 0.765517, 'd13': 0.094994, 'd23': 0.640522},
    ),
    shortDesc = u"""Fitted to 17 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=6 label="R4Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=5 label="R3Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=32 label="Cs_H_out_noH">]
[<Entry index=8 label="R6Hall">, <Entry index=11 label="Oj_out">, <Entry index=32 label="Cs_H_out_noH">]
""",
)

entry(
    index = 21,
    label = "Cd_H_out",
    group = 
"""
1 *2 Cd ux {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.160425, 'd13': 0.010315, 'd23': -0.235398},
        uncertainties = {'d12': 3.2934, 'd13': 0.419193, 'd23': 2.66257},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=17 label="Cbj_out">, <Entry index=21 label="Cd_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=21 label="Cd_H_out">]
""",
)

entry(
    index = 33,
    label = "Cd_H_out_1H",
    group = 
"""
1 *2 Cd  u0 {2,S} {3,S} {4,D}
2 *3 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,D}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=17 label="Cbj_out">, <Entry index=33 label="Cd_H_out_1H">]
""",
)

entry(
    index = 34,
    label = "Cd_H_out_noH",
    group = 
"""
1 *2 Cd  u0 {2,S} {3,S} {4,D}
2 *3 H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 22,
    label = "Ct_H_out",
    group = 
"""
1 *2 Ct u0 {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 23,
    label = "Cb_H_out",
    group = 
"""
1 *2 Cb u0 {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.32837, 'd13': 0.056611, 'd23': 0.608265},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=15 label="Cdj_out">, <Entry index=23 label="Cb_H_out">]
""",
)

entry(
    index = 13,
    label = "O_H_out",
    group = 
"""
1 *2 O u0 {2,S}
2 *3 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.138297, 'd13': -0.076649, 'd23': 0.22784},
        uncertainties = {'d12': 1.09895, 'd13': 0.113293, 'd23': 1.10421},
    ),
    shortDesc = u"""Fitted to 20 distances.
""",
    longDesc = 
u"""
[<Entry index=6 label="R4Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=7 label="R5Hall">, <Entry index=11 label="Oj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=8 label="R6Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=4 label="R2Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=5 label="R3Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=9 label="R7Hall">, <Entry index=14 label="Csj_out">, <Entry index=13 label="O_H_out">]
""",
)

tree(
"""
L1: RnH
    L2: R2Hall
    L2: R3Hall
    L2: R4Hall
    L2: R5Hall
    L2: R6Hall
    L2: R7Hall
L1: Y_rad_out
    L2: Cj_out
        L3: Csj_out
            L4: Csj_out_2H
                L5: Csj_out_CHH
                L5: Csj_out_OHH
            L4: Csj_out_1H
                L5: Csj_out_CCH
                L5: Csj_out_COH
                L5: Csj_out_OOH
            L4: Csj_out_noH
                L5: Csj_out_CCC
                L5: Csj_out_CCO
                L5: Csj_out_COO
                L5: Csj_out_OOO
        L3: Cdj_out
            L4: Cdj_out_Cd
                L5: Cdj_out_CdOs
                L5: Cdj_out_CdCs
            L4: Cdj_out_Od
                L5: Cdj_out_OdCs
                L5: Cdj_out_OdOs
        L3: Ctj_out
            L4: Ctj_out_Ct
        L3: Cbj_out
    L2: Oj_out
        L3: Oj_out_C
        L3: Oj_out_O
L1: X_H_out
    L2: C_H_out
        L3: Cs_H_out
            L4: Cs_H_out_2H
            L4: Cs_H_out_1H
            L4: Cs_H_out_noH
        L3: Cd_H_out
            L4: Cd_H_out_1H
            L4: Cd_H_out_noH
        L3: Ct_H_out
        L3: Cb_H_out
    L2: O_H_out
"""
)

