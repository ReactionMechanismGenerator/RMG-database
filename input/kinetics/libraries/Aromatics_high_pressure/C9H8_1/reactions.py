#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C9H8_1"
shortDesc = u"Phenyl radical recombining with propargyl radical"
longDesc = u"""
Ab Initio G3-type/Statistical Theory Study of the Formation of Indene in Combustion Flames. I. Pathways Involving Benzene and Phenyl Radical
V. V. Kislov and A. M. Mebel
J. Phys. Chem. A 2007, 111, 3922-3931

level of theory:G3(MP2,CC)//B3LYP/6-311G**, TST rates reported in literature and fitted in RMG
"""

entry(
    index = 1,
    label = "phenyl + C3H3 <=> C9H8_1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "phenyl + C3H3 <=> C9H8_2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

