#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionS_isomerization/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H5S2 <=> C2H5S2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.29e+11, 's^-1'),
        n = 0.211,
        Ea = (133.47, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR3J_S;CsJ-HH;S-Cs(HHH)S2s
""",
)

entry(
    index = 2,
    label = "C2H5S2-3 <=> C2H5S2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.88e+11, 's^-1'),
        n = 0.108,
        Ea = (91.6296, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: XSR4J_SS_Cs;CsJ-HH;S-HSs
""",
)

