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
    label = "benzene(1) + methyl(7) <=> C7H9(12)",
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
    label = "benzene(1) + methyl(7) <=> phenyl(16) + CH4(26)",
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
    label = "C7H9(12) <=> C7H8(17) + H(15)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.217e+10, 's^-1'), n=0.87, Ea=(25.199, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "C7H8(17) + H(15) <=> C7H7(10) + H2(23)",
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
    label = "C7H8(17) + H(15) <=> C7H7(11) + H2(23)",
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
    label = "C7H7(11) <=> C7H7(10)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.712e+10, 's^-1'), n=0.722, Ea=(41.878, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "C7H7(10) + ethyne(8) <=> C9H9(13)",
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
    label = "C9H9(13) <=> C9H9(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.257e+11, 's^-1'), n=0.139, Ea=(13.233, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "C9H9(14) <=> indene(25) + H(15)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.597e+10, 's^-1'), n=0.889, Ea=(20.893, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "benzene(1) + C3H3(9) <=> C9H9(2)",
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
    label = "benzene(1) + C3H3(9) <=> C9H9(6)",
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
    label = "C9H9(2) <=> C9H9(3)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.485e+11, 's^-1'), n=0.065, Ea=(27.941, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "C9H9(6) <=> C9H9(3)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.565e+11, 's^-1'), n=0.009, Ea=(28.521, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "C9H9(3) <=> C9H9(24)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.527e+10, 's^-1'), n=0.853, Ea=(47.848, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "C9H9(24) <=> C9H9(14)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.438e+10, 's^-1'), n=0.625, Ea=(38.324, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "C9H9(3) <=> C9H9(4)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.231e+11, 's^-1'), n=0.765, Ea=(55.941, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "C9H9(4) <=> C9H9(5)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.677e+10, 's^-1'), n=0.839, Ea=(43.638, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "C9H9(5) <=> indene(25) + H(15)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.591e+10, 's^-1'), n=0.886, Ea=(24.975, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "C9H8(20) + H(15) <=> C9H7(18) + H2(23)",
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
    label = "C9H7(18) <=> C9H7(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.534e+11, 's^-1'), n=0.102, Ea=(13.049, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "C9H8(21) + H(15) <=> C9H7(22) + H2(23)",
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
    label = "C9H7(22) <=> C9H7(19)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.431e+11, 's^-1'), n=0.114, Ea=(15.579, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "phenyl(16) + C3H3(9) <=> C9H8(20)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "phenyl(16) + C3H3(9) <=> C9H8(21)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "C9H7(19) + H(15) <=> indene(25)",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

