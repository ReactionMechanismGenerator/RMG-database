#!/usr/bin/env python
# encoding: utf-8

name = "Intra_Diels_alder_monocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""


entry(
    index = 1,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.587e+11, 's^-1'), n=0.108, Ea=(37.209, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: VIII <=> X
""",
)

entry(
    index = 2,
    label = "C6H6-3 <=> C6H6-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.012e+13, 's^-1'), n=0.1, Ea=(41.203, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: IV <=> B
""",
)

