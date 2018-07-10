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
    rank = 5,
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
    rank = 5,
    shortDesc = u"""Aaron Vandeputte CBS-QB3 HO""",
)

