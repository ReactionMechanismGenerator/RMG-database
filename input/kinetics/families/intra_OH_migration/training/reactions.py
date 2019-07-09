#!/usr/bin/env python
# encoding: utf-8

name = "intra_OH_migration/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H5O2 <=> C2H5O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.39e+11, 's^-1'),
        n = 0,
        Ea = (112.55, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OOH_S;C_rad_out_2H
""",
)

entry(
    index = 2,
    label = "C3H7O2 <=> C3H7O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.69e+11, 's^-1'),
        n = 0,
        Ea = (101.671, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2OOH_S;C_rad_out_H/NonDeC
""",
)

entry(
    index = 3,
    label = "C3H7O2-3 <=> C3H7O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.47e+10, 's^-1'),
        n = 0,
        Ea = (116.315, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OOH_SS;C_rad_out_2H
""",
)

entry(
    index = 4,
    label = "C4H9O2 <=> C4H9O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.88e+10, 's^-1'),
        n = 0,
        Ea = (111.294, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OOH_SS;C_rad_out_H/NonDeC
""",
)

entry(
    index = 5,
    label = "C5H11O2 <=> C5H11O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.79e+10, 's^-1'),
        n = 0,
        Ea = (110.039, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3OOH_SS;C_rad_out_Cs2
""",
)

entry(
    index = 6,
    label = "C4H9O2-3 <=> C4H9O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.12e+10, 's^-1'),
        n = 0,
        Ea = (68.1992, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OOH_SSS;C_rad_out_2H
""",
)

entry(
    index = 7,
    label = "C5H11O2-3 <=> C5H11O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (65.2704, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OOH_SSS;C_rad_out_H/NonDeC
""",
)

entry(
    index = 8,
    label = "C6H13O2 <=> C6H13O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.71e+09, 's^-1'),
        n = 0,
        Ea = (62.3416, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations (Catherina Wijaya). Treatment of hindered rotor included; hindered rotor PES are done at B3LYP/6-31g(d) level.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4OOH_SSS;C_rad_out_Cs2
""",
)

