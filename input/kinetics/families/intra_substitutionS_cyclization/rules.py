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
        A = (2000000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (20, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "XSR3J_S;SsJ-3-Cs;S-HC",
    kinetics = ArrheniusEP(
        A = (5420000000.0, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (42.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "XSR3J_S;CsJ-3-CsHH;S-HC",
    kinetics = ArrheniusEP(
        A = (93400000000.0, 's^-1'),
        n = 0.6,
        alpha = 1,
        E0 = (35, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "XSR3J_S;CsJ-3-SsHH;S-HSs",
    kinetics = ArrheniusEP(
        A = (304000000000.0, 's^-1'),
        n = 0.5,
        alpha = 2,
        E0 = (40.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "XSR3J_S;SsJ-3-Cs;S-Cs(HHH)C",
    kinetics = ArrheniusEP(
        A = (965000000000.0, 's^-1'),
        n = 1.1,
        alpha = 0,
        E0 = (33.2, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "XSR3J_S;CsJ-3-SsHH;S-Cs(HHH)Ss",
    kinetics = ArrheniusEP(
        A = (1760000000000.0, 's^-1'),
        n = 0.2,
        alpha = 0,
        E0 = (34.6, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "XSR3J_S;CsJ-3-SsHH;S-Ss(H)Ss",
    kinetics = ArrheniusEP(
        A = (2650000000000.0, 's^-1'),
        n = 0.1,
        alpha = 0,
        E0 = (12.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "XSR5J_SSS;CsJ-CsCsH;S-Cs(NonDe)C",
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
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "XSR6J_SSSS;CsJ-CsCsH;S-Cs(NonDe)C",
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
    longDesc = 
u"""

""",
)

