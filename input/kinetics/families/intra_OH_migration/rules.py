#!/usr/bin/env python
# encoding: utf-8

name = "intra_OH_migration/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 826,
    label = "RnOOH;Y_rad_out",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
)

entry(
    index = 827,
    label = "R2OOH_S;C_rad_out_2H",
    kinetics = ArrheniusEP(
        A = (3.39e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
)

entry(
    index = 828,
    label = "R2OOH_S;C_rad_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (2.69e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (24.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
)

entry(
    index = 829,
    label = "R3OOH_SS;C_rad_out_2H",
    kinetics = ArrheniusEP(
        A = (4.47e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (27.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
)

entry(
    index = 830,
    label = "R3OOH_SS;C_rad_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (2.88e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
)

entry(
    index = 831,
    label = "R3OOH_SS;C_rad_out_Cs2",
    kinetics = ArrheniusEP(
        A = (4.79e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
)

entry(
    index = 832,
    label = "R4OOH_SSS;C_rad_out_2H",
    kinetics = ArrheniusEP(
        A = (1.12e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (16.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
)

entry(
    index = 833,
    label = "R4OOH_SSS;C_rad_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
)

entry(
    index = 834,
    label = "R4OOH_SSS;C_rad_out_Cs2",
    kinetics = ArrheniusEP(
        A = (8.71e+09, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
)

