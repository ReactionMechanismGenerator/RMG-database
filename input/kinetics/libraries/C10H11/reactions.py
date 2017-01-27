#!/usr/bin/env python
# encoding: utf-8

name = "C10H11"
shortDesc = u"Cyclopentadiene pyrolysis in the presence of ethene"
longDesc = u"""
Calculated at the CBS-QB3 level

Citation:

Aäron G. Vandeputte, Shamel S. Merchant, Marko R. Djokic, Kevin M. Van Geem, 
Guy B. Marin, William H. Green, "Detailed study of cyclopentadiene pyrolysis in the 
presence of ethene: realistic pathways from C5H5 to naphthalene." (2016)
"""
entry(
    index = 1,
    label = "CPD + CPDyl <=> adducte",
    degeneracy = 1,
    kinetics = Arrhenius(A=(288, 'cm^3/(mol*s)'), n=2.8, Ea=(8.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "CPD + CPDyl <=> adductd",
    degeneracy = 1,
    kinetics = Arrhenius(A=(288, 'cm^3/(mol*s)'), n=2.74, Ea=(3.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "adductd <=> pdt7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+11, 's^-1'), n=0.29, Ea=(15.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ts9
""",
)

entry(
    index = 4,
    label = "pdt7 <=> pdt8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.51e+11, 's^-1'), n=0.58, Ea=(29.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "pdt8 <=> pdt9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.39e+10, 's^-1'), n=0.91, Ea=(36.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "pdt9 <=> pdt10bis",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.25e+09, 's^-1'), n=0.76, Ea=(6.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "adducte <=> pdt7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.43e+11, 's^-1'), n=0.21, Ea=(8.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "pdt11 + H <=> pdt10bis",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.09e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (2.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/pdt10bis = pdt11 + H	        2.05E+09	1.47	41.5 0.0 0.0 0.0
""",
)

entry(
    index = 9,
    label = "pdt10bis <=> pdt12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.76e+10, 's^-1'), n=0.78, Ea=(24.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "pdt12 <=> benzene + butadieneyl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.14e+12, 's^-1'), n=0.52, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "pdt13 + H <=> pdt12",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.81e+06, 'cm^3/(mol*s)'),
        n = 1.95,
        Ea = (5.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/pdt12 = pdt13 + H	        1.83E+08	1.53	18.0 0.0 0.0 0.0
""",
)

entry(
    index = 12,
    label = "adductd <=> pdt14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.02e+11, 's^-1'), n=0.85, Ea=(46.1, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ ts18, BMK/cbsb7
/adductd = pdt14	        1.58E+11	0.80	41.8 0.0 0.0 0.0
""",
)

entry(
    index = 13,
    label = "adductd <=> pdt15",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+08, 's^-1'), n=1.64, Ea=(22.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "pdt15 <=> pdt16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.29e+09, 's^-1'), n=1.04, Ea=(31.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ Rate limiting step on BMK, -2 kcal/mol based on CCSD(t)-f12/avdz
""",
)

entry(
    index = 15,
    label = "pdt16 <=> pdt17",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.36e+10, 's^-1'), n=0.44, Ea=(32.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "pdt17 <=> pdt18",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.47e+10, 's^-1'), n=0.79, Ea=(29, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "pdt18 <=> pdt19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.69e+11, 's^-1'), n=0.22, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "pdt14 <=> pdt16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.28e+08, 's^-1'), n=1.55, Ea=(18.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "pdt14 <=> pdt20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.107, 's^-1'), n=3.67, Ea=(29.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "pdt20 <=> pdt21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.9e+10, 's^-1'), n=0.29, Ea=(21.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "pdt22 + CH3 <=> pdt21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2480, 'cm^3/(mol*s)'), n=2.89, Ea=(-0.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/pdt21 = pdt22 + CH3	        3.02E+11	1.22	46.3 0.0 0.0 0.0
""",
)

entry(
    index = 22,
    label = "pdt14 <=> pdt23",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "pdt22 <=> INDENE",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.2e+09, 's^-1'), n=0.96, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "pdt23 <=> pdt9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.27e+10, 's^-1'), n=1.01, Ea=(40.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "pdt23 <=> pdt30 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=1.41, Ea=(38.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ ts31
""",
)

entry(
    index = 26,
    label = "pdt26 + H <=> pdt19",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.09e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (2.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/pdt19 = pdt26 + H	        1.16E+10	1.37	42.1 0.0 0.0 0.0
""",
)

entry(
    index = 27,
    label = "pdt18 <=> pdt25",
    degeneracy = 1,
    kinetics = Arrhenius(A=(250000, 's^-1'), n=1.95, Ea=(24, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "pdt13 + H <=> pdt25",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.58,
        Ea = (1.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/pdt25 = pdt13 + H	        3.13E+09	1.40	51.1 0.0 0.0 0.0
""",
)

entry(
    index = 29,
    label = "pdt31 + H <=> pdt8",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.26e+08, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (1.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/pdt8 = pdt31 + H	        5.25E+08	1.52	40.7 0.0 0.0 0.0
""",
)

entry(
    index = 30,
    label = "pdt17 <=> pdt24",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.48e+11, 's^-1'), n=0.26, Ea=(7.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "pdt24 <=> pdt28",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.43e+12, 's^-1'), n=0.31, Ea=(18.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 32,
    label = "pdt21 <=> pdt27",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.07e+06, 's^-1'), n=2, Ea=(26.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "INDENE + CH3 <=> pdt27",
    degeneracy = 1,
    kinetics = Arrhenius(A=(643, 'cm^3/(mol*s)'), n=2.8, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/pdt27 = INDENE + CH3 	        1.71E+11	0.86	22.7 0.0 0.0 0.0
""",
)

entry(
    index = 34,
    label = "pdt16 <=> pdt20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+08, 's^-1'), n=1.01, Ea=(26.4, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ts41
""",
)

entry(
    index = 35,
    label = "pdt28 <=> pdt29",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+09, 's^-1'), n=1.14, Ea=(22.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "pdt28 <=> pdt23",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.46e+07, 's^-1'), n=1.66, Ea=(31.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "pdt25 <=> pdt32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 's^-1'), n=0.41, Ea=(32.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "pdt32 <=> pdt22 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.72e+10, 's^-1'), n=1.33, Ea=(51.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "pdt16 <=> pdt33",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+07, 's^-1'), n=1.8, Ea=(15.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ts46
""",
)

entry(
    index = 40,
    label = "pdt33 <=> pdt20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.27e+06, 's^-1'), n=1.5, Ea=(33.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ts47
""",
)

entry(
    index = 41,
    label = "pdt33 <=> pdt29",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.16e+10, 's^-1'), n=0.2, Ea=(24.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ts48
""",
)

entry(
    index = 42,
    label = "pdt31 + H <=> pdt29",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/ Estimates for ts49 to ts51 are within 50%
/ts49
""",
)

entry(
    index = 43,
    label = "pdt30 + H <=> pdt29",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/ts50
""",
)

entry(
    index = 44,
    label = "pdt35 + H <=> pdt29",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.93e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/ts51
""",
)

entry(
    index = 45,
    label = "pdt10bis <=> pdt37",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.83e+08, 's^-1'), n=1.45, Ea=(31.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ ts52
""",
)

entry(
    index = 46,
    label = "pdt38 + H <=> pdt37",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.61e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (4.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    longDesc = 
u"""
/pdt37 = pdt38 + H             2.11E+09        1.35    27.3 0.0 0.0 0.0
""",
)

entry(
    index = 47,
    label = "pdt15 <=> pdt39",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+08, 's^-1'), n=1.8, Ea=(21.8, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ ts54
""",
)

entry(
    index = 48,
    label = "pdt39 <=> pdt33",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.38e+09, 's^-1'), n=1.08, Ea=(42.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ts55, BMK/cbsb7
/pdt39 = pdt33                 1.58E+11        0.8     41.8 0.0 0.0 0.0
""",
)

entry(
    index = 49,
    label = "pdt14 <=> pdt57",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.51e+11, 's^-1'), n=0.28, Ea=(12.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ts85 & ts86
""",
)

entry(
    index = 50,
    label = "pdt57 <=> pdt12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.75e+11, 's^-1'), n=0.44, Ea=(18.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "adductd <=> pdt55",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.36e+06, 's^-1'), n=1.7, Ea=(31.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ts82, 83, 84, 87
""",
)

entry(
    index = 52,
    label = "pdt15 <=> pdt55",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+06, 's^-1'), n=1.75, Ea=(25.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "pdt55 <=> pdt58",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.02e+11, 's^-1'), n=0.79, Ea=(35.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "pdt58 <=> pdt20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+07, 's^-1'), n=1.61, Ea=(27.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 55,
    label = "INDENYL <=> INDENYL_ADD",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e-11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/Block indenyl to odd products
""",
)

entry(
    index = 56,
    label = "INDENYL <=> INDENYL_ADD2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e-11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "INDENYL <=> INDENYL_ADD3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e-11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "INDENYL <=> INDENYL_ADD4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e-11, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

