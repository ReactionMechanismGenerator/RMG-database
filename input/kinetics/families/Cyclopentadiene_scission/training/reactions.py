#!/usr/bin/env python
# encoding: utf-8

name = "Cyclopentadiene_scission/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.45e+12, 's^-1'), n=0.194, Ea=(32.274, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: B <=> IX
""",
)

