#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_isomerization/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "XSYJ;YJ;S-RR",
    kinetics = ArrheniusEP(
        A = (1000000000000.0, 's^-1'),
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
    label = "XSR3J_S;CsJ-3-SsHH;S-Cs(HHH)Ss",
    kinetics = ArrheniusEP(
        A = (329000000000.0, 's^-1'),
        n = 0.211,
        alpha = 0,
        E0 = (31.9, 'kcal/mol'),
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
    label = "XSR4J_SS;CsJ-CsHH;S-HSs",
    kinetics = ArrheniusEP(
        A = (288000000000.0, 's^-1'),
        n = 0.108,
        alpha = 0,
        E0 = (21.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

