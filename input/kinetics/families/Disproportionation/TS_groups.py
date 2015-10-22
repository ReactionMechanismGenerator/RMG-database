#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/TS_groups"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 1,
    label = "Y_rad_birad_trirad_quadrad",
    group = "OR{Hrad, Orad, Crad}",
    distances = DistanceData(
        distances = {'d12': 1.43689, 'd13': 2.54711, 'd23': 1.12424},
        uncertainties = {'d12': 0.141937, 'd13': 0.118992, 'd23': 0.072871},
    ),
    shortDesc = u"""Fitted to 60 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=7 label="OH_R_rad">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=5 label="Crad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=104 label="CdH_Cd_Cdj">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=105 label="CdH_Ct_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=16 label="OjH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=3 label="Hrad">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=7 label="OH_R_rad">]
[<Entry index=16 label="OjH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=101 label="CdH_Cds_Oj">]
[<Entry index=59 label="CsjOH2">, <Entry index=7 label="OH_R_rad">]
[<Entry index=3 label="Hrad">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
""",
)

entry(
    index = 2,
    label = "XH_Rrad_birad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 R!H u0 {2,[S,D]} {3,S}
2 *3 R!H u1 {1,[S,D]}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 3,
    label = "Hrad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 H u1
""",
    distances = DistanceData(
        distances = {'d12': -0.039948, 'd13': -0.241565, 'd23': -0.205448},
        uncertainties = {'d12': 0.164339, 'd13': 0.172674, 'd23': 0.095642},
    ),
    shortDesc = u"""Fitted to 14 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="Hrad">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=105 label="CdH_Ct_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=3 label="Hrad">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=104 label="CdH_Cd_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=7 label="OH_R_rad">]
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
""",
)

entry(
    index = 4,
    label = "Orad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O u[1,2]
""",
    distances = DistanceData(
        distances = {'d12': 0.086633, 'd13': 0.033731, 'd23': -0.051578},
        uncertainties = {'d12': 0.173326, 'd13': 0.120209, 'd23': 0.063431},
    ),
    shortDesc = u"""Fitted to 25 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
[<Entry index=18 label="OjO">, <Entry index=101 label="CdH_Cds_Oj">]
[<Entry index=16 label="OjH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
[<Entry index=18 label="OjO">, <Entry index=7 label="OH_R_rad">]
[<Entry index=16 label="OjH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
""",
)

entry(
    index = 8,
    label = "OjR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O u1 {2,S}
2    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.086633, 'd13': 0.033731, 'd23': -0.051578},
        uncertainties = {'d12': 0.173326, 'd13': 0.120209, 'd23': 0.063431},
    ),
    shortDesc = u"""Fitted to 25 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
[<Entry index=18 label="OjO">, <Entry index=101 label="CdH_Cds_Oj">]
[<Entry index=16 label="OjH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
[<Entry index=18 label="OjO">, <Entry index=7 label="OH_R_rad">]
[<Entry index=16 label="OjH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
""",
)

entry(
    index = 16,
    label = "OjH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.214997, 'd13': -0.08773, 'd23': 0.137453},
        uncertainties = {'d12': 0.367215, 'd13': 0.25687, 'd23': 0.554846},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=16 label="OjH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=16 label="OjH">, <Entry index=55 label="CdH2_Cdj">]
""",
)

entry(
    index = 17,
    label = "OjC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O u1 {2,S}
2    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 33,
    label = "OjCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u1 {2,S}
2    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 34,
    label = "OjCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u1 {2,S}
2    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 35,
    label = "OjCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u1 {2,S}
2    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 36,
    label = "OjCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O  u1 {2,S}
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
1 *1 O u1 {2,S}
2    O ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.117073, 'd13': 0.045989, 'd23': -0.070655},
        uncertainties = {'d12': 0.181459, 'd13': 0.125843, 'd23': 0.063711},
    ),
    shortDesc = u"""Fitted to 23 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=18 label="OjO">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=101 label="CdH_Cds_Oj">]
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=7 label="OH_R_rad">]
""",
)

entry(
    index = 9,
    label = "O_atom_triplet",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 O u2
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 5,
    label = "Crad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u[1,2,3,4]
""",
    distances = DistanceData(
        distances = {'d12': -0.059505, 'd13': 0.12626, 'd23': 0.186985},
        uncertainties = {'d12': 0.106742, 'd13': 0.098032, 'd23': 0.080922},
    ),
    shortDesc = u"""Fitted to 21 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=59 label="CsjOH2">, <Entry index=7 label="OH_R_rad">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=5 label="Crad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
""",
)

entry(
    index = 10,
    label = "Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u1
""",
    distances = DistanceData(
        distances = {'d12': -0.065792, 'd13': 0.120775, 'd23': 0.186728},
        uncertainties = {'d12': 0.098306, 'd13': 0.079194, 'd23': 0.080268},
    ),
    shortDesc = u"""Fitted to 20 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=59 label="CsjOH2">, <Entry index=7 label="OH_R_rad">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
""",
)

entry(
    index = 19,
    label = "Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1
""",
    distances = DistanceData(
        distances = {'d12': -0.063825, 'd13': 0.127954, 'd23': 0.190737},
        uncertainties = {'d12': 0.100137, 'd13': 0.08858, 'd23': 0.084212},
    ),
    shortDesc = u"""Fitted to 16 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=59 label="CsjOH2">, <Entry index=7 label="OH_R_rad">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 37,
    label = "Cs_methyl",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.09543, 'd13': 0.125384, 'd23': 0.213216},
        uncertainties = {'d12': 0.131041, 'd13': 0.118242, 'd23': 0.080446},
    ),
    shortDesc = u"""Fitted to 9 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
""",
)

entry(
    index = 38,
    label = "CsjRH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    R  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.021731, 'd13': 0.119072, 'd23': 0.150965},
        uncertainties = {'d12': 0.107375, 'd13': 0.090857, 'd23': 0.13728},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=59 label="CsjOH2">, <Entry index=7 label="OH_R_rad">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
""",
)

entry(
    index = 58,
    label = "CsjCH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.018854, 'd13': 0.137483, 'd23': 0.111983},
        uncertainties = {'d12': 0.530829, 'd13': 0.156628, 'd23': 0.491418},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 107,
    label = "Csj/Cs/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 108,
    label = "Csj/Cd/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.018854, 'd13': 0.137483, 'd23': 0.111983},
        uncertainties = {'d12': 0.530829, 'd13': 0.156628, 'd23': 0.491418},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 109,
    label = "Csj/Ct/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 110,
    label = "Csj/Cb/H2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 59,
    label = "CsjOH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.059417, 'd13': 0.101975, 'd23': 0.187163},
        uncertainties = {'d12': 0.198044, 'd13': 0.19556, 'd23': 0.276898},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=59 label="CsjOH2">, <Entry index=7 label="OH_R_rad">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
""",
)

entry(
    index = 39,
    label = "CsjRRH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    R  ux {1,S}
4    R  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.024827, 'd13': 0.156684, 'd23': 0.183422},
        uncertainties = {'d12': 0.456649, 'd13': 0.308491, 'd23': 0.793499},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 60,
    label = "CsjCCH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.024827, 'd13': 0.156684, 'd23': 0.183422},
        uncertainties = {'d12': 0.456649, 'd13': 0.308491, 'd23': 0.793499},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 111,
    label = "Csj/Cs/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 112,
    label = "Csj/Cs/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.024827, 'd13': 0.156684, 'd23': 0.183422},
        uncertainties = {'d12': 0.456649, 'd13': 0.308491, 'd23': 0.793499},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 113,
    label = "Csj/Cs/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 114,
    label = "Csj/Cs/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 115,
    label = "Csj/Cd/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 116,
    label = "Csj/Cd/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 117,
    label = "Csj/Cd/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 118,
    label = "Csj/Ct/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 119,
    label = "Csj/Ct/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 120,
    label = "Csj/Cb/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 61,
    label = "CsjCOH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 121,
    label = "Csj/Cs/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 122,
    label = "Csj/Cd/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 123,
    label = "Csj/Ct/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 124,
    label = "Csj/Cb/O/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 62,
    label = "CsjOOH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 40,
    label = "CsjRRR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    R  ux {1,S}
3    R  ux {1,S}
4    R  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 63,
    label = "CsjCCC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 125,
    label = "Csj/Cs/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 126,
    label = "Csj/Cs/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 127,
    label = "Csj/Cs/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 128,
    label = "Csj/Cs/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 129,
    label = "Csj/Cs/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 130,
    label = "Csj/Cs/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 131,
    label = "Csj/Cs/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 132,
    label = "Csj/Cs/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 133,
    label = "Csj/Cs/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 134,
    label = "Csj/Cs/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 135,
    label = "Csj/Cd/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 136,
    label = "Csj/Cd/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 137,
    label = "Csj/Cd/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 138,
    label = "Csj/Cd/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 139,
    label = "Csj/Cd/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 140,
    label = "Csj/Cd/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 141,
    label = "Csj/Ct/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 142,
    label = "Csj/Ct/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 143,
    label = "Csj/Ct/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 144,
    label = "Csj/Cb/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 64,
    label = "CsjCCO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 145,
    label = "Csj/Cs/Cs/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 146,
    label = "Csj/Cs/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 147,
    label = "Csj/Cs/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 148,
    label = "Csj/Cs/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 149,
    label = "Csj/Cd/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 150,
    label = "Csj/Cd/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 151,
    label = "Csj/Cd/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 152,
    label = "Csj/Ct/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 153,
    label = "Csj/Ct/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 154,
    label = "Csj/Cb/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 65,
    label = "CsjCOO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 155,
    label = "Csj/Cs/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cs ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 156,
    label = "Csj/Cd/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cd ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 157,
    label = "Csj/Ct/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Ct u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 158,
    label = "Csj/Cb/O/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    Cb u0 {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 66,
    label = "CsjOOO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    O  ux {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 20,
    label = "Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1
""",
    distances = DistanceData(
        distances = {'d12': -0.073332, 'd13': 0.093255, 'd23': 0.17136},
        uncertainties = {'d12': 0.172432, 'd13': 0.06611, 'd23': 0.123653},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 41,
    label = "Cdj_CR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D}
2    C  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.073332, 'd13': 0.093255, 'd23': 0.17136},
        uncertainties = {'d12': 0.172432, 'd13': 0.06611, 'd23': 0.123653},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 67,
    label = "Cdj_CH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.073332, 'd13': 0.093255, 'd23': 0.17136},
        uncertainties = {'d12': 0.172432, 'd13': 0.06611, 'd23': 0.123653},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 159,
    label = "Cdj_CdsH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.092594, 'd13': 0.091955, 'd23': 0.192117},
        uncertainties = {'d12': 0.285516, 'd13': 0.105911, 'd23': 0.203821},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 160,
    label = "Cdj_CddH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.015547, 'd13': 0.097154, 'd23': 0.109089},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
""",
)

entry(
    index = 68,
    label = "Cdj_CC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 161,
    label = "Cdj_CdsCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 162,
    label = "Cdj_CdsCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 163,
    label = "Cdj_CdsCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 164,
    label = "Cdj_CdsCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 165,
    label = "Cdj_CddCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cs  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 166,
    label = "Cdj_CddCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cd  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 167,
    label = "Cdj_CddCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Ct  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 168,
    label = "Cdj_CddCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    Cb  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 69,
    label = "Cdj_CO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 169,
    label = "Cdj_CdsO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 170,
    label = "Cdj_CddO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    O   ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 42,
    label = "Cdj_OR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D}
2    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 70,
    label = "Cdj_OH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 71,
    label = "Cdj_OC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 171,
    label = "Cdj_OCs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 172,
    label = "Cdj_OCd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 173,
    label = "Cdj_OCt",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 174,
    label = "Cdj_OCb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 72,
    label = "Cdj_OO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u1 {2,D} {3,S}
2    O  u0 {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 21,
    label = "Ctj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Ct u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 43,
    label = "CtjC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Ct u1 {2,T}
2    C  ux {1,T}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 22,
    label = "Cbj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cb u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 11,
    label = "Cjj",
    group = "OR{Csjj, Cdjj}",
    distances = DistanceData(distances={}),
)

entry(
    index = 23,
    label = "Csjj",
    group = "OR{Cs_sing, Cs_trip}",
    distances = DistanceData(distances={}),
)

entry(
    index = 44,
    label = "Cs_sing",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 73,
    label = "Cs_singH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 74,
    label = "Cs_singRH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs  u0 p1 {2,S} {3,S}
2    H   u0 {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 175,
    label = "Cs_singCH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 245,
    label = "Cs_sing/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 246,
    label = "Cs_sing/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 247,
    label = "Cs_sing/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 248,
    label = "Cs_sing/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 176,
    label = "Cs_singOH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    H  u0 {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 75,
    label = "Cs_singRR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs  u0 p1 {2,S} {3,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 177,
    label = "Cs_singCC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    C  ux {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 249,
    label = "Cs_sing/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 250,
    label = "Cs_sing/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 251,
    label = "Cs_sing/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 252,
    label = "Cs_sing/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 253,
    label = "Cs_sing/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 254,
    label = "Cs_sing/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 255,
    label = "Cs_sing/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 256,
    label = "Cs_sing/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 257,
    label = "Cs_sing/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 258,
    label = "Cs_sing/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 178,
    label = "Cs_singCO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    C  ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 259,
    label = "Cs_sing/Cs/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cs ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 260,
    label = "Cs_sing/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cd ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 261,
    label = "Cs_sing/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Ct u0 {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 262,
    label = "Cs_sing/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    Cb u0 {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 179,
    label = "Cs_singOO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u0 p1 {2,S} {3,S}
2    O  ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 45,
    label = "Cs_trip",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 76,
    label = "Cs_tripH2",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 77,
    label = "Cs_tripRH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs  u2 p0 {2,S} {3,S}
2    R!H ux {1,S}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 180,
    label = "Cs_tripCH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    C  ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 263,
    label = "Cs_trip/Cs/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 264,
    label = "Cs_trip/Cd/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 265,
    label = "Cs_trip/Ct/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Ct u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 266,
    label = "Cs_trip/Cb/H",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cb u0 {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 181,
    label = "Cs_tripOH",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    O  ux {1,S}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 78,
    label = "Cs_tripRR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs  u2 p0 {2,S} {3,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 182,
    label = "Cs_tripCC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    C  ux {1,S}
3    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 267,
    label = "Cs_trip/Cs/Cs",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 268,
    label = "Cs_trip/Cs/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 269,
    label = "Cs_trip/Cs/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 270,
    label = "Cs_trip/Cs/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 271,
    label = "Cs_trip/Cd/Cd",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 272,
    label = "Cs_trip/Cd/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 273,
    label = "Cs_trip/Cd/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 274,
    label = "Cs_trip/Ct/Ct",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Ct u0 {1,S}
3    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 275,
    label = "Cs_trip/Ct/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Ct u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 276,
    label = "Cs_trip/Cb/Cb",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cb u0 {1,S}
3    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 183,
    label = "Cs_tripCO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    C  ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 277,
    label = "Cs_trip/Cs/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cs ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 278,
    label = "Cs_trip/Cd/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cd ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 279,
    label = "Cs_trip/Ct/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Ct ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 280,
    label = "Cs_trip/Cb/O",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    Cb ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 184,
    label = "Cs_tripOO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cs u2 p0 {2,S} {3,S}
2    O  ux {1,S}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 24,
    label = "Cdjj",
    group = "OR{Cd_singletR, Cd_tripletR}",
    distances = DistanceData(distances={}),
)

entry(
    index = 46,
    label = "Cd_singletR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 79,
    label = "Cd_singletC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 p1 {2,D}
2    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 80,
    label = "Cd_singletO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u0 p1 {2,D}
2    O  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 47,
    label = "Cd_tripletR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u2 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 81,
    label = "Cd_tripletC",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u2 p0 {2,D}
2    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 82,
    label = "Cd_tripletO",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 Cd u2 p0 {2,D}
2    O  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 12,
    label = "Cjjj",
    group = "OR{C_doubletR, C_quartetR}",
    distances = DistanceData(distances={}),
)

entry(
    index = 25,
    label = "C_doubletR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u1 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 26,
    label = "C_quartetR",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u3
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 13,
    label = "Cjjjj",
    group = "OR{C_quintet, C_triplet}",
    distances = DistanceData(distances={}),
)

entry(
    index = 27,
    label = "C_quintet",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u4 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 28,
    label = "C_triplet",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *1 C u2 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 6,
    label = "CH_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C   u0 {2,[S,D]} {3,S}
2 *3 R!H u1 {1,[S,D]}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.001887, 'd13': 0.018803, 'd23': 0.015887},
        uncertainties = {'d12': 0.104169, 'd13': 0.095887, 'd23': 0.073905},
    ),
    shortDesc = u"""Fitted to 47 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=5 label="Crad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=104 label="CdH_Cd_Cdj">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=105 label="CdH_Ct_Cdj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=16 label="OjH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=3 label="Hrad">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=101 label="CdH_Cds_Oj">]
[<Entry index=16 label="OjH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
""",
)

entry(
    index = 14,
    label = "CH_s_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C   u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.020386, 'd13': 0.02754, 'd23': 0.04324},
        uncertainties = {'d12': 0.090551, 'd13': 0.065309, 'd23': 0.063314},
    ),
    shortDesc = u"""Fitted to 35 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=3 label="Hrad">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=101 label="CdH_Cds_Oj">]
[<Entry index=16 label="OjH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
""",
)

entry(
    index = 29,
    label = "CsH_s_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cs  u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.024335, 'd13': 0.026644, 'd23': 0.046784},
        uncertainties = {'d12': 0.086078, 'd13': 0.065421, 'd23': 0.062089},
    ),
    shortDesc = u"""Fitted to 28 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=3 label="Hrad">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
""",
)

entry(
    index = 48,
    label = "C_methyl_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.021138, 'd13': 0.030879, 'd23': 0.047939},
        uncertainties = {'d12': 0.089342, 'd13': 0.06849, 'd23': 0.068019},
    ),
    shortDesc = u"""Fitted to 21 distances.
""",
    longDesc = 
u"""
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
""",
)

entry(
    index = 83,
    label = "C_methyl_Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.006368, 'd13': 0.026672, 'd23': 0.023482},
        uncertainties = {'d12': 0.095786, 'd13': 0.070893, 'd23': 0.06454},
    ),
    shortDesc = u"""Fitted to 16 distances.
""",
    longDesc = 
u"""
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=83 label="C_methyl_Cj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=83 label="C_methyl_Cj">]
""",
)

entry(
    index = 185,
    label = "C_methyl_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.006447, 'd13': 0.031346, 'd23': 0.015107},
        uncertainties = {'d12': 0.078237, 'd13': 0.068687, 'd23': 0.060083},
    ),
    shortDesc = u"""Fitted to 13 distances.
""",
    longDesc = 
u"""
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 186,
    label = "C_methyl_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.017116, 'd13': 0.028894, 'd23': 0.043785},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=186 label="C_methyl_Cdj">]
""",
)

entry(
    index = 84,
    label = "C_methyl_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.060904, 'd13': 0.042204, 'd23': 0.113783},
        uncertainties = {'d12': 0.111018, 'd13': 0.097838, 'd23': 0.120326},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=112 label="Csj/Cs/Cd/H">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=59 label="CsjOH2">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
""",
)

entry(
    index = 49,
    label = "CsRHH_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
4    H   u0 {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.04126, 'd13': 0.010818, 'd23': 0.047006},
        uncertainties = {'d12': 0.108158, 'd13': 0.085848, 'd23': 0.059937},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=3 label="Hrad">, <Entry index=195 label="CsH2_Cs_Oj">]
""",
)

entry(
    index = 85,
    label = "CsH2_C_Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.018494, 'd13': 0.02346, 'd23': 0.004125},
        uncertainties = {'d12': 0.234635, 'd13': 0.102373, 'd23': 0.14339},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
""",
)

entry(
    index = 187,
    label = "CsH2_Cs_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.018494, 'd13': 0.02346, 'd23': 0.004125},
        uncertainties = {'d12': 0.234635, 'd13': 0.102373, 'd23': 0.14339},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
""",
)

entry(
    index = 188,
    label = "CsH2_Cs_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 189,
    label = "CsH2_Cd_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 190,
    label = "CsH2_Cd_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 191,
    label = "CsH2_Ct_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 192,
    label = "CsH2_Ct_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 193,
    label = "CsH2_Cb_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 194,
    label = "CsH2_Cb_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 86,
    label = "CsH2_C_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.120932, 'd13': -0.006038, 'd23': 0.104179},
        uncertainties = {'d12': 0.163955, 'd13': 0.202828, 'd23': 0.067833},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=195 label="CsH2_Cs_Oj">]
""",
)

entry(
    index = 195,
    label = "CsH2_Cs_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.120932, 'd13': -0.006038, 'd23': 0.104179},
        uncertainties = {'d12': 0.163955, 'd13': 0.202828, 'd23': 0.067833},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=195 label="CsH2_Cs_Oj">]
[<Entry index=3 label="Hrad">, <Entry index=195 label="CsH2_Cs_Oj">]
""",
)

entry(
    index = 196,
    label = "CsH2_Cd_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 197,
    label = "CsH2_Ct_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Ct ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 198,
    label = "CsH2_Cb_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cb ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 87,
    label = "CsH2_O_Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 199,
    label = "CsH2_O_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 200,
    label = "CsH2_O_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 88,
    label = "CsH2_O_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 50,
    label = "CsRRH_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
4    R!H ux {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.012196, 'd13': 0.008084, 'd23': 0.017895},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
""",
)

entry(
    index = 89,
    label = "CsH_CC_Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    C ux {1,S}
5    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.012196, 'd13': 0.008084, 'd23': 0.017895},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
""",
)

entry(
    index = 201,
    label = "CsH_CsCs_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.012196, 'd13': 0.008084, 'd23': 0.017895},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=201 label="CsH_CsCs_Csj">]
""",
)

entry(
    index = 202,
    label = "CsH_CsCd_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 203,
    label = "CsH_CsCt_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 204,
    label = "CsH_CsCb_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 205,
    label = "CsH_CdCd_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 206,
    label = "CsH_CdCt_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 207,
    label = "CsH_CdCb_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 208,
    label = "CsH_CtCt_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 209,
    label = "CsH_CtCb_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 210,
    label = "CsH_CbCb_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cb u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 211,
    label = "CsH_CsCs_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 212,
    label = "CsH_CsCd_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 213,
    label = "CsH_CsCt_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 214,
    label = "CsH_CsCb_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 215,
    label = "CsH_CdCd_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 216,
    label = "CsH_CdCt_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 217,
    label = "CsH_CdCb_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 218,
    label = "CsH_CtCt_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 219,
    label = "CsH_CtCb_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 220,
    label = "CsH_CbCb_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cb u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 90,
    label = "CsH_CO_Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    C ux {1,S}
5    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 221,
    label = "CsH_CsO_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 222,
    label = "CsH_CdO_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 223,
    label = "CsH_CtO_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 224,
    label = "CsH_CbO_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cb u0 {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 225,
    label = "CsH_CsO_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 226,
    label = "CsH_CdO_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 227,
    label = "CsH_CtO_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 228,
    label = "CsH_CbO_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cb u0 {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 91,
    label = "CsH_OO_Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    O ux {1,S}
5    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 229,
    label = "CsH_OO_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    O  ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 230,
    label = "CsH_OO_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    O  ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 92,
    label = "CsH_CC_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
4    C ux {1,S}
5    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 231,
    label = "CsH_CsCs_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 232,
    label = "CsH_CsCd_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 233,
    label = "CsH_CsCt_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 234,
    label = "CsH_CsCb_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 235,
    label = "CsH_CdCd_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 236,
    label = "CsH_CdCt_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 237,
    label = "CsH_CdCb_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 238,
    label = "CsH_CtCt_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
5    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 239,
    label = "CsH_CtCb_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 240,
    label = "CsH_CbCb_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cb u0 {1,S}
5    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 93,
    label = "CsH_CO_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
4    C ux {1,S}
5    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 241,
    label = "CsH_CsO_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 242,
    label = "CsH_CdO_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 243,
    label = "CsH_CtO_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 244,
    label = "CsH_CbO_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cb u0 {1,S}
5    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 94,
    label = "CsH_OO_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
4    O ux {1,S}
5    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 30,
    label = "CdH_s_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd  u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.007814, 'd13': 0.030392, 'd23': 0.031958},
        uncertainties = {'d12': 0.141209, 'd13': 0.087458, 'd23': 0.090885},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=101 label="CdH_Cds_Oj">]
[<Entry index=16 label="OjH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
""",
)

entry(
    index = 51,
    label = "CdH_C_Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 C  u1 {1,S}
3 *4 H  u0 {1,S}
4    C  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.007437, 'd13': 0.03283, 'd23': 0.032377},
        uncertainties = {'d12': 0.154247, 'd13': 0.098587, 'd23': 0.099807},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=16 label="OjH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
""",
)

entry(
    index = 95,
    label = "CdH_Cds_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.007437, 'd13': 0.03283, 'd23': 0.032377},
        uncertainties = {'d12': 0.154247, 'd13': 0.098587, 'd23': 0.099807},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=16 label="OjH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=18 label="OjO">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=108 label="Csj/Cd/H2">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=160 label="Cdj_CddH">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=95 label="CdH_Cds_Csj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=95 label="CdH_Cds_Csj">]
""",
)

entry(
    index = 96,
    label = "CdH_Cds_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 97,
    label = "CdH_Cdd_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd  u0 {2,S} {3,S} {4,D}
2 *3 Cs  u1 {1,S}
3 *4 H   u0 {1,S}
4    Cdd ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 98,
    label = "CdH_Cdd_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd  u0 {2,S} {3,S} {4,D}
2 *3 Cd  u1 {1,S}
3 *4 H   u0 {1,S}
4    Cdd ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 52,
    label = "CdH_O_Cj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 C  u1 {1,S}
3 *4 H  u0 {1,S}
4    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 99,
    label = "CdH_Od_Csj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 100,
    label = "CdH_Od_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 53,
    label = "CdH_C_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    C  u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.011026, 'd13': 0.009674, 'd23': 0.028395},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=101 label="CdH_Cds_Oj">]
""",
)

entry(
    index = 101,
    label = "CdH_Cds_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.011026, 'd13': 0.009674, 'd23': 0.028395},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=101 label="CdH_Cds_Oj">]
""",
)

entry(
    index = 102,
    label = "CdH_Cdd_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd  u0 {2,S} {3,S} {4,D}
2 *3 O   u1 {1,S}
3 *4 H   u0 {1,S}
4    Cdd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 54,
    label = "CdH_O_Oj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 15,
    label = "CH_d_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C   u0 {2,D} {3,S}
2 *3 R!H u1 {1,D}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.097604, 'd13': -0.018741, 'd23': -0.101659},
        uncertainties = {'d12': 0.156612, 'd13': 0.174661, 'd23': 0.113029},
    ),
    shortDesc = u"""Fitted to 12 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=105 label="CdH_Ct_Cdj">]
[<Entry index=5 label="Crad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=104 label="CdH_Cd_Cdj">]
[<Entry index=16 label="OjH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
""",
)

entry(
    index = 31,
    label = "CdH2_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C   u0 {2,D} {3,S} {4,S}
2 *3 R!H u1 {1,D}
3 *4 H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.105832, 'd13': -0.00501, 'd23': -0.096005},
        uncertainties = {'d12': 0.189773, 'd13': 0.176412, 'd23': 0.076366},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=5 label="Crad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=16 label="OjH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
""",
)

entry(
    index = 55,
    label = "CdH2_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.105832, 'd13': -0.00501, 'd23': -0.096005},
        uncertainties = {'d12': 0.189773, 'd13': 0.176412, 'd23': 0.076366},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=5 label="Crad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=16 label="OjH">, <Entry index=55 label="CdH2_Cdj">]
[<Entry index=159 label="Cdj_CdsH">, <Entry index=55 label="CdH2_Cdj">]
""",
)

entry(
    index = 32,
    label = "CdRH_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C   u0 {2,D} {3,S} {4,S}
2 *3 R!H u1 {1,D}
3 *4 H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.078157, 'd13': -0.051195, 'd23': -0.115024},
        uncertainties = {'d12': 0.189241, 'd13': 0.319887, 'd23': 0.270717},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=105 label="CdH_Ct_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=104 label="CdH_Cd_Cdj">]
""",
)

entry(
    index = 56,
    label = "CdH_C_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.078157, 'd13': -0.051195, 'd23': -0.115024},
        uncertainties = {'d12': 0.189241, 'd13': 0.319887, 'd23': 0.270717},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=105 label="CdH_Ct_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=104 label="CdH_Cd_Cdj">]
""",
)

entry(
    index = 103,
    label = "CdH_Cs_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.089348, 'd13': -0.010543, 'd23': -0.08227},
        uncertainties = {'d12': 1.25849, 'd13': 0.427774, 'd23': 0.312262},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=103 label="CdH_Cs_Cdj">]
[<Entry index=3 label="Hrad">, <Entry index=103 label="CdH_Cs_Cdj">]
""",
)

entry(
    index = 104,
    label = "CdH_Cd_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.116792, 'd13': -0.076181, 'd23': -0.194827},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="Hrad">, <Entry index=104 label="CdH_Cd_Cdj">]
""",
)

entry(
    index = 105,
    label = "CdH_Ct_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.000352, 'd13': -0.168491, 'd23': -0.149859},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="Hrad">, <Entry index=105 label="CdH_Ct_Cdj">]
""",
)

entry(
    index = 106,
    label = "CdH_Cb_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    Cb u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 57,
    label = "CdH_O_Cdj",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 7,
    label = "OH_R_rad",
    group = 
"""
multiplicity [1,2,3,4,5]
1 *2 O   u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.00698, 'd13': -0.069535, 'd23': -0.058751},
        uncertainties = {'d12': 0.262111, 'd13': 0.203084, 'd23': 0.080145},
    ),
    shortDesc = u"""Fitted to 13 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=18 label="OjO">, <Entry index=7 label="OH_R_rad">]
[<Entry index=59 label="CsjOH2">, <Entry index=7 label="OH_R_rad">]
[<Entry index=3 label="Hrad">, <Entry index=7 label="OH_R_rad">]
""",
)

tree(
"""
L1: Y_rad_birad_trirad_quadrad
    L2: Hrad
    L2: Orad
        L3: OjR
            L4: OjH
            L4: OjC
                L5: OjCs
                L5: OjCd
                L5: OjCt
                L5: OjCb
            L4: OjO
        L3: O_atom_triplet
    L2: Crad
        L3: Cj
            L4: Csj
                L5: Cs_methyl
                L5: CsjRH2
                    L6: CsjCH2
                        L7: Csj/Cs/H2
                        L7: Csj/Cd/H2
                        L7: Csj/Ct/H2
                        L7: Csj/Cb/H2
                    L6: CsjOH2
                L5: CsjRRH
                    L6: CsjCCH
                        L7: Csj/Cs/Cs/H
                        L7: Csj/Cs/Cd/H
                        L7: Csj/Cs/Ct/H
                        L7: Csj/Cs/Cb/H
                        L7: Csj/Cd/Cd/H
                        L7: Csj/Cd/Ct/H
                        L7: Csj/Cd/Cb/H
                        L7: Csj/Ct/Ct/H
                        L7: Csj/Ct/Cb/H
                        L7: Csj/Cb/Cb/H
                    L6: CsjCOH
                        L7: Csj/Cs/O/H
                        L7: Csj/Cd/O/H
                        L7: Csj/Ct/O/H
                        L7: Csj/Cb/O/H
                    L6: CsjOOH
                L5: CsjRRR
                    L6: CsjCCC
                        L7: Csj/Cs/Cs/Cs
                        L7: Csj/Cs/Cs/Cd
                        L7: Csj/Cs/Cs/Ct
                        L7: Csj/Cs/Cs/Cb
                        L7: Csj/Cs/Cd/Cd
                        L7: Csj/Cs/Cd/Ct
                        L7: Csj/Cs/Cd/Cb
                        L7: Csj/Cs/Ct/Ct
                        L7: Csj/Cs/Ct/Cb
                        L7: Csj/Cs/Cb/Cb
                        L7: Csj/Cd/Cd/Cd
                        L7: Csj/Cd/Cd/Ct
                        L7: Csj/Cd/Cd/Cb
                        L7: Csj/Cd/Ct/Ct
                        L7: Csj/Cd/Ct/Cb
                        L7: Csj/Cd/Cb/Cb
                        L7: Csj/Ct/Ct/Ct
                        L7: Csj/Ct/Ct/Cb
                        L7: Csj/Ct/Cb/Cb
                        L7: Csj/Cb/Cb/Cb
                    L6: CsjCCO
                        L7: Csj/Cs/Cs/O
                        L7: Csj/Cs/Cd/O
                        L7: Csj/Cs/Ct/O
                        L7: Csj/Cs/Cb/O
                        L7: Csj/Cd/Cd/O
                        L7: Csj/Cd/Ct/O
                        L7: Csj/Cd/Cb/O
                        L7: Csj/Ct/Ct/O
                        L7: Csj/Ct/Cb/O
                        L7: Csj/Cb/Cb/O
                    L6: CsjCOO
                        L7: Csj/Cs/O/O
                        L7: Csj/Cd/O/O
                        L7: Csj/Ct/O/O
                        L7: Csj/Cb/O/O
                    L6: CsjOOO
            L4: Cdj
                L5: Cdj_CR
                    L6: Cdj_CH
                        L7: Cdj_CdsH
                        L7: Cdj_CddH
                    L6: Cdj_CC
                        L7: Cdj_CdsCs
                        L7: Cdj_CdsCd
                        L7: Cdj_CdsCt
                        L7: Cdj_CdsCb
                        L7: Cdj_CddCs
                        L7: Cdj_CddCd
                        L7: Cdj_CddCt
                        L7: Cdj_CddCb
                    L6: Cdj_CO
                        L7: Cdj_CdsO
                        L7: Cdj_CddO
                L5: Cdj_OR
                    L6: Cdj_OH
                    L6: Cdj_OC
                        L7: Cdj_OCs
                        L7: Cdj_OCd
                        L7: Cdj_OCt
                        L7: Cdj_OCb
                    L6: Cdj_OO
            L4: Ctj
                L5: CtjC
            L4: Cbj
        L3: Cjj
            L4: Csjj
                L5: Cs_sing
                    L6: Cs_singH2
                    L6: Cs_singRH
                        L7: Cs_singCH
                            L8: Cs_sing/Cs/H
                            L8: Cs_sing/Cd/H
                            L8: Cs_sing/Ct/H
                            L8: Cs_sing/Cb/H
                        L7: Cs_singOH
                    L6: Cs_singRR
                        L7: Cs_singCC
                            L8: Cs_sing/Cs/Cs
                            L8: Cs_sing/Cs/Cd
                            L8: Cs_sing/Cs/Ct
                            L8: Cs_sing/Cs/Cb
                            L8: Cs_sing/Cd/Cd
                            L8: Cs_sing/Cd/Ct
                            L8: Cs_sing/Cd/Cb
                            L8: Cs_sing/Ct/Ct
                            L8: Cs_sing/Ct/Cb
                            L8: Cs_sing/Cb/Cb
                        L7: Cs_singCO
                            L8: Cs_sing/Cs/O
                            L8: Cs_sing/Cd/O
                            L8: Cs_sing/Ct/O
                            L8: Cs_sing/Cb/O
                        L7: Cs_singOO
                L5: Cs_trip
                    L6: Cs_tripH2
                    L6: Cs_tripRH
                        L7: Cs_tripCH
                            L8: Cs_trip/Cs/H
                            L8: Cs_trip/Cd/H
                            L8: Cs_trip/Ct/H
                            L8: Cs_trip/Cb/H
                        L7: Cs_tripOH
                    L6: Cs_tripRR
                        L7: Cs_tripCC
                            L8: Cs_trip/Cs/Cs
                            L8: Cs_trip/Cs/Cd
                            L8: Cs_trip/Cs/Ct
                            L8: Cs_trip/Cs/Cb
                            L8: Cs_trip/Cd/Cd
                            L8: Cs_trip/Cd/Ct
                            L8: Cs_trip/Cd/Cb
                            L8: Cs_trip/Ct/Ct
                            L8: Cs_trip/Ct/Cb
                            L8: Cs_trip/Cb/Cb
                        L7: Cs_tripCO
                            L8: Cs_trip/Cs/O
                            L8: Cs_trip/Cd/O
                            L8: Cs_trip/Ct/O
                            L8: Cs_trip/Cb/O
                        L7: Cs_tripOO
            L4: Cdjj
                L5: Cd_singletR
                    L6: Cd_singletC
                    L6: Cd_singletO
                L5: Cd_tripletR
                    L6: Cd_tripletC
                    L6: Cd_tripletO
        L3: Cjjj
            L4: C_doubletR
            L4: C_quartetR
        L3: Cjjjj
            L4: C_quintet
            L4: C_triplet
L1: XH_Rrad_birad
    L2: CH_R_rad
        L3: CH_s_R_rad
            L4: CsH_s_R_rad
                L5: C_methyl_R_rad
                    L6: C_methyl_Cj
                        L7: C_methyl_Csj
                        L7: C_methyl_Cdj
                    L6: C_methyl_Oj
                L5: CsRHH_R_rad
                    L6: CsH2_C_Cj
                        L7: CsH2_Cs_Csj
                        L7: CsH2_Cs_Cdj
                        L7: CsH2_Cd_Csj
                        L7: CsH2_Cd_Cdj
                        L7: CsH2_Ct_Csj
                        L7: CsH2_Ct_Cdj
                        L7: CsH2_Cb_Csj
                        L7: CsH2_Cb_Cdj
                    L6: CsH2_C_Oj
                        L7: CsH2_Cs_Oj
                        L7: CsH2_Cd_Oj
                        L7: CsH2_Ct_Oj
                        L7: CsH2_Cb_Oj
                    L6: CsH2_O_Cj
                        L7: CsH2_O_Csj
                        L7: CsH2_O_Cdj
                    L6: CsH2_O_Oj
                L5: CsRRH_R_rad
                    L6: CsH_CC_Cj
                        L7: CsH_CsCs_Csj
                        L7: CsH_CsCd_Csj
                        L7: CsH_CsCt_Csj
                        L7: CsH_CsCb_Csj
                        L7: CsH_CdCd_Csj
                        L7: CsH_CdCt_Csj
                        L7: CsH_CdCb_Csj
                        L7: CsH_CtCt_Csj
                        L7: CsH_CtCb_Csj
                        L7: CsH_CbCb_Csj
                        L7: CsH_CsCs_Cdj
                        L7: CsH_CsCd_Cdj
                        L7: CsH_CsCt_Cdj
                        L7: CsH_CsCb_Cdj
                        L7: CsH_CdCd_Cdj
                        L7: CsH_CdCt_Cdj
                        L7: CsH_CdCb_Cdj
                        L7: CsH_CtCt_Cdj
                        L7: CsH_CtCb_Cdj
                        L7: CsH_CbCb_Cdj
                    L6: CsH_CO_Cj
                        L7: CsH_CsO_Csj
                        L7: CsH_CdO_Csj
                        L7: CsH_CtO_Csj
                        L7: CsH_CbO_Csj
                        L7: CsH_CsO_Cdj
                        L7: CsH_CdO_Cdj
                        L7: CsH_CtO_Cdj
                        L7: CsH_CbO_Cdj
                    L6: CsH_OO_Cj
                        L7: CsH_OO_Csj
                        L7: CsH_OO_Cdj
                    L6: CsH_CC_Oj
                        L7: CsH_CsCs_Oj
                        L7: CsH_CsCd_Oj
                        L7: CsH_CsCt_Oj
                        L7: CsH_CsCb_Oj
                        L7: CsH_CdCd_Oj
                        L7: CsH_CdCt_Oj
                        L7: CsH_CdCb_Oj
                        L7: CsH_CtCt_Oj
                        L7: CsH_CtCb_Oj
                        L7: CsH_CbCb_Oj
                    L6: CsH_CO_Oj
                        L7: CsH_CsO_Oj
                        L7: CsH_CdO_Oj
                        L7: CsH_CtO_Oj
                        L7: CsH_CbO_Oj
                    L6: CsH_OO_Oj
            L4: CdH_s_R_rad
                L5: CdH_C_Cj
                    L6: CdH_Cds_Csj
                    L6: CdH_Cds_Cdj
                    L6: CdH_Cdd_Csj
                    L6: CdH_Cdd_Cdj
                L5: CdH_O_Cj
                    L6: CdH_Od_Csj
                    L6: CdH_Od_Cdj
                L5: CdH_C_Oj
                    L6: CdH_Cds_Oj
                    L6: CdH_Cdd_Oj
                L5: CdH_O_Oj
        L3: CH_d_R_rad
            L4: CdH2_R_rad
                L5: CdH2_Cdj
            L4: CdRH_R_rad
                L5: CdH_C_Cdj
                    L6: CdH_Cs_Cdj
                    L6: CdH_Cd_Cdj
                    L6: CdH_Ct_Cdj
                    L6: CdH_Cb_Cdj
                L5: CdH_O_Cdj
    L2: OH_R_rad
"""
)

