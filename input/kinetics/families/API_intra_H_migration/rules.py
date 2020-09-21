#!/usr/bin/env python
# encoding: utf-8

name = "API_intra_H_migration/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 614,
    label = "RnH;Y_rad_out;XH_out",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""default""",
)

entry(
    index = 649,
    label = "R2H_S;Cd_rad_out;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (1.67e+10, 's^-1'),
        n = 0.79,
        alpha = 0,
        E0 = (35.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 658,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (4.89e+09, 's^-1'),
        n = 0.81,
        alpha = 0,
        E0 = (25.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 660,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (8.83e+10, 's^-1'),
        n = 0.3,
        alpha = 0,
        E0 = (29.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 662,
    label = "R2H_S;C_rad_out_Cs2;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (8.2e+09, 's^-1'),
        n = 0.65,
        alpha = 0,
        E0 = (31.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 1018,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (5.14e-16, 's^-1'),
        n = 8.15,
        alpha = 0,
        E0 = (16.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
)

entry(
    index = 1019,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (2.76e-23, 's^-1'),
        n = 10.17,
        alpha = 0,
        E0 = (13.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
)

entry(
    index = 1020,
    label = "R3H_SS;C_rad_out_Cs2;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (8.59e-19, 's^-1'),
        n = 8.79,
        alpha = 0,
        E0 = (16.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
)

entry(
    index = 1022,
    label = "R4H_SSS;C_rad_out_2H;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (0.00181, 's^-1'),
        n = 4.25,
        alpha = 0,
        E0 = (9.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
)

entry(
    index = 1024,
    label = "R5H_SSSS;C_rad_out_2H;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (10500, 's^-1'),
        n = 2.14,
        alpha = 0,
        E0 = (7.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
)

entry(
    index = 1028,
    label = "R6H_SSSSS;C_rad_out_2H;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (10500, 's^-1'),
        n = 2.14,
        alpha = 0,
        E0 = (7.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
)

entry(
    index = 1029,
    label = "R6H_SSSSS_bicyclopentane;C_rad_out_H/NonDeC;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (46.1, 's^-1'),
        n = 3.21,
        alpha = 0,
        E0 = (14.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
)

