#!/usr/bin/env python
# encoding: utf-8

name = "Sulfur/TP_Song"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "thiophene <=> IM1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(920000, 's^-1'), n=0.52, Ea=(67.07, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "thiophene <=> IM2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(367000, 's^-1'), n=0.55, Ea=(74.79, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "thiophene <=> IM4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(184000, 's^-1'), n=0.65, Ea=(86.88, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
thiophene = IM3        2.35E05    0.75    86.11    0.0    0.0    0.0
""",
)

entry(
    index = 4,
    label = "IM1 <=> C2H2 + H2CCS",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.1e+11, 's^-1'), n=0.99, Ea=(41.95, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "IM1 <=> IM5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.45e+11, 's^-1'), n=0.34, Ea=(27.75, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "IM5 <=> IM4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.13e+13, 's^-1'), n=0.86, Ea=(22.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "IM2 <=> IM6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.73e+17, 's^-1'), n=0.58, Ea=(61.23, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
IM2 = IM2a            3.15E12    -0.03    6.03    0.0    0.0    0.0
""",
)

entry(
    index = 8,
    label = "IM6 <=> CS + propyne",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.22e+12, 's^-1'), n=0.37, Ea=(14.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "IM2 <=> IM7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.79e+10, 's^-1'), n=0.64, Ea=(71.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "IM7 <=> CS + propadiene",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.27e+13, 's^-1'), n=0.22, Ea=(8.83, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "IM10 <=> IM11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.9e+12, 's^-1'), n=0.29, Ea=(15.56, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
IM3 = IM8a            3.46E19    0.59    13.39    0.0    0.0    0.0
IM8 = IM8a            2.34E12    -0.09    3.68    0.0    0.0    0.0
IM8a = IM9            5.40E16    1.27    83.03    0.0    0.0    0.0
Below reaction not found with CBS-QB3, guessed (Ea from paper)
IM9 = H2S + butadiyne    1.00E10    0.10    11.63    0.0    0.0    0.0
IM3 = IM10            1.00E12    0.23    13.53    0.0    0.0    0.0
""",
)

entry(
    index = 12,
    label = "IM11 <=> C2H2jj + H2CCS",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.63e+10, 's^-1'), n=0.98, Ea=(88.84, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "IM4 <=> IM8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.58e+11, 's^-1'), n=0.68, Ea=(45.27, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
IM4 = IM4a            1.24E12    0.02    2.07    0.0    0.0    0.0
""",
)

