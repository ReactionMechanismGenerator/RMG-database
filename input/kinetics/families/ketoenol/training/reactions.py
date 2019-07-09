#!/usr/bin/env python
# encoding: utf-8

name = "ketoenol/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H4O <=> C2H4O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (100000, 's^-1'),
        n = 2,
        Ea = (209.2, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""A. G. Vandeputte, general rate""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R_ROSR;R1_doublebond;R2_doublebond;R_O
""",
)

entry(
    index = 2,
    label = "C4H8O <=> C4H8O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (205000, 's^-1'),
        n = 2.37,
        Ea = (204.179, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte, CBS-QB3, HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_CsC;R_O_H
""",
)

entry(
    index = 3,
    label = "C2H4O <=> C2H4O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7040, 's^-1'),
        n = 2.66,
        Ea = (204.179, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""A. G. Vandeputte, BMK/cbsb7, HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H
""",
)

entry(
    index = 4,
    label = "CH2OS <=> CH2OS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (52, 's^-1'),
        n = 3.26,
        Ea = (83.5545, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_S;R2_doublebond_H;R_O_H
""",
)

entry(
    index = 5,
    label = "C2H4OS <=> C2H4OS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (104, 's^-1'),
        n = 3.21,
        Ea = (82.0482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_S;R2_doublebond_CH3;R_O_H
""",
)

entry(
    index = 6,
    label = "C3H6OS <=> C3H6OS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (87.5, 's^-1'),
        n = 3.23,
        Ea = (82.0482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""calculated by CAC, CCSD(T)/vtz f12""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_S;R2_doublebond_CH2CH3;R_O_H
""",
)

entry(
    index = 7,
    label = "C3H6O <=> C3H6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7040, 's^-1'),
        n = 2.66,
        Ea = (313.8, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""W.H. Green estimate
                   A,n from R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H
                   Ea = W.H. Green estimate
                   """,
    longDesc = 
u"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_R
""",
)

entry(
    index = 8,
    label = "C3H6O <=> C3H6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7040, 's^-1'),
        n = 2.66,
        Ea = (351.456, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""W.H. Green estimate
                   A,n from R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_H
                   Ea = C-C BDE
                   """,
    longDesc = 
u"""
Converted to training reaction from rate rule: R_ROR;R1_doublebond_CH2;R2_doublebond_H;R_O_C
""",
)

