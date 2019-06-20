#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C9H8_2"
shortDesc = u"Indenyl radical recombining with H atom"
longDesc = u"""
Ab Initio G3-type/Statistical Theory Study of the Formation of Indene in Combustion Flames. I. Pathways Involving Benzene and Phenyl Radical
V. V. Kislov and A. M. Mebel
J. Phys. Chem. A 2007, 111, 3922-3931

level of theory:G3(MP2,CC)//B3LYP/6-311G**, TST rates reported in literature and fitted in RMG
"""

entry(
    index = 1,
    label = "C9H7 + H <=> indene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

