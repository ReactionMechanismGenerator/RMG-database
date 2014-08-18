#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 809,
    label = "Rn;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (100000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 812,
    label = "R5_SD_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (102676000000.0, 's^-1'),
        n = 0.55665,
        alpha = 0,
        E0 = (37.5409, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 813,
    label = "R3_D;doublebond_intra_pri_HDe;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (105000000.0, 's^-1'),
        n = 1.192,
        alpha = 0,
        E0 = (54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 5,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 814,
    label = "R3_T;triplebond_intra_H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (105000000.0, 's^-1'),
        n = 1.192,
        alpha = 0,
        E0 = (54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 5,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 900,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (306000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 901,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2210000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 902,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (565000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 903,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2590000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 904,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (733000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 905,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1290000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 906,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1160000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 907,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (41500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 908,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1910000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 909,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (13800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 910,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3540000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 911,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (16200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 912,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4580000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 913,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (8060000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 914,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (7250000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 915,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (260000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (5.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 916,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (418000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 917,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3030000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 918,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (773000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 919,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3540000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 920,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 921,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1760000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 922,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1580000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 923,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (56800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 924,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (544000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 925,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3940000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 926,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1010000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 927,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 928,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 929,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2290000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 930,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2060000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 931,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (73900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (2.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 932,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (406000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 933,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2940000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 934,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (750000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 935,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3430000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 936,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (972000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 937,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1710000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 938,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1540000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 939,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (55100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 940,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (544000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 941,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3940000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 942,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1010000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 943,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 944,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 945,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2290000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 946,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2060000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 947,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (73900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (2.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 948,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (40200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (1.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 949,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (291000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (1.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 950,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (74300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (0.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 951,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (340000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 952,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (96200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 953,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (169000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 954,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (152000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (5.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 955,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5460000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (-3.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 956,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (18300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 957,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (132000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 958,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (33700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 959,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (155000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 960,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (43700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 961,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (76900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 962,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (69200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 963,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2480000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 964,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (114000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 965,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (827000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 966,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (211000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 967,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (966000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 968,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (274000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 969,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (481000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 970,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (433000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 971,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (15500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 972,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (24900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 973,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (181000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 974,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (46100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 975,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (211000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (41.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 976,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (59800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (41.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 977,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (105000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 978,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (94600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 979,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3390000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 980,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (32400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 981,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (235000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 982,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (60000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 983,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (275000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 984,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (77800000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 985,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (137000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 986,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (123000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 987,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4410000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 988,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (24200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 989,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (175000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 990,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (44800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 991,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (205000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (42.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 992,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (58000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (43.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 993,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (102000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 994,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (91800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 995,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3290000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 996,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (32400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 997,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (235000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 998,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (60000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 999,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (275000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1000,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (77800000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1001,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (137000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1002,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (123000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1003,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4410000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1004,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1005,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (17400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1006,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4430000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1007,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (20300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1008,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5750000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1009,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (10100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1010,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1011,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (326000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1012,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (4860000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1013,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (35200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1014,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8980000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1015,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (41100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1016,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (11600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1017,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (20500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1018,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (18400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1019,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (660000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1020,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (30400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1021,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (220000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1022,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (56200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1023,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (257000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1024,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (72800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1025,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (128000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1026,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (115000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1027,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4130000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1028,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6640000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1029,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (48100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1030,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (12300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1031,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (56200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1032,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (15900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1033,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (28000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1034,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (25200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1035,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (902000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1036,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8640000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1037,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (62600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1038,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (16000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1039,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (73100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1040,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (20700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1041,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (36400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1042,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (32800000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1043,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1170000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1044,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6450000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1045,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (46700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1046,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (11900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1047,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (54600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1048,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (15400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1049,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (27200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1050,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (24500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1051,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (876000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1052,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8640000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1053,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (62600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1054,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (16000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1055,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (73100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1056,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (20700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1057,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (36400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1058,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (32800000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1059,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1170000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1060,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (638000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1061,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4620000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1062,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1180000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1063,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1064,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1530000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1065,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2690000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1066,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2420000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1067,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (86700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (3.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1068,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (13100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1069,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (94600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1070,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (24200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1071,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (111000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1072,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (31300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1073,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (55100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1074,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (49600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1075,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1780000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1076,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (81700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1077,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (592000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1078,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (151000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1079,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (692000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1080,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (196000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1081,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (344000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1082,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (310000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1083,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (11100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1084,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (17900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1085,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (129000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1086,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (33000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1087,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (151000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1088,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (42800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1089,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (75300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1090,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (67700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1091,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2430000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1092,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (23200000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1093,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (168000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1094,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (43000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1095,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (197000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1096,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (55700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1097,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (97900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1098,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (88100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1099,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3160000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1100,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (17300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1101,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (126000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1102,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (32100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1103,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (147000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1104,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (41500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1105,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (73100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1106,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (65800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1107,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2360000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1108,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (23200000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1109,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (168000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1110,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (43000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1111,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (197000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1112,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (55700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1113,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (97900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1114,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (88100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1115,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3160000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1116,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1720000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1117,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (12400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1118,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3170000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1119,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (14500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1120,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4110000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1121,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (7230000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1122,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6510000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1123,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (233000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1124,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (382000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1125,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2770000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1126,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (707000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1127,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3240000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1128,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (916000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1129,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1610000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1130,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1450000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1131,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (51900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1132,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2390000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1133,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (17300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1134,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4420000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1135,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (20200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1136,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5730000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1137,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (10100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1138,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9070000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1139,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (325000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1140,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (522000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1141,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3780000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1142,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (966000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1143,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4420000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1144,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1250000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1145,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1146,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1980000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1147,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (71000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1148,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (680000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1149,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4920000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1150,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1260000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1151,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5750000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1152,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1630000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1153,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2860000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1154,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2580000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1155,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (92400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (1.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1156,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (507000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1157,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3670000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1158,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (938000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1159,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4290000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1160,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1220000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1161,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2140000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1162,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1920000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1163,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (68900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1164,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (680000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1165,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4920000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1166,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1260000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1167,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5750000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1168,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1630000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1169,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2860000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1170,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2580000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1171,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (92300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (1.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1172,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (50200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (0.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1173,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (364000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (0.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1174,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (92900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1175,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (425000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1176,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (120000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1177,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (212000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1178,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (190000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (5.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1179,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (6820000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (-4.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1180,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (22800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1181,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (165000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1182,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (42200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1183,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (193000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1184,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (54700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1185,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (96200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1186,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (86600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1187,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1188,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (143000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1189,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1030000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1190,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (264000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1191,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1210000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1192,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (342000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1193,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (602000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1194,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (541000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1195,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (19400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1196,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (31200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1197,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (226000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1198,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (57700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1199,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (264000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1200,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (74700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (41.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1201,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (131000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1202,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (118000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1203,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4240000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1204,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (40600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1205,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (294000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1206,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (75000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1207,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (343000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1208,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (97200000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1209,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (171000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1210,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (154000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1211,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5510000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1212,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (30300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1213,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (219000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1214,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (56000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1215,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (256000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (42.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1216,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (72500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (42.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1217,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (128000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1218,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (115000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1219,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4110000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1220,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (40600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1221,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (294000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1222,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (75000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1223,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (343000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1224,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (97200000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1225,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (171000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1226,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (154000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1227,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5510000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1228,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1229,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (21700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1230,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5540000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1231,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (25400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1232,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7180000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1233,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (12600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1234,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (11400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1235,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (407000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1236,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6070000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1237,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (44000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1238,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (11200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1239,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (51400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1240,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (14600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1241,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (25600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1242,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (23000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1243,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (826000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1244,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (38000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1245,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (275000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1246,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (70300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1247,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (322000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1248,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (91000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1249,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (160000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1250,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (144000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1251,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5160000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1252,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1253,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (60100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1254,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (15400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1255,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (70300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1256,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (19900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1257,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (35000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1258,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (31500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1259,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1130000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1260,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (10800000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1261,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (78200000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1262,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (20000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1263,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (91400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1264,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (25900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1265,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (45500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1266,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (41000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1267,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1470000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1268,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8060000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1269,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (58400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1270,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (14900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1271,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (68200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1272,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (19300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1273,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (34000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1274,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (30600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1275,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1276,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (10800000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1277,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (78200000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1278,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (20000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1279,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (91400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1280,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (25900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1281,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (45500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1282,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (41000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1283,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1470000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1284,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (798000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1285,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (5780000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1286,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1480000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1287,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (6760000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1288,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1910000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1289,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3360000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1290,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3030000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1291,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (108000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (2.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1292,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (16300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1293,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (118000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1294,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (30200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1295,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (138000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1296,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (39100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1297,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (68900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1298,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (62000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1299,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2220000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1300,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (102000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1301,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (740000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1302,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (189000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1303,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (865000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1304,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (245000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1305,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (431000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1306,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (388000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1307,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (13900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1308,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (22300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1309,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (162000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1310,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (41300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1311,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (189000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1312,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (53500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1313,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (94100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1314,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (84700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1315,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3030000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1316,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (29000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1317,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (210000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1318,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (53700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1319,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (246000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1320,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (69600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1321,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (122000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1322,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (110000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1323,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3950000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1324,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (21700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1325,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (157000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1326,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (40100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1327,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (183000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1328,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (51900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1329,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (91300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1330,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (82200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1331,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2940000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1332,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (29000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1333,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (210000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1334,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (53700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1335,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (246000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1336,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (69600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1337,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (122000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1338,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (110000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1339,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3950000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1340,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2150000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1341,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (15500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1342,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3970000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1343,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (18200000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1344,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5140000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1345,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9050000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1346,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8140000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1347,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (292000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1348,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (399000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1349,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2890000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1350,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (738000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1351,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3380000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1352,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (957000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1353,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1680000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1354,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1510000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1355,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (54300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (1.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1356,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1357,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (18100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1358,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4620000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1359,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (21100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1360,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5990000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1361,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (10500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1362,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9470000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1363,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (339000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (1.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1364,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (546000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1365,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3950000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1366,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1010000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1367,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4620000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1368,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1310000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1369,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1370,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2070000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1371,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (74200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (3.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1372,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (710000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (3.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1373,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (5140000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (3.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1374,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1310000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (3.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1375,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (6010000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1376,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1377,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2990000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1378,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2690000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1379,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (96500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (-0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1380,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (530000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1381,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3840000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1382,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (980000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1383,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4480000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1384,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1270000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1385,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2230000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1386,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2010000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1387,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (72000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (5.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1388,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (710000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (3.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1389,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (5140000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (3.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1390,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1310000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (3.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1391,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (6010000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1392,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1393,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2990000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1394,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2690000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1395,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (96500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (-0.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1396,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (52500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (-2.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1397,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (380000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (-2.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1398,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (97000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (-2.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1399,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (444000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1400,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (126000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (5.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1401,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (221000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (1.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1402,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (199000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (2.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1403,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (7130000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (-6.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1404,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (23800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1405,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (173000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1406,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (44100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1407,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (202000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1408,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (57100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1409,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1410,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (90400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1411,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3240000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1412,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (149000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1413,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1080000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1414,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (276000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1415,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1260000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1416,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (357000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1417,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (628000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1418,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (566000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1419,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (20300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1420,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (32600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1421,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (236000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1422,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (60200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1423,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (276000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1424,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (78100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1425,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (137000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1426,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (124000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1427,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4430000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1428,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (42400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1429,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (307000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1430,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (78400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1431,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (359000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1432,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (102000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1433,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (179000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1434,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (161000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1435,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5760000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1436,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (31600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1437,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (229000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1438,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (58500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1439,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (268000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1440,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (75800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1441,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (133000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1442,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (120000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1443,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1444,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (42400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1445,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (307000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1446,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (78400000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1447,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (359000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1448,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (102000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1449,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (179000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1450,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (161000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1451,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5760000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1452,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3130000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1453,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (22700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1454,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5790000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1455,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (26500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1456,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7510000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1457,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (13200000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1458,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (11900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1459,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (426000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1460,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6350000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1461,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (46000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1462,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (11700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1463,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (53700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1464,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (15200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1465,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (26700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1466,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (24100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1467,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (862000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1468,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (39700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1469,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (287000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1470,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (73400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1471,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (336000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1472,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (95100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1473,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (167000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1474,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (151000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1475,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5390000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1476,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8670000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1477,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (62800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1478,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (16000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1479,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (73400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1480,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (20800000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1481,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (36600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1482,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (32900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1483,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1180000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1484,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (11300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1485,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (81700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1486,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (20900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1487,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (95500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1488,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (27000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1489,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (47600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1490,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (42800000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1491,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1530000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (5.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1492,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8420000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1493,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (61000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1494,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (15600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1495,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (71300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1496,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (20200000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1497,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (35500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1498,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (31900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1499,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1140000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1500,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (11300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1501,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (81700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1502,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (20900000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1503,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (95500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1504,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (27000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1505,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (47600000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1506,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (42800000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1507,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1530000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (5.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1508,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (834000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1509,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (6040000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1510,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1540000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1511,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7060000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1512,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1513,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3510000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1514,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3160000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1515,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (113000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (-0.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1516,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (17100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1517,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (124000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1518,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (31600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1519,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (144000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1520,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (40900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1521,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (71900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1522,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (64700000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1523,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2320000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1524,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (107000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1525,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (773000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1526,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (197000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1527,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (904000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1528,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (256000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1529,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (450000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1530,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (405000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1531,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (14500000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1532,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (23300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1533,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (169000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1534,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (43100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1535,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (197000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1536,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (55900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1537,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (98300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1538,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (88500000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1539,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3170000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1540,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (30300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1541,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (220000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1542,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (56100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1543,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (257000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1544,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (72700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1545,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (128000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1546,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (115000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1547,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4120000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1548,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (22600000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1549,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (164000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1550,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (41900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1551,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (192000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1552,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (54300000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1553,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (95400000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1554,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (85900000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1555,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3080000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1556,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (30300000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1557,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (220000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1558,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (56100000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1559,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (257000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1560,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (72700000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1561,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (128000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1562,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (115000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1563,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4120000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1564,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2240000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1565,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (16200000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1566,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4150000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1567,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (19000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1568,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5370000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1569,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9450000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1570,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8510000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1571,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (305000000000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

entry(
    index = 1572,
    label = "R9_SDSSSD;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (17100000000.0, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
    longDesc = 
u"""

""",
)

