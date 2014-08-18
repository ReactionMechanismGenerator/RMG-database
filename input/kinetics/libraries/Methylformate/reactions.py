#!/usr/bin/env python
# encoding: utf-8

name = "Methylformate"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "Mfmt <=> CO + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.128e+12, 's^-1'), n=0.735, Ea=(68.628, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 2,
    label = "Mfmt <=> CH2O + CH2O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.158e+09, 's^-1'), n=1.28, Ea=(75.979, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "Mfmt <=> CO2 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.536e+11, 's^-1'), n=0.832, Ea=(83.612, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 4,
    label = "Mofml <=> CO2 + CH3j",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.3e+09, 's^-1'), n=1.09, Ea=(14.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "CO + CH3Oj <=> Mofml",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.97e+09, 'cm^3/(mol*s)'),
        n = 1.27,
        Ea = (5.81, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 6,
    label = "HCjO + CH2O <=> Fmoml",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5030, 'cm^3/(mol*s)'), n=2.48, Ea=(9.32, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "Hj + Mfmt <=> H2 + Mofml",
    degeneracy = 1,
    kinetics = Arrhenius(A=(228000, 'cm^3/(mol*s)'), n=2.5, Ea=(6.56, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "Hj + Mfmt <=> H2 + Fmoml",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (116000, 'cm^3/(mol*s)'),
        n = 2.55,
        Ea = (7.62, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 9,
    label = "CH3j + Mfmt <=> CH4 + Mofml",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.34, 'cm^3/(mol*s)'), n=2.82, Ea=(6.81, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "CH3j + Mfmt <=> CH4 + Fmoml",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.257, 'cm^3/(mol*s)'), n=3.96, Ea=(8.02, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "CH3Oj + HCjO <=> Mfmt",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "CH3j + OjCHO <=> Mfmt",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
)

