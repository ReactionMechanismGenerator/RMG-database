#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Cds-HH_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (20900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2,
    label = "Cds-HH_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 3,
    label = "Cds-HH_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 4,
    label = "Cds-HH_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 5,
    label = "Cds-HH_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (22100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 6,
    label = "Cds-HH_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 7,
    label = "Cds-HH_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (497, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 8,
    label = "Cds-HH_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (7750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 9,
    label = "Cds-HH_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2650, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 10,
    label = "Cds-HH_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (10200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 11,
    label = "Cds-HH_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2520, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 12,
    label = "Cds-HH_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (403, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 13,
    label = "Cds-HH_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (9460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 14,
    label = "Cds-HH_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 15,
    label = "Cds-HH_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (544, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 16,
    label = "Cds-HH_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (14300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 17,
    label = "Cds-HH_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (7590, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 18,
    label = "Cds-HH_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (22600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 19,
    label = "Cds-HH_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (21000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 20,
    label = "Cds-HH_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 21,
    label = "Cds-HH_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1710, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 22,
    label = "Cds-HH_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 23,
    label = "Cds-HH_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (22200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 24,
    label = "Cds-HH_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 25,
    label = "Cds-HH_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (499, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 26,
    label = "Cds-HH_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (7780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 27,
    label = "Cds-HH_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 28,
    label = "Cds-HH_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (10300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 29,
    label = "Cds-HH_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 30,
    label = "Cds-HH_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (404, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 31,
    label = "Cds-HH_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (9500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 32,
    label = "Cds-HH_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 33,
    label = "Cds-HH_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (546, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 34,
    label = "Cds-HH_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (14400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 35,
    label = "Cds-HH_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (7620, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 36,
    label = "Cds-HH_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (22700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 37,
    label = "Cds-HH_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (26400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 38,
    label = "Cds-HH_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 39,
    label = "Cds-HH_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (2150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 40,
    label = "Cds-HH_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1590, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 41,
    label = "Cds-HH_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (27900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 42,
    label = "Cds-HH_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (4860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 43,
    label = "Cds-HH_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (628, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 44,
    label = "Cds-HH_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (9790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 45,
    label = "Cds-HH_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (3340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 46,
    label = "Cds-HH_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (12900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 47,
    label = "Cds-HH_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (3180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 48,
    label = "Cds-HH_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (509, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 49,
    label = "Cds-HH_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (12000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 50,
    label = "Cds-HH_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2690, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 51,
    label = "Cds-HH_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (687, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 52,
    label = "Cds-HH_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (18100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 53,
    label = "Cds-HH_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (9580, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 54,
    label = "Cds-HH_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (28600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 55,
    label = "Cds-HH_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (23600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 56,
    label = "Cds-HH_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 57,
    label = "Cds-HH_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 58,
    label = "Cds-HH_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 59,
    label = "Cds-HH_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (24900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 60,
    label = "Cds-HH_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (4330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 61,
    label = "Cds-HH_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (561, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 62,
    label = "Cds-HH_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (8740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 63,
    label = "Cds-HH_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 64,
    label = "Cds-HH_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (11500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 65,
    label = "Cds-HH_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 66,
    label = "Cds-HH_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (454, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 67,
    label = "Cds-HH_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (10700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 68,
    label = "Cds-HH_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 69,
    label = "Cds-HH_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (614, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 70,
    label = "Cds-HH_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2.45e+2, 'cm^3/(mol*s)'),
        n = 3.08,
        alpha = 0,
        E0 = (1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte.  Update BMK/6-311G(2d,d,p) Eckart no HR.""",
)

entry(
    index = 71,
    label = "Cds-HH_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (8550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 72,
    label = "Cds-HH_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (25500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-3.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 73,
    label = "Cds-HH_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (26800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 74,
    label = "Cds-HH_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 75,
    label = "Cds-HH_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (2180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 76,
    label = "Cds-HH_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 77,
    label = "Cds-HH_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (28200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 78,
    label = "Cds-HH_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (4920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 79,
    label = "Cds-HH_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (636, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 80,
    label = "Cds-HH_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (9920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 81,
    label = "Cds-HH_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (3390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 82,
    label = "Cds-HH_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (13100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 83,
    label = "Cds-HH_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (3220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 84,
    label = "Cds-HH_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (515, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 85,
    label = "Cds-HH_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (12100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 86,
    label = "Cds-HH_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2730, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 87,
    label = "Cds-HH_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (696, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 88,
    label = "Cds-HH_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (18300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 89,
    label = "Cds-HH_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (9710, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 90,
    label = "Cds-HH_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (28900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-4.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 91,
    label = "Cds-HH_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (81600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 92,
    label = "Cds-HH_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (8280, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 93,
    label = "Cds-HH_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (6640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 94,
    label = "Cds-HH_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (4920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 95,
    label = "Cds-HH_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (86100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 96,
    label = "Cds-HH_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (15000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 97,
    label = "Cds-HH_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (1940, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 98,
    label = "Cds-HH_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (30200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 99,
    label = "Cds-HH_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (10300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 100,
    label = "Cds-HH_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (39900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 101,
    label = "Cds-HH_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (9820, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 102,
    label = "Cds-HH_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (1570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 103,
    label = "Cds-HH_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (36900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 104,
    label = "Cds-HH_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (8320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 105,
    label = "Cds-HH_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (2120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 106,
    label = "Cds-HH_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (55800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 107,
    label = "Cds-HH_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (29600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 108,
    label = "Cds-HH_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (88100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-5.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 109,
    label = "Cds-HH_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 110,
    label = "Cds-HH_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (782, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 111,
    label = "Cds-HH_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (627, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 112,
    label = "Cds-HH_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (464, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 113,
    label = "Cds-HH_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (8120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 114,
    label = "Cds-HH_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1410, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 115,
    label = "Cds-HH_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (183, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 116,
    label = "Cds-HH_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 117,
    label = "Cds-HH_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (974, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 118,
    label = "Cds-HH_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 119,
    label = "Cds-HH_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (926, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 120,
    label = "Cds-HH_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (148, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 121,
    label = "Cds-HH_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 122,
    label = "Cds-HH_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (785, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 123,
    label = "Cds-HH_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 124,
    label = "Cds-HH_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (5270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 125,
    label = "Cds-HH_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 126,
    label = "Cds-HH_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (8320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 127,
    label = "Cds-HH_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (16300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 128,
    label = "Cds-HH_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 129,
    label = "Cds-HH_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 130,
    label = "Cds-HH_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (985, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 131,
    label = "Cds-HH_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (17200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 132,
    label = "Cds-HH_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 133,
    label = "Cds-HH_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (388, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 134,
    label = "Cds-HH_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (6050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 135,
    label = "Cds-HH_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 136,
    label = "Cds-HH_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 137,
    label = "Cds-HH_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1960, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 138,
    label = "Cds-HH_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (314, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 139,
    label = "Cds-HH_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (7380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 140,
    label = "Cds-HH_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 141,
    label = "Cds-HH_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (425, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 142,
    label = "Cds-HH_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (11200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 143,
    label = "Cds-HH_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 144,
    label = "Cds-HH_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (17600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 145,
    label = "Cds-HH_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (30600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 146,
    label = "Cds-HH_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (3100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 147,
    label = "Cds-HH_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (2490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 148,
    label = "Cds-HH_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 149,
    label = "Cds-HH_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (32300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 150,
    label = "Cds-HH_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (5620, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 151,
    label = "Cds-HH_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (727, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 152,
    label = "Cds-HH_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (11300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 153,
    label = "Cds-HH_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (3870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 154,
    label = "Cds-HH_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (15000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 155,
    label = "Cds-HH_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (3680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 156,
    label = "Cds-HH_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (589, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 157,
    label = "Cds-HH_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (13800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 158,
    label = "Cds-HH_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (3120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 159,
    label = "Cds-HH_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (795, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 160,
    label = "Cds-HH_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (20900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 161,
    label = "Cds-HH_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (11100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 162,
    label = "Cds-HH_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (33000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-3.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 163,
    label = "Cds-HH_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (31300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 164,
    label = "Cds-HH_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (3180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 165,
    label = "Cds-HH_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (2550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 166,
    label = "Cds-HH_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 167,
    label = "Cds-HH_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (33000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 168,
    label = "Cds-HH_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (5750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 169,
    label = "Cds-HH_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (744, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 170,
    label = "Cds-HH_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (11600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 171,
    label = "Cds-HH_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (3960, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 172,
    label = "Cds-HH_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (15300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 173,
    label = "Cds-HH_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (3770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 174,
    label = "Cds-HH_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (603, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 175,
    label = "Cds-HH_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (14200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 176,
    label = "Cds-HH_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (3190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 177,
    label = "Cds-HH_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (814, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 178,
    label = "Cds-HH_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (21400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 179,
    label = "Cds-HH_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (11400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 180,
    label = "Cds-HH_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (33800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-3.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 181,
    label = "Cds-HH_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (22600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 182,
    label = "Cds-HH_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 183,
    label = "Cds-HH_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 184,
    label = "Cds-HH_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 185,
    label = "Cds-HH_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (23800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 186,
    label = "Cds-HH_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (4150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 187,
    label = "Cds-HH_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (537, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 188,
    label = "Cds-HH_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (8370, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 189,
    label = "Cds-HH_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 190,
    label = "Cds-HH_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (11100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 191,
    label = "Cds-HH_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 192,
    label = "Cds-HH_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (435, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 193,
    label = "Cds-HH_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (10200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 194,
    label = "Cds-HH_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 195,
    label = "Cds-HH_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (588, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 196,
    label = "Cds-HH_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (15400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 197,
    label = "Cds-HH_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (8190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 198,
    label = "Cds-HH_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (24400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 199,
    label = "Cds-CsH_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (10000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 200,
    label = "Cds-CsH_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 201,
    label = "Cds-CsH_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (818, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 202,
    label = "Cds-CsH_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (606, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 203,
    label = "Cds-CsH_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (10600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 204,
    label = "Cds-CsH_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 205,
    label = "Cds-CsH_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (239, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 206,
    label = "Cds-CsH_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 207,
    label = "Cds-CsH_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 208,
    label = "Cds-CsH_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4910, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 209,
    label = "Cds-CsH_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 210,
    label = "Cds-CsH_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (193, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 211,
    label = "Cds-CsH_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 212,
    label = "Cds-CsH_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 213,
    label = "Cds-CsH_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (261, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 214,
    label = "Cds-CsH_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (6870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 215,
    label = "Cds-CsH_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 216,
    label = "Cds-CsH_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (10800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 217,
    label = "Cds-CsH_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (10100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 218,
    label = "Cds-CsH_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 219,
    label = "Cds-CsH_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (821, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 220,
    label = "Cds-CsH_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (608, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 221,
    label = "Cds-CsH_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (10600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 222,
    label = "Cds-CsH_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 223,
    label = "Cds-CsH_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 224,
    label = "Cds-CsH_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 225,
    label = "Cds-CsH_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1280, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 226,
    label = "Cds-CsH_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4930, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 227,
    label = "Cds-CsH_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 228,
    label = "Cds-CsH_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (194, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 229,
    label = "Cds-CsH_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 230,
    label = "Cds-CsH_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1030, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 231,
    label = "Cds-CsH_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (262, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 232,
    label = "Cds-CsH_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (6900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 233,
    label = "Cds-CsH_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 234,
    label = "Cds-CsH_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 235,
    label = "Cds-CsH_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (12700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 236,
    label = "Cds-CsH_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 237,
    label = "Cds-CsH_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1030, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 238,
    label = "Cds-CsH_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (765, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 239,
    label = "Cds-CsH_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (13400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 240,
    label = "Cds-CsH_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 241,
    label = "Cds-CsH_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (301, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 242,
    label = "Cds-CsH_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 243,
    label = "Cds-CsH_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 244,
    label = "Cds-CsH_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (6210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 245,
    label = "Cds-CsH_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 246,
    label = "Cds-CsH_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (244, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 247,
    label = "Cds-CsH_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (5740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 248,
    label = "Cds-CsH_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 249,
    label = "Cds-CsH_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 250,
    label = "Cds-CsH_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (8680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 251,
    label = "Cds-CsH_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (4600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 252,
    label = "Cds-CsH_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (13700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 253,
    label = "Cds-CsH_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (11300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 254,
    label = "Cds-CsH_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 255,
    label = "Cds-CsH_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (922, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 256,
    label = "Cds-CsH_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (683, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 257,
    label = "Cds-CsH_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (11900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 258,
    label = "Cds-CsH_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 259,
    label = "Cds-CsH_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (269, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 260,
    label = "Cds-CsH_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 261,
    label = "Cds-CsH_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 262,
    label = "Cds-CsH_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (5540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 263,
    label = "Cds-CsH_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 264,
    label = "Cds-CsH_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (218, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 265,
    label = "Cds-CsH_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (5120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 266,
    label = "Cds-CsH_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 267,
    label = "Cds-CsH_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (295, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 268,
    label = "Cds-CsH_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (7740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 269,
    label = "Cds-CsH_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (4110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 270,
    label = "Cds-CsH_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (12200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 271,
    label = "Cds-CsH_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (12800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 272,
    label = "Cds-CsH_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 273,
    label = "Cds-CsH_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 274,
    label = "Cds-CsH_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (775, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 275,
    label = "Cds-CsH_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (13600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 276,
    label = "Cds-CsH_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 277,
    label = "Cds-CsH_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (305, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 278,
    label = "Cds-CsH_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 279,
    label = "Cds-CsH_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 280,
    label = "Cds-CsH_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (6290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 281,
    label = "Cds-CsH_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
)

entry(
    index = 282,
    label = "Cds-CsH_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (247, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
)

entry(
    index = 283,
    label = "Cds-CsH_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (5810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
)

entry(
    index = 284,
    label = "Cds-CsH_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1310, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
)

entry(
    index = 285,
    label = "Cds-CsH_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (334, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
)

entry(
    index = 286,
    label = "Cds-CsH_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (8790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 3. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
)

entry(
    index = 287,
    label = "Cds-CsH_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (4660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 20. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
)

entry(
    index = 288,
    label = "Cds-CsH_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (13900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 20. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
)

entry(
    index = 289,
    label = "Cds-CsH_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (39100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
in his reaction type 20. Based on the recommendations of
[146] Allara, D.L.; Shaw, R. J Phys. Chem. Ref. Data 1980,9,523.
""",
)

entry(
    index = 290,
    label = "Cds-CsH_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (3980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[94] Baulch,D.L.; Cobos,C.J.;Cox,R.A;Frank,P.;Hayman,G.;Just,T.;Kerr,J.A.;Murells,T.;Philling,M.J.;Troe,J.;Walker,R.W.; Warnatz, J. J Phys Chem. Ref. Data 1994,23,847.
literature review. C2H4 + H --> C2H5. C.D.W. divided rate expression by 2, to get rate of addition per site 
pg.916-920: Discussion on evaluated data

H+C2H4(+m) --> C2H5(+m): "The analysis of the rxn is based on theoretical fall-off

curves and strong collision low pressure rate coefficients which were calculated
using a rxn threshold of 154.78 kJ/mol."  The rate coefficient stored in RMG
is the high-pressure limit, k_inf.
MRH 31-Aug-2009
""",
)

entry(
    index = 291,
    label = "Cds-CsH_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (3190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[89] Tsang, W.; Hampson, R.F. J. Phys. Chem. Ref. Data 1986, 15, 1087. 
literature review. C2H4 + CH3 --> n-C3H7. C.D.W. divided rate expression by 2, to get rate of addition per site
pg. 1191: Discussion on evaluated data

Entry 18,16 (b)

Recommended data is from other Review paper by Kerr and Parsonage (1972)

MRH 28-Aug-2009
""",
)

entry(
    index = 292,
    label = "Cds-CsH_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (2360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[147] Knyazev,V.D.;Slagle,I.R. J Phys. Chem. 1996 100, 5318.
Pressure up to 10 atm. Excitation; thermal, analysis: mass spectrometry. C2H4 + C2H5--> n-C4H9. C.D.W. divided rate expression by 2, to get rate of addtion per site
""",
)

entry(
    index = 293,
    label = "Cds-CsH_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (41300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[90] Tsang,W.J. Phys. Chem. Ref. Data 1987,16,471.
literature review. C2H4+ CH2OH --> CH2CH2CH2OH C.D.W. divided rate expression by 2, to get rate of addition per site
pg. 502: Discussion on evaluated data

Entry 39,18 (a): No data available at the time.  Author suggests rate coefficient expression

of 8.0x10^-14 * exp(-3500/T) cm3/molecule/s noting rates of alkyl radical addition
to ethylene are similar (Kerr, J.A., Trotman-Dickenson, A.F.)
MRH 30-Aug-2009
""",
)

entry(
    index = 294,
    label = "Cds-CsH_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (7200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[148] Weissman and Benson. Estimated values. Activation energy is a lower limit. Pressure 1.00 atm. 
C2H4 + C2H3 --> CH2=CHCH2CH2 C.D.W. divided rate expression by 2, to get rate of addition per site
""",
)

entry(
    index = 295,
    label = "Cds-CsH_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (931, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[89] Tsang et al. Literature Review.  
C2H4 + OH --> CH2CH2OH  C.D.W. divided rate expression by 2, to get rate of addition per site

pg. 1189: Discussion on evaluated data (in theory)

Online reference does not have pages 1188-1189; pages 1198-1199 come between
pages 1187&1190 and between 1197&1200
Following discussion is only based on table (pg. 1097) that summarizes all evaluated

data in the reference
Entry 18,6 (b)

Table states rxn is pressure-dependent: C2H4+OH(+M)=C2H4OH(+M)

Only data available in table is k=9.0x10^-12
MRH 28-Aug-2009
""",
)

entry(
    index = 296,
    label = "Cds-CsH_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (14500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[149] Tsang experiments and limited review. CH3CH=CH2 + H --> iso-C3H7
""",
)

entry(
    index = 297,
    label = "Cds-CsH_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (4950, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[150] Knayzev et al. Data derived from fitting to a complex mechanism. Pressure up to 10 atm. Excitation : flash photolysis, analysis : mass spectrometry
CH3CH=CH2 + CH3 --> sec-C4H9
""",
)

entry(
    index = 298,
    label = "Cds-CsH_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (19200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[93] Tsang literature review. CH3CH=CH2 + CH3 --> sec-C4H9 
pg.237-239: Discussion on evaluated data

Entry 46,16(a): Recommended rate coefficient is that reported by Kerr and Parsonage (1972).

Author notes that rxn is pressure dependent and lists fall-off ratios and
collision efficiencies; these are not stored in RMG.
MRH 31-Aug-2009
""",
)

entry(
    index = 299,
    label = "Cds-CsH_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (4710, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[151] Barbe et al. Data is estimated. Pressure 0.04-0.26 atm. CH3CH=CH2 + .CH2CH=CH2 --> CH3CH(.)CH2CH2CH=CH2
""",
)

entry(
    index = 300,
    label = "Cds-CsH_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (754, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[93] Tsang literature review. CH3CH=CH2 + tert-C4H9 --> (CH3)3CCH2CH(.)CH3
pg.247: Discussion on evaluated data

Entry 46,44(terminal): Recommended rate coefficient is based on summary of data on alkyl

radical addition to olefins (Kerr and Parsonage, 1972).
MRH 31-Aug-2009
""",
)

entry(
    index = 301,
    label = "Cds-CsH_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (17700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[152] Perrin et al. Data is estimated. Pressure 0.01-0.13 atm. 
CH2=CHCH=CH2 + .CH3 --> CH2CH=CHCH2CH3 C.D.W. divied rate expression by 2, to get rate of addition per site.
""",
)

entry(
    index = 302,
    label = "Cds-CsH_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (3990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[153] Knayzev et al. Pressure ~ 0.01 atm. Excitation : thermal, analysis : GC Iso-C4H8 + CH3 --> (CH3)2CCH2CH3
""",
)

entry(
    index = 303,
    label = "Cds-CsH_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (1020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[303] Seres et al. Data derived from fitting to a complex mechanism. Excitation : thermal, analysis : GC Iso-C4H8 + CH3 --> (CH3)2CCH2CH3
""",
)

entry(
    index = 304,
    label = "Cds-CsH_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (26800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[149] Tsang experiments and limited review. CH3CH=CH2 + H --> n-C3H7
""",
)

entry(
    index = 305,
    label = "Cds-CsH_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (14200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[147] Knyazev et al. Pressure up to 10 atm. Excitation : thermal, analysis : mass spectrometry. 
CH3CH=CH2 + CH3 --> iso-C4H9
""",
)

entry(
    index = 306,
    label = "Cds-CsH_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (42300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-3.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[93] literature review. CH3CH=CH2 + CH3 --> iso-C4H9
pg.237-239: Discussion on evaluated data

Entry 46,16(b): Recommended rate coefficient is from reverse rate and equilibrium constant.

Author notes that rxn is pressure dependent and lists fall-off ratios and
collision efficiencies; these are not stored in RMG.
MRH 31-Aug-2009
""",
)

entry(
    index = 307,
    label = "Cds-CsH_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3690, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[155] Slagle et al. Data deriver from detailed balance/reverse rate. Pressure ~ 0.01 atm. 
Iso-C4H8 + .CH3 --> (CH3)3CCH2
""",
)

entry(
    index = 308,
    label = "Cds-CsH_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (375, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
)

entry(
    index = 309,
    label = "Cds-CsH_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (301, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
)

entry(
    index = 310,
    label = "Cds-CsH_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (223, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
)

entry(
    index = 311,
    label = "Cds-CsH_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (3900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
)

entry(
    index = 312,
    label = "Cds-CsH_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (679, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran et al. in his reaction type 3. Based on recommendations of Allara and Shaw. [146]
""",
)

entry(
    index = 313,
    label = "Cds-CsH_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (87.8, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 314,
    label = "Cds-CsH_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1370, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[156] Scherzer et al. Data derived from fitting to a complex mechanism. Pressure 0.04 atm. Excitation: thermal, analysis: GC.
CH2=C=CH2 + .CH3 --> CH3CH2C=CH2
""",
)

entry(
    index = 315,
    label = "Cds-CsH_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (467, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[157] Tsang et al. Absolute Value Measured directly. Pressure 2 - 7 atm. Excitation: thermal, analysis : GC. 
CH2=C=CH2 + H --> .CH2CH=CH2
""",
)

entry(
    index = 316,
    label = "Cds-CsH_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[158] Tsang. Data is estimated. Pressure 1.50-5.00 atm. CH2=C=CH2 + CH3 --> CH2C(CH3)=CH2
""",
)

entry(
    index = 317,
    label = "Cds-CsH_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (445, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran et al. In his reaction type 18.
""",
)

entry(
    index = 318,
    label = "Cds-CsH_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (71.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[8] Curran et al. In his reaction type 18.
""",
)

entry(
    index = 319,
    label = "Cds-CsH_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[144] Bozzelli et al. Based upon CH3 addition to CO (Anastasi and Maw)
""",
)

entry(
    index = 320,
    label = "Cds-CsH_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (377, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[159] Curran et al. His estimation in DME oxidation modeling for ketohydroperoxide decomposition. 
H2CO + HCO2. (formic acid radical) --> +  .OCH2OCHO (ester) (Rxn. 338, p. 234)

Verified by Greg Magoon; it is not immediately clear whether this rate constant is for high pressure limit, but based on other references to high pressure limit in the paper, I suspect that it is a high pressure limit value; also, note that CO_O group is used for H2CO...MRH and I have interpreted CO_O as referring to any carbonyl group
""",
)

entry(
    index = 321,
    label = "Cds-CsH_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (96.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[160] Knoll et al. Data derived from fitting to a complex mechanism. Pressure 0.08 atm. Excitation : direct photolysis, analysis : mass spectrometry.
N-C3H7 + C2HO --> N-C4H9O
""",
)

entry(
    index = 322,
    label = "Cds-CsH_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[161] Knoll et al. Absolute value measured directly. Pressure 0.28 - 1.17 atm. Excitation : thermal, analysis : mass spectrometry. 
(CH3)2CO + .CH3 --> (CH3)3CO
""",
)

entry(
    index = 323,
    label = "Cds-CsH_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[134] Warnatz literature review. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + H --> C2H3
""",
)

entry(
    index = 324,
    label = "Cds-CsH_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (3990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[162] E.W.Diau and M.C.Lin. RRK(M) extrapolation. C.D.W divided rate expression by 2, to get rate of addition per site. 
C2H2 + CH3 --> CH3CH=CH
""",
)

entry(
    index = 325,
    label = "Cds-CsH_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[163] Kerr et al. literature review. Pressure 0.03-0.20 atm. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + .C2H5 --> CH3CH2CH=CH
""",
)

entry(
    index = 326,
    label = "Cds-CsH_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (796, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[93] Tsang et al. literature review. Pressure 0.03-0.20 atm. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + .CH2CH=CH2 --> CHCH2CH=CH 

pg.263: Discussion on evaluated data

Entry 47,20(a): Recommended rate coefficient is estimated from the addition of alkyl

radicals to C2H2.  Author notes that this could be used as an upper limit for
cyclopentadiene formation.
MRH 31-Aug-2009
""",
)

entry(
    index = 327,
    label = "Cds-CsH_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (638, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[163] Kerr et al. literature review. Pressure 0.07-0.13 atm. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + Iso-C3H7 --> (CH3)2CHCH=CH
""",
)

entry(
    index = 328,
    label = "Cds-CsH_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (473, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[164] Dominguez et al. Data derived from fitting to a complex mechanism. Pressure 0.01-0.32 atm. Excitation : direct photolysis, analysis : GC. 
C2H2 + Tert-C4H9 --> (CH3)3CCH=CH C.D.W divided rate expression by 2, to get rate of addition per site.
""",
)

entry(
    index = 329,
    label = "Cds-CsH_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (8270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[121] Weissman et al. Transition state theory. C.D.W divided rate expression by 2, to get rate of addition per site.	
C2H2 + C2H3 --> CH2=CHCH=CH.
""",
)

entry(
    index = 330,
    label = "Cds-CsH_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[165] Duran et al. Ab initio. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + C2H3 --> CH2=CHCH=CH. (Rxn. -5?)

Verified by Greg Magoon: note: NIST seems to have values (http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:5 , which agree with RMG's original values) that are slightly diferent than this paper's values (p. 637); I can't seem to figure out where the NIST values are coming from (maybe Table 3?); therefore, I have changed rateLibrary to use paper parameters of 10^8.8 (/2) and 4.9 kcal/mol (these values seem to actually be taken from other publications, however), which I am assuming to be high-pressure values; also note that values from other sources are available in the NIST Kinetics Database
""",
)

entry(
    index = 331,
    label = "Cds-CsH_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (186, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[165] Duran et al. Ab initio. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + CCH --> HC(tb)CCH=CH. (Rxn. 18?) 

NIST Record: http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:4
Verified by Greg Magoon: it looks like value is taken from Rxn 18 of Table 3 (1E10), and is apparently non-pressure dependent (and non-temp dependent); based on the table, it looks like Ref. 42 in this paper may be the ultimate source of the value?
""",
)

entry(
    index = 332,
    label = "Cds-CsH_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[95] Baulch et al. literature review. C.D.W divided rate expression by 2, to get rate of addition per site.
C2H2 + .OH --> HOCH=CH

pg.583-584: Discussion on evaluated data

OH+C2H2(+m) --> C2H2OH(+m): "At temperatures below ~1100K and at atmospheric pressure,

the addition channel becomes important and shows a strong pressure dependence.
The following parameters give a reasonable representation of the high temperature data
for k and are also compatible with Atkinson's analysis at low temperature ..."
RMG stores the recommended high-pressure limit rate coefficient, k_inf.

MRH 31-Aug-2009
""",
)

entry(
    index = 333,
    label = "Cds-CsH_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (991, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[166] Miller et al. Transition State Theory. C.D.W divided rate expression by 2, to get rate of addition per site. 
Same reaction as #332, #333 ranked as more accurate in rate library than #332, but they are both from relatively old sources from the early '90s.  

C2H2 + .OH --> HOCH=CH
""",
)

entry(
    index = 334,
    label = "Cds-CsH_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
[144] Bozzelli et al. Based upon CH3 addition to C2H2 (NIST)
""",
)

entry(
    index = 335,
    label = "Cds-CsH_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (943, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 336,
    label = "Cds-CsH_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (151, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 337,
    label = "Cds-CsH_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 338,
    label = "Cds-CsH_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (799, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 339,
    label = "Cds-CsH_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (204, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 340,
    label = "Cds-CsH_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (5360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 341,
    label = "Cds-CsH_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 342,
    label = "Cds-CsH_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (8470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 343,
    label = "Cds-CsH_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (14700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 344,
    label = "Cds-CsH_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 345,
    label = "Cds-CsH_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 346,
    label = "Cds-CsH_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (885, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 347,
    label = "Cds-CsH_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (15500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 348,
    label = "Cds-CsH_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 349,
    label = "Cds-CsH_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (349, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 350,
    label = "Cds-CsH_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 351,
    label = "Cds-CsH_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 352,
    label = "Cds-CsH_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 353,
    label = "Cds-CsH_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 354,
    label = "Cds-CsH_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (283, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 355,
    label = "Cds-CsH_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 356,
    label = "Cds-CsH_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 357,
    label = "Cds-CsH_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (382, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 358,
    label = "Cds-CsH_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (10000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 359,
    label = "Cds-CsH_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 360,
    label = "Cds-CsH_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (15900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 361,
    label = "Cds-CsH_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (15000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 362,
    label = "Cds-CsH_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 363,
    label = "Cds-CsH_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 364,
    label = "Cds-CsH_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (906, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 365,
    label = "Cds-CsH_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (15900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 366,
    label = "Cds-CsH_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 367,
    label = "Cds-CsH_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (357, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 368,
    label = "Cds-CsH_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 369,
    label = "Cds-CsH_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 370,
    label = "Cds-CsH_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 371,
    label = "Cds-CsH_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 372,
    label = "Cds-CsH_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (289, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 373,
    label = "Cds-CsH_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 374,
    label = "Cds-CsH_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 375,
    label = "Cds-CsH_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (391, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 376,
    label = "Cds-CsH_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (10300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 377,
    label = "Cds-CsH_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 378,
    label = "Cds-CsH_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (16200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 379,
    label = "Cds-CsH_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (10800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 380,
    label = "Cds-CsH_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 381,
    label = "Cds-CsH_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (883, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 382,
    label = "Cds-CsH_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (654, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 383,
    label = "Cds-CsH_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (11400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 384,
    label = "Cds-CsH_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 385,
    label = "Cds-CsH_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (258, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 386,
    label = "Cds-CsH_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 387,
    label = "Cds-CsH_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1370, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 388,
    label = "Cds-CsH_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (5300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 389,
    label = "Cds-CsH_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 390,
    label = "Cds-CsH_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (209, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 391,
    label = "Cds-CsH_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 392,
    label = "Cds-CsH_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 393,
    label = "Cds-CsH_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (282, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 394,
    label = "Cds-CsH_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (7420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 395,
    label = "Cds-CsH_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3930, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 396,
    label = "Cds-CsH_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (11700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 397,
    label = "Cds-CsCs_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (6240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 398,
    label = "Cds-CsCs_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (634, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 399,
    label = "Cds-CsCs_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (508, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 400,
    label = "Cds-CsCs_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (376, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 401,
    label = "Cds-CsCs_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (6580, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 402,
    label = "Cds-CsCs_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 403,
    label = "Cds-CsCs_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (148, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 404,
    label = "Cds-CsCs_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2310, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 405,
    label = "Cds-CsCs_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (789, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 406,
    label = "Cds-CsCs_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 407,
    label = "Cds-CsCs_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (751, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 408,
    label = "Cds-CsCs_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 409,
    label = "Cds-CsCs_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2820, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 410,
    label = "Cds-CsCs_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (636, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 411,
    label = "Cds-CsCs_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (162, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 412,
    label = "Cds-CsCs_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (4270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 413,
    label = "Cds-CsCs_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 414,
    label = "Cds-CsCs_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (6740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 415,
    label = "Cds-CsCs_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (6260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Mark Saeys, CBS-QB3 calculations,without hindered rotor treatment.
""",
)

entry(
    index = 416,
    label = "Cds-CsCs_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (636, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
    longDesc = 
u"""
Sandeep CBS-QB3 calculations
""",
)

entry(
    index = 417,
    label = "Cds-CsCs_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (510, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 418,
    label = "Cds-CsCs_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (378, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 419,
    label = "Cds-CsCs_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (6610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 420,
    label = "Cds-CsCs_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 421,
    label = "Cds-CsCs_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (149, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 422,
    label = "Cds-CsCs_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 423,
    label = "Cds-CsCs_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (793, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 424,
    label = "Cds-CsCs_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 425,
    label = "Cds-CsCs_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (754, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 426,
    label = "Cds-CsCs_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (121, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 427,
    label = "Cds-CsCs_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 428,
    label = "Cds-CsCs_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (639, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 429,
    label = "Cds-CsCs_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (163, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 430,
    label = "Cds-CsCs_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (4290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 431,
    label = "Cds-CsCs_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 432,
    label = "Cds-CsCs_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (6770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 433,
    label = "Cds-CsCs_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7880, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 434,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (801, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 435,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (642, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 436,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (476, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 437,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (8320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 438,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 439,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (187, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 440,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 441,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (997, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 442,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 443,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (949, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 444,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (152, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 445,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 446,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (804, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 447,
    label = "Cds-CsCs_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (205, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 448,
    label = "Cds-CsCs_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (5390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 449,
    label = "Cds-CsCs_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 450,
    label = "Cds-CsCs_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (8520, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 451,
    label = "Cds-CsCs_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7030, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 452,
    label = "Cds-CsCs_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (714, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 453,
    label = "Cds-CsCs_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (573, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 454,
    label = "Cds-CsCs_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (425, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 455,
    label = "Cds-CsCs_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (7420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 456,
    label = "Cds-CsCs_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 457,
    label = "Cds-CsCs_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (167, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 458,
    label = "Cds-CsCs_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 459,
    label = "Cds-CsCs_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 460,
    label = "Cds-CsCs_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 461,
    label = "Cds-CsCs_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (847, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 462,
    label = "Cds-CsCs_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (135, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 463,
    label = "Cds-CsCs_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 464,
    label = "Cds-CsCs_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (717, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 465,
    label = "Cds-CsCs_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (183, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 466,
    label = "Cds-CsCs_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (4810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 467,
    label = "Cds-CsCs_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 468,
    label = "Cds-CsCs_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (7600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 469,
    label = "Cds-CsCs_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 470,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (811, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 471,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (650, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 472,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (482, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 473,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (8430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 474,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 475,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 476,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2960, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 477,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 478,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3910, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 479,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (961, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 480,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (154, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 481,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 482,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (814, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 483,
    label = "Cds-CsCs_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (208, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 484,
    label = "Cds-CsCs_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (5460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 485,
    label = "Cds-CsCs_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 486,
    label = "Cds-CsCs_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (8630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 487,
    label = "Cds-CsCs_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (24300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 488,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 489,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 490,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 491,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (25700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 492,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (4470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 493,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (578, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 494,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (9020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 495,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (3080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 496,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (11900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 497,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2930, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 498,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (468, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 499,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (11000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 500,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 501,
    label = "Cds-CsCs_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (633, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 502,
    label = "Cds-CsCs_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (16600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 503,
    label = "Cds-CsCs_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (8830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 504,
    label = "Cds-CsCs_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (26300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 505,
    label = "Cds-CsCs_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 506,
    label = "Cds-CsCs_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (233, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 507,
    label = "Cds-CsCs_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (187, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 508,
    label = "Cds-CsCs_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (139, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 509,
    label = "Cds-CsCs_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (2420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 510,
    label = "Cds-CsCs_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (422, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 511,
    label = "Cds-CsCs_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (54.6, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 512,
    label = "Cds-CsCs_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (851, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 513,
    label = "Cds-CsCs_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (291, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 514,
    label = "Cds-CsCs_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 515,
    label = "Cds-CsCs_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (276, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 516,
    label = "Cds-CsCs_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (44.2, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 517,
    label = "Cds-CsCs_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1040, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 518,
    label = "Cds-CsCs_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (234, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 519,
    label = "Cds-CsCs_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (59.7, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 520,
    label = "Cds-CsCs_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (1570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 521,
    label = "Cds-CsCs_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (833, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 522,
    label = "Cds-CsCs_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (2480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 523,
    label = "Cds-CsCs_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 524,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (495, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 525,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (397, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 526,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (294, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 527,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 528,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (895, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 529,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (116, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 530,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 531,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (616, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 532,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 533,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (586, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 534,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (93.8, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 535,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 536,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (497, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 537,
    label = "Cds-CsCs_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (127, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 538,
    label = "Cds-CsCs_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 539,
    label = "Cds-CsCs_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 540,
    label = "Cds-CsCs_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (5260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 541,
    label = "Cds-CsCs_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (9120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 542,
    label = "Cds-CsCs_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (926, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 543,
    label = "Cds-CsCs_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (743, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 544,
    label = "Cds-CsCs_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 545,
    label = "Cds-CsCs_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (9620, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 546,
    label = "Cds-CsCs_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 547,
    label = "Cds-CsCs_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (217, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 548,
    label = "Cds-CsCs_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 549,
    label = "Cds-CsCs_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 550,
    label = "Cds-CsCs_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 551,
    label = "Cds-CsCs_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 552,
    label = "Cds-CsCs_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (176, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 553,
    label = "Cds-CsCs_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 554,
    label = "Cds-CsCs_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (930, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 555,
    label = "Cds-CsCs_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (237, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 556,
    label = "Cds-CsCs_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (6240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 557,
    label = "Cds-CsCs_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3310, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 558,
    label = "Cds-CsCs_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (9860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 559,
    label = "Cds-CsCs_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (9330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 560,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (948, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 561,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (761, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 562,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (563, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 563,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (9850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 564,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 565,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (222, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 566,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 567,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 568,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 569,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 570,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 571,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 572,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (952, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 573,
    label = "Cds-CsCs_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (243, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 574,
    label = "Cds-CsCs_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (6390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 575,
    label = "Cds-CsCs_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 576,
    label = "Cds-CsCs_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (10100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 577,
    label = "Cds-CsCs_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (6740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 578,
    label = "Cds-CsCs_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (684, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 579,
    label = "Cds-CsCs_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (549, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 580,
    label = "Cds-CsCs_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (407, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 581,
    label = "Cds-CsCs_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (7110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 582,
    label = "Cds-CsCs_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 583,
    label = "Cds-CsCs_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 584,
    label = "Cds-CsCs_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 585,
    label = "Cds-CsCs_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (852, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 586,
    label = "Cds-CsCs_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 587,
    label = "Cds-CsCs_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (811, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 588,
    label = "Cds-CsCs_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 589,
    label = "Cds-CsCs_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 590,
    label = "Cds-CsCs_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (687, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 591,
    label = "Cds-CsCs_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (175, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 592,
    label = "Cds-CsCs_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (4610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 593,
    label = "Cds-CsCs_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 594,
    label = "Cds-CsCs_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (7280, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 595,
    label = "Cds-CdH_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (13200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 596,
    label = "Cds-CdH_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 597,
    label = "Cds-CdH_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 598,
    label = "Cds-CdH_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (798, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 599,
    label = "Cds-CdH_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 600,
    label = "Cds-CdH_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 601,
    label = "Cds-CdH_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (314, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 602,
    label = "Cds-CdH_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 603,
    label = "Cds-CdH_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 604,
    label = "Cds-CdH_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (6470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 605,
    label = "Cds-CdH_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1590, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 606,
    label = "Cds-CdH_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (255, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 607,
    label = "Cds-CdH_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (5980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 608,
    label = "Cds-CdH_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 609,
    label = "Cds-CdH_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (344, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 610,
    label = "Cds-CdH_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (9050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 611,
    label = "Cds-CdH_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (4800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 612,
    label = "Cds-CdH_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (14300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 613,
    label = "Cds-CdH_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (13300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 614,
    label = "Cds-CdH_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 615,
    label = "Cds-CdH_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 616,
    label = "Cds-CdH_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (801, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 617,
    label = "Cds-CdH_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 618,
    label = "Cds-CdH_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 619,
    label = "Cds-CdH_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (316, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 620,
    label = "Cds-CdH_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 621,
    label = "Cds-CdH_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 622,
    label = "Cds-CdH_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (6500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 623,
    label = "Cds-CdH_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 624,
    label = "Cds-CdH_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (256, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 625,
    label = "Cds-CdH_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 626,
    label = "Cds-CdH_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 627,
    label = "Cds-CdH_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (346, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 628,
    label = "Cds-CdH_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (9090, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 629,
    label = "Cds-CdH_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (4820, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 630,
    label = "Cds-CdH_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (14400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 631,
    label = "Cds-CdH_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (16700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 632,
    label = "Cds-CdH_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 633,
    label = "Cds-CdH_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 634,
    label = "Cds-CdH_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 635,
    label = "Cds-CdH_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (17600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 636,
    label = "Cds-CdH_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 637,
    label = "Cds-CdH_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (397, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 638,
    label = "Cds-CdH_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (6190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 639,
    label = "Cds-CdH_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 640,
    label = "Cds-CdH_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (8180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 641,
    label = "Cds-CdH_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 642,
    label = "Cds-CdH_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (322, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 643,
    label = "Cds-CdH_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (7560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 644,
    label = "Cds-CdH_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 645,
    label = "Cds-CdH_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (435, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 646,
    label = "Cds-CdH_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (11400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 647,
    label = "Cds-CdH_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (6060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 648,
    label = "Cds-CdH_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (18100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 649,
    label = "Cds-CdH_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (14900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 650,
    label = "Cds-CdH_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1510, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 651,
    label = "Cds-CdH_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 652,
    label = "Cds-CdH_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 653,
    label = "Cds-CdH_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (15700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 654,
    label = "Cds-CdH_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 655,
    label = "Cds-CdH_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (354, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 656,
    label = "Cds-CdH_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 657,
    label = "Cds-CdH_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 658,
    label = "Cds-CdH_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 659,
    label = "Cds-CdH_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 660,
    label = "Cds-CdH_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (287, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 661,
    label = "Cds-CdH_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 662,
    label = "Cds-CdH_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1520, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 663,
    label = "Cds-CdH_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (388, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 664,
    label = "Cds-CdH_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (10200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 665,
    label = "Cds-CdH_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5410, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 666,
    label = "Cds-CdH_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (16100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 667,
    label = "Cds-CdH_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (16900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 668,
    label = "Cds-CdH_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 669,
    label = "Cds-CdH_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 670,
    label = "Cds-CdH_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 671,
    label = "Cds-CdH_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (17900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 672,
    label = "Cds-CdH_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 673,
    label = "Cds-CdH_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (402, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 674,
    label = "Cds-CdH_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (6270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 675,
    label = "Cds-CdH_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 676,
    label = "Cds-CdH_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (8280, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 677,
    label = "Cds-CdH_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2040, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 678,
    label = "Cds-CdH_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (326, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 679,
    label = "Cds-CdH_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (7660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 680,
    label = "Cds-CdH_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1730, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 681,
    label = "Cds-CdH_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 682,
    label = "Cds-CdH_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (11600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 683,
    label = "Cds-CdH_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (6140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 684,
    label = "Cds-CdH_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (18300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 685,
    label = "Cds-CdH_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (51600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 686,
    label = "Cds-CdH_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (5240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 687,
    label = "Cds-CdH_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (4200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 688,
    label = "Cds-CdH_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (3110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 689,
    label = "Cds-CdH_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (54400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 690,
    label = "Cds-CdH_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (9480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 691,
    label = "Cds-CdH_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (1230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 692,
    label = "Cds-CdH_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (19100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 693,
    label = "Cds-CdH_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (6530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 694,
    label = "Cds-CdH_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (25200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 695,
    label = "Cds-CdH_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (6210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 696,
    label = "Cds-CdH_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (993, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 697,
    label = "Cds-CdH_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (23300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 698,
    label = "Cds-CdH_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (5260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 699,
    label = "Cds-CdH_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (1340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 700,
    label = "Cds-CdH_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (35300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 701,
    label = "Cds-CdH_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (18700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 702,
    label = "Cds-CdH_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (55700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-3.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 703,
    label = "Cds-CdH_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 704,
    label = "Cds-CdH_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (494, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 705,
    label = "Cds-CdH_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (397, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 706,
    label = "Cds-CdH_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (294, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 707,
    label = "Cds-CdH_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 708,
    label = "Cds-CdH_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (895, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 709,
    label = "Cds-CdH_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (116, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 710,
    label = "Cds-CdH_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 711,
    label = "Cds-CdH_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (616, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 712,
    label = "Cds-CdH_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 713,
    label = "Cds-CdH_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (586, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 714,
    label = "Cds-CdH_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (93.7, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 715,
    label = "Cds-CdH_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 716,
    label = "Cds-CdH_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (496, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 717,
    label = "Cds-CdH_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (127, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 718,
    label = "Cds-CdH_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 719,
    label = "Cds-CdH_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 720,
    label = "Cds-CdH_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (5260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 721,
    label = "Cds-CdH_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (10300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 722,
    label = "Cds-CdH_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 723,
    label = "Cds-CdH_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (841, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 724,
    label = "Cds-CdH_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (623, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 725,
    label = "Cds-CdH_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (10900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 726,
    label = "Cds-CdH_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 727,
    label = "Cds-CdH_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (245, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 728,
    label = "Cds-CdH_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 729,
    label = "Cds-CdH_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1310, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 730,
    label = "Cds-CdH_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (5050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 731,
    label = "Cds-CdH_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 732,
    label = "Cds-CdH_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (199, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 733,
    label = "Cds-CdH_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 734,
    label = "Cds-CdH_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 735,
    label = "Cds-CdH_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (269, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 736,
    label = "Cds-CdH_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (7060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 737,
    label = "Cds-CdH_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 738,
    label = "Cds-CdH_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (11200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 739,
    label = "Cds-CdH_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (19300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 740,
    label = "Cds-CdH_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1960, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 741,
    label = "Cds-CdH_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 742,
    label = "Cds-CdH_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 743,
    label = "Cds-CdH_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (20400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 744,
    label = "Cds-CdH_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 745,
    label = "Cds-CdH_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 746,
    label = "Cds-CdH_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (7160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 747,
    label = "Cds-CdH_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 748,
    label = "Cds-CdH_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (9460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 749,
    label = "Cds-CdH_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 750,
    label = "Cds-CdH_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (372, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 751,
    label = "Cds-CdH_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (8740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 752,
    label = "Cds-CdH_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1970, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 753,
    label = "Cds-CdH_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (503, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 754,
    label = "Cds-CdH_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (13200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 755,
    label = "Cds-CdH_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (7010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 756,
    label = "Cds-CdH_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (20900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 757,
    label = "Cds-CdH_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (19800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 758,
    label = "Cds-CdH_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 759,
    label = "Cds-CdH_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 760,
    label = "Cds-CdH_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 761,
    label = "Cds-CdH_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (20900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 762,
    label = "Cds-CdH_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 763,
    label = "Cds-CdH_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 764,
    label = "Cds-CdH_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (7330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 765,
    label = "Cds-CdH_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 766,
    label = "Cds-CdH_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (9680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 767,
    label = "Cds-CdH_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 768,
    label = "Cds-CdH_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (381, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 769,
    label = "Cds-CdH_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (8950, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 770,
    label = "Cds-CdH_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 771,
    label = "Cds-CdH_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (515, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 772,
    label = "Cds-CdH_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (13500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 773,
    label = "Cds-CdH_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (7180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 774,
    label = "Cds-CdH_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (21400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 775,
    label = "Cds-CdH_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (14300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 776,
    label = "Cds-CdH_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 777,
    label = "Cds-CdH_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 778,
    label = "Cds-CdH_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (862, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 779,
    label = "Cds-CdH_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (15100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 780,
    label = "Cds-CdH_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 781,
    label = "Cds-CdH_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (339, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 782,
    label = "Cds-CdH_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 783,
    label = "Cds-CdH_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 784,
    label = "Cds-CdH_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (6990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 785,
    label = "Cds-CdH_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 786,
    label = "Cds-CdH_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (275, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 787,
    label = "Cds-CdH_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 788,
    label = "Cds-CdH_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 789,
    label = "Cds-CdH_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (372, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 790,
    label = "Cds-CdH_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (9770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 791,
    label = "Cds-CdH_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 792,
    label = "Cds-CdH_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (15400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 793,
    label = "Cds-CdCs_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (6640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 794,
    label = "Cds-CdCs_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (674, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 795,
    label = "Cds-CdCs_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (541, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 796,
    label = "Cds-CdCs_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 797,
    label = "Cds-CdCs_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (7000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 798,
    label = "Cds-CdCs_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 799,
    label = "Cds-CdCs_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (158, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 800,
    label = "Cds-CdCs_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 801,
    label = "Cds-CdCs_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 802,
    label = "Cds-CdCs_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3250, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 803,
    label = "Cds-CdCs_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (799, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 804,
    label = "Cds-CdCs_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (128, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 805,
    label = "Cds-CdCs_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 806,
    label = "Cds-CdCs_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (677, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 807,
    label = "Cds-CdCs_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (173, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 808,
    label = "Cds-CdCs_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (4540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 809,
    label = "Cds-CdCs_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2410, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 810,
    label = "Cds-CdCs_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (7170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 811,
    label = "Cds-CdCs_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (6660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 812,
    label = "Cds-CdCs_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (677, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 813,
    label = "Cds-CdCs_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (543, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 814,
    label = "Cds-CdCs_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (402, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 815,
    label = "Cds-CdCs_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (7030, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 816,
    label = "Cds-CdCs_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 817,
    label = "Cds-CdCs_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (158, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 818,
    label = "Cds-CdCs_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 819,
    label = "Cds-CdCs_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (843, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 820,
    label = "Cds-CdCs_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 821,
    label = "Cds-CdCs_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (802, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 822,
    label = "Cds-CdCs_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (128, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 823,
    label = "Cds-CdCs_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 824,
    label = "Cds-CdCs_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 825,
    label = "Cds-CdCs_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (173, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 826,
    label = "Cds-CdCs_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (4560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 827,
    label = "Cds-CdCs_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 828,
    label = "Cds-CdCs_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (7200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 829,
    label = "Cds-CdCs_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (8380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 830,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (851, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 831,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (683, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 832,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (506, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 833,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (8850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 834,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 835,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (199, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 836,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 837,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 838,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 839,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 840,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (161, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 841,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 842,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (855, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 843,
    label = "Cds-CdCs_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (218, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 844,
    label = "Cds-CdCs_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (5730, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 845,
    label = "Cds-CdCs_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3040, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 846,
    label = "Cds-CdCs_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (9060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 847,
    label = "Cds-CdCs_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 848,
    label = "Cds-CdCs_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 849,
    label = "Cds-CdCs_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 850,
    label = "Cds-CdCs_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (451, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 851,
    label = "Cds-CdCs_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (7900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 852,
    label = "Cds-CdCs_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 853,
    label = "Cds-CdCs_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (178, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 854,
    label = "Cds-CdCs_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 855,
    label = "Cds-CdCs_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (947, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 856,
    label = "Cds-CdCs_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 857,
    label = "Cds-CdCs_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 858,
    label = "Cds-CdCs_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (144, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 859,
    label = "Cds-CdCs_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 860,
    label = "Cds-CdCs_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (763, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 861,
    label = "Cds-CdCs_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (195, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 862,
    label = "Cds-CdCs_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (5120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 863,
    label = "Cds-CdCs_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2710, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 864,
    label = "Cds-CdCs_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (8090, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 865,
    label = "Cds-CdCs_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (8490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 866,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (862, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 867,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (692, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 868,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (512, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 869,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (8960, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 870,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 871,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (202, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 872,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 873,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 874,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 875,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 876,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (164, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 877,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 878,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (866, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 879,
    label = "Cds-CdCs_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (221, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 880,
    label = "Cds-CdCs_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (5810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 881,
    label = "Cds-CdCs_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 882,
    label = "Cds-CdCs_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (9180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 883,
    label = "Cds-CdCs_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (25900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 884,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 885,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (2110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 886,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 887,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (27300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 888,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (4760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 889,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (615, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 890,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (9590, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 891,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (3270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 892,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (12700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 893,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (3110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 894,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (498, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 895,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (11700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 896,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 897,
    label = "Cds-CdCs_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (673, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 898,
    label = "Cds-CdCs_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (17700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 899,
    label = "Cds-CdCs_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (9390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 900,
    label = "Cds-CdCs_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 901,
    label = "Cds-CdCs_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 902,
    label = "Cds-CdCs_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (248, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 903,
    label = "Cds-CdCs_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (199, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 904,
    label = "Cds-CdCs_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (147, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 905,
    label = "Cds-CdCs_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (2580, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 906,
    label = "Cds-CdCs_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (449, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 907,
    label = "Cds-CdCs_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (58.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 908,
    label = "Cds-CdCs_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (905, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 909,
    label = "Cds-CdCs_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (309, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 910,
    label = "Cds-CdCs_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 911,
    label = "Cds-CdCs_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (294, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 912,
    label = "Cds-CdCs_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (47, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 913,
    label = "Cds-CdCs_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 914,
    label = "Cds-CdCs_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (249, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 915,
    label = "Cds-CdCs_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (63.5, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 916,
    label = "Cds-CdCs_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (1670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 917,
    label = "Cds-CdCs_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (886, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 918,
    label = "Cds-CdCs_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (2640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 919,
    label = "Cds-CdCs_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 920,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (526, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 921,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (422, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 922,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (313, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 923,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 924,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (952, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 925,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (123, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 926,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 927,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (655, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 928,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 929,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (623, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 930,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (99.7, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 931,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 932,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (528, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 933,
    label = "Cds-CdCs_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (135, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 934,
    label = "Cds-CdCs_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 935,
    label = "Cds-CdCs_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1880, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 936,
    label = "Cds-CdCs_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (5600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 937,
    label = "Cds-CdCs_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (9700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 938,
    label = "Cds-CdCs_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (985, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 939,
    label = "Cds-CdCs_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 940,
    label = "Cds-CdCs_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (585, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 941,
    label = "Cds-CdCs_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (10200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 942,
    label = "Cds-CdCs_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 943,
    label = "Cds-CdCs_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (231, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 944,
    label = "Cds-CdCs_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3590, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 945,
    label = "Cds-CdCs_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 946,
    label = "Cds-CdCs_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 947,
    label = "Cds-CdCs_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 948,
    label = "Cds-CdCs_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (187, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 949,
    label = "Cds-CdCs_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 950,
    label = "Cds-CdCs_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (989, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 951,
    label = "Cds-CdCs_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (252, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 952,
    label = "Cds-CdCs_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (6640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 953,
    label = "Cds-CdCs_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3520, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 954,
    label = "Cds-CdCs_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (10500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 955,
    label = "Cds-CdCs_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (9930, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 956,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 957,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (809, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 958,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (599, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 959,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (10500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 960,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1820, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 961,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (236, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 962,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 963,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 964,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 965,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 966,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (191, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 967,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 968,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 969,
    label = "Cds-CdCs_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (258, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 970,
    label = "Cds-CdCs_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (6790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 971,
    label = "Cds-CdCs_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 972,
    label = "Cds-CdCs_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (10700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 973,
    label = "Cds-CdCs_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 974,
    label = "Cds-CdCs_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (728, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 975,
    label = "Cds-CdCs_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (584, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 976,
    label = "Cds-CdCs_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (432, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 977,
    label = "Cds-CdCs_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (7560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 978,
    label = "Cds-CdCs_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 979,
    label = "Cds-CdCs_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 980,
    label = "Cds-CdCs_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 981,
    label = "Cds-CdCs_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (907, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 982,
    label = "Cds-CdCs_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3510, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 983,
    label = "Cds-CdCs_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (862, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 984,
    label = "Cds-CdCs_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (138, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 985,
    label = "Cds-CdCs_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 986,
    label = "Cds-CdCs_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (731, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 987,
    label = "Cds-CdCs_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (186, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 988,
    label = "Cds-CdCs_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (4900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 989,
    label = "Cds-CdCs_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 990,
    label = "Cds-CdCs_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (7740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 991,
    label = "Cds-CdCd_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 992,
    label = "Cds-CdCd_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 993,
    label = "Cds-CdCd_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 994,
    label = "Cds-CdCd_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (847, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 995,
    label = "Cds-CdCd_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (14800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 996,
    label = "Cds-CdCd_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2580, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 997,
    label = "Cds-CdCd_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (334, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 998,
    label = "Cds-CdCd_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 999,
    label = "Cds-CdCd_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1000,
    label = "Cds-CdCd_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (6870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1001,
    label = "Cds-CdCd_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1690, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1002,
    label = "Cds-CdCd_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1003,
    label = "Cds-CdCd_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1004,
    label = "Cds-CdCd_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1005,
    label = "Cds-CdCd_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (365, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1006,
    label = "Cds-CdCd_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (9610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1007,
    label = "Cds-CdCd_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5090, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1008,
    label = "Cds-CdCd_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (15200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1009,
    label = "Cds-CdCd_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (14100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1010,
    label = "Cds-CdCd_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1011,
    label = "Cds-CdCd_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1012,
    label = "Cds-CdCd_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (851, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1013,
    label = "Cds-CdCd_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (14900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1014,
    label = "Cds-CdCd_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2590, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1015,
    label = "Cds-CdCd_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (335, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1016,
    label = "Cds-CdCd_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1017,
    label = "Cds-CdCd_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1018,
    label = "Cds-CdCd_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (6900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1019,
    label = "Cds-CdCd_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1020,
    label = "Cds-CdCd_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (271, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1021,
    label = "Cds-CdCd_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1022,
    label = "Cds-CdCd_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1023,
    label = "Cds-CdCd_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (367, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1024,
    label = "Cds-CdCd_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (9650, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1025,
    label = "Cds-CdCd_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1026,
    label = "Cds-CdCd_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (15200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1027,
    label = "Cds-CdCd_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (17700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1028,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1029,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1030,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1031,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (18700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1032,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1033,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (422, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1034,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (6570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1035,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1036,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (8680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1037,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1038,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (342, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1039,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (8020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1040,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1041,
    label = "Cds-CdCd_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (462, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1042,
    label = "Cds-CdCd_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (12100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1043,
    label = "Cds-CdCd_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (6430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1044,
    label = "Cds-CdCd_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (19200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1045,
    label = "Cds-CdCd_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (15800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1046,
    label = "Cds-CdCd_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1047,
    label = "Cds-CdCd_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1048,
    label = "Cds-CdCd_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (955, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1049,
    label = "Cds-CdCd_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (16700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1050,
    label = "Cds-CdCd_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2910, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1051,
    label = "Cds-CdCd_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (376, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1052,
    label = "Cds-CdCd_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1053,
    label = "Cds-CdCd_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1054,
    label = "Cds-CdCd_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1055,
    label = "Cds-CdCd_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1910, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1056,
    label = "Cds-CdCd_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (305, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1057,
    label = "Cds-CdCd_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (7160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1058,
    label = "Cds-CdCd_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1059,
    label = "Cds-CdCd_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (412, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1060,
    label = "Cds-CdCd_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (10800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1061,
    label = "Cds-CdCd_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1062,
    label = "Cds-CdCd_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (17100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1063,
    label = "Cds-CdCd_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (18000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1064,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1820, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1065,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1066,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1067,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (19000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1068,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1069,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (427, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1070,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (6660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1071,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1072,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (8790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1073,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1074,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (346, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1075,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (8130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1076,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1077,
    label = "Cds-CdCd_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (467, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1078,
    label = "Cds-CdCd_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (12300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1079,
    label = "Cds-CdCd_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (6520, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1080,
    label = "Cds-CdCd_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (19400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1081,
    label = "Cds-CdCd_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (54800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1082,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (5560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1083,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (4460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1084,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (3300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1085,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (57800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1086,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (10100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1087,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (1300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1088,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (20300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1089,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (6930, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1090,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (26800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1091,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (6590, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1092,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (1050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1093,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (24800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1094,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (5580, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1095,
    label = "Cds-CdCd_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (1420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1096,
    label = "Cds-CdCd_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (37500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1097,
    label = "Cds-CdCd_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (19900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1098,
    label = "Cds-CdCd_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (59200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1099,
    label = "Cds-CdCd_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1100,
    label = "Cds-CdCd_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (525, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1101,
    label = "Cds-CdCd_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (421, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1102,
    label = "Cds-CdCd_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (312, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1103,
    label = "Cds-CdCd_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1104,
    label = "Cds-CdCd_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (950, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1105,
    label = "Cds-CdCd_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (123, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1106,
    label = "Cds-CdCd_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1107,
    label = "Cds-CdCd_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (654, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1108,
    label = "Cds-CdCd_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1109,
    label = "Cds-CdCd_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (622, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1110,
    label = "Cds-CdCd_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (99.5, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1111,
    label = "Cds-CdCd_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1112,
    label = "Cds-CdCd_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (527, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1113,
    label = "Cds-CdCd_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (134, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1114,
    label = "Cds-CdCd_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1115,
    label = "Cds-CdCd_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1116,
    label = "Cds-CdCd_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (5590, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1117,
    label = "Cds-CdCd_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (11000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1118,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1119,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (893, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1120,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (661, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1121,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (11600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1122,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1123,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (261, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1124,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1125,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1126,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (5360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1127,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1128,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (211, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1129,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4960, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1130,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1131,
    label = "Cds-CdCd_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (285, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1132,
    label = "Cds-CdCd_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (7500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1133,
    label = "Cds-CdCd_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1134,
    label = "Cds-CdCd_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (11800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1135,
    label = "Cds-CdCd_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (20500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1136,
    label = "Cds-CdCd_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1137,
    label = "Cds-CdCd_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1138,
    label = "Cds-CdCd_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1139,
    label = "Cds-CdCd_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (21700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1140,
    label = "Cds-CdCd_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1141,
    label = "Cds-CdCd_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (488, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1142,
    label = "Cds-CdCd_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (7610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1143,
    label = "Cds-CdCd_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1144,
    label = "Cds-CdCd_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (10000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1145,
    label = "Cds-CdCd_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1146,
    label = "Cds-CdCd_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (395, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1147,
    label = "Cds-CdCd_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (9280, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1148,
    label = "Cds-CdCd_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2090, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1149,
    label = "Cds-CdCd_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (534, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1150,
    label = "Cds-CdCd_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1151,
    label = "Cds-CdCd_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (7440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1152,
    label = "Cds-CdCd_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (22200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1153,
    label = "Cds-CdCd_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (21000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1154,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1155,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1710, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1156,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1157,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (22200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1158,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1159,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (499, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1160,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (7790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1161,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1162,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (10300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1163,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1164,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (405, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1165,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (9500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1166,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1167,
    label = "Cds-CdCd_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (547, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1168,
    label = "Cds-CdCd_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (14400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1169,
    label = "Cds-CdCd_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (7620, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1170,
    label = "Cds-CdCd_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (22700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1171,
    label = "Cds-CdCd_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (15200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1172,
    label = "Cds-CdCd_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1173,
    label = "Cds-CdCd_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1174,
    label = "Cds-CdCd_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (915, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1175,
    label = "Cds-CdCd_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (16000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1176,
    label = "Cds-CdCd_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1177,
    label = "Cds-CdCd_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1178,
    label = "Cds-CdCd_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5620, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1179,
    label = "Cds-CdCd_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1180,
    label = "Cds-CdCd_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1181,
    label = "Cds-CdCd_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1820, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1182,
    label = "Cds-CdCd_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (292, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1183,
    label = "Cds-CdCd_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1184,
    label = "Cds-CdCd_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1185,
    label = "Cds-CdCd_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (394, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1186,
    label = "Cds-CdCd_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (10400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1187,
    label = "Cds-CdCd_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1188,
    label = "Cds-CdCd_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1189,
    label = "Cds-CbH_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1190,
    label = "Cds-CbH_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1191,
    label = "Cds-CbH_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (305, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1192,
    label = "Cds-CbH_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (226, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1193,
    label = "Cds-CbH_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (3950, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1194,
    label = "Cds-CbH_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (688, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1195,
    label = "Cds-CbH_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (89, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1196,
    label = "Cds-CbH_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1197,
    label = "Cds-CbH_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (474, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1198,
    label = "Cds-CbH_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1199,
    label = "Cds-CbH_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (451, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1200,
    label = "Cds-CbH_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (72.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1201,
    label = "Cds-CbH_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1690, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1202,
    label = "Cds-CbH_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (382, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1203,
    label = "Cds-CbH_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (97.5, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1204,
    label = "Cds-CbH_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1205,
    label = "Cds-CbH_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1206,
    label = "Cds-CbH_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (4050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1207,
    label = "Cds-CbH_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1208,
    label = "Cds-CbH_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (382, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1209,
    label = "Cds-CbH_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (306, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1210,
    label = "Cds-CbH_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (227, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1211,
    label = "Cds-CbH_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (3970, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1212,
    label = "Cds-CbH_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (691, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1213,
    label = "Cds-CbH_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (89.4, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1214,
    label = "Cds-CbH_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1215,
    label = "Cds-CbH_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (476, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1216,
    label = "Cds-CbH_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1217,
    label = "Cds-CbH_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (453, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1218,
    label = "Cds-CbH_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (72.4, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1219,
    label = "Cds-CbH_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1220,
    label = "Cds-CbH_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (384, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1221,
    label = "Cds-CbH_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (97.9, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1222,
    label = "Cds-CbH_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1223,
    label = "Cds-CbH_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1224,
    label = "Cds-CbH_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (4060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1225,
    label = "Cds-CbH_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4730, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1226,
    label = "Cds-CbH_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (481, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1227,
    label = "Cds-CbH_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (386, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1228,
    label = "Cds-CbH_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (286, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1229,
    label = "Cds-CbH_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (4990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1230,
    label = "Cds-CbH_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1231,
    label = "Cds-CbH_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (112, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1232,
    label = "Cds-CbH_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1233,
    label = "Cds-CbH_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (599, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1234,
    label = "Cds-CbH_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1235,
    label = "Cds-CbH_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1236,
    label = "Cds-CbH_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (91.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1237,
    label = "Cds-CbH_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1238,
    label = "Cds-CbH_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (483, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1239,
    label = "Cds-CbH_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (123, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1240,
    label = "Cds-CbH_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1241,
    label = "Cds-CbH_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1242,
    label = "Cds-CbH_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (5110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1243,
    label = "Cds-CbH_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1244,
    label = "Cds-CbH_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (429, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1245,
    label = "Cds-CbH_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (344, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1246,
    label = "Cds-CbH_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (255, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1247,
    label = "Cds-CbH_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (4460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1248,
    label = "Cds-CbH_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (776, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1249,
    label = "Cds-CbH_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1250,
    label = "Cds-CbH_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1251,
    label = "Cds-CbH_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (534, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1252,
    label = "Cds-CbH_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1253,
    label = "Cds-CbH_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (508, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1254,
    label = "Cds-CbH_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (81.3, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1255,
    label = "Cds-CbH_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1910, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1256,
    label = "Cds-CbH_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (431, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1257,
    label = "Cds-CbH_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1258,
    label = "Cds-CbH_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1259,
    label = "Cds-CbH_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1260,
    label = "Cds-CbH_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (4560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1261,
    label = "Cds-CbH_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1262,
    label = "Cds-CbH_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (487, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1263,
    label = "Cds-CbH_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (391, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1264,
    label = "Cds-CbH_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (289, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1265,
    label = "Cds-CbH_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1266,
    label = "Cds-CbH_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (881, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1267,
    label = "Cds-CbH_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (114, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1268,
    label = "Cds-CbH_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1269,
    label = "Cds-CbH_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (606, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1270,
    label = "Cds-CbH_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1271,
    label = "Cds-CbH_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (577, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1272,
    label = "Cds-CbH_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (92.3, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1273,
    label = "Cds-CbH_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1274,
    label = "Cds-CbH_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (489, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1275,
    label = "Cds-CbH_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (125, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1276,
    label = "Cds-CbH_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3280, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1277,
    label = "Cds-CbH_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1278,
    label = "Cds-CbH_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (5180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1279,
    label = "Cds-CbH_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (14600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1280,
    label = "Cds-CbH_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1281,
    label = "Cds-CbH_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1282,
    label = "Cds-CbH_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (881, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1283,
    label = "Cds-CbH_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (15400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1284,
    label = "Cds-CbH_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1285,
    label = "Cds-CbH_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (347, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1286,
    label = "Cds-CbH_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5410, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1287,
    label = "Cds-CbH_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1288,
    label = "Cds-CbH_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1289,
    label = "Cds-CbH_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1290,
    label = "Cds-CbH_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (281, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1291,
    label = "Cds-CbH_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1292,
    label = "Cds-CbH_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1293,
    label = "Cds-CbH_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1294,
    label = "Cds-CbH_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (9990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1295,
    label = "Cds-CbH_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1296,
    label = "Cds-CbH_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (15800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1297,
    label = "Cds-CbH_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1298,
    label = "Cds-CbH_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1299,
    label = "Cds-CbH_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (112, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1300,
    label = "Cds-CbH_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (83.2, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1301,
    label = "Cds-CbH_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (1450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1302,
    label = "Cds-CbH_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (253, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1303,
    label = "Cds-CbH_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (32.8, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1304,
    label = "Cds-CbH_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (511, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1305,
    label = "Cds-CbH_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (174, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1306,
    label = "Cds-CbH_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (675, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1307,
    label = "Cds-CbH_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (166, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1308,
    label = "Cds-CbH_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (26.5, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1309,
    label = "Cds-CbH_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (624, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1310,
    label = "Cds-CbH_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (141, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1311,
    label = "Cds-CbH_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (35.9, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1312,
    label = "Cds-CbH_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (943, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1313,
    label = "Cds-CbH_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1314,
    label = "Cds-CbH_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (1490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1315,
    label = "Cds-CbH_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1316,
    label = "Cds-CbH_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (297, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1317,
    label = "Cds-CbH_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (238, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1318,
    label = "Cds-CbH_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (176, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1319,
    label = "Cds-CbH_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (3090, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1320,
    label = "Cds-CbH_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (537, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1321,
    label = "Cds-CbH_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (69.5, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1322,
    label = "Cds-CbH_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1323,
    label = "Cds-CbH_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (370, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1324,
    label = "Cds-CbH_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1325,
    label = "Cds-CbH_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (352, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1326,
    label = "Cds-CbH_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (56.3, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1327,
    label = "Cds-CbH_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1328,
    label = "Cds-CbH_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (298, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1329,
    label = "Cds-CbH_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (76.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1330,
    label = "Cds-CbH_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1331,
    label = "Cds-CbH_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1332,
    label = "Cds-CbH_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (3160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1333,
    label = "Cds-CbH_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1334,
    label = "Cds-CbH_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (556, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1335,
    label = "Cds-CbH_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (446, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1336,
    label = "Cds-CbH_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1337,
    label = "Cds-CbH_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1338,
    label = "Cds-CbH_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1339,
    label = "Cds-CbH_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1340,
    label = "Cds-CbH_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2030, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1341,
    label = "Cds-CbH_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (693, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1342,
    label = "Cds-CbH_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1343,
    label = "Cds-CbH_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (659, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1344,
    label = "Cds-CbH_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (105, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1345,
    label = "Cds-CbH_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1346,
    label = "Cds-CbH_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (558, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1347,
    label = "Cds-CbH_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (142, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1348,
    label = "Cds-CbH_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1349,
    label = "Cds-CbH_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1350,
    label = "Cds-CbH_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (5920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1351,
    label = "Cds-CbH_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1352,
    label = "Cds-CbH_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (569, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1353,
    label = "Cds-CbH_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (457, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1354,
    label = "Cds-CbH_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (338, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1355,
    label = "Cds-CbH_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5910, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1356,
    label = "Cds-CbH_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1030, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1357,
    label = "Cds-CbH_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (133, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1358,
    label = "Cds-CbH_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1359,
    label = "Cds-CbH_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (709, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1360,
    label = "Cds-CbH_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1361,
    label = "Cds-CbH_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (674, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1362,
    label = "Cds-CbH_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (108, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1363,
    label = "Cds-CbH_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1364,
    label = "Cds-CbH_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (572, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1365,
    label = "Cds-CbH_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (146, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1366,
    label = "Cds-CbH_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1367,
    label = "Cds-CbH_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2030, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1368,
    label = "Cds-CbH_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (6060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1369,
    label = "Cds-CbH_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4040, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1370,
    label = "Cds-CbH_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (411, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1371,
    label = "Cds-CbH_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1372,
    label = "Cds-CbH_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (244, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1373,
    label = "Cds-CbH_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (4270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1374,
    label = "Cds-CbH_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (743, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1375,
    label = "Cds-CbH_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (96.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1376,
    label = "Cds-CbH_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1377,
    label = "Cds-CbH_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (512, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1378,
    label = "Cds-CbH_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1379,
    label = "Cds-CbH_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (487, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1380,
    label = "Cds-CbH_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (77.9, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1381,
    label = "Cds-CbH_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1382,
    label = "Cds-CbH_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (413, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1383,
    label = "Cds-CbH_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (105, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1384,
    label = "Cds-CbH_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1385,
    label = "Cds-CbH_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1386,
    label = "Cds-CbH_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (4370, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1387,
    label = "Cds-CbCs_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1388,
    label = "Cds-CbCs_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (339, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1389,
    label = "Cds-CbCs_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (272, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1390,
    label = "Cds-CbCs_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (201, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1391,
    label = "Cds-CbCs_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (3520, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1392,
    label = "Cds-CbCs_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (613, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1393,
    label = "Cds-CbCs_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (79.3, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1394,
    label = "Cds-CbCs_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (20.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1395,
    label = "Cds-CbCs_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (422, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (20.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1396,
    label = "Cds-CbCs_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1397,
    label = "Cds-CbCs_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (402, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1398,
    label = "Cds-CbCs_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (64.2, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1399,
    label = "Cds-CbCs_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1510, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1400,
    label = "Cds-CbCs_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1401,
    label = "Cds-CbCs_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (86.8, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1402,
    label = "Cds-CbCs_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2280, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1403,
    label = "Cds-CbCs_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1404,
    label = "Cds-CbCs_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (3610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1405,
    label = "Cds-CbCs_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1406,
    label = "Cds-CbCs_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1407,
    label = "Cds-CbCs_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (273, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1408,
    label = "Cds-CbCs_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (202, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1409,
    label = "Cds-CbCs_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (3540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1410,
    label = "Cds-CbCs_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (616, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1411,
    label = "Cds-CbCs_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (79.6, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1412,
    label = "Cds-CbCs_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1240, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (20.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1413,
    label = "Cds-CbCs_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (424, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (20.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1414,
    label = "Cds-CbCs_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1415,
    label = "Cds-CbCs_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (403, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1416,
    label = "Cds-CbCs_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (64.5, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1417,
    label = "Cds-CbCs_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1520, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1418,
    label = "Cds-CbCs_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (342, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1419,
    label = "Cds-CbCs_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (87.2, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1420,
    label = "Cds-CbCs_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1421,
    label = "Cds-CbCs_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1422,
    label = "Cds-CbCs_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (3620, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1423,
    label = "Cds-CbCs_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1424,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (428, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1425,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (343, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1426,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (254, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1427,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (4450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1428,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (775, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1429,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1430,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1431,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (533, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1432,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1433,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (507, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1434,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (81.2, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1435,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1910, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1436,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1437,
    label = "Cds-CbCs_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1438,
    label = "Cds-CbCs_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2880, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1439,
    label = "Cds-CbCs_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1530, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1440,
    label = "Cds-CbCs_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (4560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1441,
    label = "Cds-CbCs_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1442,
    label = "Cds-CbCs_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (382, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1443,
    label = "Cds-CbCs_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (307, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1444,
    label = "Cds-CbCs_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (227, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1445,
    label = "Cds-CbCs_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (3970, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1446,
    label = "Cds-CbCs_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (691, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1447,
    label = "Cds-CbCs_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (89.4, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1448,
    label = "Cds-CbCs_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1449,
    label = "Cds-CbCs_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (476, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1450,
    label = "Cds-CbCs_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1451,
    label = "Cds-CbCs_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (453, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1452,
    label = "Cds-CbCs_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (72.4, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1453,
    label = "Cds-CbCs_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1454,
    label = "Cds-CbCs_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (384, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1455,
    label = "Cds-CbCs_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (97.9, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1456,
    label = "Cds-CbCs_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1457,
    label = "Cds-CbCs_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1458,
    label = "Cds-CbCs_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (4070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1459,
    label = "Cds-CbCs_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1460,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (434, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1461,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (348, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1462,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (258, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1463,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (4510, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1464,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (785, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1465,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (101, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1466,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1580, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1467,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1468,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2090, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1469,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (514, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1470,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (82.2, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1471,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1930, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1472,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (435, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1473,
    label = "Cds-CbCs_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (111, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1474,
    label = "Cds-CbCs_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1475,
    label = "Cds-CbCs_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1476,
    label = "Cds-CbCs_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (4610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1477,
    label = "Cds-CbCs_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (13000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1478,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1479,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1480,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (785, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1481,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (13700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1482,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1483,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (309, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1484,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4820, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1485,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1650, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1486,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (6370, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1487,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1488,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (251, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1489,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (5890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1490,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1491,
    label = "Cds-CbCs_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (339, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1492,
    label = "Cds-CbCs_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (8900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1493,
    label = "Cds-CbCs_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (4720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1494,
    label = "Cds-CbCs_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (14100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1495,
    label = "Cds-CbCs_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1496,
    label = "Cds-CbCs_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (125, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1497,
    label = "Cds-CbCs_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1498,
    label = "Cds-CbCs_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (74.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1499,
    label = "Cds-CbCs_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (1300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1500,
    label = "Cds-CbCs_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (226, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1501,
    label = "Cds-CbCs_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (29.2, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1502,
    label = "Cds-CbCs_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (455, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1503,
    label = "Cds-CbCs_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (155, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1504,
    label = "Cds-CbCs_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (601, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1505,
    label = "Cds-CbCs_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (148, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1506,
    label = "Cds-CbCs_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (23.6, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1507,
    label = "Cds-CbCs_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (555, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1508,
    label = "Cds-CbCs_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (125, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1509,
    label = "Cds-CbCs_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (32, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1510,
    label = "Cds-CbCs_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1511,
    label = "Cds-CbCs_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (445, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1512,
    label = "Cds-CbCs_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (1330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1513,
    label = "Cds-CbCs_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1514,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (265, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1515,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (212, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1516,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (157, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1517,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (2750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1518,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (479, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1519,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (61.9, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1520,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (965, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1521,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (329, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1522,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1523,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (313, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1524,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (50.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1525,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1526,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (266, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1527,
    label = "Cds-CbCs_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (67.8, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1528,
    label = "Cds-CbCs_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (1780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1529,
    label = "Cds-CbCs_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (945, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1530,
    label = "Cds-CbCs_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (2810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1531,
    label = "Cds-CbCs_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4880, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1532,
    label = "Cds-CbCs_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (495, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1533,
    label = "Cds-CbCs_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (397, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1534,
    label = "Cds-CbCs_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (294, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1535,
    label = "Cds-CbCs_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1536,
    label = "Cds-CbCs_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (896, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1537,
    label = "Cds-CbCs_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (116, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1538,
    label = "Cds-CbCs_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1539,
    label = "Cds-CbCs_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (617, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1540,
    label = "Cds-CbCs_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1541,
    label = "Cds-CbCs_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (587, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1542,
    label = "Cds-CbCs_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (93.9, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1543,
    label = "Cds-CbCs_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1544,
    label = "Cds-CbCs_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (497, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1545,
    label = "Cds-CbCs_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (127, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1546,
    label = "Cds-CbCs_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1547,
    label = "Cds-CbCs_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1548,
    label = "Cds-CbCs_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (5270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1549,
    label = "Cds-CbCs_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (4990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1550,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (507, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1551,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (407, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1552,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (301, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1553,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5270, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1554,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (918, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1555,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (119, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1556,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1557,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (632, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1558,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1559,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (601, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1560,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (96.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1561,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1562,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (509, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1563,
    label = "Cds-CbCs_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1564,
    label = "Cds-CbCs_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1565,
    label = "Cds-CbCs_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1566,
    label = "Cds-CbCs_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (5400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1567,
    label = "Cds-CbCs_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1568,
    label = "Cds-CbCs_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (366, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1569,
    label = "Cds-CbCs_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (294, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1570,
    label = "Cds-CbCs_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (217, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1571,
    label = "Cds-CbCs_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (3800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1572,
    label = "Cds-CbCs_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (662, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1573,
    label = "Cds-CbCs_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (85.6, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1574,
    label = "Cds-CbCs_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (21.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1575,
    label = "Cds-CbCs_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (456, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (20.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1576,
    label = "Cds-CbCs_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1577,
    label = "Cds-CbCs_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (434, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1578,
    label = "Cds-CbCs_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (69.4, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1579,
    label = "Cds-CbCs_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1580,
    label = "Cds-CbCs_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (367, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1581,
    label = "Cds-CbCs_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (93.7, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1582,
    label = "Cds-CbCs_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (2460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1583,
    label = "Cds-CbCs_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1310, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1584,
    label = "Cds-CbCs_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (3890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1585,
    label = "Cds-CtH_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (14600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1586,
    label = "Cds-CtH_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1587,
    label = "Cds-CtH_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1588,
    label = "Cds-CtH_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (880, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1589,
    label = "Cds-CtH_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (15400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1590,
    label = "Cds-CtH_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1591,
    label = "Cds-CtH_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (347, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1592,
    label = "Cds-CtH_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5410, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1593,
    label = "Cds-CtH_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1594,
    label = "Cds-CtH_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1595,
    label = "Cds-CtH_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1596,
    label = "Cds-CtH_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (281, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1597,
    label = "Cds-CtH_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1598,
    label = "Cds-CtH_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1599,
    label = "Cds-CtH_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1600,
    label = "Cds-CtH_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (9980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1601,
    label = "Cds-CtH_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1602,
    label = "Cds-CtH_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (15800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1603,
    label = "Cds-CtH_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (14600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1604,
    label = "Cds-CtH_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1605,
    label = "Cds-CtH_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1190, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1606,
    label = "Cds-CtH_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (884, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1607,
    label = "Cds-CtH_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (15500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1608,
    label = "Cds-CtH_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2690, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1609,
    label = "Cds-CtH_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (348, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1610,
    label = "Cds-CtH_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1611,
    label = "Cds-CtH_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1612,
    label = "Cds-CtH_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1613,
    label = "Cds-CtH_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1614,
    label = "Cds-CtH_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (282, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1615,
    label = "Cds-CtH_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (6630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1616,
    label = "Cds-CtH_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1617,
    label = "Cds-CtH_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (381, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1618,
    label = "Cds-CtH_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (10000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1619,
    label = "Cds-CtH_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5310, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1620,
    label = "Cds-CtH_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (15800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1621,
    label = "Cds-CtH_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (18400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1622,
    label = "Cds-CtH_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1623,
    label = "Cds-CtH_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1624,
    label = "Cds-CtH_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1625,
    label = "Cds-CtH_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (19400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1626,
    label = "Cds-CtH_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1627,
    label = "Cds-CtH_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (438, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1628,
    label = "Cds-CtH_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (6830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1629,
    label = "Cds-CtH_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1630,
    label = "Cds-CtH_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (9020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1631,
    label = "Cds-CtH_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1632,
    label = "Cds-CtH_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (355, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1633,
    label = "Cds-CtH_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (8340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1634,
    label = "Cds-CtH_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1880, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1635,
    label = "Cds-CtH_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1636,
    label = "Cds-CtH_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (12600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1637,
    label = "Cds-CtH_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (6690, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1638,
    label = "Cds-CtH_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (19900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1639,
    label = "Cds-CtH_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1640,
    label = "Cds-CtH_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1641,
    label = "Cds-CtH_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1642,
    label = "Cds-CtH_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (993, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1643,
    label = "Cds-CtH_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (17400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1644,
    label = "Cds-CtH_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1645,
    label = "Cds-CtH_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (391, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1646,
    label = "Cds-CtH_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (6100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1647,
    label = "Cds-CtH_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1648,
    label = "Cds-CtH_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (8050, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1649,
    label = "Cds-CtH_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1650,
    label = "Cds-CtH_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (317, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1651,
    label = "Cds-CtH_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (7440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1652,
    label = "Cds-CtH_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1653,
    label = "Cds-CtH_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (428, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1654,
    label = "Cds-CtH_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (11300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1655,
    label = "Cds-CtH_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5970, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1656,
    label = "Cds-CtH_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (17800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1657,
    label = "Cds-CtH_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (18700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1658,
    label = "Cds-CtH_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1659,
    label = "Cds-CtH_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1520, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1660,
    label = "Cds-CtH_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1661,
    label = "Cds-CtH_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (19700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1662,
    label = "Cds-CtH_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1663,
    label = "Cds-CtH_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (444, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1664,
    label = "Cds-CtH_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (6920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1665,
    label = "Cds-CtH_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1666,
    label = "Cds-CtH_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (9140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1667,
    label = "Cds-CtH_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2250, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1668,
    label = "Cds-CtH_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (359, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1669,
    label = "Cds-CtH_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (8440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1670,
    label = "Cds-CtH_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1671,
    label = "Cds-CtH_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (486, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1672,
    label = "Cds-CtH_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (12800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1673,
    label = "Cds-CtH_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (6770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1674,
    label = "Cds-CtH_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (20200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-3.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1675,
    label = "Cds-CtH_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (56900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1676,
    label = "Cds-CtH_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (5780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1677,
    label = "Cds-CtH_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (4630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1678,
    label = "Cds-CtH_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (3430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1679,
    label = "Cds-CtH_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (60000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1680,
    label = "Cds-CtH_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (10500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1681,
    label = "Cds-CtH_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (1350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1682,
    label = "Cds-CtH_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (21100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1683,
    label = "Cds-CtH_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (7200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1684,
    label = "Cds-CtH_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (27800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1685,
    label = "Cds-CtH_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (6850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1686,
    label = "Cds-CtH_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (1100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1687,
    label = "Cds-CtH_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (25700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1688,
    label = "Cds-CtH_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (5800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1689,
    label = "Cds-CtH_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (1480, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1690,
    label = "Cds-CtH_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (38900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1691,
    label = "Cds-CtH_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (20600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1692,
    label = "Cds-CtH_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (61500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-4.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1693,
    label = "Cds-CtH_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5370, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1694,
    label = "Cds-CtH_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (545, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1695,
    label = "Cds-CtH_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (437, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1696,
    label = "Cds-CtH_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (324, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1697,
    label = "Cds-CtH_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1698,
    label = "Cds-CtH_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (987, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1699,
    label = "Cds-CtH_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (128, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1700,
    label = "Cds-CtH_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (1990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1701,
    label = "Cds-CtH_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (679, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1702,
    label = "Cds-CtH_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1703,
    label = "Cds-CtH_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (646, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1704,
    label = "Cds-CtH_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (103, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1705,
    label = "Cds-CtH_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1706,
    label = "Cds-CtH_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (548, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1707,
    label = "Cds-CtH_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1708,
    label = "Cds-CtH_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1709,
    label = "Cds-CtH_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1950, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1710,
    label = "Cds-CtH_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (5800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1711,
    label = "Cds-CtH_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (11400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1712,
    label = "Cds-CtH_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1713,
    label = "Cds-CtH_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (928, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1714,
    label = "Cds-CtH_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (687, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1715,
    label = "Cds-CtH_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (12000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1716,
    label = "Cds-CtH_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2090, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1717,
    label = "Cds-CtH_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (271, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1718,
    label = "Cds-CtH_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1719,
    label = "Cds-CtH_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1720,
    label = "Cds-CtH_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (5570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1721,
    label = "Cds-CtH_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1370, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1722,
    label = "Cds-CtH_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (219, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1723,
    label = "Cds-CtH_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (5150, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1724,
    label = "Cds-CtH_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1725,
    label = "Cds-CtH_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (296, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1726,
    label = "Cds-CtH_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (7790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1727,
    label = "Cds-CtH_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (4130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1728,
    label = "Cds-CtH_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (12300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1729,
    label = "Cds-CtH_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (21300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1730,
    label = "Cds-CtH_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1731,
    label = "Cds-CtH_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1732,
    label = "Cds-CtH_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1733,
    label = "Cds-CtH_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (22500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1734,
    label = "Cds-CtH_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (3920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1735,
    label = "Cds-CtH_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (507, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1736,
    label = "Cds-CtH_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (7900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1737,
    label = "Cds-CtH_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1738,
    label = "Cds-CtH_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (10400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1739,
    label = "Cds-CtH_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1740,
    label = "Cds-CtH_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (411, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1741,
    label = "Cds-CtH_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (9640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1742,
    label = "Cds-CtH_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1743,
    label = "Cds-CtH_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (555, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1744,
    label = "Cds-CtH_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (14600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1745,
    label = "Cds-CtH_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (7730, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1746,
    label = "Cds-CtH_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (23000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1747,
    label = "Cds-CtH_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (21800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1748,
    label = "Cds-CtH_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1749,
    label = "Cds-CtH_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1750,
    label = "Cds-CtH_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1751,
    label = "Cds-CtH_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (23000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1752,
    label = "Cds-CtH_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (4010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1753,
    label = "Cds-CtH_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (519, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1754,
    label = "Cds-CtH_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (8090, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1755,
    label = "Cds-CtH_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1756,
    label = "Cds-CtH_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (10700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1757,
    label = "Cds-CtH_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1758,
    label = "Cds-CtH_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1759,
    label = "Cds-CtH_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (9870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1760,
    label = "Cds-CtH_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1761,
    label = "Cds-CtH_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (568, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1762,
    label = "Cds-CtH_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (14900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1763,
    label = "Cds-CtH_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (7920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1764,
    label = "Cds-CtH_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (23600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-3.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1765,
    label = "Cds-CtH_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (15800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1766,
    label = "Cds-CtH_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1767,
    label = "Cds-CtH_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1280, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1768,
    label = "Cds-CtH_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (951, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1769,
    label = "Cds-CtH_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (16600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1770,
    label = "Cds-CtH_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1771,
    label = "Cds-CtH_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (374, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1772,
    label = "Cds-CtH_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (5840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1773,
    label = "Cds-CtH_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1774,
    label = "Cds-CtH_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (7710, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1775,
    label = "Cds-CtH_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1776,
    label = "Cds-CtH_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (303, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1777,
    label = "Cds-CtH_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (7120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1778,
    label = "Cds-CtH_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1779,
    label = "Cds-CtH_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (410, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1780,
    label = "Cds-CtH_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (10800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1781,
    label = "Cds-CtH_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (5710, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1782,
    label = "Cds-CtH_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (17000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1783,
    label = "Cds-CtCs_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1784,
    label = "Cds-CtCs_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (712, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1785,
    label = "Cds-CtCs_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (571, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1786,
    label = "Cds-CtCs_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (423, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1787,
    label = "Cds-CtCs_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (7390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1788,
    label = "Cds-CtCs_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1789,
    label = "Cds-CtCs_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (167, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1790,
    label = "Cds-CtCs_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1791,
    label = "Cds-CtCs_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (887, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1792,
    label = "Cds-CtCs_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1793,
    label = "Cds-CtCs_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (843, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1794,
    label = "Cds-CtCs_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (135, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1795,
    label = "Cds-CtCs_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1796,
    label = "Cds-CtCs_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (715, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1797,
    label = "Cds-CtCs_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (182, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1798,
    label = "Cds-CtCs_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (4790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1799,
    label = "Cds-CtCs_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1800,
    label = "Cds-CtCs_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (7570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1801,
    label = "Cds-CtCs_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7040, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1802,
    label = "Cds-CtCs_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (715, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1803,
    label = "Cds-CtCs_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (573, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1804,
    label = "Cds-CtCs_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (425, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1805,
    label = "Cds-CtCs_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (7430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1806,
    label = "Cds-CtCs_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1807,
    label = "Cds-CtCs_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (167, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1808,
    label = "Cds-CtCs_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1809,
    label = "Cds-CtCs_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1810,
    label = "Cds-CtCs_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1811,
    label = "Cds-CtCs_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (847, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1812,
    label = "Cds-CtCs_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (135, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1813,
    label = "Cds-CtCs_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1814,
    label = "Cds-CtCs_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (718, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1815,
    label = "Cds-CtCs_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (183, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1816,
    label = "Cds-CtCs_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (4810, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1817,
    label = "Cds-CtCs_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1818,
    label = "Cds-CtCs_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (7600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1819,
    label = "Cds-CtCs_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (8850, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1820,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (899, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1821,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (721, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1822,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (534, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1823,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (9340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1824,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1825,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1826,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3280, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1827,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1120, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1828,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1829,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1830,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1831,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1832,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (903, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1833,
    label = "Cds-CtCs_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1834,
    label = "Cds-CtCs_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (6060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1835,
    label = "Cds-CtCs_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1836,
    label = "Cds-CtCs_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (9570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1837,
    label = "Cds-CtCs_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1838,
    label = "Cds-CtCs_Cds-CdH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (803, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1839,
    label = "Cds-CtCs_Cds-CdH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (644, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1840,
    label = "Cds-CtCs_Cds-CdH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (477, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1841,
    label = "Cds-CtCs_Cds-CdH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (8340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1842,
    label = "Cds-CtCs_Cds-CdH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1843,
    label = "Cds-CtCs_Cds-CdH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (188, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1844,
    label = "Cds-CtCs_Cds-CdH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2930, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1845,
    label = "Cds-CtCs_Cds-CdH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1846,
    label = "Cds-CtCs_Cds-CdH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1847,
    label = "Cds-CtCs_Cds-CdH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (951, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1848,
    label = "Cds-CtCs_Cds-CdH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (152, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1849,
    label = "Cds-CtCs_Cds-CdH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1850,
    label = "Cds-CtCs_Cds-CdH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (806, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1851,
    label = "Cds-CtCs_Cds-CdH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (206, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1852,
    label = "Cds-CtCs_Cds-CdH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (5410, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1853,
    label = "Cds-CtCs_Cds-CdH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1854,
    label = "Cds-CtCs_Cds-CdH;CbJ",
    kinetics = ArrheniusEP(
        A = (8540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1855,
    label = "Cds-CtCs_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (8970, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1856,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (911, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1857,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (731, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1858,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (541, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1859,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (9460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1860,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1650, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1861,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (213, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1862,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3320, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1863,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1864,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (4390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1865,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1080, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1866,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (173, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1867,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1868,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (915, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1869,
    label = "Cds-CtCs_Cds-CdCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (233, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1870,
    label = "Cds-CtCs_Cds-CdCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (6130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1871,
    label = "Cds-CtCs_Cds-CdCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3250, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1872,
    label = "Cds-CtCs_Cds-CdCs;CbJ",
    kinetics = ArrheniusEP(
        A = (9690, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1873,
    label = "Cds-CtCs_Cds-CdCd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (27300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1874,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2780, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1875,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (2230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1876,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1650, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1877,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (28800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1878,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (5020, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1879,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (650, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1880,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (10100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1881,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (3460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1882,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (13400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1883,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (3290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1884,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (526, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1885,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (12400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1886,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1887,
    label = "Cds-CtCs_Cds-CdCd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (711, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1888,
    label = "Cds-CtCs_Cds-CdCd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (18700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1889,
    label = "Cds-CtCs_Cds-CdCd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (9910, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1890,
    label = "Cds-CtCs_Cds-CdCd;CbJ",
    kinetics = ArrheniusEP(
        A = (29500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1891,
    label = "Cds-CtCs_Cds-CbH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2580, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1892,
    label = "Cds-CtCs_Cds-CbH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (262, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1893,
    label = "Cds-CtCs_Cds-CbH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1894,
    label = "Cds-CtCs_Cds-CbH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (156, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1895,
    label = "Cds-CtCs_Cds-CbH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (2720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1896,
    label = "Cds-CtCs_Cds-CbH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (474, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1897,
    label = "Cds-CtCs_Cds-CbH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (61.3, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1898,
    label = "Cds-CtCs_Cds-CbH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (956, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1899,
    label = "Cds-CtCs_Cds-CbH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (326, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1900,
    label = "Cds-CtCs_Cds-CbH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (1260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1901,
    label = "Cds-CtCs_Cds-CbH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (310, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1902,
    label = "Cds-CtCs_Cds-CbH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (49.7, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1903,
    label = "Cds-CtCs_Cds-CbH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1904,
    label = "Cds-CtCs_Cds-CbH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (263, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1905,
    label = "Cds-CtCs_Cds-CbH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (67.1, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1906,
    label = "Cds-CtCs_Cds-CbH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (1760, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1907,
    label = "Cds-CtCs_Cds-CbH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (936, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1908,
    label = "Cds-CtCs_Cds-CbH;CbJ",
    kinetics = ArrheniusEP(
        A = (2790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1909,
    label = "Cds-CtCs_Cds-CbCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1910,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (556, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1911,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (446, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1912,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1913,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (5770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1914,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1915,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1916,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2030, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1917,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (692, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1918,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (2680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1919,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (658, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1920,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (105, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1921,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (2470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1922,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (558, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1923,
    label = "Cds-CtCs_Cds-CbCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (142, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1924,
    label = "Cds-CtCs_Cds-CbCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1925,
    label = "Cds-CtCs_Cds-CbCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1926,
    label = "Cds-CtCs_Cds-CbCs;CbJ",
    kinetics = ArrheniusEP(
        A = (5910, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1927,
    label = "Cds-CtCs_Cds-CtH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (10200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1928,
    label = "Cds-CtCs_Cds-CtH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1040, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1929,
    label = "Cds-CtCs_Cds-CtH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (834, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1930,
    label = "Cds-CtCs_Cds-CtH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (618, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1931,
    label = "Cds-CtCs_Cds-CtH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (10800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1932,
    label = "Cds-CtCs_Cds-CtH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1880, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1933,
    label = "Cds-CtCs_Cds-CtH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (243, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1934,
    label = "Cds-CtCs_Cds-CtH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1935,
    label = "Cds-CtCs_Cds-CtH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1936,
    label = "Cds-CtCs_Cds-CtH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (5010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1937,
    label = "Cds-CtCs_Cds-CtH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1938,
    label = "Cds-CtCs_Cds-CtH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (197, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1939,
    label = "Cds-CtCs_Cds-CtH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4630, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1940,
    label = "Cds-CtCs_Cds-CtH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1040, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1941,
    label = "Cds-CtCs_Cds-CtH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (266, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1942,
    label = "Cds-CtCs_Cds-CtH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (7010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1943,
    label = "Cds-CtCs_Cds-CtH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3720, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1944,
    label = "Cds-CtCs_Cds-CtH;CbJ",
    kinetics = ArrheniusEP(
        A = (11100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1945,
    label = "Cds-CtCs_Cds-CtCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (10500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1946,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1947,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (854, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1948,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (633, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1949,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (11100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1950,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1930, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1951,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (249, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1952,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (3890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1953,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1954,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (5130, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1955,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1956,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (202, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1957,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (4740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1958,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1959,
    label = "Cds-CtCs_Cds-CtCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (273, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1960,
    label = "Cds-CtCs_Cds-CtCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (7170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1961,
    label = "Cds-CtCs_Cds-CtCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (3800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1962,
    label = "Cds-CtCs_Cds-CtCs;CbJ",
    kinetics = ArrheniusEP(
        A = (11300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1963,
    label = "Cds-CtCs_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7570, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1964,
    label = "Cds-CtCs_Ca;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (769, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1965,
    label = "Cds-CtCs_Ca;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (616, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1966,
    label = "Cds-CtCs_Ca;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (457, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1967,
    label = "Cds-CtCs_Ca;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (7980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1968,
    label = "Cds-CtCs_Ca;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (1390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1969,
    label = "Cds-CtCs_Ca;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1970,
    label = "Cds-CtCs_Ca;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (2800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1971,
    label = "Cds-CtCs_Ca;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (957, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1972,
    label = "Cds-CtCs_Ca;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (3700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1973,
    label = "Cds-CtCs_Ca;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (911, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1974,
    label = "Cds-CtCs_Ca;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (146, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1975,
    label = "Cds-CtCs_Ca;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (3420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1976,
    label = "Cds-CtCs_Ca;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (772, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1977,
    label = "Cds-CtCs_Ca;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (197, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1978,
    label = "Cds-CtCs_Ca;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (5180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1979,
    label = "Cds-CtCs_Ca;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (2740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1980,
    label = "Cds-CtCs_Ca;CbJ",
    kinetics = ArrheniusEP(
        A = (8180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1981,
    label = "Ca_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (39000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1982,
    label = "Ca_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (3960, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1983,
    label = "Ca_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (3180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1984,
    label = "Ca_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (2350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1985,
    label = "Ca_Cds-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (41200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1986,
    label = "Ca_Cds-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (7170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1987,
    label = "Ca_Cds-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (927, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1988,
    label = "Ca_Cds-HH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (14500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1989,
    label = "Ca_Cds-HH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (4940, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1990,
    label = "Ca_Cds-HH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (19100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1991,
    label = "Ca_Cds-HH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (4690, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1992,
    label = "Ca_Cds-HH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (751, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1993,
    label = "Ca_Cds-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (17600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1994,
    label = "Ca_Cds-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (3980, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1995,
    label = "Ca_Cds-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (1010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1996,
    label = "Ca_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (26700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1997,
    label = "Ca_Cds-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (14200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1998,
    label = "Ca_Cds-HH;CbJ",
    kinetics = ArrheniusEP(
        A = (42200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 1999,
    label = "Ca_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (44700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2000,
    label = "Ca_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (4540, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2001,
    label = "Ca_Cds-CsH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (3640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2002,
    label = "Ca_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (2700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2003,
    label = "Ca_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (47200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2004,
    label = "Ca_Cds-CsH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (8220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2005,
    label = "Ca_Cds-CsH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (1060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2006,
    label = "Ca_Cds-CsH;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (16600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2007,
    label = "Ca_Cds-CsH;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (5660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2008,
    label = "Ca_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (21900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2009,
    label = "Ca_Cds-CsH;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (5380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2010,
    label = "Ca_Cds-CsH;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (861, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2011,
    label = "Ca_Cds-CsH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (20200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2012,
    label = "Ca_Cds-CsH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (4560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2013,
    label = "Ca_Cds-CsH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (1160, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2014,
    label = "Ca_Cds-CsH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (30600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2015,
    label = "Ca_Cds-CsH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (16200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2016,
    label = "Ca_Cds-CsH;CbJ",
    kinetics = ArrheniusEP(
        A = (48300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2017,
    label = "Ca_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (57300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2018,
    label = "Ca_Cds-CsCs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (5820, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2019,
    label = "Ca_Cds-CsCs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (4670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.08, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2020,
    label = "Ca_Cds-CsCs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (3460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2021,
    label = "Ca_Cds-CsCs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (60500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2022,
    label = "Ca_Cds-CsCs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (10500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2023,
    label = "Ca_Cds-CsCs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (1360, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2024,
    label = "Ca_Cds-CsCs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (21200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2025,
    label = "Ca_Cds-CsCs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (7250, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2026,
    label = "Ca_Cds-CsCs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2027,
    label = "Ca_Cds-CsCs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (6890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2028,
    label = "Ca_Cds-CsCs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (1100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2029,
    label = "Ca_Cds-CsCs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (25900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2030,
    label = "Ca_Cds-CsCs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (5840, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2031,
    label = "Ca_Cds-CsCs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (1490, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2032,
    label = "Ca_Cds-CsCs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (39200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2033,
    label = "Ca_Cds-CsCs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (20800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2034,
    label = "Ca_Cds-CsCs;CbJ",
    kinetics = ArrheniusEP(
        A = (61900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2035,
    label = "Ct-H_Ct-H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (66900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2036,
    label = "Ct-H_Ct-H;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (6800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2037,
    label = "Ct-H_Ct-H;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (5450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2038,
    label = "Ct-H_Ct-H;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (4040, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2039,
    label = "Ct-H_Ct-H;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (70600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2040,
    label = "Ct-H_Ct-H;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (12300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2041,
    label = "Ct-H_Ct-H;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (1590, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2042,
    label = "Ct-H_Ct-H;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (24800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2043,
    label = "Ct-H_Ct-H;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (8470, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2044,
    label = "Ct-H_Ct-H;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (32800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2045,
    label = "Ct-H_Ct-H;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (8060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2046,
    label = "Ct-H_Ct-H;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (1290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2047,
    label = "Ct-H_Ct-H;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (30300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2048,
    label = "Ct-H_Ct-H;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (6830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2049,
    label = "Ct-H_Ct-H;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (1740, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2050,
    label = "Ct-H_Ct-H;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (45800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2051,
    label = "Ct-H_Ct-H;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (24300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2052,
    label = "Ct-H_Ct-H;CbJ",
    kinetics = ArrheniusEP(
        A = (72300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2053,
    label = "Ct-H_Ct-Cs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (178000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2054,
    label = "Ct-H_Ct-Cs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (18100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2055,
    label = "Ct-H_Ct-Cs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (14500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2056,
    label = "Ct-H_Ct-Cs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (10700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2057,
    label = "Ct-H_Ct-Cs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (188000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2058,
    label = "Ct-H_Ct-Cs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (32700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2059,
    label = "Ct-H_Ct-Cs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (4220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2060,
    label = "Ct-H_Ct-Cs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (65900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2061,
    label = "Ct-H_Ct-Cs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (22500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (17.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2062,
    label = "Ct-H_Ct-Cs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (87000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2063,
    label = "Ct-H_Ct-Cs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (21400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2064,
    label = "Ct-H_Ct-Cs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (3420, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2065,
    label = "Ct-H_Ct-Cs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (80400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2066,
    label = "Ct-H_Ct-Cs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (18100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2067,
    label = "Ct-H_Ct-Cs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (4620, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2068,
    label = "Ct-H_Ct-Cs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (122000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2069,
    label = "Ct-H_Ct-Cs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (64500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2070,
    label = "Ct-H_Ct-Cs;CbJ",
    kinetics = ArrheniusEP(
        A = (192000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2071,
    label = "Ct-H_Ct-Cd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (21700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2072,
    label = "Ct-H_Ct-Cd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2073,
    label = "Ct-H_Ct-Cd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2074,
    label = "Ct-H_Ct-Cd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (1310, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2075,
    label = "Ct-H_Ct-Cd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (22900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2076,
    label = "Ct-H_Ct-Cd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (4000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2077,
    label = "Ct-H_Ct-Cd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (517, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2078,
    label = "Ct-H_Ct-Cd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (8060, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2079,
    label = "Ct-H_Ct-Cd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (2750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2080,
    label = "Ct-H_Ct-Cd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (10600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2081,
    label = "Ct-H_Ct-Cd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (2620, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2082,
    label = "Ct-H_Ct-Cd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (419, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2083,
    label = "Ct-H_Ct-Cd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (9830, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2084,
    label = "Ct-H_Ct-Cd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2085,
    label = "Ct-H_Ct-Cd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (566, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2086,
    label = "Ct-H_Ct-Cd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (14900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2087,
    label = "Ct-H_Ct-Cd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (7890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2088,
    label = "Ct-H_Ct-Cd;CbJ",
    kinetics = ArrheniusEP(
        A = (23500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2089,
    label = "Ct-H_Ct-Ct;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (289000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2090,
    label = "Ct-H_Ct-Ct;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (29300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2091,
    label = "Ct-H_Ct-Ct;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (23500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2092,
    label = "Ct-H_Ct-Ct;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (17400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2093,
    label = "Ct-H_Ct-Ct;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (305000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2094,
    label = "Ct-H_Ct-Ct;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (53100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2095,
    label = "Ct-H_Ct-Ct;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (6860, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2096,
    label = "Ct-H_Ct-Ct;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (107000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2097,
    label = "Ct-H_Ct-Ct;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (36500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2098,
    label = "Ct-H_Ct-Ct;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (141000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2099,
    label = "Ct-H_Ct-Ct;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (34700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2100,
    label = "Ct-H_Ct-Ct;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (5560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2101,
    label = "Ct-H_Ct-Ct;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (131000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2102,
    label = "Ct-H_Ct-Ct;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (29400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2103,
    label = "Ct-H_Ct-Ct;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (7510, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2104,
    label = "Ct-H_Ct-Ct;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (197000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2105,
    label = "Ct-H_Ct-Ct;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (105000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2106,
    label = "Ct-H_Ct-Ct;CbJ",
    kinetics = ArrheniusEP(
        A = (312000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-2.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2107,
    label = "Ct-Cs_Ct-H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (138000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2108,
    label = "Ct-Cs_Ct-H;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2109,
    label = "Ct-Cs_Ct-H;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (11300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2110,
    label = "Ct-Cs_Ct-H;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (8350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2111,
    label = "Ct-Cs_Ct-H;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (146000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2112,
    label = "Ct-Cs_Ct-H;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (25400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2113,
    label = "Ct-Cs_Ct-H;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (3290, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2114,
    label = "Ct-Cs_Ct-H;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (51300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2115,
    label = "Ct-Cs_Ct-H;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (17500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2116,
    label = "Ct-Cs_Ct-H;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (67700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2117,
    label = "Ct-Cs_Ct-H;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (16600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2118,
    label = "Ct-Cs_Ct-H;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (2660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2119,
    label = "Ct-Cs_Ct-H;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (62600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2120,
    label = "Ct-Cs_Ct-H;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (14100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2121,
    label = "Ct-Cs_Ct-H;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (3600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2122,
    label = "Ct-Cs_Ct-H;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (94600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2123,
    label = "Ct-Cs_Ct-H;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (50200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2124,
    label = "Ct-Cs_Ct-H;CbJ",
    kinetics = ArrheniusEP(
        A = (150000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2125,
    label = "Ct-Cs_Ct-Cs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (367000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2126,
    label = "Ct-Cs_Ct-Cs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (37300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2127,
    label = "Ct-Cs_Ct-Cs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (29900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2128,
    label = "Ct-Cs_Ct-Cs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (22200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2129,
    label = "Ct-Cs_Ct-Cs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (388000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2130,
    label = "Ct-Cs_Ct-Cs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (67500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.28, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2131,
    label = "Ct-Cs_Ct-Cs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (8730, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2132,
    label = "Ct-Cs_Ct-Cs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (136000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (20.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2133,
    label = "Ct-Cs_Ct-Cs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (46500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2134,
    label = "Ct-Cs_Ct-Cs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (180000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2135,
    label = "Ct-Cs_Ct-Cs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (44200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2136,
    label = "Ct-Cs_Ct-Cs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (7070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2137,
    label = "Ct-Cs_Ct-Cs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (166000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2138,
    label = "Ct-Cs_Ct-Cs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (37500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2139,
    label = "Ct-Cs_Ct-Cs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (9560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2140,
    label = "Ct-Cs_Ct-Cs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (251000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2141,
    label = "Ct-Cs_Ct-Cs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (133000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2142,
    label = "Ct-Cs_Ct-Cs;CbJ",
    kinetics = ArrheniusEP(
        A = (397000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2143,
    label = "Ct-Cs_Ct-Cd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (44900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2144,
    label = "Ct-Cs_Ct-Cd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (4560, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2145,
    label = "Ct-Cs_Ct-Cd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (3660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2146,
    label = "Ct-Cs_Ct-Cd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (2710, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2147,
    label = "Ct-Cs_Ct-Cd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (47400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2148,
    label = "Ct-Cs_Ct-Cd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (8260, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2149,
    label = "Ct-Cs_Ct-Cd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (1070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2150,
    label = "Ct-Cs_Ct-Cd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (16700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2151,
    label = "Ct-Cs_Ct-Cd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (5680, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2152,
    label = "Ct-Cs_Ct-Cd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (22000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2153,
    label = "Ct-Cs_Ct-Cd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (5410, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2154,
    label = "Ct-Cs_Ct-Cd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (865, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2155,
    label = "Ct-Cs_Ct-Cd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (20300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2156,
    label = "Ct-Cs_Ct-Cd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (4580, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2157,
    label = "Ct-Cs_Ct-Cd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (1170, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2158,
    label = "Ct-Cs_Ct-Cd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (30700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2159,
    label = "Ct-Cs_Ct-Cd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (16300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2160,
    label = "Ct-Cs_Ct-Cd;CbJ",
    kinetics = ArrheniusEP(
        A = (48600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2161,
    label = "Ct-Cs_Ct-Ct;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (597000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2162,
    label = "Ct-Cs_Ct-Ct;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (60600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2163,
    label = "Ct-Cs_Ct-Ct;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (48600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2164,
    label = "Ct-Cs_Ct-Ct;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (36000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2165,
    label = "Ct-Cs_Ct-Ct;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (630000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2166,
    label = "Ct-Cs_Ct-Ct;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (110000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2167,
    label = "Ct-Cs_Ct-Ct;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (14200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2168,
    label = "Ct-Cs_Ct-Ct;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (221000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2169,
    label = "Ct-Cs_Ct-Ct;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (75500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2170,
    label = "Ct-Cs_Ct-Ct;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (292000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2171,
    label = "Ct-Cs_Ct-Ct;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (71800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2172,
    label = "Ct-Cs_Ct-Ct;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (11500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2173,
    label = "Ct-Cs_Ct-Ct;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (270000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2174,
    label = "Ct-Cs_Ct-Ct;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (60800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2175,
    label = "Ct-Cs_Ct-Ct;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (15500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2176,
    label = "Ct-Cs_Ct-Ct;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (408000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2177,
    label = "Ct-Cs_Ct-Ct;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (216000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2178,
    label = "Ct-Cs_Ct-Ct;CbJ",
    kinetics = ArrheniusEP(
        A = (645000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2179,
    label = "Ct-Cd_Ct-H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (36900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2180,
    label = "Ct-Cd_Ct-H;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (3750, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2181,
    label = "Ct-Cd_Ct-H;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (3010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2182,
    label = "Ct-Cd_Ct-H;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (2230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2183,
    label = "Ct-Cd_Ct-H;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (39000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2184,
    label = "Ct-Cd_Ct-H;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (6790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2185,
    label = "Ct-Cd_Ct-H;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (878, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2186,
    label = "Ct-Cd_Ct-H;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (13700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2187,
    label = "Ct-Cd_Ct-H;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (4670, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2188,
    label = "Ct-Cd_Ct-H;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (18100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2189,
    label = "Ct-Cd_Ct-H;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (4440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2190,
    label = "Ct-Cd_Ct-H;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (711, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2191,
    label = "Ct-Cd_Ct-H;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (16700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2192,
    label = "Ct-Cd_Ct-H;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (3770, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2193,
    label = "Ct-Cd_Ct-H;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (961, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2194,
    label = "Ct-Cd_Ct-H;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (25300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2195,
    label = "Ct-Cd_Ct-H;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (13400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2196,
    label = "Ct-Cd_Ct-H;CbJ",
    kinetics = ArrheniusEP(
        A = (39900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2197,
    label = "Ct-Cd_Ct-Cs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (98100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2198,
    label = "Ct-Cd_Ct-Cs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (9960, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2199,
    label = "Ct-Cd_Ct-Cs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (7990, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2200,
    label = "Ct-Cd_Ct-Cs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (5920, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2201,
    label = "Ct-Cd_Ct-Cs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (103000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2202,
    label = "Ct-Cd_Ct-Cs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (18000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2203,
    label = "Ct-Cd_Ct-Cs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (2330, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2204,
    label = "Ct-Cd_Ct-Cs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (36300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2205,
    label = "Ct-Cd_Ct-Cs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (12400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2206,
    label = "Ct-Cd_Ct-Cs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (48000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2207,
    label = "Ct-Cd_Ct-Cs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (11800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2208,
    label = "Ct-Cd_Ct-Cs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (1890, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2209,
    label = "Ct-Cd_Ct-Cs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (44400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2210,
    label = "Ct-Cd_Ct-Cs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (10000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2211,
    label = "Ct-Cd_Ct-Cs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (2550, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2212,
    label = "Ct-Cd_Ct-Cs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (67100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2213,
    label = "Ct-Cd_Ct-Cs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (35600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2214,
    label = "Ct-Cd_Ct-Cs;CbJ",
    kinetics = ArrheniusEP(
        A = (106000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2215,
    label = "Ct-Cd_Ct-Cd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (12000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2216,
    label = "Ct-Cd_Ct-Cd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2217,
    label = "Ct-Cd_Ct-Cd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (977, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2218,
    label = "Ct-Cd_Ct-Cd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (724, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2219,
    label = "Ct-Cd_Ct-Cd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (12700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2220,
    label = "Ct-Cd_Ct-Cd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2221,
    label = "Ct-Cd_Ct-Cd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (285, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2222,
    label = "Ct-Cd_Ct-Cd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (4450, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2223,
    label = "Ct-Cd_Ct-Cd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (1520, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2224,
    label = "Ct-Cd_Ct-Cd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (5870, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2225,
    label = "Ct-Cd_Ct-Cd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (1440, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2226,
    label = "Ct-Cd_Ct-Cd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (231, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2227,
    label = "Ct-Cd_Ct-Cd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (5430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2228,
    label = "Ct-Cd_Ct-Cd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (1220, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2229,
    label = "Ct-Cd_Ct-Cd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (312, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2230,
    label = "Ct-Cd_Ct-Cd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (8210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2231,
    label = "Ct-Cd_Ct-Cd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (4350, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2232,
    label = "Ct-Cd_Ct-Cd;CbJ",
    kinetics = ArrheniusEP(
        A = (13000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2233,
    label = "Ct-Cd_Ct-Ct;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (159000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2234,
    label = "Ct-Cd_Ct-Ct;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (16200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2235,
    label = "Ct-Cd_Ct-Ct;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (13000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2236,
    label = "Ct-Cd_Ct-Ct;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (9610, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2237,
    label = "Ct-Cd_Ct-Ct;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (168000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2238,
    label = "Ct-Cd_Ct-Ct;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (29300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2239,
    label = "Ct-Cd_Ct-Ct;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (3790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2240,
    label = "Ct-Cd_Ct-Ct;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (59000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2241,
    label = "Ct-Cd_Ct-Ct;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (20200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2242,
    label = "Ct-Cd_Ct-Ct;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (77900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2243,
    label = "Ct-Cd_Ct-Ct;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (19200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2244,
    label = "Ct-Cd_Ct-Ct;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (3070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2245,
    label = "Ct-Cd_Ct-Ct;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (72000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2246,
    label = "Ct-Cd_Ct-Ct;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (16200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2247,
    label = "Ct-Cd_Ct-Ct;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (4140, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2248,
    label = "Ct-Cd_Ct-Ct;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (109000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2249,
    label = "Ct-Cd_Ct-Ct;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (57800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2250,
    label = "Ct-Cd_Ct-Ct;CbJ",
    kinetics = ArrheniusEP(
        A = (172000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2251,
    label = "Ct-Ct_Ct-H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (102000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2252,
    label = "Ct-Ct_Ct-H;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (10400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2253,
    label = "Ct-Ct_Ct-H;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (8340, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (6.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2254,
    label = "Ct-Ct_Ct-H;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (6180, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2255,
    label = "Ct-Ct_Ct-H;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (108000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2256,
    label = "Ct-Ct_Ct-H;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (18800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2257,
    label = "Ct-Ct_Ct-H;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (2430, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2258,
    label = "Ct-Ct_Ct-H;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (37900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2259,
    label = "Ct-Ct_Ct-H;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (13000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (18.98, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2260,
    label = "Ct-Ct_Ct-H;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (50100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2261,
    label = "Ct-Ct_Ct-H;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (12300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2262,
    label = "Ct-Ct_Ct-H;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (1970, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2263,
    label = "Ct-Ct_Ct-H;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (46300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2264,
    label = "Ct-Ct_Ct-H;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (10400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2265,
    label = "Ct-Ct_Ct-H;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (2660, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2266,
    label = "Ct-Ct_Ct-H;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (70000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2267,
    label = "Ct-Ct_Ct-H;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (37100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2268,
    label = "Ct-Ct_Ct-H;CbJ",
    kinetics = ArrheniusEP(
        A = (111000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2269,
    label = "Ct-Ct_Ct-Cs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (272000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2270,
    label = "Ct-Ct_Ct-Cs;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (27600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2271,
    label = "Ct-Ct_Ct-Cs;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (22100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2272,
    label = "Ct-Ct_Ct-Cs;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (16400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2273,
    label = "Ct-Ct_Ct-Cs;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (287000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2274,
    label = "Ct-Ct_Ct-Cs;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (50000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (14.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2275,
    label = "Ct-Ct_Ct-Cs;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (6460, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (13.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2276,
    label = "Ct-Ct_Ct-Cs;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (101000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2277,
    label = "Ct-Ct_Ct-Cs;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (34400, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (19.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2278,
    label = "Ct-Ct_Ct-Cs;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (133000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2279,
    label = "Ct-Ct_Ct-Cs;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (32700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2280,
    label = "Ct-Ct_Ct-Cs;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (5230, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2281,
    label = "Ct-Ct_Ct-Cs;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (123000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2282,
    label = "Ct-Ct_Ct-Cs;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (27700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (12.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2283,
    label = "Ct-Ct_Ct-Cs;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (7070, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2284,
    label = "Ct-Ct_Ct-Cs;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (186000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2285,
    label = "Ct-Ct_Ct-Cs;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (98600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2286,
    label = "Ct-Ct_Ct-Cs;CbJ",
    kinetics = ArrheniusEP(
        A = (294000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2287,
    label = "Ct-Ct_Ct-Cd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (33300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (5.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2288,
    label = "Ct-Ct_Ct-Cd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (3380, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2289,
    label = "Ct-Ct_Ct-Cd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (2710, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2290,
    label = "Ct-Ct_Ct-Cd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (2010, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (2.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2291,
    label = "Ct-Ct_Ct-Cd;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (35100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2292,
    label = "Ct-Ct_Ct-Cd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (6110, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2293,
    label = "Ct-Ct_Ct-Cd;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (790, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.59, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2294,
    label = "Ct-Ct_Ct-Cd;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (12300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2295,
    label = "Ct-Ct_Ct-Cd;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (4210, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (16.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2296,
    label = "Ct-Ct_Ct-Cd;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (16300, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2297,
    label = "Ct-Ct_Ct-Cd;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (4000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2298,
    label = "Ct-Ct_Ct-Cd;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (640, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2299,
    label = "Ct-Ct_Ct-Cd;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (15000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (9.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2300,
    label = "Ct-Ct_Ct-Cd;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (3390, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2301,
    label = "Ct-Ct_Ct-Cd;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (865, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2302,
    label = "Ct-Ct_Ct-Cd;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (22700, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2303,
    label = "Ct-Ct_Ct-Cd;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (12100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2304,
    label = "Ct-Ct_Ct-Cd;CbJ",
    kinetics = ArrheniusEP(
        A = (35900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2305,
    label = "Ct-Ct_Ct-Ct;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (441000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2306,
    label = "Ct-Ct_Ct-Ct;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (44800, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2307,
    label = "Ct-Ct_Ct-Ct;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (36000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (3.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2308,
    label = "Ct-Ct_Ct-Ct;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (26600, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2309,
    label = "Ct-Ct_Ct-Ct;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (466000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2310,
    label = "Ct-Ct_Ct-Ct;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (81200, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2311,
    label = "Ct-Ct_Ct-Ct;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (10500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (10.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2312,
    label = "Ct-Ct_Ct-Ct;CsJ-CdCdH",
    kinetics = ArrheniusEP(
        A = (164000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2313,
    label = "Ct-Ct_Ct-Ct;CsJ-CdCdCs",
    kinetics = ArrheniusEP(
        A = (55900, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (15.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2314,
    label = "Ct-Ct_Ct-Ct;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (216000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2315,
    label = "Ct-Ct_Ct-Ct;CsJ-CbCsH",
    kinetics = ArrheniusEP(
        A = (53100, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2316,
    label = "Ct-Ct_Ct-Ct;CsJ-CbCsCs",
    kinetics = ArrheniusEP(
        A = (8500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.68, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2317,
    label = "Ct-Ct_Ct-Ct;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (200000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2318,
    label = "Ct-Ct_Ct-Ct;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (45000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2319,
    label = "Ct-Ct_Ct-Ct;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (11500, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (7.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2320,
    label = "Ct-Ct_Ct-Ct;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (302000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (1.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2321,
    label = "Ct-Ct_Ct-Ct;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (160000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (0.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2322,
    label = "Ct-Ct_Ct-Ct;CbJ",
    kinetics = ArrheniusEP(
        A = (477000, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (-1.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2323,
    label = "Cds-HH_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (2.31e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2324,
    label = "Cds-HH_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (2.48e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2325,
    label = "Cds-HH_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (2.88e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-0.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2326,
    label = "Cds-HH_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (2.31e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-0.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2327,
    label = "Cds-HH_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (2.58e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-0.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2328,
    label = "Cds-HH_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (2.48e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2329,
    label = "Cds-HH_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (2.23e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-0.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2330,
    label = "Cds-HH_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (2.56e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-0.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2331,
    label = "Cds-HH_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (7.57e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-1.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2332,
    label = "Cds-HH_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (2.25e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-0.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2333,
    label = "Cds-HH_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (6e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.55, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2334,
    label = "Cds-HH_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.77e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2335,
    label = "Cds-HH_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (2.09e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2336,
    label = "Cds-CsH_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.36e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2337,
    label = "Cds-CsH_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.46e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2338,
    label = "Cds-CsH_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.69e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2339,
    label = "Cds-CsH_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (1.35e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2340,
    label = "Cds-CsH_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.52e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2341,
    label = "Cds-CsH_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (1.46e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-0.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2342,
    label = "Cds-CsH_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (1.31e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2343,
    label = "Cds-CsH_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2344,
    label = "Cds-CsH_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (4.44e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-0.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2345,
    label = "Cds-CsH_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (1.32e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2346,
    label = "Cds-CsH_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (3.52e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2347,
    label = "Cds-CsH_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.04e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2348,
    label = "Cds-CsH_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (1.23e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2349,
    label = "Cds-CsCs_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (7.2e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2350,
    label = "Cds-CsCs_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (7.72e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2351,
    label = "Cds-CsCs_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (8.96e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.65, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2352,
    label = "Cds-CsCs_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (7.17e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2353,
    label = "Cds-CsCs_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (8.03e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2354,
    label = "Cds-CsCs_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (7.71e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2355,
    label = "Cds-CsCs_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (6.92e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2356,
    label = "Cds-CsCs_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (7.96e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2357,
    label = "Cds-CsCs_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (2.35e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.37, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2358,
    label = "Cds-CsCs_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (6.98e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2359,
    label = "Cds-CsCs_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (1.87e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2360,
    label = "Cds-CsCs_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (5.5e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2361,
    label = "Cds-CsCs_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (6.51e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2362,
    label = "Cds-CdH_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.62e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2363,
    label = "Cds-CdH_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.74e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.91, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2364,
    label = "Cds-CdH_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (2.02e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.39, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2365,
    label = "Cds-CdH_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (1.62e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.92, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2366,
    label = "Cds-CdH_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.81e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2367,
    label = "Cds-CdH_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (1.74e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-0.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2368,
    label = "Cds-CdH_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (1.56e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2369,
    label = "Cds-CdH_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.79e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2370,
    label = "Cds-CdH_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (5.31e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2371,
    label = "Cds-CdH_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (1.57e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2372,
    label = "Cds-CdH_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (4.2e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2373,
    label = "Cds-CdH_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.24e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2374,
    label = "Cds-CdH_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (1.47e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2375,
    label = "Cds-CdCs_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.04e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2376,
    label = "Cds-CdCs_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.11e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2377,
    label = "Cds-CdCs_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.29e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2378,
    label = "Cds-CdCs_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (1.03e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.67, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2379,
    label = "Cds-CdCs_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.16e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2380,
    label = "Cds-CdCs_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (1.11e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2381,
    label = "Cds-CdCs_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (9.97e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2382,
    label = "Cds-CdCs_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2383,
    label = "Cds-CdCs_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (3.39e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.86, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2384,
    label = "Cds-CdCs_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (1.01e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2385,
    label = "Cds-CdCs_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (2.69e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2386,
    label = "Cds-CdCs_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (7.92e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2387,
    label = "Cds-CdCs_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (9.38e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2388,
    label = "Cds-CdCd_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.35e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2389,
    label = "Cds-CdCd_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.45e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2390,
    label = "Cds-CdCd_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.68e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2391,
    label = "Cds-CdCd_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (1.34e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2392,
    label = "Cds-CdCd_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.51e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2393,
    label = "Cds-CdCd_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (1.45e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.38, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2394,
    label = "Cds-CdCd_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (1.3e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2395,
    label = "Cds-CdCd_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.49e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2396,
    label = "Cds-CdCd_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (4.41e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2397,
    label = "Cds-CdCd_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (1.31e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2398,
    label = "Cds-CdCd_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (3.5e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.33, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2399,
    label = "Cds-CdCd_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.03e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2400,
    label = "Cds-CdCd_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (1.22e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2401,
    label = "Cds-CtH_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.49e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2402,
    label = "Cds-CtH_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.6e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2403,
    label = "Cds-CtH_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.85e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2404,
    label = "Cds-CtH_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (1.48e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2405,
    label = "Cds-CtH_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.66e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2406,
    label = "Cds-CtH_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (1.59e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.21, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2407,
    label = "Cds-CtH_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (1.43e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2408,
    label = "Cds-CtH_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.65e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2409,
    label = "Cds-CtH_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (4.87e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2410,
    label = "Cds-CtH_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (1.44e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (0.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2411,
    label = "Cds-CtH_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (3.86e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2412,
    label = "Cds-CtH_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.14e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2413,
    label = "Cds-CtH_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (1.35e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2414,
    label = "Cds-CtCs_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (9.17e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2415,
    label = "Cds-CtCs_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (9.84e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2416,
    label = "Cds-CtCs_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.14e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.72, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2417,
    label = "Cds-CtCs_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (9.13e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.25, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2418,
    label = "Cds-CtCs_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.02e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2419,
    label = "Cds-CtCs_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (9.83e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2420,
    label = "Cds-CtCs_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (8.83e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2421,
    label = "Cds-CtCs_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.01e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2422,
    label = "Cds-CtCs_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (3e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.43, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2423,
    label = "Cds-CtCs_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (8.9e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2424,
    label = "Cds-CtCs_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (2.38e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2425,
    label = "Cds-CtCs_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (7.01e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2426,
    label = "Cds-CtCs_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (8.3e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2427,
    label = "Cds-CdCt_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.36e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2428,
    label = "Cds-CdCt_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.45e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2429,
    label = "Cds-CdCt_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.69e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.29, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2430,
    label = "Cds-CdCt_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (1.35e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2431,
    label = "Cds-CdCt_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.51e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2432,
    label = "Cds-CdCt_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (1.45e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2433,
    label = "Cds-CdCt_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (1.3e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2434,
    label = "Cds-CdCt_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.5e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2435,
    label = "Cds-CdCt_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (4.43e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2436,
    label = "Cds-CdCt_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (1.32e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.63, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2437,
    label = "Cds-CdCt_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (3.51e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2438,
    label = "Cds-CdCt_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.04e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2439,
    label = "Cds-CdCt_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (1.23e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2440,
    label = "Cds-CtCt_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.27e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2441,
    label = "Cds-CtCt_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.36e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2442,
    label = "Cds-CtCt_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.58e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2443,
    label = "Cds-CtCt_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (1.26e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2444,
    label = "Cds-CtCt_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.41e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.18, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2445,
    label = "Cds-CtCt_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (1.36e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2446,
    label = "Cds-CtCt_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (1.22e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2447,
    label = "Cds-CtCt_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.4e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2448,
    label = "Cds-CtCt_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (4.14e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2449,
    label = "Cds-CtCt_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (1.23e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2450,
    label = "Cds-CtCt_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (3.28e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (5.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2451,
    label = "Cds-CtCt_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (9.68e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.94, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2452,
    label = "Cds-CtCt_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (1.15e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (5.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2453,
    label = "Cds-CbH_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (4.7e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.53, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2454,
    label = "Cds-CbH_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (5.04e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2455,
    label = "Cds-CbH_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (5.85e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.51, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2456,
    label = "Cds-CbH_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (4.68e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2457,
    label = "Cds-CbH_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (5.24e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2458,
    label = "Cds-CbH_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (5.03e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2459,
    label = "Cds-CbH_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (4.52e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.32, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2460,
    label = "Cds-CbH_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (5.19e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.06, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2461,
    label = "Cds-CbH_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (1.54e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.23, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2462,
    label = "Cds-CbH_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (4.56e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2463,
    label = "Cds-CbH_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (1.22e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (5.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2464,
    label = "Cds-CbH_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (3.59e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2465,
    label = "Cds-CbH_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (4.25e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2466,
    label = "Cds-CbCs_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (6.73e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2467,
    label = "Cds-CbCs_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (7.22e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.99, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2468,
    label = "Cds-CbCs_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (8.37e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2469,
    label = "Cds-CbCs_Cds-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (6.7e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2470,
    label = "Cds-CbCs_Cds-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (7.51e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2471,
    label = "Cds-CbCs_Cds-CdCd;HJ",
    kinetics = ArrheniusEP(
        A = (7.21e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2472,
    label = "Cds-CbCs_Cds-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (6.48e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2473,
    label = "Cds-CbCs_Cds-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (7.44e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2474,
    label = "Cds-CbCs_Cds-CdCt;HJ",
    kinetics = ArrheniusEP(
        A = (2.2e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2475,
    label = "Cds-CbCs_Cds-CtCt;HJ",
    kinetics = ArrheniusEP(
        A = (6.53e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2476,
    label = "Cds-CbCs_Cds-CbH;HJ",
    kinetics = ArrheniusEP(
        A = (1.74e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (5.02, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2477,
    label = "Cds-CbCs_Cds-CbCs;HJ",
    kinetics = ArrheniusEP(
        A = (5.14e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2478,
    label = "Cds-CbCs_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (6.09e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2479,
    label = "Ct-H_Ct-H;HJ",
    kinetics = ArrheniusEP(
        A = (5.15e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2480,
    label = "Ct-H_Ct-Cs;HJ",
    kinetics = ArrheniusEP(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2481,
    label = "Ct-H_Ct-Cd;HJ",
    kinetics = ArrheniusEP(
        A = (5.7e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2482,
    label = "Ct-H_Ct-Ct;HJ",
    kinetics = ArrheniusEP(
        A = (4.24e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.48, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2483,
    label = "Ct-Cs_Ct-H;HJ",
    kinetics = ArrheniusEP(
        A = (6.92e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2484,
    label = "Ct-Cs_Ct-Cs;HJ",
    kinetics = ArrheniusEP(
        A = (2.02e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2485,
    label = "Ct-Cs_Ct-Cd;HJ",
    kinetics = ArrheniusEP(
        A = (7.66e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.93, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2486,
    label = "Ct-Cs_Ct-Ct;HJ",
    kinetics = ArrheniusEP(
        A = (5.71e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.77, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2487,
    label = "Ct-Cd_Ct-H;HJ",
    kinetics = ArrheniusEP(
        A = (2.62e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2488,
    label = "Ct-Cd_Ct-Cs;HJ",
    kinetics = ArrheniusEP(
        A = (7.63e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2489,
    label = "Ct-Cd_Ct-Cd;HJ",
    kinetics = ArrheniusEP(
        A = (2.9e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2490,
    label = "Ct-Cd_Ct-Ct;HJ",
    kinetics = ArrheniusEP(
        A = (2.16e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2491,
    label = "Ct-Ct_Ct-H;HJ",
    kinetics = ArrheniusEP(
        A = (8.37e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (4.13, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2492,
    label = "Ct-Ct_Ct-Cs;HJ",
    kinetics = ArrheniusEP(
        A = (2.44e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (5.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2493,
    label = "Ct-Ct_Ct-Cd;HJ",
    kinetics = ArrheniusEP(
        A = (9.27e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.66, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2494,
    label = "Ct-Ct_Ct-Ct;HJ",
    kinetics = ArrheniusEP(
        A = (6.9e+09, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2495,
    label = "Ca_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (4.42e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2496,
    label = "Ca_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (5.46e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (3.78, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2497,
    label = "Ca_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (3.06e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (2.74, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2498,
    label = "Cds-HH_Sd;HJ",
    kinetics = ArrheniusEP(
        A = (4.62e+08, 'cm^3/(mol*s)'),
        n = 1.7,
        alpha = 0,
        E0 = (0.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2499,
    label = "Cds-HH_Sd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (11500, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (-0.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3""",
)

entry(
    index = 2500,
    label = "Cds-HH_Sd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (557, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (-2.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3 ref + G3 contributie""",
)

entry(
    index = 2501,
    label = "Cds-HH_Sd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (178, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (-4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3 ref + G3 contributie""",
)

entry(
    index = 2502,
    label = "Cds-HH_Sd;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (120, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Aaron Vandeputte GAVs CBS-QB3 ref + G3 contributie""",
)

entry(
    index = 2511,
    label = "Cds-HH_Sd;SsJ-H",
    kinetics = ArrheniusEP(
        A = (14600, 'cm^3/(mol*s)'),
        n = 2.5,
        alpha = 0,
        E0 = (-1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2512,
    label = "Cds-HH_Sd;SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (858, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (-0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2516,
    label = "Cds-HH_Sd;SsJ-S2s",
    kinetics = ArrheniusEP(
        A = (31.9, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2517,
    label = "Cds-CsH_Sd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (871, 'cm^3/(mol*s)'),
        n = 2.7,
        alpha = 0,
        E0 = (4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2518,
    label = "Cds-CsCs_Sd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (195, 'cm^3/(mol*s)'),
        n = 2.6,
        alpha = 0,
        E0 = (5.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2521,
    label = "Sd_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (9.5e+08, 'cm^3/(mol*s)'),
        n = 1.7,
        alpha = 0,
        E0 = (-0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2522,
    label = "Sd_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3760, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2523,
    label = "Sd_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (169, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2524,
    label = "Sd_Cds-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (64.4, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2525,
    label = "Sd_Cds-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (36.2, 'cm^3/(mol*s)'),
        n = 3.1,
        alpha = 0,
        E0 = (-3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2534,
    label = "Sd_Cds-HH;SsJ-H",
    kinetics = ArrheniusEP(
        A = (7220, 'cm^3/(mol*s)'),
        n = 2.6,
        alpha = 0,
        E0 = (-6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2535,
    label = "Sd_Cds-HH;SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (382, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2539,
    label = "Sd_Cds-HH;SsJ-S2s",
    kinetics = ArrheniusEP(
        A = (13.4, 'cm^3/(mol*s)'),
        n = 3.3,
        alpha = 0,
        E0 = (1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2540,
    label = "Sd_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5360, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2541,
    label = "Sd_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5290, 'cm^3/(mol*s)'),
        n = 2.7,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2542,
    label = "Sd_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1650, 'cm^3/(mol*s)'),
        n = 3.2,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2543,
    label = "Sd_Cds-CdCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1680, 'cm^3/(mol*s)'),
        n = 3.1,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2544,
    label = "Cds-HH_Cds-HH;SsJ-H",
    kinetics = ArrheniusEP(
        A = (2490, 'cm^3/(mol*s)'),
        n = 2.7,
        alpha = 0,
        E0 = (-0.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2545,
    label = "Cds-HH_Cds-HH;SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (73.9, 'cm^3/(mol*s)'),
        n = 3.1,
        alpha = 0,
        E0 = (1.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 2549,
    label = "Cds-HH_Cds-HH;SsJ-S2s",
    kinetics = ArrheniusEP(
        A = (4.21, 'cm^3/(mol*s)'),
        n = 3.3,
        alpha = 0,
        E0 = (7.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Aaron Vandeputte GAVs G3""",
)

entry(
    index = 3000,
    label = "R_R;YJ",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 3001,
    label = "Cds-HH_Cds;HJ",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3002,
    label = "Cds-CsH_Cds;HJ",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3003,
    label = "Cds-CsCs_Cds;HJ",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3004,
    label = "Cds-HH_Cds;CsJ",
    kinetics = ArrheniusEP(
        A = (8.5e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3005,
    label = "Cds-CsH_Cds;CsJ",
    kinetics = ArrheniusEP(
        A = (8.5e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3006,
    label = "Cds-CsCs_Cds;CsJ",
    kinetics = ArrheniusEP(
        A = (8.5e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3007,
    label = "Cds-HH_Cds;O_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (12.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 20. Based on recommendations of Chen and Bozzelli [57]""",
)

entry(
    index = 3008,
    label = "Cds-CsH_Cds;O_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 20. Based on recommendations of Chen and Bozzelli [57]""",
)

entry(
    index = 3009,
    label = "Cds-CsCs_Cds;O_rad/NonDe",
    kinetics = ArrheniusEP(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 20. Based on recommendations of Chen and Bozzelli [57]""",
)

entry(
    index = 3010,
    label = "Cds-HH_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.985e+09, 'cm^3/(mol*s)', '*|/', 2),
        n = 1.28,
        alpha = 0,
        E0 = (1.29, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Baulch et al. [94] literature review.""",
)

entry(
    index = 3011,
    label = "Cds-HH_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1.655e+11, 'cm^3/(mol*s)', '*|/', 1.3),
        n = 0,
        alpha = 0,
        E0 = (7.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
)

entry(
    index = 3012,
    label = "Cds-HH_Cds-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1990, 'cm^3/(mol*s)'),
        n = 2.44,
        alpha = 0,
        E0 = (5.37, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""Knyazev et al. [147]""",
)

entry(
    index = 3013,
    label = "Cds-HH_Cds-HH;CsJ-OsHH",
    kinetics = ArrheniusEP(
        A = (2.41e+10, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        alpha = 0,
        E0 = (6.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang et al. [90] literature review.""",
)

entry(
    index = 3014,
    label = "Cds-HH_Cds-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.01, 'kcal/mol'),
        Tmin = (1260, 'K'),
        Tmax = (1310, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Weissman and Benson [148] Estimated values.""",
)

entry(
    index = 3015,
    label = "Cds-HH_Cds-HH;OJ_pri",
    kinetics = ArrheniusEP(
        A = (2.71e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang et al. [89] literature review.""",
)

entry(
    index = 3016,
    label = "Cds-HH_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.56, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [149] experiments and limited review.""",
)

entry(
    index = 3017,
    label = "Cds-HH_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (128000, 'cm^3/(mol*s)'),
        n = 2.28,
        alpha = 0,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Knyazev et al. [150]""",
)

entry(
    index = 3018,
    label = "Cds-HH_Cds-CsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1.69e+11, 'cm^3/(mol*s)', '*|/', 1.4),
        n = 0,
        alpha = 0,
        E0 = (7.41, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
)

entry(
    index = 3019,
    label = "Cds-HH_Cds-CsH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (3.55e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (16.89, 'kcal/mol'),
        Tmin = (762, 'K'),
        Tmax = (811, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Barbe et al. [151] Data are estimated.""",
)

entry(
    index = 3020,
    label = "Cds-HH_Cds-CsH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (3.07e+09, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (5.88, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
)

entry(
    index = 3021,
    label = "Cds-HH_Cds-CdH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3.155e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.49, 'kcal/mol'),
        Tmin = (743, 'K'),
        Tmax = (772, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Perrin et al. [152] Data are estimated.""",
)

entry(
    index = 3022,
    label = "Cds-HH_Cds-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (6.21e+12, 'cm^3/(mol*s)'),
        n = 0.25,
        alpha = 0,
        E0 = (1.46, 'kcal/mol'),
        Tmin = (712, 'K'),
        Tmax = (779, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Knyazev et al. [153]""",
)

entry(
    index = 3023,
    label = "Cds-HH_Cds-CsCs;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2.51e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.7, 'kcal/mol'),
        Tmin = (391, 'K'),
        Tmax = (449, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Seres et al. [154] Data derived from fitting a complex mechanism.""",
)

entry(
    index = 3024,
    label = "Cds-CsH_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.3e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3.26, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [149] experiments and limited review.""",
)

entry(
    index = 3025,
    label = "Cds-CsH_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (10000, 'cm^3/(mol*s)'),
        n = 2.57,
        alpha = 0,
        E0 = (7.71, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Knyazev et al. [147]""",
)

entry(
    index = 3026,
    label = "Cds-CsH_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (9.64e+10, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        alpha = 0,
        E0 = (8.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
)

entry(
    index = 3027,
    label = "Cds-CsCs_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2.23e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.59, 'kcal/mol'),
        Tmin = (560, 'K'),
        Tmax = (650, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Slagle et al. [155] Data derived from detailed balance/reverse rate.""",
)

entry(
    index = 3028,
    label = "Cds-HH_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (1.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3029,
    label = "Cds-CsH_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3030,
    label = "Cds-CsCs_Ca;HJ",
    kinetics = ArrheniusEP(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3031,
    label = "Cds-HH_Ca;CsJ",
    kinetics = ArrheniusEP(
        A = (8.5e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3032,
    label = "Cds-CsH_Ca;CsJ",
    kinetics = ArrheniusEP(
        A = (8.5e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3033,
    label = "Cds-CsCs_Ca;CsJ",
    kinetics = ArrheniusEP(
        A = (8.5e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (10.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 3. Based on recommendations of Allara and Shaw [146]""",
)

entry(
    index = 3034,
    label = "Cds-HH_Ca;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5.75e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.84, 'kcal/mol', '+|-', 0.2),
        Tmin = (573, 'K'),
        Tmax = (595, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Scherzer et al. [156] Data derived from fitting a complex mechanism.""",
)

entry(
    index = 3035,
    label = "Ca_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.2e+11, 'cm^3/(mol*s)', '*|/', 2.5),
        n = 0.69,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (350, 'K'),
        Tmax = (1200, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang et al. [157]""",
)

entry(
    index = 3036,
    label = "Ca_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1.58e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.97, 'kcal/mol'),
        Tmin = (996, 'K'),
        Tmax = (1180, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Tsang [158] Data is estimated.""",
)

entry(
    index = 3037,
    label = "CO_O;HJ",
    kinetics = ArrheniusEP(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 18.""",
)

entry(
    index = 3038,
    label = "CO_O;CsJ",
    kinetics = ArrheniusEP(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran et al. [8] in his reaction type 18.""",
)

entry(
    index = 3039,
    label = "CO_O;CO_pri_rad",
    kinetics = ArrheniusEP(
        A = (5.2e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Bozzelli et al. [144] based on CH3 addition to CO (Anastasi and Maw)""",
)

entry(
    index = 3040,
    label = "CO_O;O_rad/OneDe",
    kinetics = ArrheniusEP(
        A = (1.3e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran esitmation [159] in DME oxidation modeling for ketohydroperoxide decomposition.""",
)

entry(
    index = 3041,
    label = "CO-HH_O;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (7.94e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.7, 'kcal/mol', '+|-', 0.47),
        Tmin = (333, 'K'),
        Tmax = (363, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Knoll et al. [160] Data derived from fitting a complex mechanism.""",
)

entry(
    index = 3042,
    label = "CO-CsCs_O;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3.16e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (11.51, 'kcal/mol', '+|-', 1.15),
        Tmin = (413, 'K'),
        Tmax = (563, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Knoll et al. [161]""",
)

entry(
    index = 3043,
    label = "Ct-H_Ct-H;HJ",
    kinetics = ArrheniusEP(
        A = (2.75e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Warnatz [134] literature review.""",
)

entry(
    index = 3044,
    label = "Ct-H_Ct-H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1.875e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.77, 'kcal/mol'),
        Tmin = (370, 'K'),
        Tmax = (478, 'K'),
    ),
    rank = 4,
    shortDesc = u"""E.W. Diau and M.C. Lin [162] RRK(M) extrapolation.""",
)

entry(
    index = 3045,
    label = "Ct-H_Ct-H;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2.505e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.99, 'kcal/mol'),
        Tmin = (373, 'K'),
        Tmax = (473, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Kerr et al. [163] literature review.""",
)

entry(
    index = 3046,
    label = "Ct-H_Ct-H;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (1.595e+10, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (6.96, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Tsang [93] literature review.""",
)

entry(
    index = 3047,
    label = "Ct-H_Ct-H;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (2.505e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (6.9, 'kcal/mol'),
        Tmin = (363, 'K'),
        Tmax = (577, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Kerr et al. [163] literature review.""",
)

entry(
    index = 3048,
    label = "Ct-H_Ct-H;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (2.505e+10, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (5.31, 'kcal/mol'),
        Tmin = (373, 'K'),
        Tmax = (493, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Dominguez et al. [164] Data derived from fitting a complex mechanism.""",
)

entry(
    index = 3049,
    label = "Ct-H_Ct-H;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (125500, 'cm^3/(mol*s)'),
        n = 1.9,
        alpha = 0,
        E0 = (2.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Weissman et al. [121] Transition state theory.""",
)

entry(
    index = 3050,
    label = "Ct-H_Ct-H;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (3.155e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.9, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Duran et al. [165] Ab initio.""",
)

entry(
    index = 3051,
    label = "Ct-H_Ct-H;CtJ_Ct",
    kinetics = ArrheniusEP(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Duran et al. [165] Ab initio.""",
)

entry(
    index = 3052,
    label = "Ct-H_Ct-H;OJ_pri",
    kinetics = ArrheniusEP(
        A = (6.05e+11, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        alpha = 0,
        E0 = (0.46, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Baulch et al. [95] literature review.""",
)

entry(
    index = 3053,
    label = "Ct-H_Ct-H;OJ_pri",
    kinetics = ArrheniusEP(
        A = (7.6e+07, 'cm^3/(mol*s)'),
        n = 1.7,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (250, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Miller et al. [166] Transition state theory.""",
)

entry(
    index = 3054,
    label = "Ct-H_Ct-H;OJ_sec",
    kinetics = ArrheniusEP(
        A = (5.2e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (7.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Bozzelli et al. [144] based on CH3 addition to C2H2 (NIST)""",
)

entry(
    index = 3055,
    label = "Cds-HH_Cds-HH;CdsJ=Cdd",
    kinetics = ArrheniusEP(
        A = (1.04E+00, 'cm^3/(mol*s)'),
        n = 3.05,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""A.G. Vandeputte, BMK/cbsb7 no 1D-HR (slow anyway)""",
)

entry(
    index = 3056,
    label = "Ct-H_Ct-H;CdsJ=Cdd",
    kinetics = ArrheniusEP(
        A = (1.70E+05, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (13.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""A.G. Vandeputte, BMK/cbsb7 no 1D-HR (slow anyway)""",
)

entry(
    index = 3134,
    label = "Ca_Cds-HH;CdsJ=Cdd",
    kinetics = ArrheniusEP(
        A = (1.04E+00, 'cm^3/(mol*s)'),
        n = 3.05,
        alpha = 0,
        E0 = (13.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""A.G. Vandeputte estimate.  Equal to Cds-HH_Cds-HH;CdsJ=Cdd""",
)

entry(
    index = 3056,
    label = "CO-NdH_O;OJ-Os",
    kinetics = ArrheniusEP(
        A = (0.04245, 'cm^3/(mol*s)'),
        n = 3.486,
        alpha = 0,
        E0 = (22.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 5,
)

entry(
    index = 3057,
    label = "CO-CsCs_O;OJ-Os",
    kinetics = ArrheniusEP(
        A = (0.04245, 'cm^3/(mol*s)'),
        n = 3.486,
        alpha = 0,
        E0 = (22.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 5,
)

entry(
    index = 3058,
    label = "CO-HH_O;OJ-Os",
    kinetics = ArrheniusEP(
        A = (0.04245, 'cm^3/(mol*s)'),
        n = 3.486,
        alpha = 0,
        E0 = (22.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 5,
)

entry(
    index = 3059,
    label = "CO-CsCs_O;OJ-Os",
    kinetics = ArrheniusEP(
        A = (0.04245, 'cm^3/(mol*s)'),
        n = 3.486,
        alpha = 0,
        E0 = (22.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 5,
)

entry(
    index = 3060,
    label = "Cds-HH_Cds-HH;OJ-Os",
    kinetics = ArrheniusEP(
        A = (35.6, 'cm^3/(mol*s)'),
        n = 3.22,
        alpha = 0,
        E0 = (11.1, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 2,
    shortDesc = u"""pp, CBS-QB3 calculations, with hindered rotor treatment.""",
)

entry(
    index = 3061,
    label = "Cds-HH_Cds-CsH;OJ-Os",
    kinetics = ArrheniusEP(
        A = (791, 'cm^3/(mol*s)'),
        n = 2.78,
        alpha = 0,
        E0 = (9.5, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ps, CBS-QB3 calculations, with hindered rotor treatment.""",
)

entry(
    index = 3062,
    label = "Cds-HH_Cds-CsCs;OJ-Os",
    kinetics = ArrheniusEP(
        A = (1350, 'cm^3/(mol*s)'),
        n = 2.67,
        alpha = 0,
        E0 = (7.9, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 2,
    shortDesc = u"""pt, CBS-QB3 calculations, with hindered rotor treatment.""",
)

entry(
    index = 3063,
    label = "Cds-CsH_Cds-HH;OJ-Os",
    kinetics = ArrheniusEP(
        A = (10.6, 'cm^3/(mol*s)'),
        n = 3.29,
        alpha = 0,
        E0 = (9.1, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 2,
    shortDesc = u"""sp, CBS-QB3 calculations, with hindered rotor treatment.""",
)

entry(
    index = 3064,
    label = "Cds-CsH_Cds-CsH;OJ-Os",
    kinetics = ArrheniusEP(
        A = (46.2, 'cm^3/(mol*s)'),
        n = 3.09,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ss, CBS-QB3 calculations, with hindered rotor treatment.""",
)

entry(
    index = 3065,
    label = "Cds-CsH_Cds-CsCs;OJ-Os",
    kinetics = ArrheniusEP(
        A = (186, 'cm^3/(mol*s)'),
        n = 2.95,
        alpha = 0,
        E0 = (5.4, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 2,
    shortDesc = u"""st, CBS-QB3 calculations, with hindered rotor treatment.""",
)

entry(
    index = 3066,
    label = "Cds-CsCs_Cds-HH;OJ-Os",
    kinetics = ArrheniusEP(
        A = (0.337, 'cm^3/(mol*s)'),
        n = 3.67,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 2,
    shortDesc = u"""tp, CBS-QB3 calculations, with hindered rotor treatment.""",
)

entry(
    index = 3067,
    label = "Cds-CsCs_Cds-CsH;OJ-Os",
    kinetics = ArrheniusEP(
        A = (0.172, 'cm^3/(mol*s)'),
        n = 3.7,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ts, CBS-QB3 calculations, with hindered rotor treatment.""",
)

entry(
    index = 3068,
    label = "Cds-CsCs_Cds-CsCs;OJ-Os",
    kinetics = ArrheniusEP(
        A = (1.69, 'cm^3/(mol*s)'),
        n = 3.44,
        alpha = 0,
        E0 = (2.7, 'kcal/mol'),
        Tmin = (400, 'K'),
        Tmax = (1100, 'K'),
    ),
    rank = 2,
    shortDesc = u"""tt, CBS-QB3 calculations, with hindered rotor treatment.""",
)

entry(
    index = 3069,
    label = "Cds-HH_Cds-CsH;OJ_pri",
    kinetics = ArrheniusEP(
        A = (3.2E+5, 'cm^3/(mol*s)'),
        n = 2.03,
        alpha = 0,
        E0 = (-3.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = "propene+OH rate coefficient",
    longDesc = """
Ref Ab Initio Kinetics for the Decomposition of Hydroxybutyl and Butoxy Radicals of n-Butanol,Zhang P.,Klippenstein S.K.,Law C.K.
The thermochemistry for the species is obtained from Mike's n-butanol paper dx.doi.org/10.1016/j.combustflame.2010.06.002         
Original rate is too high (~ factor of 10) replaced with propene+OH rate coefficient 
    """,
)

entry(
    index = 3070,
    label = "Cds-HH_Cds-Cs\Os/H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (532000, 'cm^3/(mol*s)'),
        n = 1.85,
        alpha = 0,
        E0 = (5.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
)

entry(
    index = 3071,
    label = "Cds-HH_Cds-OsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1071, 'cm^3/(mol*s)'),
        n = 2.72,
        alpha = 0,
        E0 = (8.24, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
)

entry(
    index = 3072,
    label = "Cds-HH_Cds-CsH;CsJ-OsHH",
    kinetics = ArrheniusEP(
        A = (1.381e+06, 'cm^3/(mol*s)'),
        n = 1.76,
        alpha = 0,
        E0 = (8.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
)

entry(
    index = 3073,
    label = "CO-HH_O;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (120.1, 'cm^3/(mol*s)'),
        n = 2.8,
        alpha = 0,
        E0 = (1.79, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
)

entry(
    index = 3074,
    label = "CO-NdH_O;HJ",
    kinetics = ArrheniusEP(
        A = (9.6e+09, 'cm^3/(mol*s)'),
        n = 0.935,
        alpha = 0,
        E0 = (4.17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
)

entry(
    index = 3077,
    label = "Cds-OsH_Sd;HJ",
    kinetics = ArrheniusEP(
        A = (2.79e+08, 'cm^3/(mol*s)'),
        n = 1.63,
        alpha = 0,
        E0 = (2.71, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CCSD(T)-F12a/vtz-f12 1DHR""",
)

entry(
    index = 3078,
    label = "Cds-OsH_Sd;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (23200, 'cm^3/(mol*s)'),
        n = 2.35,
        alpha = 0,
        E0 = (5.49, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CCSD(T)-F12a/vtz-F12 1DHR""",
)

entry(
    index = 3079,
    label = "Cds-OsH_Sd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (1650, 'cm^3/(mol*s)'),
        n = 2.54,
        alpha = 0,
        E0 = (3.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CCSD(T)-F12a/vtz-F12 1dHR""",
)

entry(
    index = 3081,
    label = "Sd_Cds-CsH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (169, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (-1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""based on 2523""",
)

entry(
    index = 3082,
    label = "Cds-CsH_Sd;HJ",
    kinetics = ArrheniusEP(
        A = (2.13e+09, 'cm^3/(mol*s)'),
        n = 1.43,
        alpha = 0,
        E0 = (1.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 3083,
    label = "Cds-CsH_Sd;CsJ-SsCsH",
    kinetics = ArrheniusEP(
        A = (2.57, 'cm^3/(mol*s)'),
        n = 3.04,
        alpha = 0,
        E0 = (-1.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 3087,
    label = "Sd_Cds-CsH;CsJ",
    kinetics = ArrheniusEP(
        A = (3.91e+06, 'cm^3/(mol*s)'),
        n = 1.66,
        alpha = 0,
        E0 = (-0.87, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 3088,
    label = "C=S_O;HJ",
    kinetics = ArrheniusEP(
        A = (8.41e+09, 'cm^3/(mol*s)'),
        n = 1.23,
        alpha = 0,
        E0 = (7.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CAC calc CCSD(T)-F12a/vtz-f12 1dhr""",
)

entry(
    index = 3089,
    label = "C=S_O;CsJ",
    kinetics = ArrheniusEP(
        A = (8.04e+06, 'cm^3/(mol*s)'),
        n = 1.68,
        alpha = 0,
        E0 = (12.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CAC calc CCSD(T)-F12a/vtz-f12 1dhr""",
)

entry(
    index = 3090,
    label = "Cds-CsH_Sd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (2310, 'cm^3/(mol*s)'),
        n = 2.56,
        alpha = 0,
        E0 = (0.54, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 3091,
    label = "Cds-CsH_Sd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (50.8, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (-1.22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 3092,
    label = "Cds-CsH_Sd;SsJ-H",
    kinetics = ArrheniusEP(
        A = (1.18e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (-1.36, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (700, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AA calcs""",
)

entry(
    index = 3093,
    label = "Cds-CsH_Sd;SsJ-H",
    kinetics = ArrheniusEP(
        A = (2.46e+14, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (2.93, 'kcal/mol'),
        Tmin = (701, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AA calcs""",
)

entry(
    index = 3094,
    label = "Cds-SsH_Sd;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (1.95e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AA calcs""",
)

entry(
    index = 3095,
    label = "Cds-SsCs_Sd;HJ",
    kinetics = ArrheniusEP(
        A = (1.62e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (4.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AA calcs""",
)

entry(
    index = 3096,
    label = "Cdd-Sd_Sd;HJ",
    kinetics = ArrheniusEP(
        A = (5.02e+09, 'cm^3/(mol*s)'),
        n = 1.34,
        alpha = 0,
        E0 = (6.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 3097,
    label = "Cdd-Sd_Sd;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (971000, 'cm^3/(mol*s)'),
        n = 1.95,
        alpha = 0,
        E0 = (9.11, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 3098,
    label = "Sd_Cds-OsCs;HJ",
    kinetics = ArrheniusEP(
        A = (5.54e+08, 'cm^3/(mol*s)'),
        n = 1.24,
        alpha = 0,
        E0 = (-0.35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 3099,
    label = "Cds-OsH_Cds-CsH;SsJ-H",
    kinetics = ArrheniusEP(
        A = (128000, 'cm^3/(mol*s)'),
        n = 2.39,
        alpha = 0,
        E0 = (-3.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 3100,
    label = "Cds-HH_Cds-HH;O_atom_triplet",
    kinetics = ArrheniusEP(
        A = (4.42e+07, 'cm^3/(mol*s)'),
        n = 1.55,
        alpha = 0,
        E0 = (-0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3100,
    label = "Cds-OsCs_Sd;HJ",
    kinetics = ArrheniusEP(
        A = (2.01e+09, 'cm^3/(mol*s)'),
        n = 1.21,
        alpha = 0,
        E0 = (-1.26, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CAC calc CCSD(T)-F12a/vtz-F12 1dhr""",
)

entry(
    index = 3101,
    label = "Cds-CsH_Cds-HH;O_atom_triplet",
    kinetics = ArrheniusEP(
        A = (4.17e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (-1.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3101,
    label = "Cds-SsH_Cds;SsJ-Cd",
    kinetics = ArrheniusEP(
        A = (9.46, 'cm^3/(mol*s)'),
        n = 3.08,
        alpha = 0,
        E0 = (-6.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""CAC calc CBS-QB3, HO approx""",
)

entry(
    index = 3102,
    label = "Cds-CsH_Sd;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (288, 'cm^3/(mol*s)'),
        n = 2.55,
        alpha = 0,
        E0 = (5.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3, 1dhr""",
)

entry(
    index = 3102,
    label = "Cds-HH_Cds-CsH;O_atom_triplet",
    kinetics = ArrheniusEP(
        A = (1.06e+08, 'cm^3/(mol*s)'),
        n = 1.58,
        alpha = 0,
        E0 = (-2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3103,
    label = "Cds-HH_Cds-CsH;CsJ-CbHH",
    kinetics = ArrheniusEP(
        A = (53200, 'cm^3/(mol*s)'),
        n = 2.1,
        alpha = 0,
        E0 = (10.01, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3, 1dhr""",
)

entry(
    index = 3103,
    label = "Cds-HH_Cds-HH;O2b",
    kinetics = ArrheniusEP(
        A = (111, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (31.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3104,
    label = "Cds-CsH_Cds-HH;O2b",
    kinetics = ArrheniusEP(
        A = (44.2, 'cm^3/(mol*s)'),
        n = 3.08,
        alpha = 0,
        E0 = (30.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3105,
    label = "Cds-HH_Cds-CsH;O2b",
    kinetics = ArrheniusEP(
        A = (276, 'cm^3/(mol*s)'),
        n = 2.78,
        alpha = 0,
        E0 = (29.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3106,
    label = "Cds-HH_Cds-CdH;O2b",
    kinetics = ArrheniusEP(
        A = (130, 'cm^3/(mol*s)'),
        n = 3.01,
        alpha = 0,
        E0 = (23.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3107,
    label = "Cds-OJH_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (6.5e+06, 'cm^3/(mol*s)'),
        n = 1.86,
        alpha = 0,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3108,
    label = "Cds-OJH_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 1.84,
        alpha = 0,
        E0 = (7.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3109,
    label = "Cds-OJH_Cds-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (335, 'cm^3/(mol*s)'),
        n = 2.68,
        alpha = 0,
        E0 = (9.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""AG Vandeputte, BMK/cbsb7""",
)

entry(
    index = 3113,
    label = "Cds-HH_Cds-Cs\H3/H;HJ",
    kinetics = ArrheniusEP(
        A = (1.84e+09, 'cm^3/(mol*s)'),
        n = 1.553,
        alpha = 0,
        E0 = (1.57, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CCSD(T)/cc-pVTZ""",
)

entry(
    index = 3114,
    label = "Cds-CsH_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.17e+08, 'cm^3/(mol*s)'),
        n = 1.68,
        alpha = 0,
        E0 = (2.03, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CCSD(T)/cc-pVTZ""",
)

entry(
    index = 3115,
    label = "Cds-HH_Cds-Cs\H3/H;CsJ-OsHH",
    kinetics = ArrheniusEP(
        A = (2550, 'cm^3/(mol*s)'),
        n = 2.562,
        alpha = 0,
        E0 = (5.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""same as 3108""",
)

entry(
    index = 3116,
    label = "Cds-HH_Cds-OsH;HJ",
    kinetics = ArrheniusEP(
        A = (6.67e+12, 'cm^3/(mol*s)'),
        n = 0.1,
        alpha = 0,
        E0 = (1.544, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ED calc RQCISD(T)/aug-cc-pVTZ with 1dHR""",
)

entry(
    index = 3117,
    label = "CO-HH_O;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (216, 'cm^3/(mol*s)'),
        n = 2.97,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ED calc RQCISD(T)/aug-cc-pVTZ with 1dHR""",
)

entry(
    index = 3118,
    label = "Od_CO-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (4e+09, 'cm^3/(mol*s)'),
        n = 1.39,
        alpha = 0,
        E0 = (8.577, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 2,
    shortDesc = u"""ED calc RQCISD(T)/aug-cc-pVTZ with 1dHR""",
)

entry(
    index = 3119,
    label = "Cds-HH_Cds-Cs\H3/H;OJ_pri",
    kinetics = ArrheniusEP(
        A = (2.31e+06, 'cm^3/(mol*s)'),
        n = 1.76,
        alpha = 0,
        E0 = (-2.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3120,
    label = "Cds-OsH_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (2.182e+10, 'cm^3/(mol*s)'),
        n = 0.859,
        alpha = 0,
        E0 = (1.618, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3121,
    label = "Cds-HH_Cds-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (5.014e+08, 'cm^3/(mol*s)'),
        n = 1.733,
        alpha = 0,
        E0 = (0.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
    longDesc = """
    Update: changed rank to 5.  A.G. Vandeputte.  GA estimate is probably better.
"""
)

entry(
    index = 3122,
    label = "Cds-HH_Cds-Cs\Os/H;HJ",
    kinetics = ArrheniusEP(
        A = (5.014e+08, 'cm^3/(mol*s)'),
        n = 1.733,
        alpha = 0,
        E0 = (0.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3123,
    label = "Cds-CsH_Cds-OsH;HJ",
    kinetics = ArrheniusEP(
        A = (3.72e+08, 'cm^3/(mol*s)'),
        n = 1.477,
        alpha = 0,
        E0 = (1.61, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3124,
    label = "Cds-HH_Cds-OsH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (41670, 'cm^3/(mol*s)'),
        n = 2.299,
        alpha = 0,
        E0 = (6.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3125,
    label = "Od_CO;HJ",
    kinetics = ArrheniusEP(
        A = (386700, 'cm^3/(mol*s)'),
        n = 2.941,
        alpha = 0,
        E0 = (8.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""SSM calc CBS-QB3 1dhr, gave parent same value as one of the children""",
)

entry(
    index = 3126,
    label = "Od_CO-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (386700, 'cm^3/(mol*s)'),
        n = 2.941,
        alpha = 0,
        E0 = (8.52, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3127,
    label = "Cds-HH_Cds-HH;CsJ-OsHH",
    kinetics = ArrheniusEP(
        A = (2550, 'cm^3/(mol*s)'),
        n = 2.562,
        alpha = 0,
        E0 = (5.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3128,
    label = "Cds-Cs\Os/H_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (1.73e+08, 'cm^3/(mol*s)'),
        n = 1.583,
        alpha = 0,
        E0 = (1.81, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3129,
    label = "CO-HH_O;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (0.0034, 'cm^3/(mol*s)'),
        n = 2.48,
        alpha = 0,
        E0 = (2.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3130,
    label = "CO-CsH_O;HJ",
    kinetics = ArrheniusEP(
        A = (8, 'cm^3/(mol*s)'),
        n = 2.41,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""SSM calc CBS-QB3 1dhr""",
)

entry(
    index = 3131,
    label = "CO-HH_O;HJ",
    kinetics = ArrheniusEP(
        A = (8.1e+11, 'cm^3/(mol*s)'),
        n = 0.37,
        alpha = 0,
        E0 = (5.19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""High-P Limit from EFRC Mechanism""",
)

entry(
    index = 3200,
    label = "N3t_N3t;CH2_triplet",
    kinetics = ArrheniusEP(
        A = (1.6e+32, 'cm^3/(mol*s)'),
        n = -7.07,
        alpha = 0,
        E0 = (19.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: CH2 + N2 = CH2NN (B&D #22a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3201,
    label = "N3t_N3t;CH_doublet",
    kinetics = ArrheniusEP(
        A = (3.6e+28, 'cm^3/(mol*s)'),
        n = -5.84,
        alpha = 0,
        E0 = (2.62, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: CH + N2 = HCNN (B&D #24a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
Here CH is in its ground state (doublet), as specified in B&D p. 221: The initially formed adduct from CH+N2 is a doublet, and there's a surface crossing to eventually form HCN + N.
""",
)

entry(
    index = 3202,
    label = "N3d-H_N3d-H;HJ",
    kinetics = ArrheniusEP(
        A = (9.91e+34, 'cm^3/(mol*s)'),
        n = -7.67,
        alpha = 0,
        E0 = (12.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: N2H2 + H = N2H3 (B&D #31a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3203,
    label = "Ct-H_N3t;OJ_pri",
    kinetics = ArrheniusEP(
        A = (2.8e+30, 'cm^3/(mol*s)'),
        n = -6.37,
        alpha = 0,
        E0 = (5.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HCN + OH = NCHOH (B&D #42b4) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3204,
    label = "Ct-H_N3t;HJ",
    kinetics = ArrheniusEP(
        A = (7.24e+29, 'cm^3/(mol*s)'),
        n = -6.87,
        alpha = 0,
        E0 = (7.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HCN + H = H2CN (B&D #45a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3205,
    label = "N3t_Ct-H;HJ",
    kinetics = ArrheniusEP(
        A = (7.24e+29, 'cm^3/(mol*s)'),
        n = -6.87,
        alpha = 0,
        E0 = (7.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HCN + H = HCNH (B&D #46) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3206,
    label = "Cds-HH_N3d;HJ",
    kinetics = ArrheniusEP(
        A = (7.32e+29, 'cm^3/(mol*s)'),
        n = -6.51,
        alpha = 0,
        E0 = (8.31, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: H2CNH + H = CH3NH (B&D #49a) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3207,
    label = "N3d-H_Cds-HH;HJ",
    kinetics = ArrheniusEP(
        A = (9.86e+36, 'cm^3/(mol*s)'),
        n = -8.41,
        alpha = 0,
        E0 = (12.44, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: H2CNH + H = CH2NH2 (B&D #50) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3208,
    label = "N3t_Ct-H;O_atom_triplet",
    kinetics = ArrheniusEP(
        A = (9.99e+25, 'cm^3/(mol*s)'),
        n = -5.73,
        alpha = 0,
        E0 = (11.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 1,
    shortDesc = u"""Added by Beat Buesser""",
    longDesc = 
u"""
Added by Beat Buesser, value for reaction: HCN + O = HCNO (B&D #54) in 'Gas-Phase Combustion Chemistry' (ISBN: 978-1-4612-7088-1), chapter 2, 'Combustion Chemistry of Nitrogen', Anthony M. Dean, Joseph W. Bozzelli",
""",
)

entry(
    index = 3119,
    label = "CO-HH_O;HJ",
    kinetics = ArrheniusEP(
        A = (6.31E+07, 'cm^3/(mol*s)'),
        n = 1.80,
        alpha = 0,
        E0 = (4.0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3120,
    label = "CO-CsH_O;HJ",
    kinetics = ArrheniusEP(
        A = (8.76E+06, 'cm^3/(mol*s)'),
        n = 1.99,
        alpha = 0,
        E0 = (5.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3121,
    label = "CO-CsH_O;HJ",
    kinetics = ArrheniusEP(
        A = (7.92E+05, 'cm^3/(mol*s)'),
        n = 2.40,
        alpha = 0,
        E0 = (8.0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3122,
    label = "CO-CdH_O;HJ",
    kinetics = ArrheniusEP(
        A = (7.50E+06, 'cm^3/(mol*s)'),
        n = 2.16,
        alpha = 0,
        E0 = (4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3123,
    label = "CO-CdCs_O;HJ",
    kinetics = ArrheniusEP(
        A = (3.97E+07, 'cm^3/(mol*s)'),
        n = 1.88,
        alpha = 0,
        E0 = (7.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3124,
    label = "CO-CtH_O;HJ",
    kinetics = ArrheniusEP(
        A = (2.99E+06, 'cm^3/(mol*s)'),
        n = 2.12,
        alpha = 0,
        E0 = (4.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3125,
    label = "CO-CtCs_O;HJ",
    kinetics = ArrheniusEP(
        A = (1.59E+07, 'cm^3/(mol*s)'),
        n = 1.84,
        alpha = 0,
        E0 = (7.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3126,
    label = "Od_CO-HH;HJ",
    kinetics = ArrheniusEP(
        A = (2.33E+03, 'cm^3/(mol*s)'),
        n = 3.17,
        alpha = 0,
        E0 = (6.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3127,
    label = "Od_CO-CsH;HJ",
    kinetics = ArrheniusEP(
        A = (1.46E+03, 'cm^3/(mol*s)'),
        n = 3.14 ,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3128,
    label = "Od_CO-CsCs;HJ",
    kinetics = ArrheniusEP(
        A = (3.23E+04, 'cm^3/(mol*s)'),
        n = 2.98 ,
        alpha = 0,
        E0 = (7.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3129,
    label = "Od_CO-CdH;HJ",
    kinetics = ArrheniusEP(
        A = (3.73E+05, 'cm^3/(mol*s)'),
        n = 2.53 ,
        alpha = 0,
        E0 = (5.0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3130,
    label = "Od_CO-CdCs;HJ",
    kinetics = ArrheniusEP(
        A = (6.39E+06, 'cm^3/(mol*s)'),
        n = 2.09 ,
        alpha = 0,
        E0 = (6.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3131,
    label = "Od_CO-CtH;HJ",
    kinetics = ArrheniusEP(
        A = (1.07E+06, 'cm^3/(mol*s)'),
        n = 2.43 ,
        alpha = 0,
        E0 = (5.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3132,
    label = "Od_CO-CtCs;HJ",
    kinetics = ArrheniusEP(
        A = (1.83E+07, 'cm^3/(mol*s)'),
        n = 1.99 ,
        alpha = 0,
        E0 = (6.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte, 1D-HR in transition state""",
    longDesc = 
    """
    AGV BMK/cbsb7 with 1dHR
    """
)

entry(
    index = 3133,
    label = "Cds-HH_Cds-HH;CsJ-CdHH",
    kinetics = Arrhenius(
        A = (6.75E+02, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.700,
        Ea = (11.3, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Wang CBS-QB3""",
    longDesc = 
    """
    Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
    
    Table 4
    allyl + ethene <=> pent-1-en-5-yl

    CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions
    around single bonds, tunneling with Eckart potentials.
    """
)

entry(
    index = 3134,
    label = "Cds-HH_Cds-CsH;CsJ-CdHH",
    kinetics = Arrhenius(
        A = (7.80E+02, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.530,
        Ea = (11.0, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Wang CBS-QB3""",
    longDesc = 
    """
    Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
    
    Table 4
    allyl + propene = hex-1-en-5-yl

    CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions
    around single bonds, tunneling with Eckart potentials.
    """
)

entry(
    index = 3135,
    label = "Cds-CsH_Cds-HH;CsJ-CdHH",
    kinetics = Arrhenius(
        A = (3.43E+01, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.840,
        Ea = (12.2, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Wang CBS-QB3""",
    longDesc = 
    """
    Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
    
    Table 4
    allyl + propene = 4-methylpent-1-en-5-yl

    CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions
    around single bonds, tunneling with Eckart potentials.
    """
)

entry(
    index = 3136,
    label = "Cds-CsH_Cds-CsH;CsJ-CdHH",
    kinetics = Arrhenius(
        A = (1.19E+02, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.700,
        Ea = (11.2, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Wang CBS-QB3""",
    longDesc = 
    """
    Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
    
    Table 4
    allyl + 2-butene = 4-methylhex-1-en-5-yl

    CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions
    around single bonds, tunneling with Eckart potentials.
    """
)