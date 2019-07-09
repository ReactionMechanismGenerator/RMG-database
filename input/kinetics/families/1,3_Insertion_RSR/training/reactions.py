#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_RSR//training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "H2S + CH2O <=> CH4OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (24.4, 'cm^3/(mol*s)'),
        n = 3.27,
        Ea = (156.733, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations from CAC, energy from F12a""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Od_Cd/unsub;H_SH
""",
)

entry(
    index = 2,
    label = "H2S + C2H4O <=> C2H6OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (612, 'cm^3/(mol*s)'),
        n = 2.96,
        Ea = (152.047, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations from CAC, energy from F12a""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Od_Cd/H/Nd;H_SH
""",
)

entry(
    index = 3,
    label = "H2S + C7H6O <=> C7H8OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (193, 'cm^3/(mol*s)'),
        n = 2.84,
        Ea = (146.231, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CBS-QB3 by CAC""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Od_Cd/H/Cb;H_SH
""",
)

entry(
    index = 4,
    label = "H2S + C2H4 <=> C2H6S",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.776, 'cm^3/(mol*s)'),
        n = 3.55,
        Ea = (186.188, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_SH
""",
)

entry(
    index = 5,
    label = "H2S + C3H6 <=> C3H8S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (94.2, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (175.728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H2_Cd/H/Nd;H_SH
""",
)

entry(
    index = 6,
    label = "H2S + C4H8 <=> C4H10S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (93.4, 'cm^3/(mol*s)'),
        n = 3.02,
        Ea = (175.728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H2_Cd/Cs2;H_SH
""",
)

entry(
    index = 7,
    label = "CH4S + C2H4 <=> C3H8S-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.72, 'cm^3/(mol*s)'),
        n = 3.64,
        Ea = (172.799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_SCs(HHH)
""",
)

entry(
    index = 8,
    label = "CH4S + C3H6 <=> C4H10S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.5, 'cm^3/(mol*s)'),
        n = 3.33,
        Ea = (169.034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H2_Cd/H/Nd;H_SCs(HHH)
""",
)

entry(
    index = 9,
    label = "CH4S + C4H8 <=> C5H12S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (34, 'cm^3/(mol*s)'),
        n = 3.07,
        Ea = (166.942, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H2_Cd/Cs2;H_SCs(HHH)
""",
)

entry(
    index = 10,
    label = "C4H10S-3 + C4H8 <=> C8H18S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.24, 'cm^3/(mol*s)'),
        n = 3.33,
        Ea = (169.034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H2_Cd/Cs2;H_SCs(CsCsCs)
""",
)

entry(
    index = 11,
    label = "C2H6S-2 + C2H4 <=> C4H10S-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.522, 'cm^3/(mol*s)'),
        n = 3.67,
        Ea = (172.799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_SCs(CsHH)
""",
)

entry(
    index = 12,
    label = "H2S + C3H6O <=> C3H8OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (43400, 'cm^3/(mol*s)'),
        n = 2.9,
        Ea = (175.728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CBS-QB3 by CAC, 1dhr""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Cd/H/Nd_Cd/H/Os;H_SH
""",
)

entry(
    index = 13,
    label = "H2S + C3H6O-2 <=> C3H8OS-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.3, 'cm^3/(mol*s)'),
        n = 3.45,
        Ea = (157.988, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by CAC with 1d-hr, F12a energies""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Od_Cd/CsCs;H_SH
""",
)

entry(
    index = 14,
    label = "H2S + C2H4O2 <=> C2H6O2S",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.626, 'cm^3/(mol*s)'),
        n = 3.56,
        Ea = (162.716, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by CAC with 1d-hr, F12a energies""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Od_Cd/CsOs;H_SH
""",
)

entry(
    index = 15,
    label = "H2S + C2H2O <=> C2H4OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.264e-09, 'cm^3/(mol*s)'),
        n = 6.38,
        Ea = (199.075, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 by CAC with 1d-hr, F12a energies""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Od_Cdd;H_SH
""",
)

entry(
    index = 16,
    label = "H2S + C3H4O <=> C3H6OS",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1608, 'cm^3/(mol*s)'),
        n = 2.64,
        Ea = (154.055, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 1d-hr by CAC, F12a energy""",
    longDesc = 
u"""
Converted to training reaction from rate rule: Od_Cd/H/Cd;H_SH
""",
)

