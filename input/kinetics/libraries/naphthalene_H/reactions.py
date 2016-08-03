#!/usr/bin/env python
# encoding: utf-8

name = "naphthalene_H"
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
    label = "biCPD3ene + H <=> adducta",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63e+09, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "biCPD3ene + H <=> adductb",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.61e+10, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "biCPD3ene + H <=> adductc",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.61e+10, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "adducta <=> adductb",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.46e+08, 's^-1'), n=1.46, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 5,
    label = "adductb <=> adductc",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.46e+06, 's^-1'), n=2.01, Ea=(27.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "adducta <=> prod1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.89e+11, 's^-1'), n=0.12, Ea=(9.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 7,
    label = "prod1 <=> prod2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.73e+11, 's^-1'), n=0.31, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
/ prod1 = prod2 rate limiting, calculated BMK/cbsb7
/prod1 = prod2		        3.51E+11	0.51	21.7 0.0 0.0 0.0
""",
)

entry(
    index = 8,
    label = "prod2 <=> prod5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 's^-1'), n=0.45, Ea=(25.6, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 9,
    label = "prod2 <=> prod3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.14e+11, 's^-1'), n=0.34, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 10,
    label = "prod3 <=> prod4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.79e+11, 's^-1'), n=0.33, Ea=(10.5, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 11,
    label = "prod4 <=> naphthalene + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.34e+08, 's^-1'), n=1.55, Ea=(15.3, 'kcal/mol'), T0=(1, 'K')),
)

entry(
    index = 12,
    label = "prod5 <=> prod4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.42e+11, 's^-1'), n=0.22, Ea=(4.8, 'kcal/mol'), T0=(1, 'K')),
)

