#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "R_ROSR;R1_doublebond;R2_doublebond;R_O",
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
)

entry(
    index = 2,
    label = "R_ROR;R1_doublebond_CH2;R2_doublebond_CsC;R_O_H",
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
)

entry(
    index = 3,
    label = "R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H",
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
)

entry(
    index = 4,
    label = "R_ROR;R1_doublebond_S;R2_doublebond_H;R_O_H",
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
)

entry(
    index = 5,
    label = "R_ROR;R1_doublebond_S;R2_doublebond_CH3;R_O_H",
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
)

entry(
    index = 6,
    label = "R_ROR;R1_doublebond_S;R2_doublebond_CH2CH3;R_O_H",
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
)
    
entry(
    index = 7,
    label = "R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_R",
    kinetics = ArrheniusEP(
        A = (7040, 's^-1'),
        n = 2.66,
        alpha = 0,
        E0 = (75, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""W.H. Green estimate
                   A,n from R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H
                   Ea = W.H. Green estimate
                   """,
)
    
entry(
    index = 8,
    label = "R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_C",
    kinetics = ArrheniusEP(
        A = (7040, 's^-1'),
        n = 2.66,
        alpha = 0,
        E0 = (84, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""W.H. Green estimate
                   A,n from R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H
                   Ea = C-C BDE
                   """,
)


