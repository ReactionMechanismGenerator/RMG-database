#!/usr/bin/env python
# encoding: utf-8

name = "SubstitutionS/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "S-RR_or_RRrad;YJ",
    kinetics = ArrheniusEP(
        A = (1e+09, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 1,
    label = "S-HCs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (4.04e+08, 'cm^3/(mol*s)'),
        n = 1.49,
        alpha = 0,
        E0 = (3.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 2,
    label = "S-HCs(CsHH);HJ",
    kinetics = ArrheniusEP(
        A = (3.06e+07, 'cm^3/(mol*s)'),
        n = 2.13,
        alpha = 0,
        E0 = (3.69, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CAC CBS-QB3 1dhr""",
)

entry(
    index = 3,
    label = "S-HCs(CsCsH);HJ",
    kinetics = ArrheniusEP(
        A = (2.84e+08, 'cm^3/(mol*s)'),
        n = 1.59,
        alpha = 0,
        E0 = (3.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 4,
    label = "S-HCs(CsCsCs);HJ",
    kinetics = ArrheniusEP(
        A = (2.79e+08, 'cm^3/(mol*s)'),
        n = 1.63,
        alpha = 0,
        E0 = (2.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 5,
    label = "S-HCds(H);HJ",
    kinetics = ArrheniusEP(
        A = (2.9e+08, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 6,
    label = "S-HCds(Cs);HJ",
    kinetics = ArrheniusEP(
        A = (1.19e+06, 'cm^3/(mol*s)'),
        n = 2.44,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 7,
    label = "S-HCs(CdHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.42e+08, 'cm^3/(mol*s)'),
        n = 1.66,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 8,
    label = "S-HCs(CdCsH);HJ",
    kinetics = ArrheniusEP(
        A = (2.93e+08, 'cm^3/(mol*s)'),
        n = 1.57,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 9,
    label = "S-HCs(CdCsCs);HJ",
    kinetics = ArrheniusEP(
        A = (6.66e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        alpha = 0,
        E0 = (1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 10,
    label = "S-HCs(CtHH);HJ",
    kinetics = ArrheniusEP(
        A = (2.81e+08, 'cm^3/(mol*s)'),
        n = 1.57,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 11,
    label = "S-HCs(CtCsH);HJ",
    kinetics = ArrheniusEP(
        A = (7.79e+08, 'cm^3/(mol*s)'),
        n = 1.49,
        alpha = 0,
        E0 = (2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 12,
    label = "S-HCs(CtCsCs);HJ",
    kinetics = ArrheniusEP(
        A = (4.76e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        alpha = 0,
        E0 = (2.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 13,
    label = "S-Cs(HHH)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.64e+08, 'cm^3/(mol*s)'),
        n = 1.52,
        alpha = 0,
        E0 = (3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 14,
    label = "S-Cs(HHH)Cs(CsHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.98e+08, 'cm^3/(mol*s)'),
        n = 1.51,
        alpha = 0,
        E0 = (3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 15,
    label = "S-Cs(HHH)Cs(CsCsH);HJ",
    kinetics = ArrheniusEP(
        A = (3.68e+08, 'cm^3/(mol*s)'),
        n = 1.48,
        alpha = 0,
        E0 = (3.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 16,
    label = "S-Cs(HHH)Cs(CsCsCs);HJ",
    kinetics = ArrheniusEP(
        A = (3.14e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 17,
    label = "S-Cs(HHH)Cds(H);HJ",
    kinetics = ArrheniusEP(
        A = (2.38e+10, 'cm^3/(mol*s)'),
        n = 0.79,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 18,
    label = "S-Cs(HHH)Cds(Cs);HJ",
    kinetics = ArrheniusEP(
        A = (2.81e+09, 'cm^3/(mol*s)'),
        n = 1.15,
        alpha = 0,
        E0 = (5.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 19,
    label = "S-Cs(HHH)Cs(CdHH);HJ",
    kinetics = ArrheniusEP(
        A = (2.53e+08, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (2.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 20,
    label = "S-Cs(HHH)Cs(CdCsH);HJ",
    kinetics = ArrheniusEP(
        A = (4.05e+08, 'cm^3/(mol*s)'),
        n = 1.49,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 21,
    label = "S-Cs(HHH)Cs(CdCsCs);HJ",
    kinetics = ArrheniusEP(
        A = (1.92e+08, 'cm^3/(mol*s)'),
        n = 1.57,
        alpha = 0,
        E0 = (1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 22,
    label = "S-Cs(HHH)Cs(CtHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.33e+08, 'cm^3/(mol*s)'),
        n = 1.62,
        alpha = 0,
        E0 = (2.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 23,
    label = "S-Cs(HHH)Cs(CtCsH);HJ",
    kinetics = ArrheniusEP(
        A = (1.87e+08, 'cm^3/(mol*s)'),
        n = 1.62,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 24,
    label = "S-Cs(HHH)Cs(CtCsCs);HJ",
    kinetics = ArrheniusEP(
        A = (1.36e+08, 'cm^3/(mol*s)'),
        n = 1.63,
        alpha = 0,
        E0 = (1.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 25,
    label = "S-Cs(HHH)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.64e+08, 'cm^3/(mol*s)'),
        n = 1.52,
        alpha = 0,
        E0 = (3.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 26,
    label = "S-Cs(CsHH)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (6.81e+07, 'cm^3/(mol*s)'),
        n = 1.48,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 27,
    label = "S-Cs(CsCsH)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (6.57e+07, 'cm^3/(mol*s)'),
        n = 1.45,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 28,
    label = "S-Cs(CsCsCs)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (8.66e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 29,
    label = "S-Cds(H)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (8.62e+07, 'cm^3/(mol*s)'),
        n = 1.53,
        alpha = 0,
        E0 = (4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 30,
    label = "S-Cds(Cs)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (7.81e+07, 'cm^3/(mol*s)'),
        n = 1.6,
        alpha = 0,
        E0 = (5.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 31,
    label = "S-Cs(CdHH)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.61e+08, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (3.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 32,
    label = "S-Cs(CdCsH)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.34e+08, 'cm^3/(mol*s)'),
        n = 1.43,
        alpha = 0,
        E0 = (4.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 33,
    label = "S-Cs(CdCsCs)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.31e+08, 'cm^3/(mol*s)'),
        n = 1.52,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 34,
    label = "S-Cs(CtHH)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.21e+08, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (3.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 35,
    label = "S-Cs(CtCsH)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.42e+08, 'cm^3/(mol*s)'),
        n = 1.47,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 36,
    label = "S-Cs(CtCsCs)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (7.68e+07, 'cm^3/(mol*s)'),
        n = 1.59,
        alpha = 0,
        E0 = (4.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 37,
    label = "S-HCs(HHH);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5130, 'cm^3/(mol*s)'),
        n = 2.54,
        alpha = 0,
        E0 = (13.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 38,
    label = "S-HCs(CsHH);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (9810, 'cm^3/(mol*s)'),
        n = 2.55,
        alpha = 0,
        E0 = (11.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 39,
    label = "S-HCs(CsCsH);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5340, 'cm^3/(mol*s)'),
        n = 2.54,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 40,
    label = "S-HCs(CsCsCs);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1.38e+06, 'cm^3/(mol*s)'),
        n = 1.59,
        alpha = 0,
        E0 = (9.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 41,
    label = "S-HCds(H);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (43200, 'cm^3/(mol*s)'),
        n = 2.43,
        alpha = 0,
        E0 = (16.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 42,
    label = "S-HCds(Cs);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (96.1, 'cm^3/(mol*s)'),
        n = 3.24,
        alpha = 0,
        E0 = (14.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 43,
    label = "S-HCs(CdHH);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2720, 'cm^3/(mol*s)'),
        n = 2.64,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 44,
    label = "S-HCs(CdCsH);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3420, 'cm^3/(mol*s)'),
        n = 2.69,
        alpha = 0,
        E0 = (7.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 45,
    label = "S-HCs(CdCsCs);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (9750, 'cm^3/(mol*s)'),
        n = 2.63,
        alpha = 0,
        E0 = (6.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 46,
    label = "S-HCs(CtHH);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3470, 'cm^3/(mol*s)'),
        n = 2.64,
        alpha = 0,
        E0 = (8.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 47,
    label = "S-HCs(CtCsH);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (7000, 'cm^3/(mol*s)'),
        n = 2.65,
        alpha = 0,
        E0 = (7.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 48,
    label = "S-HCs(CtCsCs);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2910, 'cm^3/(mol*s)'),
        n = 2.6,
        alpha = 0,
        E0 = (6.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 49,
    label = "S-Ss(H)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (9.44e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (5.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 50,
    label = "S-Ss(Cs)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (7.47e+07, 'cm^3/(mol*s)'),
        n = 1.66,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 51,
    label = "S-HSs(H);HJ",
    kinetics = ArrheniusEP(
        A = (5.43e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        alpha = 0,
        E0 = (0.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 52,
    label = "S-Cs(HHH)Ss(H);HJ",
    kinetics = ArrheniusEP(
        A = (4.07e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        alpha = 0,
        E0 = (0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 53,
    label = "S-HSs(Cs);HJ",
    kinetics = ArrheniusEP(
        A = (1.03e+09, 'cm^3/(mol*s)'),
        n = 1.54,
        alpha = 0,
        E0 = (0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 54,
    label = "S-Cs(HHH)Ss(Cs);HJ",
    kinetics = ArrheniusEP(
        A = (5.31e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        alpha = 0,
        E0 = (0.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 55,
    label = "S-HSs(H);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (293000, 'cm^3/(mol*s)'),
        n = 1.72,
        alpha = 0,
        E0 = (2.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 56,
    label = "S-HSs(Cs);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3570, 'cm^3/(mol*s)'),
        n = 2.63,
        alpha = 0,
        E0 = (4.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 57,
    label = "S-Cs(HHH)Ss(H);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2020, 'cm^3/(mol*s)'),
        n = 2.72,
        alpha = 0,
        E0 = (3.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 58,
    label = "S-Cs(HHH)Ss(Cs);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5130, 'cm^3/(mol*s)'),
        n = 2.66,
        alpha = 0,
        E0 = (4.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 59,
    label = "S-Ss(H)Ss(H);HJ",
    kinetics = ArrheniusEP(
        A = (3.47e+08, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (1.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 60,
    label = "S-HSs(Ss);HJ",
    kinetics = ArrheniusEP(
        A = (2.34e+09, 'cm^3/(mol*s)'),
        n = 1.56,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 61,
    label = "S-Ss(Cs)Ss(H);HJ",
    kinetics = ArrheniusEP(
        A = (6.14e+08, 'cm^3/(mol*s)'),
        n = 1.63,
        alpha = 0,
        E0 = (1.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 62,
    label = "S-Cs(HHH)Ss(Ss);HJ",
    kinetics = ArrheniusEP(
        A = (5.07e+08, 'cm^3/(mol*s)'),
        n = 1.58,
        alpha = 0,
        E0 = (1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 63,
    label = "S-Ss(Ss)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (8.23e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 64,
    label = "S-Ss(H)Ss(Cs);HJ",
    kinetics = ArrheniusEP(
        A = (1.8e+08, 'cm^3/(mol*s)'),
        n = 1.66,
        alpha = 0,
        E0 = (2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 65,
    label = "S-HSs(Ss);HJ",
    kinetics = ArrheniusEP(
        A = (2.9e+09, 'cm^3/(mol*s)'),
        n = 1.58,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 66,
    label = "S-Ss(Ss)Cs(HHH);HJ",
    kinetics = ArrheniusEP(
        A = (6.95e+07, 'cm^3/(mol*s)'),
        n = 1.64,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 67,
    label = "S-Ss(Cs)Ss(Cs);HJ",
    kinetics = ArrheniusEP(
        A = (3.96e+08, 'cm^3/(mol*s)'),
        n = 1.66,
        alpha = 0,
        E0 = (1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 68,
    label = "S-Cs(HHH)Ss(Ss);HJ",
    kinetics = ArrheniusEP(
        A = (7.39e+08, 'cm^3/(mol*s)'),
        n = 1.61,
        alpha = 0,
        E0 = (0.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 69,
    label = "S-Ss(H)Ss(H);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2410, 'cm^3/(mol*s)'),
        n = 2.7,
        alpha = 0,
        E0 = (3.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 70,
    label = "S-HSs(Ss);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (10700, 'cm^3/(mol*s)'),
        n = 2.68,
        alpha = 0,
        E0 = (1.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 71,
    label = "S-Ss(H)Ss(Cs);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3560, 'cm^3/(mol*s)'),
        n = 2.61,
        alpha = 0,
        E0 = (5.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 72,
    label = "S-Cs(HHH)Ss(Ss);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3850, 'cm^3/(mol*s)'),
        n = 2.69,
        alpha = 0,
        E0 = (1.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 73,
    label = "S-Ss(Cs)Ss(H);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (2490, 'cm^3/(mol*s)'),
        n = 2.69,
        alpha = 0,
        E0 = (3.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 74,
    label = "S-Cs(HHH)Ss(Ss);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (6060, 'cm^3/(mol*s)'),
        n = 2.68,
        alpha = 0,
        E0 = (3.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 75,
    label = "S-Ss(Cs)Ss(Cs);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3710, 'cm^3/(mol*s)'),
        n = 2.65,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 76,
    label = "S-Cs(HHH)Ss(Ss);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5430, 'cm^3/(mol*s)'),
        n = 2.68,
        alpha = 0,
        E0 = (3.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 77,
    label = "S-HH;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (1480, 'cm^3/(mol*s)'),
        n = 2.72,
        alpha = 0,
        E0 = (19.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 78,
    label = "S-HH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (10.2, 'cm^3/(mol*s)'),
        n = 2.96,
        alpha = 0,
        E0 = (18.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 79,
    label = "S-HH;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (0.482, 'cm^3/(mol*s)'),
        n = 3.24,
        alpha = 0,
        E0 = (18.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 80,
    label = "S-HH;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (0.0839, 'cm^3/(mol*s)'),
        n = 3.51,
        alpha = 0,
        E0 = (18.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 81,
    label = "S-HH;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (6.43, 'cm^3/(mol*s)'),
        n = 3.21,
        alpha = 0,
        E0 = (8.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 82,
    label = "S-HH;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (0.717, 'cm^3/(mol*s)'),
        n = 3.37,
        alpha = 0,
        E0 = (9.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 83,
    label = "S-HH;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (15.5, 'cm^3/(mol*s)'),
        n = 3.29,
        alpha = 0,
        E0 = (31.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 84,
    label = "S-HH;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (2.54, 'cm^3/(mol*s)'),
        n = 3.35,
        alpha = 0,
        E0 = (32.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 85,
    label = "S-HH;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (0.46, 'cm^3/(mol*s)'),
        n = 3.41,
        alpha = 0,
        E0 = (32.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 86,
    label = "S-HH;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (29.3, 'cm^3/(mol*s)'),
        n = 3.13,
        alpha = 0,
        E0 = (31.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 87,
    label = "S-HH;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (2.46, 'cm^3/(mol*s)'),
        n = 3.23,
        alpha = 0,
        E0 = (31.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 88,
    label = "S-HH;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (0.205, 'cm^3/(mol*s)'),
        n = 3.46,
        alpha = 0,
        E0 = (31.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 89,
    label = "S-Cs(HHH)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (41.9, 'cm^3/(mol*s)'),
        n = 2.89,
        alpha = 0,
        E0 = (15.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 90,
    label = "S-Cs(HHH)H;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (0.963, 'cm^3/(mol*s)'),
        n = 3.09,
        alpha = 0,
        E0 = (15.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 91,
    label = "S-Cs(HHH)H;CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (0.0719, 'cm^3/(mol*s)'),
        n = 3.31,
        alpha = 0,
        E0 = (16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 92,
    label = "S-Cs(HHH)H;CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (0.00752, 'cm^3/(mol*s)'),
        n = 3.43,
        alpha = 0,
        E0 = (16.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 93,
    label = "S-Cs(HHH)H;CdsJ-H",
    kinetics = ArrheniusEP(
        A = (34.6, 'cm^3/(mol*s)'),
        n = 2.64,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 94,
    label = "S-Cs(HHH)H;CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (0.807, 'cm^3/(mol*s)'),
        n = 3.02,
        alpha = 0,
        E0 = (7.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 95,
    label = "S-Cs(HHH)H;CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (1.78, 'cm^3/(mol*s)'),
        n = 3.29,
        alpha = 0,
        E0 = (28.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 96,
    label = "S-Cs(HHH)H;CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (0.25, 'cm^3/(mol*s)'),
        n = 3.4,
        alpha = 0,
        E0 = (28.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 97,
    label = "S-Cs(HHH)H;CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (0.0101, 'cm^3/(mol*s)'),
        n = 3.51,
        alpha = 0,
        E0 = (28.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 98,
    label = "S-Cs(HHH)H;CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (1.33, 'cm^3/(mol*s)'),
        n = 3.3,
        alpha = 0,
        E0 = (27, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 99,
    label = "S-Cs(HHH)H;CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (0.0674, 'cm^3/(mol*s)'),
        n = 3.5,
        alpha = 0,
        E0 = (26.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 100,
    label = "S-Cs(HHH)H;CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (0.00339, 'cm^3/(mol*s)'),
        n = 3.67,
        alpha = 0,
        E0 = (27.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 101,
    label = "S-Cs(HHH)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (41.9, 'cm^3/(mol*s)'),
        n = 2.89,
        alpha = 0,
        E0 = (15.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 102,
    label = "S-Cs(CsHH)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (48.5, 'cm^3/(mol*s)'),
        n = 2.83,
        alpha = 0,
        E0 = (15.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 103,
    label = "S-Cs(CsCsH)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (26.7, 'cm^3/(mol*s)'),
        n = 2.86,
        alpha = 0,
        E0 = (16.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 104,
    label = "S-Cs(CsCsCs)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (25.1, 'cm^3/(mol*s)'),
        n = 2.82,
        alpha = 0,
        E0 = (17.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 105,
    label = "S-Cds(H)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (21.6, 'cm^3/(mol*s)'),
        n = 2.93,
        alpha = 0,
        E0 = (15.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 106,
    label = "S-Cds(Cs)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (17, 'cm^3/(mol*s)'),
        n = 2.82,
        alpha = 0,
        E0 = (17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 107,
    label = "S-Cs(CdHH)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (38.7, 'cm^3/(mol*s)'),
        n = 2.87,
        alpha = 0,
        E0 = (15.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 108,
    label = "S-Cs(CdCsH)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (35, 'cm^3/(mol*s)'),
        n = 2.79,
        alpha = 0,
        E0 = (16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 109,
    label = "S-Cs(CdCsCs)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (37, 'cm^3/(mol*s)'),
        n = 2.83,
        alpha = 0,
        E0 = (17, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 110,
    label = "S-Cs(CtHH)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (45, 'cm^3/(mol*s)'),
        n = 2.88,
        alpha = 0,
        E0 = (15.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 111,
    label = "S-Cs(CtCsH)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (60.8, 'cm^3/(mol*s)'),
        n = 2.83,
        alpha = 0,
        E0 = (15.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 112,
    label = "S-Cs(CtCsCs)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (16.6, 'cm^3/(mol*s)'),
        n = 2.91,
        alpha = 0,
        E0 = (16.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 113,
    label = "S-HCs(HHH);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (5540, 'cm^3/(mol*s)'),
        n = 2.52,
        alpha = 0,
        E0 = (13.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 114,
    label = "S-HCs(HHH);CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (73.3, 'cm^3/(mol*s)'),
        n = 2.76,
        alpha = 0,
        E0 = (11.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 115,
    label = "S-HCs(HHH);CsJ-CsCsH",
    kinetics = ArrheniusEP(
        A = (2.62, 'cm^3/(mol*s)'),
        n = 2.96,
        alpha = 0,
        E0 = (10.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 116,
    label = "S-HCs(HHH);CsJ-CsCsCs",
    kinetics = ArrheniusEP(
        A = (39.6, 'cm^3/(mol*s)'),
        n = 2.74,
        alpha = 0,
        E0 = (9.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 117,
    label = "S-HCs(HHH);CdsJ-H",
    kinetics = ArrheniusEP(
        A = (245, 'cm^3/(mol*s)'),
        n = 2.88,
        alpha = 0,
        E0 = (5.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 118,
    label = "S-HCs(HHH);CdsJ-Cs",
    kinetics = ArrheniusEP(
        A = (13.4, 'cm^3/(mol*s)'),
        n = 2.97,
        alpha = 0,
        E0 = (4.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 119,
    label = "S-HCs(HHH);CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (84.6, 'cm^3/(mol*s)'),
        n = 3.04,
        alpha = 0,
        E0 = (22.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 120,
    label = "S-HCs(HHH);CsJ-CdCsH",
    kinetics = ArrheniusEP(
        A = (8.56, 'cm^3/(mol*s)'),
        n = 3.23,
        alpha = 0,
        E0 = (21.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 121,
    label = "S-HCs(HHH);CsJ-CdCsCs",
    kinetics = ArrheniusEP(
        A = (1.93, 'cm^3/(mol*s)'),
        n = 3.25,
        alpha = 0,
        E0 = (22, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 122,
    label = "S-HCs(HHH);CsJ-CtHH",
    kinetics = ArrheniusEP(
        A = (103, 'cm^3/(mol*s)'),
        n = 2.96,
        alpha = 0,
        E0 = (21.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 123,
    label = "S-HCs(HHH);CsJ-CtCsH",
    kinetics = ArrheniusEP(
        A = (6.33, 'cm^3/(mol*s)'),
        n = 3.16,
        alpha = 0,
        E0 = (20.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 124,
    label = "S-HCs(HHH);CsJ-CtCsCs",
    kinetics = ArrheniusEP(
        A = (0.36, 'cm^3/(mol*s)'),
        n = 3.32,
        alpha = 0,
        E0 = (20.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 125,
    label = "S-Ss(H)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (44.4, 'cm^3/(mol*s)'),
        n = 3.04,
        alpha = 0,
        E0 = (16.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 126,
    label = "S-Ss(Cs)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (11.3, 'cm^3/(mol*s)'),
        n = 3.03,
        alpha = 0,
        E0 = (16, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 127,
    label = "S-HH;SsJ-H",
    kinetics = ArrheniusEP(
        A = (804, 'cm^3/(mol*s)'),
        n = 3.08,
        alpha = 0,
        E0 = (26.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 128,
    label = "S-Cs(HHH)H;SsJ-H",
    kinetics = ArrheniusEP(
        A = (75.2, 'cm^3/(mol*s)'),
        n = 3.3,
        alpha = 0,
        E0 = (22.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 129,
    label = "S-HH;SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1.25, 'cm^3/(mol*s)'),
        n = 4.01,
        alpha = 0,
        E0 = (24.8, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 130,
    label = "S-Cs(HHH)H;SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (0.0263, 'cm^3/(mol*s)'),
        n = 4.22,
        alpha = 0,
        E0 = (20.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 131,
    label = "S-HCs(HHH);SsJ-H",
    kinetics = ArrheniusEP(
        A = (999, 'cm^3/(mol*s)'),
        n = 3.08,
        alpha = 0,
        E0 = (13.09, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 131,
    label = "S-HCs(HHH);SsJ-H",
    kinetics = ArrheniusEP(
        A = (1180, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (13.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 132,
    label = "S-HCs(HHH);SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1.28, 'cm^3/(mol*s)'),
        n = 3.85,
        alpha = 0,
        E0 = (12.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 133,
    label = "S-Cs(HHH)Cs(HHH);SsJ-H",
    kinetics = ArrheniusEP(
        A = (1770, 'cm^3/(mol*s)'),
        n = 3.03,
        alpha = 0,
        E0 = (12.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 134,
    label = "S-Cs(HHH)Cs(HHH);SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1.17, 'cm^3/(mol*s)'),
        n = 3.89,
        alpha = 0,
        E0 = (12, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 135,
    label = "S-Ss(H)H;SsJ-H",
    kinetics = ArrheniusEP(
        A = (26.7, 'cm^3/(mol*s)'),
        n = 3.36,
        alpha = 0,
        E0 = (21.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 136,
    label = "S-HH;SsJ-Ss",
    kinetics = ArrheniusEP(
        A = (0.859, 'cm^3/(mol*s)'),
        n = 3.89,
        alpha = 0,
        E0 = (37.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 137,
    label = "S-Ss(Cs)H;SsJ-H",
    kinetics = ArrheniusEP(
        A = (83.6, 'cm^3/(mol*s)'),
        n = 3.33,
        alpha = 0,
        E0 = (20.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 138,
    label = "S-Cs(HHH)H;SsJ-Ss",
    kinetics = ArrheniusEP(
        A = (0.0413, 'cm^3/(mol*s)'),
        n = 4.06,
        alpha = 0,
        E0 = (32.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 139,
    label = "S-Ss(Ss)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (68.5, 'cm^3/(mol*s)'),
        n = 3.02,
        alpha = 0,
        E0 = (15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 140,
    label = "S-Ss(H)H;SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (0.0202, 'cm^3/(mol*s)'),
        n = 4.3,
        alpha = 0,
        E0 = (19, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 141,
    label = "S-HH;SsJ-Ss",
    kinetics = ArrheniusEP(
        A = (1.67, 'cm^3/(mol*s)'),
        n = 3.91,
        alpha = 0,
        E0 = (39.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 142,
    label = "S-Ss(Ss)H;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (12.4, 'cm^3/(mol*s)'),
        n = 3.01,
        alpha = 0,
        E0 = (15, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 143,
    label = "S-Ss(Cs)H;SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (0.0168, 'cm^3/(mol*s)'),
        n = 4.25,
        alpha = 0,
        E0 = (17.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 144,
    label = "S-Cs(HHH)H;SsJ-Ss",
    kinetics = ArrheniusEP(
        A = (0.0198, 'cm^3/(mol*s)'),
        n = 4.09,
        alpha = 0,
        E0 = (34.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 145,
    label = "S-Ss(H)Cs(HHH);SsJ-H",
    kinetics = ArrheniusEP(
        A = (467, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (12.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 146,
    label = "S-HCs(HHH);SsJ-Ss",
    kinetics = ArrheniusEP(
        A = (1.08, 'cm^3/(mol*s)'),
        n = 3.79,
        alpha = 0,
        E0 = (23.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 147,
    label = "S-Ss(H)Cs(HHH);SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (0.923, 'cm^3/(mol*s)'),
        n = 3.83,
        alpha = 0,
        E0 = (11.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 148,
    label = "S-Cs(HHH)Cs(HHH);SsJ-Ss",
    kinetics = ArrheniusEP(
        A = (0.607, 'cm^3/(mol*s)'),
        n = 3.8,
        alpha = 0,
        E0 = (25.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 149,
    label = "S-Ss(Cs)Cs(HHH);SsJ-H",
    kinetics = ArrheniusEP(
        A = (2370, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (11.7, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 150,
    label = "S-Cs(HHH)Cs(HHH);SsJ-Ss",
    kinetics = ArrheniusEP(
        A = (2.05, 'cm^3/(mol*s)'),
        n = 3.8,
        alpha = 0,
        E0 = (22.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 151,
    label = "S-Ss(Cs)Cs(HHH);SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (1.07, 'cm^3/(mol*s)'),
        n = 3.86,
        alpha = 0,
        E0 = (10.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 152,
    label = "S-Cs(HHH)Cs(HHH);SsJ-Ss",
    kinetics = ArrheniusEP(
        A = (0.615, 'cm^3/(mol*s)'),
        n = 3.78,
        alpha = 0,
        E0 = (24.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

entry(
    index = 153,
    label = "S-Cs(CsHH)Cs(CsHH);HJ",
    kinetics = ArrheniusEP(
        A = (1.27e+07, 'cm^3/(mol*s)'),
        n = 2.26,
        alpha = 0,
        E0 = (3.83, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""CAC CBS-QB3 1dhr""",
)

entry(
    index = 154,
    label = "S-HCO;HJ",
    kinetics = ArrheniusEP(
        A = (1.26e+09, 'cm^3/(mol*s)'),
        n = 1.46,
        alpha = 0,
        E0 = (3.14, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 1dhr""",
)

entry(
    index = 155,
    label = "S-HCO;CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (3.88e+06, 'cm^3/(mol*s)'),
        n = 1.4,
        alpha = 0,
        E0 = (10.56, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 1dhr""",
)

entry(
    index = 156,
    label = "S-HCs(CsOsH);HJ",
    kinetics = ArrheniusEP(
        A = (3.91e+09, 'cm^3/(mol*s)'),
        n = 1.32,
        alpha = 0,
        E0 = (3.05, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 1dhr""",
)

entry(
    index = 157,
    label = "S-HCs(CsOsH);CsJ-HHH",
    kinetics = ArrheniusEP(
        A = (0.00296, 'cm^3/(mol*s)'),
        n = 5.57,
        alpha = 0,
        E0 = (8.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 1dhr""",
)

entry(
    index = 158,
    label = "S-HCs(CsOsH);CJ",
    kinetics = ArrheniusEP(
        A = (0.00296, 'cm^3/(mol*s)'),
        n = 5.57,
        alpha = 0,
        E0 = (8.47, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""based on 157""",
)

entry(
    index = 159,
    label = "S-HCs(CsOsH);SsJ-H",
    kinetics = ArrheniusEP(
        A = (1180, 'cm^3/(mol*s)'),
        n = 3,
        alpha = 0,
        E0 = (13.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""based on CAC's 131 calc""",
)

entry(
    index = 160,
    label = "S-HSs(H);CsJ-CdHH",
    kinetics = ArrheniusEP(
        A = (930, 'cm^3/(mol*s)'),
        n = 2.61,
        alpha = 0,
        E0 = (10.07, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""CAC CBS-QB3, HO approx""",
)

entry(
    index = 161,
    label = "S-HCs(CsHH);SsJ-Cs",
    kinetics = ArrheniusEP(
        A = (72.5, 'cm^3/(mol*s)'),
        n = 3.21,
        alpha = 0,
        E0 = (11.45, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""CAC CBS-QB3 1dhr""",
)

