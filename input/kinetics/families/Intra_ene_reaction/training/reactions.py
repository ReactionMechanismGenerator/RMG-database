#!/usr/bin/env python
# encoding: utf-8

name = "Intra_ene_reaction/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""


entry(
    index = 1,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.39e+07, 's^-1'), n=1.58, Ea=(21.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product21
""",
)

entry(
    index = 2,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.06e+07, 's^-1'), n=1.74, Ea=(24.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product21 <=> product22
""",
)



entry(
    index = 3,
    label = "C9H8 <=> C9H8-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+09, 's^-1'), n=0.96, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt22 <=> INDENE
""",
)



entry(
    index = 4,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.086e+09, 's^-1'), n=1.038, Ea=(39.326, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: II <=> VIII
""",
)



entry(
    index = 5,
    label = "C6H6-3 <=> C6H6-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.697e+08, 's^-1'), n=1.15, Ea=(52.158, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P_reverse""",
    longDesc = 
u"""
Taken from entry: VIII <=> II
""",
)



entry(
    index = 6,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+07, 's^-1'), n=1.54, Ea=(13.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: C5H5CH2-1 <=> C5H5CH2-2
""",
)



entry(
    index = 7,
    label = "C6H7-3 <=> C6H7-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.2767e+08, 's^-1'),
        n = 1.42887,
        Ea = (158.561, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: C5H5CH2-2 <=> C5H5CH2-1
""",
)



entry(
    index = 8,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+08, 's^-1'), n=1.46, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: adducta <=> adductb
""",
)



entry(
    index = 9,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+08, 's^-1'), n=1.64, Ea=(22.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: adductd <=> pdt15
""",
)

entry(
    index = 10,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+08, 's^-1'), n=1.55, Ea=(18.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt16
""",
)

entry(
    index = 11,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+08, 's^-1'), n=1.8, Ea=(21.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt15 <=> pdt39
""",
)



entry(
    index = 12,
    label = "C6H8 <=> C6H8-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.0333e+08, 's^-1'), n=1.2, Ea=(24.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: c-C5H5_CH3_Sharma_TST""",
    longDesc = 
u"""
Taken from entry: C5H5CH3-5 <=> C5H5CH3-1
""",
)

entry(
    index = 13,
    label = "C6H8-3 <=> C6H8-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6539e+07, 's^-1'), n=2.1, Ea=(25.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: c-C5H5_CH3_Sharma_TST""",
    longDesc = 
u"""
Taken from entry: C5H5CH3-1 <=> C5H5CH3-2
""",
)



entry(
    index = 14,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.429e+08, 's^-1'), n=1.267, Ea=(24.384, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H9_Mebel_TST""",
    longDesc = 
u"""
Taken from entry: W8 <=> W102
""",
)

entry(
    index = 15,
    label = "C10H9-5 <=> C10H9-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.548e+09, 's^-1'), n=0.934, Ea=(9.114, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H9_Mebel_TST""",
    longDesc = 
u"""
Taken from entry: W107 <=> W108
""",
)

