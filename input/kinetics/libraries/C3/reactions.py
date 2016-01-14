#!/usr/bin/env python
# encoding: utf-8

name = ""
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "aC3H5 + C3H4a <=> prod_1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(42, 'cm^3/(mol*s)'), n=3.27, Ea=(11, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "prod_1 <=> prod_2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+09, 's^-1'), n=0.63, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "prod_2 <=> prod_3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.93e+09, 's^-1'), n=1.27, Ea=(31, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "C3H4a + iC4H7 <=> prod_6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18.6, 'cm^3/(mol*s)'), n=3, Ea=(9.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "prod_6 <=> prod_4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+11, 's^-1'), n=0.2, Ea=(27.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "prod_4 <=> prod_5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.37e+08, 's^-1'), n=1.3, Ea=(29.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "C3H4p + aC3H5 <=> prod_7",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (267000, 'cm^3/(mol*s)'),
        n = 2.15,
        Ea = (12.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 8,
    label = "prod_7 <=> prod_8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.53e+07, 's^-1'), n=1.05, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "prod_8 <=> prod_9 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.99e+10, 's^-1'), n=1, Ea=(32.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "C3H4p + iC4H7 <=> prod_10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(121, 'cm^3/(mol*s)'), n=2.9, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "prod_10 <=> prod_11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.6e+10, 's^-1'), n=0.2, Ea=(9.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "prod_11 <=> prod_12 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.77e+09, 's^-1'), n=1.4, Ea=(32, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "C3H4a + BD2YL <=> prod_13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(128, 'cm^3/(mol*s)'), n=3.05, Ea=(7.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "prod_13 <=> prod_14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.21e+11, 's^-1'), n=0.34, Ea=(21.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "prod_14 <=> prod_15 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+10, 's^-1'), n=1.27, Ea=(44.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "C3H4p + BD2YL <=> prod_16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1900, 'cm^3/(mol*s)'), n=2.92, Ea=(8.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "prod_16 <=> prod_17",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.9e+10, 's^-1'), n=0.33, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "prod_17 <=> prod_18 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.47e+10, 's^-1'), n=1.22, Ea=(45.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "aC3H5 + C3H4a <=> prod_19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3960, 'cm^3/(mol*s)'), n=2.65, Ea=(11.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "prod_19 <=> prod_2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.47e+07, 's^-1'), n=0.85, Ea=(10.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "C3H4a + iC4H7 <=> prod_20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(37, 'cm^3/(mol*s)'), n=2.89, Ea=(9.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "prod_20 <=> prod_4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.6e+11, 's^-1'), n=0.27, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "aC3H5 + C2H2 <=> prod_21",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (238000, 'cm^3/(mol*s)'),
        n = 2.26,
        Ea = (12.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 24,
    label = "prod_21 <=> prod_22",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+09, 's^-1'), n=0.62, Ea=(9.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "prod_22 <=> CPD + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.19e+09, 's^-1'), n=1.37, Ea=(31.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "C3H3 + C2H2 <=> prod_23",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.27e+06, 'cm^3/(mol*s)'),
        n = 2.15,
        Ea = (10.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 27,
    label = "prod_23 <=> prod_24",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.88e+10, 's^-1'), n=0.31, Ea=(12.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "prod_24 <=> CPDyl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+10, 's^-1'), n=0.98, Ea=(26.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "C3H3 + C3H4p <=> prod_25",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7040, 'cm^3/(mol*s)'), n=2.87, Ea=(9.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "prod_25 <=> prod_26",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.05e+11, 's^-1'), n=0.12, Ea=(12.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "prod_26 <=> meCPDyl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+10, 's^-1'), n=1.01, Ea=(27.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "C3H3 + C3H4p <=> prod_27",
    degeneracy = 1,
    kinetics = Arrhenius(A=(285, 'cm^3/(mol*s)'), n=2.93, Ea=(11.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "prod_27 <=> prod_28",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.8e+11, 's^-1'), n=0.1, Ea=(11.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 34,
    label = "prod_28 <=> meCPDyl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+10, 's^-1'), n=1.01, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "C3H3 + C3H4a <=> prod_29",
    degeneracy = 1,
    kinetics = Arrhenius(A=(850, 'cm^3/(mol*s)'), n=2.81, Ea=(8.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "prod_29 <=> prod_30",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.47e+11, 's^-1'), n=0.15, Ea=(14, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "prod_30 <=> prod_33",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+09, 's^-1'), n=1.12, Ea=(39.4, 'kcal/mol'), T0=(1, 'K')),
)

