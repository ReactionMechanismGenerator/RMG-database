#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "CO + C2H6 <=> C3H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (538, 'cm^3/(mol*s)'),
        n = 3.29,
        Ea = (437.228, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C_methyl_C_methyl
""",
)

entry(
    index = 1,
    label = "CO + H2 <=> CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.89e+09, 'cm^3/(mol*s)'),
        n = 1.16,
        Ea = (343.506, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;H2
""",
)

entry(
    index = 2,
    label = "CO + CH4 <=> C2H4O",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (65600, 'cm^3/(mol*s)'),
        n = 2.86,
        Ea = (363.59, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C_methane
""",
)

entry(
    index = 3,
    label = "CO + C2H6-2 <=> C3H6O-2",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (548400, 'cm^3/(mol*s)'),
        n = 2.53,
        Ea = (357.732, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C_pri/NonDeC
""",
)

entry(
    index = 4,
    label = "CO + C3H8 <=> C4H8O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.532e+06, 'cm^3/(mol*s)'),
        n = 2.07,
        Ea = (343.925, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: Some of the tortional motions in the alkyl part of the
transition states are treated as free rotations as they are relatively loose TSs.

Converted to training reaction from rate rule: CO;C/H2/NonDeC
""",
)

entry(
    index = 5,
    label = "CO + C4H10 <=> C5H10O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.89e+07, 'cm^3/(mol*s)'),
        n = 1.51,
        Ea = (331.373, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""[87]CBS-QB3 calculations from Sumathi 2003.""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: CO;C/H/Cs3
""",
)

entry(
    index = 6,
    label = "CO + CH4O <=> C2H4O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.127, 'cm^3/(mol*s)'),
        n = 3.7,
        Ea = (223.258, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations by Franklin, 2010""",
    longDesc = 
u"""
Taken from entry: CBS-QB3 calculations by CFG, Jan 2010 
Methyl group was hindered rotor. ester CO bond also a rotor.

Converted to training reaction from rate rule: CO;CsO_H
""",
)

