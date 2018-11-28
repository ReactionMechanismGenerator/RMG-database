#!/usr/bin/env python
# encoding: utf-8

name = "Baeyer-Villiger_step2/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""

entry(
    index = 1,
    label = "acetone_peracetic_criegee <=> methyl_acetate + acetic_acid",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.69425e11, 's^-1'), n=0.82328, Ea=(126.358, 'kJ/mol'), T0=(1, 'K')),
    rank = 6,
    shortDesc = u"""CBS-QB3 calculation without HR""",
    longDesc =
u"""
CBS-QB3 calculation without HR fitted over range from 300-600 K with Eckart tunneling
""",
)

entry(
    index = 2,
    label = "cyclohexanone_peracetic_criegee <=> caprolactone + acetic_acid",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.52064e+11, 's^-1'), n=0.572241, Ea=(93.6294, 'kJ/mol'), T0=(1, 'K')),
    rank = 6,
    shortDesc = u"""CBS-QB3 calculation without HR""",
    longDesc =
u"""
CBS-QB3 calculation without HR fitted over range from 300-600 K with Eckart tunneling
""",
)
