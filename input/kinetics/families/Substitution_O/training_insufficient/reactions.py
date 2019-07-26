#!/usr/bin/env python
# encoding: utf-8

name = "Substitution_O/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 111,
    label = "H2O-2 + CH3O-2 <=> CH4O2-6 + H-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1122.24, 'cm^3/(mol*s)'),
        n = 3.18249,
        Ea = (324.558, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc =
u"""
Converted to training reaction from rate rule: O-HH;OsJ-Cs

This reaction violates the collision limit. All species have thermo 
library values available.
""",
)

entry(
    index = 122,
    label = "CH4O2-7 + CH3O-2 <=> C2H6O3-2 + H-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.92558e-06, 'cm^3/(mol*s)'),
        n = 5.89053,
        Ea = (273.758, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc =
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)H;OsJ-Cs

This reaction violates the collision limit. C2H6O3-2 thermo is based on group 
additivity.
""",
)

entry(
    index = 127,
    label = "HO-2 + C2H6O2-4 <=> CH4O3-4 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (21552.6, 'cm^3/(mol*s)'),
        n = 2.45745,
        Ea = (202.083, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc =
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)Cs(HHH);OsJ-H

This reaction violates the collision limit. CH4O3-4 thermo is based on group
additivity.
""",
)

entry(
    index = 128,
    label = "CH3O-2 + C2H6O2-4 <=> C2H6O3-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0036016, 'cm^3/(mol*s)'),
        n = 5.31614,
        Ea = (66.9829, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc =
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: O-O2s(Cs)Cs(HHH);OsJ-Cs

This reaction violates the collision limit. C2H6O3-2 thermo is based on group
additivity.
""",
)

