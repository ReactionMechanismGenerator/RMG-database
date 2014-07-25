#!/usr/bin/env python
# encoding: utf-8

name = "Functional Group Values"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = -1,
    label = "R!H",
    group = "OR{R!Hx0, R!Hx1, R!Hx2, R!Hx3}",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "C_R0",
    group = 
"""
1 * C 0
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 1,
    label = "RsCH3",
    group = "OR{RsCH3x0, RsCH3x1, RsCH3x2}",
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
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 2,
    label = "RdCH2",
    group = "OR{RdCH2x0, RdCH2x1, RdCH2x2}",
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
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 3,
    label = "CtCH",
    group = "OR{CtCHx0, CtCHx1}",
    statmech = GroupFrequencies(
        frequencies = [
            (750, 770, 2),
            (3350, 3450, 1),
            (2000, 2200, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 4,
    label = "RsCH2sR",
    group = "OR{RsCH2sRx00, RsCH2sRx11, RsCH2sRx01, RsCH2sRx02, RsCH2sRx12, RsCH2sRx22}",
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
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 6,
    label = "Aldehyde",
    group = "OR{Aldehydex0, Aldehydex1, Aldehydex2}",
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
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 8,
    label = "Ketene",
    group = "OR{Ketenex0, Ketenex1, Ketenex2}",
    statmech = GroupFrequencies(
        frequencies = [
            (2110, 2130, 1),
            (495, 530, 1),
            (650, 925, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 7,
    label = "Cumulene",
    group = "OR{Cumulenex00, Cumulenex01, Cumulenex11, Cumulenex02, Cumulenex12, Cumulenex22}",
    statmech = GroupFrequencies(
        frequencies = [
            (540, 610, 2),
            (1970, 2140, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 5,
    label = "CdCHsR",
    group = "OR{CdCHsRx00, CdCHsRx01, CdCHsRx10, CdCHsRx11, CdCHsRx02, CdCHsRx20, CdCHsRx12, CdCHsRx21, CdCHsRx22}",
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
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 9,
    label = "CtCsR",
    group = "OR{CtCsRx00, CtCsRx01, CtCsRx10, CtCsRx11, CtCsRx02, CtCsRx12}",
    statmech = GroupFrequencies(
        frequencies = [
            (2100, 2250, 1),
            (500, 550, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 10,
    label = "RsCHsR2",
    group = "OR{RsCHsR2x000, RsCHsR2x111, RsCHsR2x222, RsCHsR2x001, RsCHsR2x002, RsCHsR2x110, RsCHsR2x112, RsCHsR2x220, RsCHsR2x221, RsCHsR2x012}",
    statmech = GroupFrequencies(
        frequencies = [
            (1380, 1390, 2),
            (370, 380, 2),
            (2800, 3000, 1),
            (430, 440, 1),
        ],
        symmetry = 6,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 11,
    label = "RdCsR2",
    group = "OR{RdCsR2x000, RdCsR2x001, RdCsR2x011, RdCsR2x002, RdCsR2x012, RdCsR2x022, RdCsR2x100, RdCsR2x101, RdCsR2x111, RdCsR2x102, RdCsR2x112, RdCsR2x122, RdCsR2x200, RdCsR2x201, RdCsR2x211, RdCsR2x202, RdCsR2x212, RdCsR2x222}",
    statmech = GroupFrequencies(
        frequencies = [
            (325, 375, 1),
            (415, 465, 1),
            (420, 450, 1),
            (1700, 1750, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 12,
    label = "Ketone",
    group = "OR{Ketonex00, Ketonex01, Ketonex11, Ketonex02, Ketonex12, Ketonex22}",
    statmech = GroupFrequencies(
        frequencies = [
            (365, 385, 1),
            (505, 600, 1),
            (445, 480, 1),
            (1700, 1720, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 13,
    label = "RsCsR3",
    group = "OR{RsCsR3x0000, RsCsR3x1111, RsCsR3x2222, RsCsR3x0001, RsCsR3x0002, RsCsR3x1110, RsCsR3x1112, RsCsR3x2220, RsCsR3x2221, RsCsR3x0011, RsCsR3x0022, RsCsR3x1122, RsCsR3x0012, RsCsR3x0112, RsCsR3x0122}",
    statmech = GroupFrequencies(
        frequencies = [
            (350, 400, 2),
            (1190, 1240, 2),
            (400, 500, 1),
        ],
        symmetry = 12,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "C_R1",
    group = 
"""
1 * C 1
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 14,
    label = "RsCH2r",
    group = "OR{RsCH2rx0, RsCH2rx1, RsCH2rx2}",
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
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 15,
    label = "RdCHr",
    group = "OR{RdCHrx0, RdCHrx1, RdCHrx2}",
    statmech = GroupFrequencies(
        frequencies = [
            (3115, 3125, 1),
            (620, 680, 1),
            (785, 800, 1),
            (1600, 1700, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCr",
    group = "OR{CtCrx0, CtCrx1}",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 16,
    label = "RsCHrsR",
    group = "OR{RsCHrsRx00, RsCHrsRx01, RsCHrsRx11, RsCHrsRx02, RsCHrsRx12, RsCHrsRx22}",
    statmech = GroupFrequencies(
        frequencies = [
            (3000, 3050, 1),
            (390, 425, 1),
            (1340, 1360, 1),
            (335, 370, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 18,
    label = "OdCrsR",
    group = "OR{OdCrsRx0, OdCrsRx1, OdCrsRx2}",
    statmech = GroupFrequencies(
        frequencies = [
            (1850, 1860, 1),
            (440, 470, 1),
            (900, 1000, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 17,
    label = "CdCrsR",
    group = "OR{CdCrsRx00, CdCrsRx01, CdCrsRx10, CdCrsRx11, CdCrsRx02, CdCrsRx20, CdCrsRx12, CdCrsRx21, CdCrsRx22}",
    statmech = GroupFrequencies(
        frequencies = [
            (1670, 1700, 1),
            (300, 440, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 19,
    label = "RsCrsR2",
    group = "OR{RsCrsR2x000, RsCrsR2x111, RsCrsR2x222, RsCrsR2x001, RsCrsR2x002, RsCrsR2x110, RsCrsR2x112, RsCrsR2x220, RsCrsR2x221, RsCrsR2x012}",
    statmech = GroupFrequencies(
        frequencies = [
            (360, 370, 2),
            (300, 400, 1),
        ],
        symmetry = 6,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "C_R2",
    group = 
"""
1 * C {2S,2T}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrr",
    group = "OR{RsCHrrx0, RsCHrrx1, RsCHrrx2}",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCrr",
    group = "OR{RdCrrx0, RdCrrx1, RdCrrx2}",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrrsR",
    group = "OR{RsCrrsRx00, RsCrrsRx01, RsCrrsRx11, RsCrrsRx02, RsCrrsRx12, RsCrrsRx22}",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "O_R0",
    group = 
"""
1 * O 0
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 20,
    label = "Alcohol",
    group = "OR{Alcoholx0, Alcoholx1, Alcoholx2}",
    statmech = GroupFrequencies(
        frequencies = [
            (3580, 3650, 1),
            (1210, 1345, 1),
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 21,
    label = "Ether",
    group = "OR{Etherx00, Etherx01, Etherx11, Etherx02, Etherx12, Etherx22}",
    statmech = GroupFrequencies(
        frequencies = [
            (350, 500, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 22,
    label = "ROOH",
    group = "OR{ROOHx0, ROOHx1, ROOHx2}",
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
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 23,
    label = "ROOR",
    group = "OR{ROORx00, ROORx01, ROORx11, ROORx02, ROORx12, ROORx22}",
    statmech = GroupFrequencies(
        frequencies = [
            (350, 500, 1),
            (795, 815, 1),
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 24,
    label = "Peroxy",
    group = "OR{Peroxyx0, Peroxyx1, Peroxyx2}",
    statmech = GroupFrequencies(
        frequencies = [
            (470, 515, 1),
            (1100, 1170, 1),
            (900, 1100, 1),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "O_R1",
    group = 
"""
1 * O 1
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Oxy",
    group = "OR{Oxyx0, Oxyx1, Oxyx2}",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "R!Hx0",
    group = 
"""
1 * R!H 0
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "R!Hx1",
    group = 
"""
1 * R!H 1
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "R!Hx2",
    group = 
"""
1 * R!H {2S,2T}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "R!Hx3",
    group = 
"""
1 * R!H {3D,3Q}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH3x0",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 0 {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
5   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH3x1",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 1 {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
5   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH3x2",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H {2S,2T} {1,S}
3   H   0       {1,S}
4   H   0       {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCH2x0",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   R!H 0 {1,D}
3   H   0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCH2x1",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   R!H 1 {1,D}
3   H   0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCH2x2",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H {2S,2T} {1,D}
3   H   0       {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCHx0",
    group = 
"""
1 * C 0 {2,T} {3,S}
2   C 0 {1,T}
3   H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCHx1",
    group = 
"""
1 * C 0 {2,T} {3,S}
2   C 1 {1,T}
3   H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH2sRx00",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   H   0 {1,S}
5   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH2sRx11",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 1 {1,S}
3   R!H 1 {1,S}
4   H   0 {1,S}
5   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH2sRx01",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 0 {1,S}
3   R!H 1 {1,S}
4   H   0 {1,S}
5   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH2sRx02",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 0       {1,S}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH2sRx12",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 1       {1,S}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH2sRx22",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Aldehydex0",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   O   0 {1,D}
3   R!H 0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Aldehydex1",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   O   0 {1,D}
3   R!H 1 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Aldehydex2",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   O   0       {1,D}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Ketenex0",
    group = 
"""
1 * C   0 {2,D} {3,D}
2   O   0 {1,D}
3   R!H 0 {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Ketenex1",
    group = 
"""
1 * C   0 {2,D} {3,D}
2   O   0 {1,D}
3   R!H 1 {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Ketenex2",
    group = 
"""
1 * C   0       {2,D} {3,D}
2   O   0       {1,D}
3   R!H {2S,2T} {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Cumulenex00",
    group = 
"""
1 * C 0 {2,D} {3,D}
2   C 0 {1,D}
3   C 0 {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Cumulenex01",
    group = 
"""
1 * C 0 {2,D} {3,D}
2   C 0 {1,D}
3   C 1 {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Cumulenex11",
    group = 
"""
1 * C 0 {2,D} {3,D}
2   C 1 {1,D}
3   C 1 {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Cumulenex02",
    group = 
"""
1 * C 0       {2,D} {3,D}
2   C 0       {1,D}
3   C {2S,2T} {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Cumulenex12",
    group = 
"""
1 * C 0       {2,D} {3,D}
2   C 1       {1,D}
3   C {2S,2T} {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Cumulenex22",
    group = 
"""
1 * C 0       {2,D} {3,D}
2   C {2S,2T} {1,D}
3   C {2S,2T} {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCHsRx00",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   C   0 {1,D}
3   R!H 0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCHsRx01",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   C   0 {1,D}
3   R!H 1 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCHsRx10",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   C   1 {1,D}
3   R!H 0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCHsRx11",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   C   1 {1,D}
3   R!H 1 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCHsRx02",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   C   0       {1,D}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCHsRx20",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   C   {2S,2T} {1,D}
3   R!H 0       {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCHsRx12",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   C   1       {1,D}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCHsRx21",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   C   {2S,2T} {1,D}
3   R!H 1       {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCHsRx22",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   C   {2S,2T} {1,D}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCsRx00",
    group = 
"""
1 * C   0 {2,T} {3,S}
2   C   0 {1,T}
3   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCsRx01",
    group = 
"""
1 * C   0 {2,T} {3,S}
2   C   0 {1,T}
3   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCsRx10",
    group = 
"""
1 * C   0 {2,T} {3,S}
2   C   1 {1,T}
3   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCsRx11",
    group = 
"""
1 * C   0 {2,T} {3,S}
2   C   1 {1,T}
3   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCsRx02",
    group = 
"""
1 * C   0       {2,T} {3,S}
2   C   0       {1,T}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCsRx12",
    group = 
"""
1 * C   0       {2,T} {3,S}
2   C   1       {1,T}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x000",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
5   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x111",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 1 {1,S}
3   R!H 1 {1,S}
4   R!H 1 {1,S}
5   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x222",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   R!H {2S,2T} {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x001",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 1 {1,S}
5   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x002",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 0       {1,S}
3   R!H 0       {1,S}
4   R!H {2S,2T} {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x110",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 1 {1,S}
3   R!H 1 {1,S}
4   R!H 0 {1,S}
5   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x112",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 1       {1,S}
3   R!H 1       {1,S}
4   R!H {2S,2T} {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x220",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   R!H 0       {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x221",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   R!H 1       {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHsR2x012",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 0       {1,S}
3   R!H 1       {1,S}
4   R!H {2S,2T} {1,S}
5   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x000",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   R!H 0 {1,D}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x001",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   R!H 0 {1,D}
3   R!H 0 {1,S}
4   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x011",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   R!H 0 {1,D}
3   R!H 1 {1,S}
4   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x002",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H 0       {1,D}
3   R!H 0       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x012",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H 0       {1,D}
3   R!H 1       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x022",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H 0       {1,D}
3   R!H {2S,2T} {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x100",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   R!H 1 {1,D}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x101",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   R!H 1 {1,D}
3   R!H 0 {1,S}
4   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x111",
    group = 
"""
1 * C   0 {2,D} {3,S} {4,S}
2   R!H 1 {1,D}
3   R!H 1 {1,S}
4   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x102",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H 1       {1,D}
3   R!H 0       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x112",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H 1       {1,D}
3   R!H 1       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x122",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H 1       {1,D}
3   R!H {2S,2T} {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x200",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H {2S,2T} {1,D}
3   R!H 0       {1,S}
4   R!H 0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x201",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H {2S,2T} {1,D}
3   R!H 0       {1,S}
4   R!H 1       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x211",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H {2S,2T} {1,D}
3   R!H 1       {1,S}
4   R!H 1       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x202",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H {2S,2T} {1,D}
3   R!H 0       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x212",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H {2S,2T} {1,D}
3   R!H 1       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCsR2x222",
    group = 
"""
1 * C   0       {2,D} {3,S} {4,S}
2   R!H {2S,2T} {1,D}
3   R!H {2S,2T} {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Ketonex00",
    group = 
"""
1 * C 0 {2,D} {3,S} {4,S}
2   O 0 {1,D}
3   C 0 {1,S}
4   C 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Ketonex01",
    group = 
"""
1 * C 0 {2,D} {3,S} {4,S}
2   O 0 {1,D}
3   C 0 {1,S}
4   C 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Ketonex11",
    group = 
"""
1 * C 0 {2,D} {3,S} {4,S}
2   O 0 {1,D}
3   C 1 {1,S}
4   C 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Ketonex02",
    group = 
"""
1 * C 0       {2,D} {3,S} {4,S}
2   O 0       {1,D}
3   C 0       {1,S}
4   C {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Ketonex12",
    group = 
"""
1 * C 0       {2,D} {3,S} {4,S}
2   O 0       {1,D}
3   C 1       {1,S}
4   C {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Ketonex22",
    group = 
"""
1 * C 0       {2,D} {3,S} {4,S}
2   O 0       {1,D}
3   C {2S,2T} {1,S}
4   C {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x0000",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
5   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x1111",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 1 {1,S}
3   R!H 1 {1,S}
4   R!H 1 {1,S}
5   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x2222",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   R!H {2S,2T} {1,S}
5   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x0001",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
5   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x0002",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 0       {1,S}
3   R!H 0       {1,S}
4   R!H 0       {1,S}
5   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x1110",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 1 {1,S}
3   R!H 1 {1,S}
4   R!H 1 {1,S}
5   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x1112",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 1       {1,S}
3   R!H 1       {1,S}
4   R!H 1       {1,S}
5   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x2220",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   R!H {2S,2T} {1,S}
5   R!H 0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x2221",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   R!H {2S,2T} {1,S}
5   R!H 1       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x0011",
    group = 
"""
1 * C   0 {2,S} {3,S} {4,S} {5,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 1 {1,S}
5   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x0022",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 0       {1,S}
3   R!H 0       {1,S}
4   R!H {2S,2T} {1,S}
5   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x1122",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 1       {1,S}
3   R!H 1       {1,S}
4   R!H {2S,2T} {1,S}
5   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x0012",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 0       {1,S}
3   R!H 0       {1,S}
4   R!H 1       {1,S}
5   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x0112",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 0       {1,S}
3   R!H 1       {1,S}
4   R!H 1       {1,S}
5   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCsR3x0122",
    group = 
"""
1 * C   0       {2,S} {3,S} {4,S} {5,S}
2   R!H 0       {1,S}
3   R!H 1       {1,S}
4   R!H {2S,2T} {1,S}
5   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH2rx0",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH2rx1",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 1 {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCH2rx2",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H {2S,2T} {1,S}
3   H   0       {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCHrx0",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   R!H 0 {1,D}
3   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCHrx1",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   R!H 1 {1,D}
3   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCHrx2",
    group = 
"""
1 * C   1       {2,D} {3,S}
2   R!H {2S,2T} {1,D}
3   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCrx0",
    group = 
"""
1 * C 1 {2,T}
2   C 0 {1,T}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CtCrx1",
    group = 
"""
1 * C 1 {2,T}
2   C 1 {1,T}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrsRx00",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrsRx01",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   R!H 1 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrsRx11",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 1 {1,S}
3   R!H 1 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrsRx02",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H 0       {1,S}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrsRx12",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H 1       {1,S}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrsRx22",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "OdCrsRx0",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   O   0 {1,D}
3   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "OdCrsRx1",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   O   0 {1,D}
3   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "OdCrsRx2",
    group = 
"""
1 * C   1       {2,D} {3,S}
2   O   0       {1,D}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCrsRx00",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   C   0 {1,D}
3   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCrsRx01",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   C   0 {1,D}
3   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCrsRx10",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   C   1 {1,D}
3   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCrsRx11",
    group = 
"""
1 * C   1 {2,D} {3,S}
2   C   1 {1,D}
3   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCrsRx02",
    group = 
"""
1 * C   1       {2,D} {3,S}
2   C   0       {1,D}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCrsRx20",
    group = 
"""
1 * C   1       {2,D} {3,S}
2   C   {2S,2T} {1,D}
3   R!H 0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCrsRx12",
    group = 
"""
1 * C   1       {2,D} {3,S}
2   C   1       {1,D}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCrsRx21",
    group = 
"""
1 * C   1       {2,D} {3,S}
2   C   {2S,2T} {1,D}
3   R!H 1       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "CdCrsRx22",
    group = 
"""
1 * C   1       {2,D} {3,S}
2   C   {2S,2T} {1,D}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x000",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x111",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 1 {1,S}
3   R!H 1 {1,S}
4   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x222",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x001",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 0 {1,S}
3   R!H 0 {1,S}
4   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x002",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H 0       {1,S}
3   R!H 0       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x110",
    group = 
"""
1 * C   1 {2,S} {3,S} {4,S}
2   R!H 1 {1,S}
3   R!H 1 {1,S}
4   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x112",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H 1       {1,S}
3   R!H 1       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x220",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   R!H 0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x221",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
4   R!H 1       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrsR2x012",
    group = 
"""
1 * C   1       {2,S} {3,S} {4,S}
2   R!H 0       {1,S}
3   R!H 1       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrrx0",
    group = 
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H 0       {1,S}
3   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrrx1",
    group = 
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H 1       {1,S}
3   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCHrrx2",
    group = 
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H {2S,2T} {1,S}
3   H   0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCrrx0",
    group = 
"""
1 * C   {2S,2T} {2,D}
2   R!H 0       {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCrrx1",
    group = 
"""
1 * C   {2S,2T} {2,D}
2   R!H 1       {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RdCrrx2",
    group = 
"""
1 * C   {2S,2T} {2,D}
2   R!H {2S,2T} {1,D}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrrsRx00",
    group = 
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H 0       {1,S}
3   R!H 0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrrsRx01",
    group = 
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H 0       {1,S}
3   R!H 1       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrrsRx11",
    group = 
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H 1       {1,S}
3   R!H 1       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrrsRx02",
    group = 
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H 0       {1,S}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrrsRx12",
    group = 
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H 1       {1,S}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "RsCrrsRx22",
    group = 
"""
1 * C   {2S,2T} {2,S} {3,S}
2   R!H {2S,2T} {1,S}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Alcoholx0",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 0 {1,S}
3   H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Alcoholx1",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 1 {1,S}
3   H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Alcoholx2",
    group = 
"""
1 * O 0       {2,S} {3,S}
2   C {2S,2T} {1,S}
3   H 0       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Etherx00",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 0 {1,S}
3   C 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Etherx01",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 0 {1,S}
3   C 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Etherx11",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 1 {1,S}
3   C 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Etherx02",
    group = 
"""
1 * O 0       {2,S} {3,S}
2   C 0       {1,S}
3   C {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Etherx12",
    group = 
"""
1 * O 0       {2,S} {3,S}
2   C 1       {1,S}
3   C {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Etherx22",
    group = 
"""
1 * O 0       {2,S} {3,S}
2   C {2S,2T} {1,S}
3   C {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "ROOHx0",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 0 {1,S}
3   O 0 {1,S} {4,S}
4   H 0 {3,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "ROOHx1",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 1 {1,S}
3   O 0 {1,S} {4,S}
4   H 0 {3,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "ROOHx2",
    group = 
"""
1 * O 0       {2,S} {3,S}
2   C {2S,2T} {1,S}
3   O 0       {1,S} {4,S}
4   H 0       {3,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "ROORx00",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 0 {1,S}
3   O 0 {1,S} {4,S}
4   C 0 {3,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "ROORx01",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 0 {1,S}
3   O 0 {1,S} {4,S}
4   C 1 {3,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "ROORx11",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 1 {1,S}
3   O 0 {1,S} {4,S}
4   C 1 {3,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "ROORx02",
    group = 
"""
1 * O 0       {2,S} {3,S}
2   C 0       {1,S}
3   O 0       {1,S} {4,S}
4   C {2S,2T} {3,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "ROORx12",
    group = 
"""
1 * O 0       {2,S} {3,S}
2   C 1       {1,S}
3   O 0       {1,S} {4,S}
4   C {2S,2T} {3,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "ROORx22",
    group = 
"""
1 * O 0       {2,S} {3,S}
2   C {2S,2T} {1,S}
3   O 0       {1,S} {4,S}
4   C {2S,2T} {3,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Peroxyx0",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 0 {1,S}
3   O 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Peroxyx1",
    group = 
"""
1 * O 0 {2,S} {3,S}
2   C 1 {1,S}
3   O 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Peroxyx2",
    group = 
"""
1 * O 0       {2,S} {3,S}
2   C {2S,2T} {1,S}
3   O 1       {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Oxyx0",
    group = 
"""
1 * O 1 {2,S}
2   C 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Oxyx1",
    group = 
"""
1 * O 1 {2,S}
2   C 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Oxyx2",
    group = 
"""
1 * O 1       {2,S}
2   C {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)




















entry(
    index = -1,
    label = "N_R0",
    group = 
"""
1 * N 0
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 25,
    label = "Amide_pri",
    group = "OR{Amide_prix0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3480, 3540, 1), # asymmetric N-H stretch, (free) primary amides
            (3380, 3420, 1), # symmetric N-H stretch, (free) primary amides
            (1670, 1690, 1), # C=O stretch, known as amide I band, primary amides (dilute solution)
            (1590, 1620, 1), # , primary amides (dilute solution)
            (1400, 1420, 1), # C-N stretch, known as amide III band, primary amides
            (1140, 1160, 1), # NH2 in-plane rocking vibration, primary amides
            (600, 750, 1),   # br. NH2 deformation vibration, primary amides
            (550, 600, 1),   # N-C=O deformation vibration, primary amides
            (450, 500, 1),   # C-C=O deformation vibration, primary amides
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
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
    index = -1,
    label = "Amide_prix0",
    group = 
"""
1 * N   0 {2,S} {5,S} {6,S}
2   C   0 {1,S} {3,S} {4,D}
3   C   0 {2,S}
4   O   0 {2,D}
5   H   0 {1,S}
6   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 26,
    label = "Amide_sec",
    group = "OR{Amide_secx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3420, 3460, 1), # N-H stretch, trans form (in dilute solution)
            (1510, 1550, 1), # amide II band, trans form (in dilute solution)
            (1665, 1700, 1), # C=O stretch, secondary amides (dilute solution)
            (1200, 1305, 1), # amide III band, secondary amides (trans form)
            (620, 770, 1),   # br. out-of-plane N-H, secondary amides (trans form)
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3420, 3460, 1), # N-H stretch, trans form (in dilute solution)
(1510, 1550, 1), # amide II band, trans form (in dilute solution)
(1665, 1700, 1), # C=O stretch, secondary amides (dilute solution)
(1200, 1305, 1), # amide III band, secondary amides (trans form)
(620, 770, 1),   # br. out-of-plane N-H, secondary amides (trans form)
""",
)

entry(
    index = -1,
    label = "Amide_secx0",
    group = 
"""
1 * N   0 {2,S} {5,S} {6,S}
2   C   0 {1,S} {3,S} {4,D}
3   C   0 {2,S}
4   O   0 {2,D}
5   C   0 {1,S}
6   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 27,
    label = "Amide_ter",
    group = "OR{Amide_terx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (1630, 1670, 1), # C=O stretch, tertiary amides (dilute solution or solid phase)
            (700, 870, 1), # asymmetric CNC stretch, tertiary amides
            (570, 620, 1), # , tertiary amides
            (440, 480, 1), # , tertiary amides
            (320, 390, 1), # , tertiary amides
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(1630, 1670, 1), # C=O stretch, tertiary amides (dilute solution or solid phase)
(700, 870, 1), # asymmetric CNC stretch, tertiary amides
(570, 620, 1), # , tertiary amides
(440, 480, 1), # , tertiary amides
(320, 390, 1), # , tertiary amides
""",
)

entry(
    index = -1,
    label = "Amide_terx0",
    group = 
"""
1 * N   0 {2,S} {5,S} {6,S}
2   C   0 {1,S} {3,S} {4,D}
3   C   0 {2,S}
4   O   0 {2,D}
5   C   0 {1,S}
6   C   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 28,
    label = "Imide",
    group = "OR{Imidex0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3200, 3280, 1), # N-H stretch, Imides (solid phase)
            (1670, 1740, 1), # C=O stretch, amide I band, Imides (solid phase)
            (1500, 1510, 1), # br., amide II band, Imides (solid phase)
            (1165, 1235, 1), # amide III band, Imides (solid phase)
            (730, 740, 1),   # br. N-H wagging, amide II band, Imides (solid phase)
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3200, 3280, 1), # N-H stretch, Imides (solid phase)
(1670, 1740, 1), # C=O stretch, amide I band, Imides (solid phase)
(1500, 1510, 1), # br., amide II band, Imides (solid phase)
(1165, 1235, 1), # amide III band, Imides (solid phase)
(730, 740, 1),   # br. N-H wagging, amide II band, Imides (solid phase)
""",
)

entry(
    index = -1,
    label = "Imidex0",
    group = 
"""
1 * N   0 {2,S} {3,S} {6,S}
2   H   0 {1,S}
3   C   0 {1,S} {4,D} {5,S}
4   O   0 {3,D}
5   R   0 {3,S}
6   C   0 {1,S} {7,D} {8,S}
7   O   0 {6,D}
8   R   0 {6,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 29,
    label = "Amine_pri",
    group = "OR{Amine_prix0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3330, 3550, 1), # asymmetric NH2 stretch, primary amines
            (3250, 3450, 1), # symmetric NH2 stretch, primary amines
            (1580, 1650, 1), # br. scissor vibration, saturated primary amines
            (1145, 1295, 1), # NH2 rocking/twisting vibration, saturated primary amines
            (650, 895, 1), # N-H bending out of plane, saturated primary amines
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3330, 3550, 1), # asymmetric NH2 stretch, primary amines
(3250, 3450, 1), # symmetric NH2 stretch, primary amines
(1580, 1650, 1), # br. scissor vibration, saturated primary amines
(1145, 1295, 1), # NH2 rocking/twisting vibration, saturated primary amines
(650, 895, 1), # N-H bending out of plane, saturated primary amines
""",
)

entry(
    index = -1,
    label = "Amine_prix0",
    group = 
"""
1 * N   0 {2,S} {3,S} {4,S}
2   C   0 {1,S}
3   H   0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 30,
    label = "Amine_sec",
    group = "OR{Amine_secx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3400, 3450, 1), # , secondary amines
            (1490, 1580, 1), # , secondary amines
            (700, 750, 1), # br. N-H wagging vibration, secondary amines
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3400, 3450, 1), # , secondary amines
(1490, 1580, 1), # , secondary amines
(700, 750, 1), # br. N-H wagging vibration, secondary amines
""",
)

entry(
    index = -1,
    label = "Amine_secx0",
    group = 
"""
1 * N   0 {2,S} {3,S} {4,S}
2   C   0 {1,S}
3   C   0 {1,S}
4   H   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 31,
    label = "Amine_ter",
    group = "OR{Amine_terx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (1020, 1250, 2),
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Amine_terx0",
    group = 
"""
1 * N   0 {2,S} {3,S} {4,S}
2   C   0 {1,S}
3   C   0 {1,S}
4   C   0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 32,
    label = "Nitrile",
    group = "OR{Nitrilex0}",
    statmech = GroupFrequencies(
        frequencies = [
            (2230, 2260, 1), # C#N stretching, saturated aliphatic nitriles
            (340, 390, 1),   # C#N deformation, aliphatic nitriles
            (200, 160, 1),   # C#N deformation, aliphatic nitriles
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(2230, 2260, 1), # C#N stretching, saturated aliphatic nitriles
(340, 390, 1),   # C#N deformation, aliphatic nitriles
(200, 160, 1),   # C#N deformation, aliphatic nitriles
""",
)

entry(
    index = -1,
    label = "Nitrilex0",
    group = 
"""
1 * N   0 {2,T}
2   C   0 {1,T} {3,S}
3   C   0 {2,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Nitrilex1",
    group = 
"""
1 * N   0 {2,T}
2   C   0 {1,T} {3,S}
3   C   1 {2,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Nitrilex2",
    group = 
"""
1 * N   0       {2,T}
2   C   0       {1,T} {3,S}
3   C   {2S,2T} {2,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 33,
    label = "Nitroso",
    group = "OR{Nitrosox0, Nitrosox1, Nitrosox2}",
    statmech = GroupFrequencies(
        frequencies = [
            (1330, 1425, 1), # aliphatic compounds
            (1320, 1345, 1), # aliphatic compounds
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(1330, 1425, 1), # aliphatic compounds
(1320, 1345, 1), # aliphatic compounds
""",
)

entry(
    index = -1,
    label = "Nitrosox0",
    group = 
"""
1 * N   0 {2,D} {3,S}
2   O   0 {1,D}
3   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Nitrosox1",
    group = 
"""
1 * N   0 {2,D} {3,S}
2   O   0 {1,D}
3   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Nitrosox2",
    group = 
"""
1 * N   0       {2,D} {3,S}
2   O   0       {1,D}
3   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 34,
    label = "Nitrites",
    group = "OR{Nitritesx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (3220, 3360, 1), # Overtones of N=O stretch, nitrite compounds
            (1650, 1680, 1), # N=O stretch, nitrites, trans form
            (750, 815, 1),   # N-O stretch trans form, saturated primary and secondary aliphatic nitro compounds
            (565, 625, 1),   # O-N=O deformation vibration, saturated primary and secondary aliphatic nitro compounds
        ],
        symmetry = 1,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(3220, 3360, 1), # Overtones of N=O stretch, nitrite compounds
(1650, 1680, 1), # N=O stretch, nitrites, trans form
(750, 815, 1),   # N-O stretch trans form, saturated primary and secondary aliphatic nitro compounds
(565, 625, 1),   # O-N=O deformation vibration, saturated primary and secondary aliphatic nitro compounds
""",
)

entry(
    index = -1,
    label = "Nitritesx0",
    group = 
"""
1 * N 0 {2,D} {3,S}
2   O 0 {1,D}
3   O 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 35,
    label = "Nitro",
    group = "OR{Nitrox0, Nitrox1, Nitrox2}",
    statmech = GroupFrequencies(
        frequencies = [
            (1545, 1555, 1), # asymmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
            (1360, 1385, 1), # symmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
            (915, 1000, 1),  # C-N stretch trans form, saturated primary and secondary aliphatic nitro compounds
            (850, 920, 1),  # br. C-N stretch gauche form, saturated primary and secondary aliphatic nitro compounds
            (605, 655, 1),  # NO2 deformation vibration, saturated primary and secondary aliphatic nitro compounds
            (470, 560, 1),  # NO2 rocking vibration, saturated primary and secondary aliphatic nitro compounds
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""  
(1545, 1555, 1), # asymmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
(1360, 1385, 1), # symmetric NO2 stretch, saturated primary and secondary aliphatic nitro compounds
(915, 1000, 1),  # C-N stretch trans form, saturated primary and secondary aliphatic nitro compounds
(850, 920, 1),  # br. C-N stretch gauche form, saturated primary and secondary aliphatic nitro compounds
(605, 655, 1),  # NO2 deformation vibration, saturated primary and secondary aliphatic nitro compounds
(470, 560, 1),  # NO2 rocking vibration, saturated primary and secondary aliphatic nitro compounds
""",
)

entry(
    index = -1,
    label = "Nitrox0",
    group = 
"""
1 * N   0 {2,D} {3,S} {4,S}
2   O   0 {1,D}
3   O   0 {1,S}
4   R!H 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Nitrox1",
    group = 
"""
1 * N   0 {2,D} {3,S} {4,S}
2   O   0 {1,D}
3   O   0 {1,S}
4   R!H 1 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = -1,
    label = "Nitrox2",
    group = 
"""
1 * N   0       {2,D} {3,S} {4,S}
2   O   0       {1,D}
3   O   0       {1,S}
4   R!H {2S,2T} {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

entry(
    index = 36,
    label = "Nitrates",
    group = "OR{Nitratesx0}",
    statmech = GroupFrequencies(
        frequencies = [
            (1615, 1660, 1), # asymmetric NO2 stretch, Nitrates, -ONO2
            (1250, 1300, 1), # symmetric NO2 stretch, Nitrates, -ONO2
            (840, 870, 1),   # br.N-O stretch, Nitrates, -ONO2
            (745, 765, 1),   # NO2 out-of-plane deformation vibration, Nitrates, -ONO2
            (680, 720, 1),   # NO2 deformation vibration, Nitrates, -ONO2
            (560, 610, 1),   # NO2 in-plane deformation vibration, Nitrates, -ONO2
        ],
        symmetry = 2,
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(1615, 1660, 1), # asymmetric NO2 stretch, Nitrates, -ONO2
(1250, 1300, 1), # symmetric NO2 stretch, Nitrates, -ONO2
(840, 870, 1),   # br.N-O stretch, Nitrates, -ONO2
(745, 765, 1),   # NO2 out-of-plane deformation vibration, Nitrates, -ONO2
(680, 720, 1),   # NO2 deformation vibration, Nitrates, -ONO2
(560, 610, 1),   # NO2 in-plane deformation vibration, Nitrates, -ONO2
""",
)

entry(
    index = -1,
    label = "Nitratesx0",
    group = 
"""
1 * N 0 {2,D} {3,S} {4,S}
2   O 0 {1,D}
3   O 0 {1,S}
4   O 0 {1,S}
""",
    statmech = None,
    shortDesc = u"""""",
    longDesc = 
u"""


""",
)

tree(
"""
L1: R!H
    L2: C_R0
        L3: RsCH3
        L3: RdCH2
        L3: CtCH
        L3: RsCH2sR
        L3: Aldehyde
        L3: Ketene
        L3: Cumulene
        L3: CdCHsR
        L3: CtCsR
        L3: RsCHsR2
        L3: RdCsR2
            L4: Ketone
        L3: RsCsR3
    L2: C_R1
        L3: RsCH2r
        L3: RdCHr
        L3: CtCr
        L3: RsCHrsR
        L3: OdCrsR
        L3: CdCrsR
        L3: RsCrsR2
    L2: C_R2
        L3: RsCHrr
        L3: RdCrr
        L3: RsCrrsR
    L2: O_R0
        L3: Alcohol
        L3: Ether
        L3: ROOH
        L3: ROOR
        L3: Peroxy
    L2: O_R1
        L3: Oxy
    L2: N_R0
        L3: Amide_pri
        L3: Amide_sec
        L3: Amide_ter
        L3: Imide
        L3: Amine_pri
        L3: Amine_sec
        L3: Amine_ter
        L3: Nitrile
        L3: Nitroso
            L4: Nitrites
        L3: Nitro
            L4: Nitrates
"""
)

