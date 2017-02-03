#!/usr/bin/env python
# encoding: utf-8

name = "Fulvene_H"
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
    label = "FULVENE + H <=> C5H4CH3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.69e+09, 'cm^3/(mol*s)'),
        n = 1.46,
        Ea = (-0.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "FULVENE + H <=> C5H5CH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.31e+08, 'cm^3/(mol*s)'), n=1.76, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 3,
    label = "FULVENE + H <=> C5H5CH2-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.26e+09, 'cm^3/(mol*s)'),
        n = 1.48,
        Ea = (0.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "FULVENE + H <=> C5H5CH2-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.52e+09, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "C5H4CH3 <=> C5H5CH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00218, 's^-1'), n=4.91, Ea=(40.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "C5H5CH2-1 <=> C5H5CH2-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.23e+07, 's^-1'), n=1.54, Ea=(13.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "C5H5CH2-3 <=> C5H5CH2-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9220, 's^-1'), n=2.81, Ea=(30.2, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 8,
    label = "C5H5CH2-1 <=> biring1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.18e+11, 's^-1'), n=0.17, Ea=(4.4, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "biring1 <=> cyC6H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.51e+11, 's^-1'), n=0.41, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "cyC6H7 <=> benzene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.84e+09, 's^-1'), n=1.3, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
)