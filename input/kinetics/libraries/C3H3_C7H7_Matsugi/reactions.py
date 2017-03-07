#!/usr/bin/env python
# encoding: utf-8

name = "C3H3_C7H7_Matsugi"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "C3H3 + C7H7 <=> W1",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.781e+17, 'cm^3/(mol*s)'),
        n = -1.568,
        Ea = (0.4547, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "C3H3 + C7H7 <=> W2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.144e+19, 'cm^3/(mol*s)'),
        n = -2.163,
        Ea = (1.195, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "W1 <=> W4",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(2.214e+09, 's^-1'), n=0.749, Ea=(47.859, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "W4 <=> W1",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(3.213e+11, 's^-1'), n=0.07, Ea=(18.329, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "W2 <=> W3",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(4.484e+11, 's^-1'), n=0.032, Ea=(50.631, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "W3 <=> W2",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(A=(3.626e+11, 's^-1'), n=0.119, Ea=(18.066, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "W4 <=> W8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.208e+11, 's^-1'), n=0.001, Ea=(25.838, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "W8 <=> W10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.949e+11, 's^-1'), n=0.486, Ea=(5.464, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "W10 <=> P5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.431e+15, 's^-1'), n=-0.34, Ea=(77.615, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "W2 <=> W14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.623e+09, 's^-1'), n=0.522, Ea=(43.633, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "W14 <=> W17",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.437e+08, 's^-1'), n=1.045, Ea=(15.153, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "W17 <=> P9 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.081e+15, 's^-1'), n=-0.263, Ea=(86.584, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "W17 <=> P10 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.899e+16, 's^-1'), n=-0.42, Ea=(88.738, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "W14 <=> P9 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.401e+11, 's^-1'), n=0.549, Ea=(19.678, 'kcal/mol'), T0=(1, 'K')),
)

