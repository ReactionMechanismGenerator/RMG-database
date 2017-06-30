#!/usr/bin/env python
# encoding: utf-8

name = "Substitution_O/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "H + CH4O <=> H2O + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (39.0416, 'cm^3/(mol*s)'),
        n = 4.3597,
        alpha = 0,
        E0 = (19.0981, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);HJ
""",
)

entry(
    index = 1,
    label = "H + C2H6O <=> H2O + C2H5",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (5567.88, 'cm^3/(mol*s)'),
        n = 3.20344,
        alpha = 0,
        E0 = (20.4702, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CsHH);HJ
""",
)

entry(
    index = 2,
    label = "H + C3H8O <=> H2O + C3H7",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (114441, 'cm^3/(mol*s)'),
        n = 2.92889,
        alpha = 0,
        E0 = (21.7186, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CsCsH);HJ
""",
)

entry(
    index = 3,
    label = "H + C4H10O <=> H2O + C4H9",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.20136e+07, 'cm^3/(mol*s)'),
        n = 2.47266,
        alpha = 0,
        E0 = (21.4759, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CsCsCs);HJ
""",
)

entry(
    index = 4,
    label = "H + C2H4O <=> H2O + C2H3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (211470, 'cm^3/(mol*s)'),
        n = 2.48131,
        alpha = 0,
        E0 = (28.7488, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCds(H);HJ
""",
)

entry(
    index = 5,
    label = "H + C3H6O <=> H2O + C3H5",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.77054e+06, 'cm^3/(mol*s)'),
        n = 2.2995,
        alpha = 0,
        E0 = (27.1044, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCds(Cs);HJ
""",
)

entry(
    index = 6,
    label = "H + C3H6O-2 <=> H2O + C3H5-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (8.34234, 'cm^3/(mol*s)'),
        n = 3.69086,
        alpha = 0,
        E0 = (14.8008, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CdHH);HJ
""",
)

entry(
    index = 7,
    label = "H + C4H8O <=> H2O + C4H7",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (86.3518, 'cm^3/(mol*s)'),
        n = 3.29954,
        alpha = 0,
        E0 = (15.4575, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CdCsH);HJ
""",
)

entry(
    index = 8,
    label = "H + C5H10O <=> H2O + C5H9",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (61645, 'cm^3/(mol*s)'),
        n = 2.05568,
        alpha = 0,
        E0 = (17.7975, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CdCsCs);HJ
""",
)

entry(
    index = 9,
    label = "H + C3H4O <=> H2O + C3H3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (389.816, 'cm^3/(mol*s)'),
        n = 3.3844,
        alpha = 0,
        E0 = (15.9483, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CtHH);HJ
""",
)

entry(
    index = 10,
    label = "H + C4H6O <=> H2O + C4H5",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (135928, 'cm^3/(mol*s)'),
        n = 2.59024,
        alpha = 0,
        E0 = (16.4688, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CtCsH);HJ
""",
)

entry(
    index = 11,
    label = "H + C5H8O <=> H2O + C5H7",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (178246, 'cm^3/(mol*s)'),
        n = 2.81287,
        alpha = 0,
        E0 = (16.6331, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CtCsCs);HJ
""",
)

entry(
    index = 12,
    label = "H + C2H6O-2 <=> CH4O-2 + CH3",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (67650, 'cm^3/(mol*s)'),
        n = 2.90685,
        alpha = 0,
        E0 = (24.375, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(HHH);HJ
""",
)

entry(
    index = 13,
    label = "H + C3H8O-2 <=> CH4O-2 + C2H5",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (552923, 'cm^3/(mol*s)'),
        n = 2.23663,
        alpha = 0,
        E0 = (23.2701, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(CsHH);HJ
""",
)

entry(
    index = 14,
    label = "H + C4H10O-2 <=> CH4O-2 + C3H7",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (7919.31, 'cm^3/(mol*s)'),
        n = 2.85451,
        alpha = 0,
        E0 = (22.9407, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(CsCsH);HJ
""",
)

entry(
    index = 15,
    label = "H + C5H12O <=> CH4O-2 + C4H9",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (5310.83, 'cm^3/(mol*s)'),
        n = 3.32233,
        alpha = 0,
        E0 = (21.1912, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(CsCsCs);HJ
""",
)

entry(
    index = 16,
    label = "H + C3H6O-3 <=> CH4O-2 + C2H3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (5.84382e+09, 'cm^3/(mol*s)'),
        n = 0.40855,
        alpha = 0,
        E0 = (30.3592, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cds(H);HJ
""",
)

entry(
    index = 17,
    label = "H + C4H8O-2 <=> CH4O-2 + C3H5",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.01997e+11, 'cm^3/(mol*s)'),
        n = 0.59721,
        alpha = 0,
        E0 = (31.5375, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cds(Cs);HJ
""",
)

entry(
    index = 18,
    label = "H + C4H8O-3 <=> CH4O-2 + C3H5-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.271178, 'cm^3/(mol*s)'),
        n = 4.39592,
        alpha = 0,
        E0 = (14.8451, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(CdHH);HJ
""",
)

entry(
    index = 19,
    label = "H + C5H10O-2 <=> CH4O-2 + C4H7",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (39.8648, 'cm^3/(mol*s)'),
        n = 3.10695,
        alpha = 0,
        E0 = (14.9909, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(CdCsH);HJ
""",
)

entry(
    index = 20,
    label = "H + C6H12O <=> CH4O-2 + C5H9",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (7.27488, 'cm^3/(mol*s)'),
        n = 3.93967,
        alpha = 0,
        E0 = (18.6481, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(CdCsCs);HJ
""",
)

entry(
    index = 21,
    label = "H + C4H6O-2 <=> CH4O-2 + C3H3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (74.6326, 'cm^3/(mol*s)'),
        n = 3.47951,
        alpha = 0,
        E0 = (16.8647, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(CtHH);HJ
""",
)

entry(
    index = 22,
    label = "H + C5H8O-2 <=> CH4O-2 + C4H5",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2084.17, 'cm^3/(mol*s)'),
        n = 2.71832,
        alpha = 0,
        E0 = (18.1929, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(CtCsH);HJ
""",
)

entry(
    index = 23,
    label = "H + C6H10O <=> CH4O-2 + C5H7",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3599.97, 'cm^3/(mol*s)'),
        n = 3.2324,
        alpha = 0,
        E0 = (18.0013, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(CtCsCs);HJ
""",
)

entry(
    index = 24,
    label = "H + C3H8O-3 <=> C2H6O-3 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (8855.14, 'cm^3/(mol*s)'),
        n = 2.87556,
        alpha = 0,
        E0 = (22.3008, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CsHH)Cs(HHH);HJ
""",
)

entry(
    index = 25,
    label = "H + C4H10O-3 <=> C3H8O-4 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (4.31229, 'cm^3/(mol*s)'),
        n = 3.87313,
        alpha = 0,
        E0 = (22.7174, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CsCsH)Cs(HHH);HJ
""",
)

entry(
    index = 26,
    label = "H + C5H12O-2 <=> C4H10O-4 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.02268, 'cm^3/(mol*s)'),
        n = 4.01774,
        alpha = 0,
        E0 = (21.6109, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CsCsCs)Cs(HHH);HJ
""",
)

entry(
    index = 27,
    label = "H + C3H6O-4 <=> C2H4O-2 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (20.283, 'cm^3/(mol*s)'),
        n = 3.09138,
        alpha = 0,
        E0 = (24.8334, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cds(H)Cs(HHH);HJ
""",
)

entry(
    index = 28,
    label = "H + C4H8O-4 <=> C3H6O-5 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (12.5685, 'cm^3/(mol*s)'),
        n = 3.66046,
        alpha = 0,
        E0 = (26.2118, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cds(Cs)Cs(HHH);HJ
""",
)

entry(
    index = 29,
    label = "H + C4H8O-5 <=> C3H6O-6 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (131.885, 'cm^3/(mol*s)'),
        n = 3.52145,
        alpha = 0,
        E0 = (21.8758, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CdHH)Cs(HHH);HJ
""",
)

entry(
    index = 30,
    label = "H + C5H10O-3 <=> C4H8O-6 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.0459721, 'cm^3/(mol*s)'),
        n = 4.358,
        alpha = 0,
        E0 = (20.8632, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CdCsH)Cs(HHH);HJ
""",
)

entry(
    index = 31,
    label = "H + C6H12O-2 <=> C5H10O-4 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.000646694, 'cm^3/(mol*s)'),
        n = 4.90628,
        alpha = 0,
        E0 = (24.5808, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CdCsCs)Cs(HHH);HJ
""",
)

entry(
    index = 32,
    label = "H + C5H8O-3 <=> C4H6O-3 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.731898, 'cm^3/(mol*s)'),
        n = 4.2888,
        alpha = 0,
        E0 = (22.1527, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CtCsH)Cs(HHH);HJ
""",
)

entry(
    index = 33,
    label = "CH4O + CH3-2 <=> CH4O-3 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (11.2231, 'cm^3/(mol*s)'),
        n = 3.62912,
        alpha = 0,
        E0 = (39.2015, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-HHH
""",
)

entry(
    index = 34,
    label = "C2H6O + CH3-2 <=> CH4O-3 + C2H5",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (39.3494, 'cm^3/(mol*s)'),
        n = 4.19271,
        alpha = 0,
        E0 = (40.7447, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CsHH);CsJ-HHH
""",
)

entry(
    index = 35,
    label = "C3H8O + CH3-2 <=> CH4O-3 + C3H7",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1798.65, 'cm^3/(mol*s)'),
        n = 3.18285,
        alpha = 0,
        E0 = (40.2407, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CsCsH);CsJ-HHH
""",
)

entry(
    index = 36,
    label = "C4H10O + CH3-2 <=> CH4O-3 + C4H9",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (747648, 'cm^3/(mol*s)'),
        n = 2.3481,
        alpha = 0,
        E0 = (41.1119, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CsCsCs);CsJ-HHH
""",
)

entry(
    index = 37,
    label = "C2H4O + CH3-2 <=> CH4O-3 + C2H3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3250.38, 'cm^3/(mol*s)'),
        n = 3.24041,
        alpha = 0,
        E0 = (49.8535, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCds(H);CsJ-HHH
""",
)

entry(
    index = 38,
    label = "C3H6O + CH3-2 <=> CH4O-3 + C3H5",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.51813e+06, 'cm^3/(mol*s)'),
        n = 1.59641,
        alpha = 0,
        E0 = (48.0894, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCds(Cs);CsJ-HHH
""",
)

entry(
    index = 39,
    label = "C3H6O-2 + CH3-2 <=> CH4O-3 + C3H5-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.0537217, 'cm^3/(mol*s)'),
        n = 3.93783,
        alpha = 0,
        E0 = (32.0065, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CdHH);CsJ-HHH
""",
)

entry(
    index = 40,
    label = "C4H8O + CH3-2 <=> CH4O-3 + C4H7",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.29521e-08, 'cm^3/(mol*s)'),
        n = 5.86437,
        alpha = 0,
        E0 = (38.1609, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CdCsH);CsJ-HHH
""",
)

entry(
    index = 41,
    label = "C5H10O + CH3-2 <=> CH4O-3 + C5H9",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.49022e-09, 'cm^3/(mol*s)'),
        n = 6.15234,
        alpha = 0,
        E0 = (38.6267, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CdCsCs);CsJ-HHH
""",
)

entry(
    index = 42,
    label = "C3H4O + CH3-2 <=> CH4O-3 + C3H3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (401.198, 'cm^3/(mol*s)'),
        n = 3.12619,
        alpha = 0,
        E0 = (33.2665, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CtHH);CsJ-HHH
""",
)

entry(
    index = 43,
    label = "C4H6O + CH3-2 <=> CH4O-3 + C4H5",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2115.14, 'cm^3/(mol*s)'),
        n = 3.15487,
        alpha = 0,
        E0 = (33.8102, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CtCsH);CsJ-HHH
""",
)

entry(
    index = 44,
    label = "C5H8O + CH3-2 <=> CH4O-3 + C5H7",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (76057.9, 'cm^3/(mol*s)'),
        n = 1.88123,
        alpha = 0,
        E0 = (33.2447, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(CtCsCs);CsJ-HHH
""",
)

entry(
    index = 45,
    label = "H + H2O2 <=> H2O + HO",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.56874e+08, 'cm^3/(mol*s)'),
        n = 1.83697,
        alpha = 0,
        E0 = (4.77337, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HOs(H);HJ
""",
)

entry(
    index = 46,
    label = "H + CH4O2 <=> CH4O-2 + HO",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (8.01017e+06, 'cm^3/(mol*s)'),
        n = 1.98323,
        alpha = 0,
        E0 = (6.78234, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Os(H);HJ
""",
)

entry(
    index = 47,
    label = "H + CH4O2-2 <=> H2O + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (6.59061e+07, 'cm^3/(mol*s)'),
        n = 1.81476,
        alpha = 0,
        E0 = (4.54109, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HOs(Cs);HJ
""",
)

entry(
    index = 48,
    label = "H + C2H6O2 <=> CH4O-2 + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.4055e+11, 'cm^3/(mol*s)'),
        n = 0.29359,
        alpha = 0,
        E0 = (6.33989, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Os(Cs);HJ
""",
)

entry(
    index = 49,
    label = "H2O2 + CH3-2 <=> CH4O-3 + HO",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (89119.8, 'cm^3/(mol*s)'),
        n = 2.58699,
        alpha = 0,
        E0 = (9.86623, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HOs(H);CsJ-HHH
""",
)

entry(
    index = 50,
    label = "CH4O2-2 + CH3-2 <=> CH4O-3 + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (26526.7, 'cm^3/(mol*s)'),
        n = 2.4453,
        alpha = 0,
        E0 = (9.7718, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HOs(Cs);CsJ-HHH
""",
)

entry(
    index = 51,
    label = "CH4O2 + CH3-2 <=> C2H6O-4 + HO",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (20989.5, 'cm^3/(mol*s)'),
        n = 2.47358,
        alpha = 0,
        E0 = (13.6473, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Os(H);CsJ-HHH
""",
)

entry(
    index = 52,
    label = "CH3-2 + C2H6O2 <=> C2H6O-4 + CH3O",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (2.5992e+07, 'cm^3/(mol*s)'),
        n = 1.07449,
        alpha = 0,
        E0 = (12.8322, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Os(Cs);CsJ-HHH
""",
)

entry(
    index = 53,
    label = "H + H2O3 <=> H2O2-2 + HO",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.73772e+06, 'cm^3/(mol*s)'),
        n = 2.13626,
        alpha = 0,
        E0 = (8.88506, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(H)Os(H);HJ
""",
)

entry(
    index = 54,
    label = "H + H2O3-2 <=> H2O + HO2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (7.17266e+08, 'cm^3/(mol*s)'),
        n = 1.4407,
        alpha = 0,
        E0 = (4.33812, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-HOs(Os);HJ
""",
)

entry(
    index = 55,
    label = "H + CH4O3 <=> CH4O2-3 + HO",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.95051e+06, 'cm^3/(mol*s)'),
        n = 2.54316,
        alpha = 0,
        E0 = (8.72631, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(Cs)Os(H);HJ
""",
)

entry(
    index = 56,
    label = "H + CH4O3-2 <=> CH4O-2 + HO2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (9.56529e+07, 'cm^3/(mol*s)'),
        n = 2.045,
        alpha = 0,
        E0 = (7.70275, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Cs(HHH)Os(Os);HJ
""",
)

entry(
    index = 57,
    label = "H + CH4O3-3 <=> H2O2-2 + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.2409e+06, 'cm^3/(mol*s)'),
        n = 2.35959,
        alpha = 0,
        E0 = (8.92478, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(H)Os(Cs);HJ
""",
)

entry(
    index = 58,
    label = "H + C2H6O3 <=> CH4O2-3 + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (7.95424e+06, 'cm^3/(mol*s)'),
        n = 2.71236,
        alpha = 0,
        E0 = (9.11699, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(Cs)Os(Cs);HJ
""",
)

entry(
    index = 59,
    label = "H2O3 + CH3-2 <=> CH4O2-4 + HO",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1119.49, 'cm^3/(mol*s)'),
        n = 3.06029,
        alpha = 0,
        E0 = (13.8761, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(H)Os(H);CsJ-HHH
""",
)

entry(
    index = 60,
    label = "H2O3-2 + CH3-2 <=> CH4O-3 + HO2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (17942.7, 'cm^3/(mol*s)'),
        n = 2.60187,
        alpha = 0,
        E0 = (8.41087, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-HOs(Os);CsJ-HHH
""",
)

entry(
    index = 61,
    label = "CH4O3-3 + CH3-2 <=> CH4O2-4 + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (152659, 'cm^3/(mol*s)'),
        n = 2.22409,
        alpha = 0,
        E0 = (14.0442, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(H)Os(Cs);CsJ-HHH
""",
)

entry(
    index = 62,
    label = "CH4O3-2 + CH3-2 <=> C2H6O-4 + HO2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (101433, 'cm^3/(mol*s)'),
        n = 2.72306,
        alpha = 0,
        E0 = (13.7891, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Cs(HHH)Os(Os);CsJ-HHH
""",
)

entry(
    index = 63,
    label = "CH4O3 + CH3-2 <=> C2H6O2-2 + HO",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (26016.1, 'cm^3/(mol*s)'),
        n = 2.61392,
        alpha = 0,
        E0 = (15.0158, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(Cs)Os(H);CsJ-HHH
""",
)

entry(
    index = 64,
    label = "CH3-2 + C2H6O3 <=> C2H6O2-2 + CH3O",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (98402.5, 'cm^3/(mol*s)'),
        n = 2.87073,
        alpha = 0,
        E0 = (13.9466, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(Cs)Os(Cs);CsJ-HHH
""",
)

entry(
    index = 65,
    label = "H2O-2 + CH3-2 <=> CH4O-3 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.0141707, 'cm^3/(mol*s)'),
        n = 5.12614,
        alpha = 0,
        E0 = (44.8893, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-HHH
""",
)

entry(
    index = 66,
    label = "H2O-2 + C2H5-2 <=> C2H6O-5 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.905842, 'cm^3/(mol*s)'),
        n = 3.53834,
        alpha = 0,
        E0 = (44.5143, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-CsHH
""",
)

entry(
    index = 67,
    label = "H2O-2 + C3H7-2 <=> C3H8O-5 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (4.8163e-05, 'cm^3/(mol*s)'),
        n = 5.13525,
        alpha = 0,
        E0 = (43.9651, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-CsCsH
""",
)

entry(
    index = 68,
    label = "H2O-2 + C4H9-2 <=> C4H10O-5 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.37409e-05, 'cm^3/(mol*s)'),
        n = 5.03769,
        alpha = 0,
        E0 = (41.7182, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-CsCsCs
""",
)

entry(
    index = 69,
    label = "H2O-2 + C2H3-2 <=> C2H4O-3 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.029503, 'cm^3/(mol*s)'),
        n = 4.11084,
        alpha = 0,
        E0 = (37.881, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CdsJ-H
""",
)

entry(
    index = 70,
    label = "H2O-2 + C3H5-3 <=> C3H6O-7 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.028266, 'cm^3/(mol*s)'),
        n = 4.04095,
        alpha = 0,
        E0 = (37.0712, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CdsJ-Cs
""",
)

entry(
    index = 71,
    label = "H2O-2 + C3H5-4 <=> C3H6O-8 + H-2",
    degeneracy = 4.0,
    kinetics = ArrheniusEP(
        A = (0.00134884, 'cm^3/(mol*s)'),
        n = 4.79715,
        alpha = 0,
        E0 = (54.0636, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-CdHH
""",
)

entry(
    index = 72,
    label = "H2O-2 + C4H7-2 <=> C4H8O-7 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.000213922, 'cm^3/(mol*s)'),
        n = 4.07435,
        alpha = 0,
        E0 = (51.1252, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-CdCsH
""",
)

entry(
    index = 73,
    label = "H2O-2 + C5H9-2 <=> C5H10O-5 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.07987e-05, 'cm^3/(mol*s)'),
        n = 4.75792,
        alpha = 0,
        E0 = (54.0086, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-CdCsCs
""",
)

entry(
    index = 74,
    label = "H2O-2 + C3H3-2 <=> C3H4O-2 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.00180117, 'cm^3/(mol*s)'),
        n = 4.62782,
        alpha = 0,
        E0 = (52.544, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-CtHH
""",
)

entry(
    index = 75,
    label = "H2O-2 + C4H5-2 <=> C4H6O-4 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.000533538, 'cm^3/(mol*s)'),
        n = 4.5494,
        alpha = 0,
        E0 = (50.9634, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-CtCsH
""",
)

entry(
    index = 76,
    label = "H2O-2 + C5H7-2 <=> C5H8O-4 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1.83141e-06, 'cm^3/(mol*s)'),
        n = 5.48115,
        alpha = 0,
        E0 = (50.1267, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;CsJ-CtCsCs
""",
)

entry(
    index = 77,
    label = "CH4O-4 + CH3-2 <=> C2H6O-4 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.02386e-06, 'cm^3/(mol*s)'),
        n = 5.80487,
        alpha = 0,
        E0 = (41.8043, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-HHH
""",
)

entry(
    index = 78,
    label = "CH4O-4 + C2H5-2 <=> C3H8O-6 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (8.43164e-05, 'cm^3/(mol*s)'),
        n = 4.81746,
        alpha = 0,
        E0 = (42.4259, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CsHH
""",
)

entry(
    index = 79,
    label = "CH4O-4 + C3H7-2 <=> C4H10O-6 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.62031e-09, 'cm^3/(mol*s)'),
        n = 6.05127,
        alpha = 0,
        E0 = (41.1164, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CsCsH
""",
)

entry(
    index = 80,
    label = "CH4O-4 + C4H9-2 <=> C5H12O-3 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (4.95558e-11, 'cm^3/(mol*s)'),
        n = 6.18012,
        alpha = 0,
        E0 = (39.6262, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CsCsCs
""",
)

entry(
    index = 81,
    label = "C2H3-2 + CH4O-4 <=> C3H6O-9 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.0166055, 'cm^3/(mol*s)'),
        n = 3.78744,
        alpha = 0,
        E0 = (32.9424, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CdsJ-H
""",
)

entry(
    index = 82,
    label = "CH4O-4 + C3H5-3 <=> C4H8O-8 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.00341995, 'cm^3/(mol*s)'),
        n = 3.88799,
        alpha = 0,
        E0 = (33.7851, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CdsJ-Cs
""",
)

entry(
    index = 83,
    label = "CH4O-4 + C3H5-4 <=> C4H8O-9 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (3.53604e-08, 'cm^3/(mol*s)'),
        n = 6.23988,
        alpha = 0,
        E0 = (48.9367, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CdHH
""",
)

entry(
    index = 84,
    label = "CH4O-4 + C4H7-2 <=> C5H10O-6 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.44203e-07, 'cm^3/(mol*s)'),
        n = 4.39147,
        alpha = 0,
        E0 = (47.0848, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CdCsH
""",
)

entry(
    index = 85,
    label = "CH4O-4 + C5H9-2 <=> C6H12O-3 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.78109e-13, 'cm^3/(mol*s)'),
        n = 7.37017,
        alpha = 0,
        E0 = (50.092, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CdCsCs
""",
)

entry(
    index = 86,
    label = "C3H3-2 + CH4O-4 <=> C4H6O-5 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.01409e-07, 'cm^3/(mol*s)'),
        n = 5.81184,
        alpha = 0,
        E0 = (48.4515, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CtHH
""",
)

entry(
    index = 87,
    label = "C4H5-2 + CH4O-4 <=> C5H8O-5 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.75102e-08, 'cm^3/(mol*s)'),
        n = 5.1553,
        alpha = 0,
        E0 = (47.0894, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CtCsH
""",
)

entry(
    index = 88,
    label = "C5H7-2 + CH4O-4 <=> C6H10O-2 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.82635e-11, 'cm^3/(mol*s)'),
        n = 6.50124,
        alpha = 0,
        E0 = (47.3836, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;CsJ-CtCsCs
""",
)

entry(
    index = 89,
    label = "C2H6O-6 + CH3-2 <=> C3H8O-7 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.01263e-06, 'cm^3/(mol*s)'),
        n = 5.88794,
        alpha = 0,
        E0 = (43.2039, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CsHH)H;CsJ-HHH
""",
)

entry(
    index = 90,
    label = "C3H8O-8 + CH3-2 <=> C4H10O-7 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.23057e-06, 'cm^3/(mol*s)'),
        n = 5.62998,
        alpha = 0,
        E0 = (44.4379, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CsCsH)H;CsJ-HHH
""",
)

entry(
    index = 91,
    label = "C4H10O-8 + CH3-2 <=> C5H12O-4 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.02826e-06, 'cm^3/(mol*s)'),
        n = 5.07693,
        alpha = 0,
        E0 = (45.5946, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CsCsCs)H;CsJ-HHH
""",
)

entry(
    index = 92,
    label = "C2H4O-4 + CH3-2 <=> C3H6O-10 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.49946e-07, 'cm^3/(mol*s)'),
        n = 5.60717,
        alpha = 0,
        E0 = (44.4058, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cds(H)H;CsJ-HHH
""",
)

entry(
    index = 93,
    label = "C3H6O-11 + CH3-2 <=> C4H8O-10 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (4.83798e-09, 'cm^3/(mol*s)'),
        n = 5.97622,
        alpha = 0,
        E0 = (43.9536, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cds(Cs)H;CsJ-HHH
""",
)

entry(
    index = 94,
    label = "C3H6O-12 + CH3-2 <=> C4H8O-11 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (3.1701e-05, 'cm^3/(mol*s)'),
        n = 4.92691,
        alpha = 0,
        E0 = (41.6393, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CdHH)H;CsJ-HHH
""",
)

entry(
    index = 95,
    label = "C4H8O-12 + CH3-2 <=> C5H10O-7 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.30403e-08, 'cm^3/(mol*s)'),
        n = 5.77538,
        alpha = 0,
        E0 = (43.2947, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CdCsH)H;CsJ-HHH
""",
)

entry(
    index = 96,
    label = "C5H10O-8 + CH3-2 <=> C6H12O-4 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.76943e-10, 'cm^3/(mol*s)'),
        n = 6.31699,
        alpha = 0,
        E0 = (44.7354, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CdCsCs)H;CsJ-HHH
""",
)

entry(
    index = 97,
    label = "C4H6O-6 + CH3-2 <=> C5H8O-6 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.04813e-07, 'cm^3/(mol*s)'),
        n = 5.68858,
        alpha = 0,
        E0 = (42.2366, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(CtCsH)H;CsJ-HHH
""",
)

entry(
    index = 98,
    label = "CH4O + C2H5-2 <=> C2H6O-5 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (17.6374, 'cm^3/(mol*s)'),
        n = 3.76118,
        alpha = 0,
        E0 = (38.9976, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CsHH
""",
)

entry(
    index = 99,
    label = "CH4O + C3H7-2 <=> C3H8O-5 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.00208552, 'cm^3/(mol*s)'),
        n = 4.62276,
        alpha = 0,
        E0 = (36.696, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CsCsH
""",
)

entry(
    index = 100,
    label = "CH4O + C4H9-2 <=> C4H10O-5 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.002356, 'cm^3/(mol*s)'),
        n = 4.14669,
        alpha = 0,
        E0 = (35.5629, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CsCsCs
""",
)

entry(
    index = 101,
    label = "C2H3-2 + CH4O <=> C2H4O-3 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.24935, 'cm^3/(mol*s)'),
        n = 4.10349,
        alpha = 0,
        E0 = (33.1943, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CdsJ-H
""",
)

entry(
    index = 102,
    label = "CH4O + C3H5-3 <=> C3H6O-7 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (154.741, 'cm^3/(mol*s)'),
        n = 2.57143,
        alpha = 0,
        E0 = (32.2648, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CdsJ-Cs
""",
)

entry(
    index = 103,
    label = "CH4O + C3H5-4 <=> C3H6O-8 + CH3",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (0.0239308, 'cm^3/(mol*s)'),
        n = 4.27768,
        alpha = 0,
        E0 = (45.4778, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CdHH
""",
)

entry(
    index = 104,
    label = "CH4O + C4H7-2 <=> C4H8O-7 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (8.84018e-11, 'cm^3/(mol*s)'),
        n = 5.87274,
        alpha = 0,
        E0 = (48.0373, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CdCsH
""",
)

entry(
    index = 105,
    label = "CH4O + C5H9-2 <=> C5H10O-5 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.68446e-15, 'cm^3/(mol*s)'),
        n = 8.08814,
        alpha = 0,
        E0 = (49.0466, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CdCsCs
""",
)

entry(
    index = 106,
    label = "C3H3-2 + CH4O <=> C3H4O-2 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (5.10728, 'cm^3/(mol*s)'),
        n = 3.60317,
        alpha = 0,
        E0 = (44.071, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CtHH
""",
)

entry(
    index = 107,
    label = "C4H5-2 + CH4O <=> C4H6O-4 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.0228734, 'cm^3/(mol*s)'),
        n = 4.3476,
        alpha = 0,
        E0 = (42.5136, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CtCsH
""",
)

entry(
    index = 108,
    label = "C5H7-2 + CH4O <=> C5H8O-4 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.00215301, 'cm^3/(mol*s)'),
        n = 3.78307,
        alpha = 0,
        E0 = (40.9472, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);CsJ-CtCsCs
""",
)

entry(
    index = 109,
    label = "HO-2 + H2O-2 <=> H2O2-3 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (29042.8, 'cm^3/(mol*s)'),
        n = 2.91678,
        alpha = 0,
        E0 = (72.6138, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;OsJ-H
""",
)

entry(
    index = 110,
    label = "HO-2 + CH4O-4 <=> CH4O2-5 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (11.0699, 'cm^3/(mol*s)'),
        n = 3.50482,
        alpha = 0,
        E0 = (66.0387, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;OsJ-H
""",
)

entry(
    index = 111,
    label = "H2O-2 + CH3O-2 <=> CH4O2-6 + H-2",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (1122.24, 'cm^3/(mol*s)'),
        n = 3.18249,
        alpha = 0,
        E0 = (77.5712, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HH;OsJ-Cs
""",
)

entry(
    index = 112,
    label = "CH4O-4 + CH3O-2 <=> C2H6O2-3 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.05378, 'cm^3/(mol*s)'),
        n = 3.66741,
        alpha = 0,
        E0 = (71.5519, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)H;OsJ-Cs
""",
)

entry(
    index = 113,
    label = "HO-2 + CH4O <=> H2O2-3 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (27760.5, 'cm^3/(mol*s)'),
        n = 2.90036,
        alpha = 0,
        E0 = (51.4343, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);OsJ-H
""",
)

entry(
    index = 114,
    label = "CH4O + CH3O-2 <=> CH4O2-6 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1244.45, 'cm^3/(mol*s)'),
        n = 3.04659,
        alpha = 0,
        E0 = (57.0105, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-HCs(HHH);OsJ-Cs
""",
)

entry(
    index = 115,
    label = "HO-2 + C2H6O-2 <=> CH4O2-5 + CH3",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (4.65288e+07, 'cm^3/(mol*s)'),
        n = 1.47906,
        alpha = 0,
        E0 = (52.3415, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(HHH);OsJ-H
""",
)

entry(
    index = 116,
    label = "CH3O-2 + C2H6O-2 <=> C2H6O2-3 + CH3",
    degeneracy = 2.0,
    kinetics = ArrheniusEP(
        A = (234442, 'cm^3/(mol*s)'),
        n = 1.9322,
        alpha = 0,
        E0 = (57.3728, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Converted to training reaction from rate rule: O-Cs(HHH)Cs(HHH);OsJ-Cs
""",
)

entry(
    index = 117,
    label = "HO-2 + H2O2-4 <=> H2O3-3 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.00278991, 'cm^3/(mol*s)'),
        n = 4.75128,
        alpha = 0,
        E0 = (60.749, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(H)H;OsJ-H
""",
)

entry(
    index = 118,
    label = "HO2-2 + H2O-2 <=> H2O3-4 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.0267498, 'cm^3/(mol*s)'),
        n = 4.5091,
        alpha = 0,
        E0 = (87.3616, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-HH;OsJ-Os
""",
)

entry(
    index = 119,
    label = "HO-2 + CH4O2-7 <=> CH4O3-4 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.000781287, 'cm^3/(mol*s)'),
        n = 5.15922,
        alpha = 0,
        E0 = (59.9826, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(Cs)H;OsJ-H
""",
)

entry(
    index = 120,
    label = "HO2-2 + CH4O-4 <=> CH4O3-5 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.54686e-05, 'cm^3/(mol*s)'),
        n = 5.55622,
        alpha = 0,
        E0 = (82.0155, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Cs(HHH)H;OsJ-Os
""",
)

entry(
    index = 121,
    label = "H2O2-4 + CH3O-2 <=> CH4O3-6 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.47435e-05, 'cm^3/(mol*s)'),
        n = 5.26357,
        alpha = 0,
        E0 = (65.8518, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(H)H;OsJ-Cs
""",
)

entry(
    index = 122,
    label = "CH4O2-7 + CH3O-2 <=> C2H6O3-2 + H-2",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (2.92558e-06, 'cm^3/(mol*s)'),
        n = 5.89053,
        alpha = 0,
        E0 = (65.4297, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(Cs)H;OsJ-Cs
""",
)

entry(
    index = 123,
    label = "HO-2 + CH4O2-8 <=> H2O3-3 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.376691, 'cm^3/(mol*s)'),
        n = 4.46709,
        alpha = 0,
        E0 = (48.0516, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(H)Cs(HHH);OsJ-H
""",
)

entry(
    index = 124,
    label = "HO2-2 + CH4O <=> H2O3-4 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.00368718, 'cm^3/(mol*s)'),
        n = 4.90384,
        alpha = 0,
        E0 = (65.6429, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-HCs(HHH);OsJ-Os
""",
)

entry(
    index = 125,
    label = "CH4O2-8 + CH3O-2 <=> CH4O3-6 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (1.37223, 'cm^3/(mol*s)'),
        n = 3.91986,
        alpha = 0,
        E0 = (53.283, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(H)Cs(HHH);OsJ-Cs
""",
)

entry(
    index = 126,
    label = "HO2-2 + C2H6O-2 <=> CH4O3-5 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (13.1108, 'cm^3/(mol*s)'),
        n = 3.71859,
        alpha = 0,
        E0 = (67.9505, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Cs(HHH)Cs(HHH);OsJ-Os
""",
)

entry(
    index = 127,
    label = "HO-2 + C2H6O2-4 <=> CH4O3-4 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (21552.6, 'cm^3/(mol*s)'),
        n = 2.45745,
        alpha = 0,
        E0 = (48.299, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(Cs)Cs(HHH);OsJ-H
""",
)

entry(
    index = 128,
    label = "CH3O-2 + C2H6O2-4 <=> C2H6O3-2 + CH3",
    degeneracy = 1.0,
    kinetics = ArrheniusEP(
        A = (0.0036016, 'cm^3/(mol*s)'),
        n = 5.31614,
        alpha = 0,
        E0 = (16.0093, 'kcal/mol'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    referenceType = "<type 'NoneType'>",
    rank = 3,
    shortDesc = u"""CB0-QB3 (1DHR)/UCCSD(T)-F12/vdz-f12""",
    longDesc = 
u"""
Taken from entry: 

Degeneracy not recalculated

Converted to training reaction from rate rule: O-Os(Cs)Cs(HHH);OsJ-Cs
""",
)

