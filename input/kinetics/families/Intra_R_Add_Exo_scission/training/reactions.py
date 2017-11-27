#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exo_scission/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""



entry(
    index = 1,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(7.179e+07, 's^-1'), n=1.101, Ea=(27.148, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W1 <=> W14
""",
)

entry(
    index = 2,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(7.809e+07, 's^-1'), n=1.057, Ea=(15.061, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C6H5_C4H4_all_TST_rates""",
    longDesc = 
u"""
Taken from entry: W14 <=> W1
""",
)

