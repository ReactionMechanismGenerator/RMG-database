#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 614,
    label = "RnH;Y_rad_out;XH_out",
    kinetics = ArrheniusEP(
        A = (10000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""default""",
    longDesc = 
u"""

""",
)

entry(
    index = 615,
    label = "R2H_S;C_rad_out_single;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (548000000.0, 's^-1'),
        n = 1.62,
        alpha = 0,
        E0 = (38.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green.
""",
)

entry(
    index = 616,
    label = "R2H_S;C_rad_out_single;Cs_H_out_1H",
    kinetics = ArrheniusEP(
        A = (959000000.0, 's^-1'),
        n = 1.39,
        alpha = 0,
        E0 = (39.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green.
""",
)

entry(
    index = 617,
    label = "R3H_SS;C_rad_out_single;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (1390000000.0, 's^-1'),
        n = 0.98,
        alpha = 0,
        E0 = (33.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green
""",
)

entry(
    index = 618,
    label = "R3H_SS;C_rad_out_single;Cs_H_out_1H",
    kinetics = ArrheniusEP(
        A = (1760000000.0, 's^-1'),
        n = 0.76,
        alpha = 0,
        E0 = (34.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.
""",
)

entry(
    index = 619,
    label = "R4H_SSS;C_rad_out_single;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (2540000000.0, 's^-1'),
        n = 0.35,
        alpha = 0,
        E0 = (19.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.
""",
)

entry(
    index = 620,
    label = "R4H_SSS;C_rad_out_single;Cs_H_out_1H",
    kinetics = ArrheniusEP(
        A = (3220000000.0, 's^-1'),
        n = 0.13,
        alpha = 0,
        E0 = (20.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.
""",
)

entry(
    index = 621,
    label = "R4H_SSS;C_rad_out_single;Cs_H_out_noH",
    kinetics = ArrheniusEP(
        A = (18600000000.0, 's^-1'),
        n = 0.58,
        alpha = 0,
        E0 = (26.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. 

NEEDS TO BE CHECKED
""",
)

entry(
    index = 622,
    label = "R5H_SSSS;C_rad_out_single;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (428000000000.0, 's^-1'),
        n = -1.05,
        alpha = 0,
        E0 = (11.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green
""",
)

entry(
    index = 623,
    label = "R5H_SSSS;C_rad_out_single;Cs_H_out_1H",
    kinetics = ArrheniusEP(
        A = (13600000000.0, 's^-1'),
        n = -0.66,
        alpha = 0,
        E0 = (14.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green
""",
)

entry(
    index = 624,
    label = "R4H_SSS;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (29.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 625,
    label = "R4H_SSS;O_rad_out;Cs_H_out_1H",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (26.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 626,
    label = "R4H_SSS;O_rad_out;Cs_H_out_noH",
    kinetics = ArrheniusEP(
        A = (100000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (24.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 627,
    label = "R5H_SSSS;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (12500000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (24.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 628,
    label = "R5H_SSSS;O_rad_out;Cs_H_out_1H",
    kinetics = ArrheniusEP(
        A = (12500000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (20.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 629,
    label = "R5H_SSSS;O_rad_out;Cs_H_out_noH",
    kinetics = ArrheniusEP(
        A = (12500000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (19.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 630,
    label = "R6H_SSSSS;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (1560000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (22.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 631,
    label = "R6H_SSSSS;O_rad_out;Cs_H_out_1H",
    kinetics = ArrheniusEP(
        A = (1560000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (19.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 632,
    label = "R6H_SSSSS;O_rad_out;Cs_H_out_noH",
    kinetics = ArrheniusEP(
        A = (1560000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (17.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 633,
    label = "R7H;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (195000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (25.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 634,
    label = "R7H;O_rad_out;Cs_H_out_1H",
    kinetics = ArrheniusEP(
        A = (195000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (25.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 635,
    label = "R7H;O_rad_out;Cs_H_out_noH",
    kinetics = ArrheniusEP(
        A = (195000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (25.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
)

entry(
    index = 636,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (4450000000.0, 's^-1'),
        n = 1.12,
        alpha = 0,
        E0 = (38.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 637,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (810000000.0, 's^-1'),
        n = 1.32,
        alpha = 0,
        E0 = (40.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 638,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (9690000000.0, 's^-1'),
        n = 0.89,
        alpha = 0,
        E0 = (35.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 639,
    label = "R2H_S;C_rad_out_Cs2;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (81200000.0, 's^-1'),
        n = 1.66,
        alpha = 0,
        E0 = (40.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 640,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (40400000000.0, 's^-1'),
        n = 0.64,
        alpha = 0,
        E0 = (33.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 641,
    label = "R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (12800000000.0, 's^-1'),
        n = 0.97,
        alpha = 0,
        E0 = (38.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 642,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (3380000000.0, 's^-1'),
        n = 0.88,
        alpha = 0,
        E0 = (38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 643,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (72500000000.0, 's^-1'),
        n = 0.6,
        alpha = 0,
        E0 = (36.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 644,
    label = "R2H_S;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1120000000.0, 's^-1'),
        n = 1.19,
        alpha = 0,
        E0 = (39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 645,
    label = "R2H_S;Cd_rad_out_double;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (2440000000.0, 's^-1'),
        n = 1.12,
        alpha = 0,
        E0 = (41.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 646,
    label = "R2H_S;C_rad_out_2H;Cd_H_out_doubleC",
    kinetics = ArrheniusEP(
        A = (268000000000.0, 's^-1'),
        n = 0.63,
        alpha = 0,
        E0 = (62.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 647,
    label = "R2H_S;Cd_rad_out_double;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (7240000000.0, 's^-1'),
        n = 0.82,
        alpha = 0,
        E0 = (37.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 648,
    label = "R2H_S;C_rad_out_H/OneDe;Cd_H_out_doubleC",
    kinetics = ArrheniusEP(
        A = (93800000000.0, 's^-1'),
        n = 0.71,
        alpha = 0,
        E0 = (62.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 649,
    label = "R2H_S;Cd_rad_out_double;Cs_H_out_OneDe",
    kinetics = ArrheniusEP(
        A = (16700000000.0, 's^-1'),
        n = 0.79,
        alpha = 0,
        E0 = (35.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 650,
    label = "R2H_S;C_rad_out_OneDe/Cs;Cd_H_out_doubleC",
    kinetics = ArrheniusEP(
        A = (1030000000.0, 's^-1'),
        n = 1.31,
        alpha = 0,
        E0 = (62.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 651,
    label = "R2H_S;C_rad_out_H/OneDe;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (2060000000.0, 's^-1'),
        n = 1.22,
        alpha = 0,
        E0 = (47.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 652,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (141000000.0, 's^-1'),
        n = 1.28,
        alpha = 0,
        E0 = (27.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 653,
    label = "R2H_S;C_rad_out_H/OneDe;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (34500000000.0, 's^-1'),
        n = 0.75,
        alpha = 0,
        E0 = (45.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 654,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (8410000000.0, 's^-1'),
        n = 0.35,
        alpha = 0,
        E0 = (29.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 655,
    label = "R2H_S;C_rad_out_H/OneDe;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1010000000000.0, 's^-1'),
        n = 0.33,
        alpha = 0,
        E0 = (42.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 656,
    label = "R2H_S;C_rad_out_Cs2;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (147000000.0, 's^-1'),
        n = 1.27,
        alpha = 0,
        E0 = (30.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 657,
    label = "R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (769000000.0, 's^-1'),
        n = 1.31,
        alpha = 0,
        E0 = (48.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
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
        A = (4890000000.0, 's^-1'),
        n = 0.81,
        alpha = 0,
        E0 = (25.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 659,
    label = "R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (21300000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
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
        A = (88300000000.0, 's^-1'),
        n = 0.3,
        alpha = 0,
        E0 = (29.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 661,
    label = "R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (36200000000000.0, 's^-1'),
        n = -0.14,
        alpha = 0,
        E0 = (44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
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
        A = (8200000000.0, 's^-1'),
        n = 0.65,
        alpha = 0,
        E0 = (31.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 663,
    label = "R2H_D;Cd_rad_out_singleH;Cd_H_out_singleH",
    kinetics = ArrheniusEP(
        A = (72800000000.0, 's^-1'),
        n = 0.86,
        alpha = 0,
        E0 = (45.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 664,
    label = "R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd",
    kinetics = ArrheniusEP(
        A = (324000000000.0, 's^-1'),
        n = 0.73,
        alpha = 0,
        E0 = (42.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 665,
    label = "R2H_D;Cd_rad_out_singleNd;Cd_H_out_singleH",
    kinetics = ArrheniusEP(
        A = (162000000000.0, 's^-1'),
        n = 0.8,
        alpha = 0,
        E0 = (47.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 666,
    label = "R2H_D;Cd_rad_out_singleNd;Cd_H_out_singleNd",
    kinetics = ArrheniusEP(
        A = (394000000000.0, 's^-1'),
        n = 0.69,
        alpha = 0,
        E0 = (44.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 667,
    label = "R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (4580000000.0, 's^-1'),
        n = 1.08,
        alpha = 0,
        E0 = (40.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 668,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy3",
    kinetics = ArrheniusEP(
        A = (11400000000.0, 's^-1'),
        n = 0.81,
        alpha = 0,
        E0 = (46.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 669,
    label = "R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (63300000000.0, 's^-1'),
        n = 0.65,
        alpha = 0,
        E0 = (38.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 670,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy3",
    kinetics = ArrheniusEP(
        A = (2740000000.0, 's^-1'),
        n = 0.98,
        alpha = 0,
        E0 = (46.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 671,
    label = "R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (590000000000.0, 's^-1'),
        n = 0.36,
        alpha = 0,
        E0 = (35.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 672,
    label = "R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2_cy3",
    kinetics = ArrheniusEP(
        A = (144000000.0, 's^-1'),
        n = 1.39,
        alpha = 0,
        E0 = (47.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 673,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy4",
    kinetics = ArrheniusEP(
        A = (9750000000.0, 's^-1'),
        n = 0.98,
        alpha = 0,
        E0 = (36.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 674,
    label = "R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (744000000.0, 's^-1'),
        n = 1.2,
        alpha = 0,
        E0 = (41.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 675,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy4",
    kinetics = ArrheniusEP(
        A = (5640000000.0, 's^-1'),
        n = 1,
        alpha = 0,
        E0 = (38.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 676,
    label = "R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (6560000000.0, 's^-1'),
        n = 0.81,
        alpha = 0,
        E0 = (39.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 677,
    label = "R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2_cy4",
    kinetics = ArrheniusEP(
        A = (931000000.0, 's^-1'),
        n = 1.21,
        alpha = 0,
        E0 = (38.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 678,
    label = "R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (48600000000.0, 's^-1'),
        n = 0.58,
        alpha = 0,
        E0 = (38.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 679,
    label = "R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (1070000000.0, 's^-1'),
        n = 1.19,
        alpha = 0,
        E0 = (42.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 680,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy5",
    kinetics = ArrheniusEP(
        A = (3350000000.0, 's^-1'),
        n = 0.99,
        alpha = 0,
        E0 = (33.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 681,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy5",
    kinetics = ArrheniusEP(
        A = (3290000000.0, 's^-1'),
        n = 0.89,
        alpha = 0,
        E0 = (36.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 682,
    label = "R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (10800000000.0, 's^-1'),
        n = 0.81,
        alpha = 0,
        E0 = (41.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 683,
    label = "R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2_cy5",
    kinetics = ArrheniusEP(
        A = (74800000.0, 's^-1'),
        n = 1.45,
        alpha = 0,
        E0 = (37.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 684,
    label = "R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (124000000000.0, 's^-1'),
        n = 1.47,
        alpha = 0,
        E0 = (39.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 685,
    label = "R2H_S_cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (225000000000.0, 's^-1'),
        n = 0.6,
        alpha = 0,
        E0 = (44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 686,
    label = "R2H_S_cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1720000000000.0, 's^-1'),
        n = 0.37,
        alpha = 0,
        E0 = (41.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 687,
    label = "R2H_S_cy3;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (569000000000.0, 's^-1'),
        n = 0.51,
        alpha = 0,
        E0 = (43.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 688,
    label = "R2H_S_cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1560000000000.0, 's^-1'),
        n = 0.24,
        alpha = 0,
        E0 = (39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 689,
    label = "R2H_S_cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (14900000000.0, 's^-1'),
        n = 0.79,
        alpha = 0,
        E0 = (42.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 691,
    label = "R2H_S_cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (171000000000.0, 's^-1'),
        n = 0.61,
        alpha = 0,
        E0 = (41.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 692,
    label = "R2H_S_cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (3720000000000.0, 's^-1'),
        n = 0.26,
        alpha = 0,
        E0 = (39.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 693,
    label = "R2H_S_cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (588000000000.0, 's^-1'),
        n = 0.51,
        alpha = 0,
        E0 = (41.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 694,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (576000000.0, 's^-1'),
        n = 1.17,
        alpha = 0,
        E0 = (36.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 695,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (5900000000.0, 's^-1'),
        n = 0.82,
        alpha = 0,
        E0 = (35.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 696,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (119000000.0, 's^-1'),
        n = 1.32,
        alpha = 0,
        E0 = (38.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 697,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (550000000.0, 's^-1'),
        n = 1.01,
        alpha = 0,
        E0 = (36.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 698,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (22500000000.0, 's^-1'),
        n = 0.66,
        alpha = 0,
        E0 = (32.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 699,
    label = "R3H_SS;C_rad_out_Cs2;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (3890000.0, 's^-1'),
        n = 1.77,
        alpha = 0,
        E0 = (37.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 700,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (7270000000.0, 's^-1'),
        n = 0.66,
        alpha = 0,
        E0 = (34.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 701,
    label = "R3H_SS;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (17100000.0, 's^-1'),
        n = 1.41,
        alpha = 0,
        E0 = (36.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 702,
    label = "R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (678000000.0, 's^-1'),
        n = 1,
        alpha = 0,
        E0 = (35.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 703,
    label = "R3H_DS;Cd_rad_out_singleH;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (5100000000.0, 's^-1'),
        n = 0.97,
        alpha = 0,
        E0 = (37.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 704,
    label = "R3H_SD;C_rad_out_2H;Cd_H_out_singleH",
    kinetics = ArrheniusEP(
        A = (4760, 's^-1'),
        n = 2.82,
        alpha = 0,
        E0 = (57.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""calculated BMK/cbsb7 Aaron Vandeputte""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 705,
    label = "R3H_DS;Cd_rad_out_singleH;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (9230000000.0, 's^-1'),
        n = 0.74,
        alpha = 0,
        E0 = (34.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 706,
    label = "R3H_SD;C_rad_out_H/NonDeC;Cd_H_out_singleH",
    kinetics = ArrheniusEP(
        A = (41600000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (64.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 707,
    label = "R3H_DS;Cd_rad_out_singleH;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (60400000000.0, 's^-1'),
        n = 0.59,
        alpha = 0,
        E0 = (32.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 708,
    label = "R3H_SD;C_rad_out_Cs2;Cd_H_out_singleH",
    kinetics = ArrheniusEP(
        A = (853000000.0, 's^-1'),
        n = 1.27,
        alpha = 0,
        E0 = (63.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 709,
    label = "R3H_DS;Cd_rad_out_singleNd;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (2580000000.0, 's^-1'),
        n = 1.08,
        alpha = 0,
        E0 = (38.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 710,
    label = "R3H_SD;C_rad_out_2H;Cd_H_out_singleNd",
    kinetics = ArrheniusEP(
        A = (191000000000.0, 's^-1'),
        n = 0.63,
        alpha = 0,
        E0 = (61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 711,
    label = "R3H_DS;Cd_rad_out_singleNd;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (5910000000.0, 's^-1'),
        n = 0.86,
        alpha = 0,
        E0 = (35.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 712,
    label = "R3H_SD;C_rad_out_H/NonDeC;Cd_H_out_singleNd",
    kinetics = ArrheniusEP(
        A = (39600000000.0, 's^-1'),
        n = 0.83,
        alpha = 0,
        E0 = (61.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 713,
    label = "R3H_DS;Cd_rad_out_singleNd;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (8050000000.0, 's^-1'),
        n = 0.86,
        alpha = 0,
        E0 = (33.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 714,
    label = "R3H_SD;C_rad_out_Cs2;Cd_H_out_singleNd",
    kinetics = ArrheniusEP(
        A = (60500000000.0, 's^-1'),
        n = 0.79,
        alpha = 0,
        E0 = (61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 715,
    label = "R3H_SS;Cd_rad_out_double;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (768000000.0, 's^-1'),
        n = 1.24,
        alpha = 0,
        E0 = (36.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 716,
    label = "R3H_SS;C_rad_out_2H;Cd_H_out_doubleC",
    kinetics = ArrheniusEP(
        A = (324000000.0, 's^-1'),
        n = 1.14,
        alpha = 0,
        E0 = (41.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 717,
    label = "R3H_SS;Cd_rad_out_double;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1660000000.0, 's^-1'),
        n = 0.99,
        alpha = 0,
        E0 = (33.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 718,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cd_H_out_doubleC",
    kinetics = ArrheniusEP(
        A = (33700000.0, 's^-1'),
        n = 1.41,
        alpha = 0,
        E0 = (42.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 719,
    label = "R3H_SS;Cd_rad_out_double;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (11000000000.0, 's^-1'),
        n = 0.78,
        alpha = 0,
        E0 = (31.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 720,
    label = "R3H_SS;C_rad_out_Cs2;Cd_H_out_doubleC",
    kinetics = ArrheniusEP(
        A = (3500000.0, 's^-1'),
        n = 1.68,
        alpha = 0,
        E0 = (42.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 721,
    label = "R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (3930000000.0, 's^-1'),
        n = 1.26,
        alpha = 0,
        E0 = (52.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 722,
    label = "R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (42000000000.0, 's^-1'),
        n = 0.82,
        alpha = 0,
        E0 = (49.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 723,
    label = "R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (564000000.0, 's^-1'),
        n = 1.47,
        alpha = 0,
        E0 = (53.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 724,
    label = "R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (143000000000.0, 's^-1'),
        n = 0.65,
        alpha = 0,
        E0 = (47.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 725,
    label = "R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (71200000.0, 's^-1'),
        n = 1.72,
        alpha = 0,
        E0 = (51.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 726,
    label = "R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (12100000000.0, 's^-1'),
        n = 0.91,
        alpha = 0,
        E0 = (49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 727,
    label = "R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (34600000000.0, 's^-1'),
        n = 0.76,
        alpha = 0,
        E0 = (47.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 728,
    label = "R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (61400000000.0, 's^-1'),
        n = 0.8,
        alpha = 0,
        E0 = (48.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 729,
    label = "R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1760000000.0, 's^-1'),
        n = 1.18,
        alpha = 0,
        E0 = (43.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 730,
    label = "R3H_SS;C_rad_out_H/OneDe;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (3800000000.0, 's^-1'),
        n = 0.99,
        alpha = 0,
        E0 = (48.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 731,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (166000000.0, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (29.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 732,
    label = "R3H_SS;C_rad_out_H/OneDe;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (6770000000.0, 's^-1'),
        n = 0.74,
        alpha = 0,
        E0 = (46.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 733,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (3410000000.0, 's^-1'),
        n = 0.73,
        alpha = 0,
        E0 = (30.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 734,
    label = "R3H_SS;C_rad_out_H/OneDe;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (90600000000.0, 's^-1'),
        n = 0.44,
        alpha = 0,
        E0 = (43.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 735,
    label = "R3H_SS;C_rad_out_Cs2;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (6400000.0, 's^-1'),
        n = 1.56,
        alpha = 0,
        E0 = (30.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 736,
    label = "R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (26200000000.0, 's^-1'),
        n = 0.69,
        alpha = 0,
        E0 = (35.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 737,
    label = "R3H_SS_23cy3;C_rad_out_2H;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (10400000000.0, 's^-1'),
        n = 0.71,
        alpha = 0,
        E0 = (34.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 738,
    label = "R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (316000000000.0, 's^-1'),
        n = 0.26,
        alpha = 0,
        E0 = (33.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 739,
    label = "R3H_SS_23cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (563000000.0, 's^-1'),
        n = 1.01,
        alpha = 0,
        E0 = (45.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 740,
    label = "R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (22600000000000.0, 's^-1'),
        n = 0.26,
        alpha = 0,
        E0 = (32.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 741,
    label = "R3H_SS_23cy3;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (26800000.0, 's^-1'),
        n = 1.42,
        alpha = 0,
        E0 = (46.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 742,
    label = "R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (1780000000.0, 's^-1'),
        n = 1.04,
        alpha = 0,
        E0 = (36.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 743,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy3",
    kinetics = ArrheniusEP(
        A = (9720000000.0, 's^-1'),
        n = 0.78,
        alpha = 0,
        E0 = (39.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 744,
    label = "R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (3390000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (33.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 745,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy3",
    kinetics = ArrheniusEP(
        A = (173000000.0, 's^-1'),
        n = 1.14,
        alpha = 0,
        E0 = (40.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 746,
    label = "R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (90800000000.0, 's^-1'),
        n = 0.36,
        alpha = 0,
        E0 = (31.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 747,
    label = "R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2_cy3",
    kinetics = ArrheniusEP(
        A = (3860000.0, 's^-1'),
        n = 1.65,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 748,
    label = "R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (29000000000.0, 's^-1'),
        n = 0.57,
        alpha = 0,
        E0 = (39.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 749,
    label = "R3H_SS_23cy4;C_rad_out_2H;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (3430000000.0, 's^-1'),
        n = 0.93,
        alpha = 0,
        E0 = (38.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 750,
    label = "R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (190000000000.0, 's^-1'),
        n = 0.27,
        alpha = 0,
        E0 = (37.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 751,
    label = "R3H_SS_23cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (259000000.0, 's^-1'),
        n = 1.2,
        alpha = 0,
        E0 = (39.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 752,
    label = "R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1630000000000.0, 's^-1'),
        n = -0.04,
        alpha = 0,
        E0 = (37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 753,
    label = "R3H_SS_23cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (21900000.0, 's^-1'),
        n = 1.55,
        alpha = 0,
        E0 = (40.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 754,
    label = "R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (108000000.0, 's^-1'),
        n = 1.25,
        alpha = 0,
        E0 = (39.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 755,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy4",
    kinetics = ArrheniusEP(
        A = (5090000000.0, 's^-1'),
        n = 0.84,
        alpha = 0,
        E0 = (34.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 756,
    label = "R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (305000000.0, 's^-1'),
        n = 0.99,
        alpha = 0,
        E0 = (37.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 757,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy4",
    kinetics = ArrheniusEP(
        A = (569000000.0, 's^-1'),
        n = 0.97,
        alpha = 0,
        E0 = (35.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 758,
    label = "R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (8200000000.0, 's^-1'),
        n = 0.54,
        alpha = 0,
        E0 = (35.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 759,
    label = "R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2_cy4",
    kinetics = ArrheniusEP(
        A = (34900000.0, 's^-1'),
        n = 1.38,
        alpha = 0,
        E0 = (35.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 760,
    label = "R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (68500000000.0, 's^-1'),
        n = 0.6,
        alpha = 0,
        E0 = (40.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 761,
    label = "R3H_SS_23cy5;C_rad_out_2H;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1250000000.0, 's^-1'),
        n = 0.99,
        alpha = 0,
        E0 = (34.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 762,
    label = "R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (367000000000.0, 's^-1'),
        n = 0.29,
        alpha = 0,
        E0 = (38.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 763,
    label = "R3H_SS_23cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (242000000.0, 's^-1'),
        n = 1.14,
        alpha = 0,
        E0 = (36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 764,
    label = "R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (942000000000.0, 's^-1'),
        n = 0.12,
        alpha = 0,
        E0 = (37.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 765,
    label = "R3H_SS_23cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1580000.0, 's^-1'),
        n = 1.78,
        alpha = 0,
        E0 = (39.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 766,
    label = "R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (314000000.0, 's^-1'),
        n = 1.26,
        alpha = 0,
        E0 = (41.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 767,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy5",
    kinetics = ArrheniusEP(
        A = (6900000000.0, 's^-1'),
        n = 0.82,
        alpha = 0,
        E0 = (32.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 768,
    label = "R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (425000000.0, 's^-1'),
        n = 1.01,
        alpha = 0,
        E0 = (39.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 769,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy5",
    kinetics = ArrheniusEP(
        A = (750000000.0, 's^-1'),
        n = 0.9,
        alpha = 0,
        E0 = (34.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 770,
    label = "R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (19700000000.0, 's^-1'),
        n = 0.46,
        alpha = 0,
        E0 = (37.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 771,
    label = "R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2_cy5",
    kinetics = ArrheniusEP(
        A = (221000000.0, 's^-1'),
        n = 1.04,
        alpha = 0,
        E0 = (34.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 772,
    label = "R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (8640000000.0, 's^-1'),
        n = 0.84,
        alpha = 0,
        E0 = (6.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 773,
    label = "R3H_SS_23cy3;C_rad_out_2H;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (50200000000.0, 's^-1'),
        n = 0.56,
        alpha = 0,
        E0 = (42.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 774,
    label = "R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (122000000000.0, 's^-1'),
        n = 0.4,
        alpha = 0,
        E0 = (34.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 775,
    label = "R3H_SS_23cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (4340000000.0, 's^-1'),
        n = 0.81,
        alpha = 0,
        E0 = (43.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 776,
    label = "R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (2720000000000.0, 's^-1'),
        n = -0.04,
        alpha = 0,
        E0 = (33.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 777,
    label = "R3H_SS_23cy3;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (161000000.0, 's^-1'),
        n = 1.26,
        alpha = 0,
        E0 = (42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 778,
    label = "R3H_SS_13cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (178000000000.0, 's^-1'),
        n = 0.29,
        alpha = 0,
        E0 = (54.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 779,
    label = "R3H_SS_13cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (24800000000.0, 's^-1'),
        n = 0.6,
        alpha = 0,
        E0 = (54.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 780,
    label = "R3H_SS_13cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (2660000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (51.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 781,
    label = "R3H_SS_13cy4;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (355000000000.0, 's^-1'),
        n = 0.37,
        alpha = 0,
        E0 = (51.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 782,
    label = "R3H_SS_13cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (136000000000.0, 's^-1'),
        n = 0.46,
        alpha = 0,
        E0 = (47.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 783,
    label = "R3H_SS_13cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (5720000000.0, 's^-1'),
        n = 0.86,
        alpha = 0,
        E0 = (47.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 784,
    label = "R3H_SS_13cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1100000000000.0, 's^-1'),
        n = 0.23,
        alpha = 0,
        E0 = (44.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 785,
    label = "R3H_SS_13cy5;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (60700000000.0, 's^-1'),
        n = 0.62,
        alpha = 0,
        E0 = (43.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 786,
    label = "R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (1840000000.0, 's^-1'),
        n = 1.05,
        alpha = 0,
        E0 = (41.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 787,
    label = "R3H_SS_23cy5;C_rad_out_2H;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (4510000000.0, 's^-1'),
        n = 0.86,
        alpha = 0,
        E0 = (33.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 788,
    label = "R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (5040000000.0, 's^-1'),
        n = 0.74,
        alpha = 0,
        E0 = (38.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 789,
    label = "R3H_SS_23cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1950000000.0, 's^-1'),
        n = 0.88,
        alpha = 0,
        E0 = (35.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 790,
    label = "R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (14400000000.0, 's^-1'),
        n = 0.74,
        alpha = 0,
        E0 = (37.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 791,
    label = "R3H_SS_23cy5;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (28500000.0, 's^-1'),
        n = 1.46,
        alpha = 0,
        E0 = (36.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 792,
    label = "R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (828000000.0, 's^-1'),
        n = 1.07,
        alpha = 0,
        E0 = (40.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 793,
    label = "R3H_SS_23cy4;C_rad_out_2H;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (19300000000.0, 's^-1'),
        n = 0.75,
        alpha = 0,
        E0 = (36.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 794,
    label = "R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (4410000000.0, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (38.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 795,
    label = "R3H_SS_23cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1960000000.0, 's^-1'),
        n = 0.96,
        alpha = 0,
        E0 = (38.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 796,
    label = "R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (23700000000.0, 's^-1'),
        n = 0.62,
        alpha = 0,
        E0 = (37.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 797,
    label = "R3H_SS_23cy4;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (49600000.0, 's^-1'),
        n = 1.46,
        alpha = 0,
        E0 = (39.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
)

entry(
    index = 798,
    label = "R3H_SS_OOCs;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (471000000.0, 's^-1'),
        n = 1.45,
        alpha = 0,
        E0 = (42.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
)

entry(
    index = 799,
    label = "R3H_SS_OOCs;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (666000000.0, 's^-1'),
        n = 1.28,
        alpha = 0,
        E0 = (39.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
)

entry(
    index = 800,
    label = "R3H_SS_OOCs;O_rad_out;Cs_H_out_H/(NonDeC/Cs)",
    kinetics = ArrheniusEP(
        A = (2430000000.0, 's^-1'),
        n = 1.17,
        alpha = 0,
        E0 = (39.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
)

entry(
    index = 801,
    label = "R3H_SS_OOCs;O_rad_out;Cs_H_out_H/(NonDeC/Cs/Cs)",
    kinetics = ArrheniusEP(
        A = (10700000000.0, 's^-1'),
        n = 0.98,
        alpha = 0,
        E0 = (39.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
)

entry(
    index = 802,
    label = "R3H_SS_OOCs;O_rad_out;Cs_H_out_H/(NonDeC/Cs/Cs/Cs)",
    kinetics = ArrheniusEP(
        A = (6620000000.0, 's^-1'),
        n = 1.04,
        alpha = 0,
        E0 = (39.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
)

entry(
    index = 803,
    label = "R3H_SS_OOCs;O_rad_out;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (4970000000.0, 's^-1'),
        n = 1.01,
        alpha = 0,
        E0 = (38.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
)

entry(
    index = 804,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (199000000000.0, 's^-1'),
        n = 0.15,
        alpha = 0,
        E0 = (34.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
)

entry(
    index = 805,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (638000000.0, 's^-1'),
        n = 1.06,
        alpha = 0,
        E0 = (33.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
)

entry(
    index = 806,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (506000000.0, 's^-1'),
        n = 1.2,
        alpha = 0,
        E0 = (33.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
)

entry(
    index = 807,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (200000000.0, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (30.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 808,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (981000000.0, 's^-1'),
        n = 0.88,
        alpha = 0,
        E0 = (29.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 809,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (3530000000.0, 's^-1'),
        n = 0.69,
        alpha = 0,
        E0 = (30.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 810,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (2640000000.0, 's^-1'),
        n = 0.78,
        alpha = 0,
        E0 = (27.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 811,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (9250000000.0, 's^-1'),
        n = 0.57,
        alpha = 0,
        E0 = (27.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 812,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs;O_rad_out;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (48700000000.0, 's^-1'),
        n = 0.35,
        alpha = 0,
        E0 = (26.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 813,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (1690000.0, 's^-1'),
        n = 1.55,
        alpha = 0,
        E0 = (21.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
)

entry(
    index = 814,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (6780000.0, 's^-1'),
        n = 1.35,
        alpha = 0,
        E0 = (20.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
)

entry(
    index = 815,
    label = "R5H_SSSS_OO(Cs/Cs/Cs)Cs;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (43500000.0, 's^-1'),
        n = 1.12,
        alpha = 0,
        E0 = (21.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
)

entry(
    index = 816,
    label = "R5H_SSSS_OOCs(Cs/Cs);O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (14100000.0, 's^-1'),
        n = 1.32,
        alpha = 0,
        E0 = (21.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
)

entry(
    index = 817,
    label = "R5H_SSSS_OOCs(Cs/Cs/Cs);O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (109000000.0, 's^-1'),
        n = 1.23,
        alpha = 0,
        E0 = (21.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
)

entry(
    index = 818,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (8940000.0, 's^-1'),
        n = 1.26,
        alpha = 0,
        E0 = (18.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
)

entry(
    index = 819,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (33800000000.0, 's^-1'),
        n = 0.21,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
)

entry(
    index = 820,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (317400000.0, 's^-1'),
        n = 1.15,
        alpha = 0,
        E0 = (15.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
)

entry(
    index = 821,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (369000, 's^-1'),
        n = 1.52,
        alpha = 0,
        E0 = (20.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
)

entry(
    index = 822,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1620000.0, 's^-1'),
        n = 1.22,
        alpha = 0,
        E0 = (16.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. 
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH
""",
)

entry(
    index = 823,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1480000.0, 's^-1'),
        n = 1.22,
        alpha = 0,
        E0 = (13.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH
""",
)

entry(
    index = 824,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (90600, 's^-1'),
        n = 1.51,
        alpha = 0,
        E0 = (19.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH
""",
)

entry(
    index = 825,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1370000.0, 's^-1'),
        n = 0.99,
        alpha = 0,
        E0 = (18.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. 
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH
""",
)

entry(
    index = 826,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (562000, 's^-1'),
        n = 1.09,
        alpha = 0,
        E0 = (14.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 850,
    label = "R3H_SS_OOCs;O_rad_out;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (300000000.0, 's^-1'),
        n = 1.23,
        alpha = 0,
        E0 = (36.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 851,
    label = "R3H_SS_OOCs;O_rad_out;Cs_H_out_NDMustO",
    kinetics = ArrheniusEP(
        A = (300000000.0, 's^-1'),
        n = 1.23,
        alpha = 0,
        E0 = (36.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 852,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (161000000.0, 's^-1'),
        n = 1.09,
        alpha = 0,
        E0 = (26.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 855,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_NDMustO",
    kinetics = ArrheniusEP(
        A = (5290000000.0, 's^-1'),
        n = 0.75,
        alpha = 0,
        E0 = (24.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 855,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (920000000.0, 's^-1'),
        n = 0.82,
        alpha = 0,
        E0 = (26.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 856,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_NDMustO",
    kinetics = ArrheniusEP(
        A = (118000000000.0, 's^-1'),
        n = 0.51,
        alpha = 0,
        E0 = (26.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 858,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (11500, 's^-1'),
        n = 2.11,
        alpha = 0,
        E0 = (15.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 863,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_NDMustO",
    kinetics = ArrheniusEP(
        A = (19000000.0, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (15.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 864,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (229000000.0, 's^-1'),
        n = 1.12,
        alpha = 0,
        E0 = (15.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 865,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_NDMustO",
    kinetics = ArrheniusEP(
        A = (117000000000.0, 's^-1'),
        n = 0.43,
        alpha = 0,
        E0 = (15.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 866,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (549, 's^-1'),
        n = 2.21,
        alpha = 0,
        E0 = (14.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 867,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_NDMustO",
    kinetics = ArrheniusEP(
        A = (72300, 's^-1'),
        n = 1.65,
        alpha = 0,
        E0 = (12.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 868,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (933000, 's^-1'),
        n = 0.75,
        alpha = 0,
        E0 = (12.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 869,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_NDMustO",
    kinetics = ArrheniusEP(
        A = (3410000.0, 's^-1'),
        n = 1.09,
        alpha = 0,
        E0 = (12.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
)

entry(
    index = 870,
    label = "R4H_SDS;C_rad_out_2H;Cd_H_out_doubleC",
    kinetics = ArrheniusEP(
        A = (1320000.0, 's^-1'),
        n = 1.6229,
        alpha = 0,
        E0 = (44.071, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
)

entry(
    index = 871,
    label = "R4H_SDS;Cd_rad_out_double;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (111000000.0, 's^-1'),
        n = 1.1915,
        alpha = 0,
        E0 = (24.7623, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
)

entry(
    index = 872,
    label = "R5H_SMSD;C_rad_out_2H;Cd_H_out_singleH",
    kinetics = ArrheniusEP(
        A = (219000, 's^-1'),
        n = 1.7613,
        alpha = 0,
        E0 = (38.275, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
)

entry(
    index = 873,
    label = "R5H_DSMS;Cd_rad_out_singleH;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (136000, 's^-1'),
        n = 1.9199,
        alpha = 0,
        E0 = (7.8968, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
)

entry(
    index = 874,
    label = "R3H_SD;C_rad_out_2H;Cd_H_out_singleDe",
    kinetics = ArrheniusEP(
        A = (15900000.0, 's^-1'),
        n = 1.4638,
        alpha = 0,
        E0 = (66.3163, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
)

entry(
    index = 875,
    label = "R3H_DS;Cd_rad_out_singleDe;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (1283710000.0, 's^-1'),
        n = 1.0541,
        alpha = 0,
        E0 = (46.1467, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
)

entry(
    index = 876,
    label = "R4H_SDS;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1110000.0, 's^-1', '*|/', 3),
        n = 1.78,
        alpha = 0,
        E0 = (27.18, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 calculations.""",
    longDesc = 
u"""
MHS CBS-QB3 calculations for CH3-CH2-CH=CH-O* == CH3-C*H-CH=CH-OH.  
Product is the cis configuration because TS is also cis.  
Note--this only affects the tunneling correction (b/c in products).  
Only methyl rotor was considered for TS.
""",
)

entry(
    index = 877,
    label = "R5H_SSSD;O_rad_out;Cd_H_out_singleH",
    kinetics = ArrheniusEP(
        A = (1234000.0, 's^-1', '*|/', 3),
        n = 1.554,
        alpha = 0,
        E0 = (26.636, 'kcal/mol', '+|-', 2),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""MRH CBS-QB3 calculations w/1d h.r. corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations with 1-d hindered rotor corrections for CH2=CH-CH2-OO => CH=CH-CH2-OOH

Previous RMG estimate for this reaction was an "Average of average" estimate.  This reaction was of
interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => C2H2+CH2O+OH.  The high-p
limit kinetics were necessary to estimate a k(T,P) for this PES.

Reactant: 2 hindered rotors were considered (the OO and CH2OO torsions)
TS: 0 hindered rotors were considered (MRH did not think 1-d separable rotor approximation was valid
	for cyclic TS)
Product: 3 hindered rotors were considered (the HO, HOO, and HOOCH2 torsions)

All external symmetry numbers were set equal to one.  The k(T) was calculated from 600 - 2000 K,
in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.468e+06 * (T/1K)^1.554 * exp(-26.636 kcal/mol / RT) cm3/mol/s.
The number appearing in the database has been divided by two to account for the reaction path degeneracy.
""",
)

entry(
    index = 878,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_OOH/H",
    kinetics = ArrheniusEP(
        A = (2470000000000.0, 's^-1'),
        n = -0.24,
        alpha = 0,
        E0 = (28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 879,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_OOH/Cs",
    kinetics = ArrheniusEP(
        A = (276000000.0, 's^-1'),
        n = 1.2,
        alpha = 0,
        E0 = (25.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 880,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/H",
    kinetics = ArrheniusEP(
        A = (12200000.0, 's^-1'),
        n = 1.6,
        alpha = 0,
        E0 = (27.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 881,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/Cs",
    kinetics = ArrheniusEP(
        A = (175000000.0, 's^-1'),
        n = 1.7,
        alpha = 0,
        E0 = (26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 882,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_OOH/H",
    kinetics = ArrheniusEP(
        A = (25900, 's^-1'),
        n = 1.9,
        alpha = 0,
        E0 = (18.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 883,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/H",
    kinetics = ArrheniusEP(
        A = (5490, 's^-1'),
        n = 2.4,
        alpha = 0,
        E0 = (19.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 884,
    label = "R5H_SSSS_OOCs(Cs/Cs/Cs);O_rad_out;Cs_H_out_OOH/H",
    kinetics = ArrheniusEP(
        A = (6.5, 's^-1'),
        n = 3.6,
        alpha = 0,
        E0 = (17.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 885,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_OOH/Cs",
    kinetics = ArrheniusEP(
        A = (57.9, 's^-1'),
        n = 2.9,
        alpha = 0,
        E0 = (17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 886,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/Cs",
    kinetics = ArrheniusEP(
        A = (175, 's^-1'),
        n = 3.1,
        alpha = 0,
        E0 = (17.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 887,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_OOH/H",
    kinetics = ArrheniusEP(
        A = (2380, 's^-1'),
        n = 1.7,
        alpha = 0,
        E0 = (16.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 888,
    label = "R6H_SSSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/H",
    kinetics = ArrheniusEP(
        A = (628, 's^-1'),
        n = 2.2,
        alpha = 0,
        E0 = (17.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 889,
    label = "R6H_SSSSS_OOCCC(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs",
    kinetics = ArrheniusEP(
        A = (377, 's^-1'),
        n = 2.2,
        alpha = 0,
        E0 = (15.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 890,
    label = "R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs",
    kinetics = ArrheniusEP(
        A = (254, 's^-1'),
        n = 2.6,
        alpha = 0,
        E0 = (16.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 891,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_OOH/H",
    kinetics = ArrheniusEP(
        A = (557, 's^-1'),
        n = 1.8,
        alpha = 0,
        E0 = (16.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 892,
    label = "R7H_OOCCCC(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs",
    kinetics = ArrheniusEP(
        A = (2000, 's^-1'),
        n = 1.9,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
)

entry(
    index = 893,
    label = "R5H_CCCC_O;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (40000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7.61, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of primary H (per H atom)""",
    longDesc = 
u"""

""",
)

entry(
    index = 894,
    label = "R5H_CCCC_O;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (40000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (6.15, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of secondary H (per H atom)""",
    longDesc = 
u"""

""",
)

entry(
    index = 895,
    label = "R5H_CCCC_O;O_rad_out;Cs_H_out",
    kinetics = ArrheniusEP(
        A = (40000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of tertiary H""",
    longDesc = 
u"""

""",
)

entry(
    index = 901,
    label = "R2H_S;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (0.0722, 's^-1'),
        n = 4.07,
        alpha = 0,
        E0 = (20.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 903,
    label = "R3H_SS_S;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (0.000821, 's^-1'),
        n = 4.56,
        alpha = 0,
        E0 = (16.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 904,
    label = "R4H_SSS;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (373000000.0, 's^-1'),
        n = 0.882,
        alpha = 0,
        E0 = (5.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 905,
    label = "R4H_SSS;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (19100000.0, 's^-1'),
        n = 1.26,
        alpha = 0,
        E0 = (7.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 906,
    label = "R4H_SSS;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (118, 's^-1'),
        n = 2.8,
        alpha = 0,
        E0 = (7.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 907,
    label = "R4H_SSS;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (21000000.0, 's^-1'),
        n = 1.28,
        alpha = 0,
        E0 = (7.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 908,
    label = "R5H_SSSS;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (22100000000.0, 's^-1'),
        n = 0.214,
        alpha = 0,
        E0 = (2.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 909,
    label = "R5H_SSSS;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (1820000000.0, 's^-1'),
        n = 0.586,
        alpha = 0,
        E0 = (3.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 910,
    label = "R5H_SSSS;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (19400000000.0, 's^-1'),
        n = 0.329,
        alpha = 0,
        E0 = (3.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 911,
    label = "R5H_SSSS;C_rad_out_2H;S_H_out",
    kinetics = ArrheniusEP(
        A = (18800000000.0, 's^-1'),
        n = 0.269,
        alpha = 0,
        E0 = (3.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 1001,
    label = "R4H_SSS_CsCsSCs;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (17000000.0, 's^-1'),
        n = 1.06,
        alpha = 0,
        E0 = (17.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""

""",
)

entry(
    index = 1002,
    label = "R5H_SSSS_CsCsCsSCs;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (214000, 's^-1'),
        n = 1.33,
        alpha = 0,
        E0 = (10.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""

""",
)

entry(
    index = 1003,
    label = "R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeS",
    kinetics = ArrheniusEP(
        A = (696000, 's^-1'),
        n = 1.95,
        alpha = 0,
        E0 = (19.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""

""",
)

entry(
    index = 1004,
    label = "R5H_SSSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeS",
    kinetics = ArrheniusEP(
        A = (531000, 's^-1'),
        n = 1.58,
        alpha = 0,
        E0 = (12.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""

""",
)

entry(
    index = 1005,
    label = "R3H_SS;O_rad_out;S_H_out",
    kinetics = ArrheniusEP(
        A = (499000000000.0, 's^-1'),
        n = 0.26,
        alpha = 0,
        E0 = (15.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""

""",
)

entry(
    index = 1006,
    label = "R3H_SS;C_rad_out_H/NonDeC;O_H_out",
    kinetics = ArrheniusEP(
        A = (5.71, 's^-1'),
        n = 3.021,
        alpha = 0,
        E0 = (25.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""

""",
)

entry(
    index = 1007,
    label = "R4H_SSS;C_rad_out_H/NonDeO;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (27900, 's^-1'),
        n = 1.97,
        alpha = 0,
        E0 = (23.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""

""",
)

entry(
    index = 1008,
    label = "R2H_S;C_rad_out_H/NonDeC;O_H_out",
    kinetics = ArrheniusEP(
        A = (4500, 's^-1'),
        n = 2.62,
        alpha = 0,
        E0 = (30.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""

""",
)

entry(
    index = 1009,
    label = "R4H_SSS;C_rad_out_H/NonDeC;O_H_out",
    kinetics = ArrheniusEP(
        A = (2960, 's^-1'),
        n = 2.11,
        alpha = 0,
        E0 = (20.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""

""",
)

entry(
    index = 1010,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (1000, 's^-1'),
        n = 2.705,
        alpha = 0,
        E0 = (34.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""

""",
)

entry(
    index = 1011,
    label = "R4H_SSS;C_rad_out_2H;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (152, 's^-1'),
        n = 2.77,
        alpha = 0,
        E0 = (14.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""

""",
)

entry(
    index = 1012,
    label = "R5H_CCCC_O;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (20700, 's^-1'),
        n = 1.78,
        alpha = 0,
        E0 = (5.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""

""",
)

entry(
    index = 1013,
    label = "R2H_S;O_rad_out;Cs_H_out_H/(NonDeC/Cs)",
    kinetics = ArrheniusEP(
        A = (76500, 's^-1'),
        n = 2.26,
        alpha = 0,
        E0 = (21.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""

""",
)

entry(
    index = 1014,
    label = "R4H_SSS;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (105000, 's^-1'),
        n = 1.76,
        alpha = 0,
        E0 = (12.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""

""",
)

entry(
    index = 1015,
    label = "R3H_SS;O_rad_out;Cs_H_out_H/(NonDeC/Cs)",
    kinetics = ArrheniusEP(
        A = (9000, 's^-1'),
        n = 2.287,
        alpha = 0,
        E0 = (20.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Obtained by reversing rate rule 1006""",
    longDesc = 
u"""

""",
)

entry(
    index = 1016,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_H/(NonDeC/Cs)",
    kinetics = ArrheniusEP(
        A = (150000, 's^-1'),
        n = 2.15,
        alpha = 0,
        E0 = (32.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Obtained by reversing rate rule 1010""",
    longDesc = 
u"""

""",
)

entry(
    index = 1017,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (9.46e-19, 's^-1'),
        n = 8.97,
        alpha = 0,
        E0 = (15.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

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
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
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
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
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
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 1021,
    label = "R4H_SSS;C_rad_out_2H;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (0.000113, 's^-1'),
        n = 4.37,
        alpha = 0,
        E0 = (8.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
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
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 1023,
    label = "R5H_SSSS;C_rad_out_2H;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (46.1, 's^-1'),
        n = 3.21,
        alpha = 0,
        E0 = (6.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
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
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 1025,
    label = "R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (0.251, 's^-1'),
        n = 3.86,
        alpha = 0,
        E0 = (9.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 1027,
    label = "R6H_SSSSS;C_rad_out_2H;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (46.1, 's^-1'),
        n = 3.21,
        alpha = 0,
        E0 = (6.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
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
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
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
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 1031,
    label = "R6H_SSSSS_bicyclopentane;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe",
    kinetics = ArrheniusEP(
        A = (10500, 's^-1'),
        n = 2.14,
        alpha = 0,
        E0 = (15.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 1032,
    label = "R4H_SMS;Y_rad_out;XH_out",
    kinetics = ArrheniusEP(
        A = (10000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (100, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""estimate""",
    longDesc = 
u"""

""",
)

entry(
    index = 1033,
    label = "R4H_SDS;C_rad_out_H/NonDeC;Cs_H_out_H/(NonDeC/Cs)",
    kinetics = ArrheniusEP(
        A = (10000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (100, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""estimate""",
    longDesc = 
u"""

""",
)

entry(
    index = 1034,
    label = "R6H_SSSSS;C_rad_out_single;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (428000000000.0, 's^-1'),
        n = -1.05,
        alpha = 0,
        E0 = (11.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""

""",
)

entry(
    index = 1035,
    label = "R6H_SSSSS;C_rad_out_single;Cs_H_out_1H",
    kinetics = ArrheniusEP(
        A = (13600000000.0, 's^-1'),
        n = -0.66,
        alpha = 0,
        E0 = (14.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""

""",
)

entry(
    index = 1036,
    label = "R3H_SS_OOCs;O_rad_out;Cs_H_out_H/Cd",
    kinetics = ArrheniusEP(
        A = (16600000.0, 's^-1'),
        n = 1.69,
        alpha = 0,
        E0 = (38.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 1037,
    label = "R4H_SSS_OOCsCd;O_rad_out;Cd_H_out_doubleC",
    kinetics = ArrheniusEP(
        A = (274, 's^-1'),
        n = 3.09,
        alpha = 0,
        E0 = (34.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 1038,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_H/(NonDeC/O)",
    kinetics = ArrheniusEP(
        A = (1.2e-16, 's^-1'),
        n = 7.98,
        alpha = 0,
        E0 = (25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1039,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (4.15e-15, 's^-1'),
        n = 8.11,
        alpha = 0,
        E0 = (28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1040,
    label = "R4H_SSS;C_rad_out_2H;O_H_out",
    kinetics = ArrheniusEP(
        A = (8.6e-09, 's^-1'),
        n = 5.55,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1041,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (2.7e-20, 's^-1'),
        n = 9.13,
        alpha = 0,
        E0 = (26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1042,
    label = "R3H_SS;C_rad_out_H/NonDeC;O_H_out",
    kinetics = ArrheniusEP(
        A = (3e-10, 's^-1'),
        n = 6.82,
        alpha = 0,
        E0 = (25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1043,
    label = "R2H_S;C_rad_out_H/NonDeO;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (4.7e-19, 's^-1'),
        n = 8.84,
        alpha = 0,
        E0 = (30, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1044,
    label = "R3H_SS;C_rad_out_H/NonDeO;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (2e-15, 's^-1'),
        n = 8.23,
        alpha = 0,
        E0 = (34.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1045,
    label = "R3H_SS;O_rad_out;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (7e-08, 's^-1'),
        n = 6.3,
        alpha = 0,
        E0 = (19.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1046,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (5e-18, 's^-1'),
        n = 8.38,
        alpha = 0,
        E0 = (27.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1047,
    label = "R2H_S;C_rad_out_2H;O_H_out",
    kinetics = ArrheniusEP(
        A = (25600, 's^-1'),
        n = 2.36,
        alpha = 0,
        E0 = (33.1, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron BMK/cbsb7 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1048,
    label = "R4H_SSS;C_rad_out_2H;O_H_out",
    kinetics = ArrheniusEP(
        A = (9790, 's^-1'),
        n = 1.91,
        alpha = 0,
        E0 = (16.7, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron BMK/cbsb7 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1049,
    label = "R4H_SSS;O_rad_out;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (16800, 's^-1'),
        n = 2.06,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron BMK/cbsb7 with 1-dHR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1050,
    label = "R2H_S;C_rad_out_H/NonDeO;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (14700000000000.0, 's^-1', '+|-', 2),
        n = 0,
        alpha = 0,
        E0 = (45, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1051,
    label = "R2H_S;C_rad_out_H/NonDeC;O_H_out",
    kinetics = ArrheniusEP(
        A = (30000000000000.0, 's^-1', '+|-', 2),
        n = 0,
        alpha = 0,
        E0 = (37, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1052,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeO",
    kinetics = ArrheniusEP(
        A = (18500000000000.0, 's^-1', '+|-', 2),
        n = -0.1,
        alpha = 0,
        E0 = (37.85, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1800, 'K'),
    ),
    rank = 3,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1053,
    label = "R2H_S;O_rad_out;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (215000000000000.0, 's^-1', '+|-', 2),
        n = -0.27,
        alpha = 0,
        E0 = (27.24, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1800, 'K'),
    ),
    rank = 3,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""

""",
)

entry(
    index = 1054,
    label = "R3H_SS;O_rad_out;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (172000000.0, 's^-1', '+|-', 2),
        n = 1.31,
        alpha = 0,
        E0 = (24.94, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1800, 'K'),
    ),
    rank = 3,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""

""",
)

