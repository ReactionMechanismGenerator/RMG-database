#!/usr/bin/env python
# encoding: utf-8

name = "vinylCPD_H"
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
    label = "vinylCPD + H <=> addA",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.36e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "vinylCPD + H <=> addB",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (2.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "vinylCPD + H <=> addC",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+09, 'cm^3/(mol*s)'),
        n = 1.48,
        Ea = (0.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "vinylCPD + H <=> addD",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.41e+08, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (1.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "addA <=> addB",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.97e+06, 's^-1'), n=1.8, Ea=(37.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "addC <=> addD",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.81e+07, 's^-1'), n=1.72, Ea=(44.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "addB <=> product7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.37e+06, 's^-1'), n=1.6, Ea=(25.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "addA <=> product7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.88e+09, 's^-1'), n=1, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "addD <=> product10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+08, 's^-1'), n=1.39, Ea=(24.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "product4 <=> product9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.11e+09, 's^-1'), n=1.34, Ea=(47.7, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ htrans6 too strained 0 rate
/ htrans7 too strained 0 rate
""",
)

entry(
    index = 11,
    label = "addA <=> product1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.69e+11, 's^-1'), n=0.24, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ ts1 to ts20
""",
)

entry(
    index = 12,
    label = "product1 <=> product2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.21e+11, 's^-1'), n=0.46, Ea=(16.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "addB <=> product3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.52e+11, 's^-1'), n=0.16, Ea=(10, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "product3 <=> product4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.56e+11, 's^-1'), n=0.55, Ea=(26.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "addB <=> CPDyl + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.87e+11, 's^-1'), n=0.68, Ea=(13.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "addC <=> product16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.77e+10, 's^-1'), n=0.87, Ea=(35, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "product16 <=> product5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.95e+10, 's^-1'), n=0.53, Ea=(31.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "addC <=> product6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.17e+10, 's^-1'), n=0.34, Ea=(31.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "product6 <=> product5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.37e+11, 's^-1'), n=0.73, Ea=(25.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "product7 <=> FULVENE + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+11, 's^-1'), n=1.15, Ea=(39.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "addD <=> CPD + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 's^-1'), n=0.81, Ea=(33.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "product2 <=> BENZENE + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.07e+11, 's^-1'), n=0.83, Ea=(22.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "product2 <=> TOLUENE + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.03e+09, 's^-1'), n=1.36, Ea=(26.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "product2 <=> product5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.03e+06, 's^-1'), n=1.96, Ea=(50.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "product5 <=> product13 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+09, 's^-1'), n=1.23, Ea=(28.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "addD <=> product8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+10, 's^-1'), n=0.51, Ea=(30.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "product8 <=> product9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+11, 's^-1'), n=0.59, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "product10 <=> product11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.56e+10, 's^-1'), n=1.17, Ea=(48.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "product11 <=> product12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+11, 's^-1'), n=0.26, Ea=(22.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 30,
    label = "product12 <=> product14 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 31,
    label = "product4 <=> product16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.03e+10, 's^-1'), n=1.1, Ea=(37, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ prod4 bscis CC & CH
""",
)

entry(
    index = 32,
    label = "product4 <=> product15 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.58e+10, 's^-1'), n=1.38, Ea=(48.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 33,
    label = "addC <=> CPD + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+12, 's^-1'), n=0.87, Ea=(45, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ ts21 to ts45
""",
)

entry(
    index = 34,
    label = "addB <=> product17",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.98e+11, 's^-1'), n=0.06, Ea=(19.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 35,
    label = "product17 <=> product6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(367000, 's^-1'), n=2.24, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 36,
    label = "product7 <=> product18",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.53e+06, 's^-1'), n=1.73, Ea=(58.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 37,
    label = "FULVENE + CH3 <=> product18",
    degeneracy = 1,
    kinetics = Arrhenius(A=(263, 'cm^3/(mol*s)'), n=2.89, Ea=(6.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 38,
    label = "product18 <=> product19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.29e+12, 's^-1'), n=0.15, Ea=(2.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 39,
    label = "product19 <=> product20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.58e+12, 's^-1'), n=0.31, Ea=(16, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 40,
    label = "addB <=> product21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.39e+07, 's^-1'), n=1.58, Ea=(21.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 41,
    label = "product21 <=> product23",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+11, 's^-1'), n=0.2, Ea=(46.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 42,
    label = "product20 <=> TOLUENE + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+10, 's^-1'), n=1.26, Ea=(28.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 43,
    label = "product23 <=> product24",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.18e+11, 's^-1'), n=0.82, Ea=(22.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 44,
    label = "product24 <=> product13 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 45,
    label = "product21 <=> product22",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.06e+07, 's^-1'), n=1.74, Ea=(24.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 46,
    label = "product22 <=> product25",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.39e+11, 's^-1'), n=0.26, Ea=(26.1, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 47,
    label = "product25 <=> product26",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.95e+10, 's^-1'), n=1.05, Ea=(39.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 48,
    label = "product26 <=> product11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.81e+10, 's^-1'), n=0.91, Ea=(32, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 49,
    label = "product22 <=> product29",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.11e+10, 's^-1'), n=0.18, Ea=(66.6, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ same as product 11 = product 12
/product27 = product28			1.39E+11	0.30	24.0  0.0 0.0 0.0
/ same as product 12 = product14 + H
/product28 = product14 + H		3.03E+10	1.22	40.9  0.0 0.0 0.0
""",
)

entry(
    index = 50,
    label = "product29 <=> product23",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+10, 's^-1'), n=0.87, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 51,
    label = "FULVENE + CH3 <=> product32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2790, 'cm^3/(mol*s)'), n=2.91, Ea=(1.3, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ rev of product 23 = product24
/product30 = product24			1.19E+11	0.82	22.4  0.0 0.0 0.0
""",
)

entry(
    index = 52,
    label = "FULVENE + CH3 <=> product31",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2470, 'cm^3/(mol*s)'), n=2.88, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 53,
    label = "product31 <=> product32",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.59e+09, 's^-1'), n=0.99, Ea=(43.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 54,
    label = "product33 <=> product34",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.56e+13, 's^-1'), n=0, Ea=(43.5, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ no ts for ts45
/ ts46 to ts61
""",
)

entry(
    index = 55,
    label = "product31 <=> product35",
    degeneracy = 1,
    kinetics = Arrhenius(A=(285000, 's^-1'), n=2.15, Ea=(43.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 56,
    label = "product35 <=> product36",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.51e+10, 's^-1'), n=0.25, Ea=(4.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 57,
    label = "product36 <=> product37",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.4e+12, 's^-1'), n=0.39, Ea=(16, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 58,
    label = "product32 <=> product38",
    degeneracy = 1,
    kinetics = Arrhenius(A=(671000, 's^-1'), n=2.07, Ea=(48.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 59,
    label = "product38 <=> product39",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.32e+10, 's^-1'), n=0.35, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 60,
    label = "product39 <=> product37",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.95e+12, 's^-1'), n=0.12, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 61,
    label = "product37 <=> product13 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.03e+10, 's^-1'), n=1.22, Ea=(40.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ ts 53 currently estimated
""",
)

entry(
    index = 62,
    label = "product34 <=> product46",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+08, 's^-1'), n=1.52, Ea=(38.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 63,
    label = "CPDyl + ethyne <=> product44",
    degeneracy = 1,
    kinetics = Arrhenius(A=(25500, 'cm^3/(mol*s)'), n=2.27, Ea=(10.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 64,
    label = "product44 <=> vinylCPDyl",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 65,
    label = "product44 <=> product45",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.32e+11, 's^-1'), n=0.3, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 66,
    label = "product45 <=> product33",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.84e+11, 's^-1'), n=0.66, Ea=(23.8, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 67,
    label = "product46 <=> BENZYL",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.85e+11, 's^-1'), n=0.49, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 68,
    label = "product44 <=> product41",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ Estimate for H shift
""",
)

entry(
    index = 69,
    label = "vinylCPDyl <=> product41",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 70,
    label = "product45 <=> product56",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.72e+08, 's^-1'), n=0.21, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ Closing down 1,3 addition /1E4 of RMG estimate
""",
)

entry(
    index = 71,
    label = "product34 <=> product57",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.72e+08, 's^-1'), n=0.21, Ea=(17, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 72,
    label = "FA + H <=> vinylCPDyl",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+09, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 73,
    label = "ethyl + CPDyl <=> ethylCPD",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

