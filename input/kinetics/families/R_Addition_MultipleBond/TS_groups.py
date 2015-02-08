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
        distances = {'d12': 1.31439, 'd13': 2.18237, 'd23': 2.85721},
        uncertainties = {'d12': 0.118039, 'd13': 0.189303, 'd23': 0.267603},
    ),
    shortDesc = u"""Fitted to 64 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=19 label="Cds_Rd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=33 label="CO2">, <Entry index=5 label="Hj">]
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=22 label="Csj_HHH">]
[<Entry index=21 label="Ct_Ct">, <Entry index=22 label="Csj_HHH">]
[<Entry index=33 label="CO2">, <Entry index=46 label="Cdj_CdC">]
[<Entry index=32 label="Cdd_CdOd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=6 label="Cj">]
[<Entry index=30 label="Cds_Od">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct">, <Entry index=38 label="Csj_CCH">]
[<Entry index=10 label="Od_C">, <Entry index=36 label="Csj_CHH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=41 label="Csj_CCC">]
[<Entry index=30 label="Cds_Od">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=36 label="Csj_CHH">]
[<Entry index=10 label="Od_C">, <Entry index=5 label="Hj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=5 label="Hj">]
[<Entry index=51 label="Cds_CdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=6 label="Cj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=37 label="Csj_OHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=45 label="Cdj_CdH">]
[<Entry index=10 label="Od_C">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=36 label="Csj_CHH">]
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
    group = "OR{Cd_Rd, Ct_Rt}",
    distances = DistanceData(
        distances = {'d12': 0.004535, 'd13': 0.027608, 'd23': 0.011318},
        uncertainties = {'d12': 0.123375, 'd13': 0.198104, 'd23': 0.279066},
    ),
    shortDesc = u"""Fitted to 58 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=19 label="Cds_Rd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=33 label="CO2">, <Entry index=5 label="Hj">]
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=22 label="Csj_HHH">]
[<Entry index=21 label="Ct_Ct">, <Entry index=22 label="Csj_HHH">]
[<Entry index=33 label="CO2">, <Entry index=46 label="Cdj_CdC">]
[<Entry index=32 label="Cdd_CdOd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=6 label="Cj">]
[<Entry index=30 label="Cds_Od">, <Entry index=5 label="Hj">]
[<Entry index=21 label="Ct_Ct">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=41 label="Csj_CCC">]
[<Entry index=30 label="Cds_Od">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=36 label="Csj_CHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=5 label="Hj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=6 label="Cj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=37 label="Csj_OHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=45 label="Cdj_CdH">]
[<Entry index=51 label="Cds_CdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=36 label="Csj_CHH">]
""",
)

entry(
    index = 8,
    label = "Cd_Rd",
    group = 
"""
1 *1 C u0 {2,D}
2 *2 R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.00986, 'd13': 0.022287, 'd23': 0.001023},
        uncertainties = {'d12': 0.126618, 'd13': 0.20241, 'd23': 0.285543},
    ),
    shortDesc = u"""Fitted to 55 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=37 label="Csj_OHH">]
[<Entry index=32 label="Cdd_CdOd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=19 label="Cds_Rd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
[<Entry index=33 label="CO2">, <Entry index=46 label="Cdj_CdC">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=33 label="CO2">, <Entry index=5 label="Hj">]
[<Entry index=30 label="Cds_Od">, <Entry index=45 label="Cdj_CdH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=6 label="Cj">]
[<Entry index=30 label="Cds_Od">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=36 label="Csj_CHH">]
[<Entry index=51 label="Cds_CdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=6 label="Cj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=36 label="Csj_CHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=5 label="Hj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=5 label="Hj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=41 label="Csj_CCC">]
[<Entry index=30 label="Cds_Od">, <Entry index=22 label="Csj_HHH">]
""",
)

entry(
    index = 19,
    label = "Cds_Rd",
    group = 
"""
1 *1 C u0 {2,D} {3,S}
2 *2 R ux {1,D}
3    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.012143, 'd13': 0.032478, 'd23': 0.011612},
        uncertainties = {'d12': 0.129523, 'd13': 0.199907, 'd23': 0.28649},
    ),
    shortDesc = u"""Fitted to 52 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=37 label="Csj_OHH">]
[<Entry index=19 label="Cds_Rd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=41 label="Csj_CCC">]
[<Entry index=30 label="Cds_Od">, <Entry index=45 label="Cdj_CdH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=6 label="Cj">]
[<Entry index=30 label="Cds_Od">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=36 label="Csj_CHH">]
[<Entry index=51 label="Cds_CdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=6 label="Cj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=36 label="Csj_CHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=5 label="Hj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=5 label="Hj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=22 label="Csj_HHH">]
""",
)

entry(
    index = 29,
    label = "Cds_Cd",
    group = 
"""
1 *1 C u0 {2,D} {3,S}
2 *2 C ux {1,D}
3    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.045372, 'd13': 0.078077, 'd23': 0.12565},
        uncertainties = {'d12': 0.039025, 'd13': 0.1785, 'd23': 0.20357},
    ),
    shortDesc = u"""Fitted to 29 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=51 label="Cds_CdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=6 label="Cj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=41 label="Csj_CCC">]
[<Entry index=29 label="Cds_Cd">, <Entry index=37 label="Csj_OHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=5 label="Hj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=36 label="Csj_CHH">]
""",
)

entry(
    index = 51,
    label = "Cds_CdCC",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 C ux {1,D}
3    C ux {1,S}
4    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.047152, 'd13': 0.093177, 'd23': 0.002233},
        uncertainties = {'d12': 0.209106, 'd13': 0.716538, 'd23': 0.398779},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=51 label="Cds_CdCC">, <Entry index=22 label="Csj_HHH">]
""",
)

entry(
    index = 52,
    label = "Cds_CdCO",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 C ux {1,D}
3    C ux {1,S}
4    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 53,
    label = "Cds_CdOO",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 C ux {1,D}
3    O ux {1,S}
4    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 60,
    label = "Cds_CdHH",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 C ux {1,D}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 61,
    label = "Cds_CdCH",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 C ux {1,D}
3    C ux {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 62,
    label = "Cds_CdOH",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 C ux {1,D}
3    O ux {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 30,
    label = "Cds_Od",
    group = 
"""
1 *1 C u0 {2,D} {3,S}
2 *2 O u0 {1,D}
3    R ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.064852, 'd13': -0.066859, 'd23': -0.200019},
        uncertainties = {'d12': 0.063591, 'd13': 0.109537, 'd23': 0.190624},
    ),
    shortDesc = u"""Fitted to 21 distances.
""",
    longDesc = 
u"""
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=36 label="Csj_CHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=6 label="Cj">]
[<Entry index=30 label="Cds_Od">, <Entry index=45 label="Cdj_CdH">]
[<Entry index=30 label="Cds_Od">, <Entry index=5 label="Hj">]
[<Entry index=30 label="Cds_Od">, <Entry index=22 label="Csj_HHH">]
""",
)

entry(
    index = 54,
    label = "Cds_OdCC",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 O u0 {1,D}
3    C ux {1,S}
4    C ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.05955, 'd13': -0.102707, 'd23': -0.289212},
        uncertainties = {'d12': 0.124866, 'd13': 0.130473, 'd23': 0.230696},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=22 label="Csj_HHH">]
""",
)

entry(
    index = 55,
    label = "Cds_OdCO",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 O u0 {1,D}
3    C ux {1,S}
4    O ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.052594, 'd13': -0.219706, 'd23': -0.298054},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
""",
)

entry(
    index = 56,
    label = "Cds_OdOO",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 O u0 {1,D}
3    O ux {1,S}
4    O ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 57,
    label = "Cds_OdHH",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 O u0 {1,D}
3    H u0 {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 58,
    label = "Cds_OdCH",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 O u0 {1,D}
3    C ux {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 59,
    label = "Cds_OdOH",
    group = 
"""
1 *1 C u0 {2,D} {3,S} {4,S}
2 *2 O u0 {1,D}
3    O ux {1,S}
4    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 20,
    label = "Cdd_RdRd",
    group = 
"""
1 *1 C u0 {2,D} {3,D}
2 *2 R ux {1,D}
3    R ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.032195, 'd13': -0.165397, 'd23': -0.193999},
        uncertainties = {'d12': 0.169365, 'd13': 0.643385, 'd23': 0.724987},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=32 label="Cdd_CdOd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=33 label="CO2">, <Entry index=46 label="Cdj_CdC">]
[<Entry index=33 label="CO2">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 31,
    label = "Cdd_CdCd",
    group = 
"""
1 *1 C u0 {2,D} {3,D}
2 *2 C ux {1,D}
3    C ux {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 32,
    label = "Cdd_CdOd",
    group = 
"""
1 *1 C u0 {2,D} {3,D}
2 *2 C ux {1,D}
3    O u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': 0.023716, 'd13': 0.004884, 'd23': -0.001034},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=32 label="Cdd_CdOd">, <Entry index=38 label="Csj_CCH">]
""",
)

entry(
    index = 33,
    label = "CO2",
    group = 
"""
1 *1 C u0 {2,D} {3,D}
2 *2 O u0 {1,D}
3    O u0 {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.072132, 'd13': -0.287027, 'd23': -0.331831},
        uncertainties = {'d12': 0.692527, 'd13': 2.62646, 'd23': 2.94644},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=33 label="CO2">, <Entry index=46 label="Cdj_CdC">]
[<Entry index=33 label="CO2">, <Entry index=5 label="Hj">]
""",
)

entry(
    index = 9,
    label = "Ct_Rt",
    group = 
"""
1 *1 C u0 {2,T}
2 *2 R ux {1,T}
""",
    distances = DistanceData(
        distances = {'d12': -0.090894, 'd13': 0.122977, 'd23': 0.195836},
        uncertainties = {'d12': 0.095773, 'd13': 0.262884, 'd23': 0.328443},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct">, <Entry index=22 label="Csj_HHH">]
[<Entry index=21 label="Ct_Ct">, <Entry index=38 label="Csj_CCH">]
""",
)

entry(
    index = 21,
    label = "Ct_Ct",
    group = 
"""
1 *1 C u0 {2,T}
2 *2 C ux {1,T}
""",
    distances = DistanceData(
        distances = {'d12': -0.090894, 'd13': 0.122977, 'd23': 0.195836},
        uncertainties = {'d12': 0.095773, 'd13': 0.262884, 'd23': 0.328443},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct">, <Entry index=22 label="Csj_HHH">]
[<Entry index=21 label="Ct_Ct">, <Entry index=38 label="Csj_CCH">]
""",
)

entry(
    index = 63,
    label = "Ct_Ct_H",
    group = 
"""
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 34,
    label = "Ct_Ct_C",
    group = 
"""
1 *1 C u0 {2,T} {3,S}
2 *2 C ux {1,T}
3    C ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 35,
    label = "Ct_Ct_O",
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
        distances = {'d12': -0.05313, 'd13': -0.32341, 'd23': -0.132582},
        uncertainties = {'d12': 0.067416, 'd13': 0.099419, 'd23': 0.173322},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=10 label="Od_C">, <Entry index=36 label="Csj_CHH">]
[<Entry index=10 label="Od_C">, <Entry index=22 label="Csj_HHH">]
[<Entry index=10 label="Od_C">, <Entry index=5 label="Hj">]
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
        distances = {'d12': -0.05313, 'd13': -0.32341, 'd23': -0.132582},
        uncertainties = {'d12': 0.067416, 'd13': 0.099419, 'd23': 0.173322},
    ),
    shortDesc = u"""Fitted to 6 distances.
""",
    longDesc = 
u"""
[<Entry index=10 label="Od_C">, <Entry index=36 label="Csj_CHH">]
[<Entry index=10 label="Od_C">, <Entry index=22 label="Csj_HHH">]
[<Entry index=10 label="Od_C">, <Entry index=5 label="Hj">]
""",
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
        distances = {'d12': -0.060111, 'd13': -0.309176, 'd23': -0.356792},
        uncertainties = {'d12': 0.097883, 'd13': 0.35237, 'd23': 0.404183},
    ),
    shortDesc = u"""Fitted to 7 distances.
""",
    longDesc = 
u"""
[<Entry index=30 label="Cds_Od">, <Entry index=5 label="Hj">]
[<Entry index=10 label="Od_C">, <Entry index=5 label="Hj">]
[<Entry index=33 label="CO2">, <Entry index=5 label="Hj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=5 label="Hj">]
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
        distances = {'d12': 0.006703, 'd13': 0.034476, 'd23': 0.039786},
        uncertainties = {'d12': 0.122734, 'd13': 0.177754, 'd23': 0.26311},
    ),
    shortDesc = u"""Fitted to 57 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=19 label="Cds_Rd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=22 label="Csj_HHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=45 label="Cdj_CdH">]
[<Entry index=21 label="Ct_Ct">, <Entry index=22 label="Csj_HHH">]
[<Entry index=33 label="CO2">, <Entry index=46 label="Cdj_CdC">]
[<Entry index=30 label="Cds_Od">, <Entry index=6 label="Cj">]
[<Entry index=21 label="Ct_Ct">, <Entry index=38 label="Csj_CCH">]
[<Entry index=10 label="Od_C">, <Entry index=36 label="Csj_CHH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=41 label="Csj_CCC">]
[<Entry index=30 label="Cds_Od">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=36 label="Csj_CHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=6 label="Cj">]
[<Entry index=29 label="Cds_Cd">, <Entry index=37 label="Csj_OHH">]
[<Entry index=32 label="Cdd_CdOd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=51 label="Cds_CdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=10 label="Od_C">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=36 label="Csj_CHH">]
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
        distances = {'d12': 0.011868, 'd13': 0.044056, 'd23': 0.055332},
        uncertainties = {'d12': 0.127224, 'd13': 0.165805, 'd23': 0.252202},
    ),
    shortDesc = u"""Fitted to 51 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=21 label="Ct_Ct">, <Entry index=22 label="Csj_HHH">]
[<Entry index=19 label="Cds_Rd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=37 label="Csj_OHH">]
[<Entry index=10 label="Od_C">, <Entry index=36 label="Csj_CHH">]
[<Entry index=21 label="Ct_Ct">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=41 label="Csj_CCC">]
[<Entry index=32 label="Cdd_CdOd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=36 label="Csj_CHH">]
[<Entry index=51 label="Cds_CdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=38 label="Csj_CCH">]
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=36 label="Csj_CHH">]
[<Entry index=10 label="Od_C">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=22 label="Csj_HHH">]
""",
)

entry(
    index = 22,
    label = "Csj_HHH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    H  u0 {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.021662, 'd13': 0.079032, 'd23': 0.051923},
        uncertainties = {'d12': 0.193675, 'd13': 0.225069, 'd23': 0.358113},
    ),
    shortDesc = u"""Fitted to 23 distances.
""",
    longDesc = 
u"""
[<Entry index=21 label="Ct_Ct">, <Entry index=22 label="Csj_HHH">]
[<Entry index=19 label="Cds_Rd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=51 label="Cds_CdCC">, <Entry index=22 label="Csj_HHH">]
[<Entry index=10 label="Od_C">, <Entry index=22 label="Csj_HHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=22 label="Csj_HHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=22 label="Csj_HHH">]
""",
)

entry(
    index = 23,
    label = "Csj_RHH",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    H   u0 {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.005548, 'd13': 0.04339, 'd23': 0.09144},
        uncertainties = {'d12': 0.025221, 'd13': 0.126731, 'd23': 0.12757},
    ),
    shortDesc = u"""Fitted to 17 distances.
""",
    longDesc = 
u"""
[<Entry index=10 label="Od_C">, <Entry index=36 label="Csj_CHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=36 label="Csj_CHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=37 label="Csj_OHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=36 label="Csj_CHH">]
""",
)

entry(
    index = 36,
    label = "Csj_CHH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.0036, 'd13': 0.040599, 'd23': 0.087576},
        uncertainties = {'d12': 0.019876, 'd13': 0.129144, 'd23': 0.121545},
    ),
    shortDesc = u"""Fitted to 16 distances.
""",
    longDesc = 
u"""
[<Entry index=10 label="Od_C">, <Entry index=36 label="Csj_CHH">]
[<Entry index=30 label="Cds_Od">, <Entry index=36 label="Csj_CHH">]
[<Entry index=29 label="Cds_Cd">, <Entry index=36 label="Csj_CHH">]
""",
)

entry(
    index = 37,
    label = "Csj_OHH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    O  ux {1,S}
3    H  u0 {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.035932, 'd13': 0.086938, 'd23': 0.15172},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=37 label="Csj_OHH">]
""",
)

entry(
    index = 24,
    label = "Csj_RRH",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    H   u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.012689, 'd13': -0.04821, 'd23': -0.059731},
        uncertainties = {'d12': 0.053298, 'd13': 0.11981, 'd23': 0.192499},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=32 label="Cdd_CdOd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=21 label="Ct_Ct">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=38 label="Csj_CCH">]
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
""",
)

entry(
    index = 38,
    label = "Csj_CCH",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    H  u0 {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.012689, 'd13': -0.04821, 'd23': -0.059731},
        uncertainties = {'d12': 0.053298, 'd13': 0.11981, 'd23': 0.192499},
    ),
    shortDesc = u"""Fitted to 8 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=32 label="Cdd_CdOd">, <Entry index=38 label="Csj_CCH">]
[<Entry index=54 label="Cds_OdCC">, <Entry index=38 label="Csj_CCH">]
[<Entry index=21 label="Ct_Ct">, <Entry index=38 label="Csj_CCH">]
[<Entry index=30 label="Cds_Od">, <Entry index=38 label="Csj_CCH">]
[<Entry index=55 label="Cds_OdCO">, <Entry index=38 label="Csj_CCH">]
""",
)

entry(
    index = 39,
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
    index = 40,
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
    index = 25,
    label = "Csj_RRR",
    group = 
"""
1 *3 Cs  u1 {2,S} {3,S} {4,S}
2    R!H ux {1,S}
3    R!H ux {1,S}
4    R!H ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.042796, 'd13': 0.045779, 'd23': 0.194816},
        uncertainties = {'d12': 0.164172, 'd13': 0.244366, 'd23': 0.509012},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=41 label="Csj_CCC">]
""",
)

entry(
    index = 41,
    label = "Csj_CCC",
    group = 
"""
1 *3 Cs u1 {2,S} {3,S} {4,S}
2    C  ux {1,S}
3    C  ux {1,S}
4    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': 0.042796, 'd13': 0.045779, 'd23': 0.194816},
        uncertainties = {'d12': 0.164172, 'd13': 0.244366, 'd23': 0.509012},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=29 label="Cds_Cd">, <Entry index=41 label="Csj_CCC">]
""",
)

entry(
    index = 42,
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
    index = 43,
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
    index = 44,
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
        distances = {'d12': -0.07943, 'd13': -0.013781, 'd23': -0.093715},
        uncertainties = {'d12': 0.296842, 'd13': 0.719409, 'd23': 1.04991},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=30 label="Cds_Od">, <Entry index=45 label="Cdj_CdH">]
[<Entry index=33 label="CO2">, <Entry index=46 label="Cdj_CdC">]
""",
)

entry(
    index = 26,
    label = "Cdj_Cd",
    group = 
"""
1 *3 Cd u1 {2,D}
2    C  ux {1,D}
""",
    distances = DistanceData(
        distances = {'d12': -0.07943, 'd13': -0.013781, 'd23': -0.093715},
        uncertainties = {'d12': 0.296842, 'd13': 0.719409, 'd23': 1.04991},
    ),
    shortDesc = u"""Fitted to 3 distances.
""",
    longDesc = 
u"""
[<Entry index=30 label="Cds_Od">, <Entry index=45 label="Cdj_CdH">]
[<Entry index=33 label="CO2">, <Entry index=46 label="Cdj_CdC">]
""",
)

entry(
    index = 45,
    label = "Cdj_CdH",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    H  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.07224, 'd13': 0.071083, 'd23': -0.032421},
        uncertainties = {'d12': 1.03128, 'd13': 1.46324, 'd23': 3.27867},
    ),
    shortDesc = u"""Fitted to 2 distances.
""",
    longDesc = 
u"""
[<Entry index=30 label="Cds_Od">, <Entry index=45 label="Cdj_CdH">]
""",
)

entry(
    index = 46,
    label = "Cdj_CdC",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    C  ux {1,S}
""",
    distances = DistanceData(
        distances = {'d12': -0.093808, 'd13': -0.183508, 'd23': -0.216304},
        uncertainties = {},
    ),
    shortDesc = u"""Fitted to 1 distances.
""",
    longDesc = 
u"""
[<Entry index=33 label="CO2">, <Entry index=46 label="Cdj_CdC">]
""",
)

entry(
    index = 47,
    label = "Cdj_CdO",
    group = 
"""
1 *3 Cd u1 {2,D} {3,S}
2    C  ux {1,D}
3    O  ux {1,S}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 27,
    label = "Cdj_Od",
    group = 
"""
1 *3 Cd u1 {2,D}
2    O  u0 {1,D}
""",
    distances = DistanceData(distances={}),
)

entry(
    index = 48,
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
    index = 49,
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
    index = 50,
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
    index = 28,
    label = "Ctj_Ct",
    group = 
"""
1 *3 Ct u1 {2,T}
2    Ct ux {1,T}
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
    distances = DistanceData(distances={}),
)

entry(
    index = 16,
    label = "OH",
    group = 
"""
1 *3 O u1 {2,S}
2    H u0 {1,S}
""",
    distances = DistanceData(distances={}),
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
        L3: Cd_Rd
            L4: Cds_Rd
                L5: Cds_Cd
                    L6: Cds_CdHH
                    L6: Cds_CdCH
                    L6: Cds_CdOH
                    L6: Cds_CdCC
                    L6: Cds_CdCO
                    L6: Cds_CdOO
                L5: Cds_Od
                    L6: Cds_OdHH
                    L6: Cds_OdCH
                    L6: Cds_OdOH
                    L6: Cds_OdCC
                    L6: Cds_OdCO
                    L6: Cds_OdOO
            L4: Cdd_RdRd
                L5: Cdd_CdCd
                L5: Cdd_CdOd
                L5: CO2
        L3: Ct_Rt
            L4: Ct_Ct
                L5: Ct_Ct_H
                L5: Ct_Ct_C
                L5: Ct_Ct_O
    L2: Od_R
        L3: Od_C
        L3: O2
L1: YJ
    L2: Hj
    L2: Cj
        L3: Csj
            L4: Csj_HHH
            L4: Csj_RHH
                L5: Csj_CHH
                L5: Csj_OHH
            L4: Csj_RRH
                L5: Csj_CCH
                L5: Csj_COH
                L5: Csj_OOH
            L4: Csj_RRR
                L5: Csj_CCC
                L5: Csj_CCO
                L5: Csj_COO
                L5: Csj_OOO
        L3: Cdj
            L4: Cdj_Cd
                L5: Cdj_CdH
                L5: Cdj_CdC
                L5: Cdj_CdO
            L4: Cdj_Od
                L5: Cdj_OdH
                L5: Cdj_OdC
                L5: Cdj_OdO
        L3: Ctj
            L4: Ctj_Ct
        L3: Cbj
    L2: Oj
        L3: OH
        L3: OjC
        L3: OjO
"""
)

