#!/usr/bin/env python
# encoding: utf-8

name = "H_Abstraction/TS_groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "X_H_or_Xrad_H_Xbirad_H_Xtrirad_H",
    group = "OR{H2, C_H, O_H}",
    distances = DistanceData(
        distances = {'d12': 1.1828, 'd13': 2.36349, 'd23': 1.18464},
        uncertainties = {'d12': 0.135335, 'd13': 0.087962, 'd23': 0.135247},
    ),
    shortDesc = u"""Fitted to 88 distances.
""",
    longDesc = 
u"""
[<Entry index=70 label="CsOHHH">, <Entry index=6 label="Hrad">]
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=28 label="OCH">, <Entry index=32 label="OjO">]
[<Entry index=29 label="OOH">, <Entry index=94 label="CsCOHj">]
[<Entry index=28 label="OCH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
[<Entry index=29 label="OOH">, <Entry index=91 label="CsCHHj">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=28 label="OCH">, <Entry index=30 label="OjH">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=6 label="Hrad">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
[<Entry index=27 label="OHH">, <Entry index=31 label="OjC">]
[<Entry index=28 label="OCH">, <Entry index=6 label="Hrad">]
[<Entry index=3 label="H2">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=3 label="H2">, <Entry index=17 label="Cj">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=3 label="H2">, <Entry index=93 label="CsCCHj">]
[<Entry index=27 label="OHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=92 label="CsOHHj">]
[<Entry index=43 label="C_methane">, <Entry index=6 label="Hrad">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=32 label="OjO">]
[<Entry index=3 label="H2">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=43 label="C_methane">, <Entry index=31 label="OjC">]
[<Entry index=29 label="OOH">, <Entry index=6 label="Hrad">]
[<Entry index=72 label="CsCOHH">, <Entry index=32 label="OjO">]
[<Entry index=71 label="CsCCHH">, <Entry index=6 label="Hrad">]
[<Entry index=14 label="Cb_H">, <Entry index=6 label="Hrad">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=6 label="Hrad">]
[<Entry index=3 label="H2">, <Entry index=36 label="Cbj">]
[<Entry index=3 label="H2">, <Entry index=31 label="OjC">]
[<Entry index=3 label="H2">, <Entry index=32 label="OjO">]
[<Entry index=3 label="H2">, <Entry index=56 label="Cs_methyl">]
[<Entry index=29 label="OOH">, <Entry index=31 label="OjC">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=91 label="CsCHHj">]
[<Entry index=4 label="C_H">, <Entry index=6 label="Hrad">]
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=6 label="Hrad">]
[<Entry index=69 label="CsCHHH">, <Entry index=30 label="OjH">]
""",
)

entry(
    index = 2,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Hrad, Orad, Crad}",
    distances = DistanceData(distances={}),
)

entry(
    index = 3,
    label = "H2",
    group = 
"""
1 *1 H u0 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.203377, 'd13': -0.17602, 'd23': 0.025309},
        uncertainties = {'d12': 0.19029, 'd13': 0.099597, 'd23': 0.144154},
    ),
    shortDesc = u"""Fitted to 28 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="H2">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=3 label="H2">, <Entry index=17 label="Cj">]
[<Entry index=3 label="H2">, <Entry index=31 label="OjC">]
[<Entry index=3 label="H2">, <Entry index=32 label="OjO">]
[<Entry index=3 label="H2">, <Entry index=56 label="Cs_methyl">]
[<Entry index=3 label="H2">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=3 label="H2">, <Entry index=93 label="CsCCHj">]
[<Entry index=3 label="H2">, <Entry index=92 label="CsOHHj">]
[<Entry index=3 label="H2">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=36 label="Cbj">]
""",
)

entry(
    index = 4,
    label = "C_H",
    group = 
"""
1 *1 C ux {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.174081, 'd13': 0.155891, 'd23': -0.021058},
        uncertainties = {'d12': 0.103125, 'd13': 0.089768, 'd23': 0.13681},
    ),
    shortDesc = u"""Fitted to 47 distances.
""",
    longDesc = 
u"""
[<Entry index=70 label="CsOHHH">, <Entry index=6 label="Hrad">]
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=6 label="Hrad">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=6 label="Hrad">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=32 label="OjO">]
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=43 label="C_methane">, <Entry index=31 label="OjC">]
[<Entry index=72 label="CsCOHH">, <Entry index=32 label="OjO">]
[<Entry index=71 label="CsCCHH">, <Entry index=6 label="Hrad">]
[<Entry index=14 label="Cb_H">, <Entry index=6 label="Hrad">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=6 label="Hrad">]
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=6 label="Hrad">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=4 label="C_H">, <Entry index=6 label="Hrad">]
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=30 label="OjH">]
""",
)

entry(
    index = 11,
    label = "Cs_H",
    group = 
"""
1 *1 Cs ux {2,S}
2 *2 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.170511, 'd13': 0.164343, 'd23': -0.009128},
        uncertainties = {'d12': 0.078362, 'd13': 0.079703, 'd23': 0.085242},
    ),
    shortDesc = u"""Fitted to 38 distances.
""",
    longDesc = 
u"""
[<Entry index=70 label="CsOHHH">, <Entry index=6 label="Hrad">]
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=6 label="Hrad">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=32 label="OjO">]
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=43 label="C_methane">, <Entry index=31 label="OjC">]
[<Entry index=72 label="CsCOHH">, <Entry index=32 label="OjO">]
[<Entry index=71 label="CsCCHH">, <Entry index=6 label="Hrad">]
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=6 label="Hrad">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=30 label="OjH">]
""",
)

entry(
    index = 22,
    label = "Csnorad_H",
    group = 
"""
1 *1 Cs u0 {2,S}
2 *2 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.170511, 'd13': 0.164343, 'd23': -0.009128},
        uncertainties = {'d12': 0.078362, 'd13': 0.079703, 'd23': 0.085242},
    ),
    shortDesc = u"""Fitted to 38 distances.
""",
    longDesc = 
u"""
[<Entry index=70 label="CsOHHH">, <Entry index=6 label="Hrad">]
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=6 label="Hrad">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=32 label="OjO">]
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=43 label="C_methane">, <Entry index=31 label="OjC">]
[<Entry index=72 label="CsCOHH">, <Entry index=32 label="OjO">]
[<Entry index=71 label="CsCCHH">, <Entry index=6 label="Hrad">]
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=6 label="Hrad">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=30 label="OjH">]
""",
)

entry(
    index = 43,
    label = "C_methane",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.205524, 'd13': 0.199594, 'd23': -0.008679},
        uncertainties = {'d12': 0.087514, 'd13': 0.107492, 'd23': 0.095443},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=43 label="C_methane">, <Entry index=31 label="OjC">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=43 label="C_methane">, <Entry index=6 label="Hrad">]
""",
)

entry(
    index = 44,
    label = "CsRHHH",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.151227, 'd13': 0.13016, 'd23': -0.025024},
        uncertainties = {'d12': 0.069259, 'd13': 0.074246, 'd23': 0.103319},
    ),
    shortDesc = u"""Fitted to 20 distances.
""",
    longDesc = 
u"""
[<Entry index=70 label="CsOHHH">, <Entry index=6 label="Hrad">]
[<Entry index=69 label="CsCHHH">, <Entry index=32 label="OjO">]
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=6 label="Hrad">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=30 label="OjH">]
""",
)

entry(
    index = 69,
    label = "CsCHHH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.151791, 'd13': 0.134074, 'd23': -0.021718},
        uncertainties = {'d12': 0.071154, 'd13': 0.062797, 'd23': 0.093793},
    ),
    shortDesc = u"""Fitted to 19 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=32 label="OjO">]
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=6 label="Hrad">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=30 label="OjH">]
""",
)

entry(
    index = 70,
    label = "CsOHHH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.133738, 'd13': 0.008809, 'd23': -0.127495},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=70 label="CsOHHH">, <Entry index=6 label="Hrad">]
""",
)

entry(
    index = 45,
    label = "CsRRHH",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.165014, 'd13': 0.18079, 'd23': 0.014094},
        uncertainties = {'d12': 0.119103, 'd13': 0.103608, 'd23': 0.066526},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=72 label="CsCOHH">, <Entry index=32 label="OjO">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=71 label="CsCCHH">, <Entry index=6 label="Hrad">]
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
""",
)

entry(
    index = 71,
    label = "CsCCHH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
5    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.157998, 'd13': 0.135122, 'd23': -0.024693},
        uncertainties = {'d12': 0.167333, 'd13': 0.127062, 'd23': 0.055443},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=6 label="Hrad">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
""",
)

entry(
    index = 72,
    label = "CsCOHH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.153554, 'd13': 0.212137, 'd23': 0.054664},
        uncertainties = {'d12': 0.292232, 'd13': 0.20859, 'd23': 0.166181},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=72 label="CsCOHH">, <Entry index=32 label="OjO">]
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
""",
)

entry(
    index = 73,
    label = "CsOOHH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.191485, 'd13': 0.208624, 'd23': 0.018716},
        uncertainties = {'d12': 0.438921, 'd13': 0.96777, 'd23': 0.719332},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
""",
)

entry(
    index = 46,
    label = "CsRRRH",
    group = 
"""
1 *1 Cs  u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 104 distances.
""",
    longDesc = 
u"""
[<Entry index=74 label="CsCCCH">, <Entry index=91 label="CsCHHj">]
[<Entry index=74 label="CsCCCH">, <Entry index=35 label="Ctj">]
[<Entry index=74 label="CsCCCH">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=74 label="CsCCCH">, <Entry index=94 label="CsCOHj">]
[<Entry index=74 label="CsCCCH">, <Entry index=17 label="Cj">]
[<Entry index=74 label="CsCCCH">, <Entry index=32 label="OjO">]
[<Entry index=74 label="CsCCCH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=74 label="CsCCCH">, <Entry index=92 label="CsOHHj">]
[<Entry index=74 label="CsCCCH">, <Entry index=31 label="OjC">]
[<Entry index=74 label="CsCCCH">, <Entry index=93 label="CsCCHj">]
[<Entry index=74 label="CsCCCH">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=74 label="CsCCCH">, <Entry index=6 label="Hrad">]
[<Entry index=74 label="CsCCCH">, <Entry index=36 label="Cbj">]
[<Entry index=74 label="CsCCCH">, <Entry index=96 label="CsCCCj">]
[<Entry index=75 label="CsCCOH">, <Entry index=6 label="Hrad">]
[<Entry index=74 label="CsCCCH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 74,
    label = "CsCCCH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
5    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 103 distances.
""",
    longDesc = 
u"""
[<Entry index=74 label="CsCCCH">, <Entry index=91 label="CsCHHj">]
[<Entry index=74 label="CsCCCH">, <Entry index=35 label="Ctj">]
[<Entry index=74 label="CsCCCH">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=74 label="CsCCCH">, <Entry index=94 label="CsCOHj">]
[<Entry index=74 label="CsCCCH">, <Entry index=17 label="Cj">]
[<Entry index=74 label="CsCCCH">, <Entry index=32 label="OjO">]
[<Entry index=74 label="CsCCCH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=74 label="CsCCCH">, <Entry index=92 label="CsOHHj">]
[<Entry index=74 label="CsCCCH">, <Entry index=31 label="OjC">]
[<Entry index=74 label="CsCCCH">, <Entry index=93 label="CsCCHj">]
[<Entry index=74 label="CsCCCH">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=74 label="CsCCCH">, <Entry index=6 label="Hrad">]
[<Entry index=74 label="CsCCCH">, <Entry index=36 label="Cbj">]
[<Entry index=74 label="CsCCCH">, <Entry index=96 label="CsCCCj">]
[<Entry index=74 label="CsCCCH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 75,
    label = "CsCCOH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=75 label="CsCCOH">, <Entry index=6 label="Hrad">]
""",
)

entry(
    index = 76,
    label = "CsCOOH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 77,
    label = "CsOOOH",
    group = 
"""
1 *1 Cs u0 {2,S} {3,S} {4,S} {5,S}
2 *2 H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 23,
    label = "Csrad_H",
    group = 
"""
1 *1 Cs u1 {2,S}
2 *2 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 38 distances.
""",
    longDesc = 
u"""
[<Entry index=47 label="C_methyl">, <Entry index=92 label="CsOHHj">]
[<Entry index=47 label="C_methyl">, <Entry index=91 label="CsCHHj">]
[<Entry index=47 label="C_methyl">, <Entry index=32 label="OjO">]
[<Entry index=47 label="C_methyl">, <Entry index=96 label="CsCCCj">]
[<Entry index=47 label="C_methyl">, <Entry index=6 label="Hrad">]
[<Entry index=47 label="C_methyl">, <Entry index=31 label="OjC">]
[<Entry index=47 label="C_methyl">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=47 label="C_methyl">, <Entry index=93 label="CsCCHj">]
[<Entry index=47 label="C_methyl">, <Entry index=94 label="CsCOHj">]
[<Entry index=47 label="C_methyl">, <Entry index=17 label="Cj">]
[<Entry index=47 label="C_methyl">, <Entry index=101 label="Cd(=C)Cj">]
""",
)

entry(
    index = 47,
    label = "C_methyl",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 38 distances.
""",
    longDesc = 
u"""
[<Entry index=47 label="C_methyl">, <Entry index=92 label="CsOHHj">]
[<Entry index=47 label="C_methyl">, <Entry index=91 label="CsCHHj">]
[<Entry index=47 label="C_methyl">, <Entry index=32 label="OjO">]
[<Entry index=47 label="C_methyl">, <Entry index=96 label="CsCCCj">]
[<Entry index=47 label="C_methyl">, <Entry index=6 label="Hrad">]
[<Entry index=47 label="C_methyl">, <Entry index=31 label="OjC">]
[<Entry index=47 label="C_methyl">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=47 label="C_methyl">, <Entry index=93 label="CsCCHj">]
[<Entry index=47 label="C_methyl">, <Entry index=94 label="CsCOHj">]
[<Entry index=47 label="C_methyl">, <Entry index=17 label="Cj">]
[<Entry index=47 label="C_methyl">, <Entry index=101 label="Cd(=C)Cj">]
""",
)

entry(
    index = 48,
    label = "CsRHjH",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 78,
    label = "CsCHjH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 79,
    label = "CsOHjH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 49,
    label = "CsRRjH",
    group = 
"""
1 *1 Cs  u1 {2,S} {3,S} {4,S}
2 *2 H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 80,
    label = "CsCCjH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 81,
    label = "CsCOjH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 82,
    label = "CsOOjH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2 *2 H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 24,
    label = "CsbiradH",
    group = "OR{Cs_singletH, Cs_tripletH}",
    distances = DistanceData(distances={}),
)

entry(
    index = 50,
    label = "Cs_singletH",
    group = 
"""
1 *1 Cs u0 p1 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    R  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 83,
    label = "Cs_singletHH",
    group = 
"""
1 *1 Cs u0 p1 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 84,
    label = "Cs_singletRH",
    group = 
"""
1 *1 Cs  u0 p1 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 108,
    label = "C_singletCH",
    group = 
"""
1 *1 Cs u0 p1 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 109,
    label = "C_singletOH",
    group = 
"""
1 *1 Cs u0 p1 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 51,
    label = "Cs_tripletH",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    R  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 85,
    label = "Cs_tripletHH",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 86,
    label = "Cs_tripletRH",
    group = 
"""
1 *1 Cs  u2 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 110,
    label = "Cs_tripletCH",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 111,
    label = "Cs_tripletOH",
    group = 
"""
1 *1 Cs u2 {2,S} {3,S}
2 *2 H  u0 {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 25,
    label = "CstriradH",
    group = "OR{Cdoublet_H, Cquartet_H}",
    distances = DistanceData(distances={}),
)

entry(
    index = 52,
    label = "Cdoublet_H",
    group = 
"""
1 *1 C u1 p1 {2,S}
2 *2 H u0 p0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 53,
    label = "Cquartet_H",
    group = 
"""
1 *1 C u3 p0 {2,S}
2 *2 H u0 p0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 12,
    label = "Cd_H",
    group = 
"""
1 *1 Cd ux {2,S}
2 *2 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.236355, 'd13': 0.09181, 'd23': -0.146584},
        uncertainties = {'d12': 0.070159, 'd13': 0.155183, 'd23': 0.176844},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=87 label="Cd(=C)HH">, <Entry index=6 label="Hrad">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=6 label="Hrad">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 26,
    label = "Cdnorad_H",
    group = 
"""
1 *1 Cd u0 {2,S}
2 *2 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.236355, 'd13': 0.09181, 'd23': -0.146584},
        uncertainties = {'d12': 0.070159, 'd13': 0.155183, 'd23': 0.176844},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=87 label="Cd(=C)HH">, <Entry index=6 label="Hrad">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=6 label="Hrad">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 54,
    label = "Cd(=C)RH",
    group = 
"""
1 *1 Cd u0 {2,S} {3,D}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.236355, 'd13': 0.09181, 'd23': -0.146584},
        uncertainties = {'d12': 0.070159, 'd13': 0.155183, 'd23': 0.176844},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=87 label="Cd(=C)HH">, <Entry index=6 label="Hrad">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=6 label="Hrad">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 87,
    label = "Cd(=C)HH",
    group = 
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.242425, 'd13': 0.11471, 'd23': -0.129509},
        uncertainties = {'d12': 0.10719, 'd13': 0.093129, 'd23': 0.097484},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=87 label="Cd(=C)HH">, <Entry index=6 label="Hrad">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 88,
    label = "Cd(=C)CH",
    group = 
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
4    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.219665, 'd13': 0.028836, 'd23': -0.193542},
        uncertainties = {'d12': 0.227745, 'd13': 1.5897, 'd23': 1.83468},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=88 label="Cd(=C)CH">, <Entry index=6 label="Hrad">]
""",
)

entry(
    index = 89,
    label = "Cd(=C)OH",
    group = 
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 55,
    label = "Cd(=O)RH",
    group = 
"""
1 *1 Cd u0 {2,S} {3,D}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 90,
    label = "Cd(=O)HH",
    group = 
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 91,
    label = "Cd(=O)CH",
    group = 
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 92,
    label = "Cd(=O)OH",
    group = 
"""
1 *1 Cd u0 {2,S} {3,D} {4,S}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 27,
    label = "Cdrad_H",
    group = 
"""
1 *1 Cd u1 {2,S}
2 *2 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 56,
    label = "Cd(=C)jH",
    group = 
"""
1 *1 Cd u1 {2,S} {3,D}
2 *2 H  u0 {1,S}
3    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 57,
    label = "Cd(=O)jH",
    group = 
"""
1 *1 Cd u1 {2,S} {3,D}
2 *2 H  u0 {1,S}
3    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 13,
    label = "Ct_H",
    group = 
"""
1 *1 Ct u0 {2,S}
2 *2 H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 12 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="CtCH">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=28 label="CtCH">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=28 label="CtCH">, <Entry index=36 label="Cbj">]
[<Entry index=28 label="CtCH">, <Entry index=91 label="CsCHHj">]
[<Entry index=28 label="CtCH">, <Entry index=93 label="CsCCHj">]
[<Entry index=28 label="CtCH">, <Entry index=96 label="CsCCCj">]
""",
)

entry(
    index = 28,
    label = "CtCH",
    group = 
"""
1 *1 Ct u0 {2,S} {3,T}
2 *2 H  u0 {1,S}
3    C  ux {1,T}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 12 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="CtCH">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=28 label="CtCH">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=28 label="CtCH">, <Entry index=36 label="Cbj">]
[<Entry index=28 label="CtCH">, <Entry index=91 label="CsCHHj">]
[<Entry index=28 label="CtCH">, <Entry index=93 label="CsCCHj">]
[<Entry index=28 label="CtCH">, <Entry index=96 label="CsCCCj">]
""",
)

entry(
    index = 14,
    label = "Cb_H",
    group = 
"""
1 *1 Cb u0 {2,S}
2 *2 H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.297705, 'd13': 0.068089, 'd23': -0.232511},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=14 label="Cb_H">, <Entry index=6 label="Hrad">]
""",
)

entry(
    index = 5,
    label = "O_H",
    group = 
"""
1 *1 O ux {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.021059, 'd13': 0.001464, 'd23': -0.004564},
        uncertainties = {'d12': 0.141176, 'd13': 0.077769, 'd23': 0.150242},
    ),
    shortDesc = u"""Fitted to 13 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="OOH">, <Entry index=6 label="Hrad">]
[<Entry index=28 label="OCH">, <Entry index=32 label="OjO">]
[<Entry index=29 label="OOH">, <Entry index=94 label="CsCOHj">]
[<Entry index=29 label="OOH">, <Entry index=31 label="OjC">]
[<Entry index=29 label="OOH">, <Entry index=91 label="CsCHHj">]
[<Entry index=27 label="OHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=28 label="OCH">, <Entry index=30 label="OjH">]
[<Entry index=28 label="OCH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=27 label="OHH">, <Entry index=31 label="OjC">]
[<Entry index=28 label="OCH">, <Entry index=6 label="Hrad">]
""",
)

entry(
    index = 13,
    label = "OradH",
    group = 
"""
1 *1 O u1 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 15 distances.
""",
    longDesc = 
u"""
[<Entry index=13 label="OradH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=13 label="OradH">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=13 label="OradH">, <Entry index=93 label="CsCCHj">]
[<Entry index=13 label="OradH">, <Entry index=92 label="CsOHHj">]
[<Entry index=13 label="OradH">, <Entry index=91 label="CsCHHj">]
[<Entry index=13 label="OradH">, <Entry index=101 label="Cd(=C)Cj">]
""",
)

entry(
    index = 14,
    label = "ORH",
    group = 
"""
1 *1 O u0 {2,S}
2 *2 H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.021059, 'd13': 0.001464, 'd23': -0.004564},
        uncertainties = {'d12': 0.141176, 'd13': 0.077769, 'd23': 0.150242},
    ),
    shortDesc = u"""Fitted to 13 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="OOH">, <Entry index=6 label="Hrad">]
[<Entry index=28 label="OCH">, <Entry index=32 label="OjO">]
[<Entry index=29 label="OOH">, <Entry index=94 label="CsCOHj">]
[<Entry index=29 label="OOH">, <Entry index=31 label="OjC">]
[<Entry index=29 label="OOH">, <Entry index=91 label="CsCHHj">]
[<Entry index=27 label="OHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=28 label="OCH">, <Entry index=30 label="OjH">]
[<Entry index=28 label="OCH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=27 label="OHH">, <Entry index=31 label="OjC">]
[<Entry index=28 label="OCH">, <Entry index=6 label="Hrad">]
""",
)

entry(
    index = 27,
    label = "OHH",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.198669, 'd13': 0.033671, 'd23': -0.132275},
        uncertainties = {'d12': 0.550538, 'd13': 0.933317, 'd23': 0.225638},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=27 label="OHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=27 label="OHH">, <Entry index=31 label="OjC">]
""",
)

entry(
    index = 28,
    label = "OCH",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.003787, 'd13': -0.053901, 'd23': -0.025534},
        uncertainties = {'d12': 0.187821, 'd13': 0.092848, 'd23': 0.215886},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="OCH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=28 label="OCH">, <Entry index=32 label="OjO">]
[<Entry index=28 label="OCH">, <Entry index=30 label="OjH">]
[<Entry index=28 label="OCH">, <Entry index=6 label="Hrad">]
""",
)

entry(
    index = 29,
    label = "OOH",
    group = 
"""
1 *1 O u0 {2,S} {3,S}
2 *2 H u0 {1,S}
3    O ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.031007, 'd13': 0.025277, 'd23': 0.058268},
        uncertainties = {'d12': 0.199773, 'd13': 0.084628, 'd23': 0.207436},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="OOH">, <Entry index=94 label="CsCOHj">]
[<Entry index=29 label="OOH">, <Entry index=6 label="Hrad">]
[<Entry index=29 label="OOH">, <Entry index=31 label="OjC">]
[<Entry index=29 label="OOH">, <Entry index=91 label="CsCHHj">]
""",
)

entry(
    index = 6,
    label = "Hrad",
    group = 
"""
1 *3 H u1
""",
    distances = DistanceData(
        distances = {'d12': 0.025157, 'd13': -0.176935, 'd23': -0.204183},
        uncertainties = {'d12': 0.144612, 'd13': 0.100283, 'd23': 0.190259},
    ),
    shortDesc = u"""Fitted to 28 distances.
""",
    longDesc = 
u"""
[<Entry index=70 label="CsOHHH">, <Entry index=6 label="Hrad">]
[<Entry index=29 label="OOH">, <Entry index=6 label="Hrad">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=6 label="Hrad">]
[<Entry index=4 label="C_H">, <Entry index=6 label="Hrad">]
[<Entry index=69 label="CsCHHH">, <Entry index=6 label="Hrad">]
[<Entry index=71 label="CsCCHH">, <Entry index=6 label="Hrad">]
[<Entry index=14 label="Cb_H">, <Entry index=6 label="Hrad">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=6 label="Hrad">]
[<Entry index=43 label="C_methane">, <Entry index=6 label="Hrad">]
[<Entry index=28 label="OCH">, <Entry index=6 label="Hrad">]
""",
)

entry(
    index = 7,
    label = "Orad",
    group = 
"""
1 *3 O u[1,2]
""",
    distances = DistanceData(
        distances = {'d12': -0.004033, 'd13': -0.000667, 'd23': 0.018405},
        uncertainties = {'d12': 0.15081, 'd13': 0.077947, 'd23': 0.140783},
    ),
    shortDesc = u"""Fitted to 13 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=32 label="OjO">]
[<Entry index=28 label="OCH">, <Entry index=32 label="OjO">]
[<Entry index=3 label="H2">, <Entry index=31 label="OjC">]
[<Entry index=3 label="H2">, <Entry index=32 label="OjO">]
[<Entry index=29 label="OOH">, <Entry index=31 label="OjC">]
[<Entry index=72 label="CsCOHH">, <Entry index=32 label="OjO">]
[<Entry index=28 label="OCH">, <Entry index=30 label="OjH">]
[<Entry index=43 label="C_methane">, <Entry index=31 label="OjC">]
[<Entry index=27 label="OHH">, <Entry index=31 label="OjC">]
[<Entry index=69 label="CsCHHH">, <Entry index=30 label="OjH">]
""",
)

entry(
    index = 15,
    label = "OjR",
    group = 
"""
1 *3 O u1 {2,S}
2    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.004033, 'd13': -0.000667, 'd23': 0.018405},
        uncertainties = {'d12': 0.15081, 'd13': 0.077947, 'd23': 0.140783},
    ),
    shortDesc = u"""Fitted to 13 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=32 label="OjO">]
[<Entry index=28 label="OCH">, <Entry index=32 label="OjO">]
[<Entry index=3 label="H2">, <Entry index=31 label="OjC">]
[<Entry index=3 label="H2">, <Entry index=32 label="OjO">]
[<Entry index=29 label="OOH">, <Entry index=31 label="OjC">]
[<Entry index=72 label="CsCOHH">, <Entry index=32 label="OjO">]
[<Entry index=28 label="OCH">, <Entry index=30 label="OjH">]
[<Entry index=43 label="C_methane">, <Entry index=31 label="OjC">]
[<Entry index=27 label="OHH">, <Entry index=31 label="OjC">]
[<Entry index=69 label="CsCHHH">, <Entry index=30 label="OjH">]
""",
)

entry(
    index = 30,
    label = "OjH",
    group = 
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.131984, 'd13': 0.031362, 'd23': 0.196079},
        uncertainties = {'d12': 0.228916, 'd13': 0.932423, 'd23': 0.555369},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=28 label="OCH">, <Entry index=30 label="OjH">]
[<Entry index=69 label="CsCHHH">, <Entry index=30 label="OjH">]
""",
)

entry(
    index = 31,
    label = "OjC",
    group = 
"""
1 *3 O u1 {2,S}
2    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.024873, 'd13': -0.055631, 'd23': -0.006176},
        uncertainties = {'d12': 0.216095, 'd13': 0.093309, 'd23': 0.187648},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="H2">, <Entry index=31 label="OjC">]
[<Entry index=29 label="OOH">, <Entry index=31 label="OjC">]
[<Entry index=27 label="OHH">, <Entry index=31 label="OjC">]
[<Entry index=43 label="C_methane">, <Entry index=31 label="OjC">]
""",
)

entry(
    index = 32,
    label = "OjO",
    group = 
"""
1 *3 O u1 {2,S}
2    O ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.058804, 'd13': 0.022952, 'd23': -0.033859},
        uncertainties = {'d12': 0.208632, 'd13': 0.084909, 'd23': 0.198846},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=32 label="OjO">]
[<Entry index=72 label="CsCOHH">, <Entry index=32 label="OjO">]
[<Entry index=3 label="H2">, <Entry index=32 label="OjO">]
[<Entry index=28 label="OCH">, <Entry index=32 label="OjO">]
""",
)

entry(
    index = 16,
    label = "O_atom_triplet",
    group = 
"""
1 *3 O u2
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 15 distances.
""",
    longDesc = 
u"""
[<Entry index=87 label="Cd(=C)HH">, <Entry index=16 label="O_atom_triplet">]
[<Entry index=69 label="CsCHHH">, <Entry index=16 label="O_atom_triplet">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=16 label="O_atom_triplet">]
[<Entry index=70 label="CsOHHH">, <Entry index=16 label="O_atom_triplet">]
[<Entry index=71 label="CsCCHH">, <Entry index=16 label="O_atom_triplet">]
[<Entry index=43 label="C_methane">, <Entry index=16 label="O_atom_triplet">]
""",
)

entry(
    index = 8,
    label = "Crad",
    group = 
"""
1 *3 C u[1,2,3]
""",
    distances = DistanceData(
        distances = {'d12': -0.020644, 'd13': 0.154245, 'd23': 0.172021},
        uncertainties = {'d12': 0.136565, 'd13': 0.089301, 'd23': 0.103054},
    ),
    shortDesc = u"""Fitted to 47 distances.
""",
    longDesc = 
u"""
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=29 label="OOH">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
[<Entry index=29 label="OOH">, <Entry index=91 label="CsCHHj">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=3 label="H2">, <Entry index=17 label="Cj">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=3 label="H2">, <Entry index=93 label="CsCCHj">]
[<Entry index=27 label="OHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=92 label="CsOHHj">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
[<Entry index=28 label="OCH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=3 label="H2">, <Entry index=36 label="Cbj">]
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=56 label="Cs_methyl">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=91 label="CsCHHj">]
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 17,
    label = "Cj",
    group = 
"""
1 *3 C u1
""",
    distances = DistanceData(
        distances = {'d12': -0.020644, 'd13': 0.154245, 'd23': 0.172021},
        uncertainties = {'d12': 0.136565, 'd13': 0.089301, 'd23': 0.103054},
    ),
    shortDesc = u"""Fitted to 47 distances.
""",
    longDesc = 
u"""
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=29 label="OOH">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
[<Entry index=29 label="OOH">, <Entry index=91 label="CsCHHj">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=3 label="H2">, <Entry index=17 label="Cj">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=3 label="H2">, <Entry index=93 label="CsCCHj">]
[<Entry index=27 label="OHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=92 label="CsOHHj">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
[<Entry index=28 label="OCH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=3 label="H2">, <Entry index=36 label="Cbj">]
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=56 label="Cs_methyl">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=91 label="CsCHHj">]
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 33,
    label = "Csj",
    group = 
"""
1 *3 Cs u1
""",
    distances = DistanceData(
        distances = {'d12': -0.008856, 'd13': 0.162612, 'd23': 0.168508},
        uncertainties = {'d12': 0.084495, 'd13': 0.079004, 'd23': 0.078181},
    ),
    shortDesc = u"""Fitted to 38 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=29 label="OOH">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
[<Entry index=29 label="OOH">, <Entry index=91 label="CsCHHj">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=3 label="H2">, <Entry index=93 label="CsCCHj">]
[<Entry index=27 label="OHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=92 label="CsOHHj">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
[<Entry index=28 label="OCH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=56 label="Cs_methyl">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=91 label="CsCHHj">]
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 56,
    label = "Cs_methyl",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.00985, 'd13': 0.198653, 'd23': 0.205745},
        uncertainties = {'d12': 0.094452, 'd13': 0.108833, 'd23': 0.088175},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=72 label="CsCOHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=69 label="CsCHHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=3 label="H2">, <Entry index=56 label="Cs_methyl">]
[<Entry index=71 label="CsCCHH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=28 label="OCH">, <Entry index=56 label="Cs_methyl">]
[<Entry index=73 label="CsOOHH">, <Entry index=56 label="Cs_methyl">]
""",
)

entry(
    index = 57,
    label = "CsRHHj",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.024219, 'd13': 0.128369, 'd23': 0.148632},
        uncertainties = {'d12': 0.102185, 'd13': 0.073177, 'd23': 0.068704},
    ),
    shortDesc = u"""Fitted to 20 distances.
""",
    longDesc = 
u"""
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=27 label="OHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=29 label="OOH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=92 label="CsOHHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=91 label="CsCHHj">]
""",
)

entry(
    index = 91,
    label = "CsCHHj",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.020934, 'd13': 0.13224, 'd23': 0.149174},
        uncertainties = {'d12': 0.092572, 'd13': 0.061609, 'd23': 0.070575},
    ),
    shortDesc = u"""Fitted to 19 distances.
""",
    longDesc = 
u"""
[<Entry index=73 label="CsOOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=29 label="OOH">, <Entry index=91 label="CsCHHj">]
[<Entry index=72 label="CsCOHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=43 label="C_methane">, <Entry index=91 label="CsCHHj">]
[<Entry index=27 label="OHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=71 label="CsCCHH">, <Entry index=91 label="CsCHHj">]
[<Entry index=3 label="H2">, <Entry index=91 label="CsCHHj">]
""",
)

entry(
    index = 92,
    label = "CsOHHj",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.12606, 'd13': 0.008352, 'd23': 0.131824},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="H2">, <Entry index=92 label="CsOHHj">]
""",
)

entry(
    index = 58,
    label = "CsRRHj",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    H   u0 {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.014982, 'd13': 0.178375, 'd23': 0.161721},
        uncertainties = {'d12': 0.066966, 'd13': 0.101725, 'd23': 0.118941},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=29 label="OOH">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=3 label="H2">, <Entry index=93 label="CsCCHj">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
""",
)

entry(
    index = 93,
    label = "CsCCHj",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.023592, 'd13': 0.133107, 'd23': 0.154884},
        uncertainties = {'d12': 0.056343, 'd13': 0.125335, 'd23': 0.166663},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=93 label="CsCCHj">]
[<Entry index=3 label="H2">, <Entry index=93 label="CsCCHj">]
[<Entry index=43 label="C_methane">, <Entry index=93 label="CsCCHj">]
""",
)

entry(
    index = 94,
    label = "CsCOHj",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.055285, 'd13': 0.209596, 'd23': 0.150406},
        uncertainties = {'d12': 0.168629, 'd13': 0.204918, 'd23': 0.291401},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="OOH">, <Entry index=94 label="CsCOHj">]
[<Entry index=43 label="C_methane">, <Entry index=94 label="CsCOHj">]
[<Entry index=69 label="CsCHHH">, <Entry index=94 label="CsCOHj">]
""",
)

entry(
    index = 95,
    label = "CsOOHj",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.019636, 'd13': 0.205759, 'd23': 0.187716},
        uncertainties = {'d12': 0.715136, 'd13': 0.943277, 'd23': 0.457006},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=95 label="CsOOHj">]
[<Entry index=43 label="C_methane">, <Entry index=95 label="CsOOHj">]
""",
)

entry(
    index = 59,
    label = "CsRRRj",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 104 distances.
""",
    longDesc = 
u"""
[<Entry index=71 label="CsCCHH">, <Entry index=96 label="CsCCCj">]
[<Entry index=3 label="H2">, <Entry index=97 label="CsCCOj">]
[<Entry index=72 label="CsCOHH">, <Entry index=96 label="CsCCCj">]
[<Entry index=28 label="CtCH">, <Entry index=96 label="CsCCCj">]
[<Entry index=43 label="C_methane">, <Entry index=96 label="CsCCCj">]
[<Entry index=69 label="CsCHHH">, <Entry index=96 label="CsCCCj">]
[<Entry index=47 label="C_methyl">, <Entry index=96 label="CsCCCj">]
[<Entry index=29 label="OOH">, <Entry index=96 label="CsCCCj">]
[<Entry index=28 label="OCH">, <Entry index=96 label="CsCCCj">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=96 label="CsCCCj">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=96 label="CsCCCj">]
[<Entry index=4 label="C_H">, <Entry index=96 label="CsCCCj">]
[<Entry index=3 label="H2">, <Entry index=96 label="CsCCCj">]
[<Entry index=14 label="Cb_H">, <Entry index=96 label="CsCCCj">]
[<Entry index=74 label="CsCCCH">, <Entry index=96 label="CsCCCj">]
[<Entry index=70 label="CsOHHH">, <Entry index=96 label="CsCCCj">]
""",
)

entry(
    index = 96,
    label = "CsCCCj",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 103 distances.
""",
    longDesc = 
u"""
[<Entry index=71 label="CsCCHH">, <Entry index=96 label="CsCCCj">]
[<Entry index=72 label="CsCOHH">, <Entry index=96 label="CsCCCj">]
[<Entry index=28 label="CtCH">, <Entry index=96 label="CsCCCj">]
[<Entry index=43 label="C_methane">, <Entry index=96 label="CsCCCj">]
[<Entry index=69 label="CsCHHH">, <Entry index=96 label="CsCCCj">]
[<Entry index=47 label="C_methyl">, <Entry index=96 label="CsCCCj">]
[<Entry index=29 label="OOH">, <Entry index=96 label="CsCCCj">]
[<Entry index=28 label="OCH">, <Entry index=96 label="CsCCCj">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=96 label="CsCCCj">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=96 label="CsCCCj">]
[<Entry index=4 label="C_H">, <Entry index=96 label="CsCCCj">]
[<Entry index=3 label="H2">, <Entry index=96 label="CsCCCj">]
[<Entry index=14 label="Cb_H">, <Entry index=96 label="CsCCCj">]
[<Entry index=74 label="CsCCCH">, <Entry index=96 label="CsCCCj">]
[<Entry index=70 label="CsOHHH">, <Entry index=96 label="CsCCCj">]
""",
)

entry(
    index = 97,
    label = "CsCCOj",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="H2">, <Entry index=97 label="CsCCOj">]
""",
)

entry(
    index = 98,
    label = "CsCOOj",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 99,
    label = "CsOOOj",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 34,
    label = "Cdj",
    group = 
"""
1 *3 Cd u1
""",
    distances = DistanceData(
        distances = {'d12': -0.14517, 'd13': 0.090544, 'd23': 0.233667},
        uncertainties = {'d12': 0.176417, 'd13': 0.155014, 'd23': 0.071444},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="H2">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=3 label="H2">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
""",
)

entry(
    index = 60,
    label = "Cd(=C)Rj",
    group = 
"""
1 *3 Cd u1 {2,D}
2    C  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.14517, 'd13': 0.090544, 'd23': 0.233667},
        uncertainties = {'d12': 0.176417, 'd13': 0.155014, 'd23': 0.071444},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="H2">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=3 label="H2">, <Entry index=101 label="Cd(=C)Cj">]
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
""",
)

entry(
    index = 100,
    label = "Cd(=C)Hj",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.128102, 'd13': 0.11315, 'd23': 0.239454},
        uncertainties = {'d12': 0.098346, 'd13': 0.09531, 'd23': 0.109276},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="H2">, <Entry index=100 label="Cd(=C)Hj">]
[<Entry index=43 label="C_methane">, <Entry index=100 label="Cd(=C)Hj">]
""",
)

entry(
    index = 101,
    label = "Cd(=C)Cj",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.192107, 'd13': 0.028379, 'd23': 0.217751},
        uncertainties = {'d12': 1.82744, 'd13': 1.58148, 'd23': 0.229102},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="H2">, <Entry index=101 label="Cd(=C)Cj">]
""",
)

entry(
    index = 102,
    label = "Cd(=C)Oj",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 61,
    label = "Cd(=O)Rj",
    group = 
"""
1 *3 Cd u1 {2,D}
2    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 103,
    label = "Cd(=O)Hj",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 104,
    label = "Cd(=O)Cj",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 105,
    label = "Cd(=O)Oj",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 35,
    label = "Ctj",
    group = 
"""
1 *3 Ct u1
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 12 distances.
""",
    longDesc = 
u"""
[<Entry index=71 label="CsCCHH">, <Entry index=35 label="Ctj">]
[<Entry index=74 label="CsCCCH">, <Entry index=35 label="Ctj">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=35 label="Ctj">]
[<Entry index=14 label="Cb_H">, <Entry index=35 label="Ctj">]
[<Entry index=69 label="CsCHHH">, <Entry index=35 label="Ctj">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=35 label="Ctj">]
""",
)

entry(
    index = 62,
    label = "CtCj",
    group = 
"""
1 *3 Cd u1 {2,T}
2    C  ux {1,T}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 36,
    label = "Cbj",
    group = 
"""
1 *3 Cb u1
""",
    distances = DistanceData(
        distances = {'d12': -0.231076, 'd13': 0.067632, 'd23': 0.295791},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="H2">, <Entry index=36 label="Cbj">]
""",
)

entry(
    index = 18,
    label = "Cjj",
    group = "OR{Csjj, Cdjj}",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 38 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=70 label="CsOHHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=4 label="C_H">, <Entry index=64 label="C_tripletRR">]
[<Entry index=74 label="CsCCCH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=3 label="H2">, <Entry index=64 label="C_tripletRR">]
[<Entry index=72 label="CsCOHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=71 label="CsCCHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=28 label="OCH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=29 label="OOH">, <Entry index=64 label="C_tripletRR">]
""",
)

entry(
    index = 37,
    label = "Csjj",
    group = "OR{C_singletRR, C_tripletRR}",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 38 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=70 label="CsOHHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=4 label="C_H">, <Entry index=64 label="C_tripletRR">]
[<Entry index=74 label="CsCCCH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=3 label="H2">, <Entry index=64 label="C_tripletRR">]
[<Entry index=72 label="CsCOHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=71 label="CsCCHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=28 label="OCH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=29 label="OOH">, <Entry index=64 label="C_tripletRR">]
""",
)

entry(
    index = 63,
    label = "C_singletRR",
    group = 
"""
1 *3 Cs u0 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 64,
    label = "C_tripletRR",
    group = 
"""
1 *3 Cs u2 p0
""",
    distances = DistanceData(distances={}),
    shortDesc = u"""Fitted to 38 distances.
""",
    longDesc = 
u"""
[<Entry index=69 label="CsCHHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=70 label="CsOHHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=87 label="Cd(=C)HH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=88 label="Cd(=C)CH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=4 label="C_H">, <Entry index=64 label="C_tripletRR">]
[<Entry index=74 label="CsCCCH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=3 label="H2">, <Entry index=64 label="C_tripletRR">]
[<Entry index=72 label="CsCOHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=71 label="CsCCHH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=28 label="OCH">, <Entry index=64 label="C_tripletRR">]
[<Entry index=29 label="OOH">, <Entry index=64 label="C_tripletRR">]
""",
)

entry(
    index = 38,
    label = "Cdjj",
    group = "OR{C_singletR, C_tripletR}",
    distances = DistanceData(distances={}),
)

entry(
    index = 65,
    label = "C_singletR",
    group = 
"""
1 *3 Cd u0 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 66,
    label = "C_tripletR",
    group = 
"""
1 *3 Cd u2 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 19,
    label = "Cjjj",
    group = "OR{C_doubletR, C_quartetR}",
    distances = DistanceData(distances={}),
)

entry(
    index = 39,
    label = "C_doubletR",
    group = 
"""
1 *3 C u1 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 40,
    label = "C_quartetR",
    group = 
"""
1 *3 C u3
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 112,
    label = "Cjjjj",
    group = "OR{C_quintet, C_triplet}",
    distances = DistanceData(distances={}),
)

entry(
    index = 113,
    label = "C_quintet",
    group = 
"""
1 *3 C u4 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 114,
    label = "C_triplet",
    group = 
"""
1 *3 C u2 p1
""",
    distances = DistanceData(distances={}),
)

tree(
"""
L1: X_H_or_Xrad_H_Xbirad_H_Xtrirad_H
    L2: H2
    L2: C_H
        L3: Cs_H
            L4: Csnorad_H
                L5: C_methane
                L5: CsRHHH
                    L6: CsCHHH
                    L6: CsOHHH
                L5: CsRRHH
                    L6: CsCCHH
                    L6: CsCOHH
                    L6: CsOOHH
                L5: CsRRRH
                    L6: CsCCCH
                    L6: CsCCOH
                    L6: CsCOOH
                    L6: CsOOOH
            L4: Csrad_H
                L5: C_methyl
                L5: CsRHjH
                    L6: CsCHjH
                    L6: CsOHjH
                L5: CsRRjH
                    L6: CsCCjH
                    L6: CsCOjH
                    L6: CsOOjH
            L4: CsbiradH
                L5: Cs_singletH
                    L6: Cs_singletHH
                    L6: Cs_singletRH
                        L7: C_singletCH
                        L7: C_singletOH
                L5: Cs_tripletH
                    L6: Cs_tripletHH
                    L6: Cs_tripletRH
                        L7: Cs_tripletCH
                        L7: Cs_tripletOH
            L4: CstriradH
                L5: Cdoublet_H
                L5: Cquartet_H
        L3: Cd_H
            L4: Cdnorad_H
                L5: Cd(=C)RH
                    L6: Cd(=C)HH
                    L6: Cd(=C)CH
                    L6: Cd(=C)OH
                L5: Cd(=O)RH
                    L6: Cd(=O)HH
                    L6: Cd(=O)CH
                    L6: Cd(=O)OH
            L4: Cdrad_H
                L5: Cd(=C)jH
                L5: Cd(=O)jH
        L3: Ct_H
            L4: CtCH
        L3: Cb_H
    L2: O_H
        L3: OradH
        L3: ORH
            L4: OHH
            L4: OCH
            L4: OOH
L1: Y_rad_birad_trirad_quadrad
    L2: Hrad
    L2: Orad
        L3: OjR
            L4: OjH
            L4: OjC
            L4: OjO
        L3: O_atom_triplet
    L2: Crad
        L3: Cj
            L4: Csj
                L5: Cs_methyl
                L5: CsRHHj
                    L6: CsCHHj
                    L6: CsOHHj
                L5: CsRRHj
                    L6: CsCCHj
                    L6: CsCOHj
                    L6: CsOOHj
                L5: CsRRRj
                    L6: CsCCCj
                    L6: CsCCOj
                    L6: CsCOOj
                    L6: CsOOOj
            L4: Cdj
                L5: Cd(=C)Rj
                    L6: Cd(=C)Hj
                    L6: Cd(=C)Cj
                    L6: Cd(=C)Oj
                L5: Cd(=O)Rj
                    L6: Cd(=O)Hj
                    L6: Cd(=O)Cj
                    L6: Cd(=O)Oj
            L4: Ctj
                L5: CtCj
            L4: Cbj
        L3: Cjj
            L4: Csjj
                L5: C_singletRR
                L5: C_tripletRR
            L4: Cdjj
                L5: C_singletR
                L5: C_tripletR
        L3: Cjjj
            L4: C_doubletR
            L4: C_quartetR
        L3: Cjjjj
            L4: C_quintet
            L4: C_triplet
"""
)

