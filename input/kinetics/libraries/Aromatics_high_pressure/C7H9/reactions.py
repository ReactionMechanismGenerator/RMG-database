#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C7H9"
shortDesc = u""
longDesc = u"""
Ab Initio G3-type/Statistical Theory Study of the Formation of Indene in Combustion Flames. I. Pathways Involving Benzene and Phenyl Radical
V. V. Kislov and A. M. Mebel
J. Phys. Chem. A 2007, 111, 3922-3931

level of theory:G3(MP2,CC)//B3LYP/6-311G**, TST rates reported in literature and fitted in RMG
"""
entry(
    index = 1,
    label = "benzene_1 + methyl_7 <=> C7H9_12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2195, 'cm^3/(mol*s)'),
        n = 2.878,
        Ea = (10.912, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "C7H9_12 <=> C7H8_17 + H_15",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.217e+10, 's^-1'), n=0.87, Ea=(25.199, 'kcal/mol'), T0=(1, 'K')),
)


