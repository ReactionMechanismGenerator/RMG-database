#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_cyclization/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "XSYJ;YJ;S-RR",
    kinetics = ArrheniusEP(
        A = (2e+12, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""A. G. Vandeputte""",
)

entry(
    index = 2,
    label = "XSR3J_S_Cs;SsJ;S-H",
    kinetics = ArrheniusEP(
        A = (5.42e+09, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (42.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
)

entry(
    index = 3,
    label = "XSR3J_S_Cs;CsJ-HH;S-H",
    kinetics = ArrheniusEP(
        A = (9.34e+10, 's^-1'),
        n = 0.6,
        alpha = 1,
        E0 = (35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
)

entry(
    index = 4,
    label = "XSR3J_S_Ss;CsJ-HH;S-H",
    kinetics = ArrheniusEP(
        A = (3.04e+11, 's^-1'),
        n = 0.5,
        alpha = 2,
        E0 = (40.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
)

entry(
    index = 5,
    label = "XSR3J_S_Ss;SsJ;S-H",
    kinetics = ArrheniusEP(
        A = (9.65e+11, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (33.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
)

entry(
    index = 6,
    label = "XSR3J_S_Ss;CsJ-HH;S-Cs(HHH)",
    kinetics = ArrheniusEP(
        A = (1.76e+12, 's^-1'),
        n = 0.2,
        alpha = 0,
        E0 = (34.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
)

entry(
    index = 7,
    label = "XSR3J_S_Ss;CsJ-HH;S-S2s(H)",
    kinetics = ArrheniusEP(
        A = (2.65e+12, 's^-1'),
        n = 0.1,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
)

entry(
    index = 8,
    label = "XSR5J_SSS_CsRCs;CsJ-CsH;S-Cs(NonDe)",
    kinetics = ArrheniusEP(
        A = (27000, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (7.73, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""AA Calc""",
)

entry(
    index = 9,
    label = "XSR6J_SSSS_CsRRCs;CsJ-CsH;S-Cs(NonDe)",
    kinetics = ArrheniusEP(
        A = (270, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (6.04, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""AA Calc""",
)

