#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/DTBS"
shortDesc = u"Di-tert-butyl Sulfide Seed Mechanism"
longDesc = u"""
Sulfur library originally created by Caleb Class in RMG-Java.
Source of kinetics is unclear, although most likely from his quantum calculations.
"""
entry(
    index = 1,
    label = "S2 <=> S2JJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+10, 's^-1'), n=1, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "C4H8JSH <=> C4H9SJ",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3760, 's^-1'), n=2.4, Ea=(12.28, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "HSJ + HSJ <=> HSSH",
    degeneracy = 1,
    kinetics = ThirdBody(
        arrheniusLow = Arrhenius(A=(8.7e+18, 'cm^6/(mol^2*s)'), n=-0.76, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
        efficiencies = {},
    ),
)

