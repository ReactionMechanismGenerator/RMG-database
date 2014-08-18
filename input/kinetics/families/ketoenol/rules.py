#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "R_ROR",
    kinetics = ArrheniusEP(
        A = (100000, 's^-1'),
        n = 2,
        alpha = 0,
        E0 = (50, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""A. G. Vandeputte, general rate""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "Cds/H2_Cds/CsOH",
    kinetics = ArrheniusEP(
        A = (205000, 's^-1'),
        n = 2.37,
        alpha = 0,
        E0 = (48.8, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, CBS-QB3, HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "Cds/H2_Cds/HOH",
    kinetics = ArrheniusEP(
        A = (7040, 's^-1'),
        n = 2.66,
        alpha = 0,
        E0 = (48.8, 'kcal/mol'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""A. G. Vandeputte, BMK/cbsb7, HO""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "S_Cds/HOH",
    kinetics = ArrheniusEP(
        A = (52, 's^-1'),
        n = 3.26,
        alpha = 0,
        E0 = (19.97, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "S_Cds/CH3OH",
    kinetics = ArrheniusEP(
        A = (104, 's^-1'),
        n = 3.21,
        alpha = 0,
        E0 = (18.64, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "S_Cds/CH2CH3OH",
    kinetics = ArrheniusEP(
        A = (87.5, 's^-1'),
        n = 3.23,
        alpha = 0,
        E0 = (18.85, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""

""",
)

