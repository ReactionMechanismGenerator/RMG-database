#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 106,
    label = "C7H9-9 <=> C7H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.98e+11, 's^-1'),
        n = 0.21,
        Ea = (64.8938, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc =
u"""
Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_csNdCt

This training reaction has fast rates for low temperatures. Thermo data for C7H9-9 and C7H9-10 is from `Group additivity`.
""",
)

entry(
    index = 114,
    label = "C8H11-5 <=> C8H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.08e+12, 's^-1'),
        n = 0.21,
        Ea = (64.3499, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc =
u"""
Converted to training reaction from rate rule: R4_S_D;doublebond_intra_HNd_pri;radadd_intra_csNdCt

This training reaction has fast rates for low temperatures. Thermo data for C8H11-5 and C8H11-6 is from `Group additivity`.
""",
)

entry(
    index = 121,
    label = "C8H11-7 <=> C8H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.31e+12, 's^-1'),
        n = 0.21,
        Ea = (58.9526, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc =
u"""
Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csHCt

This training reaction has fast rates for low temperatures. Thermo data for C8H11-7 and C8H11-8 is from `Group additivity`.
""",
)

entry(
    index = 122,
    label = "C9H13-9 <=> C9H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.48e+12, 's^-1'),
        n = 0.21,
        Ea = (63.1784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Aaron Vandeputte small GA method""",
    longDesc =
u"""
Converted to training reaction from rate rule: R4_S_D;doublebond_intra_NdNd_pri;radadd_intra_csNdCt

This training reaction has fast rates for low temperatures. Thermo data for C9H13-9 and C9H13-10 is from `Group additivity`.
""",
)

