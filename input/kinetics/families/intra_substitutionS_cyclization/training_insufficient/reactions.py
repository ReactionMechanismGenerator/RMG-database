#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_cyclization/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
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

This reaction violates the collision limit. Thermo data for CH3S2-2
and CH2S2-2 is based on Group additivity.
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

This reaction violates the collision limit. Thermo data is from 
library.
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

This reaction violates the collision limit. Thermo data for CH3S3
and CH2S2-2 is based on Group additivity.
""",
)

