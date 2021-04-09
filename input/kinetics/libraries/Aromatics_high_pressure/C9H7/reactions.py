#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C9H7"
shortDesc = u"C9H7 isomerization"
longDesc = u"""
Ab Initio G3-type/Statistical Theory Study of the Formation of Indene in Combustion Flames. I. Pathways Involving Benzene and Phenyl Radical
V. V. Kislov and A. M. Mebel
J. Phys. Chem. A 2007, 111, 3922-3931

level of theory:G3(MP2,CC)//B3LYP/6-311G**, TST rates reported in literature and fitted in RMG
"""

entry(
    index = 1,
    label = "C9H7_18 <=> C9H7_19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.534e+11, 's^-1'), n=0.102, Ea=(13.049, 'kcal/mol'), T0=(1, 'K')),
)


entry(
    index = 2,
    label = "C9H7_22 <=> C9H7_19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.431e+11, 's^-1'), n=0.114, Ea=(15.579, 'kcal/mol'), T0=(1, 'K')),
)

