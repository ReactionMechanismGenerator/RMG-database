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
        distances = {'d12': 2.28662, 'd13': 1.3095, 'd23': 1.30761},
        uncertainties = {'d12': 0.264704, 'd13': 0.0726, 'd23': 0.06722},
    ),
    shortDesc = u"""Fitted to 40 distances.
""",
    longDesc = 
u"""
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=285 label="Csj_out_CsO">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=97 label="R4H_sds">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=303 label="Cs_H_out_CsO">]
[<Entry index=9 label="R7Hall">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
""",
)

entry(
    index = 2,
    label = "Y_rad_out",
    group = "OR{Cj_out, Oj_out}",
    distances = DistanceData(distances={}),
)

entry(
    index = 3,
    label = "XH_out",
    group = "OR{C_H_out, O_H_out}",
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
        distances = {'d12': -0.374077, 'd13': -0.010788, 'd23': -0.015401},
        uncertainties = {'d12': 0.441435, 'd13': 0.056082, 'd23': 0.045976},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
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
        distances = {'d12': -0.374077, 'd13': -0.010788, 'd23': -0.015401},
        uncertainties = {'d12': 0.441435, 'd13': 0.056082, 'd23': 0.045976},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
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
    index = 84,
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
    index = 85,
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
    index = 86,
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
        distances = {'d12': -0.138585, 'd13': 0.016711, 'd23': 0.0158},
        uncertainties = {'d12': 1.60888, 'd13': 0.243793, 'd23': 0.088296},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=16 label="R3H_ss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
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
        distances = {'d12': -0.138585, 'd13': 0.016711, 'd23': 0.0158},
        uncertainties = {'d12': 1.60888, 'd13': 0.243793, 'd23': 0.088296},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=16 label="R3H_ss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
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
    index = 87,
    label = "R3H_sd",
    group = 
"""
1 *4 R!H ux {2,D} {3,S}
2 *2 R!H u0 {1,D} {4,S}
3 *1 R!H u1 {1,S}
4 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 88,
    label = "R3H_st",
    group = 
"""
1 *4 R!H ux {2,T} {3,S}
2 *2 R!H u0 {1,T} {4,S}
3 *1 R!H u1 {1,S}
4 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 89,
    label = "R3H_sb",
    group = 
"""
1 *4 R!H ux {2,B} {3,S}
2 *2 R!H u0 {1,B} {4,S}
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
    index = 90,
    label = "R3H_ds",
    group = 
"""
1 *4 R!H ux {2,S} {3,D}
2 *2 R!H u0 {1,S} {4,S}
3 *1 R!H u1 {1,D}
4 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 91,
    label = "R3H_ts",
    group = 
"""
1 *4 R!H ux {2,S} {3,T}
2 *2 R!H u0 {1,S} {4,S}
3 *1 R!H u1 {1,T}
4 *3 H   u0 {2,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 92,
    label = "R3H_bs",
    group = 
"""
1 *4 R!H ux {2,S} {3,B}
2 *2 R!H u0 {1,S} {4,S}
3 *1 R!H u1 {1,B}
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
    index = 93,
    label = "R3H_bb",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,B}
3 *2 R!H u0 {2,B} {4,S}
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
        distances = {'d12': 0.253866, 'd13': 0.034161, 'd23': 0.037123},
        uncertainties = {'d12': 0.311093, 'd13': 0.074745, 'd23': 0.100877},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
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
        distances = {'d12': 0.256695, 'd13': 0.031989, 'd23': 0.033143},
        uncertainties = {'d12': 0.427055, 'd13': 0.104668, 'd23': 0.149159},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=20 label="R4H_sss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
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
    index = 94,
    label = "R4H_ssd",
    group = 
"""
1 *5 R!H ux {2,S} {3,D}
2 *4 R!H ux {1,S} {4,S}
3 *2 R!H u0 {1,D} {5,S}
4 *1 R!H u1 {2,S}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 95,
    label = "R4H_sst",
    group = 
"""
1 *5 R!H ux {2,S} {3,T}
2 *4 R!H ux {1,S} {4,S}
3 *2 R!H u0 {1,T} {5,S}
4 *1 R!H u1 {2,S}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 96,
    label = "R4H_ssb",
    group = 
"""
1 *5 R!H ux {2,S} {3,B}
2 *4 R!H ux {1,S} {4,S}
3 *2 R!H u0 {1,B} {5,S}
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
        distances = {'d12': 0.248916, 'd13': 0.03796, 'd23': 0.044089},
        uncertainties = {'d12': 0.329751, 'd13': 0.072013, 'd23': 0.059881},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 97,
    label = "R4H_sds",
    group = 
"""
1 *5 R!H ux {2,D} {3,S}
2 *4 R!H ux {1,D} {4,S}
3 *2 R!H u0 {1,S} {5,S}
4 *1 R!H u1 {2,S}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.248916, 'd13': 0.03796, 'd23': 0.044089},
        uncertainties = {'d12': 0.329751, 'd13': 0.072013, 'd23': 0.059881},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 98,
    label = "R4H_sts",
    group = 
"""
1 *5 R!H ux {2,T} {3,S}
2 *4 R!H ux {1,T} {4,S}
3 *2 R!H u0 {1,S} {5,S}
4 *1 R!H u1 {2,S}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 99,
    label = "R4H_sbs",
    group = 
"""
1 *5 R!H ux {2,B} {3,S}
2 *4 R!H ux {1,B} {4,S}
3 *2 R!H u0 {1,S} {5,S}
4 *1 R!H u1 {2,S}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
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
    index = 100,
    label = "R4H_dss",
    group = 
"""
1 *5 R!H ux {2,S} {3,S}
2 *4 R!H ux {1,S} {4,D}
3 *2 R!H u0 {1,S} {5,S}
4 *1 R!H u1 {2,D}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 101,
    label = "R4H_tss",
    group = 
"""
1 *5 R!H ux {2,S} {3,S}
2 *4 R!H ux {1,S} {4,T}
3 *2 R!H u0 {1,S} {5,S}
4 *1 R!H u1 {2,T}
5 *3 H   u0 {3,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 102,
    label = "R4H_bss",
    group = 
"""
1 *5 R!H ux {2,S} {3,S}
2 *4 R!H ux {1,S} {4,B}
3 *2 R!H u0 {1,S} {5,S}
4 *1 R!H u1 {2,B}
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
    index = 103,
    label = "R4H_dsd",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *5 R!H ux {2,S} {4,D}
4 *2 R!H u0 {3,D} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 104,
    label = "R4H_tsd",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *5 R!H ux {2,S} {4,D}
4 *2 R!H u0 {3,D} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 105,
    label = "R4H_bsd",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *5 R!H ux {2,S} {4,D}
4 *2 R!H u0 {3,D} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 106,
    label = "R4H_dst",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *5 R!H ux {2,S} {4,T}
4 *2 R!H u0 {3,T} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 107,
    label = "R4H_tst",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *5 R!H ux {2,S} {4,T}
4 *2 R!H u0 {3,T} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 108,
    label = "R4H_bst",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *5 R!H ux {2,S} {4,T}
4 *2 R!H u0 {3,T} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 109,
    label = "R4H_dsb",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *5 R!H ux {2,S} {4,B}
4 *2 R!H u0 {3,B} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 110,
    label = "R4H_tsb",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *5 R!H ux {2,S} {4,B}
4 *2 R!H u0 {3,B} {5,S}
5 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 111,
    label = "R4H_bsb",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *5 R!H ux {2,S} {4,B}
4 *2 R!H u0 {3,B} {5,S}
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
        distances = {'d12': 0.226393, 'd13': -0.016092, 'd23': -0.0128},
        uncertainties = {'d12': 0.223044, 'd13': 0.103527, 'd23': 0.0783},
    ),
    shortDesc = u"""Fitted to 14 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=303 label="Cs_H_out_CsO">]
[<Entry index=28 label="R5H_ssss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=285 label="Csj_out_CsO">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 28,
    label = "R5H_ssss",
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
        distances = {'d12': 0.211365, 'd13': -0.020284, 'd23': -0.017394},
        uncertainties = {'d12': 0.246278, 'd13': 0.114236, 'd23': 0.086544},
    ),
    shortDesc = u"""Fitted to 12 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=303 label="Cs_H_out_CsO">]
[<Entry index=28 label="R5H_ssss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=285 label="Csj_out_CsO">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 29,
    label = "R5H_sssr",
    group = 
"""
1 *6 R!H ux {2,S} {3,S}
2 *5 R!H ux {1,S} {4,[D,T,B]}
3 *4 R!H ux {1,S} {5,S}
4 *2 R!H u0 {2,[D,T,B]} {6,S}
5 *1 R!H u1 {3,S}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 112,
    label = "R5H_sssd",
    group = 
"""
1 *6 R!H ux {2,S} {3,S}
2 *5 R!H ux {1,S} {4,D}
3 *4 R!H ux {1,S} {5,S}
4 *2 R!H u0 {2,D} {6,S}
5 *1 R!H u1 {3,S}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 113,
    label = "R5H_ssst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,T}
5 *2 R!H u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 114,
    label = "R5H_sssb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,B}
5 *2 R!H u0 {4,B} {6,S}
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
    distances = DistanceData(
        distances = {'d12': 0.286504, 'd13': 0.000674, 'd23': 0.005579},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 115,
    label = "R5H_ssds",
    group = 
"""
1 *6 R!H ux {2,D} {3,S}
2 *5 R!H ux {1,D} {4,S}
3 *4 R!H ux {1,S} {5,S}
4 *2 R!H u0 {2,S} {6,S}
5 *1 R!H u1 {3,S}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.286504, 'd13': 0.000674, 'd23': 0.005579},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 116,
    label = "R5H_ssts",
    group = 
"""
1 *6 R!H ux {2,T} {3,S}
2 *5 R!H ux {1,T} {4,S}
3 *4 R!H ux {1,S} {5,S}
4 *2 R!H u0 {2,S} {6,S}
5 *1 R!H u1 {3,S}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 117,
    label = "R5H_ssbs",
    group = 
"""
1 *6 R!H ux {2,B} {3,S}
2 *5 R!H ux {1,B} {4,S}
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
    distances = DistanceData(
        distances = {'d12': 0.286504, 'd13': 0.000674, 'd23': 0.005579},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 118,
    label = "R5H_sdss",
    group = 
"""
1 *6 R!H ux {2,S} {3,D}
2 *5 R!H ux {1,S} {4,S}
3 *4 R!H ux {1,D} {5,S}
4 *2 R!H u0 {2,S} {6,S}
5 *1 R!H u1 {3,S}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.286504, 'd13': 0.000674, 'd23': 0.005579},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 119,
    label = "R5H_stss",
    group = 
"""
1 *6 R!H ux {2,S} {3,T}
2 *5 R!H ux {1,S} {4,S}
3 *4 R!H ux {1,T} {5,S}
4 *2 R!H u0 {2,S} {6,S}
5 *1 R!H u1 {3,S}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 120,
    label = "R5H_sbss",
    group = 
"""
1 *6 R!H ux {2,S} {3,B}
2 *5 R!H ux {1,S} {4,S}
3 *4 R!H ux {1,B} {5,S}
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
1 *6 R!H ux {2,S} {3,S}
2 *5 R!H ux {1,S} {4,S}
3 *4 R!H ux {1,S} {5,[D,T,B]}
4 *2 R!H u0 {2,S} {6,S}
5 *1 R!H u1 {3,[D,T,B]}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 121,
    label = "R5H_dsss",
    group = 
"""
1 *6 R!H ux {2,S} {3,S}
2 *5 R!H ux {1,S} {4,S}
3 *4 R!H ux {1,S} {5,D}
4 *2 R!H u0 {2,S} {6,S}
5 *1 R!H u1 {3,D}
6 *3 H   u0 {4,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 122,
    label = "R5H_tsss",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 123,
    label = "R5H_bsss",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
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
    index = 124,
    label = "R5H_sdsd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,D}
3 *6 R!H ux {2,D} {4,S}
4 *5 R!H ux {3,S} {5,D}
5 *2 R!H u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 125,
    label = "R5H_stsd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *5 R!H ux {3,S} {5,D}
5 *2 R!H u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 126,
    label = "R5H_sbsd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
4 *5 R!H ux {3,S} {5,D}
5 *2 R!H u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 127,
    label = "R5H_sdst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,D}
3 *6 R!H ux {2,D} {4,S}
4 *5 R!H ux {3,S} {5,T}
5 *2 R!H u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 128,
    label = "R5H_stst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *5 R!H ux {3,S} {5,T}
5 *2 R!H u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 129,
    label = "R5H_sbst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
4 *5 R!H ux {3,S} {5,T}
5 *2 R!H u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 130,
    label = "R5H_sdsb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,D}
3 *6 R!H ux {2,D} {4,S}
4 *5 R!H ux {3,S} {5,B}
5 *2 R!H u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 131,
    label = "R5H_stsb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *5 R!H ux {3,S} {5,B}
5 *2 R!H u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 132,
    label = "R5H_sbsb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
4 *5 R!H ux {3,S} {5,B}
5 *2 R!H u0 {4,B} {6,S}
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
    index = 133,
    label = "R5H_dssd",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,D}
5 *2 R!H u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 134,
    label = "R5H_tssd",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,D}
5 *2 R!H u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 135,
    label = "R5H_bssd",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,D}
5 *2 R!H u0 {4,D} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 136,
    label = "R5H_dsst",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,T}
5 *2 R!H u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 137,
    label = "R5H_tsst",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,T}
5 *2 R!H u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 138,
    label = "R5H_bsst",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,T}
5 *2 R!H u0 {4,T} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 139,
    label = "R5H_dssb",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,B}
5 *2 R!H u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 140,
    label = "R5H_tssb",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,B}
5 *2 R!H u0 {4,B} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 141,
    label = "R5H_bssb",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *5 R!H ux {3,S} {5,B}
5 *2 R!H u0 {4,B} {6,S}
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
    index = 142,
    label = "R5H_dsds",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *5 R!H ux {3,D} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 143,
    label = "R5H_tsds",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *5 R!H ux {3,D} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 144,
    label = "R5H_bsds",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *5 R!H ux {3,D} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 145,
    label = "R5H_dsts",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *5 R!H ux {3,T} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 146,
    label = "R5H_tsts",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *5 R!H ux {3,T} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 147,
    label = "R5H_bsts",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *5 R!H ux {3,T} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 148,
    label = "R5H_dsbs",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *5 R!H ux {3,B} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 149,
    label = "R5H_tsbs",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *5 R!H ux {3,B} {5,S}
5 *2 R!H u0 {4,S} {6,S}
6 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 150,
    label = "R5H_bsbs",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *5 R!H ux {3,B} {5,S}
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
    distances = DistanceData(
        distances = {'d12': 0.179592, 'd13': -0.046361, 'd23': -0.046147},
        uncertainties = {'d12': 0.179618, 'd13': 0.602642, 'd23': 0.58002},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=44 label="R6H_sssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
""",
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
    distances = DistanceData(
        distances = {'d12': 0.179592, 'd13': -0.046361, 'd23': -0.046147},
        uncertainties = {'d12': 0.179618, 'd13': 0.602642, 'd23': 0.58002},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=44 label="R6H_sssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
""",
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
    index = 151,
    label = "R6H_ssssd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 152,
    label = "R6H_sssst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 153,
    label = "R6H_ssssb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 46,
    label = "R6H_sssrs",
    group = 
"""
1 *7 R!H ux {2,S} {3,[D,T,B]}
2 *6 R!H ux {1,S} {4,S}
3 *5 R!H ux {1,[D,T,B]} {5,S}
4 *4 R!H ux {2,S} {6,S}
5 *2 R!H u0 {3,S} {7,S}
6 *1 R!H u1 {4,S}
7 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 154,
    label = "R6H_sssds",
    group = 
"""
1 *7 R!H ux {2,S} {3,D}
2 *6 R!H ux {1,S} {4,S}
3 *5 R!H ux {1,D} {5,S}
4 *4 R!H ux {2,S} {6,S}
5 *2 R!H u0 {3,S} {7,S}
6 *1 R!H u1 {4,S}
7 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 155,
    label = "R6H_sssts",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,T}
5 *5 R!H ux {4,T} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 156,
    label = "R6H_sssbs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,B}
5 *5 R!H ux {4,B} {6,S}
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
    index = 157,
    label = "R6H_ssdss",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 158,
    label = "R6H_sstss",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 159,
    label = "R6H_ssbss",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
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
1 *7 R!H ux {2,S} {3,S}
2 *6 R!H ux {1,S} {4,[D,T,B]}
3 *5 R!H ux {1,S} {5,S}
4 *4 R!H ux {2,[D,T,B]} {6,S}
5 *2 R!H u0 {3,S} {7,S}
6 *1 R!H u1 {4,S}
7 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 160,
    label = "R6H_sdsss",
    group = 
"""
1 *7 R!H ux {2,S} {3,S}
2 *6 R!H ux {1,S} {4,D}
3 *5 R!H ux {1,S} {5,S}
4 *4 R!H ux {2,D} {6,S}
5 *2 R!H u0 {3,S} {7,S}
6 *1 R!H u1 {4,S}
7 *3 H   u0 {5,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 161,
    label = "R6H_stsss",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 162,
    label = "R6H_sbsss",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
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
    index = 163,
    label = "R6H_dssss",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 164,
    label = "R6H_tssss",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 165,
    label = "R6H_bssss",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
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
    index = 166,
    label = "R6H_ssdsd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 167,
    label = "R6H_sstsd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 168,
    label = "R6H_ssbsd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 169,
    label = "R6H_ssdst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 170,
    label = "R6H_sstst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 171,
    label = "R6H_ssbst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 172,
    label = "R6H_ssdsb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 173,
    label = "R6H_sstsb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 174,
    label = "R6H_ssbsb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
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
    index = 175,
    label = "R6H_sdssd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,D}
3 *6 R!H ux {2,D} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 176,
    label = "R6H_stssd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 177,
    label = "R6H_sbssd",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 178,
    label = "R6H_sdsst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,D}
3 *6 R!H ux {2,D} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 179,
    label = "R6H_stsst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 180,
    label = "R6H_sbsst",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 181,
    label = "R6H_sdssb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,D}
3 *6 R!H ux {2,D} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 182,
    label = "R6H_stssb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 183,
    label = "R6H_sbssb",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
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
    index = 184,
    label = "R6H_dsssd",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 185,
    label = "R6H_tsssd",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 186,
    label = "R6H_bsssd",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 187,
    label = "R6H_dssst",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 188,
    label = "R6H_tssst",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 189,
    label = "R6H_bssst",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 190,
    label = "R6H_dsssb",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 191,
    label = "R6H_tsssb",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 192,
    label = "R6H_bsssb",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
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
    index = 193,
    label = "R6H_sdsds",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,D}
3 *6 R!H ux {2,D} {4,S}
4 *7 R!H ux {3,S} {5,D}
5 *5 R!H ux {4,D} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 194,
    label = "R6H_stsds",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *7 R!H ux {3,S} {5,D}
5 *5 R!H ux {4,D} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 195,
    label = "R6H_sbsds",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
4 *7 R!H ux {3,S} {5,D}
5 *5 R!H ux {4,D} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 196,
    label = "R6H_sdsts",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,D}
3 *6 R!H ux {2,D} {4,S}
4 *7 R!H ux {3,S} {5,T}
5 *5 R!H ux {4,T} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 197,
    label = "R6H_ststs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *7 R!H ux {3,S} {5,T}
5 *5 R!H ux {4,T} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 198,
    label = "R6H_sbsts",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
4 *7 R!H ux {3,S} {5,T}
5 *5 R!H ux {4,T} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 199,
    label = "R6H_sdsbs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,D}
3 *6 R!H ux {2,D} {4,S}
4 *7 R!H ux {3,S} {5,B}
5 *5 R!H ux {4,B} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 200,
    label = "R6H_stsbs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,T}
3 *6 R!H ux {2,T} {4,S}
4 *7 R!H ux {3,S} {5,B}
5 *5 R!H ux {4,B} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 201,
    label = "R6H_sbsbs",
    group = 
"""
1 *1 R!H u1 {2,S}
2 *4 R!H ux {1,S} {3,B}
3 *6 R!H ux {2,B} {4,S}
4 *7 R!H ux {3,S} {5,B}
5 *5 R!H ux {4,B} {6,S}
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
    index = 202,
    label = "R6H_dssds",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,D}
5 *5 R!H ux {4,D} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 203,
    label = "R6H_tssds",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,D}
5 *5 R!H ux {4,D} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 204,
    label = "R6H_bssds",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,D}
5 *5 R!H ux {4,D} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 205,
    label = "R6H_dssts",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,T}
5 *5 R!H ux {4,T} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 206,
    label = "R6H_tssts",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,T}
5 *5 R!H ux {4,T} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 207,
    label = "R6H_bssts",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,T}
5 *5 R!H ux {4,T} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 208,
    label = "R6H_dssbs",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,B}
5 *5 R!H ux {4,B} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 209,
    label = "R6H_tssbs",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,B}
5 *5 R!H ux {4,B} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 210,
    label = "R6H_bssbs",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,S}
4 *7 R!H ux {3,S} {5,B}
5 *5 R!H ux {4,B} {6,S}
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
    index = 211,
    label = "R6H_dsdss",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 212,
    label = "R6H_tsdss",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 213,
    label = "R6H_bsdss",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 214,
    label = "R6H_dstss",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 215,
    label = "R6H_tstss",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 216,
    label = "R6H_bstss",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 217,
    label = "R6H_dsbss",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 218,
    label = "R6H_tsbss",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,S}
6 *2 R!H u0 {5,S} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 219,
    label = "R6H_bsbss",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
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
    index = 220,
    label = "R6H_dsdsd",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 221,
    label = "R6H_tsdsd",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 222,
    label = "R6H_bsdsd",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 223,
    label = "R6H_dstsd",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 224,
    label = "R6H_tstsd",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 225,
    label = "R6H_bstsd",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 226,
    label = "R6H_dsbsd",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 227,
    label = "R6H_tsbsd",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 228,
    label = "R6H_bsbsd",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,D}
6 *2 R!H u0 {5,D} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 229,
    label = "R6H_dsdst",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 230,
    label = "R6H_tsdst",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 231,
    label = "R6H_bsdst",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 232,
    label = "R6H_dstst",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 233,
    label = "R6H_tstst",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 234,
    label = "R6H_bstst",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 235,
    label = "R6H_dsbst",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 236,
    label = "R6H_tsbst",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 237,
    label = "R6H_bsbst",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,T}
6 *2 R!H u0 {5,T} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 238,
    label = "R6H_dsdsb",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 239,
    label = "R6H_tsdsb",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 240,
    label = "R6H_bsdsb",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,D}
4 *7 R!H ux {3,D} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 241,
    label = "R6H_dstsb",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 242,
    label = "R6H_tstsb",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 243,
    label = "R6H_bstsb",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,T}
4 *7 R!H ux {3,T} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 244,
    label = "R6H_dsbsb",
    group = 
"""
1 *1 R!H u1 {2,D}
2 *4 R!H ux {1,D} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 245,
    label = "R6H_tsbsb",
    group = 
"""
1 *1 R!H u1 {2,T}
2 *4 R!H ux {1,T} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
7 *3 H   u0 {6,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 246,
    label = "R6H_bsbsb",
    group = 
"""
1 *1 R!H u1 {2,B}
2 *4 R!H ux {1,B} {3,S}
3 *6 R!H ux {2,S} {4,B}
4 *7 R!H ux {3,B} {5,S}
5 *5 R!H ux {4,S} {6,B}
6 *2 R!H u0 {5,B} {7,S}
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
    distances = DistanceData(
        distances = {'d12': 0.208902, 'd13': -0.042516, 'd23': -0.042302},
        uncertainties = {'d12': 0.179618, 'd13': 0.62446, 'd23': 0.602658},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=9 label="R7Hall">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
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
        distances = {'d12': 0.000228, 'd13': 0.02839, 'd23': 0.000473},
        uncertainties = {'d12': 0.270562, 'd13': 0.064344, 'd23': 0.046369},
    ),
    shortDesc = u"""Fitted to 29 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=9 label="R7Hall">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=285 label="Csj_out_CsO">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=16 label="R3H_ss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 76,
    label = "Csj_out",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    R ux {1,S}
3    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.000228, 'd13': 0.02839, 'd23': 0.000473},
        uncertainties = {'d12': 0.270562, 'd13': 0.064344, 'd23': 0.046369},
    ),
    shortDesc = u"""Fitted to 29 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=9 label="R7Hall">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=285 label="Csj_out_CsO">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=16 label="R3H_ss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 247,
    label = "Csj_out_H2",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    H u0 {1,S}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.013854, 'd13': 0.045763, 'd23': -0.015571},
        uncertainties = {'d12': 0.281084, 'd13': 0.069088, 'd23': 0.038689},
    ),
    shortDesc = u"""Fitted to 17 distances.
""",
    longDesc = 
u"""
[<Entry index=9 label="R7Hall">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=44 label="R6H_sssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 248,
    label = "Csj_out_RH",
    group = 
"""
1 *1 C   u1 {2,S} {3,S}
2    R!H ux {1,S}
3    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.631901, 'd13': 0.023302, 'd23': 0.04851},
        uncertainties = {'d12': 2.07216, 'd13': 0.305519, 'd23': 0.228614},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 257,
    label = "Csj_out_CH",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    C ux {1,S}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.631901, 'd13': 0.023302, 'd23': 0.04851},
        uncertainties = {'d12': 2.07216, 'd13': 0.305519, 'd23': 0.228614},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 271,
    label = "Csj_out_CsH",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cs ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.631901, 'd13': 0.023302, 'd23': 0.04851},
        uncertainties = {'d12': 2.07216, 'd13': 0.305519, 'd23': 0.228614},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 272,
    label = "Csj_out_CdH",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cd ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 273,
    label = "Csj_out_CtH",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 274,
    label = "Csj_out_CbH",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 258,
    label = "Csj_out_OH",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    O ux {1,S}
3    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 249,
    label = "Csj_out_RR",
    group = 
"""
1 *1 C   u1 {2,S} {3,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.182712, 'd13': -0.010345, 'd23': 0.025845},
        uncertainties = {'d12': 0.320455, 'd13': 0.075614, 'd23': 0.070313},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=285 label="Csj_out_CsO">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 259,
    label = "Csj_out_CC",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    C ux {1,S}
3    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.194837, 'd13': -0.012726, 'd23': 0.028924},
        uncertainties = {'d12': 0.342385, 'd13': 0.080945, 'd23': 0.069824},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=16 label="R3H_ss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 275,
    label = "Csj_out_CsCs",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.03236, 'd13': 0.004142, 'd23': 0.034176},
        uncertainties = {'d12': 0.204354, 'd13': 0.086998, 'd23': 0.093793},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=16 label="R3H_ss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 276,
    label = "Csj_out_CsCd",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.550964, 'd13': 0.021012, 'd23': -0.05395},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 277,
    label = "Csj_out_CsCt",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 278,
    label = "Csj_out_CsCb",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 279,
    label = "Csj_out_CdCd",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 280,
    label = "Csj_out_CdCt",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 281,
    label = "Csj_out_CdCb",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 282,
    label = "Csj_out_CtCt",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 283,
    label = "Csj_out_CtCb",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 284,
    label = "Csj_out_CbCb",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 260,
    label = "Csj_out_CO",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    C ux {1,S}
3    O ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.00725, 'd13': 0.026962, 'd23': -0.022391},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=285 label="Csj_out_CsO">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 285,
    label = "Csj_out_CsO",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cs ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.00725, 'd13': 0.026962, 'd23': -0.022391},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=285 label="Csj_out_CsO">, <Entry index=13 label="O_H_out">]
""",
)

entry(
    index = 286,
    label = "Csj_out_CdO",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cd ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 287,
    label = "Csj_out_CtO",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Ct ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 288,
    label = "Csj_out_CbO",
    group = 
"""
1 *1 C  u1 {2,S} {3,S}
2    Cb ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 261,
    label = "Csj_out_OO",
    group = 
"""
1 *1 C u1 {2,S} {3,S}
2    O ux {1,S}
3    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 77,
    label = "Cdj_out",
    group = 
"""
1 *1 C u1 {2,D}
2    R ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 250,
    label = "Cdj_out_C",
    group = 
"""
1 *1 C u1 {2,D}
2    C ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 262,
    label = "Cdj_out_Cd",
    group = 
"""
1 *1 C  u1 {2,D}
2    Cd ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 263,
    label = "Cdj_out_Cdd",
    group = 
"""
1 *1 C   u1 {2,D}
2    Cdd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 251,
    label = "Cdj_out_O",
    group = 
"""
1 *1 C u1 {2,D}
2    O ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 78,
    label = "Ctj_out",
    group = 
"""
1 *1 C u1 {2,T}
2    R ux {1,T}
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
        distances = {'d12': -0.000561, 'd13': -0.069793, 'd23': -0.001163},
        uncertainties = {'d12': 0.298461, 'd13': 0.105962, 'd23': 0.119419},
    ),
    shortDesc = u"""Fitted to 11 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=303 label="Cs_H_out_CsO">]
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=97 label="R4H_sds">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=20 label="R4H_sss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
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
        distances = {'d12': 0.000228, 'd13': 0.004821, 'd23': 0.024043},
        uncertainties = {'d12': 0.270562, 'd13': 0.054834, 'd23': 0.069588},
    ),
    shortDesc = u"""Fitted to 29 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=303 label="Cs_H_out_CsO">]
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 80,
    label = "Cs_H_out",
    group = 
"""
1 *2 Cs ux {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.000228, 'd13': 0.004821, 'd23': 0.024043},
        uncertainties = {'d12': 0.270562, 'd13': 0.054834, 'd23': 0.069588},
    ),
    shortDesc = u"""Fitted to 29 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=303 label="Cs_H_out_CsO">]
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 252,
    label = "Cs_H_out_H2",
    group = 
"""
1 *2 C ux {2,S} {3,S} {4,S}
2 *3 H u0 {1,S}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.013854, 'd13': -0.009598, 'd23': 0.03979},
        uncertainties = {'d12': 0.281084, 'd13': 0.052131, 'd23': 0.080574},
    ),
    shortDesc = u"""Fitted to 17 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=271 label="Csj_out_CsH">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=9 label="R7Hall">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=276 label="Csj_out_CsCd">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=97 label="R4H_sds">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=118 label="R5H_sdss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=44 label="R6H_sssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=115 label="R5H_ssds">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=14 label="R2H_s">, <Entry index=259 label="Csj_out_CC">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=20 label="R4H_sss">, <Entry index=11 label="Oj_out">, <Entry index=252 label="Cs_H_out_H2">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=252 label="Cs_H_out_H2">]
""",
)

entry(
    index = 253,
    label = "Cs_H_out_RH",
    group = 
"""
1 *2 C   ux {2,S} {3,S} {4,S}
2 *3 H   u0 {1,S}
3    R!H ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.631901, 'd13': 0.039877, 'd23': 0.031935},
        uncertainties = {'d12': 2.07216, 'd13': 0.297528, 'd23': 0.361779},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
""",
)

entry(
    index = 264,
    label = "Cs_H_out_CH",
    group = 
"""
1 *2 C ux {2,S} {3,S} {4,S}
2 *3 H u0 {1,S}
3    C ux {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.631901, 'd13': 0.039877, 'd23': 0.031935},
        uncertainties = {'d12': 2.07216, 'd13': 0.297528, 'd23': 0.361779},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
""",
)

entry(
    index = 289,
    label = "Cs_H_out_CsH",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.631901, 'd13': 0.039877, 'd23': 0.031935},
        uncertainties = {'d12': 2.07216, 'd13': 0.297528, 'd23': 0.361779},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=289 label="Cs_H_out_CsH">]
""",
)

entry(
    index = 290,
    label = "Cs_H_out_CdH",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 291,
    label = "Cs_H_out_CtH",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 292,
    label = "Cs_H_out_CbH",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 265,
    label = "Cs_H_out_OH",
    group = 
"""
1 *2 C ux {2,S} {3,S} {4,S}
2 *3 H u0 {1,S}
3    O ux {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 254,
    label = "Cs_H_out_RR",
    group = 
"""
1 *2 C   ux {2,S} {3,S} {4,S}
2 *3 H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.182712, 'd13': 0.029572, 'd23': -0.014071},
        uncertainties = {'d12': 0.320455, 'd13': 0.074802, 'd23': 0.069067},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=303 label="Cs_H_out_CsO">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 266,
    label = "Cs_H_out_CC",
    group = 
"""
1 *2 C ux {2,S} {3,S} {4,S}
2 *3 H u0 {1,S}
3    C ux {1,S}
4    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.194837, 'd13': 0.032537, 'd23': -0.016338},
        uncertainties = {'d12': 0.342385, 'd13': 0.072862, 'd23': 0.074398},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=266 label="Cs_H_out_CC">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 293,
    label = "Cs_H_out_CsCs",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.03236, 'd13': 0.033395, 'd23': 0.004922},
        uncertainties = {'d12': 0.204354, 'd13': 0.100956, 'd23': 0.092126},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=16 label="R3H_ss">, <Entry index=11 label="Oj_out">, <Entry index=293 label="Cs_H_out_CsCs">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=293 label="Cs_H_out_CsCs">]
""",
)

entry(
    index = 294,
    label = "Cs_H_out_CsCd",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.550964, 'd13': -0.004613, 'd23': -0.028325},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="R2H_s">, <Entry index=247 label="Csj_out_H2">, <Entry index=294 label="Cs_H_out_CsCd">]
""",
)

entry(
    index = 295,
    label = "Cs_H_out_CsCt",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 296,
    label = "Cs_H_out_CsCb",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 297,
    label = "Cs_H_out_CdCd",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 298,
    label = "Cs_H_out_CdCt",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 299,
    label = "Cs_H_out_CdCb",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 300,
    label = "Cs_H_out_CtCt",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 301,
    label = "Cs_H_out_CtCb",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 302,
    label = "Cs_H_out_CbCb",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 267,
    label = "Cs_H_out_CO",
    group = 
"""
1 *2 C ux {2,S} {3,S} {4,S}
2 *3 H u0 {1,S}
3    C ux {1,S}
4    O ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.00725, 'd13': -0.016877, 'd23': 0.021448},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=303 label="Cs_H_out_CsO">]
""",
)

entry(
    index = 303,
    label = "Cs_H_out_CsO",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.00725, 'd13': -0.016877, 'd23': 0.021448},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=303 label="Cs_H_out_CsO">]
""",
)

entry(
    index = 304,
    label = "Cs_H_out_CdO",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 305,
    label = "Cs_H_out_CtO",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 306,
    label = "Cs_H_out_CbO",
    group = 
"""
1 *2 C  ux {2,S} {3,S} {4,S}
2 *3 H  u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 268,
    label = "Cs_H_out_OO",
    group = 
"""
1 *2 C ux {2,S} {3,S} {4,S}
2 *3 H u0 {1,S}
3    O ux {1,S}
4    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 81,
    label = "Cd_H_out",
    group = 
"""
1 *2 Cd ux {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 255,
    label = "Cd_H_out_C",
    group = 
"""
1 *2 Cd ux {2,S} {3,D}
2 *3 H  u0 {1,S}
3    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 269,
    label = "Cd_H_out_Cd",
    group = 
"""
1 *2 Cd ux {2,S} {3,D}
2 *3 H  u0 {1,S}
3    Cd ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 307,
    label = "Cd_H_out_CdH",
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
    index = 308,
    label = "Cd_H_out_CdC",
    group = 
"""
1 *2 Cd ux {2,S} {3,D} {4,S}
2 *3 H  u0 {1,S}
3    Cd ux {1,D}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 309,
    label = "Cd_H_out_CdCs",
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
    index = 310,
    label = "Cd_H_out_CdCd",
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
    index = 311,
    label = "Cd_H_out_CdCt",
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
    index = 312,
    label = "Cd_H_out_CdCb",
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
    index = 313,
    label = "Cd_H_out_CdO",
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
    index = 270,
    label = "Cd_H_out_Cdd",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D}
2 *3 H   u0 {1,S}
3    Cdd ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 314,
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
    index = 315,
    label = "Cd_H_out_CddC",
    group = 
"""
1 *2 Cd  ux {2,S} {3,D} {4,S}
2 *3 H   u0 {1,S}
3    Cdd u0 {1,D}
4    C   ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 316,
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
    index = 317,
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
    index = 318,
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
    index = 319,
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
    index = 320,
    label = "Cd_H_out_CddO",
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
    index = 256,
    label = "Cd_H_out_O",
    group = 
"""
1 *2 Cd ux {2,S} {3,D}
2 *3 H  u0 {1,S}
3    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 321,
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
    index = 322,
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
    index = 323,
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
    index = 324,
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
    index = 325,
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
    index = 326,
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
    index = 327,
    label = "Cd_H_out_OdO",
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
    index = 82,
    label = "Ct_H_out",
    group = 
"""
1 *2 Ct u0 {2,S}
2 *3 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 83,
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
1 *2 O ux {2,S}
2 *3 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.000561, 'd13': -0.011852, 'd23': -0.059104},
        uncertainties = {'d12': 0.298461, 'd13': 0.122404, 'd23': 0.073085},
    ),
    shortDesc = u"""Fitted to 11 distances.
""",
    longDesc = 
u"""
[<Entry index=9 label="R7Hall">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=11 label="Oj_out">, <Entry index=13 label="O_H_out">]
[<Entry index=44 label="R6H_sssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=97 label="R4H_sds">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
[<Entry index=20 label="R4H_sss">, <Entry index=247 label="Csj_out_H2">, <Entry index=13 label="O_H_out">]
[<Entry index=28 label="R5H_ssss">, <Entry index=285 label="Csj_out_CsO">, <Entry index=13 label="O_H_out">]
[<Entry index=16 label="R3H_ss">, <Entry index=275 label="Csj_out_CsCs">, <Entry index=13 label="O_H_out">]
""",
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
            L4: R3H_sd
            L4: R3H_st
            L4: R3H_sb
        L3: R3H_rs
            L4: R3H_ds
            L4: R3H_ts
            L4: R3H_bs
        L3: R3H_rr
            L4: R3H_bb
    L2: R4Hall
        L3: R4H_sss
        L3: R4H_ssr
            L4: R4H_ssd
            L4: R4H_sst
            L4: R4H_ssb
        L3: R4H_srs
            L4: R4H_sds
            L4: R4H_sts
            L4: R4H_sbs
        L3: R4H_rss
            L4: R4H_dss
            L4: R4H_tss
            L4: R4H_bss
        L3: R4H_srr
        L3: R4H_rrs
        L3: R4H_rsr
            L4: R4H_dsd
            L4: R4H_tsd
            L4: R4H_bsd
            L4: R4H_dst
            L4: R4H_tst
            L4: R4H_bst
            L4: R4H_dsb
            L4: R4H_tsb
            L4: R4H_bsb
        L3: R4H_rrr
    L2: R5Hall
        L3: R5H_ssss
        L3: R5H_sssr
            L4: R5H_sssd
            L4: R5H_ssst
            L4: R5H_sssb
        L3: R5H_ssrs
            L4: R5H_ssds
            L4: R5H_ssts
            L4: R5H_ssbs
        L3: R5H_srss
            L4: R5H_sdss
            L4: R5H_stss
            L4: R5H_sbss
        L3: R5H_rsss
            L4: R5H_dsss
            L4: R5H_tsss
            L4: R5H_bsss
        L3: R5H_ssrr
        L3: R5H_srsr
            L4: R5H_sdsd
            L4: R5H_stsd
            L4: R5H_sbsd
            L4: R5H_sdst
            L4: R5H_stst
            L4: R5H_sbst
            L4: R5H_sdsb
            L4: R5H_stsb
            L4: R5H_sbsb
        L3: R5H_rssr
            L4: R5H_dssd
            L4: R5H_tssd
            L4: R5H_bssd
            L4: R5H_dsst
            L4: R5H_tsst
            L4: R5H_bsst
            L4: R5H_dssb
            L4: R5H_tssb
            L4: R5H_bssb
        L3: R5H_srrs
        L3: R5H_rsrs
            L4: R5H_dsds
            L4: R5H_tsds
            L4: R5H_bsds
            L4: R5H_dsts
            L4: R5H_tsts
            L4: R5H_bsts
            L4: R5H_dsbs
            L4: R5H_tsbs
            L4: R5H_bsbs
        L3: R5H_rrss
        L3: R5H_srrr
        L3: R5H_rsrr
        L3: R5H_rrsr
        L3: R5H_rrrs
        L3: R5H_rrrr
    L2: R6Hall
        L3: R6H_sssss
        L3: R6H_ssssr
            L4: R6H_ssssd
            L4: R6H_sssst
            L4: R6H_ssssb
        L3: R6H_sssrs
            L4: R6H_sssds
            L4: R6H_sssts
            L4: R6H_sssbs
        L3: R6H_ssrss
            L4: R6H_ssdss
            L4: R6H_sstss
            L4: R6H_ssbss
        L3: R6H_srsss
            L4: R6H_sdsss
            L4: R6H_stsss
            L4: R6H_sbsss
        L3: R6H_rssss
            L4: R6H_dssss
            L4: R6H_tssss
            L4: R6H_bssss
        L3: R6H_sssrr
        L3: R6H_ssrsr
            L4: R6H_ssdsd
            L4: R6H_sstsd
            L4: R6H_ssbsd
            L4: R6H_ssdst
            L4: R6H_sstst
            L4: R6H_ssbst
            L4: R6H_ssdsb
            L4: R6H_sstsb
            L4: R6H_ssbsb
        L3: R6H_srssr
            L4: R6H_sdssd
            L4: R6H_stssd
            L4: R6H_sbssd
            L4: R6H_sdsst
            L4: R6H_stsst
            L4: R6H_sbsst
            L4: R6H_sdssb
            L4: R6H_stssb
            L4: R6H_sbssb
        L3: R6H_rsssr
            L4: R6H_dsssd
            L4: R6H_tsssd
            L4: R6H_bsssd
            L4: R6H_dssst
            L4: R6H_tssst
            L4: R6H_bssst
            L4: R6H_dsssb
            L4: R6H_tsssb
            L4: R6H_bsssb
        L3: R6H_ssrrs
        L3: R6H_srsrs
            L4: R6H_sdsds
            L4: R6H_stsds
            L4: R6H_sbsds
            L4: R6H_sdsts
            L4: R6H_ststs
            L4: R6H_sbsts
            L4: R6H_sdsbs
            L4: R6H_stsbs
            L4: R6H_sbsbs
        L3: R6H_rssrs
            L4: R6H_dssds
            L4: R6H_tssds
            L4: R6H_bssds
            L4: R6H_dssts
            L4: R6H_tssts
            L4: R6H_bssts
            L4: R6H_dssbs
            L4: R6H_tssbs
            L4: R6H_bssbs
        L3: R6H_srrss
        L3: R6H_rsrss
            L4: R6H_dsdss
            L4: R6H_tsdss
            L4: R6H_bsdss
            L4: R6H_dstss
            L4: R6H_tstss
            L4: R6H_bstss
            L4: R6H_dsbss
            L4: R6H_tsbss
            L4: R6H_bsbss
        L3: R6H_rrsss
        L3: R6H_ssrrr
        L3: R6H_srsrr
        L3: R6H_rssrr
        L3: R6H_srrsr
        L3: R6H_rsrsr
            L4: R6H_dsdsd
            L4: R6H_tsdsd
            L4: R6H_bsdsd
            L4: R6H_dstsd
            L4: R6H_tstsd
            L4: R6H_bstsd
            L4: R6H_dsbsd
            L4: R6H_tsbsd
            L4: R6H_bsbsd
            L4: R6H_dsdst
            L4: R6H_tsdst
            L4: R6H_bsdst
            L4: R6H_dstst
            L4: R6H_tstst
            L4: R6H_bstst
            L4: R6H_dsbst
            L4: R6H_tsbst
            L4: R6H_bsbst
            L4: R6H_dsdsb
            L4: R6H_tsdsb
            L4: R6H_bsdsb
            L4: R6H_dstsb
            L4: R6H_tstsb
            L4: R6H_bstsb
            L4: R6H_dsbsb
            L4: R6H_tsbsb
            L4: R6H_bsbsb
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
            L4: Csj_out_H2
            L4: Csj_out_RH
                L5: Csj_out_CH
                    L6: Csj_out_CsH
                    L6: Csj_out_CdH
                    L6: Csj_out_CtH
                    L6: Csj_out_CbH
                L5: Csj_out_OH
            L4: Csj_out_RR
                L5: Csj_out_CC
                    L6: Csj_out_CsCs
                    L6: Csj_out_CsCd
                    L6: Csj_out_CsCt
                    L6: Csj_out_CsCb
                    L6: Csj_out_CdCd
                    L6: Csj_out_CdCt
                    L6: Csj_out_CdCb
                    L6: Csj_out_CtCt
                    L6: Csj_out_CtCb
                    L6: Csj_out_CbCb
                L5: Csj_out_CO
                    L6: Csj_out_CsO
                    L6: Csj_out_CdO
                    L6: Csj_out_CtO
                    L6: Csj_out_CbO
                L5: Csj_out_OO
        L3: Cdj_out
            L4: Cdj_out_C
                L5: Cdj_out_Cd
                L5: Cdj_out_Cdd
            L4: Cdj_out_O
        L3: Ctj_out
        L3: Cbj_out
    L2: Oj_out
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
            L4: Cd_H_out_C
                L5: Cd_H_out_Cd
                    L6: Cd_H_out_CdH
                    L6: Cd_H_out_CdC
                        L7: Cd_H_out_CdCs
                        L7: Cd_H_out_CdCd
                        L7: Cd_H_out_CdCt
                        L7: Cd_H_out_CdCb
                    L6: Cd_H_out_CdO
                L5: Cd_H_out_Cdd
                    L6: Cd_H_out_CddH
                    L6: Cd_H_out_CddC
                        L7: Cd_H_out_CddCs
                        L7: Cd_H_out_CddCd
                        L7: Cd_H_out_CddCt
                        L7: Cd_H_out_CddCb
                    L6: Cd_H_out_CddO
            L4: Cd_H_out_O
                L5: Cd_H_out_OdH
                L5: Cd_H_out_OdC
                    L6: Cd_H_out_OdCs
                    L6: Cd_H_out_OdCd
                    L6: Cd_H_out_OdCt
                    L6: Cd_H_out_OdCb
                L5: Cd_H_out_OdO
        L3: Ct_H_out
        L3: Cb_H_out
    L2: O_H_out
"""
)

