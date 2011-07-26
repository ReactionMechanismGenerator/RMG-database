#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/rules"
shortDesc = u""
longDesc = u"""

"""
recommended = True

entry(
    index = 614,
    label = "RnH;Y_rad_out;XH_out",
    group1 = "OR{R2H, R3H, R4H, R5H, R6H, R7H}",
    group2 = 
"""
1  *1 R!H 1
""",
    group3 = 
"""
1  *2 R!H 0 {2,S}
2  *3 H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (25,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 0,
    shortDesc = u"""default""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 615,
    label = "R2H_S;C_rad_out_single;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *2 R!H 0 {1,S} {3,S}
3  *3 H 0 {2,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.48e+08,"s^-1"),
        n = 1.62,
        alpha = 0,
        E0 = (38.76,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 616,
    label = "R2H_S;C_rad_out_single;Cs_H_out_1H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *2 R!H 0 {1,S} {3,S}
3  *3 H 0 {2,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.59e+08,"s^-1"),
        n = 1.39,
        alpha = 0,
        E0 = (39.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 617,
    label = "R3H_SS;C_rad_out_single;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.39e+09,"s^-1"),
        n = 0.98,
        alpha = 0,
        E0 = (33.76,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 618,
    label = "R3H_SS;C_rad_out_single;Cs_H_out_1H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.76e+09,"s^-1"),
        n = 0.76,
        alpha = 0,
        E0 = (34.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 619,
    label = "R4H_SSS;C_rad_out_single;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.54e+09,"s^-1"),
        n = 0.35,
        alpha = 0,
        E0 = (19.76,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 620,
    label = "R4H_SSS;C_rad_out_single;Cs_H_out_1H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.22e+09,"s^-1"),
        n = 0.13,
        alpha = 0,
        E0 = (20.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 621,
    label = "R4H_SSS;C_rad_out_single;Cs_H_out_noH",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.86e+10,"s^-1"),
        n = 0.58,
        alpha = 0,
        E0 = (26.19,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. 

NEEDS TO BE CHECKED
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 622,
    label = "R5H_SSSS;C_rad_out_single;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.28e+11,"s^-1"),
        n = -1.05,
        alpha = 0,
        E0 = (11.76,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 623,
    label = "R5H_SSSS;C_rad_out_single;Cs_H_out_1H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     R 0 {1,S}
3     R 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.36e+10,"s^-1"),
        n = -0.66,
        alpha = 0,
        E0 = (14.28,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 624,
    label = "R4H_SSS;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (29.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 625,
    label = "R4H_SSS;O_rad_out;Cs_H_out_1H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (26.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 626,
    label = "R4H_SSS;O_rad_out;Cs_H_out_noH",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1e+11,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (24.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 627,
    label = "R5H_SSSS;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.25e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (24.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 628,
    label = "R5H_SSSS;O_rad_out;Cs_H_out_1H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.25e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (20.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 629,
    label = "R5H_SSSS;O_rad_out;Cs_H_out_noH",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 R!H 0 {3,S} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.25e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (19.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 630,
    label = "R6H_SSSSS;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.56e+09,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (22.35,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 631,
    label = "R6H_SSSSS;O_rad_out;Cs_H_out_1H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.56e+09,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (19.05,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 632,
    label = "R6H_SSSSS;O_rad_out;Cs_H_out_noH",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4     R!H 0 {3,S} {5,S}
5  *5 R!H 0 {4,S} {6,S}
6  *2 R!H 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.56e+09,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (17.05,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 633,
    label = "R7H;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,{S,D,T,B}}
3     R!H 0 {2,{S,D,T,B}} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.95e+08,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (25.55,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 634,
    label = "R7H;O_rad_out;Cs_H_out_1H",
    group1 = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,{S,D,T,B}}
3     R!H 0 {2,{S,D,T,B}} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.95e+08,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (25.55,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 635,
    label = "R7H;O_rad_out;Cs_H_out_noH",
    group1 = 
"""
1  *1 R!H 1 {2,{S,D,T,B}}
2  *4 R!H 0 {1,{S,D,T,B}} {3,{S,D,T,B}}
3     R!H 0 {2,{S,D,T,B}} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     R!H 0 {1,S}
4     R!H 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.95e+08,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (25.55,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 5,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 636,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_2H",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.45e+09,"s^-1"),
        n = 1.12,
        alpha = 0,
        E0 = (38.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 637,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.1e+08,"s^-1"),
        n = 1.32,
        alpha = 0,
        E0 = (40.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 638,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.69e+09,"s^-1"),
        n = 0.89,
        alpha = 0,
        E0 = (35.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 639,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_2H",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.12e+07,"s^-1"),
        n = 1.66,
        alpha = 0,
        E0 = (40.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 640,
    label = "Others-R2H_S;C_rad_out_2H;Others-Cs_H_out_Cs2",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (4.04e+10,"s^-1"),
        n = 0.64,
        alpha = 0,
        E0 = (33.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 641,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.28e+10,"s^-1"),
        n = 0.97,
        alpha = 0,
        E0 = (38.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 642,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.38e+09,"s^-1"),
        n = 0.88,
        alpha = 0,
        E0 = (38,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 643,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (7.25e+10,"s^-1"),
        n = 0.6,
        alpha = 0,
        E0 = (36.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 644,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.12e+09,"s^-1"),
        n = 1.19,
        alpha = 0,
        E0 = (39,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 645,
    label = "Others-R2H_S;Cd_rad_out_double;Cs_H_out_2H",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.44e+09,"s^-1"),
        n = 1.12,
        alpha = 0,
        E0 = (41.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 646,
    label = "Others-R2H_S;C_rad_out_2H;Cd_H_out_doubleC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     Cd 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (2.68e+11,"s^-1"),
        n = 0.63,
        alpha = 0,
        E0 = (62.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 647,
    label = "Others-R2H_S;Cd_rad_out_double;Cs_H_out_H/OneDe",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.24e+09,"s^-1"),
        n = 0.82,
        alpha = 0,
        E0 = (37.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 648,
    label = "Others-R2H_S;C_rad_out_H/OneDe;Cd_H_out_doubleC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     Cd 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (9.38e+10,"s^-1"),
        n = 0.71,
        alpha = 0,
        E0 = (62.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 649,
    label = "Others-R2H_S;Cd_rad_out_double;Cs_H_out_OneDe",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.67e+10,"s^-1"),
        n = 0.79,
        alpha = 0,
        E0 = (35.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 650,
    label = "Others-R2H_S;C_rad_out_OneDe/Cs;Cd_H_out_doubleC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     Cd 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (1.03e+09,"s^-1"),
        n = 1.31,
        alpha = 0,
        E0 = (62.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 651,
    label = "Others-R2H_S;C_rad_out_H/OneDe;Cs_H_out_2H",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.06e+09,"s^-1"),
        n = 1.22,
        alpha = 0,
        E0 = (47.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 652,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_H/OneDe",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.41e+08,"s^-1"),
        n = 1.28,
        alpha = 0,
        E0 = (27.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 653,
    label = "Others-R2H_S;C_rad_out_H/OneDe;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.45e+10,"s^-1"),
        n = 0.75,
        alpha = 0,
        E0 = (45.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 654,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.41e+09,"s^-1"),
        n = 0.35,
        alpha = 0,
        E0 = (29.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 655,
    label = "Others-R2H_S;C_rad_out_H/OneDe;Others-Cs_H_out_Cs2",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.01e+12,"s^-1"),
        n = 0.33,
        alpha = 0,
        E0 = (42.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 656,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_H/OneDe",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.47e+08,"s^-1"),
        n = 1.27,
        alpha = 0,
        E0 = (30.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 657,
    label = "Others-R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_2H",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.69e+08,"s^-1"),
        n = 1.31,
        alpha = 0,
        E0 = (48.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 658,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_OneDe",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.89e+09,"s^-1"),
        n = 0.81,
        alpha = 0,
        E0 = (25.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 659,
    label = "Others-R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.13e+10,"s^-1"),
        n = 0.77,
        alpha = 0,
        E0 = (46,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 660,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_OneDe",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.83e+10,"s^-1"),
        n = 0.3,
        alpha = 0,
        E0 = (29.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 661,
    label = "Others-R2H_S;C_rad_out_OneDe/Cs;Others-Cs_H_out_Cs2",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (3.62e+13,"s^-1"),
        n = -0.14,
        alpha = 0,
        E0 = (44,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 662,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_OneDe",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
4     {Cd,Ct,Cb,CO} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.2e+09,"s^-1"),
        n = 0.65,
        alpha = 0,
        E0 = (31.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 663,
    label = "R2H_D;Cd_rad_out_singleH;Cd_H_out_singleH",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *2 Cd 0 {1,D} {3,S}
3  *3 H 0 {2,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.28e+10,"s^-1"),
        n = 0.86,
        alpha = 0,
        E0 = (45.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 664,
    label = "R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *2 Cd 0 {1,D} {3,S}
3  *3 H 0 {2,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.24e+11,"s^-1"),
        n = 0.73,
        alpha = 0,
        E0 = (42.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 665,
    label = "R2H_D;Cd_rad_out_singleNd;Cd_H_out_singleH",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *2 Cd 0 {1,D} {3,S}
3  *3 H 0 {2,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.62e+11,"s^-1"),
        n = 0.8,
        alpha = 0,
        E0 = (47.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 666,
    label = "R2H_D;Cd_rad_out_singleNd;Cd_H_out_singleNd",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *2 Cd 0 {1,D} {3,S}
3  *3 H 0 {2,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.94e+11,"s^-1"),
        n = 0.69,
        alpha = 0,
        E0 = (44.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 667,
    label = "Others-R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_2H",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {3,S}
3     Cs 0 {1,S} {2,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.58e+09,"s^-1"),
        n = 1.08,
        alpha = 0,
        E0 = (40.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 668,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy3",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {4,S}
4     Cs 0 {1,S} {3,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.14e+10,"s^-1"),
        n = 0.81,
        alpha = 0,
        E0 = (46.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 669,
    label = "Others-R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {3,S}
3     Cs 0 {1,S} {2,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.33e+10,"s^-1"),
        n = 0.65,
        alpha = 0,
        E0 = (38.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 670,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy3",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {4,S}
4     Cs 0 {1,S} {3,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.74e+09,"s^-1"),
        n = 0.98,
        alpha = 0,
        E0 = (46.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 671,
    label = "Others-R2H_S;C_rad_out_Cs2_cy3;Others-Cs_H_out_Cs2",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {3,S}
3     Cs 0 {1,S} {2,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (5.9e+11,"s^-1"),
        n = 0.36,
        alpha = 0,
        E0 = (35.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 672,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_Cs2_cy3",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {4,S}
4     Cs 0 {1,S} {3,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.44e+08,"s^-1"),
        n = 1.39,
        alpha = 0,
        E0 = (47.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 673,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy4",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {6,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {5,S}
5     Cs 0 {3,S} {4,S}
6     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.75e+09,"s^-1"),
        n = 0.98,
        alpha = 0,
        E0 = (36.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 674,
    label = "Others-R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_2H",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {4,S}
4     {Cs,Cd} 0 {2,S} {3,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.44e+08,"s^-1"),
        n = 1.2,
        alpha = 0,
        E0 = (41.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 675,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy4",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {6,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {5,S}
5     Cs 0 {3,S} {4,S}
6     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.64e+09,"s^-1"),
        n = 1,
        alpha = 0,
        E0 = (38.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 676,
    label = "Others-R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {4,S}
4     {Cs,Cd} 0 {2,S} {3,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.56e+09,"s^-1"),
        n = 0.81,
        alpha = 0,
        E0 = (39.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 677,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_Cs2_cy4",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {6,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {5,S}
5     Cs 0 {3,S} {4,S}
6     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.31e+08,"s^-1"),
        n = 1.21,
        alpha = 0,
        E0 = (38.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 678,
    label = "Others-R2H_S;C_rad_out_Cs2_cy4;Others-Cs_H_out_Cs2",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {4,S}
4     {Cs,Cd} 0 {2,S} {3,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (4.86e+10,"s^-1"),
        n = 0.58,
        alpha = 0,
        E0 = (38.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 679,
    label = "Others-R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_2H",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {5,S}
4     {Cs,Cd,Cb,Ct} 0 {2,S} {5,{S,D,T,B}}
5     {Cs,Cd,Cb,Ct} 0 {3,S} {4,{S,D,T,B}}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.07e+09,"s^-1"),
        n = 1.19,
        alpha = 0,
        E0 = (42.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 680,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy5",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {7,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {6,S}
5     Cs 0 {3,S} {6,S}
6     Cs 0 {4,S} {5,S}
7     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.35e+09,"s^-1"),
        n = 0.99,
        alpha = 0,
        E0 = (33.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 681,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy5",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {7,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {6,S}
5     Cs 0 {3,S} {6,S}
6     Cs 0 {4,S} {5,S}
7     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.29e+09,"s^-1"),
        n = 0.89,
        alpha = 0,
        E0 = (36.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 682,
    label = "Others-R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {5,S}
4     {Cs,Cd,Cb,Ct} 0 {2,S} {5,{S,D,T,B}}
5     {Cs,Cd,Cb,Ct} 0 {3,S} {4,{S,D,T,B}}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.08e+10,"s^-1"),
        n = 0.81,
        alpha = 0,
        E0 = (41.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 683,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_Cs2_cy5",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {7,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {6,S}
5     Cs 0 {3,S} {6,S}
6     Cs 0 {4,S} {5,S}
7     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.48e+07,"s^-1"),
        n = 1.45,
        alpha = 0,
        E0 = (37.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 684,
    label = "Others-R2H_S;C_rad_out_Cs2_cy5;Others-Cs_H_out_Cs2",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {5,S}
4     {Cs,Cd,Cb,Ct} 0 {2,S} {5,{S,D,T,B}}
5     {Cs,Cd,Cb,Ct} 0 {3,S} {4,{S,D,T,B}}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.24e+11,"s^-1"),
        n = 1.47,
        alpha = 0,
        E0 = (39.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 685,
    label = "R2H_S_cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {4,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.25e+11,"s^-1"),
        n = 0.6,
        alpha = 0,
        E0 = (44,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 686,
    label = "R2H_S_cy3;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {4,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.72e+12,"s^-1"),
        n = 0.37,
        alpha = 0,
        E0 = (41.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 687,
    label = "R2H_S_cy3;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {4,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (5.69e+11,"s^-1"),
        n = 0.51,
        alpha = 0,
        E0 = (43.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 688,
    label = "R2H_S_cy4;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5     R!H 0 {1,{S,D,B}} {4,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.56e+12,"s^-1"),
        n = 0.24,
        alpha = 0,
        E0 = (39,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 689,
    label = "R2H_S_cy4;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5     R!H 0 {1,{S,D,B}} {4,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.49e+10,"s^-1"),
        n = 0.79,
        alpha = 0,
        E0 = (42.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 691,
    label = "R2H_S_cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5     R!H 0 {4,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.71e+11,"s^-1"),
        n = 0.61,
        alpha = 0,
        E0 = (41.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 692,
    label = "R2H_S_cy5;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5     R!H 0 {4,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (3.72e+12,"s^-1"),
        n = 0.26,
        alpha = 0,
        E0 = (39.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 693,
    label = "R2H_S_cy5;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *2 R!H 0 {1,S} {3,S} {4,{S,D,B}}
3  *3 H 0 {2,S}
4     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
5     R!H 0 {4,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.88e+11,"s^-1"),
        n = 0.51,
        alpha = 0,
        E0 = (41.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 694,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_2H",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.76e+08,"s^-1"),
        n = 1.17,
        alpha = 0,
        E0 = (36.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 695,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.9e+09,"s^-1"),
        n = 0.82,
        alpha = 0,
        E0 = (35.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 696,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_2H",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.19e+08,"s^-1"),
        n = 1.32,
        alpha = 0,
        E0 = (38.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 697,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.5e+08,"s^-1"),
        n = 1.01,
        alpha = 0,
        E0 = (36.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 698,
    label = "Others-R3H_SS;C_rad_out_2H;Others-Cs_H_out_Cs2",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (2.25e+10,"s^-1"),
        n = 0.66,
        alpha = 0,
        E0 = (32.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 699,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_2H",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.89e+06,"s^-1"),
        n = 1.77,
        alpha = 0,
        E0 = (37.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 700,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (7.27e+09,"s^-1"),
        n = 0.66,
        alpha = 0,
        E0 = (34.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 701,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.71e+07,"s^-1"),
        n = 1.41,
        alpha = 0,
        E0 = (36.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 702,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (6.78e+08,"s^-1"),
        n = 1,
        alpha = 0,
        E0 = (35.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 703,
    label = "R3H_DS;Cd_rad_out_singleH;Cs_H_out_2H",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.1e+09,"s^-1"),
        n = 0.97,
        alpha = 0,
        E0 = (37.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 704,
    label = "R3H_SD;C_rad_out_2H;Cd_H_out_singleH",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *2 Cd 0 {2,D} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.11e+11,"s^-1"),
        n = 0.58,
        alpha = 0,
        E0 = (38.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 705,
    label = "R3H_DS;Cd_rad_out_singleH;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.23e+09,"s^-1"),
        n = 0.74,
        alpha = 0,
        E0 = (34.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 706,
    label = "R3H_SD;C_rad_out_H/NonDeC;Cd_H_out_singleH",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *2 Cd 0 {2,D} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.16e+10,"s^-1"),
        n = 0.77,
        alpha = 0,
        E0 = (64.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 707,
    label = "R3H_DS;Cd_rad_out_singleH;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     H 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (6.04e+10,"s^-1"),
        n = 0.59,
        alpha = 0,
        E0 = (32.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 708,
    label = "R3H_SD;Others-C_rad_out_Cs2;Cd_H_out_singleH",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *2 Cd 0 {2,D} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.53e+08,"s^-1"),
        n = 1.27,
        alpha = 0,
        E0 = (63.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 709,
    label = "R3H_DS;Cd_rad_out_singleNd;Cs_H_out_2H",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.58e+09,"s^-1"),
        n = 1.08,
        alpha = 0,
        E0 = (38.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 710,
    label = "R3H_SD;C_rad_out_2H;Cd_H_out_singleNd",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *2 Cd 0 {2,D} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.91e+11,"s^-1"),
        n = 0.63,
        alpha = 0,
        E0 = (61,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 711,
    label = "R3H_DS;Cd_rad_out_singleNd;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.91e+09,"s^-1"),
        n = 0.86,
        alpha = 0,
        E0 = (35.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 712,
    label = "R3H_SD;C_rad_out_H/NonDeC;Cd_H_out_singleNd",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *2 Cd 0 {2,D} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.96e+10,"s^-1"),
        n = 0.83,
        alpha = 0,
        E0 = (61.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 713,
    label = "R3H_DS;Cd_rad_out_singleNd;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     {Cs,O} 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (8.05e+09,"s^-1"),
        n = 0.86,
        alpha = 0,
        E0 = (33.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 714,
    label = "R3H_SD;Others-C_rad_out_Cs2;Cd_H_out_singleNd",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *2 Cd 0 {2,D} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cs,O} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.05e+10,"s^-1"),
        n = 0.79,
        alpha = 0,
        E0 = (61,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 715,
    label = "Others-R3H_SS;Cd_rad_out_double;Cs_H_out_2H",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.68e+08,"s^-1"),
        n = 1.24,
        alpha = 0,
        E0 = (36.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 716,
    label = "Others-R3H_SS;C_rad_out_2H;Cd_H_out_doubleC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     Cd 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (3.24e+08,"s^-1"),
        n = 1.14,
        alpha = 0,
        E0 = (41.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 717,
    label = "Others-R3H_SS;Cd_rad_out_double;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.66e+09,"s^-1"),
        n = 0.99,
        alpha = 0,
        E0 = (33.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 718,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cd_H_out_doubleC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     Cd 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (3.37e+07,"s^-1"),
        n = 1.41,
        alpha = 0,
        E0 = (42.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 719,
    label = "Others-R3H_SS;Cd_rad_out_double;Others-Cs_H_out_Cs2",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.1e+10,"s^-1"),
        n = 0.78,
        alpha = 0,
        E0 = (31.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 720,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cd_H_out_doubleC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     Cd 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (3.5e+06,"s^-1"),
        n = 1.68,
        alpha = 0,
        E0 = (42.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 721,
    label = "R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.93e+09,"s^-1"),
        n = 1.26,
        alpha = 0,
        E0 = (52.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 722,
    label = "R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.2e+10,"s^-1"),
        n = 0.82,
        alpha = 0,
        E0 = (49.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 723,
    label = "R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.64e+08,"s^-1"),
        n = 1.47,
        alpha = 0,
        E0 = (53.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 724,
    label = "R3H_SS_2Cd;C_rad_out_2H;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.43e+11,"s^-1"),
        n = 0.65,
        alpha = 0,
        E0 = (47.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 725,
    label = "R3H_SS_2Cd;Others-C_rad_out_Cs2;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.12e+07,"s^-1"),
        n = 1.72,
        alpha = 0,
        E0 = (51.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 726,
    label = "R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.21e+10,"s^-1"),
        n = 0.91,
        alpha = 0,
        E0 = (49,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 727,
    label = "R3H_SS_2Cd;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (3.46e+10,"s^-1"),
        n = 0.76,
        alpha = 0,
        E0 = (47.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 728,
    label = "R3H_SS_2Cd;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.14e+10,"s^-1"),
        n = 0.8,
        alpha = 0,
        E0 = (48.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 729,
    label = "R3H_SS_2Cd;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.76e+09,"s^-1"),
        n = 1.18,
        alpha = 0,
        E0 = (43.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 730,
    label = "Others-R3H_SS;C_rad_out_H/OneDe;Cs_H_out_2H",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.8e+09,"s^-1"),
        n = 0.99,
        alpha = 0,
        E0 = (48.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 731,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_H/OneDe",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.66e+08,"s^-1"),
        n = 1.1,
        alpha = 0,
        E0 = (29.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 732,
    label = "Others-R3H_SS;C_rad_out_H/OneDe;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.77e+09,"s^-1"),
        n = 0.74,
        alpha = 0,
        E0 = (46.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 733,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.41e+09,"s^-1"),
        n = 0.73,
        alpha = 0,
        E0 = (30.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 734,
    label = "Others-R3H_SS;C_rad_out_H/OneDe;Others-Cs_H_out_Cs2",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (9.06e+10,"s^-1"),
        n = 0.44,
        alpha = 0,
        E0 = (43.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 735,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_H/OneDe",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.4e+06,"s^-1"),
        n = 1.56,
        alpha = 0,
        E0 = (30.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 736,
    label = "R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.62e+10,"s^-1"),
        n = 0.69,
        alpha = 0,
        E0 = (35.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 737,
    label = "R3H_SS_23cy3;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {3,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.04e+10,"s^-1"),
        n = 0.71,
        alpha = 0,
        E0 = (34.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 738,
    label = "R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.16e+11,"s^-1"),
        n = 0.26,
        alpha = 0,
        E0 = (33.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 739,
    label = "R3H_SS_23cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {3,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.63e+08,"s^-1"),
        n = 1.01,
        alpha = 0,
        E0 = (45.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 740,
    label = "R3H_SS_12cy3;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (2.26e+13,"s^-1"),
        n = 0.26,
        alpha = 0,
        E0 = (32.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 741,
    label = "R3H_SS_23cy3;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {3,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.68e+07,"s^-1"),
        n = 1.42,
        alpha = 0,
        E0 = (46.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 742,
    label = "Others-R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_2H",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {3,S}
3     Cs 0 {1,S} {2,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.78e+09,"s^-1"),
        n = 1.04,
        alpha = 0,
        E0 = (36.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 743,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy3",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {4,S}
4     Cs 0 {1,S} {3,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.72e+09,"s^-1"),
        n = 0.78,
        alpha = 0,
        E0 = (39.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 744,
    label = "Others-R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {3,S}
3     Cs 0 {1,S} {2,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.39e+09,"s^-1"),
        n = 0.77,
        alpha = 0,
        E0 = (33.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 745,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy3",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {4,S}
4     Cs 0 {1,S} {3,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.73e+08,"s^-1"),
        n = 1.14,
        alpha = 0,
        E0 = (40.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 746,
    label = "Others-R3H_SS;C_rad_out_Cs2_cy3;Others-Cs_H_out_Cs2",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {3,S}
3     Cs 0 {1,S} {2,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (9.08e+10,"s^-1"),
        n = 0.36,
        alpha = 0,
        E0 = (31.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 747,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_Cs2_cy3",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {4,S}
4     Cs 0 {1,S} {3,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.86e+06,"s^-1"),
        n = 1.65,
        alpha = 0,
        E0 = (0,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 748,
    label = "R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.9e+10,"s^-1"),
        n = 0.57,
        alpha = 0,
        E0 = (39.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 749,
    label = "R3H_SS_23cy4;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {6,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.43e+09,"s^-1"),
        n = 0.93,
        alpha = 0,
        E0 = (38.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 750,
    label = "R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.9e+11,"s^-1"),
        n = 0.27,
        alpha = 0,
        E0 = (37.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 751,
    label = "R3H_SS_23cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {6,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.59e+08,"s^-1"),
        n = 1.2,
        alpha = 0,
        E0 = (39.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 752,
    label = "R3H_SS_12cy4;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.63e+12,"s^-1"),
        n = -0.04,
        alpha = 0,
        E0 = (37,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 753,
    label = "R3H_SS_23cy4;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {6,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.19e+07,"s^-1"),
        n = 1.55,
        alpha = 0,
        E0 = (40.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 754,
    label = "Others-R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_2H",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {4,S}
4     {Cs,Cd} 0 {2,S} {3,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.08e+08,"s^-1"),
        n = 1.25,
        alpha = 0,
        E0 = (39.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 755,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy4",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {6,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {5,S}
5     Cs 0 {3,S} {4,S}
6     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.09e+09,"s^-1"),
        n = 0.84,
        alpha = 0,
        E0 = (34.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 756,
    label = "Others-R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {4,S}
4     {Cs,Cd} 0 {2,S} {3,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.05e+08,"s^-1"),
        n = 0.99,
        alpha = 0,
        E0 = (37.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 757,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy4",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {6,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {5,S}
5     Cs 0 {3,S} {4,S}
6     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.69e+08,"s^-1"),
        n = 0.97,
        alpha = 0,
        E0 = (35.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 758,
    label = "Others-R3H_SS;C_rad_out_Cs2_cy4;Others-Cs_H_out_Cs2",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {4,S}
4     {Cs,Cd} 0 {2,S} {3,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (8.2e+09,"s^-1"),
        n = 0.54,
        alpha = 0,
        E0 = (35.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 759,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_Cs2_cy4",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {6,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {5,S}
5     Cs 0 {3,S} {4,S}
6     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.49e+07,"s^-1"),
        n = 1.38,
        alpha = 0,
        E0 = (35.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 760,
    label = "R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S} {7,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {1,{S,D,B}} {6,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.85e+10,"s^-1"),
        n = 0.6,
        alpha = 0,
        E0 = (40.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 761,
    label = "R3H_SS_23cy5;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {7,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.25e+09,"s^-1"),
        n = 0.99,
        alpha = 0,
        E0 = (34.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 762,
    label = "R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {7,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {1,{S,D,B}} {6,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.67e+11,"s^-1"),
        n = 0.29,
        alpha = 0,
        E0 = (38.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 763,
    label = "R3H_SS_23cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {7,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.42e+08,"s^-1"),
        n = 1.14,
        alpha = 0,
        E0 = (36,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 764,
    label = "R3H_SS_12cy5;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {7,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {1,{S,D,B}} {6,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (9.42e+11,"s^-1"),
        n = 0.12,
        alpha = 0,
        E0 = (37.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 765,
    label = "R3H_SS_23cy5;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {7,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.58e+06,"s^-1"),
        n = 1.78,
        alpha = 0,
        E0 = (39.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 766,
    label = "Others-R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_2H",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {5,S}
4     {Cs,Cd,Cb,Ct} 0 {2,S} {5,{S,D,T,B}}
5     {Cs,Cd,Cb,Ct} 0 {3,S} {4,{S,D,T,B}}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.14e+08,"s^-1"),
        n = 1.26,
        alpha = 0,
        E0 = (41.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 767,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy5",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {7,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {6,S}
5     Cs 0 {3,S} {6,S}
6     Cs 0 {4,S} {5,S}
7     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.9e+09,"s^-1"),
        n = 0.82,
        alpha = 0,
        E0 = (32.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 768,
    label = "Others-R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {5,S}
4     {Cs,Cd,Cb,Ct} 0 {2,S} {5,{S,D,T,B}}
5     {Cs,Cd,Cb,Ct} 0 {3,S} {4,{S,D,T,B}}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.25e+08,"s^-1"),
        n = 1.01,
        alpha = 0,
        E0 = (39.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 769,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy5",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {7,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {6,S}
5     Cs 0 {3,S} {6,S}
6     Cs 0 {4,S} {5,S}
7     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.5e+08,"s^-1"),
        n = 0.9,
        alpha = 0,
        E0 = (34.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 770,
    label = "Others-R3H_SS;C_rad_out_Cs2_cy5;Others-Cs_H_out_Cs2",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3     Cs 0 {1,S} {5,S}
4     {Cs,Cd,Cb,Ct} 0 {2,S} {5,{S,D,T,B}}
5     {Cs,Cd,Cb,Ct} 0 {3,S} {4,{S,D,T,B}}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.97e+10,"s^-1"),
        n = 0.46,
        alpha = 0,
        E0 = (37.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 771,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_Cs2_cy5",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {7,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     Cs 0 {1,S} {6,S}
5     Cs 0 {3,S} {6,S}
6     Cs 0 {4,S} {5,S}
7     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.21e+08,"s^-1"),
        n = 1.04,
        alpha = 0,
        E0 = (34.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 772,
    label = "R3H_SS_12cy3;Others-C_rad_out_Cs2;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.64e+09,"s^-1"),
        n = 0.84,
        alpha = 0,
        E0 = (6.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 773,
    label = "R3H_SS_23cy3;C_rad_out_2H;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {3,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (5.02e+10,"s^-1"),
        n = 0.56,
        alpha = 0,
        E0 = (42.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 774,
    label = "R3H_SS_12cy3;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.22e+11,"s^-1"),
        n = 0.4,
        alpha = 0,
        E0 = (34.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 775,
    label = "R3H_SS_23cy3;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {3,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (4.34e+09,"s^-1"),
        n = 0.81,
        alpha = 0,
        E0 = (43.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 776,
    label = "R3H_SS_12cy3;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {2,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (2.72e+12,"s^-1"),
        n = -0.04,
        alpha = 0,
        E0 = (33.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 777,
    label = "R3H_SS_23cy3;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {3,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.61e+08,"s^-1"),
        n = 1.26,
        alpha = 0,
        E0 = (42,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 778,
    label = "R3H_SS_13cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {3,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.78e+11,"s^-1"),
        n = 0.29,
        alpha = 0,
        E0 = (54.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 779,
    label = "R3H_SS_13cy4;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {3,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.48e+10,"s^-1"),
        n = 0.6,
        alpha = 0,
        E0 = (54.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 780,
    label = "R3H_SS_13cy4;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {3,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (2.66e+12,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (51.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 781,
    label = "R3H_SS_13cy4;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {5,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {1,{S,D,B}} {3,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (3.55e+11,"s^-1"),
        n = 0.37,
        alpha = 0,
        E0 = (51.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 782,
    label = "R3H_SS_13cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.36e+11,"s^-1"),
        n = 0.46,
        alpha = 0,
        E0 = (47.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 783,
    label = "R3H_SS_13cy5;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.72e+09,"s^-1"),
        n = 0.86,
        alpha = 0,
        E0 = (47.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 784,
    label = "R3H_SS_13cy5;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.1e+12,"s^-1"),
        n = 0.23,
        alpha = 0,
        E0 = (44.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 785,
    label = "R3H_SS_13cy5;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (6.07e+10,"s^-1"),
        n = 0.62,
        alpha = 0,
        E0 = (43.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 786,
    label = "R3H_SS_12cy5;Others-C_rad_out_Cs2;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S} {7,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {1,{S,D,B}} {6,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.84e+09,"s^-1"),
        n = 1.05,
        alpha = 0,
        E0 = (41.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 787,
    label = "R3H_SS_23cy5;C_rad_out_2H;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {7,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (4.51e+09,"s^-1"),
        n = 0.86,
        alpha = 0,
        E0 = (33.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 788,
    label = "R3H_SS_12cy5;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {7,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {1,{S,D,B}} {6,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.04e+09,"s^-1"),
        n = 0.74,
        alpha = 0,
        E0 = (38.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 789,
    label = "R3H_SS_23cy5;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {7,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.95e+09,"s^-1"),
        n = 0.88,
        alpha = 0,
        E0 = (35.1,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 790,
    label = "R3H_SS_12cy5;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {7,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {1,{S,D,B}} {6,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.44e+10,"s^-1"),
        n = 0.74,
        alpha = 0,
        E0 = (37.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 791,
    label = "R3H_SS_23cy5;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {7,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {5,{S,D,B}} {7,{S,D,B}}
7     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (2.85e+07,"s^-1"),
        n = 1.46,
        alpha = 0,
        E0 = (36.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 792,
    label = "R3H_SS_12cy4;Others-C_rad_out_Cs2;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.28e+08,"s^-1"),
        n = 1.07,
        alpha = 0,
        E0 = (40.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 793,
    label = "R3H_SS_23cy4;C_rad_out_2H;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {6,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.93e+10,"s^-1"),
        n = 0.75,
        alpha = 0,
        E0 = (36.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 794,
    label = "R3H_SS_12cy4;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.41e+09,"s^-1"),
        n = 0.77,
        alpha = 0,
        E0 = (38.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 795,
    label = "R3H_SS_23cy4;C_rad_out_H/NonDeC;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {6,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.96e+09,"s^-1"),
        n = 0.96,
        alpha = 0,
        E0 = (38.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 796,
    label = "R3H_SS_12cy4;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S} {6,{S,D,B}}
2  *4 R!H 0 {1,S} {3,S} {5,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
5     R!H 0 {2,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {1,{S,D,B}} {5,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (2.37e+10,"s^-1"),
        n = 0.62,
        alpha = 0,
        E0 = (37.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 797,
    label = "R3H_SS_23cy4;Others-C_rad_out_Cs2;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S} {6,{S,D,B}}
3  *2 R!H 0 {2,S} {4,S} {5,{S,D,B}}
4  *3 H 0 {3,S}
5     R!H 0 {3,{S,D,B}} {6,{S,D,B}}
6     R!H 0 {2,{S,D,B}} {5,{S,D,B}}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (4.96e+07,"s^-1"),
        n = 1.46,
        alpha = 0,
        E0 = (39.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 798,
    label = "R3H_SS_OC;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.71e+08,"s^-1"),
        n = 1.45,
        alpha = 0,
        E0 = (42.27,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 799,
    label = "R3H_SS_OC;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.66e+08,"s^-1"),
        n = 1.28,
        alpha = 0,
        E0 = (39.74,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 800,
    label = "R3H_SS_OC;O_rad_out;Cs_H_out_H/(NonDeC/Cs)",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S}
4     H 0 {1,S}
5     Cs 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (2.43e+09,"s^-1"),
        n = 1.17,
        alpha = 0,
        E0 = (39.66,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 801,
    label = "R3H_SS_OC;O_rad_out;Cs_H_out_H/(NonDeC/Cs/Cs)",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S} {6,S}
4     H 0 {1,S}
5     Cs 0 {3,S}
6     Cs 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (1.07e+10,"s^-1"),
        n = 0.98,
        alpha = 0,
        E0 = (39.58,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 802,
    label = "R3H_SS_OC;O_rad_out;Cs_H_out_H/(NonDeC/Cs/Cs/Cs)",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S} {5,S} {6,S} {7,S}
4     H 0 {1,S}
5     Cs 0 {3,S}
6     Cs 0 {3,S}
7     Cs 0 {3,S}
""",
    kinetics = ArrheniusEP(
        A = (6.62e+09,"s^-1"),
        n = 1.04,
        alpha = 0,
        E0 = (39.34,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 803,
    label = "R3H_SS_OC;O_rad_out;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (4.97e+09,"s^-1"),
        n = 1.01,
        alpha = 0,
        E0 = (38.47,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 804,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.99e+11,"s^-1"),
        n = 0.15,
        alpha = 0,
        E0 = (34.2107,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 805,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.38e+08,"s^-1"),
        n = 1.06,
        alpha = 0,
        E0 = (33.51,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 806,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S} {7,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
7     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.06e+08,"s^-1"),
        n = 1.2,
        alpha = 0,
        E0 = (33.53,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
Sumathy CBS-Q calculations
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 807,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2e+08,"s^-1"),
        n = 1.1,
        alpha = 0,
        E0 = (30.09,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 808,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.81e+08,"s^-1"),
        n = 0.88,
        alpha = 0,
        E0 = (29.48,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 809,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S} {7,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
7     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.53e+09,"s^-1"),
        n = 0.69,
        alpha = 0,
        E0 = (30.11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 810,
    label = "R4H_SSS_OOCsCs;O_rad_out;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (2.64e+09,"s^-1"),
        n = 0.78,
        alpha = 0,
        E0 = (27.11,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 811,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (9.25e+09,"s^-1"),
        n = 0.57,
        alpha = 0,
        E0 = (27.31,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 812,
    label = "R4H_SSS_OO(Cs/Cs/Cs)Cs;O_rad_out;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S} {7,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
7     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (4.87e+10,"s^-1"),
        n = 0.35,
        alpha = 0,
        E0 = (26.39,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 813,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.69e+06,"s^-1"),
        n = 1.55,
        alpha = 0,
        E0 = (21.02,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 814,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {7,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.78e+06,"s^-1"),
        n = 1.35,
        alpha = 0,
        E0 = (20.84,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 815,
    label = "R5H_SSSS_OO(Cs/Cs/Cs)Cs;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {7,S} {8,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {3,S}
8     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.35e+07,"s^-1"),
        n = 1.12,
        alpha = 0,
        E0 = (21.88,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 816,
    label = "R5H_SSSS_OOCs(Cs/Cs);O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S} {7,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.41e+07,"s^-1"),
        n = 1.32,
        alpha = 0,
        E0 = (21.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 817,
    label = "R5H_SSSS_OOCs(Cs/Cs/Cs);O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S} {7,S} {8,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {4,S}
8     Cs 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.09e+08,"s^-1"),
        n = 1.23,
        alpha = 0,
        E0 = (21.62,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 818,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.94e+06,"s^-1"),
        n = 1.26,
        alpha = 0,
        E0 = (18.17,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 819,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {7,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.38e+10,"s^-1"),
        n = 0.21,
        alpha = 0,
        E0 = (18.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 820,
    label = "R5H_SSSS_OOCCC;O_rad_out;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (3.174e+08,"s^-1"),
        n = 1.15,
        alpha = 0,
        E0 = (15.37,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 821,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4     Cs 0 {3,S} {5,S}
5  *5 Cs 0 {4,S} {6,S}
6  *2 Cs 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (369000,"s^-1"),
        n = 1.52,
        alpha = 0,
        E0 = (20.05,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 822,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4     Cs 0 {3,S} {5,S}
5  *5 Cs 0 {4,S} {6,S}
6  *2 Cs 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.62e+06,"s^-1"),
        n = 1.22,
        alpha = 0,
        E0 = (16.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. 
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 823,
    label = "R6H_SSSSS_OO;O_rad_out;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4     Cs 0 {3,S} {5,S}
5  *5 Cs 0 {4,S} {6,S}
6  *2 Cs 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (1.48e+06,"s^-1"),
        n = 1.22,
        alpha = 0,
        E0 = (13.84,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 824,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (90600,"s^-1"),
        n = 1.51,
        alpha = 0,
        E0 = (19.95,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 825,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.37e+06,"s^-1"),
        n = 0.99,
        alpha = 0,
        E0 = (18.17,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. 
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 826,
    label = "R7H_OOCs4;O_rad_out;Others-Cs_H_out_Cs2",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = "AND{Cs_H_out_Cs2, NOT OR{Cs_H_out_Cs2_cy3, Cs_H_out_Cs2_cy4, Cs_H_out_Cs2_cy5}}",
    kinetics = ArrheniusEP(
        A = (562000,"s^-1"),
        n = 1.09,
        alpha = 0,
        E0 = (14.28,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 827,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.07e+09,"s^-1"),
        n = 0.99,
        alpha = 0,
        E0 = (37.33,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya).""",
    longDesc = 
u"""
CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 828,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.7e+08,"s^-1"),
        n = 1.15,
        alpha = 0,
        E0 = (39.04,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya).""",
    longDesc = 
u"""
CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 829,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.56e+07,"s^-1"),
        n = 1.53,
        alpha = 0,
        E0 = (40.58,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya).""",
    longDesc = 
u"""
CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 830,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.83e+11,"s^-1"),
        n = 0.45,
        alpha = 0,
        E0 = (35.92,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya).""",
    longDesc = 
u"""
CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 831,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.89e+10,"s^-1"),
        n = 0.43,
        alpha = 0,
        E0 = (38.88,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya).""",
    longDesc = 
u"""
CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 832,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.87e+08,"s^-1"),
        n = 1.28,
        alpha = 0,
        E0 = (36.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya).""",
    longDesc = 
u"""
CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 833,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.75e+08,"s^-1"),
        n = 1.29,
        alpha = 0,
        E0 = (37.93,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya).""",
    longDesc = 
u"""
CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 834,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.14e+08,"s^-1"),
        n = 1.42,
        alpha = 0,
        E0 = (38.71,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya).""",
    longDesc = 
u"""
CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 835,
    label = "Others-R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.28e+09,"s^-1"),
        n = 1.12,
        alpha = 0,
        E0 = (34.69,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 836,
    label = "Others-R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.53e+10,"s^-1"),
        n = 0.68,
        alpha = 0,
        E0 = (37.43,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 837,
    label = "Others-R2H_S;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = "AND{R2H_S, NOT OR{R2H_S, R2H_S_cy3, R2H_S_cy4, R2H_S_cy5}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.24e+09,"s^-1"),
        n = 1.11,
        alpha = 0,
        E0 = (39.38,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 838,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.02e+08,"s^-1"),
        n = 1.11,
        alpha = 0,
        E0 = (36.56,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 839,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.63e+07,"s^-1"),
        n = 1.54,
        alpha = 0,
        E0 = (37.27,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 840,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (313000,"s^-1"),
        n = 2.04,
        alpha = 0,
        E0 = (36.64,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 841,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (6.95e+09,"s^-1"),
        n = 0.79,
        alpha = 0,
        E0 = (34.71,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 842,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.53e+10,"s^-1"),
        n = 0.68,
        alpha = 0,
        E0 = (37.43,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 843,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.44e+09,"s^-1"),
        n = 0.8,
        alpha = 0,
        E0 = (35.84,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 844,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.51e+08,"s^-1"),
        n = 1.16,
        alpha = 0,
        E0 = (36.24,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""Sumathy's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sumathy's CBS-QB3 calculations. Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d') level.

The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 845,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.37e+07,"s^-1"),
        n = 1.36,
        alpha = 0,
        E0 = (37.15,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 846,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.08e+06,"s^-1"),
        n = 1.55,
        alpha = 0,
        E0 = (36.68,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 847,
    label = "Others-R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4.69e+09,"s^-1"),
        n = 0.68,
        alpha = 0,
        E0 = (34.81,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 848,
    label = "Others-R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (5.18e+08,"s^-1"),
        n = 0.87,
        alpha = 0,
        E0 = (36.12,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 849,
    label = "Others-R3H_SS;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = "AND{R3H_SS, NOT OR{R3H_SS_12cy3, R3H_SS_23cy3, R3H_SS_12cy4, R3H_SS_23cy4, R3H_SS_13cy4, R3H_SS_12cy5, R3H_SS_23cy5, R3H_SS_13cy5, R3H_SS_2Cd, R3H_SS_OC}}",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.07e+07,"s^-1"),
        n = 1.37,
        alpha = 0,
        E0 = (35.66,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 850,
    label = "R3H_SS_OC;O_rad_out;Cs_H_out_H/NonDeO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3e+08,"s^-1"),
        n = 1.23,
        alpha = 0,
        E0 = (36.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 851,
    label = "R3H_SS_OC;O_rad_out;Cs_H_out_NDMustO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *2 Cs 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3e+08,"s^-1"),
        n = 1.23,
        alpha = 0,
        E0 = (36.85,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 852,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_H/NonDeO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.61e+08,"s^-1"),
        n = 1.09,
        alpha = 0,
        E0 = (26.14,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 855,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (9.2e+08,"s^-1"),
        n = 0.82,
        alpha = 0,
        E0 = (26.28,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 856,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_NDMustO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {4,S} {6,S}
4  *2 Cs 0 {3,S} {5,S}
5  *3 H 0 {4,S}
6     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.18e+11,"s^-1"),
        n = 0.51,
        alpha = 0,
        E0 = (26.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 858,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_H/NonDeO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (11500,"s^-1"),
        n = 2.11,
        alpha = 0,
        E0 = (15.47,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 863,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_NDMustO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.9e+07,"s^-1"),
        n = 1.1,
        alpha = 0,
        E0 = (15.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 864,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_H/NonDeO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {7,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (2.29e+08,"s^-1"),
        n = 1.12,
        alpha = 0,
        E0 = (15.38,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 865,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_NDMustO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S} {7,S}
4  *5 Cs 0 {3,S} {5,S}
5  *2 Cs 0 {4,S} {6,S}
6  *3 H 0 {5,S}
7     Cs 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.17e+11,"s^-1"),
        n = 0.43,
        alpha = 0,
        E0 = (15.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 866,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_H/NonDeO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4     Cs 0 {3,S} {5,S}
5  *5 Cs 0 {4,S} {6,S}
6  *2 Cs 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (549,"s^-1"),
        n = 2.21,
        alpha = 0,
        E0 = (14.38,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 867,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_NDMustO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4     Cs 0 {3,S} {5,S}
5  *5 Cs 0 {4,S} {6,S}
6  *2 Cs 0 {5,S} {7,S}
7  *3 H 0 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (72300,"s^-1"),
        n = 1.65,
        alpha = 0,
        E0 = (12.02,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 868,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_H/NonDeO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (933000,"s^-1"),
        n = 0.75,
        alpha = 0,
        E0 = (12.82,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 869,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_NDMustO",
    group1 = 
"""
1  *1 Os 1 {2,S}
2  *4 Os 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,{S,D,T,B}}
6  *5 R!H 0 {5,{S,D,T,B}} {7,{S,D,T,B}}
7  *2 R!H 0 {6,{S,D,T,B}} {8,S}
8  *3 H 0 {7,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S} {5,S}
2  *3 H 0 {1,S}
3     O 0 {1,S}
4     {Cs,O} 0 {1,S}
5     R!H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (3.41e+06,"s^-1"),
        n = 1.09,
        alpha = 0,
        E0 = (12.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 870,
    label = "R4H_SDS;C_rad_out_2H;Cd_H_out_doubleC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *5 Cd 0 {2,D} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,D}
2  *3 H 0 {1,S}
3     Cd 0 {1,D}
""",
    kinetics = ArrheniusEP(
        A = (1.32e+06,"s^-1"),
        n = 1.6229,
        alpha = 0,
        E0 = (44.071,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 871,
    label = "R4H_SDS;Cd_rad_out_double;Cs_H_out_2H",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *5 Cd 0 {2,D} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,D}
2     Cd 0 {1,D}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.11e+08,"s^-1"),
        n = 1.1915,
        alpha = 0,
        E0 = (24.7623,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 872,
    label = "R5H_SMSD;C_rad_out_2H;Cd_H_out_singleH",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,{D,T,B}}
3     R!H 0 {2,{D,T,B}} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (219000,"s^-1"),
        n = 1.7613,
        alpha = 0,
        E0 = (38.275,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 873,
    label = "R5H_DSMS;Cd_rad_out_singleH;Cs_H_out_2H",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3     R!H 0 {2,S} {4,{D,T,B}}
4  *5 R!H 0 {3,{D,T,B}} {5,S}
5  *2 R!H 0 {4,S} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (136000,"s^-1"),
        n = 1.9199,
        alpha = 0,
        E0 = (7.8968,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 874,
    label = "R3H_SD;C_rad_out_2H;Cd_H_out_singleDe",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *2 Cd 0 {2,D} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.59e+07,"s^-1"),
        n = 1.4638,
        alpha = 0,
        E0 = (66.3163,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 875,
    label = "R3H_DS;Cd_rad_out_singleDe;Cs_H_out_2H",
    group1 = 
"""
1  *1 Cd 1 {2,D}
2  *4 Cd 0 {1,D} {3,S}
3  *2 R!H 0 {2,S} {4,S}
4  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 Cd 1 {2,S}
2     {Cd,Ct,Cb,CO} 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.28371e+09,"s^-1"),
        n = 1.0541,
        alpha = 0,
        E0 = (46.1467,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1600,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 876,
    label = "R4H_SDS;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 Cd 0 {1,S} {3,D}
3  *5 Cd 0 {2,D} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.11e+06,"s^-1","*|/",3),
        n = 1.78,
        alpha = 0,
        E0 = (27.18,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""MHS CBS-QB3 calculations.""",
    longDesc = 
u"""
MHS CBS-QB3 calculations for CH3-CH2-CH=CH-O* == CH3-C*H-CH=CH-OH.  
Product is the cis configuration because TS is also cis.  
Note--this only affects the tunneling correction (b/c in products).  
Only methyl rotor was considered for TS.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 877,
    label = "R5H_SSSD;O_rad_out;Cd_H_out_singleH",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3     R!H 0 {2,S} {4,S}
4  *5 Cd 0 {3,S} {5,D}
5  *2 Cd 0 {4,D} {6,S}
6  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cd 0 {2,S} {3,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.234e+06,"s^-1","*|/",3),
        n = 1.554,
        alpha = 0,
        E0 = (26.636,"kcal/mol","+|-",2),
        Tmin = (600,"K"),
        Tmax = (2000,"K"),
    ),
    reference = None,
    referenceType = "",
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
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 878,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_OOH/H",
    group1 = 
"""
1  *5 Cs 0 {2,S} {3,S}
2  *4 Os 0 {1,S} {4,S}
3  *2 Cs 0 {1,S} {5,S}
4  *1 Os 1 {2,S}
5  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2.47e+12,"s^-1"),
        n = -0.24,
        alpha = 0,
        E0 = (28,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 879,
    label = "R4H_SSS_OOCsCs;O_rad_out;Cs_H_out_OOH/Cs",
    group1 = 
"""
1  *5 Cs 0 {2,S} {3,S}
2  *4 Os 0 {1,S} {4,S}
3  *2 Cs 0 {1,S} {5,S}
4  *1 Os 1 {2,S}
5  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     Cs 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2.76e+08,"s^-1"),
        n = 1.2,
        alpha = 0,
        E0 = (25.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 880,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/H",
    group1 = 
"""
1  *5 Cs 0 {2,S} {3,S} {4,S}
2  *4 Os 0 {1,S} {5,S}
3  *2 Cs 0 {1,S} {6,S}
4     Cs 0 {1,S}
5  *1 Os 1 {2,S}
6  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.22e+07,"s^-1"),
        n = 1.6,
        alpha = 0,
        E0 = (27.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 881,
    label = "R4H_SSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/Cs",
    group1 = 
"""
1  *5 Cs 0 {2,S} {3,S} {4,S}
2  *4 Os 0 {1,S} {5,S}
3  *2 Cs 0 {1,S} {6,S}
4     Cs 0 {1,S}
5  *1 Os 1 {2,S}
6  *3 H 0 {3,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     Cs 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (1.75e+08,"s^-1"),
        n = 1.7,
        alpha = 0,
        E0 = (26,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 882,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_OOH/H",
    group1 = 
"""
1     Cs 0 {2,S} {3,S}
2  *5 Cs 0 {1,S} {4,S}
3  *4 Os 0 {1,S} {5,S}
4  *2 Cs 0 {2,S} {6,S}
5  *1 Os 1 {3,S}
6  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (25900,"s^-1"),
        n = 1.9,
        alpha = 0,
        E0 = (18.8,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 883,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/H",
    group1 = 
"""
1     Cs 0 {2,S} {3,S} {5,S}
2  *5 Cs 0 {1,S} {4,S}
3  *4 Os 0 {1,S} {6,S}
4  *2 Cs 0 {2,S} {7,S}
5     Cs 0 {1,S}
6  *1 Os 1 {3,S}
7  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (5490,"s^-1"),
        n = 2.4,
        alpha = 0,
        E0 = (19.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 884,
    label = "R5H_SSSS_OOCs(Cs/Cs/Cs);O_rad_out;Cs_H_out_OOH/H",
    group1 = 
"""
1  *5 Cs 0 {2,S} {3,S} {5,S} {6,S}
2     Cs 0 {1,S} {4,S}
3  *2 Cs 0 {1,S} {7,S}
4  *4 Os 0 {2,S} {8,S}
5     Cs 0 {1,S}
6     Cs 0 {1,S}
7  *3 H 0 {3,S}
8  *1 Os 1 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (6.5,"s^-1"),
        n = 3.6,
        alpha = 0,
        E0 = (17.7,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 885,
    label = "R5H_SSSS_OOCCC;O_rad_out;Cs_H_out_OOH/Cs",
    group1 = 
"""
1     Cs 0 {2,S} {3,S}
2  *5 Cs 0 {1,S} {4,S}
3  *4 Os 0 {1,S} {5,S}
4  *2 Cs 0 {2,S} {6,S}
5  *1 Os 1 {3,S}
6  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     Cs 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (57.9,"s^-1"),
        n = 2.9,
        alpha = 0,
        E0 = (17,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 886,
    label = "R5H_SSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/Cs",
    group1 = 
"""
1     Cs 0 {2,S} {3,S} {5,S}
2  *5 Cs 0 {1,S} {4,S}
3  *4 Os 0 {1,S} {6,S}
4  *2 Cs 0 {2,S} {7,S}
5     Cs 0 {1,S}
6  *1 Os 1 {3,S}
7  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     Cs 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (175,"s^-1"),
        n = 3.1,
        alpha = 0,
        E0 = (17.5,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 887,
    label = "R6H_SSSSS_OO;O_rad_out;Cs_H_out_OOH/H",
    group1 = 
"""
1     Cs 0 {2,S} {3,S}
2     Cs 0 {1,S} {4,S}
3  *5 Cs 0 {1,S} {5,S}
4  *4 Os 0 {2,S} {6,S}
5  *2 Cs 0 {3,S} {7,S}
6  *1 Os 1 {4,S}
7  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2380,"s^-1"),
        n = 1.7,
        alpha = 0,
        E0 = (16.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 888,
    label = "R6H_SSSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/H",
    group1 = 
"""
1     Cs 0 {2,S} {4,S} {6,S}
2     Cs 0 {1,S} {3,S}
3  *5 Cs 0 {2,S} {5,S}
4  *4 Os 0 {1,S} {7,S}
5  *2 Cs 0 {3,S} {8,S}
6     Cs 0 {1,S}
7  *1 Os 1 {4,S}
8  *3 H 0 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (628,"s^-1"),
        n = 2.2,
        alpha = 0,
        E0 = (17.4,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 889,
    label = "R6H_SSSSS_OOCCC(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs",
    group1 = 
"""
1  *2 Cs 0 {2,S} {6,S} {7,S}
2  *5 Cs 0 {1,S} {3,S}
3     Cs 0 {2,S} {4,S}
4     Cs 0 {3,S} {5,S}
5  *4 Os 0 {4,S} {8,S}
6  *3 H 0 {1,S}
7     Cs 0 {1,S}
8  *1 Os 1 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     Cs 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (377,"s^-1"),
        n = 2.2,
        alpha = 0,
        E0 = (15.3,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 890,
    label = "R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs",
    group1 = 
"""
1     Cs 0 {3,S} {5,S} {6,S}
2  *2 Cs 0 {4,S} {7,S} {8,S}
3     Cs 0 {1,S} {4,S}
4  *5 Cs 0 {2,S} {3,S}
5  *4 Os 0 {1,S} {9,S}
6     Cs 0 {1,S}
7  *3 H 0 {2,S}
8     Cs 0 {2,S}
9  *1 Os 1 {5,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     Cs 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (254,"s^-1"),
        n = 2.6,
        alpha = 0,
        E0 = (16.2,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 891,
    label = "R7H_OOCs4;O_rad_out;Cs_H_out_OOH/H",
    group1 = 
"""
1     R!H 0 {2,{S,D,T,B}} {3,{S,D,T,B}}
2     R!H 0 {1,{S,D,T,B}} {4,{S,D,T,B}}
3     R!H 0 {1,{S,D,T,B}} {5,S}
4  *5 R!H 0 {2,{S,D,T,B}} {6,{S,D,T,B}}
5  *4 Os 0 {3,S} {7,S}
6  *2 R!H 0 {4,{S,D,T,B}} {8,S}
7  *1 Os 1 {5,S}
8  *3 H 0 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     H 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (557,"s^-1"),
        n = 1.8,
        alpha = 0,
        E0 = (16.6,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 892,
    label = "R7H_OOCCCC(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs",
    group1 = 
"""
1  *2 R!H 0 {2,{S,D,T,B}} {7,S} {8,S}
2  *5 R!H 0 {1,{S,D,T,B}} {3,{S,D,T,B}}
3     R!H 0 {2,{S,D,T,B}} {4,{S,D,T,B}}
4     R!H 0 {3,{S,D,T,B}} {5,{S,D,T,B}}
5     R!H 0 {4,{S,D,T,B}} {6,S}
6  *4 Os 0 {5,S} {9,S}
7  *3 H 0 {1,S}
8     Cs 0 {1,S}
9  *1 Os 1 {6,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2     O 0 {1,S} {5,S}
3  *3 H 0 {1,S}
4     Cs 0 {1,S}
5     O 0 {2,S}
""",
    kinetics = ArrheniusEP(
        A = (2000,"s^-1"),
        n = 1.9,
        alpha = 0,
        E0 = (14.9,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 893,
    label = "R5H_CCCC_O;O_rad_out;Cs_H_out_2H",
    group1 = 
"""
1     C 0 {2,S} {3,S}
2  *5 C 0 {1,S} {4,S}
3  *4 C 0 {1,S} {5,S}
4  *2 C 0 {2,S} {6,S}
5  *1 O 1 {3,S}
6  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     H 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (7.61,"kcal/mol"),
        Tmin = (200,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of primary H (per H atom)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 894,
    label = "R5H_CCCC_O;O_rad_out;Cs_H_out_H/NonDeC",
    group1 = 
"""
1     C 0 {2,S} {3,S}
2  *5 C 0 {1,S} {4,S}
3  *4 C 0 {1,S} {5,S}
4  *2 C 0 {2,S} {6,S}
5  *1 O 1 {3,S}
6  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (6.15,"kcal/mol"),
        Tmin = (200,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of secondary H (per H atom)""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 895,
    label = "R5H_CCCC_O;O_rad_out;Cs_H_out",
    group1 = 
"""
1     C 0 {2,S} {3,S}
2  *5 C 0 {1,S} {4,S}
3  *4 C 0 {1,S} {5,S}
4  *2 C 0 {2,S} {6,S}
5  *1 O 1 {3,S}
6  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 O 1
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     R 0 {1,S}
4     R 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (4e+10,"s^-1"),
        n = 0,
        alpha = 0,
        E0 = (5.1,"kcal/mol"),
        Tmin = (200,"K"),
        Tmax = (1000,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 3,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of tertiary H""",
    longDesc = 
u"""

""",
    history = [
        ("Thu Sep  8 16:00:31 2011","Josh Allen <jwallen@mit.edu>","action","""Josh Allen <jwallen@mit.edu> imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8441,
    label = "R4H_SSS;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (8.73e+06,"s^-1"),
        n = 1.13,
        alpha = 0,
        E0 = (18.93,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8451,
    label = "R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (695000,"s^-1"),
        n = 1.38,
        alpha = 0,
        E0 = (19.67,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8461,
    label = "R4H_SSS;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (17400,"s^-1"),
        n = 1.89,
        alpha = 0,
        E0 = (18.51,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8471,
    label = "R4H_SSS;C_rad_out_2H;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     H 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.09e+09,"s^-1"),
        n = 0.55,
        alpha = 0,
        E0 = (17.43,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8481,
    label = "R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = 
"""
1  *1 C 1 {2,S} {3,S}
2     H 0 {1,S}
3     Cs 0 {1,S}
""",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (7.86e+07,"s^-1"),
        n = 0.84,
        alpha = 0,
        E0 = (15.38,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

entry(
    index = 8491,
    label = "R4H_SSS;Others-C_rad_out_Cs2;Cs_H_out_H/NonDeC",
    group1 = 
"""
1  *1 R!H 1 {2,S}
2  *4 R!H 0 {1,S} {3,S}
3  *5 R!H 0 {2,S} {4,S}
4  *2 R!H 0 {3,S} {5,S}
5  *3 H 0 {4,S}
""",
    group2 = "AND{C_rad_out_Cs2, NOT OR{C_rad_out_Cs2_cy3, C_rad_out_Cs2_cy4, C_rad_out_Cs2_cy5}}",
    group3 = 
"""
1  *2 Cs 0 {2,S} {3,S} {4,S}
2  *3 H 0 {1,S}
3     Cs 0 {1,S}
4     H 0 {1,S}
""",
    kinetics = ArrheniusEP(
        A = (1.05e+06,"s^-1"),
        n = 1.39,
        alpha = 0,
        E0 = (16.19,"kcal/mol"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
    ),
    reference = None,
    referenceType = "",
    rank = 2,
    shortDesc = u"""""",
    longDesc = 
u"""
The rate was added by Sandeep Sharma on Feb 01 2006 (713a0f98f91) with message "I have added the rate rules given to me by Sumathy which are present in Pitz.xls file in the Acads directory of my laptop."
The node was commented out of the tree, disabling the rate, by Sandeep Sharma on Feb 13 2006 (2e7b38d367c9) with the message "Removed nodes Cs_H_out_H/(CCCOOH) and the others from under node Cs_H_out_H/NonDeC as it is not a subnode anyway."

On 6 April 2010, Josh Allen, Mike Harper and Richard West spent quite a while trying to put these nodes in the right place in the tree and to make the definitions valid and consistent.
Unfortunately it was not clear what they were intended to mean because many of the definitions overlap. We gave up, and they remain commented out.
""",
    history = [
        ("Wed Jun  1 12:02:47 2011","Josh Allen <jwallen@mit.edu>","action","""jwallen imported this entry from the old RMG database."""),
    ],
)

