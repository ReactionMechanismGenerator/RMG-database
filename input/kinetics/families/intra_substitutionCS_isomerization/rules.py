#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_isomerization/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "XSYJ;C;YJ",
    kinetics = ArrheniusEP(
        A = (1000000000000.0, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
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
    label = "XSR3J_S;C-HHH;CsJ-3-SsHH",
    kinetics = ArrheniusEP(
        A = (1030000000.0, 's^-1'),
        n = 1.057,
        alpha = 0,
        E0 = (45.5, 'kcal/mol'),
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
    label = "XSR4J_SS;C-HHH;CsJ-CsHH",
    kinetics = ArrheniusEP(
        A = (67600000000.0, 's^-1'),
        n = 0.394,
        alpha = 0,
        E0 = (45.7, 'kcal/mol'),
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
    label = "XSR4J_SS;C-HHH;CsJ-SsHH",
    kinetics = ArrheniusEP(
        A = (151000000000.0, 's^-1'),
        n = 0.327,
        alpha = 0,
        E0 = (55.1, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 3,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""

""",
)

