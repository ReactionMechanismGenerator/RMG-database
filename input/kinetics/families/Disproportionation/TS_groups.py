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
        distances = {'d12': 1.40546, 'd13': 2.53451, 'd23': 1.13618},
        uncertainties = {'d12': 0.104768, 'd13': 0.170269, 'd23': 0.112853},
    ),
    shortDesc = u"""Fitted to 5 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 2,
    label = "XH_Rrad_birad",
    group = 
"""
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
1 *1 H u1
""",
    distances = DistanceData(
        distances = {'d12': -0.122181, 'd13': -0.238335, 'd23': -0.121874},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
""",
)

entry(
    index = 4,
    label = "Orad",
    group = 
"""
1 *1 O u[1,2]
""",
    distances = DistanceData(
        distances = {'d12': 0.130001, 'd13': 0.052048, 'd23': -0.074333},
        uncertainties = {'d12': 0.445272, 'd13': 0.262463, 'd23': 0.465853},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 8,
    label = "OjR",
    group = 
"""
1 *1 O u1 {2,S}
2    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.130001, 'd13': 0.052048, 'd23': -0.074333},
        uncertainties = {'d12': 0.445272, 'd13': 0.262463, 'd23': 0.465853},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 16,
    label = "OjH",
    group = 
"""
1 *1 O u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 17,
    label = "OjC",
    group = 
"""
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
1 *1 O u1 {2,S}
2    O ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.130001, 'd13': 0.052048, 'd23': -0.074333},
        uncertainties = {'d12': 0.445272, 'd13': 0.262463, 'd23': 0.465853},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 9,
    label = "O_atom_triplet",
    group = 
"""
1 *1 O u2
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 5,
    label = "Crad",
    group = 
"""
1 *1 C u[1,2,3,4]
""",
    distances = DistanceData(
        distances = {'d12': -0.12077, 'd13': 0.077926, 'd23': 0.196878},
        uncertainties = {'d12': 0.344591, 'd13': 0.259189, 'd23': 0.50041},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 10,
    label = "Cj",
    group = 
"""
1 *1 C u1
""",
    distances = DistanceData(
        distances = {'d12': -0.12077, 'd13': 0.077926, 'd23': 0.196878},
        uncertainties = {'d12': 0.344591, 'd13': 0.259189, 'd23': 0.50041},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 19,
    label = "Csj",
    group = 
"""
1 *1 Cs u1
""",
    distances = DistanceData(
        distances = {'d12': -0.12077, 'd13': 0.077926, 'd23': 0.196878},
        uncertainties = {'d12': 0.344591, 'd13': 0.259189, 'd23': 0.50041},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 37,
    label = "Cs_methyl",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.12077, 'd13': 0.077926, 'd23': 0.196878},
        uncertainties = {'d12': 0.344591, 'd13': 0.259189, 'd23': 0.50041},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 38,
    label = "CsjRH2",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    R  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 58,
    label = "CsjCH2",
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
    index = 107,
    label = "Csj/Cs/H2",
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
    index = 108,
    label = "Csj/Cd/H2",
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
    index = 109,
    label = "Csj/Ct/H2",
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
    index = 110,
    label = "Csj/Cb/H2",
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
    index = 59,
    label = "CsjOH2",
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
    index = 39,
    label = "CsjRRH",
    group = 
"""
1 *1 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    R  ux {1,S}
4    R  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 60,
    label = "CsjCCH",
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
    index = 111,
    label = "Csj/Cs/Cs/H",
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
    index = 112,
    label = "Csj/Cs/Cd/H",
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
    index = 113,
    label = "Csj/Cs/Ct/H",
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
    index = 114,
    label = "Csj/Cs/Cb/H",
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
    index = 115,
    label = "Csj/Cd/Cd/H",
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
    index = 116,
    label = "Csj/Cd/Ct/H",
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
    index = 117,
    label = "Csj/Cd/Cb/H",
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
    index = 118,
    label = "Csj/Ct/Ct/H",
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
    index = 119,
    label = "Csj/Ct/Cb/H",
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
    index = 120,
    label = "Csj/Cb/Cb/H",
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
    index = 61,
    label = "CsjCOH",
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
    index = 121,
    label = "Csj/Cs/O/H",
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
    index = 122,
    label = "Csj/Cd/O/H",
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
    index = 123,
    label = "Csj/Ct/O/H",
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
    index = 124,
    label = "Csj/Cb/O/H",
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
    index = 62,
    label = "CsjOOH",
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
    index = 40,
    label = "CsjRRR",
    group = 
"""
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
1 *1 Cd u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 41,
    label = "Cdj_CR",
    group = 
"""
1 *1 Cd u1 {2,D}
2    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 67,
    label = "Cdj_CH",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 159,
    label = "Cdj_CdsH",
    group = 
"""
1 *1 Cd u1 {2,D} {3,S}
2    Cd ux {1,D}
3    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 160,
    label = "Cdj_CddH",
    group = 
"""
1 *1 Cd  u1 {2,D} {3,S}
2    Cdd u0 {1,D}
3    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 68,
    label = "Cdj_CC",
    group = 
"""
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
1 *1 Ct u1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 43,
    label = "CtjC",
    group = 
"""
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
1 *1 Cs u0 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 73,
    label = "Cs_singH2",
    group = 
"""
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
1 *1 Cs u2 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 76,
    label = "Cs_tripH2",
    group = 
"""
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
1 *1 Cd u0 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 79,
    label = "Cd_singletC",
    group = 
"""
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
1 *1 Cd u2 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 81,
    label = "Cd_tripletC",
    group = 
"""
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
1 *1 C u1 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 26,
    label = "C_quartetR",
    group = 
"""
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
1 *1 C u4 p0
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 28,
    label = "C_triplet",
    group = 
"""
1 *1 C u2 p1
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 6,
    label = "CH_R_rad",
    group = 
"""
1 *2 C   u0 {2,[S,D]} {3,S}
2 *3 R!H u1 {1,[S,D]}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.021683, 'd13': 0.034894, 'd23': 0.012985},
        uncertainties = {'d12': 0.131373, 'd13': 0.223534, 'd23': 0.130676},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 14,
    label = "CH_s_R_rad",
    group = 
"""
1 *2 C   u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.021683, 'd13': 0.034894, 'd23': 0.012985},
        uncertainties = {'d12': 0.131373, 'd13': 0.223534, 'd23': 0.130676},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 29,
    label = "CsH_s_R_rad",
    group = 
"""
1 *2 Cs  u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.021683, 'd13': 0.034894, 'd23': 0.012985},
        uncertainties = {'d12': 0.131373, 'd13': 0.223534, 'd23': 0.130676},
    ),
    shortDesc = u"""Fitted to 4 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 48,
    label = "C_methyl_R_rad",
    group = 
"""
1 *2 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
4    H   u0 {1,S}
5    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.020682, 'd13': 0.040302, 'd23': 0.016086},
        uncertainties = {'d12': 0.193761, 'd13': 0.368015, 'd23': 0.208862},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 83,
    label = "C_methyl_Cj",
    group = 
"""
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.037758, 'd13': 0.074593, 'd23': 0.033465},
        uncertainties = {'d12': 0.228662, 'd13': 0.263657, 'd23': 0.401699},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 185,
    label = "C_methyl_Csj",
    group = 
"""
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.037758, 'd13': 0.074593, 'd23': 0.033465},
        uncertainties = {'d12': 0.228662, 'd13': 0.263657, 'd23': 0.401699},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=185 label="C_methyl_Csj">]
[<Entry index=18 label="OjO">, <Entry index=185 label="C_methyl_Csj">]
""",
)

entry(
    index = 186,
    label = "C_methyl_Cdj",
    group = 
"""
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cd u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 84,
    label = "C_methyl_Oj",
    group = 
"""
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    H u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.056163, 'd13': -0.114004, 'd23': -0.062116},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=3 label="Hrad">, <Entry index=84 label="C_methyl_Oj">]
""",
)

entry(
    index = 49,
    label = "CsRHH_R_rad",
    group = 
"""
1 *2 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
4    H   u0 {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.024435, 'd13': 0.020022, 'd23': 0.004456},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=18 label="OjO">, <Entry index=187 label="CsH2_Cs_Csj">]
""",
)

entry(
    index = 85,
    label = "CsH2_C_Cj",
    group = 
"""
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.024435, 'd13': 0.020022, 'd23': 0.004456},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
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
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cs ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.024435, 'd13': 0.020022, 'd23': 0.004456},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
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
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O u1 {1,S}
3 *4 H u0 {1,S}
4    H u0 {1,S}
5    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 195,
    label = "CsH2_Cs_Oj",
    group = 
"""
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
5    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 196,
    label = "CsH2_Cd_Oj",
    group = 
"""
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
1 *2 C   u0 {2,S} {3,S} {4,S} {5,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
4    R!H ux {1,S}
5    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 89,
    label = "CsH_CC_Cj",
    group = 
"""
1 *2 C u0 {2,S} {3,S} {4,S} {5,S}
2 *3 C u1 {1,S}
3 *4 H u0 {1,S}
4    C ux {1,S}
5    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 201,
    label = "CsH_CsCs_Csj",
    group = 
"""
1 *2 C  u0 {2,S} {3,S} {4,S} {5,S}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
5    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 202,
    label = "CsH_CsCd_Csj",
    group = 
"""
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
1 *2 Cd  u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 51,
    label = "CdH_C_Cj",
    group = 
"""
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 C  u1 {1,S}
3 *4 H  u0 {1,S}
4    C  ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 95,
    label = "CdH_Cds_Csj",
    group = 
"""
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 Cs u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 96,
    label = "CdH_Cds_Cdj",
    group = 
"""
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
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    C  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 101,
    label = "CdH_Cds_Oj",
    group = 
"""
1 *2 Cd u0 {2,S} {3,S} {4,D}
2 *3 O  u1 {1,S}
3 *4 H  u0 {1,S}
4    Cd u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 102,
    label = "CdH_Cdd_Oj",
    group = 
"""
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
1 *2 C   u0 {2,D} {3,S}
2 *3 R!H u1 {1,D}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 31,
    label = "CdH2_R_rad",
    group = 
"""
1 *2 C   u0 {2,D} {3,S} {4,S}
2 *3 R!H u1 {1,D}
3 *4 H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 55,
    label = "CdH2_Cdj",
    group = 
"""
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 32,
    label = "CdRH_R_rad",
    group = 
"""
1 *2 C   u0 {2,D} {3,S} {4,S}
2 *3 R!H u1 {1,D}
3 *4 H   u0 {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 56,
    label = "CdH_C_Cdj",
    group = 
"""
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 103,
    label = "CdH_Cs_Cdj",
    group = 
"""
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    Cs ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 104,
    label = "CdH_Cd_Cdj",
    group = 
"""
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    Cd ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 105,
    label = "CdH_Ct_Cdj",
    group = 
"""
1 *2 C  u0 {2,D} {3,S} {4,S}
2 *3 Cd u1 {1,D}
3 *4 H  u0 {1,S}
4    Ct u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 106,
    label = "CdH_Cb_Cdj",
    group = 
"""
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
1 *2 O   u0 {2,S} {3,S}
2 *3 R!H u1 {1,S}
3 *4 H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.065048, 'd13': -0.104683, 'd23': -0.038955},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=37 label="Cs_methyl">, <Entry index=7 label="OH_R_rad">]
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

