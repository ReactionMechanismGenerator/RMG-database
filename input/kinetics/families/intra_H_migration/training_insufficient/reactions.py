#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 18,
    label = "C7H7-7 <=> C7H7-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc =
u"""
Taken from entry: vinylCPDyl <=> product41

This training reaction has very high rates in the backward direction 10^20 1/s for lower temperatures when using thermo data from `vinylCPD_H`. 

This training reaction is duplicate to 
da Silva, G., Cole, J. A., Bozzelli, J. W., Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions, The Journal of Physical Chemistry A, 114 (6), 2275-2283, 2010, which shows decreasing rates for decreasing temperatures.
""",
)

