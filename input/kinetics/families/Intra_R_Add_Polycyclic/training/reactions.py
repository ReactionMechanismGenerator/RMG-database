#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Polycyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.69e+11, 's^-1'), n=0.24, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addA <=> product1
""",
)

entry(
    index = 1,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.21e+11, 's^-1'), n=0.46, Ea=(16.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product1 <=> product2
""",
)

entry(
    index = 2,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.52e+11, 's^-1'), n=0.16, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product3
""",
)

entry(
    index = 3,
    label = "C7H9-7 <=> C7H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.56e+11, 's^-1'), n=0.55, Ea=(26.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product3 <=> product4
""",
)

entry(
    index = 4,
    label = "C7H9-9 <=> C7H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.01e+11, 's^-1'), n=0.59, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product8 <=> product9
""",
)

entry(
    index = 5,
    label = "C7H9-11 <=> C7H9-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.98e+11, 's^-1'), n=0.06, Ea=(19.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product17
""",
)

entry(
    index = 6,
    label = "C7H9-13 <=> C7H9-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.29e+12, 's^-1'), n=0.15, Ea=(2.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product18 <=> product19
""",
)

entry(
    index = 7,
    label = "C7H9-15 <=> C7H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41e+11, 's^-1'), n=0.2, Ea=(46.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product21 <=> product23
""",
)

entry(
    index = 8,
    label = "C7H9-17 <=> C7H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.39e+11, 's^-1'), n=0.26, Ea=(26.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product22 <=> product25
""",
)

entry(
    index = 9,
    label = "C7H9-19 <=> C7H9-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.11e+10, 's^-1'), n=0.18, Ea=(66.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product22 <=> product29
""",
)

entry(
    index = 10,
    label = "C7H7 <=> C7H7-2",
    degeneracy = 7.0,
    kinetics = Arrhenius(A=(1.56e+13, 's^-1'), n=0, Ea=(43.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product33 <=> product34
""",
)

entry(
    index = 11,
    label = "C7H9-21 <=> C7H9-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.51e+10, 's^-1'), n=0.25, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product35 <=> product36
""",
)

entry(
    index = 12,
    label = "C7H9-23 <=> C7H9-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.4e+12, 's^-1'), n=0.39, Ea=(16, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product36 <=> product37
""",
)

entry(
    index = 13,
    label = "C7H7-3 <=> C7H7-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.32e+11, 's^-1'), n=0.3, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product44 <=> product45
""",
)

entry(
    index = 14,
    label = "C7H7-5 <=> C7H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.84e+11, 's^-1'), n=0.66, Ea=(23.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product45 <=> product33
""",
)

entry(
    index = 15,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.18e+11, 's^-1'), n=0.17, Ea=(4.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: C5H5CH2-1 <=> biring1
""",
)

entry(
    index = 16,
    label = "C6H7-3 <=> C6H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.51e+11, 's^-1'), n=0.41, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: biring1 <=> cyC6H7
""",
)

entry(
    index = 17,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.7e+12, 's^-1'), n=0, Ea=(17.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: fascella""",
    longDesc = 
u"""
Taken from entry: C9H91 <=> C9H9c4
""",
)

entry(
    index = 18,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.89e+11, 's^-1'), n=0.12, Ea=(9.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: adducta <=> prod1
""",
)

entry(
    index = 19,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.73e+11, 's^-1'), n=0.31, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod1 <=> prod2
""",
)

entry(
    index = 20,
    label = "C10H9-5 <=> C10H9-6",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(4.14e+11, 's^-1'), n=0.34, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod2 <=> prod3
""",
)

entry(
    index = 21,
    label = "C10H9-7 <=> C10H9-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.42e+11, 's^-1'), n=0.22, Ea=(4.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod5 <=> prod4
""",
)

entry(
    index = 22,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.51e+11, 's^-1'), n=0.58, Ea=(29.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt7 <=> pdt8
""",
)

entry(
    index = 23,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.69e+11, 's^-1'), n=0.22, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt18 <=> pdt19
""",
)

entry(
    index = 24,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.9e+10, 's^-1'), n=0.29, Ea=(21.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt20 <=> pdt21
""",
)

entry(
    index = 25,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt23
""",
)

entry(
    index = 26,
    label = "C10H11-9 <=> C10H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.48e+11, 's^-1'), n=0.26, Ea=(7.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt17 <=> pdt24
""",
)

entry(
    index = 27,
    label = "C10H11-11 <=> C10H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.43e+12, 's^-1'), n=0.31, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt24 <=> pdt28
""",
)

entry(
    index = 28,
    label = "C10H11-13 <=> C10H11-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0.41, Ea=(32.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt25 <=> pdt32
""",
)

entry(
    index = 29,
    label = "C10H11-15 <=> C10H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.16e+10, 's^-1'), n=0.2, Ea=(24.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt33 <=> pdt29
""",
)

entry(
    index = 30,
    label = "C10H11-17 <=> C10H11-18",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.51e+11, 's^-1'), n=0.28, Ea=(12.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt57
""",
)

entry(
    index = 31,
    label = "C10H11-19 <=> C10H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.75e+11, 's^-1'), n=0.44, Ea=(18.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt57 <=> pdt12
""",
)

entry(
    index = 32,
    label = "C9H9-3 <=> C9H9-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.257e+11, 's^-1'), n=0.139, Ea=(13.233, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9(13) <=> C9H9(14)
""",
)

