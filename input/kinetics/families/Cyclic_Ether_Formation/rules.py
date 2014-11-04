#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 812,
    label = "RnOO;Y_rad_intra",
    kinetics = ArrheniusEP(
        A = (1e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
)

entry(
    index = 813,
    label = "R2OOH_S;C_pri_rad_intra",
    kinetics = ArrheniusEP(
        A = (3.98e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 813,
    label = "R2OOR_S;C_pri_rad_intra",
    kinetics = ArrheniusEP(
        A = (3.98e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 814,
    label = "R2OOH_S;C_sec_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.38e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 814,
    label = "R2OOR_S;C_sec_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.38e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 815,
    label = "R2OOR_S;C_ter_rad_intra",
    kinetics = ArrheniusEP(
        A = (3.09e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 815,
    label = "R2OOH_S;C_ter_rad_intra",
    kinetics = ArrheniusEP(
        A = (3.09e+12, 's^-1', '*|/', 1.2),
        n = 0,
        alpha = (1.3, '', '+|-', 0.3),
        E0 = (37, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 816,
    label = "R3OOH_SS;C_pri_rad_intra",
    kinetics = ArrheniusEP(
        A = (4.47e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 816,
    label = "R3OOR_SS;C_pri_rad_intra",
    kinetics = ArrheniusEP(
        A = (4.47e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 817,
    label = "R3OOH_SS;C_sec_rad_intra",
    kinetics = ArrheniusEP(
        A = (2.04e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 817,
    label = "R3OOR_SS;C_sec_rad_intra",
    kinetics = ArrheniusEP(
        A = (2.04e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 818,
    label = "R3OOR_SS;C_ter_rad_intra",
    kinetics = ArrheniusEP(
        A = (3.31e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 818,
    label = "R3OOH_SS;C_ter_rad_intra",
    kinetics = ArrheniusEP(
        A = (3.31e+11, 's^-1', '*|/', 1.74),
        n = 0,
        alpha = (1, '', '+|-', 0.1),
        E0 = (38.2, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 819,
    label = "R4OOR_SSS;C_pri_rad_intra",
    kinetics = ArrheniusEP(
        A = (5.13e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (14.8, 'kcal/mol', '+|-', 2),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 819,
    label = "R4OOH_SSS;C_pri_rad_intra",
    kinetics = ArrheniusEP(
        A = (5.13e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (14.8, 'kcal/mol', '+|-', 2),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 820,
    label = "R4OOR_SSS;C_sec_rad_intra",
    kinetics = ArrheniusEP(
        A = (3.63e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (13, 'kcal/mol', '+|-', 2.5),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 820,
    label = "R4OOH_SSS;C_sec_rad_intra",
    kinetics = ArrheniusEP(
        A = (3.63e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (13, 'kcal/mol', '+|-', 2.5),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 821,
    label = "R4OOR_SSS;C_ter_rad_intra",
    kinetics = ArrheniusEP(
        A = (2.57e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (11.5, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 821,
    label = "R4OOH_SSS;C_ter_rad_intra",
    kinetics = ArrheniusEP(
        A = (2.57e+10, 's^-1', '*|/', 1.41),
        n = 0,
        alpha = 0,
        E0 = (11.5, 'kcal/mol', '+|-', 3),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.""",
)

entry(
    index = 822,
    label = "R2OOR_S;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (6e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
)

entry(
    index = 822,
    label = "R2OOH_S;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (6e+11, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
)

entry(
    index = 823,
    label = "R3OOR_SS;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (7.5e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
)

entry(
    index = 823,
    label = "R3OOH_SS;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (7.5e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (15.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
)

entry(
    index = 824,
    label = "R4OOR_SSS;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (9.38e+09, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
)

entry(
    index = 824,
    label = "R4OOH_SSS;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (9.38e+09, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
)

entry(
    index = 825,
    label = "R5OOH_SSSS;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.17e+09, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
)

entry(
    index = 825,
    label = "R5OOR_SSSS;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.17e+09, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
)

entry(
    index = 826,
    label = "R5OOR_SSSSCO;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.27e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment of hindered rotor (SSM)""",
)

entry(
    index = 826,
    label = "R5OOH_SSSSCO;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.27e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment of hindered rotor (SSM)""",
)

entry(
    index = 827,
    label = "R2OOR_SCO;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (6.92e+15, 's^-1'),
        n = -0.53,
        alpha = 0,
        E0 = (24.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment for hindered rotor, QTST Calculation (CFG & JWA)""",
)

entry(
    index = 827,
    label = "R2OOH_SCO;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (6.92e+15, 's^-1'),
        n = -0.53,
        alpha = 0,
        E0 = (24.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 Including treatment for hindered rotor, QTST Calculation (CFG & JWA)""",
)

entry(
    index = 828,
    label = "R4OOR_SSSCO;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.27e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
)

entry(
    index = 828,
    label = "R4OOH_SSSCO;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.27e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
)

entry(
    index = 829,
    label = "R3OOH_SSCO;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.27e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
)

entry(
    index = 829,
    label = "R3OOR_SSCO;Cs_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.27e+08, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (18.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Estimate (Same as 5 memebered ring)""",
)

entry(
    index = 830,
    label = "R2OOJ_S;C_pri_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.62e+09, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (31.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 831,
    label = "R2OOJ_S;C_pri_rad_intra",
    kinetics = ArrheniusEP(
        A = (1.61e+09, 's^-1'),
        n = 1.09,
        alpha = 0,
        E0 = (29.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 832,
    label = "R2OOJ_S;C_rad/H/NonDeC_intra",
    kinetics = ArrheniusEP(
        A = (3.27e+09, 's^-1'),
        n = 1.06,
        alpha = 0,
        E0 = (31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

