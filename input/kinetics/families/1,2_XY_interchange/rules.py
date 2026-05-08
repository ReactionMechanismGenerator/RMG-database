#!/usr/bin/env python
# encoding: utf-8

name = "1,2_XY_interchange/rules"
shortDesc = u""
longDesc = u"""
Sources:
[1] Ju-Sung Kim, Laura M. Brandt, George L. Heard, and Bert E. Holmes.
    Computational study of the threshold energy for the 1,2-interchange of X and R 
    (X, R = halogens, pseudohalogens, and monovalent hydrocarbon groups) on CH2XCH2R. 
    Canadian Journal of Chemistry. 94(12): 1038-1043. https://doi.org/10.1139/cjc-2016-0293

    Table 1. Threshold energy barriers for interchange reactions (kJ/mol) calculated at 
    the B3PW91/6-311+G(2d,p) level of theory and basis set
"""

entry(
    index = 0,
    label = "XY",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (250, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""default""",
)

entry(
    index = 1,
    label = "YY",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (200, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""default""",
)

entry(
    index = 2,
    label = "FF",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (289, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""E0 from Table 1 in [1]""",
)

entry(
    index = 3,
    label = "ClCl",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (183, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""E0 from Table 1 in [1]""",
)

entry(
    index = 4,
    label = "BrBr",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (141, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""E0 from Table 1 in [1]""",
)

entry(
    index = 5,
    label = "FCl",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (236, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""E0 from Table 1 in [1]""",
)

entry(
    index = 6,
    label = "ClBr",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (162, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""E0 from Table 1 in [1]""",
)

entry(
    index = 7,
    label = "FBr",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (216, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""E0 from Table 1 in [1]""",
)

entry(
    index = 8,
    label = "OY",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (250, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""default""",
)

entry(
    index = 9,
    label = "OF",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (299, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""E0 from Table 1 in [1]""",
    longDesc = 
u"""
Average of OCH3 and OH
""",
)

entry(
    index = 10,
    label = "OCl",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (244.5, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""E0 from Table 1 in [1]""",
    longDesc = 
u"""
Average of OCH3 and OH
""",
)

entry(
    index = 11,
    label = "OBr",
    kinetics = ArrheniusEP(
        A = (1e+13, 's^-1'),
        n = 0,
        alpha = 0,
        E0 = (222.5, 'kJ/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""E0 from Table 1 in [1]""",
    longDesc = 
u"""
Average of OCH3 and OH
""",
)