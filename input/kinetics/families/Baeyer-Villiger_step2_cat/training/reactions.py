#!/usr/bin/env python
# encoding: utf-8

name = "Baeyer-Villiger_step2_cat/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "acetone_methyl_criegee + acetic_acid1 <=> methyl_acetate + methanol + acetic_acid2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.40212, 'cm^3/(mol*s)'), n=3.34273, Ea=(99.7987, 'kJ/mol'), T0=(1, 'K')),
    rank = 6,
    shortDesc = u"""CBS-QB3 calculation without HR""",
    longDesc =
u"""
CBS-QB3 calculation without HR fitted over range from 300-600 K with Eckart tunneling
""",
)

entry(
    index = 2,
    label = "cyclohexanone_methyl_criegee + acetic_acid1 <=> caprolactone + methanol + acetic_acid2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.00474858, 'cm^3/(mol*s)'), n=4.24247, Ea=(83.3223, 'kJ/mol'), T0=(1, 'K')),
    rank = 6,
    shortDesc = u"""CBS-QB3 calculation without HR""",
    longDesc =
u"""
CBS-QB3 calculation without HR fitted over range from 300-600 K with Eckart tunneling
""",
)
