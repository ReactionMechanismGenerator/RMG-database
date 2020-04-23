#!/usr/bin/env python
# encoding: utf-8

name = "CJ-frag"
shortDesc = u""
longDesc = u""""""

entry(
    index = 1,
    label = "s18 + HO2 <=> s18-rad1 + H2O2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.07227e-07, 'cm^3/(mol*s)'), n=5.51849, Ea=(15.8562, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
)

entry(
    index = 2,
    label = "s18 + HO2 <=> s18-rad2 + H2O2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(3.90798e-39, 'cm^3/(mol*s)'), n=15.3474, Ea=(6.51402, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
)

entry(
    index = 3,
    label = "s13 + HO2 <=> s13-rad1 + H2O2",
    degeneracy = 3,
    kinetics = Arrhenius(A=(4.71793e-12, 'cm^3/(mol*s)'), n=6.72494, Ea=(60.2257, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
)

entry(
    index = 4,
    label = "s13 + HO2 <=> s13-rad2 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.98982e-15, 'cm^3/(mol*s)'), n=8.10231, Ea=(11.9227, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
)

entry(
    index = 5,
    label = "s13 + HO2 <=> s13-rad3 + H2O2",
    degeneracy = 2,
    kinetics = Arrhenius(A=(1.90173e-38, 'cm^3/(mol*s)'), n=15.5664, Ea=(4.28132, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
)

entry(
    index = 6,
    label = "s13 + HO2 <=> s13-rad4 + H2O2",
    degeneracy = 3,
    kinetics = Arrhenius(A=(1.92115e-13, 'cm^3/(mol*s)'), n=7.39711, Ea=(56.9552, 'kJ/mol'), T0=(1, 'K')),
    shortDesc = u"""""",
)