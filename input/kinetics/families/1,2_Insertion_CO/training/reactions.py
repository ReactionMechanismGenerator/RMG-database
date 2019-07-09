#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 1,
    label = "C2H6 + CO <=> C3H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (538, 'cm^3/(mol*s)'),
        n = 3.29,
        Ea = (437.228, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C_methyl_C_methyl
""",
)

entry(
    index = 2,
    label = "H2 + CO <=> CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.89e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (343.506, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;H2
""",
)

entry(
    index = 3,
    label = "CH4 + CO <=> C2H4O",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (65600, 'cm^3/(mol*s)'),
        n = 2.86,
        Ea = (363.59, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C_methane
""",
)

entry(
    index = 4,
    label = "C2H6-2 + CO <=> C3H6O-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (548400, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (357.732, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C_pri/NonDeC
""",
)

entry(
    index = 5,
    label = "C3H8 + CO <=> C4H8O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.532e+06, 'cm^3/(mol*s)'),
        n = 2.07,
        Ea = (343.925, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C/H2/NonDeC
""",
)

entry(
    index = 6,
    label = "C4H10 + CO <=> C5H10O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.89e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (331.373, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: CO;C/H/Cs3
""",
)

entry(
    index = 7,
    label = "CH4O + CO <=> C2H4O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.127, 'cm^3/(mol*s)'),
        n = 3.7,
        Ea = (223.258, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 calculations by Franklin, 2010""",
    longDesc = 
u"""
CBS-QB3 calculations by CFG, Jan 2010 
Methyl group was hindered rotor. ester CO bond also a rotor.

Converted to training reaction from rate rule: CO;CsO_H
""",
)

