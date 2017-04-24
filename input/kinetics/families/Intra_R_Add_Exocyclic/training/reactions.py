#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""


entry(
    index = 1,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.32e+10, 's^-1'), n=0.35, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product38 <=> product39
""",
)

entry(
    index = 2,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.95e+12, 's^-1'), n=0.12, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product39 <=> product37
""",
)



entry(
    index = 3,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.69e+11, 's^-1'), n=0.22, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt18 <=> pdt19
""",
)

entry(
    index = 4,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt23
""",
)

entry(
    index = 5,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.02e+11, 's^-1'), n=0.79, Ea=(35.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt55 <=> pdt58
""",
)



entry(
    index = 6,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 's^-1'), n=0.45, Ea=(25.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod2 <=> prod5
""",
)

entry(
    index = 7,
    label = "C9H11 <=> C9H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.399e+11, 's^-1'), n=0.121, Ea=(15.859, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2012_Kislov_Phenyl_Propene_w_new_pathway""",
    longDesc = 
u"""
Taken from entry: i2 <=> i3
""",
)

entry(
    index = 8,
    label = "C9H11-5 <=> C9H11-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.815e+11, 's^-1'), n=0.121, Ea=(32.19, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2012_Kislov_Phenyl_Propene_w_new_pathway""",
    longDesc = 
u"""
Taken from entry: i2 <=> i8
""",
)

entry(
    index = 9,
    label = "C9H11-3 <=> C9H11-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.528e+11, 's^-1'), n=0.199, Ea=(16.505, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2012_Kislov_Phenyl_Propene_w_new_pathway""",
    longDesc = 
u"""
Taken from entry: i1 <=> i3
""",
)

entry(
    index = 10,
    label = "C9H11-7 <=> C9H11-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.31e+11, 's^-1'), n=0.001, Ea=(17.806, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2012_Kislov_Phenyl_Propene_w_new_pathway""",
    longDesc = 
u"""
Taken from entry: i4 <=> i5
""",
)


entry(
    index = 11,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.249e+08, 's^-1'), n=0.846, Ea=(19.298, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_Vinyl_1_3_Butadiene""",
    longDesc = 
u"""
Taken from entry: C6H9 <=> c5-C6H9
""",
)



entry(
    index = 12,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.54e+10, 's^-1'), n=0.69, Ea=(20.376, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W2 <=> W8
""",
)

entry(
    index = 13,
    label = "C10H9-5 <=> C10H9-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.423e+09, 's^-1'), n=0.834, Ea=(24.235, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W2 <=> W19
""",
)

entry(
    index = 14,
    label = "C10H9-7 <=> C10H9-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.233e+11, 's^-1'), n=0.39, Ea=(35.846, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W3 <=> W19
""",
)

entry(
    index = 15,
    label = "C10H9-9 <=> C10H9-10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.126e+14, 's^-1'), n=-0.355, Ea=(28.539, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W9 <=> W8
""",
)

entry(
    index = 16,
    label = "C10H9-11 <=> C10H9-12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.258e+10, 's^-1'), n=0.21, Ea=(7.415, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W10 <=> W13
""",
)

entry(
    index = 17,
    label = "C10H9-13 <=> C10H9-14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.881e+08, 's^-1'), n=1.062, Ea=(16.546, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W14 <=> W15
""",
)

entry(
    index = 18,
    label = "C10H9-15 <=> C10H9-16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.443e+10, 's^-1'), n=0.474, Ea=(23.82, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W16 <=> W15
""",
)



entry(
    index = 19,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.257e+11, 's^-1'), n=0.139, Ea=(13.233, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9(13) <=> C9H9(14)
""",
)

entry(
    index = 20,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.18e+11, 's^-1'), n=0.17, Ea=(4.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: C5H5CH2-1 <=> biring1
""",
)

entry(
    index = 21,
    label = "C6H7-3 <=> C6H7-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.51e+11, 's^-1'), n=0.41, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: biring1 <=> cyC6H7
""",
)



entry(
    index = 22,
    label = "C10H9-17 <=> C10H9-18",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.89e+11, 's^-1'), n=0.12, Ea=(9.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: adducta <=> prod1
""",
)

entry(
    index = 23,
    label = "C10H9-19 <=> C10H9-20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.73e+11, 's^-1'), n=0.31, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod1 <=> prod2
""",
)

entry(
    index = 24,
    label = "C10H9-21 <=> C10H9-22",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.14e+11, 's^-1'), n=0.34, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod2 <=> prod3
""",
)

entry(
    index = 25,
    label = "C10H9-11 <=> C10H9-12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.42e+11, 's^-1'), n=0.22, Ea=(4.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod5 <=> prod4
""",
)



entry(
    index = 26,
    label = "C10H9-23 <=> C10H9-24",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.79e+11, 's^-1'), n=0.33, Ea=(10.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod3 <=> prod4
""",
)



entry(
    index = 27,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+11, 's^-1'), n=0.29, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: adductd <=> pdt7
""",
)

entry(
    index = 28,
    label = "C10H11-9 <=> C10H11-10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.25e+09, 's^-1'), n=0.76, Ea=(6.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt9 <=> pdt10bis
""",
)

entry(
    index = 29,
    label = "C10H11-11 <=> C10H11-12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.43e+11, 's^-1'), n=0.21, Ea=(8.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: adducte <=> pdt7
""",
)

entry(
    index = 30,
    label = "C10H11-13 <=> C10H11-14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.36e+10, 's^-1'), n=0.44, Ea=(32.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt16 <=> pdt17
""",
)

entry(
    index = 31,
    label = "C10H11-15 <=> C10H11-16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.48e+11, 's^-1'), n=0.26, Ea=(7.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt17 <=> pdt24
""",
)

entry(
    index = 32,
    label = "C10H11-17 <=> C10H11-18",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.43e+12, 's^-1'), n=0.31, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt24 <=> pdt28
""",
)

entry(
    index = 33,
    label = "C10H11-19 <=> C10H11-20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.51e+11, 's^-1'), n=0.28, Ea=(12.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt57
""",
)

entry(
    index = 34,
    label = "C10H11-21 <=> C10H11-22",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.75e+11, 's^-1'), n=0.44, Ea=(18.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt57 <=> pdt12
""",
)



entry(
    index = 35,
    label = "C10H11-23 <=> C10H11-24",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.51e+11, 's^-1'), n=0.58, Ea=(29.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt7 <=> pdt8
""",
)

entry(
    index = 36,
    label = "C10H11-25 <=> C10H11-26",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.39e+10, 's^-1'), n=0.91, Ea=(36.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt8 <=> pdt9
""",
)



entry(
    index = 37,
    label = "C10H11-27 <=> C10H11-28",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.27e+10, 's^-1'), n=1.01, Ea=(40.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt23 <=> pdt9
""",
)

entry(
    index = 38,
    label = "C10H11-29 <=> C10H11-30",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0.41, Ea=(32.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt25 <=> pdt32
""",
)



entry(
    index = 39,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.69e+11, 's^-1'), n=0.24, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addA <=> product1
""",
)

entry(
    index = 40,
    label = "C7H9-7 <=> C7H9-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.21e+11, 's^-1'), n=0.46, Ea=(16.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product1 <=> product2
""",
)

entry(
    index = 41,
    label = "C7H9-9 <=> C7H9-10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52e+11, 's^-1'), n=0.16, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product3
""",
)

entry(
    index = 42,
    label = "C7H9-11 <=> C7H9-12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.56e+11, 's^-1'), n=0.55, Ea=(26.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product3 <=> product4
""",
)

entry(
    index = 43,
    label = "C7H9-13 <=> C7H9-14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.95e+10, 's^-1'), n=0.53, Ea=(31.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product16 <=> product5
""",
)

entry(
    index = 44,
    label = "C7H9-15 <=> C7H9-16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.37e+11, 's^-1'), n=0.73, Ea=(25.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product6 <=> product5
""",
)

entry(
    index = 45,
    label = "C7H9-17 <=> C7H9-18",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+11, 's^-1'), n=0.59, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product8 <=> product9
""",
)

entry(
    index = 46,
    label = "C7H9-19 <=> C7H9-20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.98e+11, 's^-1'), n=0.06, Ea=(19.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product17
""",
)

entry(
    index = 47,
    label = "C7H9-21 <=> C7H9-22",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+12, 's^-1'), n=0.15, Ea=(2.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product18 <=> product19
""",
)

entry(
    index = 48,
    label = "C7H9-23 <=> C7H9-24",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+11, 's^-1'), n=0.2, Ea=(46.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product21 <=> product23
""",
)

entry(
    index = 49,
    label = "C7H9-25 <=> C7H9-26",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.11e+10, 's^-1'), n=0.18, Ea=(66.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product22 <=> product29
""",
)

entry(
    index = 50,
    label = "C7H7 <=> C7H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.56e+13, 's^-1'), n=0, Ea=(43.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product33 <=> product34
""",
)

entry(
    index = 51,
    label = "C7H9-27 <=> C7H9-28",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.51e+10, 's^-1'), n=0.25, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product35 <=> product36
""",
)

entry(
    index = 52,
    label = "C7H9-29 <=> C7H9-30",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 's^-1'), n=0.39, Ea=(16, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product36 <=> product37
""",
)

entry(
    index = 53,
    label = "C7H7-3 <=> C7H7-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.32e+11, 's^-1'), n=0.3, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product44 <=> product45
""",
)

entry(
    index = 54,
    label = "C7H7-5 <=> C7H7-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.84e+11, 's^-1'), n=0.66, Ea=(23.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product45 <=> product33
""",
)



entry(
    index = 55,
    label = "C7H9-31 <=> C7H9-32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.58e+12, 's^-1'), n=0.31, Ea=(16, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product19 <=> product20
""",
)

entry(
    index = 56,
    label = "C7H7-7 <=> C7H7-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.85e+11, 's^-1'), n=0.49, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product46 <=> BENZYL
""",
)



entry(
    index = 57,
    label = "C7H9-33 <=> C7H9-34",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+11, 's^-1'), n=0.82, Ea=(22.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product23 <=> product24
""",
)



entry(
    index = 58,
    label = "C8H7O <=> C8H7O-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.1405e+11, 's^-1'), n=0.213, Ea=(30.11, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: OH_phenylacetylene_CBSQB3""",
    longDesc = 
u"""
Taken from entry: i4_9 <=> i6
""",
)



entry(
    index = 59,
    label = "C9H9-3 <=> C9H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.66e+11, 's^-1'), n=0.412, Ea=(27.805, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2016_Mebel_C6H9""",
    longDesc = 
u"""
Taken from entry: W1_2 <=> W31
""",
)

entry(
    index = 60,
    label = "C9H9-5 <=> C9H9-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.454e+11, 's^-1'), n=0.447, Ea=(24.536, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2016_Mebel_C6H9""",
    longDesc = 
u"""
Taken from entry: W3_4 <=> W31
""",
)

entry(
    index = 61,
    label = "C9H9-7 <=> C9H9-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.185e+11, 's^-1'), n=0.586, Ea=(37.614, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2016_Mebel_C6H9""",
    longDesc = 
u"""
Taken from entry: W6 <=> W29
""",
)

entry(
    index = 62,
    label = "C9H9-9 <=> C9H9-10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.241e+10, 's^-1'), n=0.754, Ea=(22.335, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2016_Mebel_C6H9""",
    longDesc = 
u"""
Taken from entry: W11 <=> W29
""",
)

entry(
    index = 63,
    label = "C9H9-11 <=> C9H9-12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.932e+07, 's^-1'), n=1.035, Ea=(14.54, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2016_Mebel_C6H9""",
    longDesc = 
u"""
Taken from entry: W21 <=> W24
""",
)

entry(
    index = 64,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.258e+10, 's^-1'), n=0.51, Ea=(12.883, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2016_Mebel_C6H9""",
    longDesc = 
u"""
Taken from entry: W20 <=> W18
""",
)

entry(
    index = 65,
    label = "C9H9-13 <=> C9H9-14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.713e+10, 's^-1'), n=0.481, Ea=(30.309, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2016_Mebel_C6H9""",
    longDesc = 
u"""
Taken from entry: W45 <=> W24
""",
)



entry(
    index = 66,
    label = "C9H9-15 <=> C9H9-16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.63e+12, 's^-1'), n=-0.455, Ea=(30.695, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2016_Mebel_C6H9""",
    longDesc = 
u"""
Taken from entry: W8_9 <=> W15
""",
)



entry(
    index = 67,
    label = "C10H11-31 <=> C10H11-32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(324000, 's^-1'), n=1.64, Ea=(110.61, 'kJ/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2005_Ismail_C6H5_C4H6""",
    longDesc = 
u"""
Taken from entry: (4)phenyl_buten_3_yl <=> trihydronaphthalene
""",
)



entry(
    index = 68,
    label = "C10H9-25 <=> C10H9-26",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.311e+09, 's^-1'), n=0.537, Ea=(2.307, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H9_Mebel_TST""",
    longDesc = 
u"""
Taken from entry: W5 <=> W8
""",
)

entry(
    index = 69,
    label = "C10H9-27 <=> C10H9-28",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.588e+10, 's^-1'), n=0.535, Ea=(9.58, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H9_Mebel_TST""",
    longDesc = 
u"""
Taken from entry: W8 <=> W13
""",
)

entry(
    index = 70,
    label = "C10H9-29 <=> C10H9-30",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.53e+12, 's^-1'), n=0.189, Ea=(29.234, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H9_Mebel_TST""",
    longDesc = 
u"""
Taken from entry: W6 <=> W13
""",
)

entry(
    index = 71,
    label = "C10H9-31 <=> C10H9-32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.161e+12, 's^-1'), n=0.277, Ea=(28.025, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H9_Mebel_TST""",
    longDesc = 
u"""
Taken from entry: W13 <=> W107
""",
)

entry(
    index = 72,
    label = "C10H9-33 <=> C10H9-34",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.998e+12, 's^-1'), n=0.237, Ea=(16.277, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H9_Mebel_TST""",
    longDesc = 
u"""
Taken from entry: W117 <=> W118
""",
)



entry(
    index = 73,
    label = "C8H7O-3 <=> C8H7O-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.725e+10, 's^-1'), n=0.547, Ea=(34.586, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: OH_phenylacetylene_CBSQB3""",
    longDesc = 
u"""
Taken from entry: i20 <=> i21
""",
)

entry(
    index = 74,
    label = "C8H7O-5 <=> C8H7O-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.831e+11, 's^-1'), n=0.359, Ea=(33.014, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: OH_phenylacetylene_CBSQB3""",
    longDesc = 
u"""
Taken from entry: ic2 <=> i21
""",
)



entry(
    index = 75,
    label = "C10H7 <=> C10H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.42e+11, 's^-1'), n=0.258, Ea=(3.797, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2016_Mebel_C6H4C2H_C2H2_High_P""",
    longDesc = 
u"""
Taken from entry: W1 <=> W3_6
""",
)

