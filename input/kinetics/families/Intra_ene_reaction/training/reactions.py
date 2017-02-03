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

