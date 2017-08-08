#!/usr/bin/env python
# encoding: utf-8

name = "Intra_RH_Add_Endocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""


entry(
    index = 1,
    label = "C5H8O <=> C5H8O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.2e+18, '1/s'),
        n = -1.04,
        Ea = (524.7, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: ZarasCyclopentanone""",
    longDesc = 
u"""
Taken from entry: CPO <=> CPO-enechain
""",
)

