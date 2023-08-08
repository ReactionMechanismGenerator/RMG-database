#!/usr/bin/env python
# encoding: utf-8

name = "Aromatics_high_pressure/C9H9_2"
shortDesc = u"Benzyl radical+Acetylene and Benzene+Propargyl radical"
longDesc = u"""
Ab Initio G3-type/Statistical Theory Study of the Formation of Indene in Combustion Flames. I. Pathways Involving Benzene and Phenyl Radical
V. V. Kislov and A. M. Mebel
J. Phys. Chem. A 2007, 111, 3922-3931

level of theory:G3(MP2,CC)//B3LYP/6-311G**, TST rates reported in literature and fitted in RMG
"""
entry(
    index = 7,
    label = "C7H7_10 + ethyne_8 <=> C9H9_13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (31630, 'cm^3/(mol*s)'),
        n = 2.479,
        Ea = (11.061, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "C9H9_13 <=> C9H9_14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.257e+11, 's^-1'), n=0.139, Ea=(13.233, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "C9H9_14 <=> indene_25 + H_15",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.597e+10, 's^-1'), n=0.889, Ea=(20.893, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "benzene_1 + C3H3_9 <=> C9H9_2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (144.6, 'cm^3/(mol*s)'),
        n = 2.951,
        Ea = (14.055, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 11,
    label = "benzene_1 + C3H3_9 <=> C9H9_6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (312.3, 'cm^3/(mol*s)'),
        n = 2.973,
        Ea = (16.396, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 12,
    label = "C9H9_2 <=> C9H9_3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.485e+11, 's^-1'), n=0.065, Ea=(27.941, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "C9H9_6 <=> C9H9_3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.565e+11, 's^-1'), n=0.009, Ea=(28.521, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "C9H9_3 <=> C9H9_24",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.527e+10, 's^-1'), n=0.853, Ea=(47.848, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "C9H9_24 <=> C9H9_14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.438e+10, 's^-1'), n=0.625, Ea=(38.324, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "C9H9_3 <=> C9H9_4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.231e+11, 's^-1'), n=0.765, Ea=(55.941, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "C9H9_4 <=> C9H9_5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.677e+10, 's^-1'), n=0.839, Ea=(43.638, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "C9H9_5 <=> indene_25 + H_15",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.591e+10, 's^-1'), n=0.886, Ea=(24.975, 'kcal/mol'), T0=(1, 'K')),
)


