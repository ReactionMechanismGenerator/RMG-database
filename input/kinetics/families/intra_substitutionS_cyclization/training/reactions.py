#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_cyclization/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "CH3S2 <=> CH2S2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.42e+09, 's^-1'),
        n = 1.1,
        Ea = (179.494, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR3J_S_Cs;SsJ;S-H
""",
)

entry(
    index = 2,
    label = "C2H5S <=> C2H4S + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.34e+10, 's^-1'),
        n = 0.6,
        Ea = (146.44, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR3J_S_Cs;CsJ-HH;S-H
""",
)

entry(
    index = 3,
    label = "CH3S2-2 <=> CH2S2-2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.04e+11, 's^-1'),
        n = 0.5,
        Ea = (167.778, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR3J_S_Ss;CsJ-HH;S-H
""",
)

entry(
    index = 4,
    label = "HS3 <=> S3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.65e+11, 's^-1'),
        n = 1.1,
        Ea = (138.909, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR3J_S_Ss;SsJ;S-H
""",
)

entry(
    index = 5,
    label = "C2H5S2 <=> CH2S2-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.76e+12, 's^-1'),
        n = 0.2,
        Ea = (144.766, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR3J_S_Ss;CsJ-HH;S-Cs(HHH)
""",
)

entry(
    index = 6,
    label = "CH3S3 <=> CH2S2-2 + HS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.65e+12, 's^-1'),
        n = 0.1,
        Ea = (50.6264, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR3J_S_Ss;CsJ-HH;S-S2s(H)
""",
)

entry(
    index = 7,
    label = "C6H13S <=> C5H10S + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (27000, 's^-1'),
        n = 0,
        Ea = (32.3423, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""AA Calc""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR5J_SSS_CsRCs;CsJ-CsH;S-Cs(NonDe)
""",
)

entry(
    index = 8,
    label = "C7H15S <=> C6H12S + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (270, 's^-1'),
        n = 0,
        Ea = (25.2714, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""AA Calc""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR6J_SSSS_CsRRCs;CsJ-CsH;S-Cs(NonDe)
""",
)

