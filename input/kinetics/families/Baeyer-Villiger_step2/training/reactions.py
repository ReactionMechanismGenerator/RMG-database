#!/usr/bin/env python
# encoding: utf-8

name = "Baeyer-Villiger_step2/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
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
