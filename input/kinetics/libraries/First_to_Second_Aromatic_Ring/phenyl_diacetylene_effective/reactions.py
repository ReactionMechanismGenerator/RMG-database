#!/usr/bin/env python
# encoding: utf-8

name = "phenyl_diacetylene_effective"
shortDesc = u"CBS-QB3"
longDesc = u"""
Effective rate for an adduct of phenyl radical + diacetylene to form either benzofulvenyl or 2-naphthyl radical.
Rate-limiting step is trans-cis isomerization of the adduct, calculated using CBS-QB3+TST.
"""
entry(
    index = 1,
    label = "i2_trans <=> i3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.992e+11, 's^-1'), n=0.670, Ea=(58.336, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "i2_trans <=> i4",
    degeneracy = 1,
    kinetics=Arrhenius(A=(2.992e+11, 's^-1'), n=0.670, Ea=(58.336, 'kcal/mol'), T0=(1, 'K')),
)

