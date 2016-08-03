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
        A = (1e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
)

entry(
    index = 812,
    label = "R5_SD_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.02676e+11, 's^-1'),
        n = 0.55665,
        alpha = 0,
        E0 = (37.5409, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 2,
)

entry(
    index = 813,
    label = "R3_D;doublebond_intra_pri_HDe;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.05e+08, 's^-1'),
        n = 1.192,
        alpha = 0,
        E0 = (54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 5,
)

entry(
    index = 814,
    label = "R3_T;triplebond_intra_H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.05e+08, 's^-1'),
        n = 1.192,
        alpha = 0,
        E0 = (54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 5,
)

entry(
    index = 817,
    label = "R5_SM;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
)

entry(
    index = 817,
    label = "Cs-R5_SS_CS;thiyl_intra_H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.48e+06, 's^-1'),
        n = 1.17,
        alpha = 0,
        E0 = (0.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CBS-QB3, 1d-hr by CAC""",
)

entry(
    index = 818,
    label = "R6_SMM;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
)

entry(
    index = 819,
    label = "R5_SD_D;doublebond_intra_pri_HNd;radadd_intra_S",
    kinetics = ArrheniusEP(
        A = (7.97e+11, 's^-1'),
        n = 0.1,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""same reaction as above""",
)

entry(
    index = 821,
    label = "R5_DS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.73e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""BMK/cbsb7 + 1D-HR""",
)

entry(
    index = 822,
    label = "R6_DSS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.03e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""BMK/cbsb7 + 1D-HR""",
)

entry(
    index = 823,
    label = "R5_MS;multiplebond_intra;radadd_intra_cdsingle",
    kinetics = ArrheniusEP(
        A = (3.73e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess, i.e. 821""",
)

entry(
    index = 824,
    label = "R6_MSR;multiplebond_intra;radadd_intra_cdsingle",
    kinetics = ArrheniusEP(
        A = (1.03e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess, i.e. 822""",
)

entry(
    index = 900,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.06e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 901,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.22e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 902,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.57e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 903,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.59e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 904,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.34e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 905,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.29e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 906,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.16e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 907,
    label = "R6_SSS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.88e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 908,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.92e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 909,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.39e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 910,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.49e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 911,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.62e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 912,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.59e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 913,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (8.08e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 914,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (7.27e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 915,
    label = "R6_SSS_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.05e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 916,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (4.19e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 917,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.03e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 918,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (7.62e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 919,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.54e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 920,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 921,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.76e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 922,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.59e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 923,
    label = "R6_SSS_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (6.67e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 924,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.13e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 925,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (8.2e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 926,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.06e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 927,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (9.59e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 928,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.71e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 929,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (4.77e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 930,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (4.29e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 931,
    label = "R6_SSS_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.8e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 932,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (4.07e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 933,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.95e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 934,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (7.4e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 935,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.44e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 936,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (9.74e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 937,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.71e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 938,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.54e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 939,
    label = "R6_SSS_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (6.48e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 940,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.96e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 941,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.14e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 942,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.38e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 943,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.5e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 944,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.08e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 945,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.25e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 946,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.12e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 947,
    label = "R6_SSS_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.71e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 948,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.58e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 949,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.87e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 950,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.7e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 951,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.19e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 952,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6.19e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 953,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.09e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 954,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9.8e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 955,
    label = "R6_SSS_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.12e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 956,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.83e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 957,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.32e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 958,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.33e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 959,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.55e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 960,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.38e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 961,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (7.71e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 962,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.94e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 963,
    label = "R4_S_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.91e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 964,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.14e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 965,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (8.29e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 966,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.08e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 967,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (9.68e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 968,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.74e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 969,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (4.82e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 970,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (4.34e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 971,
    label = "R4_S_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.82e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 972,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.5e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 973,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.81e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 974,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.55e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 975,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.12e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (41.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 976,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.99e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (41.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 977,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.05e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 978,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9.48e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 979,
    label = "R4_S_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.98e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 980,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.76e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 981,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.9e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 982,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.23e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 983,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.72e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 984,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.62e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 985,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.85e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 986,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.56e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 987,
    label = "R4_S_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.08e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 988,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.43e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 989,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.76e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 990,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.42e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 991,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.05e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (42.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 992,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.82e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (43.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 993,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.02e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 994,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9.21e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 995,
    label = "R4_S_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.87e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 996,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.76e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 997,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.28e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 998,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.21e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 999,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.49e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1000,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.23e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1001,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (7.44e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1002,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.69e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1003,
    label = "R4_S_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.81e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1004,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.54e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1005,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.12e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1006,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.81e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1007,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.31e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (41.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1008,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.7e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (42.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1009,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.5e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1010,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.85e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1011,
    label = "R4_S_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.46e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1012,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (4.86e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1013,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.52e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1014,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8.84e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1015,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.11e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1016,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.16e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1017,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.05e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1018,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.84e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1019,
    label = "R5_SS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (7.74e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1020,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.04e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1021,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.2e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1022,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.53e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1023,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.57e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1024,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.28e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1025,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.28e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1026,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.15e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1027,
    label = "R5_SS_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.84e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1028,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.64e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1029,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.81e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1030,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.21e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1031,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.62e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1032,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.59e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1033,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.8e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1034,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.52e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1035,
    label = "R5_SS_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.06e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1036,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.8e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1037,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.3e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1038,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.27e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1039,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.52e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1040,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.3e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1041,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (7.57e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1042,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.81e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1043,
    label = "R5_SS_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.86e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1044,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.45e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1045,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.67e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1046,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.17e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1047,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.46e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1048,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.55e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1049,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.72e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1050,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.45e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1051,
    label = "R5_SS_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.03e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1052,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (4.69e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1053,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.4e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1054,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8.53e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1055,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.97e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1056,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.12e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1057,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.98e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1058,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.78e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1059,
    label = "R5_SS_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (7.47e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1060,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (4.1e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1061,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.97e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1062,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (7.45e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1063,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.47e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1064,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (9.82e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1065,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.73e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1066,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.55e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1067,
    label = "R5_SS_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (6.53e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1068,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.31e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1069,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (9.48e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1070,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.38e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1071,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.11e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1072,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.14e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1073,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (5.52e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1074,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (4.97e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1075,
    label = "R6_SMS_D;doublebond_intra_pri_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.09e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1076,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8.19e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1077,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (5.93e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1078,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.49e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1079,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (6.93e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1080,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.96e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1081,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.45e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1082,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.11e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1083,
    label = "R6_SMS_D;doublebond_intra_pri_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.3e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1084,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.79e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1085,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.3e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1086,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.26e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1087,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.51e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1088,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.29e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1089,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (7.54e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1090,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.79e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1091,
    label = "R6_SMS_D;doublebond_intra_pri_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.85e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1092,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (4.84e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1093,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.51e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1094,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8.8e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1095,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.1e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1096,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.16e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1097,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.04e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1098,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.84e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1099,
    label = "R6_SMS_D;doublebond_intra_pri_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (7.71e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1100,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.74e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1101,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.26e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1102,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.16e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1103,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.47e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1104,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.16e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1105,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (7.32e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1106,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.59e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1107,
    label = "R6_SMS_D;doublebond_intra_pri_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.77e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1108,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.26e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1109,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (9.15e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1110,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.3e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1111,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.07e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1112,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.03e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1113,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (5.32e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1114,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (4.79e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1115,
    label = "R6_SMS_D;doublebond_intra_pri_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.01e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1116,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.1e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1117,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (8e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1118,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.01e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1119,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (9.35e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1120,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.65e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1121,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (4.65e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1122,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (4.19e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1123,
    label = "R6_SMS_D;doublebond_intra_pri_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.76e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1124,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.83e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1125,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.77e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1126,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.97e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1127,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.24e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1128,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (9.18e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1129,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.61e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1130,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.45e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1131,
    label = "R6_SSS_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (6.1e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1132,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.4e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1133,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.74e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1134,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.36e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1135,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.03e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1136,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.74e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1137,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.01e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1138,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9.09e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1139,
    label = "R6_SSS_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.82e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1140,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5.24e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1141,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.79e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1142,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (9.52e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1143,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.43e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1144,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.25e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1145,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.21e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1146,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.99e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1147,
    label = "R6_SSS_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (8.34e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1148,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.42e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1149,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.03e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1150,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.58e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1151,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.2e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1152,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.39e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1153,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (5.97e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1154,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.37e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1155,
    label = "R6_SSS_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.26e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1156,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5.08e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1157,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.68e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1158,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (9.25e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1159,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.3e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1160,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.22e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1161,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.14e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1162,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.93e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1163,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (8.1e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1164,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.7e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1165,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.68e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1166,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.72e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1167,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.13e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1168,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (8.86e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1169,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.56e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1170,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.4e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1171,
    label = "R6_SSS_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.89e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1172,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.23e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1173,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.34e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1174,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.88e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1175,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.73e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1176,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.74e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1177,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.36e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1178,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.23e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1179,
    label = "R6_SSS_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.15e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1180,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.29e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1181,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.66e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1182,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.16e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1183,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.94e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1184,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.48e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1185,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.64e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1186,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.67e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1187,
    label = "R4_S_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.64e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1188,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.43e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1189,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.04e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1190,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.6e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1191,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.21e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1192,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.43e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1193,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.03e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1194,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.42e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1195,
    label = "R4_S_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.28e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1196,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.13e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1197,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.26e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1198,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.69e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1199,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.65e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1200,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.49e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (41.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1201,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.32e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1202,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.19e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1203,
    label = "R4_S_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.98e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1204,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8.45e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1205,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (6.12e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1206,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.54e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1207,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.15e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1208,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.03e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1209,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.56e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1210,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.21e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1211,
    label = "R4_S_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.35e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1212,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.03e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1213,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.2e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1214,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.52e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1215,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.57e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (42.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1216,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.27e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (42.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1217,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.28e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1218,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.15e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1219,
    label = "R4_S_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.84e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1220,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.21e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1221,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.6e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1222,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.01e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1223,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.87e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1224,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.29e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1225,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.3e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1226,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.37e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1227,
    label = "R4_S_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.51e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1228,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.93e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1229,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.4e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1230,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.51e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1231,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.63e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (41.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1232,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.62e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (42.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1233,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (8.13e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1234,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (7.31e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1235,
    label = "R4_S_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.07e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1236,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.07e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1237,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.4e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1238,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.1e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1239,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.14e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1240,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.46e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1241,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.56e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1242,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.3e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1243,
    label = "R5_SS_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (9.68e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1244,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.8e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1245,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.75e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1246,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.91e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1247,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.22e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1248,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (9.1e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1249,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.6e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1250,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.44e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1251,
    label = "R5_SS_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (6.05e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1252,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8.3e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1253,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (6.01e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1254,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.51e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1255,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.03e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1256,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.99e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1257,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.5e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1258,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.15e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1259,
    label = "R5_SS_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.32e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1260,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.25e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1261,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.63e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1262,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.08e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1263,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.9e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1264,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.38e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1265,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.46e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1266,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.52e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1267,
    label = "R5_SS_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.58e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1268,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8.06e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1269,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (5.84e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1270,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.47e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1271,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (6.83e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1272,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.93e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1273,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.4e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1274,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.06e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1275,
    label = "R5_SS_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.28e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1276,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5.86e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1277,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.25e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1278,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.07e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1279,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.96e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1280,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.4e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1281,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.47e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1282,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.22e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1283,
    label = "R5_SS_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (9.34e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1284,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5.12e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1285,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.71e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1286,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (9.32e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1287,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.34e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1288,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.23e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1289,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.16e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1290,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.94e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1291,
    label = "R5_SS_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (8.16e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1292,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.64e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1293,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.19e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1294,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.98e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1295,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.39e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1296,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.92e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1297,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.9e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1298,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.21e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1299,
    label = "R6_SMS_D;doublebond_intra_secNd_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.61e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1300,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.02e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1301,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (7.42e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1302,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.86e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1303,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (8.67e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1304,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.45e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1305,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (4.31e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1306,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.88e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1307,
    label = "R6_SMS_D;doublebond_intra_secNd_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.63e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1308,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.24e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1309,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.62e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1310,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.07e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1311,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.89e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1312,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.36e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1313,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.43e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1314,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.49e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1315,
    label = "R6_SMS_D;doublebond_intra_secNd_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.56e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1316,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.05e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1317,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.38e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1318,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.1e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1319,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.12e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1320,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.45e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1321,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.55e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1322,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.29e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1323,
    label = "R6_SMS_D;doublebond_intra_secNd_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (9.64e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1324,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.17e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1325,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.57e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1326,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.95e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1327,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.84e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1328,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.21e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1329,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.16e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1330,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.24e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1331,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.46e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1332,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.58e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1333,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.14e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1334,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.87e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1335,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.34e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1336,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.78e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1337,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.66e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1338,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.99e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1339,
    label = "R6_SMS_D;doublebond_intra_secNd_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.52e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1340,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.38e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1341,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1342,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.51e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1343,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.17e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1344,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.31e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1345,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (5.82e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1346,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.24e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1347,
    label = "R6_SMS_D;doublebond_intra_secNd_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.2e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1348,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (4e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1349,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.9e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1350,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (7.28e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1351,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.39e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1352,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (9.59e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1353,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.69e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1354,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.52e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1355,
    label = "R6_SSS_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (6.38e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1356,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.5e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1357,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.81e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1358,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.55e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1359,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.12e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1360,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1361,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.05e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1362,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9.49e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1363,
    label = "R6_SSS_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.99e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1364,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5.47e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1365,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.96e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1366,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (9.95e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (8.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1367,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.63e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1368,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.31e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1369,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.31e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1370,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.07e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1371,
    label = "R6_SSS_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (8.71e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1372,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.48e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1373,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.07e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1374,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.69e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1375,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.25e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1376,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.54e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1377,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.23e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1378,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.61e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1379,
    label = "R6_SSS_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.36e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (5.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1380,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5.31e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1381,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.85e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1382,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (9.66e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1383,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.5e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1384,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.27e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1385,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.24e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1386,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.01e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1387,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (8.46e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1388,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.86e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1389,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.8e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1390,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (7.02e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (7.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1391,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.27e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1392,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (9.25e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1393,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.63e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1394,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.46e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1395,
    label = "R6_SSS_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (6.15e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (4.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1396,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.37e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1397,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.44e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1398,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.14e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (9.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1399,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.86e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1400,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (8.09e+08, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1401,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.42e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1402,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.28e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1403,
    label = "R6_SSS_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.38e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (6.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1404,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.39e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1405,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.73e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1406,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.35e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1407,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.02e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1408,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.72e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1409,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.01e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1410,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9.06e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1411,
    label = "R4_S_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.81e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1412,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.49e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1413,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.08e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1414,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.72e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1415,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.26e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1416,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.58e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1417,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.3e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1418,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.67e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1419,
    label = "R4_S_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.38e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1420,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.27e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1421,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.36e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1422,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.94e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1423,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.76e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1424,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.82e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1425,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.38e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1426,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.24e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1427,
    label = "R4_S_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.2e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1428,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8.83e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1429,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (6.4e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1430,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.61e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1431,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.47e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1432,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.12e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1433,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.72e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1434,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.35e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1435,
    label = "R4_S_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.41e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1436,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.17e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1437,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.3e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1438,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.77e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1439,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.68e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1440,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.6e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (40.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1441,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.34e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1442,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.2e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1443,
    label = "R4_S_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.05e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1444,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.31e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1445,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.67e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1446,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.19e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1447,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.95e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1448,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.52e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (37.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1449,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.71e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (33.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1450,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.74e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (34.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1451,
    label = "R4_S_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.67e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1452,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.01e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1453,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.46e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1454,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.66e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (32.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1455,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.71e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (38.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1456,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.83e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (39.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1457,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (8.49e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (35.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1458,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (7.64e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (36.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1459,
    label = "R4_S_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.21e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1460,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.35e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1461,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.6e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1462,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.15e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1463,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.37e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1464,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.52e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1465,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.67e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1466,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.41e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1467,
    label = "R5_SS_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.01e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (10.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1468,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.97e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1469,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.88e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1470,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (7.22e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1471,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.36e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1472,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (9.51e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1473,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.67e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1474,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.51e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1475,
    label = "R5_SS_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (6.32e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1476,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8.67e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1477,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (6.28e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1478,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.58e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1479,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.34e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1480,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.08e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1481,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.66e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1482,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.29e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1483,
    label = "R5_SS_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.38e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (12.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1484,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.35e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1485,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.7e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1486,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.27e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1487,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.99e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1488,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.62e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1489,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.89e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1490,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.9e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1491,
    label = "R5_SS_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.74e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1492,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8.42e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1493,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (6.1e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1494,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.53e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1495,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.13e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1496,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.02e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1497,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.55e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1498,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.19e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1499,
    label = "R5_SS_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.34e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1500,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.12e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1501,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.44e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1502,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.11e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (14.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1503,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.18e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1504,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.47e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1505,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.58e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (17.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1506,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.32e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1507,
    label = "R5_SS_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (9.76e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (11.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1508,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5.35e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1509,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.88e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (15.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1510,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (9.74e+09, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (16.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1511,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.53e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1512,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.28e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1513,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.26e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1514,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.03e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1515,
    label = "R5_SS_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (8.53e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (13.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1516,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.71e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1517,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.24e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1518,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.11e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1519,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.45e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1520,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.1e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1521,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (7.21e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1522,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.49e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1523,
    label = "R6_SMS_D;doublebond_intra_secDe_2H;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.72e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1524,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.07e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1525,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (7.75e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1526,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.95e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1527,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (9.05e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1528,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.56e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1529,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (4.51e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1530,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (4.06e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1531,
    label = "R6_SMS_D;doublebond_intra_secDe_HNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.7e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (18.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1532,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.34e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1533,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.69e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1534,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.25e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1535,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.98e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1536,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.6e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1537,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.85e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1538,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.87e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1539,
    label = "R6_SMS_D;doublebond_intra_secDe_NdNd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.72e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1540,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.32e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1541,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.58e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1542,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.15e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1543,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.35e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1544,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.51e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (29.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1545,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.66e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1546,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.4e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (26.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1547,
    label = "R6_SMS_D;doublebond_intra_secDe_HCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.01e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1548,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.27e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1549,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.64e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1550,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.13e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1551,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.92e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1552,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.44e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (31.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1553,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.57e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1554,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.61e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1555,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCd;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.62e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1556,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.65e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1557,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.2e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1558,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1559,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.4e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1560,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.95e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1561,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.95e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (24.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1562,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.26e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (25.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1563,
    label = "R6_SMS_D;doublebond_intra_secDe_HCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.63e+12, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (19.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1564,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.44e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1565,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.04e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1566,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.62e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (23.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1567,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.22e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1568,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.46e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (30.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1569,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.08e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (27.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1570,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.47e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (28.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1571,
    label = "R6_SMS_D;doublebond_intra_secDe_NdCt;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.3e+11, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (21.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1572,
    label = "R9_SDSSSD;doublebond_intra_pri_2H;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.71e+10, 's^-1'),
        n = 0.19,
        alpha = 0,
        E0 = (20.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

