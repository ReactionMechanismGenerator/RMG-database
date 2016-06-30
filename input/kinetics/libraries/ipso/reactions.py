#!/usr/bin/env python
# encoding: utf-8

name = "ipso"
shortDesc = u"Homebenzylic rearrangement reactions under combustion conditions"
longDesc = u"""
Calculated at the CBS-QB3 level

Citation:

Wang, Zhang, and Zhang, 
“Kinetics of Homoallylic/Homobenzylic Rearrangement Reactions under Combustion Conditions.”
"""
entry(
    index = 1,
    label = "R2 <=> M2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+07, 's^-1'),
        n = 1.03,
        Ea = (14.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "M2 <=> P2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.25e+12, 's^-1'),
        n = 0.19,
        Ea = (4.10, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "R4 <=> M4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.63e+05, 's^-1'),
        n = 1.23,
        Ea = (17.56, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "M4 <=> P4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.51e+12, 's^-1'),
        n = 0.19,
        Ea = (9.77, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "R6 <=> M6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.37e+03, 's^-1'), n=1.38, Ea=(8.62, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "M6 <=> P6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+13, 's^-1'), n=0.11, Ea=(18.40, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "R2 <=> CH3C8H8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.31e+06, 's^-1'), n=1.17, Ea=(28.33, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "R4 <=> CH3C9H10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.51e+05, 's^-1'), n=1.22, Ea=(12.69, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "R6 <=> CH3C10H12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.75e+03, 's^-1'), n=1.32, Ea=(8.21, 'kcal/mol'), T0=(1, 'K')),
)

