#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/rules"
shortDesc = u""
longDesc = u"""
General comments go at the top of the file,

or in a section(s) titled 'General'

.. the ID must match those in the rateLibrary AS A STRING (ie. '2' is different from '02')
"""
entry(
    index = 807,
    label = "Rn;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
)

entry(
    index = 808,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.51e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (6.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
)

entry(
    index = 809,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHDe",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (25.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
)

entry(
    index = 810,
    label = "R6_SMS_D;doublebond_intra;radadd_intra_cs",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (46.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
)

entry(
    index = 811,
    label = "R6_SSM_D;doublebond_intra;radadd_intra_cs",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (46.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
)

entry(
    index = 812,
    label = "R5_SD_D;doublebond_intra_HNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (46.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
)

entry(
    index = 813,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_O",
    kinetics = ArrheniusEP(
        A = (2.724e+10, 's^-1', '*|/', 3),
        n = 0.478,
        alpha = 0,
        E0 = (29.169, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations with 1d h.r. corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations for the reaction CH2=CH-CH2-OO => *CH2-cycle(CH-CH2-O-O)

Previous RMG estimate for this reaction was an "Average of average" estimate.  This reaction was of
interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => CH2O+CH2CHO.  The high-p
limit kinetics were necessary to estimate a k(T,P) for this PES.

Reactant: 2 hindered rotors were considered (the OO and CH2OO torsions)
TS: 0 hindered rotors were considered (the only low-frequency torisonal mode corresponded to
	a hindered rotation within the cycle; MRH did not think treating this as a 1-d separable
	hindered rotor was accurate)
Product: 1 hindered rotor was considered (the *CH2 torsion)

All external symmetry numbers were set equal to one.  The k(T) was calculated from 600 - 2000 K,
in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.724e+10 * (T/1K)^0.478 * exp(-29.169 kcal/mol / RT) cm3/mol/s.
""",
)

entry(
    index = 900,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5e+08, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 901,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.35e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 902,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.07e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 903,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.26e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 904,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (8.46e+08, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 905,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.45e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 906,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.57e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 907,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (9.68e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 908,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5.26e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 909,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.52e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 910,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.12e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 911,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.32e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 912,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (8.89e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 913,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.57e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 914,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.7e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 915,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.02e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 916,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8.81e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 917,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (5.89e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 918,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.88e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 919,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.22e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 920,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.49e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 921,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (4.31e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 922,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (4.53e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 923,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.7e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 924,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (8.62e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 925,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (5.76e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 926,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.84e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 927,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.17e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 928,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.46e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 929,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (4.21e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 930,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (4.43e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 931,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.67e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 932,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.65e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 933,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.44e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 934,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (7.79e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 935,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (9.19e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 936,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6.17e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 937,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.78e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (10.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 938,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.88e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 939,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (7.06e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (1.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 940,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.6e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 941,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.41e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 942,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.41e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 943,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.66e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 944,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.12e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 945,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.22e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (9.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 946,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.39e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (10.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 947,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.28e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (1.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 948,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.84e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 949,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.57e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 950,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8.21e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 951,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (9.68e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 952,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6.5e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 953,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.88e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (9.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 954,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.98e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (10.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 955,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (7.43e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (1.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 956,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.84e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 957,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.57e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 958,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8.21e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 959,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (9.68e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 960,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6.5e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 961,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.88e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 962,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.98e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 963,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (7.44e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 964,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (4.04e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 965,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.7e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 966,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8.62e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 967,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.02e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 968,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6.83e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 969,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.97e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 970,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.08e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 971,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (7.81e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 972,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.77e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 973,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.52e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 974,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.45e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 975,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.7e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 976,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.14e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 977,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.31e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 978,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.48e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 979,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.31e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 980,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (6.62e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 981,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.42e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 982,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.41e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 983,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.67e+14, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 984,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.12e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 985,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (3.23e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 986,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (3.4e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 987,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.28e+14, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 988,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.8e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 989,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.87e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 990,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.98e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 991,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.05e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 992,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.74e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 993,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.37e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 994,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.44e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 995,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.42e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 996,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (5.07e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 997,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (3.39e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 998,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.08e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 999,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.28e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1000,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (8.57e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1001,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (2.48e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1002,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (2.61e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1003,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (9.8e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (2.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1004,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.95e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1005,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.97e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1006,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.3e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1007,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.43e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1008,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.99e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1009,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.44e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1010,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.52e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1011,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.71e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1012,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.52e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1013,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.02e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1014,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.25e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1015,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.83e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (26.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1016,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.57e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1017,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (7.43e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1018,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (7.82e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (23.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1019,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.94e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1020,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.6e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1021,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.07e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1022,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.41e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1023,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.02e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1024,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.7e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (26.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1025,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (7.81e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1026,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.22e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (23.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1027,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.09e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1028,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.68e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1029,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.79e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1030,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.72e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1031,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (6.75e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1032,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.53e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (26.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1033,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.31e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1034,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.38e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (23.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1035,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.18e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1036,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.62e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1037,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.75e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1038,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.59e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1039,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (6.6e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (24.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1040,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.43e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1041,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.28e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (21.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1042,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.35e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1043,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.07e+13, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1044,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.11e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1045,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (7.41e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1046,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.37e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1047,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.79e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (23.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1048,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.87e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (24.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1049,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (5.42e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (19.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1050,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.7e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (20.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1051,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.14e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1052,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.01e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1053,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.34e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1054,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.28e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1055,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.05e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1056,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.39e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (23.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1057,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (9.8e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (19.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1058,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.03e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (20.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1059,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.88e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1060,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.17e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1061,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (7.81e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1062,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.49e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1063,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.94e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (23.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1064,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.98e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (23.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1065,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (5.71e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (19.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1066,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.01e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (20.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1067,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.26e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1068,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.71e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1069,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.14e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1070,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.65e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1071,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.31e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1072,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.89e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1073,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (8.36e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1074,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.8e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1075,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.31e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1076,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.8e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1077,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.2e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1078,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.84e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1079,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.53e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1080,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.04e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1081,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (8.78e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1082,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9.24e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1083,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.48e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1084,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.01e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1085,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.01e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1086,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.43e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1087,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.59e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1088,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.09e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1089,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.47e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1090,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.55e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1091,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.83e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1092,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.95e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1093,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.97e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1094,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.29e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1095,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.42e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1096,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.98e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1097,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.44e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1098,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.51e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1099,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.7e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1100,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.25e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1101,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (8.34e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1102,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.66e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1103,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.14e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1104,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.11e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1105,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.09e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1106,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.41e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1107,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.41e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1108,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.25e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1109,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.51e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1110,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.82e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1111,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.68e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1112,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.81e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1113,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.1e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1114,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.16e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1115,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.36e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (2.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1116,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.31e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1117,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (8.78e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1118,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.81e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1119,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.31e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1120,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.22e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1121,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.42e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1122,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.75e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

entry(
    index = 1123,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.54e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aan Vandeputte small GA method""",
)

