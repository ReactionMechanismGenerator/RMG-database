#!/usr/bin/env python
# encoding: utf-8

name = "GRI-HCO"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "HCO + H2O <=> H + CO + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+18, 'cm^3/(mol*s)'), n=-1, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "HCO <=> H + CO",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(
            A = (1.87e+17, 'cm^3/(mol*s)'),
            n = -1,
            Ea = (17000, 'cal/mol'),
            T0 = (1, 'K'),
        ),
        efficiencies = {'C': 2, 'O=C=O': 2, 'CC': 3, 'O': 0, '[H][H]': 2, '[C]=O': 1.5},
    ),
)

