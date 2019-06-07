#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "H2 + CO2 <=> CH2O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.51e+09, 'cm^3/(mol*s)'),
        n = 1.23,
        Ea = (309.198, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: CO2_Cdd;H2
""",
)

entry(
    index = 2,
    label = "CH4 + CO2 <=> C2H4O2",
    degeneracy = 8.0,
    kinetics = Arrhenius(
        A = (36240, 'cm^3/(mol*s)'),
        n = 2.83,
        Ea = (331.373, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: CO2_Cdd;C_methane
""",
)

entry(
    index = 3,
    label = "C2H6 + CO2 <=> C3H6O2",
    degeneracy = 12.0,
    kinetics = Arrhenius(
        A = (130800, 'cm^3/(mol*s)'),
        n = 2.56,
        Ea = (320.494, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: CO2_Cdd;C_pri/NonDeC
""",
)

entry(
    index = 4,
    label = "C3H8 + CO2 <=> C4H8O2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (424000, 'cm^3/(mol*s)'),
        n = 2.13,
        Ea = (322.168, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: CO2_Cdd;C/H2/NonDeC
""",
)

entry(
    index = 5,
    label = "C3H8-2 + CO2-2 <=> C4H8O2-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (292, 'cm^3/(mol*s)'),
        n = 3.13,
        Ea = (493.712, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte calculation for methylpropanate using BMK/CBSB7""",
    longDesc = 
u"""
Converted to training reaction from rate rule: CO2_Od;C_methyl_C_pri
""",
)

