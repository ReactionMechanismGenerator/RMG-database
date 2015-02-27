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
        distances = {'d12': 1.77816, 'd13': 1.3221, 'd23': 1.78075},
        uncertainties = {'d12': 0.507274, 'd13': 0.073632, 'd23': 0.496207},
    ),
    shortDesc = u"""Fitted to 22 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=126 label="Cs_H_out_CC">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=199 label="Cs_H_out_CsO">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
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
        distances = {'d12': -0.455364, 'd13': 0.021481, 'd23': -0.346809},
        uncertainties = {'d12': 0.741229, 'd13': 0.053992, 'd23': 0.729329},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=126 label="Cs_H_out_CC">]
""",
)

entry(
    index = 14,
    label = "R2H_s",
    group = 
"""
1 *2 R!H u0 {2,S} {3,S}
2 *1 R!H u1 {1,S}
3 *3 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.455364, 'd13': 0.021481, 'd23': -0.346809},
        uncertainties = {'d12': 0.741229, 'd13': 0.053992, 'd23': 0.729329},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=126 label="Cs_H_out_CC">]
""",
)

entry(
    index = 15,
    label = "R2H_r",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *2 R!H u0 {1,[D,T,B]} {3,S}
3 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 88,
    label = "R2H_d",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *2 R!H u0 {1,D} {3,S}
3 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 89,
    label = "R2H_t",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *2 R!H u0 {1,T} {3,S}
3 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 90,
    label = "R2H_b",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *2 R!H u0 {1,B} {3,S}
3 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
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
        distances = {'d12': -0.147038, 'd13': -0.014367, 'd23': -0.008426},
        uncertainties = {'d12': 6.61156, 'd13': 0.306064, 'd23': 5.6648},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=16 label="R3H_ss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 16,
    label = "R3H_ss",
    group = 
"""
1 *4 R!H ux {2,S} {3,S}
2 *2 R!H u0 {1,S} {4,S}
3 *1 R!H u1 {1,S}
4 *3 H   u0 {2,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.147038, 'd13': -0.014367, 'd23': -0.008426},
        uncertainties = {'d12': 6.61156, 'd13': 0.306064, 'd23': 5.6648},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=16 label="R3H_ss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 17,
    label = "R3H_sr",
    group = 
"""
1 *4 R!H ux {2,[D,T,B]} {3,S}
2 *2 R!H u0 {1,[D,T,B]} {4,S}
3 *1 R!H u1 {1,S}
4 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 18,
    label = "R3H_rs",
    group = 
"""
1 *4 R!H ux {2,S} {3,[D,T,B]}
2 *2 R!H u0 {1,S} {4,S}
3 *1 R!H u1 {1,[D,T,B]}
4 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 19,
    label = "R3H_rr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *2 R!H u0 {2,[D,T,B]} {4,S}
4 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
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
        distances = {'d12': 0.192432, 'd13': 0.035625, 'd23': 0.14586},
        uncertainties = {'d12': 0.565094, 'd13': 0.0521, 'd23': 0.679342},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
""",
)

entry(
    index = 20,
    label = "R4H_sss",
    group = 
"""
1 *5 R!H ux {2,S} {3,S}
2 *4 R!H ux {1,S} {4,S}
3 *2 R!H u0 {1,S} {5,S}
4 *1 R!H u1 {2,S}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.187434, 'd13': 0.050032, 'd23': 0.163131},
        uncertainties = {'d12': 0.822657, 'd13': 0.060089, 'd23': 0.977161},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
""",
)

entry(
    index = 21,
    label = "R4H_ssr",
    group = 
"""
1 *5 R!H ux {2,S} {3,[D,T,B]}
2 *4 R!H ux {1,S} {4,S}
3 *2 R!H u0 {1,[D,T,B]} {5,S}
4 *1 R!H u1 {2,S}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 22,
    label = "R4H_srs",
    group = 
"""
1 *5 R!H ux {2,[D,T,B]} {3,S}
2 *4 R!H ux {1,[D,T,B]} {4,S}
3 *2 R!H u0 {1,S} {5,S}
4 *1 R!H u1 {2,S}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.199247, 'd13': 0.01598, 'd23': 0.122309},
        uncertainties = {'d12': 0.820286, 'd13': 0.088665, 'd23': 0.997839},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
""",
)

entry(
    index = 23,
    label = "R4H_rss",
    group = 
"""
1 *5 R!H ux {2,S} {3,S}
2 *4 R!H ux {1,S} {4,[D,T,B]}
3 *2 R!H u0 {1,S} {5,S}
4 *1 R!H u1 {2,[D,T,B]}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 24,
    label = "R4H_srr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *5 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *2 R!H u0 {3,[D,T,B]} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 25,
    label = "R4H_rrs",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *5 R!H ux {2,[D,T,B]} {4,S}
4 *2 R!H u0 {3,S} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 26,
    label = "R4H_rsr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *5 R!H ux {2,S} {4,[D,T,B]}
4 *2 R!H u0 {3,[D,T,B]} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 27,
    label = "R4H_rrr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *5 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *2 R!H u0 {3,[D,T,B]} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
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
        distances = {'d12': 0.106227, 'd13': -0.067741, 'd23': 0.054558},
        uncertainties = {'d12': 0.576611, 'd13': 0.131001, 'd23': 0.457029},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_sss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=199 label="Cs_H_out_CsO">]
""",
)

entry(
    index = 28,
    label = "R5H_sss",
    group = 
"""
1 *6 R!H ux {2,S} {3,S}
2 *5 R!H ux {1,S} {4,S}
3 *4 R!H ux {1,S} {5,S}
4 *2 R!H u0 {2,S} {6,S}
5 *1 R!H u1 {3,S}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.106227, 'd13': -0.067741, 'd23': 0.054558},
        uncertainties = {'d12': 0.576611, 'd13': 0.131001, 'd23': 0.457029},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_sss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=199 label="Cs_H_out_CsO">]
""",
)

entry(
    index = 29,
    label = "R5H_sssr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,[D,T,B]}
5 *2 R!H u0 {4,[D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 30,
    label = "R5H_ssrs",
    group = 
"""
1 *6 R!H ux {2,[D,T,B]} {3,S}
2 *5 R!H ux {1,[D,T,B]} {4,S}
3 *4 R!H ux {1,S} {5,S}
4 *2 R!H u0 {2,S} {6,S}
5 *1 R!H u1 {3,S}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 31,
    label = "R5H_srss",
    group = 
"""
1 *6 R!H ux {2,S} {3,[D,T,B]}
2 *5 R!H ux {1,S} {4,S}
3 *4 R!H ux {1,[D,T,B]} {5,S}
4 *2 R!H u0 {2,S} {6,S}
5 *1 R!H u1 {3,S}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 32,
    label = "R5H_rsss",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 33,
    label = "R5H_ssrr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *5 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *2 R!H u0 {4,[D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 34,
    label = "R5H_srsr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *5 R!H ux {3,S} {5,[D,T,B]}
5 *2 R!H u0 {4,[D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 35,
    label = "R5H_rssr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,[D,T,B]}
5 *2 R!H u0 {4,[D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 36,
    label = "R5H_srrs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *5 R!H ux {3,[D,T,B]} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 37,
    label = "R5H_rsrs",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *5 R!H ux {3,[D,T,B]} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 38,
    label = "R5H_rrss",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *5 R!H ux {3,S} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 39,
    label = "R5H_srrr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *5 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *2 R!H u0 {4,[D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 40,
    label = "R5H_rsrr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *5 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *2 R!H u0 {4,[D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 41,
    label = "R5H_rrsr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *5 R!H ux {3,S} {5,[D,T,B]}
5 *2 R!H u0 {4,[D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 42,
    label = "R5H_rrrs",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *5 R!H ux {3,[D,T,B]} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 43,
    label = "R5H_rrrr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *5 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *2 R!H u0 {4,[D,T,B]} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
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
    distances = DistanceData(distances={}),
)

entry(
    index = 44,
    label = "R6H_sssss",
    group = 
"""
1 *7 R!H ux {2,S} {3,S}
2 *6 R!H ux {1,S} {4,S}
3 *5 R!H ux {1,S} {5,S}
4 *4 R!H ux {2,S} {6,S}
5 *2 R!H u0 {3,S} {7,S}
6 *1 R!H u1 {4,S}
7 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 45,
    label = "R6H_ssssr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 46,
    label = "R6H_sssrs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 47,
    label = "R6H_ssrss",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 48,
    label = "R6H_srsss",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 49,
    label = "R6H_rssss",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 50,
    label = "R6H_sssrr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 51,
    label = "R6H_ssrsr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,S}
5 *5 R!H ux {4,S} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 52,
    label = "R6H_srssr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 53,
    label = "R6H_rsssr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 54,
    label = "R6H_ssrrs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 55,
    label = "R6H_srsrs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *7 R!H ux {3,S} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 56,
    label = "R6H_rssrs",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 57,
    label = "R6H_srrss",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 58,
    label = "R6H_rsrss",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 59,
    label = "R6H_rrsss",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 60,
    label = "R6H_ssrrr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 61,
    label = "R6H_srsrr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *7 R!H ux {3,S} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 62,
    label = "R6H_rssrr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 63,
    label = "R6H_srrsr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,S}
5 *5 R!H ux {4,S} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 64,
    label = "R6H_rsrsr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,S}
5 *5 R!H ux {4,S} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 65,
    label = "R6H_rrssr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 66,
    label = "R6H_srrrs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 67,
    label = "R6H_rsrrs",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 68,
    label = "R6H_rrsrs",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *7 R!H ux {3,S} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 69,
    label = "R6H_rrrss",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 70,
    label = "R6H_srrrr",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 71,
    label = "R6H_rsrrr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,S}
3 *6 R!H ux {2,S} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 72,
    label = "R6H_rrsrr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,S}
4 *7 R!H ux {3,S} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 73,
    label = "R6H_rrrsr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,S}
5 *5 R!H ux {4,S} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 74,
    label = "R6H_rrrrs",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 75,
    label = "R6H_rrrrr",
    group = 
"""
1 *1 R!H u1 {2,[D,T,B]}
2 *4 R!H ux {1,[D,T,B]} {3,[D,T,B]}
3 *6 R!H ux {2,[D,T,B]} {4,[D,T,B]}
4 *7 R!H ux {3,[D,T,B]} {5,[D,T,B]}
5 *5 R!H ux {4,[D,T,B]} {6,[D,T,B]}
6 *2 R!H u0 {5,[D,T,B]} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
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
    distances = DistanceData(distances={}),
)

entry(
    index = 10,
    label = "Cj_out",
    group = 
"""
1 *1 C u1
""",
    distances = DistanceData(
        distances = {'d12': -0.168709, 'd13': 0.024245, 'd23': 0.133967},
        uncertainties = {'d12': 0.403966, 'd13': 0.066498, 'd23': 0.450716},
    ),
    shortDesc = u"""Fitted to 16 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=126 label="Cs_H_out_CC">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_sss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
""",
)

entry(
    index = 76,
    label = "Csj_out",
    group = 
"""
1 *1 Cs u1
""",
    distances = DistanceData(
        distances = {'d12': -0.168709, 'd13': 0.024245, 'd23': 0.133967},
        uncertainties = {'d12': 0.403966, 'd13': 0.066498, 'd23': 0.450716},
    ),
    shortDesc = u"""Fitted to 16 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=126 label="Cs_H_out_CC">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_sss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
""",
)

entry(
    index = 91,
    label = "Csj_out_RH2",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 110,
    label = "Csj_out_CH2",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 133,
    label = "Csj_out_CsH2",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 134,
    label = "Csj_out_CdH2",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 135,
    label = "Csj_out_CtH2",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 136,
    label = "Csj_out_CbH2",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 111,
    label = "Csj_out_OHH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 92,
    label = "Csj_out_RRH",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 112,
    label = "Csj_out_CCH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 137,
    label = "Csj_out_CsCsH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 138,
    label = "Csj_out_CsCdH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 139,
    label = "Csj_out_CsCtH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 140,
    label = "Csj_out_CsCbH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 141,
    label = "Csj_out_CdCdH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 142,
    label = "Csj_out_CdCtH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 143,
    label = "Csj_out_CdCbH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 144,
    label = "Csj_out_CtCtH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 145,
    label = "Csj_out_CtCbH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 146,
    label = "Csj_out_CbCbH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 113,
    label = "Csj_out_COH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 147,
    label = "Csj_out_CsOH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 148,
    label = "Csj_out_CdOH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 149,
    label = "Csj_out_CtOH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 150,
    label = "Csj_out_CbOH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 114,
    label = "Csj_out_OOH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 93,
    label = "Csj_out_RRR",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 115,
    label = "Csj_out_CCC",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 151,
    label = "Csj_out_CsCsCs",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 152,
    label = "Csj_out_CsCsCd",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 153,
    label = "Csj_out_CsCsCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 154,
    label = "Csj_out_CsCsCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 155,
    label = "Csj_out_CsCdCd",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 156,
    label = "Csj_out_CsCdCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 157,
    label = "Csj_out_CsCdCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 158,
    label = "Csj_out_CsCtCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 159,
    label = "Csj_out_CsCtCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 160,
    label = "Csj_out_CsCbCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 161,
    label = "Csj_out_CdCdCd",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 162,
    label = "Csj_out_CdCdCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 163,
    label = "Csj_out_CdCdCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 164,
    label = "Csj_out_CdCtCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 165,
    label = "Csj_out_CdCtCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 166,
    label = "Csj_out_CdCbCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 167,
    label = "Csj_out_CtCtCt",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 168,
    label = "Csj_out_CtCtCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 169,
    label = "Csj_out_CtCbCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 170,
    label = "Csj_out_CbCbCb",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 116,
    label = "Csj_out_CCO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 171,
    label = "Csj_out_CsCsO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 172,
    label = "Csj_out_CsCdO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 173,
    label = "Csj_out_CsCtO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 174,
    label = "Csj_out_CsCbO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 175,
    label = "Csj_out_CdCdO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 176,
    label = "Csj_out_CdCtO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 177,
    label = "Csj_out_CdCbO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 178,
    label = "Csj_out_CtCtO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 179,
    label = "Csj_out_CtCbO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 180,
    label = "Csj_out_CbCbO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 117,
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
    index = 181,
    label = "Csj_out_CsOO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 182,
    label = "Csj_out_CdOO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 183,
    label = "Csj_out_CtOO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 184,
    label = "Csj_out_CbOO",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 118,
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
    index = 77,
    label = "Cdj_out",
    group = 
"""
1 *1 Cd u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 94,
    label = "Cdj_out_Cd",
    group = 
"""
1 *1 Cd       u1 {2,D}
2    [Cd,Cdd] ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 119,
    label = "Cdj_out_CdH",
    group = 
"""
1 *1 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    H        u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 207,
    label = "Cdj_out_CdsH",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 208,
    label = "Cdj_out_CddH",
    group = 
"""
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 120,
    label = "Cdj_out_CdO",
    group = 
"""
1 *1 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    O        ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 209,
    label = "Cdj_out_CdsO",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 210,
    label = "Cdj_out_CddO",
    group = 
"""
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    O   ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 121,
    label = "Cdj_out_CdC",
    group = 
"""
1 *1 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    C        ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 211,
    label = "Cdj_out_CdsCs",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 212,
    label = "Cdj_out_CdsCd",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 213,
    label = "Cdj_out_CdsCt",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 214,
    label = "Cdj_out_CdsCb",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 215,
    label = "Cdj_out_CddCs",
    group = 
"""
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cs  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 216,
    label = "Cdj_out_CddCd",
    group = 
"""
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 217,
    label = "Cdj_out_CddCt",
    group = 
"""
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 218,
    label = "Cdj_out_CddCb",
    group = 
"""
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 95,
    label = "Cdj_out_Od",
    group = 
"""
1 *1 Cd u1 {2,D}
2    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 122,
    label = "Cdj_out_OdC",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 219,
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
    index = 220,
    label = "Cdj_out_OdCd",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 221,
    label = "Cdj_out_OdCt",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 222,
    label = "Cdj_out_OdCb",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 123,
    label = "Cdj_out_OdO",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 78,
    label = "Ctj_out",
    group = 
"""
1 *1 Ct u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 96,
    label = "Ctj_out_Ct",
    group = 
"""
1 *1 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 79,
    label = "Cbj_out",
    group = 
"""
1 *1 Cb u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 11,
    label = "Oj_out",
    group = 
"""
1 *1 O u1
""",
    distances = DistanceData(
        distances = {'d12': 0.316329, 'd13': -0.04546, 'd23': -0.251189},
        uncertainties = {'d12': 0.969152, 'd13': 0.124487, 'd23': 0.832847},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=199 label="Cs_H_out_CsO">]
""",
)

entry(
    index = 80,
    label = "Oj_out_C",
    group = 
"""
1 *1 O u1 {2,S}
2    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 97,
    label = "Oj_out_Cs",
    group = 
"""
1 *1 O  u1 {2,S}
2    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 98,
    label = "Oj_out_Cd",
    group = 
"""
1 *1 O  u1 {2,S}
2    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 99,
    label = "Oj_out_Ct",
    group = 
"""
1 *1 O  u1 {2,S}
2    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 100,
    label = "Oj_out_Cb",
    group = 
"""
1 *1 O  u1 {2,S}
2    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 81,
    label = "Oj_out_O",
    group = 
"""
1 *1 O u1 {2,S}
2    O u0 {1,S}
""",
    distances = DistanceData(distances={}),
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
        distances = {'d12': 0.169147, 'd13': 0.021219, 'd23': -0.202374},
        uncertainties = {'d12': 0.595167, 'd13': 0.065105, 'd23': 0.578635},
    ),
    shortDesc = u"""Fitted to 16 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=126 label="Cs_H_out_CC">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=199 label="Cs_H_out_CsO">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 82,
    label = "Cs_H_out",
    group = 
"""
1 *2 Cs ux {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.169147, 'd13': 0.021219, 'd23': -0.202374},
        uncertainties = {'d12': 0.595167, 'd13': 0.065105, 'd23': 0.578635},
    ),
    shortDesc = u"""Fitted to 16 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=126 label="Cs_H_out_CC">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=199 label="Cs_H_out_CsO">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 101,
    label = "Cs_H_out_H2",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.174086, 'd13': 0.016086, 'd23': 0.138593},
        uncertainties = {'d12': 0.783136, 'd13': 0.051918, 'd23': 0.843648},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=22 label="R4H_srs">, <Entry index=11 label="Oj_out">, <Entry index=101 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=101 label="Cs_H_out_H2">]
""",
)

entry(
    index = 102,
    label = "Cs_H_out_RH",
    group = 
"""
1 *2 Cs  ux {2,S} {3,S} {4,S}
2 *3 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 124,
    label = "Cs_H_out_CH",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 185,
    label = "Cs_H_out_CsH",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 186,
    label = "Cs_H_out_CdH",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 187,
    label = "Cs_H_out_CtH",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 188,
    label = "Cs_H_out_CbH",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 125,
    label = "Cs_H_out_OH",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 103,
    label = "Cs_H_out_RR",
    group = 
"""
1 *2 Cs  ux {2,S} {3,S} {4,S}
2 *3 H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.452687, 'd13': 0.025459, 'd23': -0.484042},
        uncertainties = {'d12': 0.607358, 'd13': 0.086643, 'd23': 0.51061},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=126 label="Cs_H_out_CC">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=199 label="Cs_H_out_CsO">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 126,
    label = "Cs_H_out_CC",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.454622, 'd13': 0.028704, 'd23': -0.494607},
        uncertainties = {'d12': 0.642928, 'd13': 0.085914, 'd23': 0.551448},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=14 label="R2H_s">, <Entry index=76 label="Csj_out">, <Entry index=126 label="Cs_H_out_CC">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 189,
    label = "Cs_H_out_CsCs",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.591325, 'd13': 0.030426, 'd23': -0.529691},
        uncertainties = {'d12': 0.797887, 'd13': 0.10583, 'd23': 0.660741},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=20 label="R4H_sss">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=189 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 190,
    label = "Cs_H_out_CsCd",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 191,
    label = "Cs_H_out_CsCt",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 192,
    label = "Cs_H_out_CsCb",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 193,
    label = "Cs_H_out_CdCd",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 194,
    label = "Cs_H_out_CdCt",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 195,
    label = "Cs_H_out_CdCb",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 196,
    label = "Cs_H_out_CtCt",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 197,
    label = "Cs_H_out_CtCb",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 198,
    label = "Cs_H_out_CbCb",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 127,
    label = "Cs_H_out_CO",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.432365, 'd13': -0.00861, 'd23': -0.373117},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=199 label="Cs_H_out_CsO">]
""",
)

entry(
    index = 199,
    label = "Cs_H_out_CsO",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.432365, 'd13': -0.00861, 'd23': -0.373117},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_sss">, <Entry index=11 label="Oj_out">, <Entry index=199 label="Cs_H_out_CsO">]
""",
)

entry(
    index = 200,
    label = "Cs_H_out_CdO",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 201,
    label = "Cs_H_out_CtO",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 202,
    label = "Cs_H_out_CbO",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 128,
    label = "Cs_H_out_OO",
    group = 
"""
1 *2 Cs ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 83,
    label = "Cd_H_out",
    group = 
"""
1 *2 Cd ux {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 104,
    label = "Cd_H_out_RdH",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    R!H ux {1,D}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 129,
    label = "Cd_H_out_CdH",
    group = 
"""
1 *2 Cd       ux {2,S} {3,D} {4,S}
2 *3 H        u0 {1,S}
3    [Cd,Cdd] ux {1,D}
4    H        u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 223,
    label = "Cd_H_out_CdsH",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,D}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 224,
    label = "Cd_H_out_CddH",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    Cdd u0 {1,D}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 130,
    label = "Cd_H_out_OdH",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    O  u0 {1,D}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 105,
    label = "Cd_H_out_RdR",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    R!H ux {1,D}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 131,
    label = "Cd_H_out_CdR",
    group = 
"""
1 *2 Cd       ux {2,S} {3,D} {4,S}
2 *3 H        u0 {1,S}
3    [Cd,Cdd] ux {1,D}
4    R!H      ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 203,
    label = "Cd_H_out_CdC",
    group = 
"""
1 *2 Cd       ux {2,S} {3,D} {4,S}
2 *3 H        u0 {1,S}
3    [Cd,Cdd] ux {1,D}
4    C        ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 225,
    label = "Cd_H_out_CdsCs",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,D}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 226,
    label = "Cd_H_out_CdsCd",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,D}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 227,
    label = "Cd_H_out_CdsCt",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,D}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 228,
    label = "Cd_H_out_CdsCb",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,D}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 229,
    label = "Cd_H_out_CddCs",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    Cdd u0 {1,D}
4    Cs  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 230,
    label = "Cd_H_out_CddCd",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    Cdd u0 {1,D}
4    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 231,
    label = "Cd_H_out_CddCt",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    Cdd u0 {1,D}
4    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 232,
    label = "Cd_H_out_CddCb",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    Cdd u0 {1,D}
4    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 204,
    label = "Cd_H_out_CdOs",
    group = 
"""
1 *2 Cd       ux {2,S} {3,D} {4,S}
2 *3 H        u0 {1,S}
3    [Cd,Cdd] ux {1,D}
4    O        ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 233,
    label = "Cd_H_out_CdsOs",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,D}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 234,
    label = "Cd_H_out_CddOs",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    Cdd u0 {1,D}
4    O   ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 132,
    label = "Cd_H_out_OdR",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    O   u0 {1,D}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 205,
    label = "Cd_H_out_OdC",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    O  u0 {1,D}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 235,
    label = "Cd_H_out_OdCs",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    O  u0 {1,D}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 236,
    label = "Cd_H_out_OdCd",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    O  u0 {1,D}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 237,
    label = "Cd_H_out_OdCt",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    O  u0 {1,D}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 238,
    label = "Cd_H_out_OdCb",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    O  u0 {1,D}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 206,
    label = "Cd_H_out_OdOs",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    O  u0 {1,D}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 84,
    label = "Ct_H_out",
    group = 
"""
1 *2 Ct u0 {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 85,
    label = "Cb_H_out",
    group = 
"""
1 *2 Cb u0 {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
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
        distances = {'d12': -0.394675, 'd13': -0.04951, 'd23': 0.472205},
        uncertainties = {'d12': 0.325073, 'd13': 0.12766, 'd23': 0.345078},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_sss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=22 label="R4H_srs">, <Entry index=76 label="Csj_out">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 86,
    label = "O_H_out_C",
    group = 
"""
1 *2 O u0 {2,S} {3,S}
2 *3 H u0 {1,S}
3    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 106,
    label = "O_H_out_Cs",
    group = 
"""
1 *2 O  u0 {2,S} {3,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 107,
    label = "O_H_out_Cd",
    group = 
"""
1 *2 O  u0 {2,S} {3,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 108,
    label = "O_H_out_Ct",
    group = 
"""
1 *2 O  u0 {2,S} {3,S}
2 *3 H  u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 109,
    label = "O_H_out_Cb",
    group = 
"""
1 *2 O  u0 {2,S} {3,S}
2 *3 H  u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 87,
    label = "O_H_out_O",
    group = 
"""
1 *2 O u0 {2,S} {3,S}
2 *3 H u0 {1,S}
3    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

tree(
"""
L1: RnH
    L2: R2Hall
        L3: R2H_s
        L3: R2H_r
            L4: R2H_d
            L4: R2H_t
            L4: R2H_b
    L2: R3Hall
        L3: R3H_ss
        L3: R3H_sr
        L3: R3H_rs
        L3: R3H_rr
    L2: R4Hall
        L3: R4H_sss
        L3: R4H_ssr
        L3: R4H_srs
        L3: R4H_rss
        L3: R4H_srr
        L3: R4H_rrs
        L3: R4H_rsr
        L3: R4H_rrr
    L2: R5Hall
        L3: R5H_sss
        L3: R5H_sssr
        L3: R5H_ssrs
        L3: R5H_srss
        L3: R5H_rsss
        L3: R5H_ssrr
        L3: R5H_srsr
        L3: R5H_rssr
        L3: R5H_srrs
        L3: R5H_rsrs
        L3: R5H_rrss
        L3: R5H_srrr
        L3: R5H_rsrr
        L3: R5H_rrsr
        L3: R5H_rrrs
        L3: R5H_rrrr
    L2: R6Hall
        L3: R6H_sssss
        L3: R6H_ssssr
        L3: R6H_sssrs
        L3: R6H_ssrss
        L3: R6H_srsss
        L3: R6H_rssss
        L3: R6H_sssrr
        L3: R6H_ssrsr
        L3: R6H_srssr
        L3: R6H_rsssr
        L3: R6H_ssrrs
        L3: R6H_srsrs
        L3: R6H_rssrs
        L3: R6H_srrss
        L3: R6H_rsrss
        L3: R6H_rrsss
        L3: R6H_ssrrr
        L3: R6H_srsrr
        L3: R6H_rssrr
        L3: R6H_srrsr
        L3: R6H_rsrsr
        L3: R6H_rrssr
        L3: R6H_srrrs
        L3: R6H_rsrrs
        L3: R6H_rrsrs
        L3: R6H_rrrss
        L3: R6H_srrrr
        L3: R6H_rsrrr
        L3: R6H_rrsrr
        L3: R6H_rrrsr
        L3: R6H_rrrrs
        L3: R6H_rrrrr
    L2: R7Hall
L1: Y_rad_out
    L2: Cj_out
        L3: Csj_out
            L4: Csj_out_RH2
                L5: Csj_out_CH2
                    L6: Csj_out_CsH2
                    L6: Csj_out_CdH2
                    L6: Csj_out_CtH2
                    L6: Csj_out_CbH2
                L5: Csj_out_OHH
            L4: Csj_out_RRH
                L5: Csj_out_CCH
                    L6: Csj_out_CsCsH
                    L6: Csj_out_CsCdH
                    L6: Csj_out_CsCtH
                    L6: Csj_out_CsCbH
                    L6: Csj_out_CdCdH
                    L6: Csj_out_CdCtH
                    L6: Csj_out_CdCbH
                    L6: Csj_out_CtCtH
                    L6: Csj_out_CtCbH
                    L6: Csj_out_CbCbH
                L5: Csj_out_COH
                    L6: Csj_out_CsOH
                    L6: Csj_out_CdOH
                    L6: Csj_out_CtOH
                    L6: Csj_out_CbOH
                L5: Csj_out_OOH
            L4: Csj_out_RRR
                L5: Csj_out_CCC
                    L6: Csj_out_CsCsCs
                    L6: Csj_out_CsCsCd
                    L6: Csj_out_CsCsCt
                    L6: Csj_out_CsCsCb
                    L6: Csj_out_CsCdCd
                    L6: Csj_out_CsCdCt
                    L6: Csj_out_CsCdCb
                    L6: Csj_out_CsCtCt
                    L6: Csj_out_CsCtCb
                    L6: Csj_out_CsCbCb
                    L6: Csj_out_CdCdCd
                    L6: Csj_out_CdCdCt
                    L6: Csj_out_CdCdCb
                    L6: Csj_out_CdCtCt
                    L6: Csj_out_CdCtCb
                    L6: Csj_out_CdCbCb
                    L6: Csj_out_CtCtCt
                    L6: Csj_out_CtCtCb
                    L6: Csj_out_CtCbCb
                    L6: Csj_out_CbCbCb
                L5: Csj_out_CCO
                    L6: Csj_out_CsCsO
                    L6: Csj_out_CsCdO
                    L6: Csj_out_CsCtO
                    L6: Csj_out_CsCbO
                    L6: Csj_out_CdCdO
                    L6: Csj_out_CdCtO
                    L6: Csj_out_CdCbO
                    L6: Csj_out_CtCtO
                    L6: Csj_out_CtCbO
                    L6: Csj_out_CbCbO
                L5: Csj_out_COO
                    L6: Csj_out_CsOO
                    L6: Csj_out_CdOO
                    L6: Csj_out_CtOO
                    L6: Csj_out_CbOO
                L5: Csj_out_OOO
        L3: Cdj_out
            L4: Cdj_out_Cd
                L5: Cdj_out_CdH
                    L6: Cdj_out_CdsH
                    L6: Cdj_out_CddH
                L5: Cdj_out_CdO
                    L6: Cdj_out_CdsO
                    L6: Cdj_out_CddO
                L5: Cdj_out_CdC
                    L6: Cdj_out_CdsCs
                    L6: Cdj_out_CdsCd
                    L6: Cdj_out_CdsCt
                    L6: Cdj_out_CdsCb
                    L6: Cdj_out_CddCs
                    L6: Cdj_out_CddCd
                    L6: Cdj_out_CddCt
                    L6: Cdj_out_CddCb
            L4: Cdj_out_Od
                L5: Cdj_out_OdC
                    L6: Cdj_out_OdCs
                    L6: Cdj_out_OdCd
                    L6: Cdj_out_OdCt
                    L6: Cdj_out_OdCb
                L5: Cdj_out_OdO
        L3: Ctj_out
            L4: Ctj_out_Ct
        L3: Cbj_out
    L2: Oj_out
        L3: Oj_out_C
            L4: Oj_out_Cs
            L4: Oj_out_Cd
            L4: Oj_out_Ct
            L4: Oj_out_Cb
        L3: Oj_out_O
L1: XH_out
    L2: C_H_out
        L3: Cs_H_out
            L4: Cs_H_out_H2
            L4: Cs_H_out_RH
                L5: Cs_H_out_CH
                    L6: Cs_H_out_CsH
                    L6: Cs_H_out_CdH
                    L6: Cs_H_out_CtH
                    L6: Cs_H_out_CbH
                L5: Cs_H_out_OH
            L4: Cs_H_out_RR
                L5: Cs_H_out_CC
                    L6: Cs_H_out_CsCs
                    L6: Cs_H_out_CsCd
                    L6: Cs_H_out_CsCt
                    L6: Cs_H_out_CsCb
                    L6: Cs_H_out_CdCd
                    L6: Cs_H_out_CdCt
                    L6: Cs_H_out_CdCb
                    L6: Cs_H_out_CtCt
                    L6: Cs_H_out_CtCb
                    L6: Cs_H_out_CbCb
                L5: Cs_H_out_CO
                    L6: Cs_H_out_CsO
                    L6: Cs_H_out_CdO
                    L6: Cs_H_out_CtO
                    L6: Cs_H_out_CbO
                L5: Cs_H_out_OO
        L3: Cd_H_out
            L4: Cd_H_out_RdH
                L5: Cd_H_out_CdH
                    L6: Cd_H_out_CdsH
                    L6: Cd_H_out_CddH
                L5: Cd_H_out_OdH
            L4: Cd_H_out_RdR
                L5: Cd_H_out_CdR
                    L6: Cd_H_out_CdC
                        L7: Cd_H_out_CdsCs
                        L7: Cd_H_out_CdsCd
                        L7: Cd_H_out_CdsCt
                        L7: Cd_H_out_CdsCb
                        L7: Cd_H_out_CddCs
                        L7: Cd_H_out_CddCd
                        L7: Cd_H_out_CddCt
                        L7: Cd_H_out_CddCb
                    L6: Cd_H_out_CdOs
                        L7: Cd_H_out_CdsOs
                        L7: Cd_H_out_CddOs
                L5: Cd_H_out_OdR
                    L6: Cd_H_out_OdC
                        L7: Cd_H_out_OdCs
                        L7: Cd_H_out_OdCd
                        L7: Cd_H_out_OdCt
                        L7: Cd_H_out_OdCb
                    L6: Cd_H_out_OdOs
        L3: Ct_H_out
        L3: Cb_H_out
    L2: O_H_out
        L3: O_H_out_C
            L4: O_H_out_Cs
            L4: O_H_out_Cd
            L4: O_H_out_Ct
            L4: O_H_out_Cb
        L3: O_H_out_O
"""
)

