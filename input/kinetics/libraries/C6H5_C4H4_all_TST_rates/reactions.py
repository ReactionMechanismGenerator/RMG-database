#!/usr/bin/env python
# encoding: utf-8

name = "C6H5_C4H4_all_TST_rates"
shortDesc = u"level of theory: G3(MP2,CC)//B3LYP/6-311G(d,p)"
longDesc = u"""
Kinetics from:
Formation Mechanism of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames
A. M. Mebel*, A. Landera, R. I. Kaiser*
Department of Chemistry and Biochemistry, Florida International UniVersity, Miami, FL 33199
Chemical Science and Engineering Devision, Argonne National Laboratory, Argonne, IL 60439
Department of Chemistry, University of Hawaii at Manoa, Honolulu, HI 96822
"""
entry(
    index = 1,
    label = "W1 <=> W4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(264300, 's^-1'), n=1.839, Ea=(33.509, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "W1 <=> W14",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(7.179e+07, 's^-1'), n=1.101, Ea=(27.148, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "W1 <=> W16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(120000, 's^-1'), n=2.099, Ea=(35.296, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "C6H5 + C4H4 <=> W1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (32420, 'cm^3/(mol*s)'),
        n = 2.179,
        Ea = (-0.282, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "W1 <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.456e+08, 's^-1'), n=1.511, Ea=(40.052, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "W2 <=> W8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.54e+10, 's^-1'), n=0.69, Ea=(20.376, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "W2 <=> W19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.423e+09, 's^-1'), n=0.834, Ea=(24.235, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "C6H5 + C4H4 <=> W2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (392600, 'cm^3/(mol*s)'),
        n = 2.192,
        Ea = (4.297, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "W3 <=> W7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.62e+09, 's^-1'), n=1.05, Ea=(31.179, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "W3 <=> W19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.233e+11, 's^-1'), n=0.39, Ea=(35.846, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "W3 <=> W20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.806e+09, 's^-1'), n=1.172, Ea=(51.258, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "C6H5 + C4H4 <=> W3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (44410, 'cm^3/(mol*s)'),
        n = 2.177,
        Ea = (1.454, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 13,
    label = "W4 <=> W5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.09e+08, 's^-1'), n=0.695, Ea=(6.499, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "W5 <=> W6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.346e+08, 's^-1'), n=1.296, Ea=(39.967, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "W7 <=> W6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.983e+12, 's^-1'), n=-0.321, Ea=(5.655, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "W9 <=> W7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(65110, 's^-1'), n=2.209, Ea=(29.053, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "W17 <=> W7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.323e+10, 's^-1'), n=0.901, Ea=(33.428, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "W8 <=> W9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.078e+13, 's^-1'), n=-0.048, Ea=(6.657, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "W9 <=> W10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.048e+09, 's^-1'), n=0.924, Ea=(30.972, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 20,
    label = "W10 <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.076e+12, 's^-1'), n=0.597, Ea=(36.928, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 21,
    label = "W11 <=> W10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.899e+10, 's^-1'), n=0.97, Ea=(33.321, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 22,
    label = "W10 <=> W13",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.258e+10, 's^-1'), n=0.21, Ea=(7.415, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 23,
    label = "W10 <=> W20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.56e+08, 's^-1'), n=1.408, Ea=(41.295, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 24,
    label = "W14 <=> W15",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.881e+08, 's^-1'), n=1.062, Ea=(16.546, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 25,
    label = "W15 <=> W16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.895e+11, 's^-1'), n=0.516, Ea=(3.785, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 26,
    label = "W16 <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.394e+10, 's^-1'), n=1.133, Ea=(39.957, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 27,
    label = "W7 <=> W20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.658e+09, 's^-1'), n=0.699, Ea=(7.063, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 28,
    label = "W20 <=> P2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+13, 's^-1'), n=0.609, Ea=(49.05, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 29,
    label = "C6H5 + C4H4 <=> W14",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1579, 'cm^3/(mol*s)'),
        n = 2.629,
        Ea = (2.073, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 30,
    label = "P1 + H <=> W6",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.86e+09, 'cm^3/(mol*s)'),
        n = 1.549,
        Ea = (4.523, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 31,
    label = "P1 + H <=> W13",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.781e+08, 'cm^3/(mol*s)'),
        n = 1.663,
        Ea = (10.356, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 32,
    label = "P4 + H <=> W3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.123e+11, 'cm^3/(mol*s)'),
        n = 1.058,
        Ea = (3.961, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 33,
    label = "P4 + H <=> W9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.652e+08, 'cm^3/(mol*s)'),
        n = 1.535,
        Ea = (3.84, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 34,
    label = "P5 + H <=> W3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.278e+08, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (5.344, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 35,
    label = "P5 + H <=> W20",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.138e+09, 'cm^3/(mol*s)'),
        n = 1.597,
        Ea = (4.011, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 36,
    label = "P6 + H <=> W14",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.081e+08, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (6.797, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 37,
    label = "W14 <=> W1",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(7.809e+07, 's^-1'), n=1.057, Ea=(15.061, 'kcal/mol'), T0=(1, 'K')),
)

