#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_ROR/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CH4O + C4H8 <=> C5H12O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (93.6, 'cm^3/(mol*s)'),
        n = 2.85,
        Ea = (175.31, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H2_Cd/Nd2;H_OCmethyl
""",
)

entry(
    index = 2,
    label = "CH4O + C3H6 <=> C4H10O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (24.8, 'cm^3/(mol*s)'),
        n = 2.93,
        Ea = (183.678, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H2_Cd/H/Nd;H_OCmethyl
""",
)

entry(
    index = 3,
    label = "CH4O + C2H4 <=> C3H8O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (94.6, 'cm^3/(mol*s)'),
        n = 3,
        Ea = (196.648, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_OCmethyl
""",
)

entry(
    index = 4,
    label = "H2O + C2H2O <=> C2H4O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (314, 'cm^3/(mol*s)'),
        n = 3.04,
        Ea = (164.85, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: cco_2H;H_OH
""",
)

entry(
    index = 5,
    label = "H2O + C3H4O <=> C3H6O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (103, 'cm^3/(mol*s)'),
        n = 3.05,
        Ea = (171.544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: cco_HNd;H_OH
""",
)

entry(
    index = 6,
    label = "H2O + C4H6O <=> C4H8O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2900, 'cm^3/(mol*s)'),
        n = 2.8,
        Ea = (170.707, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: cco_Nd2;H_OH
""",
)

entry(
    index = 7,
    label = "H2O + C2H4 <=> C2H6O",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (588, 'cm^3/(mol*s)'),
        n = 2.94,
        Ea = (222.17, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_OH
""",
)

entry(
    index = 8,
    label = "H2O + C3H6-2 <=> C3H8O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (454, 'cm^3/(mol*s)'),
        n = 2.74,
        Ea = (238.07, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H/Nd_Cd/H2;H_OH
""",
)

entry(
    index = 9,
    label = "H2O + C3H6 <=> C3H8O-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (130.4, 'cm^3/(mol*s)'),
        n = 2.92,
        Ea = (212.129, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H2_Cd/H/Nd;H_OH
""",
)

entry(
    index = 10,
    label = "H2O + C4H8 <=> C4H10O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2500, 'cm^3/(mol*s)'),
        n = 2.76,
        Ea = (202.924, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H2_Cd/Nd2;H_OH
""",
)

entry(
    index = 11,
    label = "H2O + CH2S <=> CH4OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.486, 'cm^3/(mol*s)'),
        n = 3.55,
        Ea = (101.797, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations by CAC, F12a energy""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Sd_Cd/unsub;H_OH
""",
)

entry(
    index = 12,
    label = "H2O + C2H4S <=> C2H6OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00532, 'cm^3/(mol*s)'),
        n = 3.95,
        Ea = (102.717, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations by CAC, F12a energy""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Sd_Cd/H/Nd;H_OH
""",
)

entry(
    index = 13,
    label = "H2O + C4H4S <=> C4H6OS",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (24.08, 'cm^3/(mol*s)'),
        n = 3.27,
        Ea = (266.814, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Thiophene2;H_OH
""",
)

entry(
    index = 14,
    label = "H2O + C4H4S-2 <=> C4H6OS-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (83.2, 'cm^3/(mol*s)'),
        n = 3.23,
        Ea = (257.023, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Thiophene3;H_OH
""",
)

entry(
    index = 15,
    label = "H2O + C7H6S <=> C7H8OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0328, 'cm^3/(mol*s)'),
        n = 3.89,
        Ea = (122.173, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Sd_Cd/H/Cb;H_OH
""",
)

entry(
    index = 16,
    label = "H2O + C3H6S <=> C3H8OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0001012, 'cm^3/(mol*s)'),
        n = 4.54,
        Ea = (101.713, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Sd_Cd/CsCs;H_OH
""",
)

entry(
    index = 17,
    label = "H2O + C4H8-2 <=> C4H10O-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.0362e+08, 'cm^3/(mol*s)'),
        n = 1.302,
        Ea = (263.174, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/Nd2_Cd/H2;H_OH
""",
)

entry(
    index = 18,
    label = "H2O + C4H6 <=> C4H8O",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (0.0001096, 'cm^3/(mol*s)'),
        n = 4.73,
        Ea = (218.823, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""AG Vandeputte, CBS-QB3 + HO""",
    longDesc = 
u"""
Updated by AG Vandeputte, CBSQB3 + HO,
    calculated for butadiene + H2O -> 2-butenol

Converted to training reaction from rate rule: Cd/H/De_Cd/H2;H_OH
""",
)

entry(
    index = 19,
    label = "CH4O-2 + C2H4 <=> C3H8O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.58e-05, 'cm^3/(mol*s)'),
        n = 3.97,
        Ea = (329.281, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""AG Vandeputte, CBS-QB3 + HO""",
    longDesc = 
u"""
AG Vandeputte, calculated the rate coefficient for methanol + ethene -> propanol

Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;CH3OH
""",
)

entry(
    index = 20,
    label = "H2O + C2H4OS <=> C2H6O2S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.08e-05, 'cm^3/(mol*s)'),
        n = 4.64,
        Ea = (135.436, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Sd_Cd/CsOs;H_OH
""",
)

entry(
    index = 21,
    label = "H2O + COS <=> CH2O2S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.78e-07, 'cm^3/(mol*s)'),
        n = 5.4,
        Ea = (188.698, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 1d-hr calc by CAC, F12a energy""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Sd_Cdd/O2d;H_OH
""",
)

entry(
    index = 22,
    label = "H2O + C3H4S <=> C3H6OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.1196, 'cm^3/(mol*s)'),
        n = 3.75,
        Ea = (122.759, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CBS-QB3 1d-hr by CAC, F12a energy""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Sd_Cd/H/Cd;H_OH
""",
)

