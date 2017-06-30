#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_RSR//training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "H2S + CH2O <=> CH4OS",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (24.4, 'cm^3/(mol*s)'),
        n = 3.27,
        alpha = 0,
        E0 = (37.46, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations from CAC, energy from F12a""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Od_Cd/unsub;H_SH
""",
)

entry(
    index = 1,
    label = "H2S + C2H4O <=> C2H6OS",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (612, 'cm^3/(mol*s)'),
        n = 2.96,
        alpha = 0,
        E0 = (36.34, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 calculations from CAC, energy from F12a""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Od_Cd/H/Nd;H_SH
""",
)

entry(
    index = 2,
    label = "H2S + C7H6O <=> C7H8OS",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (96.5, 'cm^3/(mol*s)'),
        n = 2.84,
        alpha = 0,
        E0 = (34.95, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CBS-QB3 by CAC""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: Od_Cd/H/Cb;H_SH
""",
)

entry(
    index = 3,
    label = "H2S + C2H4 <=> C2H6S",
    degeneracy = 4.0,
    kinetics = ArrheniusEP(
        A = (1.776, 'cm^3/(mol*s)'),
        n = 3.55,
        alpha = 0,
        E0 = (44.5, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_SH
""",
)

entry(
    index = 4,
    label = "H2S + C3H6 <=> C3H8S",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (94.2, 'cm^3/(mol*s)'),
        n = 3.02,
        alpha = 0,
        E0 = (42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H2_Cd/H/Nd;H_SH
""",
)

entry(
    index = 5,
    label = "H2S + C4H8 <=> C4H10S",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (93.4, 'cm^3/(mol*s)'),
        n = 3.02,
        alpha = 0,
        E0 = (42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H2_Cd/Cs2;H_SH
""",
)

entry(
    index = 6,
    label = "CH4S + C2H4 <=> C3H8S-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.72, 'cm^3/(mol*s)'),
        n = 3.64,
        alpha = 0,
        E0 = (41.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_SCs(HHH)
""",
)

entry(
    index = 7,
    label = "CH4S + C3H6 <=> C4H10S-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.5, 'cm^3/(mol*s)'),
        n = 3.33,
        alpha = 0,
        E0 = (40.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H2_Cd/H/Nd;H_SCs(HHH)
""",
)

entry(
    index = 8,
    label = "CH4S + C4H8 <=> C5H12S",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (34, 'cm^3/(mol*s)'),
        n = 3.07,
        alpha = 0,
        E0 = (39.9, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H2_Cd/Cs2;H_SCs(HHH)
""",
)

entry(
    index = 9,
    label = "C4H10S-3 + C4H8 <=> C8H18S",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.24, 'cm^3/(mol*s)'),
        n = 3.33,
        alpha = 0,
        E0 = (40.4, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H2_Cd/Cs2;H_SCs(CsCsCs)
""",
)

entry(
    index = 10,
    label = "C2H6S-2 + C2H4 <=> C4H10S-4",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.522, 'cm^3/(mol*s)'),
        n = 3.67,
        alpha = 0,
        E0 = (41.3, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by AGV""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/unsub_Cd/unsub;H_SCs(CsHH)
""",
)

entry(
    index = 11,
    label = "H2S + C3H6O <=> C3H8OS",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (43400, 'cm^3/(mol*s)'),
        n = 2.9,
        alpha = 0,
        E0 = (42, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CBS-QB3 by CAC, 1dhr""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Cd/H/Nd_Cd/H/Os;H_SH
""",
)

entry(
    index = 12,
    label = "H2S + C3H6O-2 <=> C3H8OS-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (3.3, 'cm^3/(mol*s)'),
        n = 3.45,
        alpha = 0,
        E0 = (37.76, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by CAC with 1d-hr, F12a energies""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Od_Cd/CsCs;H_SH
""",
)

entry(
    index = 13,
    label = "H2S + C2H4O2 <=> C2H6O2S",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.626, 'cm^3/(mol*s)'),
        n = 3.56,
        alpha = 0,
        E0 = (38.89, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by CAC with 1d-hr, F12a energies""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Od_Cd/CsOs;H_SH
""",
)

entry(
    index = 14,
    label = "H2S + C2H2O <=> C2H4OS",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.264e-09, 'cm^3/(mol*s)'),
        n = 6.38,
        alpha = 0,
        E0 = (47.58, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 by CAC with 1d-hr, F12a energies""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Od_Cdd;H_SH
""",
)

entry(
    index = 15,
    label = "H2S + C3H4O <=> C3H6OS",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1608, 'cm^3/(mol*s)'),
        n = 2.64,
        alpha = 0,
        E0 = (36.82, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 2,
    shortDesc = u"""CBS-QB3 1d-hr by CAC, F12a energy""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: Od_Cd/H/Cd;H_SH
""",
)

