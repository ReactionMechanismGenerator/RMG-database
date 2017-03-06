#!/usr/bin/env python
# encoding: utf-8

name = "Intra_5_membered_conjugated_C=C_C=C_addition/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""



entry(
    index = 1,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.16177e+12, 's^-1'), n=-0.0456701, Ea=(160.977, 'kJ/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: II <=> A
""",
)

