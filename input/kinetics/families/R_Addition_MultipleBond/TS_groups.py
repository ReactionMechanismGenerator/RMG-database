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
        distances = {'d12': 1.30721, 'd13': 2.00448, 'd23': 2.61279},
        uncertainties = {'d12': 0.069042, 'd13': 0.146742, 'd23': 0.230692},
    ),
    shortDesc = u"""Fitted to 158 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=8 label="Cd_R">, <Entry index=5 label="Hj">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
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
        distances = {'d12': 0.004967, 'd13': 0.023505, 'd23': 0.01151},
        uncertainties = {'d12': 0.071819, 'd13': 0.141972, 'd23': 0.237605},
    ),
    shortDesc = u"""Fitted to 144 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=8 label="Cd_R">, <Entry index=5 label="Hj">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 8,
    label = "Cd_R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u0 {2,D}
2 *2 R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.011442, 'd13': 0.022726, 'd23': 0.006411},
        uncertainties = {'d12': 0.074089, 'd13': 0.143336, 'd23': 0.244321},
    ),
    shortDesc = u"""Fitted to 134 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=8 label="Cd_R">, <Entry index=5 label="Hj">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 19,
    label = "Cds_R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D}
2 *2 R  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.04613, 'd13': 0.059501, 'd23': 0.077838},
        uncertainties = {'d12': 0.03137, 'd13': 0.095746, 'd23': 0.175383},
    ),
    shortDesc = u"""Fitted to 90 distances.
""",
    longDesc = 
u"""
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 36,
    label = "Cds_Cd_H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 [Cd,Cdd] ux {1,D}
3    H        u0 {1,S}
4    H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.045291, 'd13': 0.08721, 'd23': 0.146565},
        uncertainties = {'d12': 0.039936, 'd13': 0.11405, 'd23': 0.200375},
    ),
    shortDesc = u"""Fitted to 34 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 62,
    label = "Cds_Cds/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.046912, 'd13': 0.095151, 'd23': 0.147575},
        uncertainties = {'d12': 0.040827, 'd13': 0.10972, 'd23': 0.201195},
    ),
    shortDesc = u"""Fitted to 30 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
""",
)

entry(
    index = 63,
    label = "Cds_Cdd/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd ux {1,D}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.028197, 'd13': 0.00347, 'd23': 0.135915},
        uncertainties = {'d12': 0.062566, 'd13': 0.261397, 'd23': 0.364967},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 37,
    label = "Cds_Cd_RH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 [Cd,Cdd] ux {1,D}
3    R!H      ux {1,S}
4    H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.046434, 'd13': 0.054617, 'd23': 0.055242},
        uncertainties = {'d12': 0.02848, 'd13': 0.074958, 'd23': 0.140426},
    ),
    shortDesc = u"""Fitted to 37 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 64,
    label = "Cds_Cds/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.044214, 'd13': 0.053166, 'd23': 0.038586},
        uncertainties = {'d12': 0.032053, 'd13': 0.074402, 'd23': 0.150569},
    ),
    shortDesc = u"""Fitted to 24 distances.
""",
    longDesc = 
u"""
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
""",
)

entry(
    index = 65,
    label = "Cds_Cds/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cd ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.043742, 'd13': -0.012341, 'd23': 0.05318},
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.03851, 'd13': 0.10654, 'd23': 0.209643},
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *1 Cd       u0 {2,D} {3,S} {4,S}
2 *2 [Cd,Cdd] ux {1,D}
3    R!H      ux {1,S}
4    R!H      ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.047561, 'd13': -0.000354, 'd23': -0.044953},
        uncertainties = {'d12': 0.024104, 'd13': 0.114835, 'd23': 0.221848},
    ),
    shortDesc = u"""Fitted to 19 distances.
""",
    longDesc = 
u"""
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
""",
)

entry(
    index = 72,
    label = "Cds_Cds/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 {2,D} {3,S} {4,S}
2 *2 Cd ux {1,D}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.044092, 'd13': 0.005843, 'd23': -0.06979},
        uncertainties = {'d12': 0.032529, 'd13': 0.119377, 'd23': 0.235043},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
""",
)

entry(
    index = 73,
    label = "Cds_Cds/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *1 Cd  u0 {2,D} {3,S} {4,S}
2 *2 Cdd u0 {1,D}
3    Cs  ux {1,S}
4    Cs  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.025502, 'd13': -0.051901, 'd23': -0.04391},
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D}
2 *2 R   ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.006662, 'd13': -0.017622, 'd23': -0.087249},
        uncertainties = {'d12': 0.022863, 'd13': 0.112921, 'd23': 0.164994},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 42,
    label = "Cdd_CC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 C   ux {1,D}
3    C   ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.009779, 'd13': 0.118288, 'd23': 0.023941},
        uncertainties = {'d12': 0.029907, 'd13': 0.162312, 'd23': 0.146926},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
""",
)

entry(
    index = 106,
    label = "Cdd_Cds/Cds",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  ux {1,D}
3    Cd  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.009779, 'd13': 0.118288, 'd23': 0.023941},
        uncertainties = {'d12': 0.029907, 'd13': 0.162312, 'd23': 0.146926},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
""",
)

entry(
    index = 107,
    label = "Cdd_Cds/Cdd",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 C   ux {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.027151, 'd13': -0.038746, 'd23': -0.090485},
        uncertainties = {'d12': 0.035218, 'd13': 0.151784, 'd23': 0.264509},
    ),
    shortDesc = u"""Fitted to 5 distances.
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
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 Cd  ux {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.027151, 'd13': -0.038746, 'd23': -0.090485},
        uncertainties = {'d12': 0.035218, 'd13': 0.151784, 'd23': 0.264509},
    ),
    shortDesc = u"""Fitted to 5 distances.
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *1 Cdd u0 {2,D} {3,D}
2 *2 O   u0 {1,D}
3    O   u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.08543, 'd13': -0.37483, 'd23': -0.435677},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 9,
    label = "Ct_R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u0 {2,T}
2 *2 R ux {1,T}
""",
    distances = DistanceData(
        distances = {'d12': -0.08686, 'd13': 0.034556, 'd23': 0.08383},
        uncertainties = {'d12': 0.035118, 'd13': 0.149368, 'd23': 0.144894},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 21,
    label = "Ct_Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.086533, 'd13': 0.065931, 'd23': 0.126234},
        uncertainties = {'d12': 0.044946, 'd13': 0.113299, 'd23': 0.076632},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 22,
    label = "Ct_Ct/R",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C   u0 {2,T} {3,S}
2 *2 C   ux {1,T}
3    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.088331, 'd13': -0.106634, 'd23': -0.10699},
        uncertainties = {'d12': 0.036576, 'd13': 0.494102, 'd23': 0.536007},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 45,
    label = "Ct_Ct/C",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.088331, 'd13': -0.106634, 'd23': -0.10699},
        uncertainties = {'d12': 0.036576, 'd13': 0.494102, 'd23': 0.536007},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 111,
    label = "Ct_Ct/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.090958, 'd13': -0.099841, 'd23': -0.11991},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 112,
    label = "Ct_Ct/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.088088, 'd13': -0.102411, 'd23': -0.11246},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 113,
    label = "Ct_Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C  u0 {2,T} {3,S}
2 *2 C  ux {1,T}
3    Ct u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.085948, 'd13': -0.117651, 'd23': -0.0886},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 114,
    label = "Ct_Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *1 O u0 {2,D}
2 *2 R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.067256, 'd13': -0.318274, 'd23': -0.155852},
        uncertainties = {'d12': 0.033094, 'd13': 0.215099, 'd23': 0.1646},
    ),
    shortDesc = u"""Fitted to 14 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 10,
    label = "Od_C",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O u0 {2,D}
2 *2 C ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.067256, 'd13': -0.318274, 'd23': -0.155852},
        uncertainties = {'d12': 0.033094, 'd13': 0.215099, 'd23': 0.1646},
    ),
    shortDesc = u"""Fitted to 14 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 23,
    label = "Od_Cds",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C ux {2,D} {3,S}
2 *1 O u0 {1,D}
3    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.05961, 'd13': -0.354429, 'd23': -0.162289},
        uncertainties = {'d12': 0.036582, 'd13': 0.225341, 'd23': 0.174691},
    ),
    shortDesc = u"""Fitted to 12 distances.
""",
    longDesc = 
u"""
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
""",
)

entry(
    index = 24,
    label = "Od_Cdd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C ux {2,D} {3,D}
2 *1 O u0 {1,D}
3    R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.091044, 'd13': -0.205789, 'd23': -0.135826},
        uncertainties = {'d12': 0.04378, 'd13': 1.48025, 'd23': 0.99814},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
""",
)

entry(
    index = 11,
    label = "O2",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *3 H u1
""",
    distances = DistanceData(
        distances = {'d12': -0.013882, 'd13': -0.187527, 'd23': -0.203432},
        uncertainties = {'d12': 0.078021, 'd13': 0.153554, 'd23': 0.218774},
    ),
    shortDesc = u"""Fitted to 44 distances.
""",
    longDesc = 
u"""
[<Entry index=111 label="Ct_Ct/Cs">, <Entry index=5 label="Hj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=5 label="Hj">]
[<Entry index=23 label="Od_Cds">, <Entry index=5 label="Hj">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=8 label="Cd_R">, <Entry index=5 label="Hj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=5 label="Hj">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=5 label="Hj">]
[<Entry index=112 label="Ct_Ct/Cd">, <Entry index=5 label="Hj">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=5 label="Hj">]
[<Entry index=65 label="Cds_Cds/Cd/H">, <Entry index=5 label="Hj">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=5 label="Hj">]
[<Entry index=82 label="Cds_Cdd/Cs/Cs">, <Entry index=5 label="Hj">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=5 label="Hj">]
[<Entry index=113 label="Ct_Ct/Ct">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 6,
    label = "Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 C u1
""",
    distances = DistanceData(
        distances = {'d12': -0.00937, 'd13': 0.143727, 'd23': 0.166583},
        uncertainties = {'d12': 0.076095, 'd13': 0.159197, 'd23': 0.281234},
    ),
    shortDesc = u"""Fitted to 77 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=6 label="Cj">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=23 label="Od_Cds">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=6 label="Cj">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=6 label="Cj">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=6 label="Cj">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=6 label="Cj">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 12,
    label = "Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1
""",
    distances = DistanceData(
        distances = {'d12': -0.01107, 'd13': 0.15573, 'd23': 0.196126},
        uncertainties = {'d12': 0.077118, 'd13': 0.131, 'd23': 0.226695},
    ),
    shortDesc = u"""Fitted to 54 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 25,
    label = "Csj_methyl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.002435, 'd13': 0.168683, 'd23': 0.216852},
        uncertainties = {'d12': 0.072947, 'd13': 0.127742, 'd23': 0.222395},
    ),
    shortDesc = u"""Fitted to 29 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=25 label="Csj_methyl">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=25 label="Csj_methyl">]
[<Entry index=24 label="Od_Cdd">, <Entry index=25 label="Csj_methyl">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=8 label="Cd_R">, <Entry index=25 label="Csj_methyl">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=44 label="CO2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=25 label="Csj_methyl">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=25 label="Csj_methyl">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=25 label="Csj_methyl">]
[<Entry index=23 label="Od_Cds">, <Entry index=25 label="Csj_methyl">]
[<Entry index=68 label="Cds_Cdd/Cs/H">, <Entry index=25 label="Csj_methyl">]
""",
)

entry(
    index = 26,
    label = "Csj_RH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.01306, 'd13': 0.155259, 'd23': 0.191287},
        uncertainties = {'d12': 0.096115, 'd13': 0.152084, 'd23': 0.275029},
    ),
    shortDesc = u"""Fitted to 18 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
""",
)

entry(
    index = 47,
    label = "Csj_CH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.017731, 'd13': 0.143925, 'd23': 0.197404},
        uncertainties = {'d12': 0.110729, 'd13': 0.161598, 'd23': 0.280167},
    ),
    shortDesc = u"""Fitted to 11 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=47 label="Csj_CH2">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
""",
)

entry(
    index = 115,
    label = "Csj_Cs/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.023349, 'd13': 0.141981, 'd23': 0.197492},
        uncertainties = {'d12': 0.117703, 'd13': 0.171082, 'd23': 0.293193},
    ),
    shortDesc = u"""Fitted to 10 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=8 label="Cd_R">, <Entry index=115 label="Csj_Cs/H2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=115 label="Csj_Cs/H2">]
""",
)

entry(
    index = 116,
    label = "Csj_Cd/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.006466, 'd13': 0.171261, 'd23': 0.182651},
        uncertainties = {'d12': 0.102772, 'd13': 0.188833, 'd23': 0.361245},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=48 label="Csj_OH2">]
[<Entry index=106 label="Cdd_Cds/Cds">, <Entry index=48 label="Csj_OH2">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=48 label="Csj_OH2">]
[<Entry index=24 label="Od_Cdd">, <Entry index=48 label="Csj_OH2">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=48 label="Csj_OH2">]
""",
)

entry(
    index = 27,
    label = "Csj_RRH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.055722, 'd13': 0.080161, 'd23': 0.089168},
        uncertainties = {'d12': 0.086847, 'd13': 0.169694, 'd23': 0.240791},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
""",
)

entry(
    index = 49,
    label = "Csj_CCH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.080798, 'd13': 0.02716, 'd23': 0.001713},
        uncertainties = {'d12': 0.019774, 'd13': 0.256458, 'd23': 0.318381},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
[<Entry index=8 label="Cd_R">, <Entry index=49 label="Csj_CCH">]
""",
)

entry(
    index = 119,
    label = "Csj_Cs/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.083531, 'd13': 0.035911, 'd23': 0.019894},
        uncertainties = {'d12': 0.032034, 'd13': 0.41219, 'd23': 0.49995},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=119 label="Csj_Cs/Cs/H">]
""",
)

entry(
    index = 120,
    label = "Csj_Cs/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.030646, 'd13': 0.133162, 'd23': 0.176623},
        uncertainties = {'d12': 0.262472, 'd13': 0.294578, 'd23': 0.509795},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
""",
)

entry(
    index = 129,
    label = "Csj_Cs/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    O  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.030646, 'd13': 0.133162, 'd23': 0.176623},
        uncertainties = {'d12': 0.262472, 'd13': 0.294578, 'd23': 0.509795},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=129 label="Csj_Cs/O/H">]
[<Entry index=8 label="Cd_R">, <Entry index=129 label="Csj_Cs/O/H">]
""",
)

entry(
    index = 130,
    label = "Csj_Cd/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *3 Cd u1
""",
    distances = DistanceData(
        distances = {'d12': -0.011836, 'd13': 0.175425, 'd23': 0.214972},
        uncertainties = {'d12': 0.097184, 'd13': 0.108743, 'd23': 0.228992},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 29,
    label = "Cdj_Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd       u1 {2,D}
2    [Cd,Cdd] ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.011836, 'd13': 0.175425, 'd23': 0.214972},
        uncertainties = {'d12': 0.097184, 'd13': 0.108743, 'd23': 0.228992},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 56,
    label = "Cdj_CdH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    H        u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.043276, 'd13': 0.20029, 'd23': 0.220166},
        uncertainties = {'d12': 0.161992, 'd13': 0.186158, 'd23': 0.404211},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 167,
    label = "Cdj_CdsH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.043276, 'd13': 0.20029, 'd23': 0.220166},
        uncertainties = {'d12': 0.161992, 'd13': 0.186158, 'd23': 0.404211},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct/H">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=8 label="Cd_R">, <Entry index=167 label="Cdj_CdsH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=167 label="Cdj_CdsH">]
""",
)

entry(
    index = 168,
    label = "Cdj_CddH",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *3 Cd       u1 {2,D} {3,S}
2    [Cd,Cdd] ux {1,D}
3    C        ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.006795, 'd13': 0.160691, 'd23': 0.211895},
        uncertainties = {'d12': 0.111369, 'd13': 0.120423, 'd23': 0.242407},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=173 label="Cdj_Cdd/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=170 label="Cdj_Cds/Cd">]
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
""",
)

entry(
    index = 169,
    label = "Cdj_Cds/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.027209, 'd13': 0.174633, 'd23': 0.232747},
        uncertainties = {'d12': 0.913471, 'd13': 0.615556, 'd23': 1.75673},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=8 label="Cd_R">, <Entry index=169 label="Cdj_Cds/Cs">]
[<Entry index=109 label="Cdd_Cds/O">, <Entry index=169 label="Cdj_Cds/Cs">]
""",
)

entry(
    index = 170,
    label = "Cdj_Cds/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.012251, 'd13': 0.26261, 'd23': 0.293781},
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *3 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cs  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.029571, 'd13': 0.099274, 'd23': 0.155313},
        uncertainties = {'d12': 0.36415, 'd13': 0.690849, 'd23': 0.857497},
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *3 Ct u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 31,
    label = "Ctj_Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *3 Cb u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 7,
    label = "Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1
""",
    distances = DistanceData(
        distances = {'d12': 0.029544, 'd13': -0.056477, 'd23': -0.079245},
        uncertainties = {'d12': 0.04345, 'd13': 0.122663, 'd23': 0.117218},
    ),
    shortDesc = u"""Fitted to 37 distances.
""",
    longDesc = 
u"""
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
""",
)

entry(
    index = 16,
    label = "OH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.013221, 'd13': 0.056824, 'd23': -0.105878},
        uncertainties = {'d12': 0.054872, 'd13': 0.189583, 'd23': 0.115007},
    ),
    shortDesc = u"""Fitted to 11 distances.
""",
    longDesc = 
u"""
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=16 label="OH">]
[<Entry index=21 label="Ct_Ct/H">, <Entry index=16 label="OH">]
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=16 label="OH">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=16 label="OH">]
[<Entry index=23 label="Od_Cds">, <Entry index=16 label="OH">]
""",
)

entry(
    index = 17,
    label = "OjC",
    group = 
"""
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
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
multiplicity [1,2,3,4,5]
1 *3 O u1 {2,S}
2    O ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.035945, 'd13': -0.100909, 'd23': -0.068801},
        uncertainties = {'d12': 0.042126, 'd13': 0.100301, 'd23': 0.126031},
    ),
    shortDesc = u"""Fitted to 26 distances.
""",
    longDesc = 
u"""
[<Entry index=64 label="Cds_Cds/Cs/H">, <Entry index=18 label="OjO">]
[<Entry index=62 label="Cds_Cds/H2">, <Entry index=18 label="OjO">]
[<Entry index=63 label="Cds_Cdd/H2">, <Entry index=18 label="OjO">]
[<Entry index=72 label="Cds_Cds/Cs/Cs">, <Entry index=18 label="OjO">]
[<Entry index=37 label="Cds_Cd_RH">, <Entry index=18 label="OjO">]
[<Entry index=38 label="Cds_Cd_RR">, <Entry index=18 label="OjO">]
""",
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

