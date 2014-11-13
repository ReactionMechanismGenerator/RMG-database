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
        A = (1e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    index = 814,
    label = "R6_SSM;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (30, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
)

entry(
    index = 815,
    label = "R6_SMM;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (40, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
)

entry(
    index = 816,
    label = "R7_MSMS;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0.21,
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
    label = "R7_SMSM;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (40, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
)

entry(
    index = 818,
    label = "R7_MMSR;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (30, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
)

entry(
    index = 819,
    label = "R7_RSMM;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (40, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
)

entry(
    index = 820,
    label = "R7_SMMS;multiplebond_intra;radadd_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess""",
)

entry(
    index = 821,
    label = "R5_DS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.41e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""BMK/cbsb7 + 1D-HR""",
)

entry(
    index = 822,
    label = "R6_DSS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (8.73e+09, 's^-1'),
        n = 0.21,
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
        A = (5.41e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.8, 'kcal/mol'),
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
        A = (8.73e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Guess, i.e. 822""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 902,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.05e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (7.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 903,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.08e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 904,
    label = "R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.04e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 910,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.1e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 911,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.44e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 912,
    label = "R6_SSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.09e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 918,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.85e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (6.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 919,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.25e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 920,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.83e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 923,
    label = "R6_SSS_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.71e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 924,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (3.04e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 925,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (2.04e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 926,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.38e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 927,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.31e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 928,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6.33e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 929,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.49e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (9.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 930,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.57e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (10.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 931,
    label = "R6_SSS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.89e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (1.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 934,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (7.65e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 935,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.16e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 936,
    label = "R6_SSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.58e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 942,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.38e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 943,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (9.34e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 944,
    label = "R6_SSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.37e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 950,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8.06e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 951,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.44e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 952,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.99e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 955,
    label = "R6_SSS_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (7.44e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (1.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 958,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8.06e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 959,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.44e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 960,
    label = "R4_S_D;doublebond_intra_2H_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (7.99e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 966,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (8.47e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 967,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (5.72e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 968,
    label = "R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (8.39e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 973,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (4.53e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 974,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.42e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 975,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (9.58e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 976,
    label = "R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.41e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 980,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.34e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 981,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.56e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 982,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.9e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 983,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.31e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 984,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.86e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 985,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.14e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 986,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.2e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 987,
    label = "R4_S_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.52e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (3.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 990,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.88e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 991,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.97e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 992,
    label = "R4_S_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.82e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 998,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.06e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 999,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (7.17e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1000,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.05e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1003,
    label = "R4_S_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (9.81e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (2.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1006,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.19e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1007,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.18e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1008,
    label = "R4_S_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6.13e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1014,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.19e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1015,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.15e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1016,
    label = "R5_SS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.16e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1022,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.35e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1023,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.26e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1024,
    label = "R5_SS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.32e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1030,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (5.62e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1031,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.79e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (24.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1032,
    label = "R5_SS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (5.57e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1036,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (9.25e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1037,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (6.19e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1038,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (1.94e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1039,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.31e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1040,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (1.92e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1041,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (4.52e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (19.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1042,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (4.76e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (20.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1043,
    label = "R5_SS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.79e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1046,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.32e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1047,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.57e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1048,
    label = "R5_SS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.3e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (23.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1054,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.21e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1055,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.84e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1056,
    label = "R5_SS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.17e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1062,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.45e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1063,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.65e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1064,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.43e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1066,
    label = "R5_SS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.01e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (20.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1068,
    label = "R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.69e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (21.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1069,
    label = "R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.13e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1070,
    label = "R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.55e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (21.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1071,
    label = "R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.4e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (30.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1072,
    label = "R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.52e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (30.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1073,
    label = "R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (8.27e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1074,
    label = "R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (8.7e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (28.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1075,
    label = "R6_SMS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.27e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (19.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1076,
    label = "R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.78e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (21.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1077,
    label = "R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.19e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1078,
    label = "R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.73e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (21.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1079,
    label = "R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.52e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (30.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1080,
    label = "R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.69e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (30.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1081,
    label = "R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (8.69e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1082,
    label = "R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (9.14e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (28.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1083,
    label = "R6_SMS_D;doublebond_intra_HNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (3.44e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (19.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1084,
    label = "R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.98e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (21.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1085,
    label = "R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.99e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (21.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1086,
    label = "R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.25e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (21.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1087,
    label = "R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.22e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (29.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1088,
    label = "R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6.19e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (30.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1089,
    label = "R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.46e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1090,
    label = "R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.53e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (28.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1091,
    label = "R6_SMS_D;doublebond_intra_NdNd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (5.77e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1092,
    label = "R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.03e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1093,
    label = "R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (6.88e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1094,
    label = "R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.16e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1095,
    label = "R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.46e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1096,
    label = "R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.14e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1097,
    label = "R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (5.03e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (24.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1098,
    label = "R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.29e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1099,
    label = "R6_SMS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (1.99e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1100,
    label = "R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.23e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1101,
    label = "R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (8.25e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (19.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1102,
    label = "R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.59e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1103,
    label = "R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.75e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1104,
    label = "R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.56e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1105,
    label = "R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.03e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (24.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1106,
    label = "R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.34e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1107,
    label = "R6_SMS_D;doublebond_intra_NdCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.39e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1108,
    label = "R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.23e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1109,
    label = "R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (1.49e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1110,
    label = "R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.68e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1111,
    label = "R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.16e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (26.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1112,
    label = "R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.64e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1113,
    label = "R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (1.09e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (24.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1114,
    label = "R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (1.15e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1115,
    label = "R6_SMS_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.32e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (15.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1116,
    label = "R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.3e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1117,
    label = "R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (8.69e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (19.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1118,
    label = "R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.73e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1119,
    label = "R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.84e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1120,
    label = "R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.7e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (27.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1121,
    label = "R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (6.35e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (24.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1122,
    label = "R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.68e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (25.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1123,
    label = "R6_SMS_D;doublebond_intra_NdCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.51e+12, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1124,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1125,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1126,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.59e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1127,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.42e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1128,
    label = "R7_SSSS_D;doublebond_intra_2H_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.56e+09, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1129,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1130,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1131,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1132,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1133,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1134,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (3.77e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1135,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (2.54e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1136,
    label = "R7_SSSS_D;doublebond_intra_HNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (3.74e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1137,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1138,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1139,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1140,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1141,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1142,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (6.32e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (8.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1143,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (4.26e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (16.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1144,
    label = "R7_SSSS_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (6.26e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (17.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1145,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1146,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1147,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1148,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (1.04e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1149,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (6.96e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1150,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.18e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1151,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.47e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1152,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.16e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1153,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csHCt",
    kinetics = ArrheniusEP(
        A = (5.08e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (11.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1154,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (5.35e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1155,
    label = "R7_SSSS_D;doublebond_intra_HCd_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (2.01e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (2.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1156,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1157,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1158,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.62e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1159,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.77e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1160,
    label = "R7_SSSS_D;doublebond_intra_NdCd_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.59e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1161,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1162,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1163,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1164,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_cs2H",
    kinetics = ArrheniusEP(
        A = (2.26e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1165,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1166,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (4.73e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1167,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (3.19e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (13.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1168,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (4.69e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1169,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1170,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1171,
    label = "R7_SSSS_D;doublebond_intra_HCt_pri;radadd_intra_cdsingleH",
    kinetics = ArrheniusEP(
        A = (4.37e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (2.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1172,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1173,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHNd",
    kinetics = ArrheniusEP(
        A = (8.79e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1174,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdNd",
    kinetics = ArrheniusEP(
        A = (2.76e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (5.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1175,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csHCd",
    kinetics = ArrheniusEP(
        A = (1.86e+11, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1176,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCd",
    kinetics = ArrheniusEP(
        A = (2.73e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (14.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1177,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1178,
    label = "R7_SSSS_D;doublebond_intra_NdCt_pri;radadd_intra_csNdCt",
    kinetics = ArrheniusEP(
        A = (6.76e+10, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (12.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

entry(
    index = 1179,
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
    shortDesc = u"""Aaron Vandeputte small GA method""",
)

