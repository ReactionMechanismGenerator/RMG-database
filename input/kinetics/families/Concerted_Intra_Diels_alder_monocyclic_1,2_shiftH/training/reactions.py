#!/usr/bin/env python
# encoding: utf-8

name = "Concerted_Intra_Diels_alder_monocyclic_1,2_shiftH/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.994e+12, 's^-1'), n=0.197, Ea=(51.841, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: VIII <=> IX
""",
)

