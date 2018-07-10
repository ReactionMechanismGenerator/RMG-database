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
    index = 615,
    label = "R2H_S;C_rad_out_single;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (5.48e+08, 's^-1'),
        n = 1.62,
        alpha = 0,
        E0 = (38.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
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
        A = (1.39e+09, 's^-1'),
        n = 0.98,
        alpha = 0,
        E0 = (33.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green
""",
)

entry(
    index = 619,
    label = "R4H_SSS;C_rad_out_single;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (2.54e+09, 's^-1'),
        n = 0.35,
        alpha = 0,
        E0 = (19.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.
""",
)

entry(
    index = 622,
    label = "R5H_SSSS;C_rad_out_single;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (4.28e+11, 's^-1'),
        n = -1.05,
        alpha = 0,
        E0 = (11.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green
""",
)

entry(
    index = 636,
    label = "R2H_S;C_rad_out_2H;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (4.45e+09, 's^-1'),
        n = 1.12,
        alpha = 0,
        E0 = (38.7, 'kcal/mol'),
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
    index = 641,
    label = "R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.28e+10, 's^-1'),
        n = 0.97,
        alpha = 0,
        E0 = (38.5, 'kcal/mol'),
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
    index = 642,
    label = "R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (3.38e+09, 's^-1'),
        n = 0.88,
        alpha = 0,
        E0 = (38, 'kcal/mol'),
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
    index = 663,
    label = "R2H_D;Cd_rad_out_singleH;Cd_H_out_singleH",
    kinetics = ArrheniusEP(
        A = (7.28e+10, 's^-1'),
        n = 0.86,
        alpha = 0,
        E0 = (45.7, 'kcal/mol'),
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
    index = 666,
    label = "R2H_D;Cd_rad_out_singleNd;Cd_H_out_singleNd",
    kinetics = ArrheniusEP(
        A = (3.94e+11, 's^-1'),
        n = 0.69,
        alpha = 0,
        E0 = (44.6, 'kcal/mol'),
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
    index = 685,
    label = "R2H_S_cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (2.25e+11, 's^-1'),
        n = 0.6,
        alpha = 0,
        E0 = (44, 'kcal/mol'),
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
    index = 686,
    label = "R2H_S_cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.72e+12, 's^-1'),
        n = 0.37,
        alpha = 0,
        E0 = (41.6, 'kcal/mol'),
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
    index = 687,
    label = "R2H_S_cy3;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (5.69e+11, 's^-1'),
        n = 0.51,
        alpha = 0,
        E0 = (43.3, 'kcal/mol'),
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
    index = 688,
    label = "R2H_S_cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.56e+12, 's^-1'),
        n = 0.24,
        alpha = 0,
        E0 = (39, 'kcal/mol'),
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
    index = 689,
    label = "R2H_S_cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.49e+10, 's^-1'),
        n = 0.79,
        alpha = 0,
        E0 = (42.6, 'kcal/mol'),
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
    index = 691,
    label = "R2H_S_cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.71e+11, 's^-1'),
        n = 0.61,
        alpha = 0,
        E0 = (41.9, 'kcal/mol'),
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
    index = 692,
    label = "R2H_S_cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (3.72e+12, 's^-1'),
        n = 0.26,
        alpha = 0,
        E0 = (39.2, 'kcal/mol'),
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
    index = 693,
    label = "R2H_S_cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (5.88e+11, 's^-1'),
        n = 0.51,
        alpha = 0,
        E0 = (41.7, 'kcal/mol'),
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
    index = 694,
    label = "R3H_SS;C_rad_out_2H;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (5.76e+08, 's^-1'),
        n = 1.17,
        alpha = 0,
        E0 = (36.7, 'kcal/mol'),
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
    index = 697,
    label = "R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (5.5e+08, 's^-1'),
        n = 1.01,
        alpha = 0,
        E0 = (36.4, 'kcal/mol'),
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
    index = 702,
    label = "R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (6.78e+08, 's^-1'),
        n = 1,
        alpha = 0,
        E0 = (35.3, 'kcal/mol'),
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
    index = 721,
    label = "R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (3.93e+09, 's^-1'),
        n = 1.26,
        alpha = 0,
        E0 = (52.9, 'kcal/mol'),
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
    index = 726,
    label = "R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.21e+10, 's^-1'),
        n = 0.91,
        alpha = 0,
        E0 = (49, 'kcal/mol'),
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
    index = 729,
    label = "R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.76e+09, 's^-1'),
        n = 1.18,
        alpha = 0,
        E0 = (43.8, 'kcal/mol'),
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
    index = 736,
    label = "R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (2.62e+10, 's^-1'),
        n = 0.69,
        alpha = 0,
        E0 = (35.1, 'kcal/mol'),
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
    index = 737,
    label = "R3H_SS_23cy3;C_rad_out_2H;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.04e+10, 's^-1'),
        n = 0.71,
        alpha = 0,
        E0 = (34.9, 'kcal/mol'),
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
    index = 738,
    label = "R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (3.16e+11, 's^-1'),
        n = 0.26,
        alpha = 0,
        E0 = (33.5, 'kcal/mol'),
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
    index = 739,
    label = "R3H_SS_23cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (5.63e+08, 's^-1'),
        n = 1.01,
        alpha = 0,
        E0 = (45.4, 'kcal/mol'),
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
    index = 740,
    label = "R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (2.26e+13, 's^-1'),
        n = 0.26,
        alpha = 0,
        E0 = (32.1, 'kcal/mol'),
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
    index = 741,
    label = "R3H_SS_23cy3;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (2.68e+07, 's^-1'),
        n = 1.42,
        alpha = 0,
        E0 = (46.3, 'kcal/mol'),
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
    index = 748,
    label = "R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (2.9e+10, 's^-1'),
        n = 0.57,
        alpha = 0,
        E0 = (39.8, 'kcal/mol'),
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
    index = 749,
    label = "R3H_SS_23cy4;C_rad_out_2H;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (3.43e+09, 's^-1'),
        n = 0.93,
        alpha = 0,
        E0 = (38.3, 'kcal/mol'),
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
    index = 750,
    label = "R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.9e+11, 's^-1'),
        n = 0.27,
        alpha = 0,
        E0 = (37.9, 'kcal/mol'),
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
    index = 751,
    label = "R3H_SS_23cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (2.59e+08, 's^-1'),
        n = 1.2,
        alpha = 0,
        E0 = (39.7, 'kcal/mol'),
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
    index = 752,
    label = "R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.63e+12, 's^-1'),
        n = -0.04,
        alpha = 0,
        E0 = (37, 'kcal/mol'),
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
    index = 753,
    label = "R3H_SS_23cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (2.19e+07, 's^-1'),
        n = 1.55,
        alpha = 0,
        E0 = (40.1, 'kcal/mol'),
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
    index = 760,
    label = "R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (6.85e+10, 's^-1'),
        n = 0.6,
        alpha = 0,
        E0 = (40.8, 'kcal/mol'),
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
    index = 761,
    label = "R3H_SS_23cy5;C_rad_out_2H;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.25e+09, 's^-1'),
        n = 0.99,
        alpha = 0,
        E0 = (34.8, 'kcal/mol'),
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
    index = 762,
    label = "R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (3.67e+11, 's^-1'),
        n = 0.29,
        alpha = 0,
        E0 = (38.2, 'kcal/mol'),
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
    index = 763,
    label = "R3H_SS_23cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (2.42e+08, 's^-1'),
        n = 1.14,
        alpha = 0,
        E0 = (36, 'kcal/mol'),
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
    index = 764,
    label = "R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (9.42e+11, 's^-1'),
        n = 0.12,
        alpha = 0,
        E0 = (37.4, 'kcal/mol'),
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
    index = 765,
    label = "R3H_SS_23cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.58e+06, 's^-1'),
        n = 1.78,
        alpha = 0,
        E0 = (39.7, 'kcal/mol'),
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
    index = 772,
    label = "R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (8.64e+09, 's^-1'),
        n = 0.84,
        alpha = 0,
        E0 = (6.5, 'kcal/mol'),
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
    index = 773,
    label = "R3H_SS_23cy3;C_rad_out_2H;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (5.02e+10, 's^-1'),
        n = 0.56,
        alpha = 0,
        E0 = (42.7, 'kcal/mol'),
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
    index = 774,
    label = "R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.22e+11, 's^-1'),
        n = 0.4,
        alpha = 0,
        E0 = (34.8, 'kcal/mol'),
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
    index = 775,
    label = "R3H_SS_23cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (4.34e+09, 's^-1'),
        n = 0.81,
        alpha = 0,
        E0 = (43.6, 'kcal/mol'),
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
    index = 776,
    label = "R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (2.72e+12, 's^-1'),
        n = -0.04,
        alpha = 0,
        E0 = (33.4, 'kcal/mol'),
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
    index = 777,
    label = "R3H_SS_23cy3;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.61e+08, 's^-1'),
        n = 1.26,
        alpha = 0,
        E0 = (42, 'kcal/mol'),
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
    index = 778,
    label = "R3H_SS_13cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.78e+11, 's^-1'),
        n = 0.29,
        alpha = 0,
        E0 = (54.3, 'kcal/mol'),
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
    index = 779,
    label = "R3H_SS_13cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (2.48e+10, 's^-1'),
        n = 0.6,
        alpha = 0,
        E0 = (54.6, 'kcal/mol'),
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
    index = 780,
    label = "R3H_SS_13cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (2.66e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (51.4, 'kcal/mol'),
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
    index = 781,
    label = "R3H_SS_13cy4;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (3.55e+11, 's^-1'),
        n = 0.37,
        alpha = 0,
        E0 = (51.7, 'kcal/mol'),
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
    index = 782,
    label = "R3H_SS_13cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (1.36e+11, 's^-1'),
        n = 0.46,
        alpha = 0,
        E0 = (47.2, 'kcal/mol'),
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
    index = 783,
    label = "R3H_SS_13cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (5.72e+09, 's^-1'),
        n = 0.86,
        alpha = 0,
        E0 = (47.2, 'kcal/mol'),
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
    index = 784,
    label = "R3H_SS_13cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.1e+12, 's^-1'),
        n = 0.23,
        alpha = 0,
        E0 = (44.4, 'kcal/mol'),
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
    index = 785,
    label = "R3H_SS_13cy5;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (6.07e+10, 's^-1'),
        n = 0.62,
        alpha = 0,
        E0 = (43.4, 'kcal/mol'),
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
    index = 786,
    label = "R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (1.84e+09, 's^-1'),
        n = 1.05,
        alpha = 0,
        E0 = (41.1, 'kcal/mol'),
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
    index = 787,
    label = "R3H_SS_23cy5;C_rad_out_2H;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (4.51e+09, 's^-1'),
        n = 0.86,
        alpha = 0,
        E0 = (33.5, 'kcal/mol'),
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
    index = 788,
    label = "R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (5.04e+09, 's^-1'),
        n = 0.74,
        alpha = 0,
        E0 = (38.8, 'kcal/mol'),
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
    index = 789,
    label = "R3H_SS_23cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.95e+09, 's^-1'),
        n = 0.88,
        alpha = 0,
        E0 = (35.1, 'kcal/mol'),
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
    index = 790,
    label = "R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.44e+10, 's^-1'),
        n = 0.74,
        alpha = 0,
        E0 = (37.5, 'kcal/mol'),
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
    index = 791,
    label = "R3H_SS_23cy5;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (2.85e+07, 's^-1'),
        n = 1.46,
        alpha = 0,
        E0 = (36.4, 'kcal/mol'),
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
    index = 792,
    label = "R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (8.28e+08, 's^-1'),
        n = 1.07,
        alpha = 0,
        E0 = (40.7, 'kcal/mol'),
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
    index = 793,
    label = "R3H_SS_23cy4;C_rad_out_2H;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.93e+10, 's^-1'),
        n = 0.75,
        alpha = 0,
        E0 = (36.5, 'kcal/mol'),
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
    index = 794,
    label = "R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    kinetics = ArrheniusEP(
        A = (4.41e+09, 's^-1'),
        n = 0.77,
        alpha = 0,
        E0 = (38.8, 'kcal/mol'),
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
    index = 795,
    label = "R3H_SS_23cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (1.96e+09, 's^-1'),
        n = 0.96,
        alpha = 0,
        E0 = (38.4, 'kcal/mol'),
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
    index = 796,
    label = "R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (2.37e+10, 's^-1'),
        n = 0.62,
        alpha = 0,
        E0 = (37.6, 'kcal/mol'),
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
    index = 797,
    label = "R3H_SS_23cy4;C_rad_out_Cs2;Cs_H_out_Cs2",
    kinetics = ArrheniusEP(
        A = (4.96e+07, 's^-1'),
        n = 1.46,
        alpha = 0,
        E0 = (39.4, 'kcal/mol'),
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
    rank = 10,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
)

entry(
    index = 1032,
    label = "R4H_SMS;Y_rad_out;XH_out",
    kinetics = ArrheniusEP(
        A = (1e+10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (100, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""estimate""",
)

entry(
    index = 1034,
    label = "R6H_SSSSS;C_rad_out_single;Cs_H_out_2H",
    kinetics = ArrheniusEP(
        A = (4.28e+11, 's^-1'),
        n = -1.05,
        alpha = 0,
        E0 = (11.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
)

entry(
    index = 1057,
    label = "R4H_MMS;Cd_rad_out;Cs_H_out",
    kinetics = ArrheniusEP(
        A = (1e-10, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Aaron Vandeputte guess""",
)

