#!/usr/bin/env python
# encoding: utf-8

name = "kislovB"
shortDesc = u"level of theory:Ab initio G3(MP2,CC)//B3LYP"
longDesc = u"""
Kinetics from:
Ab Initio G3-type/Statistical Theory Study of the Formation of Indene in Combustion
Flames. I. Pathways Involving Benzene and Phenyl Radical
V. V. Kislov and A. M. Mebel*
Department of Chemistry and Biochemistry, Florida International UniVersity, Miami, Florida 33199
Received: October 30, 2006; In Final Form: December 19, 2006
J. Phys. Chem. A 2007, 111, 3922-3931
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
    label = "benzene_1 + methyl_7 <=> phenyl_16 + CH4_26",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5151, 'cm^3/(mol*s)'),
        n = 2.896,
        Ea = (15.308, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "C7H9_12 <=> C7H8_17 + H_15",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.217e+10, 's^-1'), n=0.87, Ea=(25.199, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "C7H8_17 + H_15 <=> C7H7_10 + H2_23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.152e+06, 'cm^3/(mol*s)'),
        n = 1.985,
        Ea = (6.175, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "C7H8_17 + H_15 <=> C7H7_11 + H2_23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.738e+07, 'cm^3/(mol*s)'),
        n = 1.889,
        Ea = (15.461, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "C7H7_11 <=> C7H7_10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.712e+10, 's^-1'), n=0.722, Ea=(41.878, 'kcal/mol'), T0=(1, 'K')),
)

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

entry(
    index = 19,
    label = "C9H8_20 + H_15 <=> C9H7_18 + H2_23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.54e+07, 'cm^3/(mol*s)'),
        n = 1.901,
        Ea = (15.418, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 20,
    label = "C9H7_18 <=> C9H7_19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.534e+11, 's^-1'), n=0.102, Ea=(13.049, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "C9H8_21 + H_15 <=> C9H7_22 + H2_23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.725e+07, 'cm^3/(mol*s)'),
        n = 1.892,
        Ea = (16.619, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 22,
    label = "C9H7_22 <=> C9H7_19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.431e+11, 's^-1'), n=0.114, Ea=(15.579, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "phenyl_16 + C3H3_9 <=> C9H8_20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "phenyl_16 + C3H3_9 <=> C9H8_21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "C9H7_19 + H_15 <=> indene_25",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

