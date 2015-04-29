#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/TS_groups"
shortDesc = u""
longDesc = u"""
The reaction site *3 should be a triplet, otherwise it will react via the 1+2_Cycloaddition family instead.
"""

entry(
    index = 1,
    label = "R_R",
    group = "OR{Cn_R, Od_R}",
    distances = DistanceData(
        distances = {'d12': 1.30778, 'd13': 2.02744, 'd23': 2.67397},
        uncertainties = {'d12': 0.0686, 'd13': 0.184543, 'd23': 0.268151},
    ),
    shortDesc = u"""Fitted to 30 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 2,
    label = "YJ",
    group = "OR{Hj, Cj, Oj}",
    distances = DistanceData(distances={}),
)

entry(
    index = 3,
    label = "Cn_R",
    group = "OR{Cd_R, Ct_R}",
    distances = DistanceData(
        distances = {'d12': 0.006411, 'd13': 0.039179, 'd23': 0.022561},
        uncertainties = {'d12': 0.072737, 'd13': 0.184808, 'd23': 0.280341},
    ),
    shortDesc = u"""Fitted to 26 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 8,
    label = "Cd_R",
    group = 
"""
1 *1 C u0 {2,D}
2 *2 R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.013856, 'd13': 0.035399, 'd23': 0.018876},
        uncertainties = {'d12': 0.07425, 'd13': 0.186927, 'd23': 0.28431},
    ),
    shortDesc = u"""Fitted to 25 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 19,
    label = "Cds_R",
    group = 
"""
1 *1 Cd u0 {2,D}
2 *2 R  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.036818, 'd13': 0.068456, 'd23': 0.086976},
        uncertainties = {'d12': 0.026916, 'd13': 0.135383, 'd23': 0.156649},
    ),
    shortDesc = u"""Fitted to 15 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 36,
    label = "Cds_Cd_H2",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 [Cd,Cdd] ux {1,D}
3    H        u0 {1,S}
4    H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.033599, 'd13': 0.087298, 'd23': 0.11377},
        uncertainties = {'d12': 0.040312, 'd13': 0.12773, 'd23': 0.160581},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 62,
    label = "Cds_Cds/H2",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.034065, 'd13': 0.110312, 'd23': 0.12661},
        uncertainties = {'d12': 0.049025, 'd13': 0.135613, 'd23': 0.126181},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 63,
    label = "Cds_Cdd/H2",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd ux {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.030915, 'd13': -0.045029, 'd23': 0.039937},
        uncertainties = {'d12': 0.248131, 'd13': 1.04827, 'd23': 1.68466},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 37,
    label = "Cds_Cd_RH",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 [Cd,Cdd] ux {1,D}
3    R!H      ux {1,S}
4    H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.042321, 'd13': 0.082805, 'd23': 0.096916},
        uncertainties = {'d12': 0.029244, 'd13': 0.149272, 'd23': 0.165732},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 64,
    label = "Cds_Cds/Cs/H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.045244, 'd13': 0.065213, 'd23': 0.042237},
        uncertainties = {'d12': 0.261088, 'd13': 0.346104, 'd23': 0.457703},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 65,
    label = "Cds_Cds/Cd/H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cd ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.037002, 'd13': -0.037727, 'd23': -0.019734},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 66,
    label = "Cds_Cds/Ct/H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 67,
    label = "Cds_Cds/Cb/H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 68,
    label = "Cds_Cdd/Cs/H",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.032582, 'd13': 0.118643, 'd23': 0.196563},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 69,
    label = "Cds_Cdd/Cd/H",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cd  ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 70,
    label = "Cds_Cdd/Ct/H",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Ct  u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 71,
    label = "Cds_Cdd/Cb/H",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cb  u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 38,
    label = "Cds_Cd_RR",
    group = 
"""
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 [Cd,Cdd] ux {1,D}
3    R!H      ux {1,S}
4    R!H      ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.032965, 'd13': -0.064167, 'd23': -0.066728},
        uncertainties = {'d12': 0.035046, 'd13': 0.507909, 'd23': 0.565834},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 72,
    label = "Cds_Cds/Cs/Cs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 73,
    label = "Cds_Cds/Cs/Cd",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 74,
    label = "Cds_Cds/Cs/Ct",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 75,
    label = "Cds_Cds/Cs/Cb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 76,
    label = "Cds_Cds/Cd/Cd",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 77,
    label = "Cds_Cds/Cd/Ct",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 78,
    label = "Cds_Cds/Cd/Cb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 79,
    label = "Cds_Cds/Ct/Ct",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 80,
    label = "Cds_Cds/Ct/Cb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 81,
    label = "Cds_Cds/Cb/Cb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 82,
    label = "Cds_Cdd/Cs/Cs",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    Cs  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.018762, 'd13': -0.077287, 'd23': -0.116824},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 83,
    label = "Cds_Cdd/Cs/Cd",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 84,
    label = "Cds_Cdd/Cs/Ct",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 85,
    label = "Cds_Cdd/Cs/Cb",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 86,
    label = "Cds_Cdd/Cd/Cd",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cd  ux {1,S}
4    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 87,
    label = "Cds_Cdd/Cd/Ct",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cd  ux {1,S}
4    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 88,
    label = "Cds_Cdd/Cd/Cb",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cd  ux {1,S}
4    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 89,
    label = "Cds_Cdd/Ct/Ct",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Ct  u0 {1,S}
4    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 90,
    label = "Cds_Cdd/Ct/Cb",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Ct  u0 {1,S}
4    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 91,
    label = "Cds_Cdd/Cb/Cb",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cb  u0 {1,S}
4    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 39,
    label = "Cds_Od_H2",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 40,
    label = "Cds_Od_RH",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 O   u0 {1,D}
3    H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 92,
    label = "Cds_Od/Cs/H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 93,
    label = "Cds_Od/Cd/H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 94,
    label = "Cds_Od/Ct/H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 95,
    label = "Cds_Od/Cb/H",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 41,
    label = "Cds_Od_RR",
    group = 
"""
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 O   u0 {1,D}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 96,
    label = "Cds_Od/Cs/Cs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 97,
    label = "Cds_Od/Cs/Cd",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 98,
    label = "Cds_Od/Cs/Ct",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 99,
    label = "Cds_Od/Cs/Cb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 100,
    label = "Cds_Od/Cd/Cd",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 101,
    label = "Cds_Od/Cd/Ct",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 102,
    label = "Cds_Od/Cd/Cb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 103,
    label = "Cds_Od/Ct/Ct",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 104,
    label = "Cds_Od/Ct/Cb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 105,
    label = "Cds_Od/Cb/Cb",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 O  u0 {1,D}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 20,
    label = "Cdd_RR",
    group = 
"""
1 *1 Cdd u0 {2,D}
2 *2 R   ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.011867, 'd13': 0.011936, 'd23': -0.04575},
        uncertainties = {'d12': 0.015868, 'd13': 0.182358, 'd23': 0.44316},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 42,
    label = "Cdd_CC",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 C   ux {1,D}
3    C   ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.001087, 'd13': 0.20275, 'd23': 0.024798},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
""",
)

entry(
    index = 106,
    label = "Cdd_Cds/Cds",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  ux {1,D}
3    Cd  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.001087, 'd13': 0.20275, 'd23': 0.024798},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
""",
)

entry(
    index = 107,
    label = "Cdd_Cds/Cdd",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  ux {1,D}
3    Cdd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 108,
    label = "Cdd_Cdd/Cdd",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D}
3    Cdd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 43,
    label = "Cdd_CO",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 C   ux {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.013664, 'd13': -0.019866, 'd23': -0.057508},
        uncertainties = {'d12': 0.02615, 'd13': 0.265138, 'd23': 0.71715},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 109,
    label = "Cdd_Cds/O",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  ux {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.013664, 'd13': -0.019866, 'd23': -0.057508},
        uncertainties = {'d12': 0.02615, 'd13': 0.265138, 'd23': 0.71715},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 110,
    label = "Cdd_Cdd/O",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cdd u0 {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 44,
    label = "CO2",
    group = 
"""
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O   u0 {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 9,
    label = "Ct_R",
    group = 
"""
1 *1 C u0 {2,T}
2 *2 R ux {1,T}
""",
    distances = DistanceData(
        distances = {'d12': -0.097819, 'd13': 0.092099, 'd23': 0.074142},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 21,
    label = "Ct_Ct/H",
    group = 
"""
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.097819, 'd13': 0.092099, 'd23': 0.074142},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 22,
    label = "Ct_Ct/R",
    group = 
"""
1 *1 C   u0 {2,T} {3,S}
2 *2 C   ux {1,T}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 45,
    label = "Ct_Ct/C",
    group = 
"""
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 111,
    label = "Ct_Ct/Cs",
    group = 
"""
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 112,
    label = "Ct_Ct/Cd",
    group = 
"""
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 113,
    label = "Ct_Ct/Ct",
    group = 
"""
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 114,
    label = "Ct_Ct/Cb",
    group = 
"""
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 46,
    label = "Ct_Ct/O",
    group = 
"""
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 4,
    label = "Od_R",
    group = 
"""
1 *1 O u0 {2,D}
2 *2 R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.064111, 'd13': -0.391786, 'd23': -0.225606},
        uncertainties = {'d12': 0.069797, 'd13': 0.342792, 'd23': 0.34522},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
""",
)

entry(
    index = 10,
    label = "Od_C",
    group = 
"""
1 *1 O u0 {2,D}
2 *2 C ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.064111, 'd13': -0.391786, 'd23': -0.225606},
        uncertainties = {'d12': 0.069797, 'd13': 0.342792, 'd23': 0.34522},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
""",
)

entry(
    index = 23,
    label = "Od_Cds",
    group = 
"""
1 *2 C ux {2,D} {3,S}
2 *1 O u0 {1,D}
3    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.064111, 'd13': -0.391786, 'd23': -0.225606},
        uncertainties = {'d12': 0.069797, 'd13': 0.342792, 'd23': 0.34522},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
""",
)

entry(
    index = 24,
    label = "Od_Cdd",
    group = 
"""
1 *2 C ux {2,D} {3,D}
2 *1 O u0 {1,D}
3    R ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 11,
    label = "O2",
    group = 
"""
1 *1 O u0 {2,D}
2 *2 O u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 5,
    label = "Hj",
    group = 
"""
1 *3 H u1
""",
    distances = DistanceData(
        distances = {'d12': -0.001548, 'd13': -0.182656, 'd23': -0.179982},
        uncertainties = {'d12': 0.02766, 'd13': 0.229325, 'd23': 0.306308},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 6,
    label = "Cj",
    group = 
"""
1 *3 C u1
""",
    distances = DistanceData(
        distances = {'d12': -0.001678, 'd13': 0.09499, 'd23': 0.102194},
        uncertainties = {'d12': 0.086391, 'd13': 0.195937, 'd23': 0.294911},
    ),
    shortDesc = u"""Fitted to 19 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 12,
    label = "Csj",
    group = 
"""
1 *3 Cs u1
""",
    distances = DistanceData(
        distances = {'d12': -0.003956, 'd13': 0.108397, 'd23': 0.128048},
        uncertainties = {'d12': 0.116975, 'd13': 0.113768, 'd23': 0.197602},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 25,
    label = "Csj_methyl",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.004179, 'd13': 0.124539, 'd23': 0.156884},
        uncertainties = {'d12': 0.140912, 'd13': 0.136601, 'd23': 0.238514},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 26,
    label = "Csj_RH2",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 47,
    label = "Csj_CH2",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 115,
    label = "Csj_Cs/H2",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 116,
    label = "Csj_Cd/H2",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 117,
    label = "Csj_Ct/H2",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 118,
    label = "Csj_Cb/H2",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 48,
    label = "Csj_OH2",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 27,
    label = "Csj_RRH",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.074458, 'd13': -0.031494, 'd23': -0.121858},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
""",
)

entry(
    index = 49,
    label = "Csj_CCH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.074458, 'd13': -0.031494, 'd23': -0.121858},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
""",
)

entry(
    index = 119,
    label = "Csj_Cs/Cs/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 120,
    label = "Csj_Cs/Cd/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 121,
    label = "Csj_Cs/Ct/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 122,
    label = "Csj_Cs/Cb/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 123,
    label = "Csj_Cd/Cd/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 124,
    label = "Csj_Cd/Ct/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 125,
    label = "Csj_Cd/Cb/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 126,
    label = "Csj_Ct/Ct/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 127,
    label = "Csj_Ct/Cb/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 128,
    label = "Csj_Cb/Cb/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 50,
    label = "Csj_COH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 129,
    label = "Csj_Cs/O/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 130,
    label = "Csj_Cd/O/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 131,
    label = "Csj_Ct/O/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 132,
    label = "Csj_Cb/O/H",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 51,
    label = "Csj_OOH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 28,
    label = "Csj_RRR",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 52,
    label = "Csj_CCC",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 133,
    label = "Csj_Cs/Cs/Cs",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 134,
    label = "Csj_Cs/Cs/Cd",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 135,
    label = "Csj_Cs/Cs/Ct",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 136,
    label = "Csj_Cs/Cs/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 137,
    label = "Csj_Cs/Cd/Cd",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 138,
    label = "Csj_Cs/Cd/Ct",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 139,
    label = "Csj_Cs/Cd/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 140,
    label = "Csj_Cs/Ct/Ct",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 141,
    label = "Csj_Cs/Ct/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 142,
    label = "Csj_Cs/Cb/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 143,
    label = "Csj_Cd/Cd/Cd",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 144,
    label = "Csj_Cd/Cd/Ct",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 145,
    label = "Csj_Cd/Cd/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 146,
    label = "Csj_Cd/Ct/Ct",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 147,
    label = "Csj_Cd/Ct/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 148,
    label = "Csj_Cd/Cb/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 149,
    label = "Csj_Ct/Ct/Ct",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 150,
    label = "Csj_Ct/Ct/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 151,
    label = "Csj_Ct/Cb/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 152,
    label = "Csj_Cb/Cb/Cb",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 53,
    label = "Csj_CCO",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 153,
    label = "Csj_Cs/Cs/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 154,
    label = "Csj_Cs/Cd/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 155,
    label = "Csj_Cs/Ct/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 156,
    label = "Csj_Cs/Cb/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 157,
    label = "Csj_Cd/Cd/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 158,
    label = "Csj_Cd/Ct/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 159,
    label = "Csj_Cd/Cb/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 160,
    label = "Csj_Ct/Ct/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 161,
    label = "Csj_Ct/Cb/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 162,
    label = "Csj_Cb/Cb/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 54,
    label = "Csj_COO",
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
    index = 163,
    label = "Csj_Cs/O/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 164,
    label = "Csj_Cd/O/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 165,
    label = "Csj_Ct/O/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 166,
    label = "Csj_Cb/O/O",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 55,
    label = "Csj_OOO",
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
    index = 13,
    label = "Cdj",
    group = 
"""
1 *3 Cd u1
""",
    distances = DistanceData(
        distances = {'d12': 0.012402, 'd13': 0.14759, 'd23': 0.181334},
        uncertainties = {'d12': 0.038016, 'd13': 0.129231, 'd23': 0.146268},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 29,
    label = "Cdj_Cd",
    group = 
"""
1 *3 Cd       u1 {2,D}
2    [Cd,Cdd] ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.012402, 'd13': 0.14759, 'd23': 0.181334},
        uncertainties = {'d12': 0.038016, 'd13': 0.129231, 'd23': 0.146268},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 56,
    label = "Cdj_CdH",
    group = 
"""
1 *3 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01073, 'd13': 0.197393, 'd23': 0.248507},
        uncertainties = {'d12': 0.217052, 'd13': 0.945911, 'd23': 1.17308},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 167,
    label = "Cdj_CdsH",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01073, 'd13': 0.197393, 'd23': 0.248507},
        uncertainties = {'d12': 0.217052, 'd13': 0.945911, 'd23': 1.17308},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 168,
    label = "Cdj_CddH",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 57,
    label = "Cdj_CdC",
    group = 
"""
1 *3 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    C        ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.02204, 'd13': 0.126839, 'd23': 0.153345},
        uncertainties = {'d12': 0.052026, 'd13': 0.154765, 'd23': 0.160861},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
""",
)

entry(
    index = 169,
    label = "Cdj_Cds/Cs",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.007068, 'd13': 0.145488, 'd23': 0.198503},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
""",
)

entry(
    index = 170,
    label = "Cdj_Cds/Cd",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.016676, 'd13': 0.230901, 'd23': 0.236109},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
""",
)

entry(
    index = 171,
    label = "Cdj_Cds/Ct",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 172,
    label = "Cdj_Cds/Cb",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 173,
    label = "Cdj_Cdd/Cs",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cs  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.032208, 'd13': 0.065484, 'd23': 0.089385},
        uncertainties = {'d12': 0.314198, 'd13': 0.747758, 'd23': 0.569045},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
""",
)

entry(
    index = 174,
    label = "Cdj_Cdd/Cd",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 175,
    label = "Cdj_Cdd/Ct",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 176,
    label = "Cdj_Cdd/Cb",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 58,
    label = "Cdj_CdO",
    group = 
"""
1 *3 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    O        ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 177,
    label = "Cdj_CdsO",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 178,
    label = "Cdj_CddO",
    group = 
"""
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    O   ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 30,
    label = "Cdj_Od",
    group = 
"""
1 *3 Cd u1 {2,D}
2    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 59,
    label = "Cdj_OdH",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 60,
    label = "Cdj_OdC",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 179,
    label = "Cdj_OdCs",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 180,
    label = "Cdj_OdCd",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 181,
    label = "Cdj_OdCt",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 182,
    label = "Cdj_OdCb",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 61,
    label = "Cdj_OdO",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 14,
    label = "Ctj",
    group = 
"""
1 *3 Ct u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 31,
    label = "Ctj_Ct",
    group = 
"""
1 *3 Ct u1 {2,T}
2    Ct u0 {1,T}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 15,
    label = "Cbj",
    group = 
"""
1 *3 Cb u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 7,
    label = "Oj",
    group = 
"""
1 *3 O u1
""",
    distances = DistanceData(
        distances = {'d12': 0.022725, 'd13': -0.043189, 'd23': -0.122485},
        uncertainties = {'d12': 0.409561, 'd13': 0.262467, 'd23': 0.657435},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
""",
)

entry(
    index = 16,
    label = "OH",
    group = 
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.022725, 'd13': -0.043189, 'd23': -0.122485},
        uncertainties = {'d12': 0.409561, 'd13': 0.262467, 'd23': 0.657435},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
""",
)

entry(
    index = 17,
    label = "OjC",
    group = 
"""
1 *3 O u1 {2,S}
2    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 32,
    label = "OjCs",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 33,
    label = "OjCd",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 34,
    label = "OjCt",
    group = 
"""
1 *3 O  u1 {2,S}
2    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 35,
    label = "OjCb",
    group = 
"""
1 *3 O  u1 {2,S}
2    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 18,
    label = "OjO",
    group = 
"""
1 *3 O u1 {2,S}
2    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

tree(
"""
L1: R_R
    L2: Cn_R
        L3: Cd_R
            L4: Cds_R
                L5: Cds_Cd_H2
                    L6: Cds_Cds/H2
                    L6: Cds_Cdd/H2
                L5: Cds_Cd_RH
                    L6: Cds_Cds/Cs/H
                    L6: Cds_Cds/Cd/H
                    L6: Cds_Cds/Ct/H
                    L6: Cds_Cds/Cb/H
                    L6: Cds_Cdd/Cs/H
                    L6: Cds_Cdd/Cd/H
                    L6: Cds_Cdd/Ct/H
                    L6: Cds_Cdd/Cb/H
                L5: Cds_Cd_RR
                    L6: Cds_Cds/Cs/Cs
                    L6: Cds_Cds/Cs/Cd
                    L6: Cds_Cds/Cs/Ct
                    L6: Cds_Cds/Cs/Cb
                    L6: Cds_Cds/Cd/Cd
                    L6: Cds_Cds/Cd/Ct
                    L6: Cds_Cds/Cd/Cb
                    L6: Cds_Cds/Ct/Ct
                    L6: Cds_Cds/Ct/Cb
                    L6: Cds_Cds/Cb/Cb
                    L6: Cds_Cdd/Cs/Cs
                    L6: Cds_Cdd/Cs/Cd
                    L6: Cds_Cdd/Cs/Ct
                    L6: Cds_Cdd/Cs/Cb
                    L6: Cds_Cdd/Cd/Cd
                    L6: Cds_Cdd/Cd/Ct
                    L6: Cds_Cdd/Cd/Cb
                    L6: Cds_Cdd/Ct/Ct
                    L6: Cds_Cdd/Ct/Cb
                    L6: Cds_Cdd/Cb/Cb
                L5: Cds_Od_H2
                L5: Cds_Od_RH
                    L6: Cds_Od/Cs/H
                    L6: Cds_Od/Cd/H
                    L6: Cds_Od/Ct/H
                    L6: Cds_Od/Cb/H
                L5: Cds_Od_RR
                    L6: Cds_Od/Cs/Cs
                    L6: Cds_Od/Cs/Cd
                    L6: Cds_Od/Cs/Ct
                    L6: Cds_Od/Cs/Cb
                    L6: Cds_Od/Cd/Cd
                    L6: Cds_Od/Cd/Ct
                    L6: Cds_Od/Cd/Cb
                    L6: Cds_Od/Ct/Ct
                    L6: Cds_Od/Ct/Cb
                    L6: Cds_Od/Cb/Cb
            L4: Cdd_RR
                L5: Cdd_CC
                    L6: Cdd_Cds/Cds
                    L6: Cdd_Cds/Cdd
                    L6: Cdd_Cdd/Cdd
                L5: Cdd_CO
                    L6: Cdd_Cds/O
                    L6: Cdd_Cdd/O
                L5: CO2
        L3: Ct_R
            L4: Ct_Ct/H
            L4: Ct_Ct/R
                L5: Ct_Ct/C
                    L6: Ct_Ct/Cs
                    L6: Ct_Ct/Cd
                    L6: Ct_Ct/Ct
                    L6: Ct_Ct/Cb
                L5: Ct_Ct/O
    L2: Od_R
        L3: Od_C
            L4: Od_Cds
            L4: Od_Cdd
        L3: O2
L1: YJ
    L2: Hj
    L2: Cj
        L3: Csj
            L4: Csj_methyl
            L4: Csj_RH2
                L5: Csj_CH2
                    L6: Csj_Cs/H2
                    L6: Csj_Cd/H2
                    L6: Csj_Ct/H2
                    L6: Csj_Cb/H2
                L5: Csj_OH2
            L4: Csj_RRH
                L5: Csj_CCH
                    L6: Csj_Cs/Cs/H
                    L6: Csj_Cs/Cd/H
                    L6: Csj_Cs/Ct/H
                    L6: Csj_Cs/Cb/H
                    L6: Csj_Cd/Cd/H
                    L6: Csj_Cd/Ct/H
                    L6: Csj_Cd/Cb/H
                    L6: Csj_Ct/Ct/H
                    L6: Csj_Ct/Cb/H
                    L6: Csj_Cb/Cb/H
                L5: Csj_COH
                    L6: Csj_Cs/O/H
                    L6: Csj_Cd/O/H
                    L6: Csj_Ct/O/H
                    L6: Csj_Cb/O/H
                L5: Csj_OOH
            L4: Csj_RRR
                L5: Csj_CCC
                    L6: Csj_Cs/Cs/Cs
                    L6: Csj_Cs/Cs/Cd
                    L6: Csj_Cs/Cs/Ct
                    L6: Csj_Cs/Cs/Cb
                    L6: Csj_Cs/Cd/Cd
                    L6: Csj_Cs/Cd/Ct
                    L6: Csj_Cs/Cd/Cb
                    L6: Csj_Cs/Ct/Ct
                    L6: Csj_Cs/Ct/Cb
                    L6: Csj_Cs/Cb/Cb
                    L6: Csj_Cd/Cd/Cd
                    L6: Csj_Cd/Cd/Ct
                    L6: Csj_Cd/Cd/Cb
                    L6: Csj_Cd/Ct/Ct
                    L6: Csj_Cd/Ct/Cb
                    L6: Csj_Cd/Cb/Cb
                    L6: Csj_Ct/Ct/Ct
                    L6: Csj_Ct/Ct/Cb
                    L6: Csj_Ct/Cb/Cb
                    L6: Csj_Cb/Cb/Cb
                L5: Csj_CCO
                    L6: Csj_Cs/Cs/O
                    L6: Csj_Cs/Cd/O
                    L6: Csj_Cs/Ct/O
                    L6: Csj_Cs/Cb/O
                    L6: Csj_Cd/Cd/O
                    L6: Csj_Cd/Ct/O
                    L6: Csj_Cd/Cb/O
                    L6: Csj_Ct/Ct/O
                    L6: Csj_Ct/Cb/O
                    L6: Csj_Cb/Cb/O
                L5: Csj_COO
                    L6: Csj_Cs/O/O
                    L6: Csj_Cd/O/O
                    L6: Csj_Ct/O/O
                    L6: Csj_Cb/O/O
                L5: Csj_OOO
        L3: Cdj
            L4: Cdj_Cd
                L5: Cdj_CdH
                    L6: Cdj_CdsH
                    L6: Cdj_CddH
                L5: Cdj_CdC
                    L6: Cdj_Cds/Cs
                    L6: Cdj_Cds/Cd
                    L6: Cdj_Cds/Ct
                    L6: Cdj_Cds/Cb
                    L6: Cdj_Cdd/Cs
                    L6: Cdj_Cdd/Cd
                    L6: Cdj_Cdd/Ct
                    L6: Cdj_Cdd/Cb
                L5: Cdj_CdO
                    L6: Cdj_CdsO
                    L6: Cdj_CddO
            L4: Cdj_Od
                L5: Cdj_OdH
                L5: Cdj_OdC
                    L6: Cdj_OdCs
                    L6: Cdj_OdCd
                    L6: Cdj_OdCt
                    L6: Cdj_OdCb
                L5: Cdj_OdO
        L3: Ctj
            L4: Ctj_Ct
        L3: Cbj
    L2: Oj
        L3: OH
        L3: OjC
            L4: OjCs
            L4: OjCd
            L4: OjCt
            L4: OjCb
        L3: OjO
"""
)

