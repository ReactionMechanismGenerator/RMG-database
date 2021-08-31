#!/usr/bin/env python
# encoding: utf-8

name = "Functional Group Values"
shortDesc = ""
longDesc = """

"""
entry(
    index = 0,
    label = "R!H!Val7",
    group = "OR{R!H!Val7x0, R!H!Val7x1, R!H!Val7x2_trip, R!H!Val7x3_quart}",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 1,
    label = "R!H!Val7x0",
    group = 
"""
1 * R!H!Val7 u0
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 2,
    label = "C_R0",
    group = 
"""
1 * C u0
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 3,
    label = "RsCH3",
    group = 
"""
1 * C        u0 {2,S} {3,S} {4,S} {5,S}
2   R!H!Val7 ux {1,S}
3   [H,Val7] u0 {1,S}
4   [H,Val7] u0 {1,S}
5   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2750, 2850, 3),
            (1350, 1500, 2),
            (700, 800, 1),
            (1000, 1100, 1),
            (1350, 1400, 1),
            (900, 1100, 1),
        ],
        symmetry = 6,
    ),
    shortDesc = """Alkane end group""",
    longDesc = 
"""
Goldsmith. (2010). Predicting Combustion Properties of Hydrocarbon Fuel Mixtures. (Doctoral dissertation). 
pg 125 Retrieved from http://web.mit.edu/cfgold/www/Homepage/Thesis_files/Thesis.pdf

(2750, 2850, 3), 	#C-H stretch
(1350, 1500, 2), 	#R-C-H bend
(700, 800, 1),		#R-C-H rock
(1000, 1100, 1),	#R-C-H rock
(1350, 1400, 1),	#Umbrella
(900, 1100, 1),
""",
)

entry(
    index = 4,
    label = "Cs-halhalhalCs_42",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Val7 u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (155, 231, 1),
            (254, 336, 1),
            (519, 583, 1),
            (532, 644, 1),
            (578, 734, 1),
            (1096, 1196, 1),
            (1166, 1218, 1),
            (1291, 1409, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 5,
    label = "Cs-F1sF1sF1sCs_42",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (155, 231, 1),
            (254, 336, 1),
            (519, 583, 1),
            (532, 644, 1),
            (578, 734, 1),
            (1096, 1196, 1),
            (1166, 1218, 1),
            (1291, 1409, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 6,
    label = "Cs-F1sF1sF1sCs_86",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   Cs  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (198, 308, 1),
            (478, 566, 1),
            (488, 682, 1),
            (563, 657, 1),
            (770, 928, 1),
            (1136, 1184, 1),
            (1168, 1262, 1),
            (1320, 1484, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 7,
    label = "Cs-Br1sBr1sBr1sCs_236",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (115, 145, 1),
            (130, 226, 1),
            (135, 151, 1),
            (189, 213, 1),
            (220, 290, 1),
            (444, 604, 1),
            (559, 635, 1),
            (972, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 8,
    label = "Cs-Br1sBr1sBr1sCs_284",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (133, 147, 1),
            (144, 168, 1),
            (183, 201, 1),
            (227, 265, 1),
            (230, 376, 1),
            (452, 558, 1),
            (582, 696, 1),
            (1063, 1205, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 9,
    label = "Cs-Cl1sCl1sCl1sCs_377",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (146, 194, 1),
            (198, 242, 1),
            (244, 278, 1),
            (285, 337, 1),
            (337, 483, 1),
            (593, 691, 1),
            (746, 826, 1),
            (963, 1097, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 10,
    label = "Cs-Cl1sCl1sCl1sCs_396",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (204, 246, 1),
            (244, 280, 1),
            (244, 334, 1),
            (394, 484, 1),
            (533, 661, 1),
            (640, 742, 1),
            (763, 883, 1),
            (1055, 1213, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 11,
    label = "Cs-Br1sF1sF1sCs_530",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (125, 215, 1),
            (234, 332, 1),
            (271, 313, 1),
            (450, 666, 1),
            (518, 636, 1),
            (944, 1140, 1),
            (1118, 1198, 1),
            (1118, 1254, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 12,
    label = "Cs-Br1sF1sF1sCs_599",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (114, 210, 1),
            (231, 277, 1),
            (234, 322, 1),
            (484, 698, 1),
            (489, 631, 1),
            (555, 613, 1),
            (1059, 1259, 1),
            (1173, 1259, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 13,
    label = "Cs-Br1sCl1sCl1sCs_546",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (50, 262, 1),
            (154, 304, 1),
            (185, 213, 1),
            (208, 244, 1),
            (234, 314, 1),
            (484, 630, 1),
            (657, 795, 1),
            (989, 1123, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 14,
    label = "Cs-Br1sCl1sCl1sCs_601",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (139, 179, 1),
            (178, 198, 1),
            (221, 285, 1),
            (267, 353, 1),
            (285, 485, 1),
            (505, 641, 1),
            (639, 815, 1),
            (1019, 1207, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 15,
    label = "Cs-Br1sCl1sF1sCs_580",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (187, 213, 1),
            (258, 304, 1),
            (263, 359, 1),
            (371, 517, 1),
            (499, 635, 1),
            (667, 883, 1),
            (1050, 1228, 1),
            (1068, 1154, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 16,
    label = "Cs-Br1sCl1sF1sCs_569",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (169, 193, 1),
            (208, 326, 1),
            (218, 266, 1),
            (366, 498, 1),
            (507, 591, 1),
            (531, 671, 1),
            (549, 773, 1),
            (1139, 1255, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 17,
    label = "Cs-Br1sBr1sF1sCs_586",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (55, 209, 1),
            (127, 235, 1),
            (147, 163, 1),
            (251, 351, 1),
            (262, 316, 1),
            (501, 627, 1),
            (976, 1150, 1),
            (1062, 1152, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 18,
    label = "Cs-Br1sBr1sF1sCs_561",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (15, 245, 1),
            (94, 266, 1),
            (136, 156, 1),
            (144, 254, 1),
            (225, 283, 1),
            (454, 624, 1),
            (542, 628, 1),
            (1118, 1284, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 19,
    label = "Cs-Br1sBr1sCl1sCs_588",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (79, 195, 1),
            (147, 165, 1),
            (190, 208, 1),
            (214, 316, 1),
            (225, 263, 1),
            (449, 599, 1),
            (616, 726, 1),
            (969, 1109, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 20,
    label = "Cs-Br1sBr1sCl1sCs_611",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (73, 267, 1),
            (140, 158, 1),
            (166, 190, 1),
            (171, 291, 1),
            (221, 265, 1),
            (448, 570, 1),
            (626, 780, 1),
            (1025, 1203, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 21,
    label = "Cs-Cl1sF1sF1sCs_603",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (142, 234, 1),
            (289, 351, 1),
            (358, 472, 1),
            (375, 529, 1),
            (534, 654, 1),
            (594, 754, 1),
            (1096, 1262, 1),
            (1112, 1198, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 22,
    label = "Cs-Cl1sF1sF1sCs_568",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (150, 292, 1),
            (277, 337, 1),
            (418, 514, 1),
            (527, 611, 1),
            (567, 705, 1),
            (766, 942, 1),
            (1078, 1234, 1),
            (1184, 1238, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 23,
    label = "Cs-Cl1sCl1sF1sCs_651",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (229, 289, 1),
            (282, 366, 1),
            (316, 502, 1),
            (378, 484, 1),
            (544, 680, 1),
            (728, 894, 1),
            (1007, 1185, 1),
            (1078, 1178, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 24,
    label = "Cs-Cl1sCl1sF1sCs_647",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (230, 280, 1),
            (265, 349, 1),
            (387, 483, 1),
            (501, 629, 1),
            (560, 722, 1),
            (647, 871, 1),
            (1016, 1192, 1),
            (1115, 1245, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 25,
    label = "Cs-halCsHH_48",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (442, 614, 1),
            (1089, 1143, 1),
            (1126, 1238, 1),
            (1254, 1408, 1),
            (1339, 1465, 1),
            (1463, 1525, 1),
            (3023, 3127, 1),
            (3088, 3132, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 26,
    label = "Cs-F1sCsHH_48",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (442, 614, 1),
            (1089, 1143, 1),
            (1126, 1238, 1),
            (1254, 1408, 1),
            (1339, 1465, 1),
            (1463, 1525, 1),
            (3023, 3127, 1),
            (3088, 3132, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 27,
    label = "Cs-F1sCsHH_67",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  u1 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (487, 615, 1),
            (1046, 1130, 1),
            (1173, 1279, 1),
            (1303, 1457, 1),
            (1390, 1450, 1),
            (1428, 1534, 1),
            (3009, 3105, 1),
            (3044, 3194, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 28,
    label = "Cs-Br1sCsHH_219",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (164, 210, 1),
            (578, 648, 1),
            (1078, 1138, 1),
            (1184, 1248, 1),
            (1239, 1363, 1),
            (1414, 1510, 1),
            (3131, 3235, 1),
            (3146, 3194, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 29,
    label = "Cs-Br1sCsHH_222",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   u1 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (175, 261, 1),
            (580, 722, 1),
            (1087, 1237, 1),
            (1114, 1172, 1),
            (1134, 1214, 1),
            (1460, 1492, 1),
            (3116, 3198, 1),
            (3177, 3225, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 30,
    label = "Cs-Cl1sCsHH_365",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (170, 234, 1),
            (715, 827, 1),
            (1049, 1135, 1),
            (1170, 1248, 1),
            (1275, 1393, 1),
            (1424, 1506, 1),
            (3071, 3165, 1),
            (3145, 3185, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 31,
    label = "Cs-Cl1sCsHH_373",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   u1 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (441, 547, 1),
            (558, 682, 1),
            (1099, 1195, 1),
            (1163, 1327, 1),
            (1199, 1283, 1),
            (1460, 1490, 1),
            (3092, 3182, 1),
            (3153, 3199, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 32,
    label = "Cs-halhalCsH_52",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (176, 294, 1),
            (457, 589, 1),
            (547, 707, 1),
            (1086, 1160, 1),
            (1127, 1157, 1),
            (1302, 1442, 1),
            (1365, 1447, 1),
            (3042, 3152, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 33,
    label = "Cs-F1sF1sCsH_52",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (176, 294, 1),
            (457, 589, 1),
            (547, 707, 1),
            (1086, 1160, 1),
            (1127, 1157, 1),
            (1302, 1442, 1),
            (1365, 1447, 1),
            (3042, 3152, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 34,
    label = "Cs-F1sF1sCsH_84",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (463, 581, 1),
            (545, 677, 1),
            (848, 1004, 1),
            (1037, 1149, 1),
            (1097, 1177, 1),
            (1301, 1447, 1),
            (1377, 1455, 1),
            (3039, 3185, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 35,
    label = "Cs-Br1sBr1sCsH_215",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (153, 169, 1),
            (195, 243, 1),
            (529, 601, 1),
            (589, 689, 1),
            (1116, 1166, 1),
            (1152, 1194, 1),
            (1279, 1441, 1),
            (3140, 3208, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 36,
    label = "Cs-Br1sBr1sCsH_237",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (108, 214, 1),
            (137, 157, 1),
            (167, 247, 1),
            (548, 616, 1),
            (1044, 1184, 1),
            (1106, 1180, 1),
            (1126, 1236, 1),
            (3162, 3224, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 37,
    label = "Cs-Cl1sCl1sCsH_371",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (146, 216, 1),
            (213, 271, 1),
            (609, 693, 1),
            (752, 866, 1),
            (1068, 1184, 1),
            (1191, 1269, 1),
            (1273, 1429, 1),
            (3122, 3202, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 38,
    label = "Cs-Cl1sCl1sCsH_374",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (133, 213, 1),
            (195, 265, 1),
            (540, 636, 1),
            (563, 713, 1),
            (1152, 1222, 1),
            (1178, 1282, 1),
            (1295, 1465, 1),
            (3144, 3210, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 39,
    label = "Cs-Br1sF1sCsH_533",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (223, 333, 1),
            (383, 579, 1),
            (610, 782, 1),
            (817, 981, 1),
            (1094, 1168, 1),
            (1112, 1324, 1),
            (1252, 1402, 1),
            (3061, 3189, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 40,
    label = "Cs-Br1sF1sCsH_541",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (57, 205, 1),
            (151, 253, 1),
            (457, 601, 1),
            (465, 683, 1),
            (1043, 1195, 1),
            (1146, 1214, 1),
            (1324, 1492, 1),
            (3083, 3219, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 41,
    label = "Cs-Br1sCl1sCsH_536",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (129, 223, 1),
            (156, 364, 1),
            (186, 226, 1),
            (581, 699, 1),
            (1068, 1170, 1),
            (1157, 1251, 1),
            (1271, 1479, 1),
            (3104, 3220, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 42,
    label = "Cs-Br1sCl1sCsH_562",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (139, 257, 1),
            (158, 202, 1),
            (298, 470, 1),
            (604, 732, 1),
            (1076, 1166, 1),
            (1121, 1349, 1),
            (1135, 1297, 1),
            (3132, 3246, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 43,
    label = "Cs-Cl1sF1sCsH_544",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (127, 227, 1),
            (263, 397, 1),
            (450, 626, 1),
            (1085, 1149, 1),
            (1107, 1249, 1),
            (1279, 1407, 1),
            (1397, 1543, 1),
            (3074, 3168, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 44,
    label = "Cs-Cl1sF1sCsH_564",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (140, 258, 1),
            (274, 472, 1),
            (445, 563, 1),
            (560, 670, 1),
            (1143, 1227, 1),
            (1158, 1286, 1),
            (1380, 1490, 1),
            (3095, 3195, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 45,
    label = "Cs-halO2sHH_57",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (490, 606, 1),
            (1063, 1107, 1),
            (1163, 1203, 1),
            (1255, 1349, 1),
            (1444, 1488, 1),
            (1481, 1559, 1),
            (3003, 3117, 1),
            (3089, 3149, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 46,
    label = "Cs-F1sO2sHH_57",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (490, 606, 1),
            (1063, 1107, 1),
            (1163, 1203, 1),
            (1255, 1349, 1),
            (1444, 1488, 1),
            (1481, 1559, 1),
            (3003, 3117, 1),
            (3089, 3149, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 47,
    label = "Cs-F1sO2sHH_184",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s u1 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (558, 558, 1),
            (760, 760, 1),
            (1040, 1040, 1),
            (1161, 1161, 1),
            (1162, 1162, 1),
            (1315, 1315, 1),
            (1378, 1378, 1),
            (2858, 2858, 1),
            (2872, 2872, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 48,
    label = "Cs-Br1sO2sHH_235",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (241, 323, 1),
            (560, 606, 1),
            (1103, 1175, 1),
            (1252, 1296, 1),
            (1280, 1388, 1),
            (1464, 1502, 1),
            (3091, 3161, 1),
            (3155, 3249, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 49,
    label = "Cs-Br1sO2sHH_278",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  u1 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (297, 297, 1),
            (532, 532, 1),
            (562, 562, 1),
            (988, 988, 1),
            (1137, 1137, 1),
            (1189, 1189, 1),
            (1302, 1302, 1),
            (2927, 2927, 1),
            (2969, 2969, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 50,
    label = "Cs-Cl1sO2sHH_409",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (283, 403, 1),
            (617, 713, 1),
            (1096, 1192, 1),
            (1273, 1339, 1),
            (1296, 1428, 1),
            (1442, 1522, 1),
            (3091, 3157, 1),
            (3128, 3244, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 51,
    label = "Cs-Cl1sO2sHH_525",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  u1 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (378, 378, 1),
            (650, 650, 1),
            (651, 651, 1),
            (1030, 1030, 1),
            (1153, 1153, 1),
            (1235, 1235, 1),
            (1310, 1310, 1),
            (2923, 2923, 1),
            (2961, 2961, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 52,
    label = "Cs-halhalhalO2s_58",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Val7 u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (395, 467, 1),
            (475, 579, 1),
            (579, 647, 1),
            (616, 720, 1),
            (753, 917, 1),
            (1175, 1223, 1),
            (1210, 1280, 1),
            (1259, 1385, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 53,
    label = "Cs-F1sF1sF1sO2s_58",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   O2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (395, 467, 1),
            (475, 579, 1),
            (579, 647, 1),
            (616, 720, 1),
            (753, 917, 1),
            (1175, 1223, 1),
            (1210, 1280, 1),
            (1259, 1385, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 54,
    label = "Cs-F1sF1sF1sO2s_197",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   O2s u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (268, 268, 1),
            (397, 397, 1),
            (573, 573, 1),
            (594, 594, 1),
            (616, 616, 1),
            (900, 900, 1),
            (1178, 1178, 1),
            (1236, 1236, 1),
            (1267, 1267, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 55,
    label = "Cs-Br1sBr1sBr1sO2s_251",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (139, 165, 1),
            (140, 148, 1),
            (183, 213, 1),
            (255, 333, 1),
            (290, 392, 1),
            (477, 619, 1),
            (603, 687, 1),
            (734, 868, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 56,
    label = "Cs-Cl1sCl1sCl1sO2s_390",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (220, 252, 1),
            (229, 275, 1),
            (273, 337, 1),
            (349, 419, 1),
            (400, 496, 1),
            (506, 648, 1),
            (774, 872, 1),
            (828, 976, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 57,
    label = "Cs-Cl1sCl1sCl1sO2s_515",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   O2s  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (194, 194, 1),
            (224, 224, 1),
            (314, 314, 1),
            (361, 361, 1),
            (363, 363, 1),
            (459, 459, 1),
            (549, 549, 1),
            (739, 739, 1),
            (1198, 1198, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 58,
    label = "Cs-Br1sF1sF1sO2s_531",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (244, 388, 1),
            (274, 310, 1),
            (277, 335, 1),
            (465, 595, 1),
            (573, 683, 1),
            (751, 945, 1),
            (1152, 1214, 1),
            (1175, 1339, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 59,
    label = "Cs-Br1sBr1sF1sO2s_559",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (95, 183, 1),
            (149, 173, 1),
            (278, 396, 1),
            (284, 304, 1),
            (288, 338, 1),
            (554, 670, 1),
            (741, 931, 1),
            (1135, 1233, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 60,
    label = "Cs-Cl1sCl1sF1sO2s_572",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (218, 270, 1),
            (269, 349, 1),
            (367, 427, 1),
            (372, 474, 1),
            (437, 577, 1),
            (613, 701, 1),
            (802, 916, 1),
            (1133, 1275, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 61,
    label = "Cs-Br1sCl1sCl1sO2s_596",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (189, 207, 1),
            (199, 231, 1),
            (257, 297, 1),
            (289, 361, 1),
            (383, 461, 1),
            (475, 623, 1),
            (657, 739, 1),
            (795, 915, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 62,
    label = "Cs-Br1sCl1sF1sO2s_615",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (191, 223, 1),
            (277, 315, 1),
            (282, 352, 1),
            (364, 470, 1),
            (445, 601, 1),
            (573, 705, 1),
            (774, 904, 1),
            (1139, 1251, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 63,
    label = "Cs-Cl1sF1sF1sO2s_626",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (273, 355, 1),
            (329, 425, 1),
            (385, 501, 1),
            (480, 594, 1),
            (566, 714, 1),
            (872, 1028, 1),
            (1150, 1216, 1),
            (1167, 1339, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 64,
    label = "Cs-Cl1sF1sF1sO2s_630",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   O2s  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (269, 269, 1),
            (279, 279, 1),
            (389, 389, 1),
            (555, 555, 1),
            (569, 569, 1),
            (583, 583, 1),
            (908, 908, 1),
            (1221, 1221, 1),
            (1337, 1337, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 65,
    label = "Cs-Br1sBr1sCl1sO2s_636",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (145, 165, 1),
            (186, 196, 1),
            (214, 258, 1),
            (241, 323, 1),
            (352, 450, 1),
            (483, 633, 1),
            (617, 749, 1),
            (792, 928, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 66,
    label = "Cs-halhalhalCd_59",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Val7 u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (181, 257, 1),
            (234, 358, 1),
            (513, 659, 1),
            (527, 601, 1),
            (651, 785, 1),
            (734, 852, 1),
            (1160, 1194, 1),
            (1194, 1262, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 67,
    label = "Cs-F1sF1sF1sCd_59",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   Cd  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (181, 257, 1),
            (234, 358, 1),
            (513, 659, 1),
            (527, 601, 1),
            (651, 785, 1),
            (734, 852, 1),
            (1160, 1194, 1),
            (1194, 1262, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 68,
    label = "Cs-F1sF1sF1sCd_135",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   Cd  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (101, 161, 1),
            (254, 414, 1),
            (507, 595, 1),
            (555, 645, 1),
            (616, 744, 1),
            (767, 897, 1),
            (943, 1183, 1),
            (1137, 1187, 1),
            (1164, 1224, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 69,
    label = "Cs-Br1sBr1sBr1sCd_265",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (106, 282, 1),
            (135, 153, 1),
            (146, 164, 1),
            (181, 211, 1),
            (208, 274, 1),
            (250, 324, 1),
            (596, 674, 1),
            (675, 763, 1),
            (716, 876, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 70,
    label = "Cs-Br1sBr1sBr1sCd_318",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (77, 125, 1),
            (129, 151, 1),
            (134, 154, 1),
            (167, 203, 1),
            (210, 322, 1),
            (228, 378, 1),
            (426, 572, 1),
            (537, 649, 1),
            (623, 705, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 71,
    label = "Cs-Cl1sCl1sCl1sCd_383",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (103, 247, 1),
            (179, 221, 1),
            (217, 263, 1),
            (220, 334, 1),
            (258, 318, 1),
            (541, 637, 1),
            (688, 808, 1),
            (748, 810, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 72,
    label = "Cs-Cl1sCl1sCl1sCd_462",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (84, 126, 1),
            (186, 248, 1),
            (198, 284, 1),
            (246, 350, 1),
            (331, 483, 1),
            (495, 639, 1),
            (641, 727, 1),
            (670, 784, 1),
            (764, 942, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 73,
    label = "Cs-Br1sCl1sF1sCd_542",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (182, 202, 1),
            (217, 267, 1),
            (222, 392, 1),
            (271, 321, 1),
            (325, 491, 1),
            (560, 700, 1),
            (784, 900, 1),
            (1089, 1209, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 74,
    label = "Cs-Br1sCl1sF1sCd_656",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (95, 129, 1),
            (179, 205, 1),
            (209, 271, 1),
            (266, 292, 1),
            (356, 478, 1),
            (491, 575, 1),
            (492, 672, 1),
            (615, 711, 1),
            (883, 1097, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 75,
    label = "Cs-Cl1sCl1sF1sCd_548",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (221, 251, 1),
            (235, 319, 1),
            (269, 415, 1),
            (332, 462, 1),
            (412, 594, 1),
            (660, 770, 1),
            (794, 892, 1),
            (822, 982, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 76,
    label = "Cs-Cl1sCl1sF1sCd_668",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (122, 160, 1),
            (228, 256, 1),
            (263, 313, 1),
            (281, 379, 1),
            (380, 500, 1),
            (455, 583, 1),
            (637, 767, 1),
            (680, 930, 1),
            (821, 1035, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 77,
    label = "Cs-Br1sF1sF1sCd_553",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (128, 200, 1),
            (238, 370, 1),
            (265, 331, 1),
            (274, 300, 1),
            (531, 671, 1),
            (769, 913, 1),
            (1057, 1239, 1),
            (1129, 1209, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 78,
    label = "Cs-Br1sF1sF1sCd_534",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (96, 132, 1),
            (181, 393, 1),
            (236, 268, 1),
            (259, 301, 1),
            (501, 581, 1),
            (541, 765, 1),
            (574, 654, 1),
            (777, 869, 1),
            (1149, 1193, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 79,
    label = "Cs-Br1sCl1sCl1sCd_578",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (168, 204, 1),
            (194, 368, 1),
            (201, 231, 1),
            (207, 269, 1),
            (243, 341, 1),
            (516, 652, 1),
            (684, 854, 1),
            (729, 831, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 80,
    label = "Cs-Br1sCl1sCl1sCd_692",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (65, 105, 1),
            (177, 195, 1),
            (194, 196, 1),
            (249, 309, 1),
            (261, 273, 1),
            (390, 442, 1),
            (491, 579, 1),
            (553, 729, 1),
            (800, 1060, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 81,
    label = "Cs-Br1sBr1sCl1sCd_591",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (103, 229, 1),
            (136, 160, 1),
            (185, 211, 1),
            (206, 260, 1),
            (223, 309, 1),
            (485, 649, 1),
            (663, 847, 1),
            (674, 804, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 82,
    label = "Cs-Br1sBr1sCl1sCd_649",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (72, 110, 1),
            (130, 168, 1),
            (162, 202, 1),
            (207, 243, 1),
            (216, 290, 1),
            (294, 332, 1),
            (373, 567, 1),
            (505, 665, 1),
            (622, 772, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 83,
    label = "Cs-Br1sBr1sF1sCd_623",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (39, 245, 1),
            (136, 160, 1),
            (165, 247, 1),
            (254, 316, 1),
            (271, 331, 1),
            (593, 743, 1),
            (773, 901, 1),
            (1072, 1202, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 84,
    label = "Cs-Br1sBr1sF1sCd_639",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (85, 119, 1),
            (133, 169, 1),
            (188, 270, 1),
            (258, 354, 1),
            (263, 295, 1),
            (393, 601, 1),
            (549, 759, 1),
            (588, 702, 1),
            (995, 1147, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 85,
    label = "Cs-Cl1sF1sF1sCd_633",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (216, 292, 1),
            (300, 348, 1),
            (328, 488, 1),
            (430, 630, 1),
            (603, 723, 1),
            (805, 921, 1),
            (1012, 1218, 1),
            (1125, 1225, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 86,
    label = "Cs-Cl1sF1sF1sCd_677",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (129, 165, 1),
            (242, 312, 1),
            (290, 366, 1),
            (319, 417, 1),
            (517, 545, 1),
            (582, 650, 1),
            (650, 692, 1),
            (820, 892, 1),
            (1151, 1195, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 87,
    label = "Cs-halhalCtH_69",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (95, 191, 1),
            (383, 525, 1),
            (603, 657, 1),
            (831, 1029, 1),
            (1099, 1115, 1),
            (1121, 1215, 1),
            (1385, 1401, 1),
            (2976, 3114, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 88,
    label = "Cs-F1sF1sCtH_69",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Ct  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (95, 191, 1),
            (383, 525, 1),
            (603, 657, 1),
            (831, 1029, 1),
            (1099, 1115, 1),
            (1121, 1215, 1),
            (1385, 1401, 1),
            (2976, 3114, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 89,
    label = "Cs-Br1sBr1sCtH_299",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (135, 175, 1),
            (201, 305, 1),
            (308, 410, 1),
            (344, 426, 1),
            (599, 653, 1),
            (1103, 1167, 1),
            (1144, 1240, 1),
            (3137, 3175, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 90,
    label = "Cs-Cl1sCl1sCtH_420",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (216, 278, 1),
            (242, 392, 1),
            (360, 452, 1),
            (662, 700, 1),
            (676, 718, 1),
            (1150, 1238, 1),
            (1204, 1250, 1),
            (3106, 3166, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 91,
    label = "Cs-Cl1sF1sCtH_538",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (157, 273, 1),
            (347, 395, 1),
            (372, 536, 1),
            (682, 752, 1),
            (1028, 1140, 1),
            (1205, 1299, 1),
            (1228, 1362, 1),
            (3044, 3142, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 92,
    label = "Cs-Br1sCl1sCtH_579",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (144, 302, 1),
            (179, 235, 1),
            (345, 489, 1),
            (550, 726, 1),
            (668, 716, 1),
            (1115, 1203, 1),
            (1201, 1271, 1),
            (3121, 3173, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 93,
    label = "Cs-Br1sF1sCtH_660",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (64, 282, 1),
            (257, 305, 1),
            (272, 424, 1),
            (595, 717, 1),
            (1008, 1132, 1),
            (1148, 1214, 1),
            (1254, 1390, 1),
            (3068, 3148, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 94,
    label = "Cs-halhalO2sH_70",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   O2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (480, 558, 1),
            (523, 663, 1),
            (745, 915, 1),
            (1086, 1144, 1),
            (1147, 1185, 1),
            (1338, 1440, 1),
            (1394, 1432, 1),
            (3056, 3172, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 95,
    label = "Cs-F1sF1sO2sH_70",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (480, 558, 1),
            (523, 663, 1),
            (745, 915, 1),
            (1086, 1144, 1),
            (1147, 1185, 1),
            (1338, 1440, 1),
            (1394, 1432, 1),
            (3056, 3172, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 96,
    label = "Cs-F1sF1sO2sH_174",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (480, 480, 1),
            (502, 502, 1),
            (615, 615, 1),
            (942, 942, 1),
            (1118, 1118, 1),
            (1159, 1159, 1),
            (1274, 1274, 1),
            (1324, 1324, 1),
            (2842, 2842, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 97,
    label = "Cs-Br1sBr1sO2sH_248",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (152, 174, 1),
            (242, 326, 1),
            (373, 503, 1),
            (585, 635, 1),
            (638, 768, 1),
            (1137, 1179, 1),
            (1300, 1406, 1),
            (3137, 3229, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 98,
    label = "Cs-Cl1sCl1sO2sH_393",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (212, 274, 1),
            (316, 406, 1),
            (491, 633, 1),
            (672, 756, 1),
            (751, 897, 1),
            (1197, 1241, 1),
            (1296, 1418, 1),
            (3123, 3219, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 99,
    label = "Cs-Cl1sCl1sO2sH_484",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (262, 262, 1),
            (312, 312, 1),
            (399, 399, 1),
            (602, 602, 1),
            (657, 657, 1),
            (1015, 1015, 1),
            (1106, 1106, 1),
            (1133, 1133, 1),
            (2885, 2885, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 100,
    label = "Cs-Cl1sF1sO2sH_540",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (287, 465, 1),
            (343, 409, 1),
            (568, 706, 1),
            (802, 954, 1),
            (1114, 1180, 1),
            (1270, 1354, 1),
            (1333, 1459, 1),
            (3081, 3201, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 101,
    label = "Cs-Cl1sF1sO2sH_704",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (236, 236, 1),
            (336, 336, 1),
            (486, 486, 1),
            (601, 601, 1),
            (1043, 1043, 1),
            (1123, 1123, 1),
            (1198, 1198, 1),
            (1371, 1371, 1),
            (3042, 3042, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 102,
    label = "Cs-Br1sF1sO2sH_589",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (170, 254, 1),
            (264, 352, 1),
            (553, 701, 1),
            (774, 958, 1),
            (1137, 1201, 1),
            (1227, 1317, 1),
            (1325, 1429, 1),
            (3079, 3215, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 103,
    label = "Cs-Br1sCl1sO2sH_597",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (191, 229, 1),
            (219, 335, 1),
            (371, 515, 1),
            (604, 674, 1),
            (757, 905, 1),
            (1175, 1223, 1),
            (1289, 1419, 1),
            (3115, 3243, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 104,
    label = "Cs-halCtHH_72",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Ct   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (255, 383, 1),
            (995, 1051, 1),
            (1036, 1106, 1),
            (1217, 1301, 1),
            (1232, 1402, 1),
            (1366, 1452, 1),
            (3002, 3106, 1),
            (3004, 3034, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 105,
    label = "Cs-F1sCtHH_72",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Ct  ux {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (255, 383, 1),
            (995, 1051, 1),
            (1036, 1106, 1),
            (1217, 1301, 1),
            (1232, 1402, 1),
            (1366, 1452, 1),
            (3002, 3106, 1),
            (3004, 3034, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 106,
    label = "Cs-Br1sCtHH_269",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Ct   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (261, 315, 1),
            (321, 415, 1),
            (755, 879, 1),
            (831, 901, 1),
            (1148, 1162, 1),
            (1181, 1211, 1),
            (3084, 3104, 1),
            (3137, 3165, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 107,
    label = "Cs-Cl1sCtHH_405",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Ct   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (261, 359, 1),
            (655, 729, 1),
            (748, 904, 1),
            (881, 939, 1),
            (1169, 1191, 1),
            (1250, 1278, 1),
            (3065, 3093, 1),
            (3104, 3156, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 108,
    label = "Cs-halCdHH_75",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Cd   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (166, 258, 1),
            (854, 1008, 1),
            (1066, 1142, 1),
            (1198, 1304, 1),
            (1253, 1397, 1),
            (1428, 1520, 1),
            (3056, 3148, 1),
            (3059, 3251, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 109,
    label = "Cs-F1sCdHH_75",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cd  ux {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (166, 258, 1),
            (854, 1008, 1),
            (1066, 1142, 1),
            (1198, 1304, 1),
            (1253, 1397, 1),
            (1428, 1520, 1),
            (3056, 3148, 1),
            (3059, 3251, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 110,
    label = "Cs-F1sCdHH_95",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cd  u1 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (98, 146, 1),
            (536, 632, 1),
            (875, 989, 1),
            (1009, 1077, 1),
            (1202, 1292, 1),
            (1337, 1447, 1),
            (1384, 1538, 1),
            (2913, 3059, 1),
            (3013, 3065, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 111,
    label = "Cs-Br1sCdHH_228",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (154, 226, 1),
            (591, 677, 1),
            (848, 900, 1),
            (1134, 1192, 1),
            (1142, 1280, 1),
            (1200, 1262, 1),
            (3116, 3228, 1),
            (3167, 3203, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 112,
    label = "Cs-Br1sCdHH_282",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cd   u1 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (41, 143, 1),
            (190, 368, 1),
            (533, 631, 1),
            (837, 865, 1),
            (1093, 1153, 1),
            (1143, 1203, 1),
            (1405, 1501, 1),
            (3055, 3129, 1),
            (3107, 3149, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 113,
    label = "Cs-Cl1sCdHH_375",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (183, 259, 1),
            (673, 773, 1),
            (848, 936, 1),
            (1141, 1209, 1),
            (1202, 1296, 1),
            (1337, 1491, 1),
            (3096, 3218, 1),
            (3148, 3190, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 114,
    label = "Cs-Cl1sCdHH_394",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cd   u1 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (88, 164, 1),
            (506, 640, 1),
            (588, 760, 1),
            (849, 923, 1),
            (1125, 1177, 1),
            (1163, 1265, 1),
            (1367, 1507, 1),
            (3029, 3127, 1),
            (3099, 3121, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 115,
    label = "Cs-halhalhalCO_94",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Val7 u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (209, 251, 1),
            (227, 321, 1),
            (538, 636, 1),
            (609, 747, 1),
            (733, 847, 1),
            (1189, 1223, 1),
            (1213, 1269, 1),
            (1263, 1365, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 116,
    label = "Cs-F1sF1sF1sCO_94",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (209, 251, 1),
            (227, 321, 1),
            (538, 636, 1),
            (609, 747, 1),
            (733, 847, 1),
            (1189, 1223, 1),
            (1213, 1269, 1),
            (1263, 1365, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 117,
    label = "Cs-F1sF1sF1sCO_172",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   CO  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (230, 230, 1),
            (386, 386, 1),
            (530, 530, 1),
            (542, 542, 1),
            (666, 666, 1),
            (1153, 1153, 1),
            (1221, 1221, 1),
            (1240, 1240, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 118,
    label = "Cs-Br1sBr1sBr1sCO_341",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (129, 141, 1),
            (151, 169, 1),
            (162, 364, 1),
            (182, 190, 1),
            (188, 220, 1),
            (213, 343, 1),
            (585, 671, 1),
            (1023, 1171, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 119,
    label = "Cs-Br1sBr1sBr1sCO_348",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (123, 123, 1),
            (146, 146, 1),
            (162, 162, 1),
            (198, 198, 1),
            (318, 318, 1),
            (351, 351, 1),
            (643, 643, 1),
            (675, 675, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 120,
    label = "Cs-Cl1sCl1sCl1sCO_471",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (82, 272, 1),
            (166, 202, 1),
            (178, 294, 1),
            (254, 288, 1),
            (262, 312, 1),
            (611, 691, 1),
            (810, 962, 1),
            (817, 841, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 121,
    label = "Cs-Cl1sCl1sCl1sCO_505",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (174, 174, 1),
            (250, 250, 1),
            (257, 257, 1),
            (307, 307, 1),
            (380, 380, 1),
            (572, 572, 1),
            (742, 742, 1),
            (777, 777, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 122,
    label = "Cs-Br1sBr1sF1sCO_556",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (141, 159, 1),
            (161, 237, 1),
            (219, 387, 1),
            (274, 324, 1),
            (303, 365, 1),
            (621, 703, 1),
            (884, 980, 1),
            (1118, 1240, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 123,
    label = "Cs-Br1sBr1sF1sCO_735",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (137, 137, 1),
            (169, 169, 1),
            (214, 214, 1),
            (300, 300, 1),
            (324, 324, 1),
            (548, 548, 1),
            (674, 674, 1),
            (1155, 1155, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 124,
    label = "Cs-Cl1sCl1sF1sCO_583",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (97, 255, 1),
            (185, 227, 1),
            (220, 306, 1),
            (306, 400, 1),
            (325, 439, 1),
            (775, 869, 1),
            (839, 981, 1),
            (1192, 1280, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 125,
    label = "Cs-Cl1sCl1sF1sCO_694",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (182, 182, 1),
            (245, 245, 1),
            (272, 272, 1),
            (382, 382, 1),
            (537, 537, 1),
            (570, 570, 1),
            (770, 770, 1),
            (1162, 1162, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 126,
    label = "Cs-Br1sBr1sCl1sCO_618",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (77, 271, 1),
            (134, 146, 1),
            (179, 379, 1),
            (194, 204, 1),
            (204, 218, 1),
            (225, 301, 1),
            (612, 672, 1),
            (1068, 1262, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 127,
    label = "Cs-Br1sBr1sCl1sCO_627",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (135, 135, 1),
            (163, 163, 1),
            (197, 197, 1),
            (241, 241, 1),
            (327, 327, 1),
            (399, 399, 1),
            (653, 653, 1),
            (726, 726, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 128,
    label = "Cs-Cl1sF1sF1sCO_622",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (154, 266, 1),
            (210, 274, 1),
            (330, 348, 1),
            (347, 483, 1),
            (575, 645, 1),
            (820, 924, 1),
            (1194, 1228, 1),
            (1225, 1337, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 129,
    label = "Cs-Cl1sF1sF1sCO_570",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (183, 183, 1),
            (346, 346, 1),
            (402, 402, 1),
            (422, 422, 1),
            (566, 566, 1),
            (667, 667, 1),
            (1156, 1156, 1),
            (1191, 1191, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 130,
    label = "Cs-Br1sCl1sCl1sCO_652",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (87, 271, 1),
            (164, 178, 1),
            (214, 228, 1),
            (227, 239, 1),
            (227, 327, 1),
            (564, 746, 1),
            (610, 698, 1),
            (796, 966, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 131,
    label = "Cs-Br1sCl1sCl1sCO_700",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (144, 144, 1),
            (205, 205, 1),
            (214, 214, 1),
            (273, 273, 1),
            (385, 385, 1),
            (508, 508, 1),
            (714, 714, 1),
            (739, 739, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 132,
    label = "Cs-Br1sF1sF1sCO_658",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (87, 225, 1),
            (211, 273, 1),
            (220, 372, 1),
            (264, 316, 1),
            (578, 614, 1),
            (803, 895, 1),
            (1175, 1243, 1),
            (1218, 1328, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 133,
    label = "Cs-Br1sF1sF1sCO_741",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (151, 151, 1),
            (302, 302, 1),
            (302, 302, 1),
            (419, 419, 1),
            (530, 530, 1),
            (655, 655, 1),
            (1153, 1153, 1),
            (1188, 1188, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 134,
    label = "Cs-Br1sCl1sF1sCO_714",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (111, 241, 1),
            (176, 190, 1),
            (221, 249, 1),
            (279, 333, 1),
            (335, 357, 1),
            (662, 726, 1),
            (887, 1005, 1),
            (1189, 1273, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 135,
    label = "Cs-Br1sCl1sF1sCO_712",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (173, 173, 1),
            (198, 198, 1),
            (222, 222, 1),
            (309, 309, 1),
            (394, 394, 1),
            (564, 564, 1),
            (715, 715, 1),
            (1160, 1160, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 136,
    label = "Cs-halhalCdH_97",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (87, 255, 1),
            (155, 255, 1),
            (543, 653, 1),
            (1088, 1120, 1),
            (1106, 1180, 1),
            (1251, 1383, 1),
            (1373, 1449, 1),
            (3068, 3238, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 137,
    label = "Cs-F1sF1sCdH_97",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cd  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (87, 255, 1),
            (155, 255, 1),
            (543, 653, 1),
            (1088, 1120, 1),
            (1106, 1180, 1),
            (1251, 1383, 1),
            (1373, 1449, 1),
            (3068, 3238, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 138,
    label = "Cs-F1sF1sCdH_109",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cd  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (83, 159, 1),
            (359, 559, 1),
            (503, 641, 1),
            (605, 791, 1),
            (1041, 1111, 1),
            (1094, 1146, 1),
            (1289, 1461, 1),
            (1298, 1416, 1),
            (2998, 3132, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 139,
    label = "Cs-Br1sBr1sCdH_229",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (55, 179, 1),
            (109, 197, 1),
            (143, 169, 1),
            (201, 289, 1),
            (635, 685, 1),
            (756, 904, 1),
            (1143, 1183, 1),
            (3160, 3234, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 140,
    label = "Cs-Br1sBr1sCdH_298",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cd   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (59, 97, 1),
            (131, 159, 1),
            (144, 266, 1),
            (233, 395, 1),
            (510, 586, 1),
            (568, 626, 1),
            (755, 925, 1),
            (1091, 1129, 1),
            (3140, 3174, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 141,
    label = "Cs-Cl1sCl1sCdH_367",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (160, 208, 1),
            (214, 290, 1),
            (229, 355, 1),
            (696, 738, 1),
            (718, 810, 1),
            (1152, 1246, 1),
            (1205, 1231, 1),
            (3155, 3241, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 142,
    label = "Cs-Cl1sCl1sCdH_426",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (83, 123, 1),
            (153, 263, 1),
            (237, 375, 1),
            (493, 611, 1),
            (638, 708, 1),
            (640, 776, 1),
            (1146, 1258, 1),
            (1154, 1224, 1),
            (3103, 3165, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 143,
    label = "Cs-Br1sF1sCdH_535",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (118, 192, 1),
            (150, 340, 1),
            (245, 331, 1),
            (625, 775, 1),
            (1085, 1287, 1),
            (1095, 1169, 1),
            (1184, 1272, 1),
            (3109, 3251, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 144,
    label = "Cs-Br1sF1sCdH_585",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (87, 141, 1),
            (218, 262, 1),
            (260, 468, 1),
            (480, 640, 1),
            (549, 661, 1),
            (823, 1023, 1),
            (1123, 1155, 1),
            (1139, 1281, 1),
            (3074, 3142, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 145,
    label = "Cs-Br1sCl1sCdH_551",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (65, 223, 1),
            (169, 297, 1),
            (171, 223, 1),
            (623, 741, 1),
            (726, 846, 1),
            (1150, 1212, 1),
            (1159, 1295, 1),
            (3142, 3248, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 146,
    label = "Cs-Br1sCl1sCdH_646",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (67, 93, 1),
            (101, 333, 1),
            (123, 195, 1),
            (210, 276, 1),
            (479, 617, 1),
            (635, 737, 1),
            (827, 981, 1),
            (1110, 1176, 1),
            (3121, 3175, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 147,
    label = "Cs-Cl1sF1sCdH_563",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (148, 226, 1),
            (234, 376, 1),
            (467, 671, 1),
            (721, 845, 1),
            (1076, 1186, 1),
            (1137, 1371, 1),
            (1208, 1304, 1),
            (3132, 3262, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 148,
    label = "Cs-Cl1sF1sCdH_624",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (90, 126, 1),
            (259, 349, 1),
            (447, 583, 1),
            (622, 732, 1),
            (738, 932, 1),
            (1011, 1157, 1),
            (1194, 1264, 1),
            (1249, 1447, 1),
            (3068, 3162, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 149,
    label = "Cs-halhalCOH_133",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (128, 262, 1),
            (227, 313, 1),
            (1096, 1198, 1),
            (1108, 1152, 1),
            (1283, 1435, 1),
            (1345, 1431, 1),
            (1384, 1434, 1),
            (3051, 3099, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 150,
    label = "Cs-F1sF1sCOH_133",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   CO  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (128, 262, 1),
            (227, 313, 1),
            (1096, 1198, 1),
            (1108, 1152, 1),
            (1283, 1435, 1),
            (1345, 1431, 1),
            (1384, 1434, 1),
            (3051, 3099, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 151,
    label = "Cs-F1sF1sCOH_191",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   CO  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (360, 360, 1),
            (407, 407, 1),
            (608, 608, 1),
            (1153, 1153, 1),
            (1157, 1157, 1),
            (1303, 1303, 1),
            (1378, 1378, 1),
            (3033, 3033, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 152,
    label = "Cs-Br1sBr1sCOH_256",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (92, 188, 1),
            (152, 160, 1),
            (169, 239, 1),
            (577, 649, 1),
            (1121, 1191, 1),
            (1138, 1216, 1),
            (1177, 1275, 1),
            (3150, 3206, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 153,
    label = "Cs-Br1sBr1sCOH_356",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   CO   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (145, 145, 1),
            (163, 163, 1),
            (307, 307, 1),
            (589, 589, 1),
            (626, 626, 1),
            (1127, 1127, 1),
            (1198, 1198, 1),
            (3174, 3174, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 154,
    label = "Cs-Cl1sCl1sCOH_418",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (156, 246, 1),
            (212, 284, 1),
            (217, 419, 1),
            (677, 751, 1),
            (1140, 1332, 1),
            (1162, 1264, 1),
            (1211, 1263, 1),
            (3123, 3203, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 155,
    label = "Cs-Cl1sCl1sCOH_495",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   CO   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (191, 191, 1),
            (265, 265, 1),
            (580, 580, 1),
            (673, 673, 1),
            (733, 733, 1),
            (1189, 1189, 1),
            (1234, 1234, 1),
            (3148, 3148, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 156,
    label = "Cs-Cl1sF1sCOH_574",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (110, 252, 1),
            (210, 302, 1),
            (335, 525, 1),
            (1081, 1153, 1),
            (1136, 1244, 1),
            (1281, 1391, 1),
            (1292, 1388, 1),
            (3055, 3175, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 157,
    label = "Cs-Cl1sF1sCOH_605",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   CO   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (184, 184, 1),
            (368, 368, 1),
            (535, 535, 1),
            (684, 684, 1),
            (1147, 1147, 1),
            (1206, 1206, 1),
            (1323, 1323, 1),
            (3064, 3064, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 158,
    label = "Cs-Br1sF1sCOH_612",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (65, 233, 1),
            (218, 366, 1),
            (230, 296, 1),
            (1081, 1145, 1),
            (1151, 1217, 1),
            (1215, 1335, 1),
            (1261, 1411, 1),
            (3071, 3183, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 159,
    label = "Cs-Br1sF1sCOH_736",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   CO   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (149, 149, 1),
            (299, 299, 1),
            (531, 531, 1),
            (598, 598, 1),
            (1136, 1136, 1),
            (1169, 1169, 1),
            (1317, 1317, 1),
            (3071, 3071, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 160,
    label = "Cs-Br1sCl1sCOH_632",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (63, 221, 1),
            (119, 215, 1),
            (190, 206, 1),
            (623, 689, 1),
            (1135, 1225, 1),
            (1139, 1323, 1),
            (1166, 1272, 1),
            (3118, 3218, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 161,
    label = "Cs-Br1sCl1sCOH_716",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   CO   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (185, 185, 1),
            (216, 216, 1),
            (302, 302, 1),
            (603, 603, 1),
            (709, 709, 1),
            (1140, 1140, 1),
            (1237, 1237, 1),
            (3166, 3166, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 162,
    label = "Cs-halCOHH_138",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   CO   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (183, 305, 1),
            (1070, 1134, 1),
            (1218, 1290, 1),
            (1318, 1440, 1),
            (1427, 1509, 1),
            (1467, 1483, 1),
            (2979, 3095, 1),
            (3058, 3108, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 163,
    label = "Cs-F1sCOHH_138",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   CO  ux {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (183, 305, 1),
            (1070, 1134, 1),
            (1218, 1290, 1),
            (1318, 1440, 1),
            (1427, 1509, 1),
            (1467, 1483, 1),
            (2979, 3095, 1),
            (3058, 3108, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 164,
    label = "Cs-F1sCOHH_182",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   CO  u1 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (310, 310, 1),
            (819, 819, 1),
            (1134, 1134, 1),
            (1239, 1239, 1),
            (1344, 1344, 1),
            (1458, 1458, 1),
            (3009, 3009, 1),
            (3067, 3067, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 165,
    label = "Cs-Br1sCOHH_301",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   CO   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (153, 229, 1),
            (606, 704, 1),
            (1069, 1143, 1),
            (1167, 1323, 1),
            (1199, 1241, 1),
            (1442, 1464, 1),
            (3094, 3140, 1),
            (3154, 3230, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 166,
    label = "Cs-Br1sCOHH_347",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   CO   u1 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (132, 132, 1),
            (565, 565, 1),
            (736, 736, 1),
            (1132, 1132, 1),
            (1189, 1189, 1),
            (1409, 1409, 1),
            (3102, 3102, 1),
            (3164, 3164, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 167,
    label = "Cs-Cl1sCOHH_401",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   CO   ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (177, 259, 1),
            (736, 802, 1),
            (886, 974, 1),
            (1136, 1212, 1),
            (1261, 1335, 1),
            (1435, 1453, 1),
            (3039, 3145, 1),
            (3120, 3170, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 168,
    label = "Cs-Cl1sCOHH_498",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   CO   u1 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (176, 176, 1),
            (664, 664, 1),
            (785, 785, 1),
            (1167, 1167, 1),
            (1250, 1250, 1),
            (1414, 1414, 1),
            (3088, 3088, 1),
            (3144, 3144, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 169,
    label = "Cs-halhalhalCt_158",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Val7 u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (76, 144, 1),
            (363, 497, 1),
            (416, 478, 1),
            (575, 687, 1),
            (600, 626, 1),
            (732, 812, 1),
            (1165, 1201, 1),
            (1180, 1192, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 170,
    label = "Cs-F1sF1sF1sCt_158",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (76, 144, 1),
            (363, 497, 1),
            (416, 478, 1),
            (575, 687, 1),
            (600, 626, 1),
            (732, 812, 1),
            (1165, 1201, 1),
            (1180, 1192, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 171,
    label = "Cs-Br1sBr1sBr1sCt_303",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (135, 155, 1),
            (141, 157, 1),
            (177, 215, 1),
            (246, 330, 1),
            (358, 458, 1),
            (364, 482, 1),
            (582, 718, 1),
            (645, 655, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 172,
    label = "Cs-Cl1sCl1sCl1sCt_387",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (107, 163, 1),
            (228, 248, 1),
            (239, 253, 1),
            (287, 315, 1),
            (334, 450, 1),
            (401, 467, 1),
            (679, 723, 1),
            (682, 768, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 173,
    label = "Cs-Br1sCl1sF1sCt_547",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (164, 236, 1),
            (240, 308, 1),
            (283, 325, 1),
            (335, 449, 1),
            (361, 401, 1),
            (535, 739, 1),
            (609, 759, 1),
            (913, 1075, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 174,
    label = "Cs-Br1sBr1sCl1sCt_555",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (144, 166, 1),
            (182, 198, 1),
            (206, 356, 1),
            (211, 273, 1),
            (250, 332, 1),
            (350, 428, 1),
            (612, 704, 1),
            (645, 751, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 175,
    label = "Cs-Cl1sCl1sF1sCt_557",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (192, 298, 1),
            (270, 352, 1),
            (337, 385, 1),
            (361, 453, 1),
            (403, 545, 1),
            (622, 722, 1),
            (665, 853, 1),
            (925, 1079, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 176,
    label = "Cs-Br1sF1sF1sCt_642",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (83, 149, 1),
            (267, 299, 1),
            (294, 304, 1),
            (357, 433, 1),
            (623, 709, 1),
            (740, 922, 1),
            (999, 1171, 1),
            (1143, 1183, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 177,
    label = "Cs-Br1sBr1sF1sCt_653",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (84, 166, 1),
            (146, 158, 1),
            (265, 375, 1),
            (284, 300, 1),
            (304, 360, 1),
            (343, 479, 1),
            (636, 692, 1),
            (815, 927, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 178,
    label = "Cs-Br1sCl1sCl1sCt_661",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (172, 218, 1),
            (189, 235, 1),
            (236, 302, 1),
            (271, 335, 1),
            (276, 462, 1),
            (359, 429, 1),
            (648, 712, 1),
            (653, 785, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 179,
    label = "Cs-Cl1sF1sF1sCt_687",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (74, 160, 1),
            (328, 360, 1),
            (365, 405, 1),
            (428, 456, 1),
            (525, 627, 1),
            (583, 793, 1),
            (958, 1142, 1),
            (1161, 1169, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 180,
    label = "Cs-halC2sHH_177",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   C2s  ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (199, 299, 1),
            (684, 784, 1),
            (1059, 1159, 1),
            (1205, 1305, 1),
            (1308, 1408, 1),
            (2933, 3033, 1),
            (2961, 3061, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 181,
    label = "Cs-F1sC2sHH_177",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   C2s ux {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (199, 299, 1),
            (684, 784, 1),
            (1059, 1159, 1),
            (1205, 1305, 1),
            (1308, 1408, 1),
            (2933, 3033, 1),
            (2961, 3061, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 182,
    label = "Cs-Br1sC2sHH_350",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   C2s  ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (340, 440, 1),
            (545, 645, 1),
            (600, 700, 1),
            (1016, 1116, 1),
            (2990, 3090, 1),
            (3035, 3135, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 183,
    label = "Cs-Cl1sC2sHH_521",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   C2s  ux {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (121, 221, 1),
            (603, 703, 1),
            (701, 801, 1),
            (1172, 1272, 1),
            (1302, 1402, 1),
            (2985, 3085, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 184,
    label = "Cs-halhalC2sH_183",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   C2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (207, 307, 1),
            (359, 459, 1),
            (1093, 1193, 1),
            (1311, 1411, 1),
            (2894, 2994, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 185,
    label = "Cs-F1sF1sC2sH_183",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   C2s ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (207, 307, 1),
            (359, 459, 1),
            (1093, 1193, 1),
            (1311, 1411, 1),
            (2894, 2994, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 186,
    label = "Cs-Br1sBr1sC2sH_332",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   C2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (210, 310, 1),
            (455, 555, 1),
            (502, 602, 1),
            (1008, 1108, 1),
            (1156, 1256, 1),
            (3115, 3215, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 187,
    label = "Cs-Cl1sCl1sC2sH_496",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   C2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (127, 227, 1),
            (206, 306, 1),
            (637, 737, 1),
            (1000, 1100, 1),
            (3099, 3199, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 188,
    label = "Cs-halhalhalC2s_194",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Val7 u0 {1,S}
5   C2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (211, 311, 1),
            (296, 396, 1),
            (479, 579, 1),
            (1181, 1281, 1),
            (1256, 1356, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 189,
    label = "Cs-F1sF1sF1sC2s_194",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   C2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (211, 311, 1),
            (296, 396, 1),
            (479, 579, 1),
            (1181, 1281, 1),
            (1256, 1356, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 190,
    label = "Cs-Cl1sCl1sCl1sC2s_507",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   C2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (118, 218, 1),
            (175, 275, 1),
            (246, 346, 1),
            (338, 438, 1),
            (742, 842, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 191,
    label = "RdCH2",
    group = 
"""
1 * C        u0 {2,D} {3,S} {4,S}
2   R!H!Val7 ux {1,D}
3   [H,Val7] u0 {1,S}
4   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2950, 3100, 2),
            (1330, 1430, 1),
            (900, 1050, 1),
            (1000, 1050, 1),
            (1600, 1700, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """Alkene end group""",
    longDesc = 
"""
(2950, 3100, 2),	#C-H stretch
(1330, 1430, 1),	#R-C-H scissor
(900, 1050, 1),		#R-C-H swing
(1000, 1050, 1),	#R-C-H rock
(1600, 1700, 1),
""",
)

entry(
    index = 192,
    label = "Cd-halCdH_45",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   Cd   ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (151, 237, 1),
            (609, 755, 1),
            (844, 966, 1),
            (1147, 1245, 1),
            (1323, 1443, 1),
            (3181, 3261, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 193,
    label = "Cd-F1sCdH_45",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   Cd  ux {1,D}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (151, 237, 1),
            (609, 755, 1),
            (844, 966, 1),
            (1147, 1245, 1),
            (1323, 1443, 1),
            (3181, 3261, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 194,
    label = "Cd-F1sCdH_85",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   Cd  u1 {1,D}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (535, 695, 1),
            (819, 901, 1),
            (1081, 1199, 1),
            (1292, 1394, 1),
            (3088, 3216, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 195,
    label = "Cd-Br1sCdH_225",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (145, 199, 1),
            (198, 300, 1),
            (658, 746, 1),
            (1143, 1245, 1),
            (1174, 1328, 1),
            (3223, 3267, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 196,
    label = "Cd-Br1sCdH_289",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   Cd   u1 {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (120, 208, 1),
            (518, 596, 1),
            (685, 809, 1),
            (1117, 1211, 1),
            (3187, 3261, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 197,
    label = "Cd-Br1sCdH_362",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   Cd   u2 {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (314, 314, 1),
            (508, 508, 1),
            (597, 597, 1),
            (1073, 1073, 1),
            (1186, 1186, 1),
            (3152, 3152, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 198,
    label = "Cd-Cl1sCdH_372",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (156, 230, 1),
            (613, 741, 1),
            (770, 876, 1),
            (1098, 1238, 1),
            (1254, 1406, 1),
            (3204, 3274, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 199,
    label = "Cd-Cl1sCdH_386",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   Cd   u1 {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (469, 605, 1),
            (636, 720, 1),
            (726, 866, 1),
            (1157, 1265, 1),
            (3156, 3246, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 200,
    label = "Cd-halhalCd_54",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (141, 223, 1),
            (164, 316, 1),
            (539, 615, 1),
            (578, 694, 1),
            (1133, 1287, 1),
            (1372, 1454, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 201,
    label = "Cd-F1sF1sCd_54",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (141, 223, 1),
            (164, 316, 1),
            (539, 615, 1),
            (578, 694, 1),
            (1133, 1287, 1),
            (1372, 1454, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 202,
    label = "Cd-F1sF1sCd_78",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cd  u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (519, 605, 1),
            (544, 656, 1),
            (552, 694, 1),
            (978, 1162, 1),
            (1211, 1319, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 203,
    label = "Cd-Br1sBr1sCd_254",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (135, 173, 1),
            (158, 230, 1),
            (161, 293, 1),
            (290, 396, 1),
            (530, 638, 1),
            (782, 882, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 204,
    label = "Cd-Br1sBr1sCd_220",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (157, 173, 1),
            (248, 308, 1),
            (317, 463, 1),
            (419, 537, 1),
            (610, 722, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 205,
    label = "Cd-Cl1sCl1sCd_399",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (123, 183, 1),
            (146, 312, 1),
            (236, 324, 1),
            (397, 525, 1),
            (593, 693, 1),
            (1004, 1190, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 206,
    label = "Cd-Cl1sCl1sCd_423",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (226, 318, 1),
            (419, 633, 1),
            (432, 510, 1),
            (519, 663, 1),
            (738, 890, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 207,
    label = "Cd-Cl1sF1sCd_527",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (118, 208, 1),
            (220, 382, 1),
            (427, 569, 1),
            (512, 664, 1),
            (687, 865, 1),
            (1146, 1248, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 208,
    label = "Cd-Cl1sF1sCd_529",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (93, 239, 1),
            (434, 496, 1),
            (486, 582, 1),
            (561, 685, 1),
            (1090, 1252, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 209,
    label = "Cd-Br1sCl1sCd_539",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (112, 166, 1),
            (199, 263, 1),
            (202, 356, 1),
            (311, 513, 1),
            (753, 941, 1),
            (1094, 1254, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 210,
    label = "Cd-Br1sCl1sCd_549",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (59, 223, 1),
            (193, 253, 1),
            (393, 469, 1),
            (444, 600, 1),
            (529, 727, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 211,
    label = "Cd-Br1sF1sCd_550",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (106, 188, 1),
            (236, 368, 1),
            (316, 500, 1),
            (511, 663, 1),
            (511, 757, 1),
            (1130, 1238, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 212,
    label = "Cd-Br1sF1sCd_558",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (71, 225, 1),
            (279, 415, 1),
            (476, 544, 1),
            (516, 614, 1),
            (1075, 1247, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 213,
    label = "CO-halO2dH_82",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   O2d  ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (674, 674, 1),
            (1050, 1050, 1),
            (1121, 1121, 1),
            (1395, 1395, 1),
            (1906, 1906, 1),
            (3070, 3070, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 214,
    label = "CO-F1sO2dH_82",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   O2d ux {1,D}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (674, 674, 1),
            (1050, 1050, 1),
            (1121, 1121, 1),
            (1395, 1395, 1),
            (1906, 1906, 1),
            (3070, 3070, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 215,
    label = "CO-Cl1sO2dH_526",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   O2d  ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (445, 445, 1),
            (720, 720, 1),
            (950, 950, 1),
            (1328, 1328, 1),
            (1875, 1875, 1),
            (3061, 3061, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 216,
    label = "Cd-halhalCdd_130",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (52, 136, 1),
            (94, 146, 1),
            (315, 393, 1),
            (583, 699, 1),
            (757, 893, 1),
            (1232, 1356, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 217,
    label = "Cd-F1sF1sCdd_130",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cdd ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (52, 136, 1),
            (94, 146, 1),
            (315, 393, 1),
            (583, 699, 1),
            (757, 893, 1),
            (1232, 1356, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 218,
    label = "Cd-Br1sBr1sCdd_243",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (82, 124, 1),
            (118, 190, 1),
            (197, 311, 1),
            (317, 389, 1),
            (351, 463, 1),
            (697, 807, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 219,
    label = "Cd-Cl1sCl1sCdd_376",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (74, 126, 1),
            (211, 313, 1),
            (307, 427, 1),
            (400, 572, 1),
            (407, 501, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 220,
    label = "Cd-Br1sCl1sCdd_537",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (32, 244, 1),
            (62, 120, 1),
            (157, 283, 1),
            (340, 470, 1),
            (361, 431, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 221,
    label = "Cd-Br1sF1sCdd_571",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (50, 104, 1),
            (70, 244, 1),
            (196, 398, 1),
            (273, 391, 1),
            (328, 454, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 222,
    label = "Cd-Cl1sF1sCdd_614",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (41, 211, 1),
            (67, 123, 1),
            (340, 450, 1),
            (381, 557, 1),
            (647, 791, 1),
            (1047, 1159, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 223,
    label = "Cd-halCddH_136",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   Cdd  ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (79, 147, 1),
            (178, 316, 1),
            (330, 434, 1),
            (1147, 1267, 1),
            (3490, 3490, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 224,
    label = "Cd-F1sCddH_136",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   Cdd ux {1,D}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (79, 147, 1),
            (178, 316, 1),
            (330, 434, 1),
            (1147, 1267, 1),
            (3490, 3490, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 225,
    label = "Cd-Br1sCddH_276",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   Cdd  ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (63, 113, 1),
            (172, 298, 1),
            (287, 397, 1),
            (366, 490, 1),
            (3488, 3488, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 226,
    label = "Cd-Cl1sCddH_458",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   Cdd  ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (66, 128, 1),
            (110, 244, 1),
            (253, 409, 1),
            (286, 454, 1),
            (3488, 3488, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 227,
    label = "CO-halhalO2d_188",
    group = 
"""
1 * CO   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (584, 584, 1),
            (619, 619, 1),
            (793, 793, 1),
            (989, 989, 1),
            (1281, 1281, 1),
            (1989, 1989, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 228,
    label = "CO-F1sF1sO2d_188",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2d ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (584, 584, 1),
            (619, 619, 1),
            (793, 793, 1),
            (989, 989, 1),
            (1281, 1281, 1),
            (1989, 1989, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 229,
    label = "CO-Br1sBr1sO2d_302",
    group = 
"""
1 * CO   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (175, 175, 1),
            (343, 343, 1),
            (418, 418, 1),
            (518, 518, 1),
            (727, 727, 1),
            (1906, 1906, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 230,
    label = "CO-Cl1sCl1sO2d_516",
    group = 
"""
1 * CO   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (297, 297, 1),
            (435, 435, 1),
            (562, 562, 1),
            (587, 587, 1),
            (818, 818, 1),
            (1900, 1900, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 231,
    label = "CO-Br1sF1sO2d_669",
    group = 
"""
1 * CO   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (340, 340, 1),
            (381, 381, 1),
            (631, 631, 1),
            (725, 725, 1),
            (1115, 1115, 1),
            (1941, 1941, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 232,
    label = "CO-Br1sCl1sO2d_679",
    group = 
"""
1 * CO   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (235, 235, 1),
            (367, 367, 1),
            (510, 510, 1),
            (552, 552, 1),
            (776, 776, 1),
            (1902, 1902, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 233,
    label = "CO-Cl1sF1sO2d_726",
    group = 
"""
1 * CO   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (405, 405, 1),
            (488, 488, 1),
            (676, 676, 1),
            (758, 758, 1),
            (1132, 1132, 1),
            (1942, 1942, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 234,
    label = "Cd-halC2dH_457",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   C2d  ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (98, 98, 1),
            (689, 689, 1),
            (742, 742, 1),
            (1025, 1025, 1),
            (1654, 1654, 1),
            (3206, 3206, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 235,
    label = "Cd-Cl1sC2dH_457",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   C2d  ux {1,D}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (98, 98, 1),
            (689, 689, 1),
            (742, 742, 1),
            (1025, 1025, 1),
            (1654, 1654, 1),
            (3206, 3206, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 236,
    label = "CtCH",
    group = 
"""
1 * C        u0 {2,T} {3,S}
2   C        ux {1,T}
3   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (750, 770, 2),
            (3350, 3450, 1),
            (2000, 2200, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """Alkyne end group""",
    longDesc = 
"""
(750, 770, 2),		#R-C-H bend
(3350, 3450, 1),	#C-H stretch
(2000, 2200, 1),
""",
)

entry(
    index = 237,
    label = "Ct-halCt_39",
    group = 
"""
1 * Ct   u0 {2,S} {3,T}
2   Val7 u0 {1,S}
3   Ct   ux {1,T}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (174, 304, 1),
            (355, 447, 1),
            (1306, 1428, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 238,
    label = "Ct-F1sCt_39",
    group = 
"""
1 * Ct  u0 {2,S} {3,T}
2   F1s u0 {1,S}
3   Ct  ux {1,T}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (174, 304, 1),
            (355, 447, 1),
            (1306, 1428, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 239,
    label = "Ct-Br1sCt_259",
    group = 
"""
1 * Ct   u0 {2,S} {3,T}
2   Br1s u0 {1,S}
3   Ct   ux {1,T}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (136, 216, 1),
            (262, 340, 1),
            (357, 457, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 240,
    label = "Ct-Cl1sCt_380",
    group = 
"""
1 * Ct   u0 {2,S} {3,T}
2   Cl1s u0 {1,S}
3   Ct   ux {1,T}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (153, 251, 1),
            (304, 376, 1),
            (583, 707, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 241,
    label = "RsCH2sR",
    group = 
"""
1 * C        u0 {2,S} {3,S} {4,S} {5,S}
2   R!H!Val7 ux {1,S}
3   R!H!Val7 ux {1,S}
4   [H,Val7] u0 {1,S}
5   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2750, 2850, 2),
            (1425, 1450, 1),
            (1225, 1275, 1),
            (1270, 1340, 1),
            (700, 800, 1),
            (300, 400, 1),
        ],
        symmetry = 4,
    ),
    shortDesc = """separated carbon with two single bonds""",
    longDesc = 
"""
(2750, 2850, 2),	#C-H stretch
(1425, 1450, 1),	#H-C-H scissor
(1225, 1275, 1),	#R-C-H symmetric
(1270, 1340, 1),	#R-C-H asymmetric
(700, 800, 1),		#H-C-H side rock
(300, 400, 1),		#R-C-R scissor
""",
)

entry(
    index = 242,
    label = "Cs-halhalCsCs_40",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (186, 258, 1),
            (302, 356, 1),
            (410, 480, 1),
            (483, 561, 1),
            (545, 633, 1),
            (1193, 1235, 1),
            (1433, 1517, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 243,
    label = "Cs-F1sF1sCsCs_40",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
5   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (186, 258, 1),
            (302, 356, 1),
            (410, 480, 1),
            (483, 561, 1),
            (545, 633, 1),
            (1193, 1235, 1),
            (1433, 1517, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 244,
    label = "Cs-F1sF1sCsCs_41",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
5   Cs  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (181, 249, 1),
            (286, 344, 1),
            (486, 552, 1),
            (511, 665, 1),
            (553, 637, 1),
            (1169, 1241, 1),
            (1190, 1306, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 245,
    label = "Cs-Br1sBr1sCsCs_217",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (145, 165, 1),
            (190, 268, 1),
            (265, 285, 1),
            (278, 314, 1),
            (381, 495, 1),
            (507, 587, 1),
            (1150, 1200, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 246,
    label = "Cs-Br1sBr1sCsCs_271",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (130, 144, 1),
            (130, 238, 1),
            (230, 262, 1),
            (230, 352, 1),
            (249, 301, 1),
            (470, 542, 1),
            (1132, 1238, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 247,
    label = "Cs-Br1sBr1sCsCs_353",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
5   Cs   u2 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (273, 373, 1),
            (327, 427, 1),
            (383, 483, 1),
            (1224, 1324, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 248,
    label = "Cs-Cl1sCl1sCsCs_378",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (156, 228, 1),
            (231, 279, 1),
            (289, 329, 1),
            (312, 396, 1),
            (379, 515, 1),
            (602, 710, 1),
            (994, 1178, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 249,
    label = "Cs-Cl1sCl1sCsCs_364",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (176, 232, 1),
            (225, 245, 1),
            (274, 296, 1),
            (294, 346, 1),
            (484, 552, 1),
            (563, 647, 1),
            (1128, 1212, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 250,
    label = "Cs-Br1sCl1sCsCs_543",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (100, 214, 1),
            (187, 227, 1),
            (266, 298, 1),
            (275, 331, 1),
            (324, 444, 1),
            (459, 613, 1),
            (1082, 1206, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 251,
    label = "Cs-Br1sCl1sCsCs_532",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (157, 199, 1),
            (230, 276, 1),
            (233, 321, 1),
            (310, 426, 1),
            (408, 588, 1),
            (606, 688, 1),
            (1378, 1570, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 252,
    label = "Cs-Br1sF1sCsCs_565",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (141, 251, 1),
            (261, 335, 1),
            (267, 301, 1),
            (381, 501, 1),
            (472, 700, 1),
            (476, 626, 1),
            (1466, 1500, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 253,
    label = "Cs-Br1sF1sCsCs_648",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (219, 269, 1),
            (454, 618, 1),
            (584, 712, 1),
            (859, 1025, 1),
            (1173, 1273, 1),
            (1373, 1551, 1),
            (1424, 1524, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 254,
    label = "Cs-Cl1sF1sCsCs_613",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (278, 322, 1),
            (346, 408, 1),
            (379, 577, 1),
            (382, 468, 1),
            (515, 681, 1),
            (1154, 1248, 1),
            (1473, 1495, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 255,
    label = "Cs-Cl1sF1sCsCs_609",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (137, 277, 1),
            (269, 299, 1),
            (276, 362, 1),
            (366, 494, 1),
            (506, 612, 1),
            (595, 679, 1),
            (1177, 1263, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 256,
    label = "Cs-halhalO2sCs_47",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   O2s  ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (183, 263, 1),
            (327, 399, 1),
            (503, 589, 1),
            (506, 644, 1),
            (608, 780, 1),
            (1145, 1213, 1),
            (1339, 1481, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 257,
    label = "Cs-F1sF1sO2sCs_47",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (183, 263, 1),
            (327, 399, 1),
            (503, 589, 1),
            (506, 644, 1),
            (608, 780, 1),
            (1145, 1213, 1),
            (1339, 1481, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 258,
    label = "Cs-F1sF1sO2sCs_121",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   Cs  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (202, 304, 1),
            (469, 581, 1),
            (520, 674, 1),
            (579, 755, 1),
            (732, 952, 1),
            (1136, 1220, 1),
            (1240, 1408, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 259,
    label = "Cs-F1sF1sO2sCs_134",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s u1 {1,S}
5   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (261, 441, 1),
            (281, 365, 1),
            (497, 569, 1),
            (525, 693, 1),
            (557, 771, 1),
            (857, 927, 1),
            (1026, 1214, 1),
            (1153, 1249, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 260,
    label = "Cs-Br1sBr1sO2sCs_234",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (138, 232, 1),
            (144, 160, 1),
            (246, 404, 1),
            (264, 314, 1),
            (275, 363, 1),
            (505, 589, 1),
            (1364, 1472, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 261,
    label = "Cs-Br1sBr1sO2sCs_300",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (133, 149, 1),
            (184, 268, 1),
            (227, 277, 1),
            (261, 371, 1),
            (349, 495, 1),
            (498, 578, 1),
            (1372, 1464, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 262,
    label = "Cs-Br1sBr1sO2sCs_309",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  u1 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (281, 309, 1),
            (375, 395, 1),
            (416, 480, 1),
            (923, 1023, 1),
            (958, 1050, 1),
            (1166, 1266, 1),
            (1484, 1584, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 263,
    label = "Cs-Cl1sCl1sO2sCs_379",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (195, 245, 1),
            (279, 321, 1),
            (338, 418, 1),
            (378, 496, 1),
            (437, 601, 1),
            (626, 740, 1),
            (1319, 1469, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 264,
    label = "Cs-Cl1sCl1sO2sCs_414",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  u1 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (178, 234, 1),
            (257, 317, 1),
            (338, 404, 1),
            (403, 541, 1),
            (428, 616, 1),
            (600, 762, 1),
            (646, 832, 1),
            (1086, 1252, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 265,
    label = "Cs-Cl1sCl1sO2sCs_415",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (201, 259, 1),
            (269, 337, 1),
            (321, 427, 1),
            (459, 547, 1),
            (551, 693, 1),
            (591, 785, 1),
            (1380, 1474, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 266,
    label = "Cs-Br1sCl1sO2sCs_552",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (172, 214, 1),
            (252, 304, 1),
            (275, 371, 1),
            (333, 463, 1),
            (476, 594, 1),
            (585, 733, 1),
            (1339, 1521, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 267,
    label = "Cs-Br1sCl1sO2sCs_625",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (232, 278, 1),
            (372, 462, 1),
            (533, 665, 1),
            (693, 839, 1),
            (1259, 1435, 1),
            (1427, 1527, 1),
            (1434, 1476, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 268,
    label = "Cs-Br1sCl1sO2sCs_725",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  u1 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (262, 362, 1),
            (351, 451, 1),
            (503, 603, 1),
            (1452, 1552, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 269,
    label = "Cs-Br1sF1sO2sCs_584",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (137, 217, 1),
            (274, 312, 1),
            (279, 365, 1),
            (376, 522, 1),
            (567, 705, 1),
            (597, 775, 1),
            (1164, 1376, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 270,
    label = "Cs-Br1sF1sO2sCs_619",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (181, 275, 1),
            (216, 348, 1),
            (372, 578, 1),
            (464, 604, 1),
            (588, 666, 1),
            (1198, 1330, 1),
            (1446, 1496, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 271,
    label = "Cs-Cl1sF1sO2sCs_592",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (261, 335, 1),
            (326, 408, 1),
            (371, 475, 1),
            (488, 636, 1),
            (544, 734, 1),
            (1089, 1233, 1),
            (1335, 1499, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 272,
    label = "Cs-Cl1sF1sO2sCs_595",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (120, 252, 1),
            (229, 315, 1),
            (322, 404, 1),
            (499, 571, 1),
            (556, 748, 1),
            (579, 671, 1),
            (1205, 1411, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 273,
    label = "Cs-Cl1sF1sO2sCs_690",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  u1 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (169, 213, 1),
            (219, 303, 1),
            (291, 337, 1),
            (365, 455, 1),
            (398, 594, 1),
            (510, 628, 1),
            (1171, 1215, 1),
            (1456, 1484, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 274,
    label = "Cs-halhalCsCd_55",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cs   ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (244, 304, 1),
            (327, 363, 1),
            (343, 417, 1),
            (477, 601, 1),
            (627, 783, 1),
            (1125, 1207, 1),
            (1150, 1276, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 275,
    label = "Cs-F1sF1sCsCd_55",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
5   Cd  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (244, 304, 1),
            (327, 363, 1),
            (343, 417, 1),
            (477, 601, 1),
            (627, 783, 1),
            (1125, 1207, 1),
            (1150, 1276, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 276,
    label = "Cs-F1sF1sCsCd_120",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
5   Cd  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (106, 166, 1),
            (285, 329, 1),
            (412, 480, 1),
            (417, 605, 1),
            (567, 797, 1),
            (680, 834, 1),
            (1102, 1258, 1),
            (1148, 1222, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 277,
    label = "Cs-F1sF1sCdCs_53",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cd  ux {1,S}
5   Cs  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (207, 289, 1),
            (297, 369, 1),
            (408, 524, 1),
            (563, 645, 1),
            (605, 763, 1),
            (737, 855, 1),
            (975, 1147, 1),
            (1148, 1250, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 278,
    label = "Cs-Br1sBr1sCsCd_286",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (137, 157, 1),
            (140, 252, 1),
            (245, 357, 1),
            (257, 283, 1),
            (277, 317, 1),
            (380, 552, 1),
            (548, 646, 1),
            (754, 922, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 279,
    label = "Cs-Br1sBr1sCsCd_293",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (132, 154, 1),
            (153, 233, 1),
            (244, 384, 1),
            (248, 268, 1),
            (267, 291, 1),
            (359, 539, 1),
            (461, 599, 1),
            (529, 663, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 280,
    label = "Cs-Br1sBr1sCdCs_581",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cd   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (222, 360, 1),
            (302, 436, 1),
            (586, 710, 1),
            (709, 861, 1),
            (725, 769, 1),
            (892, 944, 1),
            (1087, 1175, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 281,
    label = "Cs-Cl1sCl1sCsCd_370",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (157, 273, 1),
            (225, 245, 1),
            (271, 295, 1),
            (299, 335, 1),
            (350, 374, 1),
            (557, 625, 1),
            (798, 886, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 282,
    label = "Cs-Cl1sCl1sCsCd_385",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (136, 178, 1),
            (221, 263, 1),
            (260, 380, 1),
            (278, 304, 1),
            (410, 504, 1),
            (454, 594, 1),
            (607, 741, 1),
            (662, 800, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 283,
    label = "Cs-Cl1sCl1sCdCs_493",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (198, 260, 1),
            (222, 426, 1),
            (244, 316, 1),
            (307, 367, 1),
            (428, 638, 1),
            (556, 722, 1),
            (719, 895, 1),
            (803, 951, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 284,
    label = "Cs-Cl1sF1sCsCd_582",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (242, 280, 1),
            (261, 317, 1),
            (330, 398, 1),
            (364, 576, 1),
            (559, 735, 1),
            (831, 891, 1),
            (1076, 1220, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 285,
    label = "Cs-Cl1sF1sCdCs_634",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (241, 243, 1),
            (247, 401, 1),
            (248, 264, 1),
            (264, 298, 1),
            (553, 605, 1),
            (566, 696, 1),
            (701, 761, 1),
            (1224, 1226, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 286,
    label = "Cs-Cl1sF1sCsCd_560",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (156, 176, 1),
            (290, 312, 1),
            (306, 384, 1),
            (343, 543, 1),
            (396, 466, 1),
            (513, 623, 1),
            (601, 689, 1),
            (1133, 1187, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 287,
    label = "Cs-Br1sF1sCsCd_604",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (71, 219, 1),
            (211, 261, 1),
            (233, 355, 1),
            (263, 301, 1),
            (349, 499, 1),
            (780, 912, 1),
            (1096, 1198, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 288,
    label = "Cs-Br1sF1sCsCd_703",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (105, 137, 1),
            (180, 256, 1),
            (237, 295, 1),
            (245, 421, 1),
            (398, 538, 1),
            (421, 617, 1),
            (642, 828, 1),
            (1103, 1231, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 289,
    label = "Cs-Br1sF1sCdCs_734",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (234, 302, 1),
            (239, 391, 1),
            (616, 722, 1),
            (742, 842, 1),
            (1016, 1116, 1),
            (1215, 1315, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 290,
    label = "Cs-Br1sCl1sCsCd_617",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (187, 215, 1),
            (219, 385, 1),
            (231, 273, 1),
            (265, 321, 1),
            (389, 565, 1),
            (540, 690, 1),
            (757, 897, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 291,
    label = "Cs-Br1sCl1sCsCd_635",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (94, 140, 1),
            (165, 179, 1),
            (219, 267, 1),
            (283, 337, 1),
            (327, 491, 1),
            (386, 556, 1),
            (475, 681, 1),
            (619, 619, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 292,
    label = "Cs-Br1sCl1sCdCs_686",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (306, 316, 1),
            (569, 669, 1),
            (689, 789, 1),
            (709, 809, 1),
            (868, 968, 1),
            (1074, 1174, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 293,
    label = "Cs-halCsCOH_61",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (172, 240, 1),
            (337, 389, 1),
            (423, 613, 1),
            (1123, 1227, 1),
            (1284, 1350, 1),
            (1437, 1525, 1),
            (3006, 3112, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 294,
    label = "Cs-F1sCsCOH_61",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   CO  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (172, 240, 1),
            (337, 389, 1),
            (423, 613, 1),
            (1123, 1227, 1),
            (1284, 1350, 1),
            (1437, 1525, 1),
            (3006, 3112, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 295,
    label = "Cs-F1sCsCOH_89",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  u1 {1,S}
4   CO  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (95, 265, 1),
            (209, 257, 1),
            (1058, 1160, 1),
            (1187, 1321, 1),
            (1284, 1366, 1),
            (1328, 1350, 1),
            (3285, 3295, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 296,
    label = "Cs-F1sCsCOH_49",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   CO  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (245, 265, 1),
            (296, 434, 1),
            (495, 657, 1),
            (1126, 1200, 1),
            (1246, 1288, 1),
            (1364, 1532, 1),
            (3007, 3113, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 297,
    label = "Cs-Br1sCsCOH_267",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (123, 281, 1),
            (221, 265, 1),
            (237, 339, 1),
            (1101, 1179, 1),
            (1138, 1238, 1),
            (1324, 1444, 1),
            (3117, 3151, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 298,
    label = "Cs-Br1sCsCOH_313",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   u1 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (127, 151, 1),
            (181, 271, 1),
            (849, 971, 1),
            (1000, 1132, 1),
            (1159, 1269, 1),
            (1346, 1456, 1),
            (3115, 3235, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 299,
    label = "Cs-Br1sCsCOH_316",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   CO   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (129, 139, 1),
            (221, 293, 1),
            (480, 548, 1),
            (575, 647, 1),
            (1170, 1220, 1),
            (1275, 1439, 1),
            (3090, 3152, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 300,
    label = "Cs-Cl1sCsCOH_425",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (81, 251, 1),
            (213, 277, 1),
            (262, 386, 1),
            (1094, 1194, 1),
            (1222, 1282, 1),
            (1446, 1514, 1),
            (3101, 3159, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 301,
    label = "Cs-Cl1sCsCOH_467",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   CO   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (172, 200, 1),
            (298, 342, 1),
            (519, 621, 1),
            (624, 734, 1),
            (1208, 1254, 1),
            (1365, 1469, 1),
            (3077, 3123, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 302,
    label = "Cs-Cl1sCsCOH_486",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   u1 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (121, 213, 1),
            (207, 305, 1),
            (599, 693, 1),
            (1132, 1232, 1),
            (1209, 1361, 1),
            (1241, 1381, 1),
            (3128, 3262, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 303,
    label = "Cs-halO2sCsH_65",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (205, 317, 1),
            (423, 563, 1),
            (514, 686, 1),
            (1105, 1199, 1),
            (1293, 1437, 1),
            (1381, 1463, 1),
            (3031, 3163, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 304,
    label = "Cs-F1sO2sCsH_65",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cs  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (205, 317, 1),
            (423, 563, 1),
            (514, 686, 1),
            (1105, 1199, 1),
            (1293, 1437, 1),
            (1381, 1463, 1),
            (3031, 3163, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 305,
    label = "Cs-F1sO2sCsH_106",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s u1 {1,S}
4   Cs  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (348, 434, 1),
            (466, 658, 1),
            (603, 811, 1),
            (805, 939, 1),
            (1066, 1152, 1),
            (1168, 1252, 1),
            (1209, 1369, 1),
            (3108, 3166, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 306,
    label = "Cs-F1sO2sCsH_131",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cs  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (401, 573, 1),
            (564, 712, 1),
            (601, 775, 1),
            (1078, 1160, 1),
            (1259, 1391, 1),
            (1337, 1437, 1),
            (3048, 3250, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 307,
    label = "Cs-Br1sO2sCsH_231",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (238, 366, 1),
            (249, 311, 1),
            (349, 475, 1),
            (500, 588, 1),
            (1177, 1239, 1),
            (1384, 1478, 1),
            (3103, 3179, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 308,
    label = "Cs-Br1sO2sCsH_233",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  u1 {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (236, 294, 1),
            (239, 357, 1),
            (288, 436, 1),
            (472, 590, 1),
            (873, 953, 1),
            (1084, 1208, 1),
            (1132, 1204, 1),
            (3091, 3181, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 309,
    label = "Cs-Br1sO2sCsH_266",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (300, 386, 1),
            (552, 656, 1),
            (853, 1007, 1),
            (1119, 1285, 1),
            (1139, 1217, 1),
            (1384, 1480, 1),
            (3123, 3181, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 310,
    label = "Cs-Cl1sO2sCsH_428",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (176, 290, 1),
            (344, 430, 1),
            (433, 589, 1),
            (1118, 1238, 1),
            (1245, 1397, 1),
            (1346, 1470, 1),
            (3078, 3170, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 311,
    label = "Cs-Cl1sO2sCsH_429",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  u1 {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (133, 311, 1),
            (270, 368, 1),
            (361, 505, 1),
            (570, 700, 1),
            (1027, 1181, 1),
            (1089, 1215, 1),
            (1119, 1163, 1),
            (2914, 3142, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 312,
    label = "Cs-Cl1sO2sCsH_398",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (233, 321, 1),
            (252, 410, 1),
            (469, 583, 1),
            (632, 794, 1),
            (1171, 1263, 1),
            (1371, 1483, 1),
            (3097, 3223, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 313,
    label = "Cs-halhalO2sO2s_79",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   O2s  ux {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (408, 462, 1),
            (496, 634, 1),
            (573, 665, 1),
            (597, 727, 1),
            (750, 958, 1),
            (1142, 1214, 1),
            (1310, 1482, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 314,
    label = "Cs-F1sF1sO2sO2s_79",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   O2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (408, 462, 1),
            (496, 634, 1),
            (573, 665, 1),
            (597, 727, 1),
            (750, 958, 1),
            (1142, 1214, 1),
            (1310, 1482, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 315,
    label = "Cs-F1sF1sO2sO2s_93",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   O2s u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (355, 395, 1),
            (418, 554, 1),
            (554, 618, 1),
            (578, 668, 1),
            (608, 812, 1),
            (885, 991, 1),
            (1093, 1229, 1),
            (1216, 1372, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 316,
    label = "Cs-Br1sBr1sO2sO2s_241",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (145, 161, 1),
            (267, 403, 1),
            (287, 327, 1),
            (291, 347, 1),
            (344, 544, 1),
            (591, 651, 1),
            (633, 711, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 317,
    label = "Cs-Cl1sCl1sO2sO2s_430",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (219, 275, 1),
            (245, 453, 1),
            (325, 363, 1),
            (370, 422, 1),
            (414, 468, 1),
            (619, 683, 1),
            (687, 777, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 318,
    label = "Cs-Br1sF1sO2sO2s_594",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (246, 396, 1),
            (285, 301, 1),
            (286, 338, 1),
            (462, 562, 1),
            (561, 657, 1),
            (642, 794, 1),
            (1290, 1484, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 319,
    label = "Cs-Br1sCl1sO2sO2s_616",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (186, 216, 1),
            (298, 368, 1),
            (306, 336, 1),
            (387, 443, 1),
            (502, 706, 1),
            (587, 723, 1),
            (710, 876, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 320,
    label = "Cs-Cl1sF1sO2sO2s_629",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (338, 352, 1),
            (353, 397, 1),
            (382, 474, 1),
            (431, 587, 1),
            (584, 712, 1),
            (641, 815, 1),
            (1346, 1482, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 321,
    label = "Cs-halCsCsH_88",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (194, 306, 1),
            (365, 469, 1),
            (408, 614, 1),
            (1107, 1203, 1),
            (1236, 1394, 1),
            (1392, 1520, 1),
            (3058, 3180, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 322,
    label = "Cs-F1sCsCsH_88",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cs  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (194, 306, 1),
            (365, 469, 1),
            (408, 614, 1),
            (1107, 1203, 1),
            (1236, 1394, 1),
            (1392, 1520, 1),
            (3058, 3180, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 323,
    label = "Cs-F1sCsCsH_74",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cs  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (207, 311, 1),
            (436, 622, 1),
            (447, 691, 1),
            (1074, 1182, 1),
            (1276, 1366, 1),
            (1311, 1469, 1),
            (3045, 3235, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 324,
    label = "Cs-Br1sCsCsH_218",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (177, 235, 1),
            (251, 311, 1),
            (433, 521, 1),
            (1096, 1184, 1),
            (1156, 1206, 1),
            (1442, 1516, 1),
            (3112, 3166, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 325,
    label = "Cs-Br1sCsCsH_268",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (120, 172, 1),
            (161, 367, 1),
            (179, 301, 1),
            (1106, 1256, 1),
            (1113, 1199, 1),
            (1434, 1526, 1),
            (3119, 3193, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 326,
    label = "Cs-Cl1sCsCsH_369",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (177, 277, 1),
            (261, 319, 1),
            (400, 522, 1),
            (1116, 1216, 1),
            (1155, 1299, 1),
            (1408, 1540, 1),
            (3097, 3167, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 327,
    label = "Cs-Cl1sCsCsH_397",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (114, 226, 1),
            (231, 327, 1),
            (473, 603, 1),
            (1120, 1228, 1),
            (1125, 1297, 1),
            (1378, 1484, 1),
            (3095, 3217, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 328,
    label = "Cs-halO2sCOH_104",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (153, 311, 1),
            (313, 407, 1),
            (860, 1004, 1),
            (1068, 1186, 1),
            (1275, 1423, 1),
            (1357, 1373, 1),
            (3018, 3072, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 329,
    label = "Cs-F1sO2sCOH_104",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   CO  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (153, 311, 1),
            (313, 407, 1),
            (860, 1004, 1),
            (1068, 1186, 1),
            (1275, 1423, 1),
            (1357, 1373, 1),
            (3018, 3072, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 330,
    label = "Cs-F1sO2sCOH_149",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   CO  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (308, 402, 1),
            (315, 505, 1),
            (557, 643, 1),
            (1127, 1235, 1),
            (1327, 1355, 1),
            (1420, 1420, 1),
            (3041, 3071, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 331,
    label = "Cs-F1sO2sCOH_173",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s u1 {1,S}
4   CO  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (222, 260, 1),
            (248, 396, 1),
            (579, 599, 1),
            (718, 912, 1),
            (1064, 1128, 1),
            (1172, 1268, 1),
            (1285, 1319, 1),
            (2841, 2943, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 332,
    label = "Cs-Br1sO2sCOH_325",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (168, 318, 1),
            (280, 340, 1),
            (306, 478, 1),
            (740, 850, 1),
            (1163, 1249, 1),
            (1369, 1503, 1),
            (3125, 3167, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 333,
    label = "Cs-Br1sO2sCOH_339",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  u1 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (406, 506, 1),
            (442, 542, 1),
            (1137, 1237, 1),
            (2984, 3084, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 334,
    label = "Cs-Br1sO2sCOH_246",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   CO   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (269, 269, 1),
            (280, 280, 1),
            (300, 300, 1),
            (705, 705, 1),
            (1175, 1175, 1),
            (1427, 1427, 1),
            (3176, 3176, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 335,
    label = "Cs-Cl1sO2sCOH_511",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (220, 430, 1),
            (294, 358, 1),
            (587, 649, 1),
            (1168, 1248, 1),
            (1289, 1361, 1),
            (1458, 1466, 1),
            (3099, 3151, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 336,
    label = "Cs-Cl1sO2sCOH_520",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   CO   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (234, 456, 1),
            (238, 340, 1),
            (281, 495, 1),
            (632, 682, 1),
            (1155, 1239, 1),
            (1413, 1413, 1),
            (3096, 3130, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 337,
    label = "Cs-Cl1sO2sCOH_460",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  u1 {1,S}
4   CO   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (179, 247, 1),
            (298, 434, 1),
            (364, 364, 1),
            (548, 594, 1),
            (717, 929, 1),
            (1138, 1288, 1),
            (1170, 1226, 1),
            (2985, 3049, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 338,
    label = "Cs-halhalO2sCd_107",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   O2s  ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (236, 314, 1),
            (238, 404, 1),
            (481, 585, 1),
            (517, 653, 1),
            (690, 802, 1),
            (781, 919, 1),
            (1028, 1178, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 339,
    label = "Cs-F1sF1sO2sCd_107",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   Cd  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (236, 314, 1),
            (238, 404, 1),
            (481, 585, 1),
            (517, 653, 1),
            (690, 802, 1),
            (781, 919, 1),
            (1028, 1178, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 340,
    label = "Cs-F1sF1sO2sCd_125",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s u1 {1,S}
5   Cd  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (429, 623, 1),
            (474, 636, 1),
            (607, 789, 1),
            (827, 987, 1),
            (1119, 1281, 1),
            (1128, 1162, 1),
            (1177, 1277, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 341,
    label = "Cs-F1sF1sO2sCd_126",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   Cd  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (110, 170, 1),
            (395, 453, 1),
            (428, 570, 1),
            (558, 684, 1),
            (588, 746, 1),
            (730, 956, 1),
            (801, 951, 1),
            (1006, 1158, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 342,
    label = "Cs-Br1sBr1sO2sCd_227",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (138, 154, 1),
            (247, 347, 1),
            (263, 319, 1),
            (272, 378, 1),
            (284, 430, 1),
            (566, 668, 1),
            (659, 745, 1),
            (710, 834, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 343,
    label = "Cs-Br1sBr1sO2sCd_344",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (98, 164, 1),
            (135, 151, 1),
            (225, 277, 1),
            (272, 306, 1),
            (279, 375, 1),
            (422, 518, 1),
            (514, 612, 1),
            (606, 672, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 344,
    label = "Cs-Br1sBr1sO2sCd_698",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  u1 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (83, 183, 1),
            (244, 344, 1),
            (627, 727, 1),
            (1159, 1259, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 345,
    label = "Cs-Cl1sCl1sO2sCd_427",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (200, 272, 1),
            (275, 353, 1),
            (313, 441, 1),
            (347, 463, 1),
            (435, 615, 1),
            (682, 762, 1),
            (782, 864, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 346,
    label = "Cs-Cl1sCl1sO2sCd_431",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (169, 191, 1),
            (220, 266, 1),
            (273, 339, 1),
            (367, 435, 1),
            (388, 498, 1),
            (460, 636, 1),
            (601, 731, 1),
            (680, 730, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 347,
    label = "Cs-Cl1sCl1sO2sCd_485",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  u1 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (329, 355, 1),
            (358, 372, 1),
            (541, 675, 1),
            (747, 871, 1),
            (825, 995, 1),
            (1215, 1249, 1),
            (1279, 1379, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 348,
    label = "Cs-Br1sF1sO2sCd_528",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (64, 212, 1),
            (237, 287, 1),
            (248, 402, 1),
            (275, 315, 1),
            (513, 615, 1),
            (707, 791, 1),
            (850, 922, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 349,
    label = "Cs-Br1sF1sO2sCd_673",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (126, 158, 1),
            (213, 263, 1),
            (219, 403, 1),
            (279, 303, 1),
            (485, 559, 1),
            (573, 631, 1),
            (626, 732, 1),
            (787, 861, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 350,
    label = "Cs-Br1sF1sO2sCd_705",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  u1 {1,S}
5   Cd   ux {1,S}
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 351,
    label = "Cs-Br1sCl1sO2sCd_600",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (171, 201, 1),
            (218, 286, 1),
            (286, 366, 1),
            (288, 430, 1),
            (361, 489, 1),
            (598, 746, 1),
            (704, 798, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 352,
    label = "Cs-Br1sCl1sO2sCd_637",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (120, 158, 1),
            (152, 210, 1),
            (244, 276, 1),
            (259, 335, 1),
            (404, 458, 1),
            (465, 495, 1),
            (541, 677, 1),
            (627, 679, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 353,
    label = "Cs-Cl1sF1sO2sCd_665",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (225, 293, 1),
            (311, 387, 1),
            (348, 438, 1),
            (437, 573, 1),
            (563, 709, 1),
            (731, 919, 1),
            (785, 889, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 354,
    label = "Cs-Cl1sF1sO2sCd_682",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (143, 195, 1),
            (304, 406, 1),
            (312, 334, 1),
            (352, 446, 1),
            (443, 533, 1),
            (563, 675, 1),
            (564, 736, 1),
            (810, 810, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 355,
    label = "Cs-Cl1sF1sO2sCd_644",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  u1 {1,S}
5   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (335, 435, 1),
            (490, 590, 1),
            (653, 753, 1),
            (1070, 1170, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 356,
    label = "Cs-halCsCdH_108",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (243, 325, 1),
            (243, 413, 1),
            (797, 909, 1),
            (1058, 1234, 1),
            (1082, 1188, 1),
            (1233, 1361, 1),
            (3158, 3320, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 357,
    label = "Cs-F1sCsCdH_108",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cd  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (243, 325, 1),
            (243, 413, 1),
            (797, 909, 1),
            (1058, 1234, 1),
            (1082, 1188, 1),
            (1233, 1361, 1),
            (3158, 3320, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 358,
    label = "Cs-F1sCdCsH_50",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cd  ux {1,S}
4   Cs  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (96, 252, 1),
            (209, 325, 1),
            (527, 655, 1),
            (638, 804, 1),
            (1079, 1135, 1),
            (1231, 1325, 1),
            (1303, 1393, 1),
            (3218, 3328, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 359,
    label = "Cs-F1sCsCdH_77",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cd  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (139, 189, 1),
            (248, 376, 1),
            (519, 603, 1),
            (558, 750, 1),
            (880, 916, 1),
            (1147, 1267, 1),
            (1279, 1319, 1),
            (3102, 3232, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 360,
    label = "Cs-Br1sCsCdH_226",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (109, 265, 1),
            (209, 305, 1),
            (267, 409, 1),
            (819, 915, 1),
            (1127, 1199, 1),
            (1151, 1259, 1),
            (3130, 3246, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 361,
    label = "Cs-Br1sCsCdH_320",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (220, 276, 1),
            (836, 890, 1),
            (1072, 1152, 1),
            (1115, 1211, 1),
            (3082, 3158, 1),
            (3100, 3200, 1),
            (3120, 3176, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 362,
    label = "Cs-Br1sCdCsH_355",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (356, 380, 1),
            (702, 720, 1),
            (819, 887, 1),
            (1071, 1137, 1),
            (1169, 1173, 1),
            (1170, 1224, 1),
            (3250, 3284, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 363,
    label = "Cs-Cl1sCsCdH_410",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (125, 263, 1),
            (263, 317, 1),
            (298, 392, 1),
            (793, 909, 1),
            (1160, 1240, 1),
            (1162, 1322, 1),
            (3151, 3271, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 364,
    label = "Cs-Cl1sCsCdH_472",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (132, 184, 1),
            (219, 313, 1),
            (387, 475, 1),
            (524, 690, 1),
            (579, 735, 1),
            (850, 980, 1),
            (1172, 1232, 1),
            (3098, 3202, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 365,
    label = "Cs-Cl1sCdCsH_474",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,S}
4   Cs   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (83, 253, 1),
            (197, 303, 1),
            (234, 428, 1),
            (597, 761, 1),
            (621, 839, 1),
            (1118, 1252, 1),
            (1177, 1335, 1),
            (3191, 3279, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 366,
    label = "Cs-halO2sO2sH_111",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (448, 570, 1),
            (532, 694, 1),
            (567, 753, 1),
            (1110, 1232, 1),
            (1307, 1413, 1),
            (1380, 1448, 1),
            (3020, 3148, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 367,
    label = "Cs-F1sO2sO2sH_111",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   O2s ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (448, 570, 1),
            (532, 694, 1),
            (567, 753, 1),
            (1110, 1232, 1),
            (1307, 1413, 1),
            (1380, 1448, 1),
            (3020, 3148, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 368,
    label = "Cs-F1sO2sO2sH_139",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   O2s u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (421, 481, 1),
            (502, 604, 1),
            (564, 710, 1),
            (1025, 1113, 1),
            (1111, 1249, 1),
            (1195, 1335, 1),
            (1232, 1370, 1),
            (3006, 3106, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 369,
    label = "Cs-Br1sO2sO2sH_249",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (210, 344, 1),
            (282, 326, 1),
            (480, 616, 1),
            (569, 605, 1),
            (1193, 1249, 1),
            (1373, 1461, 1),
            (3101, 3201, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 370,
    label = "Cs-Br1sO2sO2sH_322",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (807, 907, 1),
            (935, 1035, 1),
            (998, 1098, 1),
            (1130, 1230, 1),
            (2928, 3028, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 371,
    label = "Cs-Cl1sO2sO2sH_389",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (341, 457, 1),
            (356, 402, 1),
            (587, 649, 1),
            (648, 706, 1),
            (1227, 1295, 1),
            (1363, 1449, 1),
            (3093, 3201, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 372,
    label = "Cs-Cl1sO2sO2sH_469",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (367, 403, 1),
            (509, 649, 1),
            (1005, 1219, 1),
            (1212, 1262, 1),
            (1379, 1469, 1),
            (2829, 2867, 1),
            (3048, 3068, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 373,
    label = "Cs-halhalCsCt_124",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cs   ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (102, 206, 1),
            (333, 377, 1),
            (373, 455, 1),
            (565, 717, 1),
            (584, 788, 1),
            (1101, 1199, 1),
            (1136, 1256, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 374,
    label = "Cs-F1sF1sCsCt_124",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
5   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (102, 206, 1),
            (333, 377, 1),
            (373, 455, 1),
            (565, 717, 1),
            (584, 788, 1),
            (1101, 1199, 1),
            (1136, 1256, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 375,
    label = "Cs-F1sF1sCsCt_154",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  u1 {1,S}
5   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (155, 225, 1),
            (321, 397, 1),
            (429, 543, 1),
            (548, 648, 1),
            (622, 740, 1),
            (929, 1099, 1),
            (1091, 1211, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 376,
    label = "Cs-Br1sBr1sCsCt_315",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (136, 160, 1),
            (189, 267, 1),
            (250, 292, 1),
            (283, 351, 1),
            (358, 414, 1),
            (371, 537, 1),
            (583, 655, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 377,
    label = "Cs-Br1sBr1sCsCt_721",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   u1 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (141, 241, 1),
            (265, 365, 1),
            (558, 658, 1),
            (797, 897, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 378,
    label = "Cs-Cl1sCl1sCsCt_403",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (126, 174, 1),
            (249, 275, 1),
            (253, 419, 1),
            (297, 321, 1),
            (384, 538, 1),
            (385, 471, 1),
            (880, 1000, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 379,
    label = "Cs-Cl1sCl1sCsCt_476",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   u1 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (121, 183, 1),
            (238, 274, 1),
            (266, 330, 1),
            (349, 511, 1),
            (372, 424, 1),
            (600, 722, 1),
            (600, 740, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 380,
    label = "Cs-Cl1sF1sCsCt_608",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (143, 187, 1),
            (288, 332, 1),
            (344, 376, 1),
            (374, 526, 1),
            (377, 435, 1),
            (635, 703, 1),
            (1105, 1185, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 381,
    label = "Cs-Cl1sF1sCsCt_655",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   u1 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (159, 211, 1),
            (266, 346, 1),
            (343, 387, 1),
            (392, 404, 1),
            (522, 692, 1),
            (650, 674, 1),
            (1207, 1207, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 382,
    label = "Cs-Br1sF1sCsCt_640",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (147, 199, 1),
            (275, 299, 1),
            (293, 369, 1),
            (333, 479, 1),
            (352, 412, 1),
            (596, 704, 1),
            (1086, 1186, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 383,
    label = "Cs-Br1sF1sCsCt_638",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   u1 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (182, 210, 1),
            (327, 357, 1),
            (550, 574, 1),
            (612, 712, 1),
            (726, 932, 1),
            (757, 851, 1),
            (1220, 1320, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 384,
    label = "Cs-Br1sCl1sCsCt_672",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (112, 162, 1),
            (184, 248, 1),
            (265, 289, 1),
            (295, 461, 1),
            (320, 384, 1),
            (454, 474, 1),
            (617, 671, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 385,
    label = "Cs-Br1sCl1sCsCt_699",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   u1 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (132, 138, 1),
            (265, 299, 1),
            (266, 390, 1),
            (515, 701, 1),
            (623, 723, 1),
            (899, 999, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 386,
    label = "Cs-halCsCtH_128",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (183, 283, 1),
            (340, 416, 1),
            (511, 707, 1),
            (1026, 1110, 1),
            (1224, 1316, 1),
            (1259, 1369, 1),
            (2993, 3081, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 387,
    label = "Cs-F1sCsCtH_128",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Ct  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (183, 283, 1),
            (340, 416, 1),
            (511, 707, 1),
            (1026, 1110, 1),
            (1224, 1316, 1),
            (1259, 1369, 1),
            (2993, 3081, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 388,
    label = "Cs-F1sCsCtH_163",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  u1 {1,S}
4   Ct  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (264, 382, 1),
            (471, 621, 1),
            (572, 730, 1),
            (862, 1028, 1),
            (968, 1040, 1),
            (1307, 1351, 1),
            (3278, 3278, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 389,
    label = "Cs-Br1sCsCtH_272",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (197, 275, 1),
            (305, 447, 1),
            (392, 470, 1),
            (592, 728, 1),
            (1045, 1125, 1),
            (1180, 1218, 1),
            (3094, 3136, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 390,
    label = "Cs-Br1sCsCtH_290",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   u1 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (312, 362, 1),
            (366, 624, 1),
            (552, 674, 1),
            (916, 1024, 1),
            (1158, 1182, 1),
            (3086, 3186, 1),
            (3134, 3160, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 391,
    label = "Cs-Cl1sCsCtH_438",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (185, 269, 1),
            (264, 364, 1),
            (360, 438, 1),
            (617, 705, 1),
            (1054, 1174, 1),
            (1209, 1269, 1),
            (3071, 3119, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 392,
    label = "Cs-Cl1sCsCtH_439",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   u1 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (246, 328, 1),
            (328, 422, 1),
            (466, 628, 1),
            (580, 744, 1),
            (1072, 1278, 1),
            (1144, 1198, 1),
            (3031, 3195, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 393,
    label = "Cs-halO2sCdH_137",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (173, 299, 1),
            (433, 621, 1),
            (795, 915, 1),
            (939, 1091, 1),
            (1091, 1273, 1),
            (1281, 1415, 1),
            (3158, 3314, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 394,
    label = "Cs-F1sO2sCdH_137",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cd  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (173, 299, 1),
            (433, 621, 1),
            (795, 915, 1),
            (939, 1091, 1),
            (1091, 1273, 1),
            (1281, 1415, 1),
            (3158, 3314, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 395,
    label = "Cs-F1sO2sCdH_161",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s u1 {1,S}
4   Cd  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (331, 391, 1),
            (697, 841, 1),
            (865, 1065, 1),
            (1027, 1129, 1),
            (1107, 1157, 1),
            (1196, 1296, 1),
            (3200, 3294, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 396,
    label = "Cs-F1sO2sCdH_129",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cd  u1 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (136, 188, 1),
            (415, 555, 1),
            (554, 728, 1),
            (605, 837, 1),
            (877, 975, 1),
            (1210, 1374, 1),
            (1334, 1426, 1),
            (2975, 3151, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 397,
    label = "Cs-Br1sO2sCdH_261",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (154, 254, 1),
            (260, 360, 1),
            (261, 445, 1),
            (627, 725, 1),
            (1137, 1221, 1),
            (1169, 1261, 1),
            (3158, 3278, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 398,
    label = "Cs-Br1sO2sCdH_304",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cd   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (421, 515, 1),
            (635, 731, 1),
            (1037, 1157, 1),
            (1173, 1251, 1),
            (1372, 1482, 1),
            (3055, 3203, 1),
            (3098, 3182, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 399,
    label = "Cs-Br1sO2sCdH_360",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  u1 {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (320, 396, 1),
            (822, 872, 1),
            (1087, 1167, 1),
            (1166, 1240, 1),
            (1173, 1307, 1),
            (3189, 3251, 1),
            (3191, 3211, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 400,
    label = "Cs-Cl1sO2sCdH_468",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (224, 350, 1),
            (322, 426, 1),
            (539, 671, 1),
            (738, 852, 1),
            (1134, 1316, 1),
            (1177, 1271, 1),
            (3163, 3293, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 401,
    label = "Cs-Cl1sO2sCdH_477",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  u1 {1,S}
4   Cd   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (606, 774, 1),
            (698, 794, 1),
            (879, 923, 1),
            (1032, 1160, 1),
            (1150, 1246, 1),
            (3147, 3247, 1),
            (3215, 3275, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 402,
    label = "Cs-Cl1sO2sCdH_463",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cd   u1 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (118, 166, 1),
            (339, 453, 1),
            (389, 521, 1),
            (560, 660, 1),
            (614, 716, 1),
            (859, 937, 1),
            (1176, 1214, 1),
            (3074, 3180, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 403,
    label = "Cs-halhalCsCO_157",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cs   ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (216, 246, 1),
            (318, 378, 1),
            (319, 535, 1),
            (354, 456, 1),
            (1199, 1291, 1),
            (1208, 1264, 1),
            (1213, 1347, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 404,
    label = "Cs-F1sF1sCsCO_157",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
5   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (216, 246, 1),
            (318, 378, 1),
            (319, 535, 1),
            (354, 456, 1),
            (1199, 1291, 1),
            (1208, 1264, 1),
            (1213, 1347, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 405,
    label = "Cs-F1sF1sCsCO_185",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
5   CO  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (129, 209, 1),
            (346, 354, 1),
            (397, 405, 1),
            (444, 572, 1),
            (643, 807, 1),
            (1193, 1293, 1),
            (1203, 1243, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 406,
    label = "Cs-F1sF1sCsCO_145",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  u1 {1,S}
5   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (232, 266, 1),
            (285, 397, 1),
            (318, 444, 1),
            (596, 706, 1),
            (855, 1001, 1),
            (1179, 1255, 1),
            (1216, 1286, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 407,
    label = "Cs-Br1sBr1sCsCO_255",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (78, 278, 1),
            (146, 160, 1),
            (216, 302, 1),
            (231, 377, 1),
            (242, 268, 1),
            (257, 379, 1),
            (1139, 1193, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 408,
    label = "Cs-Br1sBr1sCsCO_710",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   u1 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (192, 210, 1),
            (213, 295, 1),
            (308, 408, 1),
            (568, 668, 1),
            (927, 1027, 1),
            (928, 1028, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 409,
    label = "Cs-Br1sBr1sCsCO_250",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (134, 148, 1),
            (155, 171, 1),
            (255, 397, 1),
            (276, 304, 1),
            (296, 320, 1),
            (535, 587, 1),
            (580, 648, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 410,
    label = "Cs-Cl1sCl1sCsCO_452",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (81, 255, 1),
            (190, 258, 1),
            (264, 386, 1),
            (271, 307, 1),
            (318, 494, 1),
            (744, 898, 1),
            (1077, 1245, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 411,
    label = "Cs-Cl1sCl1sCsCO_453",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (93, 331, 1),
            (148, 182, 1),
            (248, 270, 1),
            (285, 319, 1),
            (287, 387, 1),
            (507, 617, 1),
            (689, 731, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 412,
    label = "Cs-Cl1sCl1sCsCO_443",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   u1 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (217, 239, 1),
            (231, 355, 1),
            (277, 323, 1),
            (319, 471, 1),
            (325, 457, 1),
            (576, 646, 1),
            (1217, 1265, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 413,
    label = "Cs-Cl1sF1sCsCO_607",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (216, 258, 1),
            (221, 307, 1),
            (291, 479, 1),
            (305, 345, 1),
            (516, 642, 1),
            (1207, 1241, 1),
            (1243, 1243, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 414,
    label = "Cs-Cl1sF1sCsCO_695",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   u1 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (229, 271, 1),
            (231, 241, 1),
            (273, 331, 1),
            (308, 564, 1),
            (546, 626, 1),
            (1206, 1342, 1),
            (1210, 1258, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 415,
    label = "Cs-Cl1sF1sCsCO_722",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (196, 222, 1),
            (240, 254, 1),
            (302, 318, 1),
            (379, 393, 1),
            (470, 638, 1),
            (605, 605, 1),
            (1145, 1277, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 416,
    label = "Cs-Br1sCl1sCsCO_645",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (141, 329, 1),
            (180, 218, 1),
            (241, 283, 1),
            (252, 322, 1),
            (291, 403, 1),
            (582, 664, 1),
            (1110, 1230, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 417,
    label = "Cs-Br1sCl1sCsCO_675",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (170, 182, 1),
            (180, 250, 1),
            (265, 299, 1),
            (288, 352, 1),
            (298, 378, 1),
            (499, 631, 1),
            (577, 741, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 418,
    label = "Cs-Br1sCl1sCsCO_576",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   u1 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (206, 212, 1),
            (311, 313, 1),
            (365, 465, 1),
            (868, 968, 1),
            (965, 1065, 1),
            (1164, 1264, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 419,
    label = "Cs-Br1sF1sCsCO_684",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (206, 276, 1),
            (209, 245, 1),
            (210, 378, 1),
            (279, 311, 1),
            (351, 541, 1),
            (1195, 1281, 1),
            (1210, 1240, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 420,
    label = "Cs-Br1sF1sCsCO_697",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (142, 160, 1),
            (232, 324, 1),
            (256, 302, 1),
            (290, 310, 1),
            (446, 620, 1),
            (558, 558, 1),
            (1137, 1259, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 421,
    label = "Cs-Br1sF1sCsCO_643",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   u1 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (160, 210, 1),
            (216, 228, 1),
            (613, 753, 1),
            (638, 642, 1),
            (1232, 1332, 1),
            (1248, 1348, 1),
            (1258, 1346, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 422,
    label = "Cs-halCsC2sH_160",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   C2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (303, 403, 1),
            (394, 494, 1),
            (1203, 1303, 1),
            (3095, 3195, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 423,
    label = "Cs-F1sCsC2sH_160",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   C2s ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (303, 403, 1),
            (394, 494, 1),
            (1203, 1303, 1),
            (3095, 3195, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 424,
    label = "Cs-Br1sCsC2sH_363",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   C2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (305, 405, 1),
            (359, 459, 1),
            (894, 994, 1),
            (3102, 3202, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 425,
    label = "Cs-Cl1sCsC2sH_508",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   C2s  ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (269, 369, 1),
            (351, 451, 1),
            (919, 1019, 1),
            (3100, 3200, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 426,
    label = "Cs-halhalO2sCO_165",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   O2s  ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (218, 284, 1),
            (327, 407, 1),
            (463, 575, 1),
            (605, 795, 1),
            (835, 875, 1),
            (1140, 1210, 1),
            (1216, 1390, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 427,
    label = "Cs-F1sF1sO2sCO_165",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (218, 284, 1),
            (327, 407, 1),
            (463, 575, 1),
            (605, 795, 1),
            (835, 875, 1),
            (1140, 1210, 1),
            (1216, 1390, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 428,
    label = "Cs-F1sF1sO2sCO_199",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   CO  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (254, 254, 1),
            (363, 363, 1),
            (525, 525, 1),
            (544, 544, 1),
            (658, 658, 1),
            (1137, 1137, 1),
            (1402, 1402, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 429,
    label = "Cs-F1sF1sO2sCO_164",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s u1 {1,S}
5   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (327, 427, 1),
            (589, 689, 1),
            (864, 964, 1),
            (1285, 1385, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 430,
    label = "Cs-Br1sBr1sO2sCO_244",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (140, 156, 1),
            (239, 283, 1),
            (248, 402, 1),
            (271, 347, 1),
            (358, 528, 1),
            (583, 691, 1),
            (1287, 1431, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 431,
    label = "Cs-Br1sBr1sO2sCO_334",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (138, 138, 1),
            (166, 166, 1),
            (255, 255, 1),
            (319, 319, 1),
            (324, 324, 1),
            (537, 537, 1),
            (625, 625, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 432,
    label = "Cs-Cl1sCl1sO2sCO_447",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (141, 263, 1),
            (193, 279, 1),
            (316, 378, 1),
            (342, 386, 1),
            (423, 623, 1),
            (763, 861, 1),
            (1355, 1389, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 433,
    label = "Cs-Cl1sCl1sO2sCO_513",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  u1 {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (283, 383, 1),
            (300, 400, 1),
            (611, 711, 1),
            (875, 975, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 434,
    label = "Cs-Cl1sCl1sO2sCO_524",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (166, 202, 1),
            (254, 334, 1),
            (255, 257, 1),
            (316, 476, 1),
            (492, 636, 1),
            (515, 557, 1),
            (678, 736, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 435,
    label = "Cs-Br1sF1sO2sCO_621",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (44, 236, 1),
            (225, 271, 1),
            (262, 306, 1),
            (272, 320, 1),
            (561, 627, 1),
            (1117, 1251, 1),
            (1428, 1442, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 436,
    label = "Cs-Br1sF1sO2sCO_680",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (226, 226, 1),
            (262, 262, 1),
            (285, 285, 1),
            (300, 300, 1),
            (608, 608, 1),
            (650, 650, 1),
            (1389, 1389, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 437,
    label = "Cs-Br1sCl1sO2sCO_641",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (181, 213, 1),
            (212, 288, 1),
            (237, 319, 1),
            (295, 481, 1),
            (300, 428, 1),
            (591, 743, 1),
            (1353, 1381, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 438,
    label = "Cs-Br1sCl1sO2sCO_631",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (174, 174, 1),
            (215, 215, 1),
            (251, 251, 1),
            (320, 320, 1),
            (513, 513, 1),
            (560, 560, 1),
            (660, 660, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 439,
    label = "Cs-Cl1sF1sO2sCO_666",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (251, 279, 1),
            (300, 368, 1),
            (353, 389, 1),
            (409, 653, 1),
            (568, 716, 1),
            (1111, 1249, 1),
            (1430, 1440, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 440,
    label = "Cs-Cl1sF1sO2sCO_715",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  u1 {1,S}
5   CO   ux {1,S}
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 441,
    label = "Cs-Cl1sF1sO2sCO_720",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (249, 249, 1),
            (275, 275, 1),
            (342, 342, 1),
            (393, 393, 1),
            (614, 614, 1),
            (676, 676, 1),
            (1391, 1391, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 442,
    label = "Cs-halO2sCtH_169",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (135, 349, 1),
            (430, 498, 1),
            (615, 691, 1),
            (845, 933, 1),
            (1022, 1090, 1),
            (1318, 1366, 1),
            (3790, 3790, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 443,
    label = "Cs-F1sO2sCtH_169",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Ct  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (135, 349, 1),
            (430, 498, 1),
            (615, 691, 1),
            (845, 933, 1),
            (1022, 1090, 1),
            (1318, 1366, 1),
            (3790, 3790, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 444,
    label = "Cs-F1sO2sCtH_143",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s u1 {1,S}
4   Ct  ux {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (174, 270, 1),
            (394, 430, 1),
            (594, 610, 1),
            (628, 718, 1),
            (1032, 1070, 1),
            (1089, 1093, 1),
            (1197, 1203, 1),
            (1282, 1282, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 445,
    label = "Cs-Br1sO2sCtH_317",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (94, 220, 1),
            (285, 323, 1),
            (346, 430, 1),
            (588, 632, 1),
            (1117, 1237, 1),
            (1221, 1427, 1),
            (3784, 3784, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 446,
    label = "Cs-Br1sO2sCtH_340",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  u1 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (200, 228, 1),
            (200, 292, 1),
            (301, 371, 1),
            (522, 588, 1),
            (625, 751, 1),
            (859, 1025, 1),
            (1127, 1131, 1),
            (1212, 1258, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 447,
    label = "Cs-Cl1sO2sCtH_465",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (103, 223, 1),
            (364, 392, 1),
            (428, 448, 1),
            (606, 690, 1),
            (1136, 1268, 1),
            (1247, 1347, 1),
            (3786, 3786, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 448,
    label = "Cs-Cl1sO2sCtH_413",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  u1 {1,S}
4   Ct   ux {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (123, 217, 1),
            (316, 376, 1),
            (405, 441, 1),
            (622, 660, 1),
            (888, 1026, 1),
            (1027, 1079, 1),
            (1079, 1145, 1),
            (1141, 1275, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 449,
    label = "Cs-halhalO2sCt_170",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   O2s  ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (120, 194, 1),
            (342, 456, 1),
            (416, 456, 1),
            (560, 662, 1),
            (591, 611, 1),
            (673, 815, 1),
            (1097, 1157, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 450,
    label = "Cs-F1sF1sO2sCt_170",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
5   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (120, 194, 1),
            (342, 456, 1),
            (416, 456, 1),
            (560, 662, 1),
            (591, 611, 1),
            (673, 815, 1),
            (1097, 1157, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 451,
    label = "Cs-F1sF1sO2sCt_87",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s u1 {1,S}
5   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (131, 209, 1),
            (383, 439, 1),
            (392, 424, 1),
            (519, 673, 1),
            (587, 589, 1),
            (612, 724, 1),
            (1068, 1172, 1),
            (1095, 1111, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 452,
    label = "Cs-Br1sBr1sO2sCt_294",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (50, 142, 1),
            (114, 174, 1),
            (291, 337, 1),
            (294, 426, 1),
            (313, 353, 1),
            (339, 459, 1),
            (626, 658, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 453,
    label = "Cs-Cl1sCl1sO2sCt_470",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (114, 180, 1),
            (205, 319, 1),
            (375, 435, 1),
            (376, 394, 1),
            (439, 461, 1),
            (621, 753, 1),
            (634, 700, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 454,
    label = "Cs-Cl1sCl1sO2sCt_522",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  u1 {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (267, 367, 1),
            (374, 474, 1),
            (653, 753, 1),
            (1107, 1207, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 455,
    label = "Cs-Br1sCl1sO2sCt_650",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (113, 185, 1),
            (230, 308, 1),
            (298, 346, 1),
            (367, 413, 1),
            (417, 477, 1),
            (577, 663, 1),
            (609, 753, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 456,
    label = "Cs-Cl1sF1sO2sCt_663",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (128, 182, 1),
            (342, 358, 1),
            (385, 409, 1),
            (406, 460, 1),
            (521, 639, 1),
            (674, 686, 1),
            (831, 923, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 457,
    label = "Cs-Br1sF1sO2sCt_676",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
5   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (136, 230, 1),
            (284, 304, 1),
            (306, 332, 1),
            (371, 463, 1),
            (554, 634, 1),
            (621, 733, 1),
            (830, 882, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 458,
    label = "Cs-halhalCsC2s_181",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cs   ux {1,S}
5   C2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (297, 397, 1),
            (403, 503, 1),
            (1091, 1191, 1),
            (1418, 1518, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 459,
    label = "Cs-F1sF1sCsC2s_181",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
5   C2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (297, 397, 1),
            (403, 503, 1),
            (1091, 1191, 1),
            (1418, 1518, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 460,
    label = "Cs-Cl1sCl1sCsC2s_500",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
5   C2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (197, 297, 1),
            (206, 306, 1),
            (287, 387, 1),
            (1131, 1231, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 461,
    label = "Aldehyde",
    group = 
"""
1 * C        u0 {2,D} {3,S} {4,S}
2   O        ux {1,D}
3   R!H!Val7 ux {1,S}
4   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2695, 2870, 1),
            (700, 800, 1),
            (1380, 1410, 1),
            (450, 500, 1),
            (1750, 1800, 1),
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """carbon with double bond to oxygen and single bond to R""",
    longDesc = 
"""
(2695, 2870, 1),	#C-H stretch
(700, 800, 1),		#R-C-H bend
(1380, 1410, 1), 	#R-C-H bend
(450, 500, 1),		#OdC-R scissor
(1750, 1800, 1),	#OdC stretch
""",
)

entry(
    index = 462,
    label = "CO-halO2dCs_90",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (430, 542, 1),
            (558, 676, 1),
            (687, 849, 1),
            (1103, 1211, 1),
            (1906, 1946, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 463,
    label = "CO-F1sO2dCs_90",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   O2d ux {1,D}
4   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (430, 542, 1),
            (558, 676, 1),
            (687, 849, 1),
            (1103, 1211, 1),
            (1906, 1946, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 464,
    label = "CO-F1sO2dCs_116",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   O2d ux {1,D}
4   Cs  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (542, 680, 1),
            (621, 675, 1),
            (735, 925, 1),
            (1110, 1310, 1),
            (1739, 1767, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 465,
    label = "CO-Br1sO2dCs_239",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (275, 329, 1),
            (348, 430, 1),
            (467, 553, 1),
            (1042, 1168, 1),
            (1881, 1923, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 466,
    label = "CO-Br1sO2dCs_279",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   O2d  ux {1,D}
4   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (242, 304, 1),
            (243, 359, 1),
            (533, 577, 1),
            (1093, 1171, 1),
            (1720, 1770, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 467,
    label = "CO-Br1sO2dCs_335",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   O2d  ux {1,D}
4   Cs   u2 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (288, 388, 1),
            (630, 730, 1),
            (1116, 1216, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 468,
    label = "CO-Cl1sO2dCs_444",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   O2d  ux {1,D}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (174, 322, 1),
            (390, 456, 1),
            (465, 525, 1),
            (973, 1109, 1),
            (1879, 1923, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 469,
    label = "CO-Cl1sO2dCs_475",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   O2d  ux {1,D}
4   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (273, 381, 1),
            (510, 584, 1),
            (582, 682, 1),
            (1082, 1210, 1),
            (1702, 1754, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 470,
    label = "CO-halO2dCd_100",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   O2d  ux {1,D}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (184, 326, 1),
            (467, 599, 1),
            (735, 863, 1),
            (805, 859, 1),
            (1161, 1295, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 471,
    label = "CO-F1sO2dCd_100",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   O2d ux {1,D}
4   Cd  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (184, 326, 1),
            (467, 599, 1),
            (735, 863, 1),
            (805, 859, 1),
            (1161, 1295, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 472,
    label = "CO-F1sO2dCd_122",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   O2d ux {1,D}
4   Cd  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (81, 123, 1),
            (169, 197, 1),
            (422, 626, 1),
            (651, 745, 1),
            (784, 900, 1),
            (1131, 1291, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 473,
    label = "CO-Br1sO2dCd_281",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   O2d  ux {1,D}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (136, 196, 1),
            (310, 366, 1),
            (410, 558, 1),
            (679, 781, 1),
            (823, 923, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 474,
    label = "CO-Br1sO2dCd_314",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   O2d  ux {1,D}
4   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (91, 219, 1),
            (96, 168, 1),
            (302, 338, 1),
            (546, 568, 1),
            (617, 637, 1),
            (854, 1008, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 475,
    label = "CO-Cl1sO2dCd_454",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   O2d  ux {1,D}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (218, 308, 1),
            (321, 495, 1),
            (423, 501, 1),
            (718, 814, 1),
            (776, 974, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 476,
    label = "CO-Cl1sO2dCd_466",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   O2d  ux {1,D}
4   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (92, 222, 1),
            (100, 156, 1),
            (431, 497, 1),
            (562, 660, 1),
            (632, 652, 1),
            (820, 970, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 477,
    label = "CO-halO2sO2d_103",
    group = 
"""
1 * CO   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (394, 570, 1),
            (620, 708, 1),
            (742, 834, 1),
            (1217, 1375, 1),
            (1901, 1945, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 478,
    label = "CO-F1sO2sO2d_103",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   O2d ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (394, 570, 1),
            (620, 708, 1),
            (742, 834, 1),
            (1217, 1375, 1),
            (1901, 1945, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 479,
    label = "CO-F1sO2sO2d_195",
    group = 
"""
1 * CO  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   O2s u1 {1,S}
4   O2d ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (509, 509, 1),
            (537, 537, 1),
            (765, 765, 1),
            (1011, 1011, 1),
            (1202, 1202, 1),
            (1550, 1550, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 480,
    label = "CO-Br1sO2sO2d_287",
    group = 
"""
1 * CO   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (316, 450, 1),
            (359, 389, 1),
            (628, 652, 1),
            (683, 803, 1),
            (1867, 1889, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 481,
    label = "CO-Cl1sO2sO2d_445",
    group = 
"""
1 * CO   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (396, 464, 1),
            (470, 628, 1),
            (645, 775, 1),
            (690, 840, 1),
            (1866, 1892, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 482,
    label = "CO-halO2dC2s_155",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   O2d  ux {1,D}
4   C2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (475, 575, 1),
            (714, 814, 1),
            (1125, 1225, 1),
            (1245, 1345, 1),
            (1826, 1926, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 483,
    label = "CO-F1sO2dC2s_155",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   O2d ux {1,D}
4   C2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (475, 575, 1),
            (714, 814, 1),
            (1125, 1225, 1),
            (1245, 1345, 1),
            (1826, 1926, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 484,
    label = "CO-halO2dCO_159",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   O2d  ux {1,D}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (216, 356, 1),
            (532, 706, 1),
            (785, 851, 1),
            (1197, 1295, 1),
            (1909, 1939, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 485,
    label = "CO-F1sO2dCO_159",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   O2d ux {1,D}
4   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (216, 356, 1),
            (532, 706, 1),
            (785, 851, 1),
            (1197, 1295, 1),
            (1909, 1939, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 486,
    label = "CO-F1sO2dCO_190",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   O2d ux {1,D}
4   CO  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (233, 233, 1),
            (496, 496, 1),
            (705, 705, 1),
            (1150, 1150, 1),
            (2014, 2014, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 487,
    label = "CO-Br1sO2dCO_311",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   O2d  ux {1,D}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (170, 184, 1),
            (348, 362, 1),
            (442, 574, 1),
            (970, 1068, 1),
            (1860, 1890, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 488,
    label = "CO-Br1sO2dCO_345",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   O2d  ux {1,D}
4   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (123, 123, 1),
            (319, 319, 1),
            (399, 399, 1),
            (665, 665, 1),
            (2195, 2195, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 489,
    label = "CO-Cl1sO2dCO_497",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   O2d  ux {1,D}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (186, 244, 1),
            (393, 443, 1),
            (516, 602, 1),
            (997, 1111, 1),
            (1857, 1889, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 490,
    label = "CO-Cl1sO2dCO_499",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   O2d  ux {1,D}
4   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (141, 141, 1),
            (383, 383, 1),
            (516, 516, 1),
            (684, 684, 1),
            (2196, 2196, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 491,
    label = "CO-halO2dCt_192",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   O2d  ux {1,D}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (232, 274, 1),
            (570, 606, 1),
            (659, 735, 1),
            (800, 872, 1),
            (1146, 1226, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 492,
    label = "CO-F1sO2dCt_192",
    group = 
"""
1 * CO  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   O2d ux {1,D}
4   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (232, 274, 1),
            (570, 606, 1),
            (659, 735, 1),
            (800, 872, 1),
            (1146, 1226, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 493,
    label = "CO-Br1sO2dCt_330",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   O2d  ux {1,D}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (214, 314, 1),
            (338, 348, 1),
            (377, 409, 1),
            (639, 645, 1),
            (865, 1085, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 494,
    label = "CO-Cl1sO2dCt_412",
    group = 
"""
1 * CO   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   O2d  ux {1,D}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (194, 294, 1),
            (403, 419, 1),
            (498, 700, 1),
            (600, 702, 1),
            (905, 1091, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 495,
    label = "Ketene",
    group = 
"""
1 * Cdd u0 {2,D} {3,D}
2   O2d u0 {1,D}
3   C   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2110, 2130, 1),
            (495, 530, 1),
            (650, 925, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """carbon with one carbon double bond and one oxygen double bond""",
    longDesc = 
"""
(2110, 2130, 1),	#OdC stretch
(495, 530, 1),		#OdCdC bend
(650, 925, 1),		#OdCdC bend
""",
)

entry(
    index = 496,
    label = "Cumulene",
    group = 
"""
1 * C u0 {2,D} {3,D}
2   C ux {1,D}
3   C ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (540, 610, 2),
            (1970, 2140, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """Carbon with two double bonds to carbons""",
    longDesc = 
"""
(540, 610, 2),	#C-C-C scissor
(1970, 2140, 1),#C-C-C asymmetric
""",
)

entry(
    index = 497,
    label = "CdCHsR",
    group = 
"""
1 * C        u0 {2,D} {3,S} {4,S}
2   C        ux {1,D}
3   R!H!Val7 ux {1,S}
4   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2995, 3025, 1),
            (975, 1000, 1),
            (1300, 1375, 1),
            (400, 500, 1),
            (1630, 1680, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """carbon with a double bond to carbon and a single bond to R""",
    longDesc = 
"""
(2995, 3025, 1),	#C-H stretch
(975, 1000, 1),		#R-C-H bend
(1300, 1375, 1),	#R-C-H bend
(400, 500, 1),		#CdC-R scissor
(1630, 1680, 1),	#CdC stretch
""",
)

entry(
    index = 498,
    label = "Cd-halCdCt_44",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   Cd   ux {1,D}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (120, 238, 1),
            (387, 459, 1),
            (590, 668, 1),
            (717, 905, 1),
            (783, 993, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 499,
    label = "Cd-F1sCdCt_44",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   Cd  ux {1,D}
4   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (120, 238, 1),
            (387, 459, 1),
            (590, 668, 1),
            (717, 905, 1),
            (783, 993, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 500,
    label = "Cd-F1sCtCd_96",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   Ct  ux {1,S}
4   Cd  u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (281, 363, 1),
            (331, 511, 1),
            (546, 670, 1),
            (589, 625, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 501,
    label = "Cd-Br1sCdCt_277",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,D}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (233, 375, 1),
            (346, 502, 1),
            (381, 547, 1),
            (563, 735, 1),
            (619, 791, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 502,
    label = "Cd-Br1sCtCd_295",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Ct   ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (119, 247, 1),
            (262, 400, 1),
            (343, 453, 1),
            (496, 612, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 503,
    label = "Cd-Cl1sCdCt_488",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,D}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (267, 357, 1),
            (369, 459, 1),
            (515, 701, 1),
            (521, 681, 1),
            (728, 936, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 504,
    label = "Cd-Cl1sCtCd_489",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Ct   ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (229, 303, 1),
            (262, 390, 1),
            (447, 531, 1),
            (522, 688, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 505,
    label = "Cd-halCsCd_56",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (260, 386, 1),
            (409, 525, 1),
            (515, 635, 1),
            (761, 893, 1),
            (1354, 1482, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 506,
    label = "Cd-F1sCsCd_56",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (260, 386, 1),
            (409, 525, 1),
            (515, 635, 1),
            (761, 893, 1),
            (1354, 1482, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 507,
    label = "Cd-F1sCdCs_76",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   Cd  ux {1,D}
4   Cs  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (206, 336, 1),
            (431, 607, 1),
            (515, 611, 1),
            (528, 696, 1),
            (1312, 1446, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 508,
    label = "Cd-F1sCsCd_118",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cd  u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (161, 331, 1),
            (427, 521, 1),
            (441, 625, 1),
            (1076, 1234, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 509,
    label = "Cd-Br1sCsCd_224",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (177, 229, 1),
            (276, 336, 1),
            (401, 499, 1),
            (565, 629, 1),
            (1092, 1170, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 510,
    label = "Cd-Br1sCsCd_253",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (223, 343, 1),
            (362, 480, 1),
            (443, 519, 1),
            (490, 602, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 511,
    label = "Cd-Br1sCdCs_263",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,D}
4   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (164, 270, 1),
            (228, 302, 1),
            (457, 537, 1),
            (596, 708, 1),
            (699, 825, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 512,
    label = "Cd-Cl1sCsCd_411",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (209, 351, 1),
            (351, 469, 1),
            (453, 605, 1),
            (590, 710, 1),
            (1044, 1222, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 513,
    label = "Cd-Cl1sCsCd_432",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (195, 349, 1),
            (410, 496, 1),
            (469, 597, 1),
            (1016, 1144, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 514,
    label = "Cd-Cl1sCdCs_433",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,D}
4   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (188, 378, 1),
            (217, 329, 1),
            (455, 571, 1),
            (537, 709, 1),
            (683, 799, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 515,
    label = "Cd-halO2sCd_81",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (262, 390, 1),
            (483, 597, 1),
            (572, 732, 1),
            (631, 807, 1),
            (1275, 1439, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 516,
    label = "Cd-F1sO2sCd_81",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (262, 390, 1),
            (483, 597, 1),
            (572, 732, 1),
            (631, 807, 1),
            (1275, 1439, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 517,
    label = "Cd-F1sO2sCd_71",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cd  u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (222, 364, 1),
            (420, 572, 1),
            (498, 576, 1),
            (1187, 1249, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 518,
    label = "Cd-Br1sO2sCd_252",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (216, 304, 1),
            (317, 401, 1),
            (457, 583, 1),
            (524, 728, 1),
            (636, 766, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 519,
    label = "Cd-Br1sO2sCd_258",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (264, 374, 1),
            (404, 496, 1),
            (471, 549, 1),
            (528, 628, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 520,
    label = "Cd-Cl1sO2sCd_384",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (254, 350, 1),
            (366, 454, 1),
            (499, 579, 1),
            (632, 734, 1),
            (683, 853, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 521,
    label = "Cd-Cl1sO2sCd_436",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (196, 322, 1),
            (442, 510, 1),
            (486, 618, 1),
            (567, 695, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 522,
    label = "Cd-Cl1sO2sCd_512",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   O2s  u1 {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (328, 428, 1),
            (819, 919, 1),
            (1083, 1183, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 523,
    label = "Cd-halCdCd_91",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   Cd   ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (217, 343, 1),
            (449, 587, 1),
            (660, 812, 1),
            (790, 914, 1),
            (798, 948, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 524,
    label = "Cd-F1sCdCd_91",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   Cd  ux {1,S}
4   Cd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (217, 343, 1),
            (449, 587, 1),
            (660, 812, 1),
            (790, 914, 1),
            (798, 948, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 525,
    label = "Cd-F1sCdCd_92",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   Cd  ux {1,S}
4   Cd  u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (174, 326, 1),
            (386, 506, 1),
            (510, 668, 1),
            (789, 919, 1),
            (801, 997, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 526,
    label = "Cd-F1sCdCd_127",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   Cd  ux {1,D}
4   Cd  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (59, 113, 1),
            (117, 289, 1),
            (459, 517, 1),
            (515, 649, 1),
            (544, 666, 1),
            (703, 779, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 527,
    label = "Cd-Br1sCdCd_285",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cd   ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (147, 213, 1),
            (298, 398, 1),
            (481, 583, 1),
            (548, 682, 1),
            (691, 805, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 528,
    label = "Cd-Br1sCdCd_292",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,D}
4   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (114, 156, 1),
            (137, 237, 1),
            (369, 491, 1),
            (459, 507, 1),
            (499, 671, 1),
            (623, 741, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 529,
    label = "Cd-Br1sCdCd_270",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cd   ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (126, 206, 1),
            (245, 409, 1),
            (355, 485, 1),
            (529, 635, 1),
            (672, 786, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 530,
    label = "Cd-Cl1sCdCd_402",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cd   ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (151, 265, 1),
            (309, 413, 1),
            (498, 608, 1),
            (656, 786, 1),
            (755, 885, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 531,
    label = "Cd-Cl1sCdCd_422",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,D}
4   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (47, 117, 1),
            (166, 268, 1),
            (462, 530, 1),
            (486, 656, 1),
            (488, 520, 1),
            (637, 789, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 532,
    label = "Cd-Cl1sCdCd_440",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cd   ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (223, 313, 1),
            (336, 464, 1),
            (520, 646, 1),
            (549, 721, 1),
            (775, 933, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 533,
    label = "Cd-halCOCd_99",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   CO   ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (239, 337, 1),
            (351, 469, 1),
            (659, 789, 1),
            (775, 903, 1),
            (1272, 1368, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 534,
    label = "Cd-F1sCOCd_99",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   CO  ux {1,S}
4   Cd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (239, 337, 1),
            (351, 469, 1),
            (659, 789, 1),
            (775, 903, 1),
            (1272, 1368, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 535,
    label = "Cd-F1sCOCd_179",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   CO  ux {1,S}
4   Cd  u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (188, 300, 1),
            (332, 436, 1),
            (622, 760, 1),
            (1184, 1298, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 536,
    label = "Cd-F1sCdCO_180",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   Cd  ux {1,D}
4   CO  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (191, 291, 1),
            (347, 447, 1),
            (1170, 1270, 1),
            (1682, 1782, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 537,
    label = "Cd-Br1sCOCd_280",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   CO   ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (154, 200, 1),
            (297, 351, 1),
            (535, 601, 1),
            (543, 709, 1),
            (1110, 1184, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 538,
    label = "Cd-Br1sCdCO_329",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,D}
4   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (163, 185, 1),
            (180, 256, 1),
            (293, 347, 1),
            (330, 432, 1),
            (493, 647, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 539,
    label = "Cd-Br1sCOCd_349",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   CO   ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (140, 214, 1),
            (233, 361, 1),
            (404, 444, 1),
            (1044, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 540,
    label = "Cd-Cl1sCOCd_451",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   CO   ux {1,S}
4   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (191, 257, 1),
            (321, 433, 1),
            (562, 720, 1),
            (620, 674, 1),
            (1193, 1241, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 541,
    label = "Cd-Cl1sCdCO_473",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,D}
4   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (131, 203, 1),
            (206, 290, 1),
            (299, 347, 1),
            (496, 660, 1),
            (536, 572, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 542,
    label = "Cd-Cl1sCOCd_487",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   CO   ux {1,S}
4   Cd   u1 {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (186, 236, 1),
            (263, 403, 1),
            (591, 669, 1),
            (1072, 1124, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 543,
    label = "Cd-halCsCdd_141",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (104, 186, 1),
            (245, 407, 1),
            (330, 466, 1),
            (761, 907, 1),
            (1218, 1388, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 544,
    label = "Cd-F1sCsCdd_141",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cdd ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (104, 186, 1),
            (245, 407, 1),
            (330, 466, 1),
            (761, 907, 1),
            (1218, 1388, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 545,
    label = "Cd-F1sCsCdd_150",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   Cs  u1 {1,S}
4   Cdd ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (80, 184, 1),
            (368, 474, 1),
            (895, 995, 1),
            (1140, 1198, 1),
            (1264, 1272, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 546,
    label = "Cd-Br1sCsCdd_247",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (101, 151, 1),
            (182, 298, 1),
            (251, 391, 1),
            (417, 495, 1),
            (1042, 1182, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 547,
    label = "Cd-Br1sCsCdd_620",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   Cs   u1 {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (117, 207, 1),
            (123, 169, 1),
            (416, 436, 1),
            (1140, 1202, 1),
            (1232, 1424, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 548,
    label = "Cd-Cl1sCsCdd_421",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (109, 159, 1),
            (207, 359, 1),
            (311, 465, 1),
            (821, 985, 1),
            (1043, 1145, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 549,
    label = "Cd-Cl1sCsCdd_503",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   Cs   u1 {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (396, 502, 1),
            (983, 1167, 1),
            (1176, 1306, 1),
            (1235, 1357, 1),
            (1329, 1449, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 550,
    label = "Cd-halO2sCdd_153",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (95, 299, 1),
            (141, 301, 1),
            (339, 523, 1),
            (526, 788, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 551,
    label = "Cd-F1sO2sCdd_153",
    group = 
"""
1 * Cd  u0 {2,S} {3,S} {4,D}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cdd ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (95, 299, 1),
            (141, 301, 1),
            (339, 523, 1),
            (526, 788, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 552,
    label = "Cd-Br1sO2sCdd_291",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (85, 155, 1),
            (202, 302, 1),
            (283, 413, 1),
            (357, 451, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 553,
    label = "Cd-Cl1sO2sCdd_408",
    group = 
"""
1 * Cd   u0 {2,S} {3,S} {4,D}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (90, 154, 1),
            (228, 352, 1),
            (328, 432, 1),
            (412, 532, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 554,
    label = "Cd-halCdC2s_175",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Val7 u0 {1,S}
3   Cd   ux {1,D}
4   C2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (355, 455, 1),
            (706, 806, 1),
            (836, 936, 1),
            (1162, 1262, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 555,
    label = "Cd-F1sCdC2s_175",
    group = 
"""
1 * Cd  u0 {2,S} {3,D} {4,S}
2   F1s u0 {1,S}
3   Cd  ux {1,D}
4   C2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (355, 455, 1),
            (706, 806, 1),
            (836, 936, 1),
            (1162, 1262, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 556,
    label = "Cd-Br1sCdC2s_296",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,D}
4   C2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (400, 500, 1),
            (416, 516, 1),
            (626, 726, 1),
            (1150, 1250, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 557,
    label = "Cd-Cl1sCdC2s_482",
    group = 
"""
1 * Cd   u0 {2,S} {3,D} {4,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,D}
4   C2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (426, 526, 1),
            (535, 635, 1),
            (715, 815, 1),
            (1160, 1260, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 558,
    label = "CtCsR",
    group = 
"""
1 * C        u0 {2,T} {3,S}
2   C        ux {1,T}
3   R!H!Val7 ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2100, 2250, 1),
            (500, 550, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """carbon with one triplet bond and one single bond""",
    longDesc = 
"""
(2100, 2250, 1),	#CtC stretch
(500, 550, 1),		#CtC-C bend
""",
)

entry(
    index = 559,
    label = "RsCHsR2",
    group = 
"""
1 * C        u0 {2,S} {3,S} {4,S} {5,S}
2   R!H!Val7 ux {1,S}
3   R!H!Val7 ux {1,S}
4   R!H!Val7 ux {1,S}
5   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1380, 1390, 2),
            (370, 380, 2),
            (2800, 3000, 1),
            (430, 440, 1),
        ],
        symmetry = 6,
    ),
    shortDesc = """carbon with three single bonds""",
    longDesc = 
"""
(1380, 1390, 2),	#R-C-H bend
(370, 380, 2),		#C-C-C scissor
(2800, 3000, 1),	#C-H stretch
(430, 440, 1),		#Umbrella
""",
)

entry(
    index = 560,
    label = "Cs-halO2sO2sCs_62",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (334, 416, 1),
            (343, 379, 1),
            (494, 674, 1),
            (498, 632, 1),
            (628, 816, 1),
            (1447, 1501, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 561,
    label = "Cs-F1sO2sO2sCs_62",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   O2s ux {1,S}
5   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (334, 416, 1),
            (343, 379, 1),
            (494, 674, 1),
            (498, 632, 1),
            (628, 816, 1),
            (1447, 1501, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 562,
    label = "Cs-F1sO2sO2sCs_114",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   O2s u1 {1,S}
5   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (256, 490, 1),
            (321, 351, 1),
            (424, 580, 1),
            (426, 528, 1),
            (623, 793, 1),
            (1146, 1294, 1),
            (1477, 1477, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 563,
    label = "Cs-F1sO2sO2sCs_147",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   O2s ux {1,S}
5   Cs  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (328, 400, 1),
            (404, 544, 1),
            (507, 651, 1),
            (541, 697, 1),
            (589, 721, 1),
            (1288, 1402, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 564,
    label = "Cs-Br1sO2sO2sCs_260",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (257, 287, 1),
            (278, 358, 1),
            (287, 317, 1),
            (348, 480, 1),
            (503, 605, 1),
            (614, 692, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 565,
    label = "Cs-Br1sO2sO2sCs_681",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (107, 147, 1),
            (255, 311, 1),
            (367, 443, 1),
            (534, 568, 1),
            (632, 682, 1),
            (1464, 1564, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 566,
    label = "Cs-Cl1sO2sO2sCs_435",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (285, 329, 1),
            (326, 366, 1),
            (379, 425, 1),
            (401, 531, 1),
            (550, 696, 1),
            (626, 728, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 567,
    label = "Cs-Cl1sO2sO2sCs_659",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  u1 {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (353, 453, 1),
            (510, 610, 1),
            (753, 853, 1),
            (1912, 2012, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 568,
    label = "Cs-Cl1sO2sO2sCs_391",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (274, 334, 1),
            (324, 356, 1),
            (460, 524, 1),
            (1258, 1452, 1),
            (1412, 1498, 1),
            (3220, 3232, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 569,
    label = "Cs-halO2sCsCs_63",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (318, 348, 1),
            (354, 414, 1),
            (366, 530, 1),
            (521, 695, 1),
            (1154, 1354, 1),
            (1414, 1546, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 570,
    label = "Cs-F1sO2sCsCs_63",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cs  ux {1,S}
5   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (318, 348, 1),
            (354, 414, 1),
            (366, 530, 1),
            (521, 695, 1),
            (1154, 1354, 1),
            (1414, 1546, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 571,
    label = "Cs-F1sO2sCsCs_152",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cs  ux {1,S}
5   Cs  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (289, 343, 1),
            (342, 428, 1),
            (440, 590, 1),
            (571, 737, 1),
            (593, 785, 1),
            (1204, 1386, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 572,
    label = "Cs-F1sO2sCsCs_51",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   O2s u1 {1,S}
4   Cs  ux {1,S}
5   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (269, 303, 1),
            (302, 366, 1),
            (359, 515, 1),
            (402, 442, 1),
            (580, 716, 1),
            (866, 924, 1),
            (1136, 1238, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 573,
    label = "Cs-Br1sO2sCsCs_275",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (259, 281, 1),
            (287, 367, 1),
            (288, 312, 1),
            (319, 457, 1),
            (421, 595, 1),
            (1449, 1501, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 574,
    label = "Cs-Br1sO2sCsCs_351",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (308, 342, 1),
            (419, 467, 1),
            (509, 599, 1),
            (1227, 1431, 1),
            (1405, 1525, 1),
            (1425, 1525, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 575,
    label = "Cs-Br1sO2sCsCs_358",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   O2s  u1 {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (183, 271, 1),
            (248, 260, 1),
            (250, 284, 1),
            (276, 346, 1),
            (320, 414, 1),
            (485, 639, 1),
            (1167, 1199, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 576,
    label = "Cs-Cl1sO2sCsCs_459",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (292, 314, 1),
            (315, 363, 1),
            (347, 497, 1),
            (366, 424, 1),
            (456, 616, 1),
            (1477, 1489, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 577,
    label = "Cs-Cl1sO2sCsCs_464",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  u1 {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (122, 282, 1),
            (258, 280, 1),
            (289, 335, 1),
            (329, 443, 1),
            (342, 374, 1),
            (540, 686, 1),
            (1157, 1207, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 578,
    label = "Cs-Cl1sO2sCsCs_417",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (227, 299, 1),
            (293, 339, 1),
            (311, 391, 1),
            (331, 459, 1),
            (437, 583, 1),
            (1367, 1531, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 579,
    label = "Cs-halCsCsCs_123",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (296, 346, 1),
            (317, 337, 1),
            (349, 417, 1),
            (352, 538, 1),
            (437, 551, 1),
            (1488, 1512, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 580,
    label = "Cs-F1sCsCsCs_123",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cs  ux {1,S}
5   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (296, 346, 1),
            (317, 337, 1),
            (349, 417, 1),
            (352, 538, 1),
            (437, 551, 1),
            (1488, 1512, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 581,
    label = "Cs-F1sCsCsCs_105",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cs  ux {1,S}
5   Cs  u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (249, 329, 1),
            (295, 327, 1),
            (345, 419, 1),
            (375, 595, 1),
            (616, 790, 1),
            (1288, 1506, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 582,
    label = "Cs-Br1sCsCsCs_307",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (243, 445, 1),
            (261, 355, 1),
            (262, 276, 1),
            (277, 305, 1),
            (373, 473, 1),
            (495, 627, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 583,
    label = "Cs-Br1sCsCsCs_326",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (266, 462, 1),
            (336, 362, 1),
            (383, 455, 1),
            (385, 489, 1),
            (1193, 1209, 1),
            (1487, 1493, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 584,
    label = "Cs-Cl1sCsCsCs_395",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
5   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (277, 327, 1),
            (287, 303, 1),
            (328, 388, 1),
            (350, 544, 1),
            (359, 465, 1),
            (613, 763, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 585,
    label = "Cs-Cl1sCsCsCs_406",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
5   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (262, 292, 1),
            (297, 333, 1),
            (297, 495, 1),
            (319, 375, 1),
            (440, 602, 1),
            (1484, 1490, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 586,
    label = "CdCsR2",
    group = 
"""
1 * C        u0 {2,D} {3,S} {4,S}
2   C        ux {1,D}
3   R!H!Val7 ux {1,S}
4   R!H!Val7 ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (325, 375, 1),
            (415, 465, 1),
            (420, 450, 1),
            (1700, 1750, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """carbon with one carbon double bond and two single bonds""",
    longDesc = 
"""
(325, 375, 1),	#R-C-R scissor
(415, 465, 1),	#CdC-R scissor
(420, 450, 1),	#Umbrella
(1700, 1750, 1),#CdC stretch
""",
)

entry(
    index = 587,
    label = "Ketone",
    group = 
"""
1 * C u0 {2,D} {3,S} {4,S}
2   O u0 {1,D}
3   C ux {1,S}
4   C ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (365, 385, 1),
            (505, 600, 1),
            (445, 480, 1),
            (1700, 1720, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """carbon with one oxygen double bond and two single bonds""",
    longDesc = 
"""
(365, 385, 1),	#R-C-R scissor
(505, 600, 1),	#OdC-R scissor
(445, 480, 1),	#Umbrella
(1700, 1720, 1),#OdC stretch
""",
)

entry(
    index = 588,
    label = "CsCsC3",
    group = 
"""
1 * C u0 {2,S} {3,S} {4,S} {5,S}
2   C ux {1,S}
3   C ux {1,S}
4   C ux {1,S}
5   C ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (350, 400, 2),
            (1190, 1240, 2),
            (400, 500, 1),
        ],
        symmetry = 12,
    ),
    shortDesc = """carbon with four single bonds to carbon""",
    longDesc = 
"""
(350, 400, 2),	#C-C-C scissor
(1190, 1240, 2),#C-C-C bend
(400, 500, 1),	#Umbrella
""",
)

entry(
    index = 589,
    label = "C2s-halCs_64",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (535, 699, 1),
            (831, 965, 1),
            (1159, 1215, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 590,
    label = "C2s-F1sCs_64",
    group = 
"""
1 * C2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (535, 699, 1),
            (831, 965, 1),
            (1159, 1215, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 591,
    label = "C2s-Br1sCs_333",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (155, 251, 1),
            (515, 613, 1),
            (1091, 1163, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 592,
    label = "C2s-Cl1sCs_455",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (495, 525, 1),
            (597, 657, 1),
            (1043, 1151, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 593,
    label = "Cs-halHHH_98",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1097, 1097, 1),
            (1206, 1206, 1),
            (1206, 1206, 1),
            (1493, 1493, 1),
            (1493, 1493, 1),
            (1509, 1509, 1),
            (3011, 3011, 1),
            (3086, 3086, 1),
            (3086, 3086, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 594,
    label = "Cs-F1sHHH_98",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1097, 1097, 1),
            (1206, 1206, 1),
            (1206, 1206, 1),
            (1493, 1493, 1),
            (1493, 1493, 1),
            (1509, 1509, 1),
            (3011, 3011, 1),
            (3086, 3086, 1),
            (3086, 3086, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 595,
    label = "Cs-Br1sHHH_342",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (598, 598, 1),
            (962, 962, 1),
            (962, 962, 1),
            (1328, 1328, 1),
            (1472, 1472, 1),
            (1472, 1472, 1),
            (3087, 3087, 1),
            (3198, 3198, 1),
            (3198, 3198, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 596,
    label = "Cs-Cl1sHHH_502",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (720, 720, 1),
            (1022, 1022, 1),
            (1022, 1022, 1),
            (1374, 1374, 1),
            (1478, 1478, 1),
            (1478, 1478, 1),
            (3074, 3074, 1),
            (3177, 3177, 1),
            (3177, 3177, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 597,
    label = "C2s-halCO_156",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (246, 278, 1),
            (1286, 1294, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 598,
    label = "C2s-F1sCO_156",
    group = 
"""
1 * C2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (246, 278, 1),
            (1286, 1294, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 599,
    label = "Cs-halhalhalH_168",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Val7 u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (506, 506, 1),
            (506, 506, 1),
            (703, 703, 1),
            (1151, 1151, 1),
            (1179, 1179, 1),
            (1179, 1179, 1),
            (1414, 1414, 1),
            (1414, 1414, 1),
            (3086, 3086, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 600,
    label = "Cs-F1sF1sF1sH_168",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (506, 506, 1),
            (506, 506, 1),
            (703, 703, 1),
            (1151, 1151, 1),
            (1179, 1179, 1),
            (1179, 1179, 1),
            (1414, 1414, 1),
            (1414, 1414, 1),
            (3086, 3086, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 601,
    label = "Cs-Br1sBr1sBr1sH_361",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (150, 150, 1),
            (150, 150, 1),
            (220, 220, 1),
            (532, 532, 1),
            (639, 639, 1),
            (639, 639, 1),
            (1161, 1161, 1),
            (1161, 1161, 1),
            (3194, 3194, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 602,
    label = "Cs-Cl1sCl1sCl1sH_519",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (256, 256, 1),
            (256, 256, 1),
            (362, 362, 1),
            (664, 664, 1),
            (741, 741, 1),
            (742, 742, 1),
            (1226, 1226, 1),
            (1226, 1226, 1),
            (3175, 3175, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 603,
    label = "Cs-Cl1sCl1sF1sH_657",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (268, 268, 1),
            (362, 362, 1),
            (451, 451, 1),
            (721, 721, 1),
            (762, 762, 1),
            (1141, 1141, 1),
            (1244, 1244, 1),
            (1339, 1339, 1),
            (3140, 3140, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 604,
    label = "Cs-Br1sCl1sCl1sH_670",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (210, 210, 1),
            (216, 216, 1),
            (326, 326, 1),
            (592, 592, 1),
            (705, 705, 1),
            (743, 743, 1),
            (1185, 1185, 1),
            (1224, 1224, 1),
            (3181, 3181, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 605,
    label = "Cs-Cl1sF1sF1sH_671",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (358, 358, 1),
            (399, 399, 1),
            (600, 600, 1),
            (774, 774, 1),
            (1140, 1140, 1),
            (1179, 1179, 1),
            (1317, 1317, 1),
            (1394, 1394, 1),
            (3110, 3110, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 606,
    label = "Cs-Br1sBr1sCl1sH_685",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (163, 163, 1),
            (196, 196, 1),
            (276, 276, 1),
            (561, 561, 1),
            (641, 641, 1),
            (729, 729, 1),
            (1162, 1162, 1),
            (1204, 1204, 1),
            (3187, 3187, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 607,
    label = "Cs-Br1sBr1sF1sH_723",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (164, 164, 1),
            (294, 294, 1),
            (352, 352, 1),
            (611, 611, 1),
            (674, 674, 1),
            (1135, 1135, 1),
            (1180, 1180, 1),
            (1320, 1320, 1),
            (3147, 3147, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 608,
    label = "Cs-Br1sF1sF1sH_724",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (309, 309, 1),
            (309, 309, 1),
            (585, 585, 1),
            (692, 692, 1),
            (1135, 1135, 1),
            (1180, 1180, 1),
            (1286, 1286, 1),
            (1388, 1388, 1),
            (3112, 3112, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 609,
    label = "Cs-Br1sCl1sF1sH_729",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (216, 216, 1),
            (308, 308, 1),
            (419, 419, 1),
            (642, 642, 1),
            (745, 745, 1),
            (1138, 1138, 1),
            (1211, 1211, 1),
            (1330, 1330, 1),
            (3143, 3143, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 610,
    label = "C2s-halCt_171",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (252, 252, 1),
            (948, 948, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 611,
    label = "C2s-F1sCt_171",
    group = 
"""
1 * C2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (252, 252, 1),
            (948, 948, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 612,
    label = "C2s-halCd_176",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (277, 353, 1),
            (605, 639, 1),
            (1128, 1128, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 613,
    label = "C2s-F1sCd_176",
    group = 
"""
1 * C2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   Cd  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (277, 353, 1),
            (605, 639, 1),
            (1128, 1128, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 614,
    label = "C2s-Br1sCd_297",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (230, 290, 1),
            (634, 634, 1),
            (668, 668, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 615,
    label = "C2s-Cl1sCd_483",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (240, 334, 1),
            (548, 730, 1),
            (742, 742, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 616,
    label = "C2s-halO2s_178",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (655, 665, 1),
            (1253, 1413, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 617,
    label = "C2s-F1sO2s_178",
    group = 
"""
1 * C2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (655, 665, 1),
            (1253, 1413, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 618,
    label = "C2s-Br1sO2s_319",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (236, 384, 1),
            (502, 736, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 619,
    label = "C2s-Cl1sO2s_461",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (391, 459, 1),
            (702, 840, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 620,
    label = "Cs-halhalhalhal_186",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Val7 u0 {1,S}
5   Val7 u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (429, 429, 1),
            (429, 429, 1),
            (625, 625, 1),
            (625, 625, 1),
            (625, 625, 1),
            (914, 914, 1),
            (1289, 1289, 1),
            (1289, 1289, 1),
            (1289, 1289, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 621,
    label = "Cs-F1sF1sF1sF1s_186",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
5   F1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (429, 429, 1),
            (429, 429, 1),
            (625, 625, 1),
            (625, 625, 1),
            (625, 625, 1),
            (914, 914, 1),
            (1289, 1289, 1),
            (1289, 1289, 1),
            (1289, 1289, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 622,
    label = "Cs-Br1sBr1sBr1sBr1s_238",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   Br1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (123, 123, 1),
            (123, 123, 1),
            (181, 181, 1),
            (181, 181, 1),
            (181, 181, 1),
            (264, 264, 1),
            (643, 643, 1),
            (643, 643, 1),
            (644, 644, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 623,
    label = "Cs-Cl1sCl1sCl1sCl1s_518",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (214, 214, 1),
            (214, 214, 1),
            (311, 311, 1),
            (311, 311, 1),
            (311, 311, 1),
            (453, 453, 1),
            (754, 754, 1),
            (754, 754, 1),
            (754, 754, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 624,
    label = "Cs-Cl1sCl1sF1sF1s_593",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (253, 253, 1),
            (316, 316, 1),
            (426, 426, 1),
            (429, 429, 1),
            (444, 444, 1),
            (666, 666, 1),
            (858, 858, 1),
            (1128, 1128, 1),
            (1217, 1217, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 625,
    label = "Cs-Br1sCl1sCl1sCl1s_674",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (187, 187, 1),
            (187, 187, 1),
            (242, 242, 1),
            (292, 292, 1),
            (292, 292, 1),
            (416, 416, 1),
            (694, 694, 1),
            (748, 748, 1),
            (748, 748, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 626,
    label = "Cs-Br1sBr1sCl1sCl1s_689",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (151, 151, 1),
            (171, 171, 1),
            (227, 227, 1),
            (238, 238, 1),
            (260, 260, 1),
            (376, 376, 1),
            (661, 661, 1),
            (712, 712, 1),
            (745, 745, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 627,
    label = "Cs-Br1sBr1sBr1sF1s_691",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (145, 145, 1),
            (145, 145, 1),
            (212, 212, 1),
            (304, 304, 1),
            (305, 305, 1),
            (393, 393, 1),
            (710, 710, 1),
            (710, 710, 1),
            (1123, 1123, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 628,
    label = "Cs-Br1sF1sF1sF1s_693",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (298, 298, 1),
            (298, 298, 1),
            (336, 336, 1),
            (549, 549, 1),
            (549, 549, 1),
            (760, 760, 1),
            (1072, 1072, 1),
            (1246, 1246, 1),
            (1246, 1246, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 629,
    label = "Cs-Cl1sCl1sCl1sF1s_696",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (238, 238, 1),
            (238, 238, 1),
            (341, 341, 1),
            (393, 393, 1),
            (393, 393, 1),
            (524, 524, 1),
            (802, 802, 1),
            (803, 803, 1),
            (1142, 1142, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 630,
    label = "Cs-Br1sCl1sCl1sF1s_709",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
5   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (197, 197, 1),
            (211, 211, 1),
            (296, 296, 1),
            (331, 331, 1),
            (387, 387, 1),
            (493, 493, 1),
            (755, 755, 1),
            (795, 795, 1),
            (1135, 1135, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 631,
    label = "Cs-Br1sBr1sF1sF1s_711",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
5   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (159, 159, 1),
            (277, 277, 1),
            (324, 324, 1),
            (329, 329, 1),
            (362, 362, 1),
            (630, 630, 1),
            (784, 784, 1),
            (1117, 1117, 1),
            (1202, 1202, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 632,
    label = "Cs-Cl1sF1sF1sF1s_713",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
5   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (340, 340, 1),
            (340, 340, 1),
            (456, 456, 1),
            (560, 560, 1),
            (560, 560, 1),
            (780, 780, 1),
            (1086, 1086, 1),
            (1254, 1254, 1),
            (1254, 1254, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 633,
    label = "Cs-Br1sBr1sCl1sF1s_732",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
5   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (156, 156, 1),
            (191, 191, 1),
            (260, 260, 1),
            (306, 306, 1),
            (339, 339, 1),
            (457, 457, 1),
            (719, 719, 1),
            (771, 771, 1),
            (1129, 1129, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 634,
    label = "Cs-Br1sBr1sBr1sCl1s_733",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
5   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (138, 138, 1),
            (138, 138, 1),
            (207, 207, 1),
            (213, 213, 1),
            (213, 213, 1),
            (326, 326, 1),
            (652, 652, 1),
            (652, 652, 1),
            (725, 725, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 635,
    label = "Cs-Br1sCl1sF1sF1s_738",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
5   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (208, 208, 1),
            (290, 290, 1),
            (326, 326, 1),
            (402, 402, 1),
            (432, 432, 1),
            (647, 647, 1),
            (824, 824, 1),
            (1122, 1122, 1),
            (1210, 1210, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 636,
    label = "Cs-halhalHH_193",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (531, 531, 1),
            (1130, 1130, 1),
            (1136, 1136, 1),
            (1194, 1194, 1),
            (1273, 1273, 1),
            (1488, 1488, 1),
            (1538, 1538, 1),
            (3014, 3014, 1),
            (3074, 3074, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 637,
    label = "Cs-F1sF1sHH_193",
    group = 
"""
1 * Cs  u0 {2,S} {3,S} {4,S} {5,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   H   u0 {1,S}
5   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (531, 531, 1),
            (1130, 1130, 1),
            (1136, 1136, 1),
            (1194, 1194, 1),
            (1273, 1273, 1),
            (1488, 1488, 1),
            (1538, 1538, 1),
            (3014, 3014, 1),
            (3074, 3074, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 638,
    label = "Cs-Br1sBr1sHH_305",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (168, 168, 1),
            (574, 574, 1),
            (629, 629, 1),
            (815, 815, 1),
            (1109, 1109, 1),
            (1215, 1215, 1),
            (1431, 1431, 1),
            (3137, 3137, 1),
            (3228, 3228, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 639,
    label = "Cs-Cl1sCl1sHH_510",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (278, 278, 1),
            (704, 704, 1),
            (730, 730, 1),
            (896, 896, 1),
            (1162, 1162, 1),
            (1281, 1281, 1),
            (1455, 1455, 1),
            (3120, 3120, 1),
            (3202, 3202, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 640,
    label = "Cs-Br1sCl1sHH_688",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (222, 222, 1),
            (596, 596, 1),
            (725, 725, 1),
            (851, 851, 1),
            (1139, 1139, 1),
            (1246, 1246, 1),
            (1444, 1444, 1),
            (3128, 3128, 1),
            (3216, 3216, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 641,
    label = "Cs-Cl1sF1sHH_701",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (376, 376, 1),
            (724, 724, 1),
            (1006, 1006, 1),
            (1127, 1127, 1),
            (1255, 1255, 1),
            (1373, 1373, 1),
            (1510, 1510, 1),
            (3071, 3071, 1),
            (3147, 3147, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 642,
    label = "Cs-Br1sF1sHH_708",
    group = 
"""
1 * Cs   u0 {2,S} {3,S} {4,S} {5,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   H    u0 {1,S}
5   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (306, 306, 1),
            (619, 619, 1),
            (941, 941, 1),
            (1128, 1128, 1),
            (1248, 1248, 1),
            (1332, 1332, 1),
            (1505, 1505, 1),
            (3081, 3081, 1),
            (3164, 3164, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 643,
    label = "C2s-halhal_327",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (192, 192, 1),
            (594, 594, 1),
            (627, 627, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 644,
    label = "C2s-Br1sBr1s_327",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (192, 192, 1),
            (594, 594, 1),
            (627, 627, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 645,
    label = "C2s-Cl1sCl1s_523",
    group = 
"""
1 * C2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (328, 328, 1),
            (719, 719, 1),
            (727, 727, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 646,
    label = "C2sc-halCsCsc_739",
    group = 
"""
1 * C2sc u0 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Csc  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (159, 159, 1),
            (285, 285, 1),
            (287, 287, 1),
            (345, 345, 1),
            (409, 409, 1),
            (508, 508, 1),
            (590, 590, 1),
            (1153, 1153, 1),
            (1281, 1281, 1),
            (1717, 1717, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 647,
    label = "C2sc-Cl1sCsCsc_739",
    group = 
"""
1 * C2sc u0 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Csc  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (159, 159, 1),
            (285, 285, 1),
            (287, 287, 1),
            (345, 345, 1),
            (409, 409, 1),
            (508, 508, 1),
            (590, 590, 1),
            (1153, 1153, 1),
            (1281, 1281, 1),
            (1717, 1717, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 648,
    label = "Csc-halO2sC2sc_740",
    group = 
"""
1 * Csc  u0 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   O2s  u1 {1,S}
4   C2sc ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (109, 209, 1),
            (235, 335, 1),
            (237, 337, 1),
            (295, 395, 1),
            (359, 459, 1),
            (458, 558, 1),
            (540, 640, 1),
            (1103, 1203, 1),
            (1231, 1331, 1),
            (1667, 1767, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 649,
    label = "Csc-Br1sO2sC2sc_740",
    group = 
"""
1 * Csc  u0 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   O2s  u1 {1,S}
4   C2sc ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (109, 209, 1),
            (235, 335, 1),
            (237, 337, 1),
            (295, 395, 1),
            (359, 459, 1),
            (458, 558, 1),
            (540, 640, 1),
            (1103, 1203, 1),
            (1231, 1331, 1),
            (1667, 1767, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 650,
    label = "O_R0",
    group = 
"""
1 * O u0
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 651,
    label = "Alcohol",
    group = 
"""
1 * O        u0 {2,S} {3,S}
2   C        ux {1,S}
3   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3580, 3650, 1),
            (1210, 1345, 1),
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """Oxygen with a single bond to hydrogen and another single bond to carbon""",
    longDesc = 
"""
(3580, 3650, 1),	#O-H stretch
(1210, 1345, 1),	#R-O-H bend
(900, 1100, 1),
""",
)

entry(
    index = 652,
    label = "O2s-halCs_37",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (504, 610, 1),
            (1067, 1155, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 653,
    label = "O2s-F1sCs_37",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (504, 610, 1),
            (1067, 1155, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 654,
    label = "O2s-Br1sCs_221",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (185, 243, 1),
            (1066, 1156, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 655,
    label = "O2s-Br1sCs_727",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (145, 245, 1),
            (1013, 1113, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 656,
    label = "O2s-Cl1sCs_388",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (193, 287, 1),
            (1037, 1163, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 657,
    label = "O2s-Cl1sCs_667",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Cs   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (228, 232, 1),
            (1036, 1152, 1),
            (1066, 1096, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 658,
    label = "O2s-halCd_80",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (175, 287, 1),
            (726, 856, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 659,
    label = "O2s-F1sCd_80",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   Cd  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (175, 287, 1),
            (726, 856, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 660,
    label = "O2s-Br1sCd_242",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (140, 204, 1),
            (588, 686, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 661,
    label = "O2s-Cl1sCd_382",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (180, 254, 1),
            (1100, 1234, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 662,
    label = "O2s-Cl1sCd_517",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Cd   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1042, 1142, 1),
            (1186, 1286, 1),
            (3074, 3174, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 663,
    label = "O2s-halCO_102",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (947, 1033, 1),
            (1057, 1169, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 664,
    label = "O2s-F1sCO_102",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (947, 1033, 1),
            (1057, 1169, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 665,
    label = "O2s-Br1sCO_306",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (165, 225, 1),
            (1099, 1203, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 666,
    label = "O2s-Br1sCO_328",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (229, 229, 1),
            (744, 744, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 667,
    label = "O2s-Cl1sCO_478",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (187, 285, 1),
            (1041, 1193, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 668,
    label = "O2s-Cl1sCO_509",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   CO   u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (274, 274, 1),
            (783, 783, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 669,
    label = "O2s-halCt_144",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (327, 421, 1),
            (408, 552, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 670,
    label = "O2s-F1sCt_144",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (327, 421, 1),
            (408, 552, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 671,
    label = "O2s-Br1sCt_346",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (149, 307, 1),
            (286, 400, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 672,
    label = "O2s-Cl1sCt_448",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (241, 393, 1),
            (340, 366, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 673,
    label = "Ether",
    group = 
"""
1 * O u0 {2,S} {3,S}
2   C u2 {1,S}
3   C u2 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (350, 500, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """oxygen with two single carbon bonds""",
    longDesc = 
"""
(350, 500, 1),	#C-O-C scissor
""",
)

entry(
    index = 674,
    label = "COOH",
    group = 
"""
1 * O        u0 {2,S} {3,S}
2   O        u0 {1,S} {4,S}
3   C        ux {1,S}
4   [H,Val7] u0 {2,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3580, 3650, 1),
            (1300, 1320, 1),
            (350, 425, 1),
            (825, 875, 1),
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """Peroxide""",
    longDesc = 
"""
(3580, 3650, 1),	#O-H stretch
(1300, 1320, 1),	#O-O-H bend
(350, 425, 1),		#C-O-O scissor
(825, 875, 1),		#O-O stretch
(900, 1100, 1),
""",
)

entry(
    index = 675,
    label = "COOC",
    group = 
"""
1 * O u0 {2,S} {3,S}
2   O u0 {1,S} {4,S}
3   C ux {1,S}
4   C ux {2,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (350, 500, 1),
            (795, 815, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """peroxide""",
    longDesc = 
"""
(350, 500, 1),	#C-O-O scissor
(795, 815, 1),	#O-O stretch
""",
)

entry(
    index = 676,
    label = "Peroxy",
    group = 
"""
1 * O u0 {2,S} {3,S}
2   C ux {1,S}
3   O u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (470, 515, 1),
            (1100, 1170, 1),
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """Oxygen single bonded to one carbon and one oxygen""",
    longDesc = 
"""
(470, 515, 1),	#C-O-O scissor
(1100, 1170, 1),#O-O stretch
(900, 1100, 1)
""",
)

entry(
    index = 677,
    label = "O2s-halO2s_46",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (206, 348, 1),
            (496, 614, 1),
            (551, 713, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 678,
    label = "O2s-F1sO2s_46",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (206, 348, 1),
            (496, 614, 1),
            (551, 713, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 679,
    label = "O2s-F1sO2s_187",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   O2s u1 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (449, 449, 1),
            (679, 679, 1),
            (1504, 1504, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 680,
    label = "O2s-Br1sO2s_230",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (204, 332, 1),
            (206, 268, 1),
            (467, 577, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 681,
    label = "O2s-Cl1sO2s_437",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (166, 278, 1),
            (347, 539, 1),
            (503, 677, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 682,
    label = "O2s-halH_132",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1005, 1005, 1),
            (1417, 1417, 1),
            (3730, 3730, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 683,
    label = "O2s-F1sH_132",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1005, 1005, 1),
            (1417, 1417, 1),
            (3730, 3730, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 684,
    label = "O2s-Br1sH_337",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (636, 636, 1),
            (1200, 1200, 1),
            (3777, 3777, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 685,
    label = "O2s-Cl1sH_504",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (738, 738, 1),
            (1277, 1277, 1),
            (3767, 3767, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 686,
    label = "O2s-halhal_196",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (486, 486, 1),
            (915, 915, 1),
            (1034, 1034, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 687,
    label = "O2s-F1sF1s_196",
    group = 
"""
1 * O2s u0 {2,S} {3,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (486, 486, 1),
            (915, 915, 1),
            (1034, 1034, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 688,
    label = "O2s-Br1sBr1s_359",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (180, 180, 1),
            (536, 536, 1),
            (605, 605, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 689,
    label = "O2s-Cl1sCl1s_492",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (294, 294, 1),
            (656, 656, 1),
            (658, 658, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 690,
    label = "O2s-Br1sF1s_702",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (307, 307, 1),
            (623, 623, 1),
            (907, 907, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 691,
    label = "O2s-Cl1sF1s_707",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (377, 377, 1),
            (701, 701, 1),
            (907, 907, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 692,
    label = "O2s-Br1sCl1s_717",
    group = 
"""
1 * O2s  u0 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (236, 236, 1),
            (567, 567, 1),
            (666, 666, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 693,
    label = "N_R0",
    group = 
"""
1 * N u0
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 694,
    label = "Amine_pri",
    group = 
"""
1 * N        u0 {2,S} {3,S} {4,S}
2   C        u0 {1,S}
3   [H,Val7] u0 {1,S}
4   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3330, 3550, 1),
            (3250, 3450, 1),
            (1580, 1650, 1),
            (1145, 1295, 1),
            (650, 895, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""
(3330, 3550, 1), # asymmetric NH2 stretch, primary amines
(3250, 3450, 1), # symmetric NH2 stretch, primary amines
(1580, 1650, 1), # br. scissor vibration, saturated primary amines
(1145, 1295, 1), # NH2 rocking/twisting vibration, saturated primary amines
(650, 895, 1), # N-H bending out of plane, saturated primary amines
""",
)

entry(
    index = 695,
    label = "Amide_pri",
    group = 
"""
1 * N        u0 {2,S} {5,S} {6,S}
2   CO       u0 {1,S} {3,S} {4,D}
3   C        u0 {2,S}
4   O        u0 {2,D}
5   [H,Val7] u0 {1,S}
6   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3480, 3540, 1),
            (3380, 3420, 1),
            (1670, 1690, 1),
            (1590, 1620, 1),
            (1400, 1420, 1),
            (1140, 1160, 1),
            (600, 750, 1),
            (550, 600, 1),
            (450, 500, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""
(3480, 3540, 1), # asymmetric N-H stretch, (free) primary amides
(3380, 3420, 1), # symmetric N-H stretch, (free) primary amides
(1670, 1690, 1), # C=O stretch, known as amide I band, primary amides (dilute solution)
(1590, 1620, 1), # , primary amides (dilute solution)
(1400, 1420, 1), # C-N stretch, known as amide III band, primary amides
(1140, 1160, 1), # NH2 in-plane rocking vibration, primary amides
(600, 750, 1),   # br. NH2 deformation vibration, primary amides
(550, 600, 1),   # N-C=O deformation vibration, primary amides
(450, 500, 1),   # C-C=O deformation vibration, primary amides
""",
)

entry(
    index = 696,
    label = "Amine_sec",
    group = 
"""
1 * N        u0 {2,S} {3,S} {4,S}
2   C        u0 {1,S}
3   C        u0 {1,S}
4   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3400, 3450, 1),
            (1490, 1580, 1),
            (700, 750, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""
(3400, 3450, 1), # , secondary amines
(1490, 1580, 1), # , secondary amines
(700, 750, 1), # br. N-H wagging vibration, secondary amines
""",
)

entry(
    index = 697,
    label = "Amide_sec",
    group = 
"""
1 * N        u0 {2,S} {5,S} {6,S}
2   CO       u0 {1,S} {3,S} {4,D}
3   C        u0 {2,S}
4   O        u0 {2,D}
5   C        u0 {1,S}
6   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3420, 3460, 1),
            (1510, 1550, 1),
            (1665, 1700, 1),
            (1200, 1305, 1),
            (620, 770, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""
(3420, 3460, 1), # N-H stretch, trans form (in dilute solution)
(1510, 1550, 1), # amide II band, trans form (in dilute solution)
(1665, 1700, 1), # C=O stretch, secondary amides (dilute solution)
(1200, 1305, 1), # amide III band, secondary amides (trans form)
(620, 770, 1),   # br. out-of-plane N-H, secondary amides (trans form)
""",
)

entry(
    index = 698,
    label = "Imide",
    group = 
"""
1 * N        u0 {2,S} {3,S} {6,S}
2   [H,Val7] u0 {1,S}
3   CO       u0 {1,S} {4,D} {5,S}
4   O        u0 {3,D}
5   R        u0 {3,S}
6   CO       u0 {1,S} {7,D} {8,S}
7   O        u0 {6,D}
8   R        u0 {6,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3200, 3280, 1),
            (1670, 1740, 1),
            (1500, 1510, 1),
            (1165, 1235, 1),
            (730, 740, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""
(3200, 3280, 1), # N-H stretch, Imides (solid phase)
(1670, 1740, 1), # C=O stretch, amide I band, Imides (solid phase)
(1500, 1510, 1), # br., amide II band, Imides (solid phase)
(1165, 1235, 1), # amide III band, Imides (solid phase)
(730, 740, 1),   # br. N-H wagging, amide II band, Imides (solid phase)
""",
)

entry(
    index = 699,
    label = "Amine_ter",
    group = 
"""
1 * N u0 {2,S} {3,S} {4,S}
2   C u0 {1,S}
3   C u0 {1,S}
4   C u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1020, 1250, 2),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 700,
    label = "Amide_ter",
    group = 
"""
1 * N  u0 {2,S} {5,S} {6,S}
2   CO u0 {1,S} {3,S} {4,D}
3   C  u0 {2,S}
4   O  u0 {2,D}
5   C  u0 {1,S}
6   C  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1630, 1670, 1),
            (700, 870, 1),
            (570, 620, 1),
            (440, 480, 1),
            (320, 390, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""
(1630, 1670, 1), # C=O stretch, tertiary amides (dilute solution or solid phase)
(700, 870, 1), # asymmetric CNC stretch, tertiary amides
(570, 620, 1), # , tertiary amides
(440, 480, 1), # , tertiary amides
(320, 390, 1), # , tertiary amides
""",
)

entry(
    index = 701,
    label = "Nitrile",
    group = 
"""
1 * N u0 {2,T}
2   C u0 {1,T} {3,S}
3   C ux {2,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (2230, 2260, 1),
            (340, 390, 1),
            (200, 160, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """N triple bonded to a carbon and single bonded to another carbon""",
    longDesc = 
"""
(2230, 2260, 1), # C#N stretching, saturated aliphatic nitriles
(340, 390, 1),   # C#N deformation, aliphatic nitriles
(200, 160, 1),   # C#N deformation, aliphatic nitriles
""",
)

entry(
    index = 702,
    label = "Nitroso",
    group = 
"""
1 * N        u0 {2,D} {3,S}
2   O        u0 {1,D}
3   R!H!Val7 ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1330, 1425, 1),
            (1320, 1345, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""
(1330, 1425, 1), # aliphatic compounds
(1320, 1345, 1), # aliphatic compounds
""",
)

entry(
    index = 703,
    label = "Nitro",
    group = 
"""
1 * N5dc     u0 {2,D} {3,S} {4,S}
2   O        u0 {1,D}
3   O        u0 {1,S}
4   R!H!Val7 ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1360, 1385, 1),
            (915, 1000, 1),
            (850, 920, 1),
            (605, 655, 1),
            (470, 560, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """""",
    longDesc = 
"""
(1545, 1555, 1), # asymmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
(1360, 1385, 1), # symmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
(915, 1000, 1),  # C-N stretch trans form, saturated primary and secondary aliphatic nitro compounds
(850, 920, 1),  # br. C-N stretch gauche form, saturated primary and secondary aliphatic nitro compounds
(605, 655, 1),  # NO2 deformation vibration, saturated primary and secondary aliphatic nitro compounds
(470, 560, 1),  # NO2 rocking vibration, saturated primary and secondary aliphatic nitro compounds
""",
)

entry(
    index = 704,
    label = "Nitrates",
    group = 
"""
1 * N5dc u0 {2,D} {3,S} {4,S}
2   O    u0 {1,D}
3   O    u0 {1,S}
4   O    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1615, 1660, 1),
            (1250, 1300, 1),
            (840, 870, 1),
            (745, 765, 1),
            (680, 720, 1),
            (560, 610, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """""",
    longDesc = 
"""
(1615, 1660, 1), # asymmetric NO2 stretch, Nitrates, -ONO2
(1250, 1300, 1), # symmetric NO2 stretch, Nitrates, -ONO2
(840, 870, 1),   # br.N-O stretch, Nitrates, -ONO2
(745, 765, 1),   # NO2 out-of-plane deformation vibration, Nitrates, -ONO2
(680, 720, 1),   # NO2 deformation vibration, Nitrates, -ONO2
(560, 610, 1),   # NO2 in-plane deformation vibration, Nitrates, -ONO2
""",
)

entry(
    index = 705,
    label = "Nitrites",
    group = 
"""
1 * N u0 {2,D} {3,S}
2   O u0 {1,D}
3   O u0 {1,S} {4,S}
4   R u0 {3,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3220, 3360, 1),
            (1650, 1680, 1),
            (750, 815, 1),
            (565, 625, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""
(3220, 3360, 1), # Overtones of N=O stretch, nitrite compounds
(1650, 1680, 1), # N=O stretch, nitrites, trans form
(750, 815, 1),   # N-O stretch trans form, saturated primary and secondary aliphatic nitro compounds
(565, 625, 1),   # O-N=O deformation vibration, saturated primary and secondary aliphatic nitro compounds
""",
)

entry(
    index = 706,
    label = "R!H!Val7x1",
    group = 
"""
1 * R!H!Val7 u1
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 707,
    label = "C_R1",
    group = 
"""
1 * C u1
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 708,
    label = "RsCH2r",
    group = 
"""
1 * C        u1 {2,S} {3,S} {4,S}
2   R!H!Val7 ux {1,S}
3   [H,Val7] u0 {1,S}
4   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3000, 3100, 2),
            (415, 465, 1),
            (780, 850, 1),
            (1435, 1475, 1),
            (900, 1100, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """Carbon radical with one single bond""",
    longDesc = 
"""
(3000, 3100, 2),	#C-H stretch
(415, 465, 1),		#R-C-H swing
(780, 850, 1),		#R-C-H rock
(1435, 1475, 1),	#R-C-H scissor
(900, 1100, 1),
""",
)

entry(
    index = 709,
    label = "Cs-halCsH_38",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (262, 406, 1),
            (528, 622, 1),
            (1148, 1246, 1),
            (1368, 1480, 1),
            (3164, 3240, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 710,
    label = "Cs-F1sCsH_38",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (262, 406, 1),
            (528, 622, 1),
            (1148, 1246, 1),
            (1368, 1480, 1),
            (3164, 3240, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 711,
    label = "Cs-Br1sCsH_240",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (191, 287, 1),
            (432, 578, 1),
            (1050, 1182, 1),
            (1128, 1286, 1),
            (3187, 3273, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 712,
    label = "Cs-Cl1sCsH_366",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (179, 277, 1),
            (483, 601, 1),
            (1065, 1201, 1),
            (1150, 1310, 1),
            (3206, 3266, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 713,
    label = "Cs-halhalCs_43",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (146, 234, 1),
            (414, 562, 1),
            (504, 606, 1),
            (1176, 1296, 1),
            (1354, 1460, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 714,
    label = "Cs-F1sF1sCs_43",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (146, 234, 1),
            (414, 562, 1),
            (504, 606, 1),
            (1176, 1296, 1),
            (1354, 1460, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 715,
    label = "Cs-Br1sBr1sCs_245",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (110, 192, 1),
            (157, 203, 1),
            (204, 340, 1),
            (427, 559, 1),
            (1020, 1140, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 716,
    label = "Cs-Cl1sCl1sCs_392",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (129, 217, 1),
            (242, 326, 1),
            (368, 506, 1),
            (578, 702, 1),
            (1001, 1155, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 717,
    label = "Cs-Cl1sF1sCs_554",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (323, 457, 1),
            (392, 584, 1),
            (472, 596, 1),
            (1062, 1200, 1),
            (1173, 1363, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 718,
    label = "Cs-Br1sF1sCs_577",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (70, 194, 1),
            (224, 364, 1),
            (400, 548, 1),
            (1027, 1179, 1),
            (1175, 1377, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 719,
    label = "Cs-Br1sCl1sCs_598",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (105, 301, 1),
            (107, 225, 1),
            (196, 272, 1),
            (480, 642, 1),
            (1012, 1160, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 720,
    label = "Cs-halCdH_60",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Cd   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (173, 295, 1),
            (515, 663, 1),
            (653, 819, 1),
            (693, 939, 1),
            (1188, 1292, 1),
            (3205, 3269, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 721,
    label = "Cs-F1sCdH_60",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   Cd  ux {1,S}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (173, 295, 1),
            (515, 663, 1),
            (653, 819, 1),
            (693, 939, 1),
            (1188, 1292, 1),
            (3205, 3269, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 722,
    label = "Cs-Br1sCdH_264",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cd   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (121, 221, 1),
            (531, 611, 1),
            (606, 714, 1),
            (652, 868, 1),
            (733, 855, 1),
            (3210, 3276, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 723,
    label = "Cs-Cl1sCdH_368",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cd   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (165, 261, 1),
            (556, 656, 1),
            (666, 798, 1),
            (756, 948, 1),
            (787, 883, 1),
            (3223, 3269, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 724,
    label = "Cs-halO2sH_66",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (505, 655, 1),
            (1117, 1193, 1),
            (1185, 1289, 1),
            (1311, 1435, 1),
            (3104, 3190, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 725,
    label = "Cs-F1sO2sH_66",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (505, 655, 1),
            (1117, 1193, 1),
            (1185, 1289, 1),
            (1311, 1435, 1),
            (3104, 3190, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 726,
    label = "Cs-Br1sO2sH_216",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (251, 337, 1),
            (548, 608, 1),
            (804, 894, 1),
            (1284, 1418, 1),
            (3166, 3224, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 727,
    label = "Cs-Cl1sO2sH_404",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (427, 591, 1),
            (616, 714, 1),
            (837, 951, 1),
            (1252, 1372, 1),
            (3161, 3221, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 728,
    label = "Cs-halhalO2s_83",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (444, 542, 1),
            (521, 679, 1),
            (613, 787, 1),
            (1100, 1188, 1),
            (1236, 1350, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 729,
    label = "Cs-F1sF1sO2s_83",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   O2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (444, 542, 1),
            (521, 679, 1),
            (613, 787, 1),
            (1100, 1188, 1),
            (1236, 1350, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 730,
    label = "Cs-Br1sBr1sO2s_262",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (145, 173, 1),
            (257, 367, 1),
            (355, 443, 1),
            (470, 602, 1),
            (760, 906, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 731,
    label = "Cs-Cl1sCl1sO2s_381",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (239, 303, 1),
            (374, 434, 1),
            (487, 579, 1),
            (541, 633, 1),
            (858, 930, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 732,
    label = "Cs-Cl1sF1sO2s_567",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (193, 331, 1),
            (377, 437, 1),
            (549, 639, 1),
            (627, 785, 1),
            (1198, 1294, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 733,
    label = "Cs-Br1sCl1sO2s_575",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (167, 239, 1),
            (335, 415, 1),
            (398, 514, 1),
            (523, 607, 1),
            (819, 929, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 734,
    label = "Cs-Br1sF1sO2s_590",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (206, 376, 1),
            (208, 308, 1),
            (498, 678, 1),
            (549, 619, 1),
            (1180, 1348, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 735,
    label = "Cs-halhalCd_101",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (124, 198, 1),
            (231, 363, 1),
            (414, 566, 1),
            (474, 694, 1),
            (695, 865, 1),
            (1255, 1461, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 736,
    label = "Cs-F1sF1sCd_101",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Cd  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (124, 198, 1),
            (231, 363, 1),
            (414, 566, 1),
            (474, 694, 1),
            (695, 865, 1),
            (1255, 1461, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 737,
    label = "Cs-Br1sBr1sCd_273",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (148, 234, 1),
            (151, 195, 1),
            (184, 318, 1),
            (267, 439, 1),
            (522, 632, 1),
            (752, 862, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 738,
    label = "Cs-Cl1sCl1sCd_400",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (95, 207, 1),
            (171, 297, 1),
            (235, 307, 1),
            (524, 656, 1),
            (647, 829, 1),
            (863, 977, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 739,
    label = "Cs-Br1sCl1sCd_545",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (76, 254, 1),
            (162, 244, 1),
            (187, 313, 1),
            (399, 603, 1),
            (497, 653, 1),
            (806, 946, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 740,
    label = "Cs-Cl1sF1sCd_566",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (144, 232, 1),
            (217, 363, 1),
            (358, 508, 1),
            (477, 633, 1),
            (677, 869, 1),
            (709, 855, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 741,
    label = "Cs-Br1sF1sCd_573",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (107, 201, 1),
            (241, 353, 1),
            (272, 412, 1),
            (440, 648, 1),
            (677, 861, 1),
            (772, 950, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 742,
    label = "Cs-halhalCO_117",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (142, 216, 1),
            (300, 392, 1),
            (739, 897, 1),
            (1373, 1439, 1),
            (1506, 1542, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 743,
    label = "Cs-F1sF1sCO_117",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (142, 216, 1),
            (300, 392, 1),
            (739, 897, 1),
            (1373, 1439, 1),
            (1506, 1542, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 744,
    label = "Cs-Br1sBr1sCO_288",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (154, 208, 1),
            (165, 169, 1),
            (292, 330, 1),
            (575, 649, 1),
            (1103, 1207, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 745,
    label = "Cs-Cl1sCl1sCO_442",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (170, 238, 1),
            (184, 336, 1),
            (270, 294, 1),
            (966, 1012, 1),
            (1170, 1308, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 746,
    label = "Cs-Cl1sF1sCO_587",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (191, 265, 1),
            (263, 419, 1),
            (505, 643, 1),
            (1090, 1292, 1),
            (1350, 1458, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 747,
    label = "Cs-Br1sCl1sCO_606",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (160, 208, 1),
            (203, 271, 1),
            (239, 401, 1),
            (932, 964, 1),
            (1064, 1274, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 748,
    label = "Cs-Br1sF1sCO_662",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (84, 290, 1),
            (208, 268, 1),
            (295, 339, 1),
            (1050, 1274, 1),
            (1336, 1446, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 749,
    label = "Cs-halhalCt_140",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (176, 236, 1),
            (217, 353, 1),
            (358, 414, 1),
            (511, 661, 1),
            (1261, 1401, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 750,
    label = "Cs-F1sF1sCt_140",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (176, 236, 1),
            (217, 353, 1),
            (358, 414, 1),
            (511, 661, 1),
            (1261, 1401, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 751,
    label = "Cs-Br1sBr1sCt_308",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (158, 210, 1),
            (159, 177, 1),
            (285, 387, 1),
            (306, 464, 1),
            (335, 405, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 752,
    label = "Cs-Cl1sCl1sCt_450",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (176, 218, 1),
            (233, 295, 1),
            (338, 412, 1),
            (370, 502, 1),
            (485, 525, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 753,
    label = "Cs-Cl1sF1sCt_610",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (166, 232, 1),
            (284, 334, 1),
            (304, 518, 1),
            (354, 402, 1),
            (1114, 1186, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 754,
    label = "Cs-Br1sCl1sCt_628",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (166, 198, 1),
            (186, 266, 1),
            (272, 406, 1),
            (327, 395, 1),
            (436, 436, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 755,
    label = "Cs-Br1sF1sCt_664",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (161, 177, 1),
            (251, 403, 1),
            (282, 508, 1),
            (285, 303, 1),
            (984, 1152, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 756,
    label = "Cs-halCOH_146",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   CO   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (169, 301, 1),
            (1168, 1262, 1),
            (1250, 1444, 1),
            (1469, 1503, 1),
            (3209, 3233, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 757,
    label = "Cs-F1sCOH_146",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   CO  ux {1,S}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (169, 301, 1),
            (1168, 1262, 1),
            (1250, 1444, 1),
            (1469, 1503, 1),
            (3209, 3233, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 758,
    label = "Cs-Br1sCOH_338",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   CO   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (137, 221, 1),
            (587, 671, 1),
            (1132, 1226, 1),
            (1151, 1277, 1),
            (3209, 3241, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 759,
    label = "Cs-Cl1sCOH_419",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   CO   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (132, 240, 1),
            (851, 909, 1),
            (1127, 1361, 1),
            (1225, 1391, 1),
            (3223, 3249, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 760,
    label = "Cs-halCtH_162",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Ct   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (233, 367, 1),
            (333, 515, 1),
            (1079, 1191, 1),
            (1228, 1350, 1),
            (3210, 3218, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 761,
    label = "Cs-F1sCtH_162",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   Ct  ux {1,S}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (233, 367, 1),
            (333, 515, 1),
            (1079, 1191, 1),
            (1228, 1350, 1),
            (3210, 3218, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 762,
    label = "Cs-Br1sCtH_324",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Ct   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (242, 368, 1),
            (292, 400, 1),
            (423, 445, 1),
            (1155, 1231, 1),
            (3228, 3232, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 763,
    label = "Cs-Cl1sCtH_446",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Ct   ux {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (294, 386, 1),
            (333, 473, 1),
            (482, 578, 1),
            (1182, 1272, 1),
            (3221, 3225, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 764,
    label = "RdCHr",
    group = 
"""
1 * C        u1 {2,D} {3,S}
2   R!H!Val7 ux {1,D}
3   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3115, 3125, 1),
            (620, 680, 1),
            (785, 800, 1),
            (1600, 1700, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """carbon radical with one single bond""",
    longDesc = 
"""
(3115, 3125, 1),	#C-H stretch
(620, 680, 1),		#CdC-H bend
(785, 800, 1),		#CdC-H bend
(1600, 1700, 1),
""",
)

entry(
    index = 765,
    label = "Cd-halCd_113",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Val7 u0 {1,S}
3   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (125, 209, 1),
            (569, 711, 1),
            (1121, 1259, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 766,
    label = "Cd-F1sCd_113",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   F1s u0 {1,S}
3   Cd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (125, 209, 1),
            (569, 711, 1),
            (1121, 1259, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 767,
    label = "Cd-Br1sCd_232",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Br1s u0 {1,S}
3   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (114, 190, 1),
            (218, 374, 1),
            (549, 657, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 768,
    label = "Cd-Cl1sCd_416",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Cl1s u0 {1,S}
3   Cd   ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (107, 189, 1),
            (599, 737, 1),
            (754, 908, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 769,
    label = "Cd-halCdd_151",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Val7 u0 {1,S}
3   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (40, 234, 1),
            (110, 304, 1),
            (757, 867, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 770,
    label = "Cd-F1sCdd_151",
    group = 
"""
1 * Cd  u1 {2,S} {3,D}
2   F1s u0 {1,S}
3   Cdd ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (40, 234, 1),
            (110, 304, 1),
            (757, 867, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 771,
    label = "Cd-Br1sCdd_283",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Br1s u0 {1,S}
3   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (92, 114, 1),
            (111, 227, 1),
            (257, 311, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 772,
    label = "Cd-Cl1sCdd_480",
    group = 
"""
1 * Cd   u1 {2,S} {3,D}
2   Cl1s u0 {1,S}
3   Cdd  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (71, 137, 1),
            (105, 235, 1),
            (276, 394, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 773,
    label = "CO-halO2d_198",
    group = 
"""
1 * CO   u1 {2,S} {3,D}
2   Val7 u0 {1,S}
3   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (636, 636, 1),
            (1085, 1085, 1),
            (1918, 1918, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 774,
    label = "CO-F1sO2d_198",
    group = 
"""
1 * CO  u1 {2,S} {3,D}
2   F1s u0 {1,S}
3   O2d ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (636, 636, 1),
            (1085, 1085, 1),
            (1918, 1918, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 775,
    label = "CO-Cl1sO2d_491",
    group = 
"""
1 * CO   u1 {2,S} {3,D}
2   Cl1s u0 {1,S}
3   O2d  ux {1,D}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (341, 341, 1),
            (585, 585, 1),
            (1957, 1957, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 776,
    label = "CtCr",
    group = 
"""
1 * C u1 {2,T}
2   C ux {1,T}
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 777,
    label = "RsCHrsR",
    group = 
"""
1 * C        u1 {2,S} {3,S} {4,S}
2   R!H!Val7 ux {1,S}
3   R!H!Val7 ux {1,S}
4   [H,Val7] u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (3000, 3050, 1),
            (390, 425, 1),
            (1340, 1360, 1),
            (335, 370, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = """carbon radical with two single bonds""",
    longDesc = 
"""
(3000, 3050, 1),	#C-H stretch
(390, 425, 1),		#R-C-H bend
(1340, 1360, 1),	#R-C-H bend
(335, 370, 1),		#R-C-R scissor
""",
)

entry(
    index = 778,
    label = "Cs-halCsCt_68",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (211, 315, 1),
            (293, 411, 1),
            (363, 497, 1),
            (1195, 1321, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 779,
    label = "Cs-F1sCsCt_68",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Ct  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (211, 315, 1),
            (293, 411, 1),
            (363, 497, 1),
            (1195, 1321, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 780,
    label = "Cs-Br1sCsCt_274",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (172, 260, 1),
            (241, 343, 1),
            (331, 469, 1),
            (416, 444, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 781,
    label = "Cs-Cl1sCsCt_449",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (233, 329, 1),
            (293, 375, 1),
            (310, 430, 1),
            (1042, 1154, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 782,
    label = "Cs-halCsCs_73",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (165, 259, 1),
            (333, 401, 1),
            (397, 493, 1),
            (1395, 1505, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 783,
    label = "Cs-F1sCsCs_73",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (165, 259, 1),
            (333, 401, 1),
            (397, 493, 1),
            (1395, 1505, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 784,
    label = "Cs-Br1sCsCs_223",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (138, 220, 1),
            (252, 298, 1),
            (364, 450, 1),
            (1407, 1529, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 785,
    label = "Cs-Cl1sCsCs_407",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (108, 190, 1),
            (278, 366, 1),
            (358, 456, 1),
            (1401, 1519, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 786,
    label = "Cs-halO2sCs_110",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (353, 437, 1),
            (368, 578, 1),
            (616, 798, 1),
            (1350, 1522, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 787,
    label = "Cs-F1sO2sCs_110",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   Cs  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (353, 437, 1),
            (368, 578, 1),
            (616, 798, 1),
            (1350, 1522, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 788,
    label = "Cs-Br1sO2sCs_257",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (160, 260, 1),
            (268, 324, 1),
            (444, 498, 1),
            (463, 577, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 789,
    label = "Cs-Cl1sO2sCs_441",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (313, 383, 1),
            (401, 485, 1),
            (460, 618, 1),
            (1412, 1542, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 790,
    label = "Cs-halCsCd_112",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (310, 382, 1),
            (613, 705, 1),
            (770, 864, 1),
            (1249, 1319, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 791,
    label = "Cs-F1sCsCd_112",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   Cd  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (310, 382, 1),
            (613, 705, 1),
            (770, 864, 1),
            (1249, 1319, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 792,
    label = "Cs-Cl1sCsCd_501",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (306, 360, 1),
            (346, 426, 1),
            (1427, 1473, 1),
            (1467, 1487, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 793,
    label = "Cs-Br1sCsCd_728",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   Cd   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (308, 408, 1),
            (399, 499, 1),
            (1110, 1210, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 794,
    label = "Cs-halCsCO_115",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (196, 272, 1),
            (315, 379, 1),
            (1242, 1390, 1),
            (1461, 1467, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 795,
    label = "Cs-F1sCsCO_115",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   Cs  ux {1,S}
4   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (196, 272, 1),
            (315, 379, 1),
            (1242, 1390, 1),
            (1461, 1467, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 796,
    label = "Cs-Br1sCsCO_310",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (179, 253, 1),
            (265, 365, 1),
            (289, 469, 1),
            (1234, 1300, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 797,
    label = "Cs-Cl1sCsCO_481",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cs   ux {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (82, 230, 1),
            (191, 277, 1),
            (320, 388, 1),
            (1456, 1476, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 798,
    label = "Cs-halO2sO2s_142",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (428, 536, 1),
            (497, 675, 1),
            (664, 858, 1),
            (1354, 1468, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 799,
    label = "Cs-F1sO2sO2s_142",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   O2s ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (428, 536, 1),
            (497, 675, 1),
            (664, 858, 1),
            (1354, 1468, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 800,
    label = "Cs-Br1sO2sO2s_343",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (208, 248, 1),
            (274, 330, 1),
            (567, 587, 1),
            (568, 634, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 801,
    label = "Cs-Cl1sO2sO2s_434",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   O2s  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (310, 380, 1),
            (345, 439, 1),
            (561, 633, 1),
            (610, 678, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 802,
    label = "Cs-halO2sCO_148",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   O2s  ux {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (253, 307, 1),
            (474, 528, 1),
            (1484, 1504, 1),
            (1502, 1560, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 803,
    label = "Cs-F1sO2sCO_148",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   O2s ux {1,S}
4   CO  ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (253, 307, 1),
            (474, 528, 1),
            (1484, 1504, 1),
            (1502, 1560, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 804,
    label = "Cs-Br1sO2sCO_321",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   O2s  ux {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (122, 220, 1),
            (325, 345, 1),
            (384, 406, 1),
            (1435, 1475, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 805,
    label = "Cs-Cl1sO2sCO_514",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   O2s  ux {1,S}
4   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (189, 263, 1),
            (355, 367, 1),
            (467, 515, 1),
            (1456, 1488, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 806,
    label = "OdCrsR",
    group = 
"""
1 * C        u1 {2,D} {3,S}
2   O        u0 {1,D}
3   R!H!Val7 ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1850, 1860, 1),
            (440, 470, 1),
            (900, 1000, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """carbon radical with one oxygen double bond and one single bond""",
    longDesc = 
"""
(1850, 1860, 1),	#OdC stretch
(440, 470, 1),		#OdC-R bend
(900, 1000, 1),
""",
)

entry(
    index = 807,
    label = "CdCrsR",
    group = 
"""
1 * C        u1 {2,D} {3,S}
2   C        ux {1,D}
3   R!H!Val7 ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1670, 1700, 1),
            (300, 440, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """carbon radical with one carbon double bond and one single bond""",
    longDesc = 
"""
(1670, 1700, 1),	#CdC stretch
(300, 440, 1),		#CdC-R bend
""",
)

entry(
    index = 808,
    label = "RsCrsR2",
    group = 
"""
1 * C        u1 {2,S} {3,S} {4,S}
2   R!H!Val7 ux {1,S}
3   R!H!Val7 ux {1,S}
4   R!H!Val7 ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (360, 370, 2),
            (300, 400, 1),
        ],
        symmetry = 6,
    ),
    shortDesc = """carbon radical with three single bonds""",
    longDesc = 
"""
(360, 370, 2),	#C-C-C scissor
(300, 400, 1),	#Umbrella
""",
)

entry(
    index = 809,
    label = "Cs-halhalH_119",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (549, 549, 1),
            (1005, 1005, 1),
            (1195, 1195, 1),
            (1212, 1212, 1),
            (1359, 1359, 1),
            (3085, 3085, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 810,
    label = "Cs-F1sF1sH_119",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (549, 549, 1),
            (1005, 1005, 1),
            (1195, 1195, 1),
            (1212, 1212, 1),
            (1359, 1359, 1),
            (3085, 3085, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 811,
    label = "Cs-Br1sBr1sH_312",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (182, 182, 1),
            (431, 431, 1),
            (620, 620, 1),
            (760, 760, 1),
            (1176, 1176, 1),
            (3217, 3217, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 812,
    label = "Cs-Cl1sCl1sH_490",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (300, 300, 1),
            (471, 471, 1),
            (752, 752, 1),
            (875, 875, 1),
            (1225, 1225, 1),
            (3221, 3221, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 813,
    label = "Cs-Cl1sF1sH_602",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (402, 402, 1),
            (715, 715, 1),
            (848, 848, 1),
            (1208, 1208, 1),
            (1304, 1304, 1),
            (3155, 3155, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 814,
    label = "Cs-Br1sCl1sH_718",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (241, 241, 1),
            (449, 449, 1),
            (664, 664, 1),
            (843, 843, 1),
            (1202, 1202, 1),
            (3218, 3218, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 815,
    label = "Cs-Br1sF1sH_737",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (330, 330, 1),
            (637, 637, 1),
            (790, 790, 1),
            (1208, 1208, 1),
            (1288, 1288, 1),
            (3147, 3147, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 816,
    label = "Cs-halHH_166",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (576, 576, 1),
            (1180, 1180, 1),
            (1217, 1217, 1),
            (1485, 1485, 1),
            (3118, 3118, 1),
            (3268, 3268, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 817,
    label = "Cs-F1sHH_166",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   H   u0 {1,S}
4   H   u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (576, 576, 1),
            (1180, 1180, 1),
            (1217, 1217, 1),
            (1485, 1485, 1),
            (3118, 3118, 1),
            (3268, 3268, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 818,
    label = "Cs-Br1sHH_357",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (192, 192, 1),
            (698, 698, 1),
            (927, 927, 1),
            (1379, 1379, 1),
            (3177, 3177, 1),
            (3336, 3336, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 819,
    label = "Cs-Cl1sHH_479",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   H    u0 {1,S}
4   H    u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (71, 71, 1),
            (833, 833, 1),
            (988, 988, 1),
            (1405, 1405, 1),
            (3177, 3177, 1),
            (3333, 3333, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 820,
    label = "Cs-halhalhal_189",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Val7 u0 {1,S}
3   Val7 u0 {1,S}
4   Val7 u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (504, 504, 1),
            (504, 504, 1),
            (700, 700, 1),
            (1092, 1092, 1),
            (1279, 1279, 1),
            (1279, 1279, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 821,
    label = "Cs-F1sF1sF1s_189",
    group = 
"""
1 * Cs  u1 {2,S} {3,S} {4,S}
2   F1s u0 {1,S}
3   F1s u0 {1,S}
4   F1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (504, 504, 1),
            (504, 504, 1),
            (700, 700, 1),
            (1092, 1092, 1),
            (1279, 1279, 1),
            (1279, 1279, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 822,
    label = "Cs-Br1sBr1sBr1s_323",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Br1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (157, 157, 1),
            (157, 157, 1),
            (238, 238, 1),
            (313, 313, 1),
            (753, 753, 1),
            (754, 754, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 823,
    label = "Cs-Cl1sCl1sCl1s_456",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (269, 269, 1),
            (269, 269, 1),
            (326, 326, 1),
            (481, 481, 1),
            (874, 874, 1),
            (875, 875, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 824,
    label = "Cs-Br1sCl1sF1s_654",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (222, 222, 1),
            (322, 322, 1),
            (432, 432, 1),
            (524, 524, 1),
            (837, 837, 1),
            (1203, 1203, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 825,
    label = "Cs-Br1sBr1sF1s_678",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (168, 168, 1),
            (306, 306, 1),
            (370, 370, 1),
            (475, 475, 1),
            (776, 776, 1),
            (1197, 1197, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 826,
    label = "Cs-Br1sF1sF1s_683",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (302, 302, 1),
            (314, 314, 1),
            (582, 582, 1),
            (664, 664, 1),
            (1174, 1174, 1),
            (1255, 1255, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 827,
    label = "Cs-Br1sBr1sCl1s_706",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Br1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (172, 172, 1),
            (207, 207, 1),
            (277, 277, 1),
            (362, 362, 1),
            (762, 762, 1),
            (838, 838, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 828,
    label = "Cs-Cl1sF1sF1s_719",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   F1s  u0 {1,S}
4   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (356, 356, 1),
            (411, 411, 1),
            (598, 598, 1),
            (736, 736, 1),
            (1178, 1178, 1),
            (1264, 1264, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 829,
    label = "Cs-Cl1sCl1sF1s_730",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Cl1s u0 {1,S}
3   Cl1s u0 {1,S}
4   F1s  u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (275, 275, 1),
            (376, 376, 1),
            (459, 459, 1),
            (585, 585, 1),
            (879, 879, 1),
            (1210, 1210, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 830,
    label = "Cs-Br1sCl1sCl1s_731",
    group = 
"""
1 * Cs   u1 {2,S} {3,S} {4,S}
2   Br1s u0 {1,S}
3   Cl1s u0 {1,S}
4   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (220, 220, 1),
            (231, 231, 1),
            (306, 306, 1),
            (420, 420, 1),
            (813, 813, 1),
            (867, 867, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 831,
    label = "O_R1",
    group = 
"""
1 * O u1
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 832,
    label = "Oxy",
    group = 
"""
1 * O u1 {2,S}
2   C ux {1,S}
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 833,
    label = "O2s-hal_167",
    group = 
"""
1 * O2s  u1 {2,S}
2   Val7 u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1151, 1151, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 834,
    label = "O2s-F1s_167",
    group = 
"""
1 * O2s u1 {2,S}
2   F1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (1151, 1151, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 835,
    label = "O2s-Br1s_352",
    group = 
"""
1 * O2s  u1 {2,S}
2   Br1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (729, 729, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 836,
    label = "O2s-Cl1s_494",
    group = 
"""
1 * O2s  u1 {2,S}
2   Cl1s u0 {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (845, 845, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 837,
    label = "R!H!Val7x2_trip",
    group = 
"""
1 * R!H!Val7 u2
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 838,
    label = "C_R2",
    group = 
"""
1 * C u2
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 839,
    label = "RsCHrr",
    group = 
"""
1 * C        u2 {2,S} {3,S}
2   R!H!Val7 ux {1,S}
3   [H,Val7] u0 {1,S}
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 840,
    label = "Cs-halCt_331",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (151, 151, 1),
            (403, 403, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 841,
    label = "Cs-Br1sCt_331",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (151, 151, 1),
            (403, 403, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 842,
    label = "Cs-Cl1sCt_506",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   Ct   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (169, 169, 1),
            (397, 397, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 843,
    label = "Cs-halCO_336",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   Val7 u0 {1,S}
3   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (146, 180, 1),
            (1117, 1217, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 844,
    label = "Cs-Br1sCO_336",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   Br1s u0 {1,S}
3   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (146, 180, 1),
            (1117, 1217, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 845,
    label = "Cs-Cl1sCO_424",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   Cl1s u0 {1,S}
3   CO   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (189, 197, 1),
            (1169, 1241, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 846,
    label = "Cs-halCs_354",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   Val7 u0 {1,S}
3   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (90, 90, 1),
            (150, 150, 1),
            (200, 300, 1),
            (247, 247, 1),
            (273, 373, 1),
            (327, 427, 1),
            (381, 481, 1),
            (383, 483, 1),
            (1015, 1115, 1),
            (1224, 1324, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 847,
    label = "Cs-Br1sCs_354",
    group = 
"""
1 * Cs   u2 {2,S} {3,S}
2   Br1s u0 {1,S}
3   Cs   ux {1,S}
""",
    statmech = GroupFrequencies(
        frequencies = [
            (90, 90, 1),
            (150, 150, 1),
            (200, 300, 1),
            (247, 247, 1),
            (273, 373, 1),
            (327, 427, 1),
            (381, 481, 1),
            (383, 483, 1),
            (1015, 1115, 1),
            (1224, 1324, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 848,
    label = "RdCrr",
    group = 
"""
1 * C        u2 {2,D}
2   R!H!Val7 u2 {1,D}
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 849,
    label = "RsCrrsR",
    group = 
"""
1 * C        u2 {2,S} {3,S}
2   R!H!Val7 ux {1,S}
3   R!H!Val7 ux {1,S}
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

entry(
    index = 850,
    label = "R!H!Val7x3_quart",
    group = 
"""
1 * R!H!Val7 u3
""",
    statmech = None,
    shortDesc = """""",
    longDesc = 
"""

""",
)

tree(
"""
L1: R!H!Val7
    L2: R!H!Val7x0
        L3: C_R0
            L4: RsCH3
                L5: Cs-halhalhalCs_42
                    L6: Cs-F1sF1sF1sCs_42
                        L7: Cs-F1sF1sF1sCs_86
                    L6: Cs-Br1sBr1sBr1sCs_236
                        L7: Cs-Br1sBr1sBr1sCs_284
                    L6: Cs-Cl1sCl1sCl1sCs_377
                        L7: Cs-Cl1sCl1sCl1sCs_396
                    L6: Cs-Br1sF1sF1sCs_530
                        L7: Cs-Br1sF1sF1sCs_599
                    L6: Cs-Br1sCl1sCl1sCs_546
                        L7: Cs-Br1sCl1sCl1sCs_601
                    L6: Cs-Br1sCl1sF1sCs_580
                        L7: Cs-Br1sCl1sF1sCs_569
                    L6: Cs-Br1sBr1sF1sCs_586
                        L7: Cs-Br1sBr1sF1sCs_561
                    L6: Cs-Br1sBr1sCl1sCs_588
                        L7: Cs-Br1sBr1sCl1sCs_611
                    L6: Cs-Cl1sF1sF1sCs_603
                        L7: Cs-Cl1sF1sF1sCs_568
                    L6: Cs-Cl1sCl1sF1sCs_651
                        L7: Cs-Cl1sCl1sF1sCs_647
                L5: Cs-halCsHH_48
                    L6: Cs-F1sCsHH_48
                        L7: Cs-F1sCsHH_67
                    L6: Cs-Br1sCsHH_219
                        L7: Cs-Br1sCsHH_222
                    L6: Cs-Cl1sCsHH_365
                        L7: Cs-Cl1sCsHH_373
                L5: Cs-halhalCsH_52
                    L6: Cs-F1sF1sCsH_52
                        L7: Cs-F1sF1sCsH_84
                    L6: Cs-Br1sBr1sCsH_215
                        L7: Cs-Br1sBr1sCsH_237
                    L6: Cs-Cl1sCl1sCsH_371
                        L7: Cs-Cl1sCl1sCsH_374
                    L6: Cs-Br1sF1sCsH_533
                        L7: Cs-Br1sF1sCsH_541
                    L6: Cs-Br1sCl1sCsH_536
                        L7: Cs-Br1sCl1sCsH_562
                    L6: Cs-Cl1sF1sCsH_544
                        L7: Cs-Cl1sF1sCsH_564
                L5: Cs-halO2sHH_57
                    L6: Cs-F1sO2sHH_57
                        L7: Cs-F1sO2sHH_184
                    L6: Cs-Br1sO2sHH_235
                        L7: Cs-Br1sO2sHH_278
                    L6: Cs-Cl1sO2sHH_409
                        L7: Cs-Cl1sO2sHH_525
                L5: Cs-halhalhalO2s_58
                    L6: Cs-F1sF1sF1sO2s_58
                        L7: Cs-F1sF1sF1sO2s_197
                    L6: Cs-Br1sBr1sBr1sO2s_251
                    L6: Cs-Cl1sCl1sCl1sO2s_390
                        L7: Cs-Cl1sCl1sCl1sO2s_515
                    L6: Cs-Br1sF1sF1sO2s_531
                    L6: Cs-Br1sBr1sF1sO2s_559
                    L6: Cs-Cl1sCl1sF1sO2s_572
                    L6: Cs-Br1sCl1sCl1sO2s_596
                    L6: Cs-Br1sCl1sF1sO2s_615
                    L6: Cs-Cl1sF1sF1sO2s_626
                        L7: Cs-Cl1sF1sF1sO2s_630
                    L6: Cs-Br1sBr1sCl1sO2s_636
                L5: Cs-halhalhalCd_59
                    L6: Cs-F1sF1sF1sCd_59
                        L7: Cs-F1sF1sF1sCd_135
                    L6: Cs-Br1sBr1sBr1sCd_265
                        L7: Cs-Br1sBr1sBr1sCd_318
                    L6: Cs-Cl1sCl1sCl1sCd_383
                        L7: Cs-Cl1sCl1sCl1sCd_462
                    L6: Cs-Br1sCl1sF1sCd_542
                        L7: Cs-Br1sCl1sF1sCd_656
                    L6: Cs-Cl1sCl1sF1sCd_548
                        L7: Cs-Cl1sCl1sF1sCd_668
                    L6: Cs-Br1sF1sF1sCd_553
                        L7: Cs-Br1sF1sF1sCd_534
                    L6: Cs-Br1sCl1sCl1sCd_578
                        L7: Cs-Br1sCl1sCl1sCd_692
                    L6: Cs-Br1sBr1sCl1sCd_591
                        L7: Cs-Br1sBr1sCl1sCd_649
                    L6: Cs-Br1sBr1sF1sCd_623
                        L7: Cs-Br1sBr1sF1sCd_639
                    L6: Cs-Cl1sF1sF1sCd_633
                        L7: Cs-Cl1sF1sF1sCd_677
                L5: Cs-halhalCtH_69
                    L6: Cs-F1sF1sCtH_69
                    L6: Cs-Br1sBr1sCtH_299
                    L6: Cs-Cl1sCl1sCtH_420
                    L6: Cs-Cl1sF1sCtH_538
                    L6: Cs-Br1sCl1sCtH_579
                    L6: Cs-Br1sF1sCtH_660
                L5: Cs-halhalO2sH_70
                    L6: Cs-F1sF1sO2sH_70
                        L7: Cs-F1sF1sO2sH_174
                    L6: Cs-Br1sBr1sO2sH_248
                    L6: Cs-Cl1sCl1sO2sH_393
                        L7: Cs-Cl1sCl1sO2sH_484
                    L6: Cs-Cl1sF1sO2sH_540
                        L7: Cs-Cl1sF1sO2sH_704
                    L6: Cs-Br1sF1sO2sH_589
                    L6: Cs-Br1sCl1sO2sH_597
                L5: Cs-halCtHH_72
                    L6: Cs-F1sCtHH_72
                    L6: Cs-Br1sCtHH_269
                    L6: Cs-Cl1sCtHH_405
                L5: Cs-halCdHH_75
                    L6: Cs-F1sCdHH_75
                        L7: Cs-F1sCdHH_95
                    L6: Cs-Br1sCdHH_228
                        L7: Cs-Br1sCdHH_282
                    L6: Cs-Cl1sCdHH_375
                        L7: Cs-Cl1sCdHH_394
                L5: Cs-halhalhalCO_94
                    L6: Cs-F1sF1sF1sCO_94
                        L7: Cs-F1sF1sF1sCO_172
                    L6: Cs-Br1sBr1sBr1sCO_341
                        L7: Cs-Br1sBr1sBr1sCO_348
                    L6: Cs-Cl1sCl1sCl1sCO_471
                        L7: Cs-Cl1sCl1sCl1sCO_505
                    L6: Cs-Br1sBr1sF1sCO_556
                        L7: Cs-Br1sBr1sF1sCO_735
                    L6: Cs-Cl1sCl1sF1sCO_583
                        L7: Cs-Cl1sCl1sF1sCO_694
                    L6: Cs-Br1sBr1sCl1sCO_618
                        L7: Cs-Br1sBr1sCl1sCO_627
                    L6: Cs-Cl1sF1sF1sCO_622
                        L7: Cs-Cl1sF1sF1sCO_570
                    L6: Cs-Br1sCl1sCl1sCO_652
                        L7: Cs-Br1sCl1sCl1sCO_700
                    L6: Cs-Br1sF1sF1sCO_658
                        L7: Cs-Br1sF1sF1sCO_741
                    L6: Cs-Br1sCl1sF1sCO_714
                        L7: Cs-Br1sCl1sF1sCO_712
                L5: Cs-halhalCdH_97
                    L6: Cs-F1sF1sCdH_97
                        L7: Cs-F1sF1sCdH_109
                    L6: Cs-Br1sBr1sCdH_229
                        L7: Cs-Br1sBr1sCdH_298
                    L6: Cs-Cl1sCl1sCdH_367
                        L7: Cs-Cl1sCl1sCdH_426
                    L6: Cs-Br1sF1sCdH_535
                        L7: Cs-Br1sF1sCdH_585
                    L6: Cs-Br1sCl1sCdH_551
                        L7: Cs-Br1sCl1sCdH_646
                    L6: Cs-Cl1sF1sCdH_563
                        L7: Cs-Cl1sF1sCdH_624
                L5: Cs-halhalCOH_133
                    L6: Cs-F1sF1sCOH_133
                        L7: Cs-F1sF1sCOH_191
                    L6: Cs-Br1sBr1sCOH_256
                        L7: Cs-Br1sBr1sCOH_356
                    L6: Cs-Cl1sCl1sCOH_418
                        L7: Cs-Cl1sCl1sCOH_495
                    L6: Cs-Cl1sF1sCOH_574
                        L7: Cs-Cl1sF1sCOH_605
                    L6: Cs-Br1sF1sCOH_612
                        L7: Cs-Br1sF1sCOH_736
                    L6: Cs-Br1sCl1sCOH_632
                        L7: Cs-Br1sCl1sCOH_716
                L5: Cs-halCOHH_138
                    L6: Cs-F1sCOHH_138
                        L7: Cs-F1sCOHH_182
                    L6: Cs-Br1sCOHH_301
                        L7: Cs-Br1sCOHH_347
                    L6: Cs-Cl1sCOHH_401
                        L7: Cs-Cl1sCOHH_498
                L5: Cs-halhalhalCt_158
                    L6: Cs-F1sF1sF1sCt_158
                    L6: Cs-Br1sBr1sBr1sCt_303
                    L6: Cs-Cl1sCl1sCl1sCt_387
                    L6: Cs-Br1sCl1sF1sCt_547
                    L6: Cs-Br1sBr1sCl1sCt_555
                    L6: Cs-Cl1sCl1sF1sCt_557
                    L6: Cs-Br1sF1sF1sCt_642
                    L6: Cs-Br1sBr1sF1sCt_653
                    L6: Cs-Br1sCl1sCl1sCt_661
                    L6: Cs-Cl1sF1sF1sCt_687
                L5: Cs-halC2sHH_177
                    L6: Cs-F1sC2sHH_177
                    L6: Cs-Br1sC2sHH_350
                    L6: Cs-Cl1sC2sHH_521
                L5: Cs-halhalC2sH_183
                    L6: Cs-F1sF1sC2sH_183
                    L6: Cs-Br1sBr1sC2sH_332
                    L6: Cs-Cl1sCl1sC2sH_496
                L5: Cs-halhalhalC2s_194
                    L6: Cs-F1sF1sF1sC2s_194
                    L6: Cs-Cl1sCl1sCl1sC2s_507
            L4: RdCH2
                L5: Cd-halCdH_45
                    L6: Cd-F1sCdH_45
                        L7: Cd-F1sCdH_85
                    L6: Cd-Br1sCdH_225
                        L7: Cd-Br1sCdH_289
                        L7: Cd-Br1sCdH_362
                    L6: Cd-Cl1sCdH_372
                        L7: Cd-Cl1sCdH_386
                L5: Cd-halhalCd_54
                    L6: Cd-F1sF1sCd_54
                        L7: Cd-F1sF1sCd_78
                    L6: Cd-Br1sBr1sCd_254
                        L7: Cd-Br1sBr1sCd_220
                    L6: Cd-Cl1sCl1sCd_399
                        L7: Cd-Cl1sCl1sCd_423
                    L6: Cd-Cl1sF1sCd_527
                        L7: Cd-Cl1sF1sCd_529
                    L6: Cd-Br1sCl1sCd_539
                        L7: Cd-Br1sCl1sCd_549
                    L6: Cd-Br1sF1sCd_550
                        L7: Cd-Br1sF1sCd_558
                L5: CO-halO2dH_82
                    L6: CO-F1sO2dH_82
                    L6: CO-Cl1sO2dH_526
                L5: Cd-halhalCdd_130
                    L6: Cd-F1sF1sCdd_130
                    L6: Cd-Br1sBr1sCdd_243
                    L6: Cd-Cl1sCl1sCdd_376
                    L6: Cd-Br1sCl1sCdd_537
                    L6: Cd-Br1sF1sCdd_571
                    L6: Cd-Cl1sF1sCdd_614
                L5: Cd-halCddH_136
                    L6: Cd-F1sCddH_136
                    L6: Cd-Br1sCddH_276
                    L6: Cd-Cl1sCddH_458
                L5: CO-halhalO2d_188
                    L6: CO-F1sF1sO2d_188
                    L6: CO-Br1sBr1sO2d_302
                    L6: CO-Cl1sCl1sO2d_516
                    L6: CO-Br1sF1sO2d_669
                    L6: CO-Br1sCl1sO2d_679
                    L6: CO-Cl1sF1sO2d_726
                L5: Cd-halC2dH_457
                    L6: Cd-Cl1sC2dH_457
            L4: CtCH
                L5: Ct-halCt_39
                    L6: Ct-F1sCt_39
                    L6: Ct-Br1sCt_259
                    L6: Ct-Cl1sCt_380
            L4: RsCH2sR
                L5: Cs-halhalCsCs_40
                    L6: Cs-F1sF1sCsCs_40
                        L7: Cs-F1sF1sCsCs_41
                    L6: Cs-Br1sBr1sCsCs_217
                        L7: Cs-Br1sBr1sCsCs_271
                        L7: Cs-Br1sBr1sCsCs_353
                    L6: Cs-Cl1sCl1sCsCs_378
                        L7: Cs-Cl1sCl1sCsCs_364
                    L6: Cs-Br1sCl1sCsCs_543
                        L7: Cs-Br1sCl1sCsCs_532
                    L6: Cs-Br1sF1sCsCs_565
                        L7: Cs-Br1sF1sCsCs_648
                    L6: Cs-Cl1sF1sCsCs_613
                        L7: Cs-Cl1sF1sCsCs_609
                L5: Cs-halhalO2sCs_47
                    L6: Cs-F1sF1sO2sCs_47
                        L7: Cs-F1sF1sO2sCs_121
                        L7: Cs-F1sF1sO2sCs_134
                    L6: Cs-Br1sBr1sO2sCs_234
                        L7: Cs-Br1sBr1sO2sCs_300
                        L7: Cs-Br1sBr1sO2sCs_309
                    L6: Cs-Cl1sCl1sO2sCs_379
                        L7: Cs-Cl1sCl1sO2sCs_414
                        L7: Cs-Cl1sCl1sO2sCs_415
                    L6: Cs-Br1sCl1sO2sCs_552
                        L7: Cs-Br1sCl1sO2sCs_625
                        L7: Cs-Br1sCl1sO2sCs_725
                    L6: Cs-Br1sF1sO2sCs_584
                        L7: Cs-Br1sF1sO2sCs_619
                    L6: Cs-Cl1sF1sO2sCs_592
                        L7: Cs-Cl1sF1sO2sCs_595
                        L7: Cs-Cl1sF1sO2sCs_690
                L5: Cs-halhalCsCd_55
                    L6: Cs-F1sF1sCsCd_55
                        L7: Cs-F1sF1sCsCd_120
                        L7: Cs-F1sF1sCdCs_53
                    L6: Cs-Br1sBr1sCsCd_286
                        L7: Cs-Br1sBr1sCsCd_293
                        L7: Cs-Br1sBr1sCdCs_581
                    L6: Cs-Cl1sCl1sCsCd_370
                        L7: Cs-Cl1sCl1sCsCd_385
                        L7: Cs-Cl1sCl1sCdCs_493
                    L6: Cs-Cl1sF1sCsCd_582
                        L7: Cs-Cl1sF1sCdCs_634
                        L7: Cs-Cl1sF1sCsCd_560
                    L6: Cs-Br1sF1sCsCd_604
                        L7: Cs-Br1sF1sCsCd_703
                        L7: Cs-Br1sF1sCdCs_734
                    L6: Cs-Br1sCl1sCsCd_617
                        L7: Cs-Br1sCl1sCsCd_635
                        L7: Cs-Br1sCl1sCdCs_686
                L5: Cs-halCsCOH_61
                    L6: Cs-F1sCsCOH_61
                        L7: Cs-F1sCsCOH_89
                        L7: Cs-F1sCsCOH_49
                    L6: Cs-Br1sCsCOH_267
                        L7: Cs-Br1sCsCOH_313
                        L7: Cs-Br1sCsCOH_316
                    L6: Cs-Cl1sCsCOH_425
                        L7: Cs-Cl1sCsCOH_467
                        L7: Cs-Cl1sCsCOH_486
                L5: Cs-halO2sCsH_65
                    L6: Cs-F1sO2sCsH_65
                        L7: Cs-F1sO2sCsH_106
                        L7: Cs-F1sO2sCsH_131
                    L6: Cs-Br1sO2sCsH_231
                        L7: Cs-Br1sO2sCsH_233
                        L7: Cs-Br1sO2sCsH_266
                    L6: Cs-Cl1sO2sCsH_428
                        L7: Cs-Cl1sO2sCsH_429
                        L7: Cs-Cl1sO2sCsH_398
                L5: Cs-halhalO2sO2s_79
                    L6: Cs-F1sF1sO2sO2s_79
                        L7: Cs-F1sF1sO2sO2s_93
                    L6: Cs-Br1sBr1sO2sO2s_241
                    L6: Cs-Cl1sCl1sO2sO2s_430
                    L6: Cs-Br1sF1sO2sO2s_594
                    L6: Cs-Br1sCl1sO2sO2s_616
                    L6: Cs-Cl1sF1sO2sO2s_629
                L5: Cs-halCsCsH_88
                    L6: Cs-F1sCsCsH_88
                        L7: Cs-F1sCsCsH_74
                    L6: Cs-Br1sCsCsH_218
                        L7: Cs-Br1sCsCsH_268
                    L6: Cs-Cl1sCsCsH_369
                        L7: Cs-Cl1sCsCsH_397
                L5: Cs-halO2sCOH_104
                    L6: Cs-F1sO2sCOH_104
                        L7: Cs-F1sO2sCOH_149
                        L7: Cs-F1sO2sCOH_173
                    L6: Cs-Br1sO2sCOH_325
                        L7: Cs-Br1sO2sCOH_339
                        L7: Cs-Br1sO2sCOH_246
                    L6: Cs-Cl1sO2sCOH_511
                        L7: Cs-Cl1sO2sCOH_520
                        L7: Cs-Cl1sO2sCOH_460
                L5: Cs-halhalO2sCd_107
                    L6: Cs-F1sF1sO2sCd_107
                        L7: Cs-F1sF1sO2sCd_125
                        L7: Cs-F1sF1sO2sCd_126
                    L6: Cs-Br1sBr1sO2sCd_227
                        L7: Cs-Br1sBr1sO2sCd_344
                        L7: Cs-Br1sBr1sO2sCd_698
                    L6: Cs-Cl1sCl1sO2sCd_427
                        L7: Cs-Cl1sCl1sO2sCd_431
                        L7: Cs-Cl1sCl1sO2sCd_485
                    L6: Cs-Br1sF1sO2sCd_528
                        L7: Cs-Br1sF1sO2sCd_673
                        L7: Cs-Br1sF1sO2sCd_705
                    L6: Cs-Br1sCl1sO2sCd_600
                        L7: Cs-Br1sCl1sO2sCd_637
                    L6: Cs-Cl1sF1sO2sCd_665
                        L7: Cs-Cl1sF1sO2sCd_682
                        L7: Cs-Cl1sF1sO2sCd_644
                L5: Cs-halCsCdH_108
                    L6: Cs-F1sCsCdH_108
                        L7: Cs-F1sCdCsH_50
                        L7: Cs-F1sCsCdH_77
                    L6: Cs-Br1sCsCdH_226
                        L7: Cs-Br1sCsCdH_320
                        L7: Cs-Br1sCdCsH_355
                    L6: Cs-Cl1sCsCdH_410
                        L7: Cs-Cl1sCsCdH_472
                        L7: Cs-Cl1sCdCsH_474
                L5: Cs-halO2sO2sH_111
                    L6: Cs-F1sO2sO2sH_111
                        L7: Cs-F1sO2sO2sH_139
                    L6: Cs-Br1sO2sO2sH_249
                        L7: Cs-Br1sO2sO2sH_322
                    L6: Cs-Cl1sO2sO2sH_389
                        L7: Cs-Cl1sO2sO2sH_469
                L5: Cs-halhalCsCt_124
                    L6: Cs-F1sF1sCsCt_124
                        L7: Cs-F1sF1sCsCt_154
                    L6: Cs-Br1sBr1sCsCt_315
                        L7: Cs-Br1sBr1sCsCt_721
                    L6: Cs-Cl1sCl1sCsCt_403
                        L7: Cs-Cl1sCl1sCsCt_476
                    L6: Cs-Cl1sF1sCsCt_608
                        L7: Cs-Cl1sF1sCsCt_655
                    L6: Cs-Br1sF1sCsCt_640
                        L7: Cs-Br1sF1sCsCt_638
                    L6: Cs-Br1sCl1sCsCt_672
                        L7: Cs-Br1sCl1sCsCt_699
                L5: Cs-halCsCtH_128
                    L6: Cs-F1sCsCtH_128
                        L7: Cs-F1sCsCtH_163
                    L6: Cs-Br1sCsCtH_272
                        L7: Cs-Br1sCsCtH_290
                    L6: Cs-Cl1sCsCtH_438
                        L7: Cs-Cl1sCsCtH_439
                L5: Cs-halO2sCdH_137
                    L6: Cs-F1sO2sCdH_137
                        L7: Cs-F1sO2sCdH_161
                        L7: Cs-F1sO2sCdH_129
                    L6: Cs-Br1sO2sCdH_261
                        L7: Cs-Br1sO2sCdH_304
                        L7: Cs-Br1sO2sCdH_360
                    L6: Cs-Cl1sO2sCdH_468
                        L7: Cs-Cl1sO2sCdH_477
                        L7: Cs-Cl1sO2sCdH_463
                L5: Cs-halhalCsCO_157
                    L6: Cs-F1sF1sCsCO_157
                        L7: Cs-F1sF1sCsCO_185
                        L7: Cs-F1sF1sCsCO_145
                    L6: Cs-Br1sBr1sCsCO_255
                        L7: Cs-Br1sBr1sCsCO_710
                        L7: Cs-Br1sBr1sCsCO_250
                    L6: Cs-Cl1sCl1sCsCO_452
                        L7: Cs-Cl1sCl1sCsCO_453
                        L7: Cs-Cl1sCl1sCsCO_443
                    L6: Cs-Cl1sF1sCsCO_607
                        L7: Cs-Cl1sF1sCsCO_695
                        L7: Cs-Cl1sF1sCsCO_722
                    L6: Cs-Br1sCl1sCsCO_645
                        L7: Cs-Br1sCl1sCsCO_675
                        L7: Cs-Br1sCl1sCsCO_576
                    L6: Cs-Br1sF1sCsCO_684
                        L7: Cs-Br1sF1sCsCO_697
                        L7: Cs-Br1sF1sCsCO_643
                L5: Cs-halCsC2sH_160
                    L6: Cs-F1sCsC2sH_160
                    L6: Cs-Br1sCsC2sH_363
                    L6: Cs-Cl1sCsC2sH_508
                L5: Cs-halhalO2sCO_165
                    L6: Cs-F1sF1sO2sCO_165
                        L7: Cs-F1sF1sO2sCO_199
                        L7: Cs-F1sF1sO2sCO_164
                    L6: Cs-Br1sBr1sO2sCO_244
                        L7: Cs-Br1sBr1sO2sCO_334
                    L6: Cs-Cl1sCl1sO2sCO_447
                        L7: Cs-Cl1sCl1sO2sCO_513
                        L7: Cs-Cl1sCl1sO2sCO_524
                    L6: Cs-Br1sF1sO2sCO_621
                        L7: Cs-Br1sF1sO2sCO_680
                    L6: Cs-Br1sCl1sO2sCO_641
                        L7: Cs-Br1sCl1sO2sCO_631
                    L6: Cs-Cl1sF1sO2sCO_666
                        L7: Cs-Cl1sF1sO2sCO_715
                        L7: Cs-Cl1sF1sO2sCO_720
                L5: Cs-halO2sCtH_169
                    L6: Cs-F1sO2sCtH_169
                        L7: Cs-F1sO2sCtH_143
                    L6: Cs-Br1sO2sCtH_317
                        L7: Cs-Br1sO2sCtH_340
                    L6: Cs-Cl1sO2sCtH_465
                        L7: Cs-Cl1sO2sCtH_413
                L5: Cs-halhalO2sCt_170
                    L6: Cs-F1sF1sO2sCt_170
                        L7: Cs-F1sF1sO2sCt_87
                    L6: Cs-Br1sBr1sO2sCt_294
                    L6: Cs-Cl1sCl1sO2sCt_470
                        L7: Cs-Cl1sCl1sO2sCt_522
                    L6: Cs-Br1sCl1sO2sCt_650
                    L6: Cs-Cl1sF1sO2sCt_663
                    L6: Cs-Br1sF1sO2sCt_676
                L5: Cs-halhalCsC2s_181
                    L6: Cs-F1sF1sCsC2s_181
                    L6: Cs-Cl1sCl1sCsC2s_500
            L4: Aldehyde
                L5: CO-halO2dCs_90
                    L6: CO-F1sO2dCs_90
                        L7: CO-F1sO2dCs_116
                    L6: CO-Br1sO2dCs_239
                        L7: CO-Br1sO2dCs_279
                        L7: CO-Br1sO2dCs_335
                    L6: CO-Cl1sO2dCs_444
                        L7: CO-Cl1sO2dCs_475
                L5: CO-halO2dCd_100
                    L6: CO-F1sO2dCd_100
                        L7: CO-F1sO2dCd_122
                    L6: CO-Br1sO2dCd_281
                        L7: CO-Br1sO2dCd_314
                    L6: CO-Cl1sO2dCd_454
                        L7: CO-Cl1sO2dCd_466
                L5: CO-halO2sO2d_103
                    L6: CO-F1sO2sO2d_103
                        L7: CO-F1sO2sO2d_195
                    L6: CO-Br1sO2sO2d_287
                    L6: CO-Cl1sO2sO2d_445
                L5: CO-halO2dC2s_155
                    L6: CO-F1sO2dC2s_155
                L5: CO-halO2dCO_159
                    L6: CO-F1sO2dCO_159
                        L7: CO-F1sO2dCO_190
                    L6: CO-Br1sO2dCO_311
                        L7: CO-Br1sO2dCO_345
                    L6: CO-Cl1sO2dCO_497
                        L7: CO-Cl1sO2dCO_499
                L5: CO-halO2dCt_192
                    L6: CO-F1sO2dCt_192
                    L6: CO-Br1sO2dCt_330
                    L6: CO-Cl1sO2dCt_412
            L4: Ketene
            L4: Cumulene
            L4: CdCHsR
                L5: Cd-halCdCt_44
                    L6: Cd-F1sCdCt_44
                        L7: Cd-F1sCtCd_96
                    L6: Cd-Br1sCdCt_277
                        L7: Cd-Br1sCtCd_295
                    L6: Cd-Cl1sCdCt_488
                        L7: Cd-Cl1sCtCd_489
                L5: Cd-halCsCd_56
                    L6: Cd-F1sCsCd_56
                        L7: Cd-F1sCdCs_76
                        L7: Cd-F1sCsCd_118
                    L6: Cd-Br1sCsCd_224
                        L7: Cd-Br1sCsCd_253
                        L7: Cd-Br1sCdCs_263
                    L6: Cd-Cl1sCsCd_411
                        L7: Cd-Cl1sCsCd_432
                        L7: Cd-Cl1sCdCs_433
                L5: Cd-halO2sCd_81
                    L6: Cd-F1sO2sCd_81
                        L7: Cd-F1sO2sCd_71
                    L6: Cd-Br1sO2sCd_252
                        L7: Cd-Br1sO2sCd_258
                    L6: Cd-Cl1sO2sCd_384
                        L7: Cd-Cl1sO2sCd_436
                        L7: Cd-Cl1sO2sCd_512
                L5: Cd-halCdCd_91
                    L6: Cd-F1sCdCd_91
                        L7: Cd-F1sCdCd_92
                        L7: Cd-F1sCdCd_127
                    L6: Cd-Br1sCdCd_285
                        L7: Cd-Br1sCdCd_292
                        L7: Cd-Br1sCdCd_270
                    L6: Cd-Cl1sCdCd_402
                        L7: Cd-Cl1sCdCd_422
                        L7: Cd-Cl1sCdCd_440
                L5: Cd-halCOCd_99
                    L6: Cd-F1sCOCd_99
                        L7: Cd-F1sCOCd_179
                        L7: Cd-F1sCdCO_180
                    L6: Cd-Br1sCOCd_280
                        L7: Cd-Br1sCdCO_329
                        L7: Cd-Br1sCOCd_349
                    L6: Cd-Cl1sCOCd_451
                        L7: Cd-Cl1sCdCO_473
                        L7: Cd-Cl1sCOCd_487
                L5: Cd-halCsCdd_141
                    L6: Cd-F1sCsCdd_141
                        L7: Cd-F1sCsCdd_150
                    L6: Cd-Br1sCsCdd_247
                        L7: Cd-Br1sCsCdd_620
                    L6: Cd-Cl1sCsCdd_421
                        L7: Cd-Cl1sCsCdd_503
                L5: Cd-halO2sCdd_153
                    L6: Cd-F1sO2sCdd_153
                    L6: Cd-Br1sO2sCdd_291
                    L6: Cd-Cl1sO2sCdd_408
                L5: Cd-halCdC2s_175
                    L6: Cd-F1sCdC2s_175
                    L6: Cd-Br1sCdC2s_296
                    L6: Cd-Cl1sCdC2s_482
            L4: CtCsR
            L4: RsCHsR2
                L5: Cs-halO2sO2sCs_62
                    L6: Cs-F1sO2sO2sCs_62
                        L7: Cs-F1sO2sO2sCs_114
                        L7: Cs-F1sO2sO2sCs_147
                    L6: Cs-Br1sO2sO2sCs_260
                        L7: Cs-Br1sO2sO2sCs_681
                    L6: Cs-Cl1sO2sO2sCs_435
                        L7: Cs-Cl1sO2sO2sCs_659
                        L7: Cs-Cl1sO2sO2sCs_391
                L5: Cs-halO2sCsCs_63
                    L6: Cs-F1sO2sCsCs_63
                        L7: Cs-F1sO2sCsCs_152
                        L7: Cs-F1sO2sCsCs_51
                    L6: Cs-Br1sO2sCsCs_275
                        L7: Cs-Br1sO2sCsCs_351
                        L7: Cs-Br1sO2sCsCs_358
                    L6: Cs-Cl1sO2sCsCs_459
                        L7: Cs-Cl1sO2sCsCs_464
                        L7: Cs-Cl1sO2sCsCs_417
                L5: Cs-halCsCsCs_123
                    L6: Cs-F1sCsCsCs_123
                        L7: Cs-F1sCsCsCs_105
                    L6: Cs-Br1sCsCsCs_307
                        L7: Cs-Br1sCsCsCs_326
                    L6: Cs-Cl1sCsCsCs_395
                        L7: Cs-Cl1sCsCsCs_406
            L4: CdCsR2
            L4: Ketone
            L4: CsCsC3
            L4: C2s-halCs_64
                L5: C2s-F1sCs_64
                L5: C2s-Br1sCs_333
                L5: C2s-Cl1sCs_455
            L4: Cs-halHHH_98
                L5: Cs-F1sHHH_98
                L5: Cs-Br1sHHH_342
                L5: Cs-Cl1sHHH_502
            L4: C2s-halCO_156
                L5: C2s-F1sCO_156
            L4: Cs-halhalhalH_168
                L5: Cs-F1sF1sF1sH_168
                L5: Cs-Br1sBr1sBr1sH_361
                L5: Cs-Cl1sCl1sCl1sH_519
                L5: Cs-Cl1sCl1sF1sH_657
                L5: Cs-Br1sCl1sCl1sH_670
                L5: Cs-Cl1sF1sF1sH_671
                L5: Cs-Br1sBr1sCl1sH_685
                L5: Cs-Br1sBr1sF1sH_723
                L5: Cs-Br1sF1sF1sH_724
                L5: Cs-Br1sCl1sF1sH_729
            L4: C2s-halCt_171
                L5: C2s-F1sCt_171
            L4: C2s-halCd_176
                L5: C2s-F1sCd_176
                L5: C2s-Br1sCd_297
                L5: C2s-Cl1sCd_483
            L4: C2s-halO2s_178
                L5: C2s-F1sO2s_178
                L5: C2s-Br1sO2s_319
                L5: C2s-Cl1sO2s_461
            L4: Cs-halhalhalhal_186
                L5: Cs-F1sF1sF1sF1s_186
                L5: Cs-Br1sBr1sBr1sBr1s_238
                L5: Cs-Cl1sCl1sCl1sCl1s_518
                L5: Cs-Cl1sCl1sF1sF1s_593
                L5: Cs-Br1sCl1sCl1sCl1s_674
                L5: Cs-Br1sBr1sCl1sCl1s_689
                L5: Cs-Br1sBr1sBr1sF1s_691
                L5: Cs-Br1sF1sF1sF1s_693
                L5: Cs-Cl1sCl1sCl1sF1s_696
                L5: Cs-Br1sCl1sCl1sF1s_709
                L5: Cs-Br1sBr1sF1sF1s_711
                L5: Cs-Cl1sF1sF1sF1s_713
                L5: Cs-Br1sBr1sCl1sF1s_732
                L5: Cs-Br1sBr1sBr1sCl1s_733
                L5: Cs-Br1sCl1sF1sF1s_738
            L4: Cs-halhalHH_193
                L5: Cs-F1sF1sHH_193
                L5: Cs-Br1sBr1sHH_305
                L5: Cs-Cl1sCl1sHH_510
                L5: Cs-Br1sCl1sHH_688
                L5: Cs-Cl1sF1sHH_701
                L5: Cs-Br1sF1sHH_708
            L4: C2s-halhal_327
                L5: C2s-Br1sBr1s_327
                L5: C2s-Cl1sCl1s_523
            L4: C2sc-halCsCsc_739
                L5: C2sc-Cl1sCsCsc_739
            L4: Csc-halO2sC2sc_740
                L5: Csc-Br1sO2sC2sc_740
        L3: O_R0
            L4: Alcohol
                L5: O2s-halCs_37
                    L6: O2s-F1sCs_37
                    L6: O2s-Br1sCs_221
                        L7: O2s-Br1sCs_727
                    L6: O2s-Cl1sCs_388
                        L7: O2s-Cl1sCs_667
                L5: O2s-halCd_80
                    L6: O2s-F1sCd_80
                    L6: O2s-Br1sCd_242
                    L6: O2s-Cl1sCd_382
                        L7: O2s-Cl1sCd_517
                L5: O2s-halCO_102
                    L6: O2s-F1sCO_102
                    L6: O2s-Br1sCO_306
                        L7: O2s-Br1sCO_328
                    L6: O2s-Cl1sCO_478
                        L7: O2s-Cl1sCO_509
                L5: O2s-halCt_144
                    L6: O2s-F1sCt_144
                    L6: O2s-Br1sCt_346
                    L6: O2s-Cl1sCt_448
            L4: Ether
            L4: COOH
            L4: COOC
            L4: Peroxy
            L4: O2s-halO2s_46
                L5: O2s-F1sO2s_46
                    L6: O2s-F1sO2s_187
                L5: O2s-Br1sO2s_230
                L5: O2s-Cl1sO2s_437
            L4: O2s-halH_132
                L5: O2s-F1sH_132
                L5: O2s-Br1sH_337
                L5: O2s-Cl1sH_504
            L4: O2s-halhal_196
                L5: O2s-F1sF1s_196
                L5: O2s-Br1sBr1s_359
                L5: O2s-Cl1sCl1s_492
                L5: O2s-Br1sF1s_702
                L5: O2s-Cl1sF1s_707
                L5: O2s-Br1sCl1s_717
        L3: N_R0
            L4: Amine_pri
                L5: Amide_pri
            L4: Amine_sec
                L5: Amide_sec
                L5: Imide
            L4: Amine_ter
                L5: Amide_ter
            L4: Nitrile
            L4: Nitroso
                L5: Nitro
                    L6: Nitrates
                L5: Nitrites
    L2: R!H!Val7x1
        L3: C_R1
            L4: RsCH2r
                L5: Cs-halCsH_38
                    L6: Cs-F1sCsH_38
                    L6: Cs-Br1sCsH_240
                    L6: Cs-Cl1sCsH_366
                L5: Cs-halhalCs_43
                    L6: Cs-F1sF1sCs_43
                    L6: Cs-Br1sBr1sCs_245
                    L6: Cs-Cl1sCl1sCs_392
                    L6: Cs-Cl1sF1sCs_554
                    L6: Cs-Br1sF1sCs_577
                    L6: Cs-Br1sCl1sCs_598
                L5: Cs-halCdH_60
                    L6: Cs-F1sCdH_60
                    L6: Cs-Br1sCdH_264
                    L6: Cs-Cl1sCdH_368
                L5: Cs-halO2sH_66
                    L6: Cs-F1sO2sH_66
                    L6: Cs-Br1sO2sH_216
                    L6: Cs-Cl1sO2sH_404
                L5: Cs-halhalO2s_83
                    L6: Cs-F1sF1sO2s_83
                    L6: Cs-Br1sBr1sO2s_262
                    L6: Cs-Cl1sCl1sO2s_381
                    L6: Cs-Cl1sF1sO2s_567
                    L6: Cs-Br1sCl1sO2s_575
                    L6: Cs-Br1sF1sO2s_590
                L5: Cs-halhalCd_101
                    L6: Cs-F1sF1sCd_101
                    L6: Cs-Br1sBr1sCd_273
                    L6: Cs-Cl1sCl1sCd_400
                    L6: Cs-Br1sCl1sCd_545
                    L6: Cs-Cl1sF1sCd_566
                    L6: Cs-Br1sF1sCd_573
                L5: Cs-halhalCO_117
                    L6: Cs-F1sF1sCO_117
                    L6: Cs-Br1sBr1sCO_288
                    L6: Cs-Cl1sCl1sCO_442
                    L6: Cs-Cl1sF1sCO_587
                    L6: Cs-Br1sCl1sCO_606
                    L6: Cs-Br1sF1sCO_662
                L5: Cs-halhalCt_140
                    L6: Cs-F1sF1sCt_140
                    L6: Cs-Br1sBr1sCt_308
                    L6: Cs-Cl1sCl1sCt_450
                    L6: Cs-Cl1sF1sCt_610
                    L6: Cs-Br1sCl1sCt_628
                    L6: Cs-Br1sF1sCt_664
                L5: Cs-halCOH_146
                    L6: Cs-F1sCOH_146
                    L6: Cs-Br1sCOH_338
                    L6: Cs-Cl1sCOH_419
                L5: Cs-halCtH_162
                    L6: Cs-F1sCtH_162
                    L6: Cs-Br1sCtH_324
                    L6: Cs-Cl1sCtH_446
            L4: RdCHr
                L5: Cd-halCd_113
                    L6: Cd-F1sCd_113
                    L6: Cd-Br1sCd_232
                    L6: Cd-Cl1sCd_416
                L5: Cd-halCdd_151
                    L6: Cd-F1sCdd_151
                    L6: Cd-Br1sCdd_283
                    L6: Cd-Cl1sCdd_480
                L5: CO-halO2d_198
                    L6: CO-F1sO2d_198
                    L6: CO-Cl1sO2d_491
            L4: CtCr
            L4: RsCHrsR
                L5: Cs-halCsCt_68
                    L6: Cs-F1sCsCt_68
                    L6: Cs-Br1sCsCt_274
                    L6: Cs-Cl1sCsCt_449
                L5: Cs-halCsCs_73
                    L6: Cs-F1sCsCs_73
                    L6: Cs-Br1sCsCs_223
                    L6: Cs-Cl1sCsCs_407
                L5: Cs-halO2sCs_110
                    L6: Cs-F1sO2sCs_110
                    L6: Cs-Br1sO2sCs_257
                    L6: Cs-Cl1sO2sCs_441
                L5: Cs-halCsCd_112
                    L6: Cs-F1sCsCd_112
                    L6: Cs-Cl1sCsCd_501
                    L6: Cs-Br1sCsCd_728
                L5: Cs-halCsCO_115
                    L6: Cs-F1sCsCO_115
                    L6: Cs-Br1sCsCO_310
                    L6: Cs-Cl1sCsCO_481
                L5: Cs-halO2sO2s_142
                    L6: Cs-F1sO2sO2s_142
                    L6: Cs-Br1sO2sO2s_343
                    L6: Cs-Cl1sO2sO2s_434
                L5: Cs-halO2sCO_148
                    L6: Cs-F1sO2sCO_148
                    L6: Cs-Br1sO2sCO_321
                    L6: Cs-Cl1sO2sCO_514
            L4: OdCrsR
            L4: CdCrsR
            L4: RsCrsR2
            L4: Cs-halhalH_119
                L5: Cs-F1sF1sH_119
                L5: Cs-Br1sBr1sH_312
                L5: Cs-Cl1sCl1sH_490
                L5: Cs-Cl1sF1sH_602
                L5: Cs-Br1sCl1sH_718
                L5: Cs-Br1sF1sH_737
            L4: Cs-halHH_166
                L5: Cs-F1sHH_166
                L5: Cs-Br1sHH_357
                L5: Cs-Cl1sHH_479
            L4: Cs-halhalhal_189
                L5: Cs-F1sF1sF1s_189
                L5: Cs-Br1sBr1sBr1s_323
                L5: Cs-Cl1sCl1sCl1s_456
                L5: Cs-Br1sCl1sF1s_654
                L5: Cs-Br1sBr1sF1s_678
                L5: Cs-Br1sF1sF1s_683
                L5: Cs-Br1sBr1sCl1s_706
                L5: Cs-Cl1sF1sF1s_719
                L5: Cs-Cl1sCl1sF1s_730
                L5: Cs-Br1sCl1sCl1s_731
        L3: O_R1
            L4: Oxy
            L4: O2s-hal_167
                L5: O2s-F1s_167
                L5: O2s-Br1s_352
                L5: O2s-Cl1s_494
    L2: R!H!Val7x2_trip
        L3: C_R2
            L4: RsCHrr
                L5: Cs-halCt_331
                    L6: Cs-Br1sCt_331
                    L6: Cs-Cl1sCt_506
                L5: Cs-halCO_336
                    L6: Cs-Br1sCO_336
                    L6: Cs-Cl1sCO_424
                L5: Cs-halCs_354
                    L6: Cs-Br1sCs_354
            L4: RdCrr
            L4: RsCrrsR
    L2: R!H!Val7x3_quart
"""
)

