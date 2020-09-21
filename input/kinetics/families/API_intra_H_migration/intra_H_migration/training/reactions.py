#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C2H3O3 <=> C2H3O3-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.3e+09, 's^-1', '*|/', 2.51189),
        n = 0.75,
        Ea = (23.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['J. W. Allen', 'C. F. Goldsmith', 'W. H. Green'],
        title = 'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '14',
        pages = '1131-1155',
        year = '2012',
    ),
    referenceType = "theory",
    rank = 10,
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
DOI: 10.1039/C1CP22765C
""",
)

entry(
    index = 1,
    label = "S1C4 <=> S1C4b",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.775e+09, 's^-1', '*|/', 3),
        n = 0.686,
        Ea = (6.774, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['E. E. Dames', 'W. H. Green'],
        title = 'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = 'Intl. J. Chem. Kin.',
        volume = '48(9)',
        pages = '544-555',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 10,
    shortDesc = u"""TST calculations at M08SO/MG3S level""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S level
using Qchem. High-pressure-limit rate coefficient computed
using Cantherm with 1D hindered rotor treatment.
DOI: 10.1002/kin.21015
""",
)

entry(
    index = 2,
    label = "S2C4 <=> S2C4b",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (15400, 's^-1', '*|/', 3),
        n = 2.338,
        Ea = (7.127, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ['E. E. Dames', 'W. H. Green'],
        title = 'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = 'Intl. J. Chem. Kin.',
        volume = '48(9)',
        pages = '544-555',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 10,
    shortDesc = u"""TST calculations at M08SO/MG3S level""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S level
using Qchem. High-pressure-limit rate coefficient computed
using Cantherm with 1D hindered rotor treatment.
DOI: 10.1002/kin.21015
""",
)

entry(
    index = 3,
    label = "C4H7O2 <=> C4H7O2b",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (63.58, 's^-1', '*|/', 3.66),
        n = 2.81162,
        Ea = (8.231, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
    ),
    referenceType = "theory",
    rank = 10,
    shortDesc = u"""TST calculations at M08SO/MG3S level by edames""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S* level using Qchem. High-pressure-limit rate coefficient computed using Cantherm with 1D hindered rotor treatment for all relevant rotors. (*A computational grid with 75 radial points and 434 angular points per radial point was used in the calculations for all species)
""",
)

entry(
    index = 4,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.97e+06, 's^-1'), n=1.8, Ea=(37.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addA <=> addB
""",
)

entry(
    index = 5,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.81e+07, 's^-1'), n=1.72, Ea=(44.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addC <=> addD
""",
)

entry(
    index = 6,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.37e+06, 's^-1'), n=1.6, Ea=(25.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product7
""",
)

entry(
    index = 7,
    label = "C7H9-7 <=> C7H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.88e+09, 's^-1'), n=1, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addA <=> product7
""",
)

entry(
    index = 8,
    label = "C7H9-9 <=> C7H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.36e+08, 's^-1'), n=1.39, Ea=(24.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addD <=> product10
""",
)

entry(
    index = 9,
    label = "C7H9-11 <=> C7H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.11e+09, 's^-1'), n=1.34, Ea=(47.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product4 <=> product9
""",
)

entry(
    index = 10,
    label = "C7H9-13 <=> C7H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.03e+06, 's^-1'), n=1.96, Ea=(50.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product2 <=> product5
""",
)

entry(
    index = 11,
    label = "C7H9-15 <=> C7H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(367000, 's^-1'), n=2.24, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product17 <=> product6
""",
)

entry(
    index = 12,
    label = "C7H9-17 <=> C7H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.9e+10, 's^-1'), n=0.87, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product29 <=> product23
""",
)

entry(
    index = 13,
    label = "C7H9-19 <=> C7H9-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(285000, 's^-1'), n=2.15, Ea=(43.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product31 <=> product35
""",
)

entry(
    index = 14,
    label = "C7H9-21 <=> C7H9-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(671000, 's^-1'), n=2.07, Ea=(48.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product32 <=> product38
""",
)

entry(
    index = 15,
    label = "C7H7 <=> C7H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.41e+08, 's^-1'), n=1.52, Ea=(38.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product34 <=> product46
""",
)

entry(
    index = 16,
    label = "C7H7-3 <=> C7H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product44 <=> vinylCPDyl
""",
)

entry(
    index = 17,
    label = "C7H7-5 <=> C7H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product44 <=> product41
""",
)

entry(
    index = 18,
    label = "C7H7-7 <=> C7H7-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: vinylCPDyl <=> product41
""",
)

entry(
    index = 19,
    label = "C5H5 <=> C5H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.15e+10, 's^-1'), n=0.98, Ea=(26.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_24 <=> CPDyl
""",
)

entry(
    index = 20,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.71e+10, 's^-1'), n=1.01, Ea=(27.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_26 <=> meCPDyl
""",
)

entry(
    index = 21,
    label = "C6H7-3 <=> C6H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.8e+10, 's^-1'), n=1.01, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_28 <=> meCPDyl
""",
)

entry(
    index = 22,
    label = "C6H7-5 <=> C6H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.24e+09, 's^-1'), n=1.12, Ea=(39.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_30 <=> prod_33
""",
)

entry(
    index = 23,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(0.107, 's^-1'), n=3.67, Ea=(29.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt20
""",
)

entry(
    index = 24,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(250000, 's^-1'), n=1.95, Ea=(24, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt18 <=> pdt25
""",
)

entry(
    index = 25,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.59e+08, 's^-1'), n=1.01, Ea=(26.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt16 <=> pdt20
""",
)

entry(
    index = 26,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.67e+09, 's^-1'), n=1.14, Ea=(22.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt28 <=> pdt29
""",
)

entry(
    index = 27,
    label = "C10H11-9 <=> C10H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.46e+07, 's^-1'), n=1.66, Ea=(31.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt28 <=> pdt23
""",
)

entry(
    index = 28,
    label = "C10H11-11 <=> C10H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.83e+08, 's^-1'), n=1.45, Ea=(31.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt10bis <=> pdt37
""",
)

entry(
    index = 29,
    label = "C10H11-13 <=> C10H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.36e+06, 's^-1'), n=1.7, Ea=(31.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: adductd <=> pdt55
""",
)

entry(
    index = 30,
    label = "C10H11-15 <=> C10H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.78e+06, 's^-1'), n=1.75, Ea=(25.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt15 <=> pdt55
""",
)

entry(
    index = 31,
    label = "C10H11-17 <=> C10H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.04e+07, 's^-1'), n=1.61, Ea=(27.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt58 <=> pdt20
""",
)

entry(
    index = 32,
    label = "C6H7-8 <=> C6H7-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.107e+09, 's^-1'), n=0.879, Ea=(22.386, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Krasnoukhov, V. S.', 'Porfiriev, D. P.', 'Zavershinskiy, I. P.', 'Azyazov, V. N.', 'Mebel, A. M.'],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = 'The Journal of Physical Chemistry A',
        volume = '121 (48)',
        pages = '9191-9200',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-f12//B2PLYPD3/aug-cc-pVDZ
""",
)

entry(
    index = 33,
    label = "C9H11 <=> C9H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.68e-11, 's^-1'), n=6.833, Ea=(28.023, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i1 <=> i4
""",
)

entry(
    index = 34,
    label = "C9H11-3 <=> C9H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.842e-10, 's^-1'), n=6.38, Ea=(25.872, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i1 <=> i7
""",
)

entry(
    index = 35,
    label = "C9H11-5 <=> C9H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.414e-06, 's^-1'), n=5.188, Ea=(22.253, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i2 <=> i9
""",
)

entry(
    index = 36,
    label = "C9H11-7 <=> C9H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.478, 's^-1'), n=3.436, Ea=(23.671, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i1 <=> inew
""",
)

entry(
    index = 37,
    label = "C9H11-9 <=> C9H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(721.5, 's^-1'), n=2.46, Ea=(3.681, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: inew <=> i4
""",
)

entry(
    index = 38,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.265e-07, 's^-1'), n=5.639, Ea=(24.541, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: c5-C6H9 <=> c5-C6H9-3
""",
)

entry(
    index = 39,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.537e-16, 's^-1'), n=8.138, Ea=(14.583, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: c5-C6H9 <=> c5-C6H9-2
""",
)

entry(
    index = 40,
    label = "C6H9-5 <=> C6H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.239e-08, 's^-1'), n=6.224, Ea=(24.481, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: c5-C6H9-3 <=> c5-C6H9-2
""",
)

entry(
    index = 41,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(264300, 's^-1'), n=1.839, Ea=(33.509, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W1 <=> W4
""",
)

entry(
    index = 42,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(120000, 's^-1'), n=2.099, Ea=(35.296, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W1 <=> W16
""",
)

entry(
    index = 43,
    label = "C10H9-5 <=> C10H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.62e+09, 's^-1'), n=1.05, Ea=(31.179, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W3 <=> W7
""",
)

entry(
    index = 44,
    label = "C10H9-7 <=> C10H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.806e+09, 's^-1'), n=1.172, Ea=(51.258, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W3 <=> W20
""",
)

entry(
    index = 45,
    label = "C10H9-9 <=> C10H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.346e+08, 's^-1'), n=1.296, Ea=(39.967, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W5 <=> W6
""",
)

entry(
    index = 46,
    label = "C10H9-11 <=> C10H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(65110, 's^-1'), n=2.209, Ea=(29.053, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W9 <=> W7
""",
)

entry(
    index = 47,
    label = "C10H9-13 <=> C10H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.048e+09, 's^-1'), n=0.924, Ea=(30.972, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W9 <=> W10
""",
)

entry(
    index = 48,
    label = "C10H9-15 <=> C10H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.56e+08, 's^-1'), n=1.408, Ea=(41.295, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W10 <=> W20
""",
)

entry(
    index = 49,
    label = "C10H9-17 <=> C10H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.658e+09, 's^-1'), n=0.699, Ea=(7.063, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W7 <=> W20
""",
)

entry(
    index = 50,
    label = "C6H7-9 <=> C6H7-10",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.169e+11, 's^-1'), n=0.707, Ea=(27.741, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Krasnoukhov, V. S.', 'Porfiriev, D. P.', 'Zavershinskiy, I. P.', 'Azyazov, V. N.', 'Mebel, A. M.'],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = 'The Journal of Physical Chemistry A',
        volume = '121 (48)',
        pages = '9191-9200',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-f12//B2PLYPD3/aug-cc-pVDZ
""",
)

entry(
    index = 51,
    label = "C10H11-19 <=> C10H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.07e+06, 's^-1'), n=2, Ea=(26.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt21 <=> pdt27
""",
)

entry(
    index = 52,
    label = "C10H11-21 <=> C10H11-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.18e+07, 's^-1'), n=1.8, Ea=(15.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt16 <=> pdt33
""",
)

entry(
    index = 53,
    label = "C10H11-23 <=> C10H11-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.27e+06, 's^-1'), n=1.5, Ea=(33.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt33 <=> pdt20
""",
)

entry(
    index = 54,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.75e+11, 's^-1'), n=0.633, Ea=(46.955, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W1_2 <=> W5
""",
)

entry(
    index = 55,
    label = "C9H9-3 <=> C9H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(401300, 's^-1'), n=2.064, Ea=(37.093, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W1_2 <=> W8_9
""",
)

entry(
    index = 56,
    label = "C9H9-5 <=> C9H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.915e+06, 's^-1'), n=1.697, Ea=(19.915, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W3_4 <=> W13
""",
)

entry(
    index = 57,
    label = "C9H9-7 <=> C9H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(240, 's^-1'), n=2.932, Ea=(30.907, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W3_4 <=> W6
""",
)

entry(
    index = 58,
    label = "C9H9-9 <=> C9H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(53440, 's^-1'), n=2.305, Ea=(38.286, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W5 <=> W8_9
""",
)

entry(
    index = 59,
    label = "C9H9-11 <=> C9H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.166e+07, 's^-1'), n=1.625, Ea=(37.367, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W6 <=> W13
""",
)

entry(
    index = 60,
    label = "C9H9-13 <=> C9H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(420000, 's^-1'), n=2.094, Ea=(61.014, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W8_9 <=> W20
""",
)

entry(
    index = 61,
    label = "C9H9-15 <=> C9H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.5e+08, 's^-1'), n=0.835, Ea=(58.13, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W8_9 <=> W11
""",
)

entry(
    index = 62,
    label = "C9H9-17 <=> C9H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.45e+06, 's^-1'), n=1.572, Ea=(60.563, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W8_9 <=> W21
""",
)

entry(
    index = 63,
    label = "C9H9-19 <=> C9H9-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.286e+08, 's^-1'), n=1.323, Ea=(24.182, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W11 <=> W21
""",
)

entry(
    index = 64,
    label = "C9H9-21 <=> C9H9-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.37e+08, 's^-1'), n=1.713, Ea=(43.474, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W11 <=> W20
""",
)

entry(
    index = 65,
    label = "C9H9-23 <=> C9H9-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(59980, 's^-1'), n=1.941, Ea=(8.652, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: W21 <=> W20
""",
)

entry(
    index = 66,
    label = "C10H9-19 <=> C10H9-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.964e+07, 's^-1'), n=1.633, Ea=(47.984, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W101 <=> W8
""",
)

entry(
    index = 67,
    label = "C10H9-21 <=> C10H9-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.193e+07, 's^-1'), n=1.425, Ea=(7.283, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W5 <=> W103
""",
)

entry(
    index = 68,
    label = "C10H9-23 <=> C10H9-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+11, 's^-1'), n=0.703, Ea=(23.53, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W104 <=> W6
""",
)

entry(
    index = 69,
    label = "C10H9-25 <=> C10H9-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.423e+08, 's^-1'), n=1.522, Ea=(63.602, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W106 <=> W107
""",
)

entry(
    index = 70,
    label = "C10H9-27 <=> C10H9-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(68.8, 's^-1'), n=3.351, Ea=(60.931, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W106 <=> W108
""",
)

entry(
    index = 71,
    label = "C10H9-9 <=> C10H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.753e+08, 's^-1'), n=1.291, Ea=(40.177, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W112 <=> W118
""",
)

entry(
    index = 72,
    label = "C10H9-29 <=> C10H9-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.93e+07, 's^-1'), n=1.684, Ea=(33.806, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W6 <=> W118
""",
)

entry(
    index = 73,
    label = "C10H9-31 <=> C10H9-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.401e+08, 's^-1'), n=1.453, Ea=(42.614, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W115 <=> W117
""",
)

entry(
    index = 74,
    label = "C10H9-33 <=> C10H9-34",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.181e+10, 's^-1'), n=0.964, Ea=(32.063, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W102 <=> W119
""",
)

entry(
    index = 75,
    label = "C10H7 <=> C10H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.843e+08, 's^-1'), n=1.605, Ea=(56.952, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: W2 <=> W4
""",
)

entry(
    index = 76,
    label = "C10H7-3 <=> C10H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(24735, 's^-1'), n=2.344, Ea=(38.798, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: W3_6 <=> W5
""",
)

entry(
    index = 77,
    label = "C10H7-5 <=> C10H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(191.5, 's^-1'), n=3.05, Ea=(53.137, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: W3_6 <=> W7
""",
)

entry(
    index = 78,
    label = "C8H7 <=> C8H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.445e+06, 's^-1'), n=1.735, Ea=(23.162, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: W1 <=> W3
""",
)

entry(
    index = 79,
    label = "C7H7-9 <=> C7H7-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.712e+10, 's^-1'), n=0.722, Ea=(41.878, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C7H7_11 <=> C7H7_10
""",
)

entry(
    index = 80,
    label = "C9H9-25 <=> C9H9-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.527e+10, 's^-1'), n=0.853, Ea=(47.848, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9_3 <=> C9H9_24
""",
)

entry(
    index = 81,
    label = "C9H9-27 <=> C9H9-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.438e+10, 's^-1'), n=0.625, Ea=(38.324, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9_24 <=> C9H9_14
""",
)

entry(
    index = 82,
    label = "C9H9-29 <=> C9H9-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.231e+11, 's^-1'), n=0.765, Ea=(55.941, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9_3 <=> C9H9_4
""",
)

entry(
    index = 83,
    label = "C9H9-31 <=> C9H9-32",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.677e+10, 's^-1'), n=0.839, Ea=(43.638, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9_4 <=> C9H9_5
""",
)

entry(
    index = 84,
    label = "C:CC[CH2] <=> C:C[CH]C",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.72e+06, 's^-1'), n=1.99, Ea=(27.2, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 1.1 - 1,2 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 85,
    label = "C:CCC[CH2] <=> C:C[CH]CC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(25000, 's^-1'), n=2.28, Ea=(28.5, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 1.2 - 1,3 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 86,
    label = "C:CCCC[CH2] <=> C:C[CH]CCC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(42200, 's^-1'), n=1.93, Ea=(13.5, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 1.3 - 1,4 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 87,
    label = "C:CCCCC[CH2] <=> C:C[CH]CCCC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(15400, 's^-1'), n=1.87, Ea=(7.3, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 1.4 - 1,5 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 88,
    label = "C:CCCCCC[CH2] <=> C:C[CH]CCCCC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1160, 's^-1'), n=1.94, Ea=(6.6, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 1.5 - 1,6 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 89,
    label = "C:C(C)C[CH2] <=> C:C([CH2])CC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(32400, 's^-1'), n=2.04, Ea=(19.7, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 2.1 - 1,4 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 90,
    label = "C:C(C)CC[CH2] <=> C:C([CH2])CCC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(6900, 's^-1'), n=1.98, Ea=(10.2, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 2.2 - 1,5 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 91,
    label = "C:C(C)CCC[CH2] <=> C:C([CH2])CCCC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(312, 's^-1'), n=2.1, Ea=(10.7, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 2.3 - 1,6 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 92,
    label = "CC:CC[CH2] <=> [CH2]C:CCC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(121000, 's^-1'), n=1.9, Ea=(13.3, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 3.1 - 1,5 H-shift
Calculation was made for the trans isomer
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 93,
    label = "CC:CCC[CH2] <=> [CH2]C:CCCC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(8010, 's^-1'), n=1.94, Ea=(13.3, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 3.2 - 1,6 H-shift
Calculation was made for the trans isomer
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 94,
    label = "C:C([CH2])CC:C <=> C:C(C)[CH]C:C",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(20800, 's^-1'), n=2.49, Ea=(43.1, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 7.1 - 1,3 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 95,
    label = "C:CCC:C[CH2] <=> C:C[CH]C:CC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(256000, 's^-1'), n=2, Ea=(28.1, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 8.1 - 1,4 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 96,
    label = "C:C([CH2])C:CC <=> C:C(C)C:C[CH2]",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(4.44e+06, 's^-1'), n=1.64, Ea=(24, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 9.1 - 1,5 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 97,
    label = "C:C(C)[CH2] <=> C:C([CH2])C",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(235500, 's^-1'), n=2.44, Ea=(51.6, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 4.1 - 1,3 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 98,
    label = "C:C([CH2])CCC:C <=> C:C(C)C[CH]C:C",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(103200, 's^-1'), n=2.04, Ea=(25.3, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 4.2 - 1,4 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 99,
    label = "C:C([CH2])CCCC:C <=> C:C(C)CC[CH]C:C",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(18840, 's^-1'), n=1.93, Ea=(16.2, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 4.3 - 1,5 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 100,
    label = "C:C([CH2])CCCCC:C <=> C:C(C)CCC[CH]C:C",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(113.6, 's^-1'), n=2.07, Ea=(15.1, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 4.4 - 1,6 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 101,
    label = "CC:C[CH2] <=> [CH2]C:CC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(800000, 's^-1'), n=1.81, Ea=(35.8, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 5.1 - 1,4 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 102,
    label = "C:CCCC:C[CH2] <=> C:C[CH]CC:CC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(252000, 's^-1'), n=1.85, Ea=(21.1, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 5.2 - 1,5 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 103,
    label = "C:CCCCC:C[CH2] <=> C:C[CH]CCC:CC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(10940, 's^-1'), n=1.94, Ea=(20.9, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 5.3 - 1,6 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 104,
    label = "C:C([CH2])CC:CC <=> C:C(C)CC:C[CH2]",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(63300, 's^-1'), n=1.92, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
Reaction 6.1 - 1,6 H-shift
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 105,
    label = "C[CH2] <=> [CH2]C",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(7.05e+06, 's^-1'), n=1.81, Ea=(37.1, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,2 H-Shift Primary-Primary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 106,
    label = "CCC[CH2]-1 <=> CC[CH]C",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.48e+07, 's^-1'), n=1.57, Ea=(35.3, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,2 H-Shift Primary-Secondary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 107,
    label = "CC[CH2] <=> [CH2]CC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(88500, 's^-1'), n=2.17, Ea=(35.4, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,3 H-Shift Primary-Primary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 108,
    label = "CCCC[CH2] <=> CC[CH]CC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.064e+06, 's^-1'), n=1.93, Ea=(33.8, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,3 H-Shift Primary-Secondary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 109,
    label = "CCC[CH2]-2 <=> [CH2]CCC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(114000, 's^-1'), n=1.74, Ea=(19.8, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,4 H-Shift Primary-Primary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 110,
    label = "CCCCCCC[CH2]-1 <=> CCCC[CH]CCC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(754000, 's^-1'), n=1.63, Ea=(17.9, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,4 H-Shift Primary-Secondary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 111,
    label = "CCCC[CH2]-2 <=> [CH2]CCCC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(68850, 's^-1'), n=1.68, Ea=(12.6, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,5 H-Shift Primary-Primary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 112,
    label = "CCCCC[CH2]-1 <=> C[CH]CCCC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(262000, 's^-1'), n=1.62, Ea=(11.1, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,5 H-Shift Primary-Secondary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 113,
    label = "CCCCC[CH2]-2 <=> [CH2]CCCCC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3690, 's^-1'), n=1.79, Ea=(11.9, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,6 H-Shift Primary-Primary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 114,
    label = "CCCCCC[CH2]-1 <=> C[CH]CCCCC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(25800, 's^-1'), n=1.67, Ea=(10.2, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,6 H-Shift Primary-Secondary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 115,
    label = "CCCCCC[CH2]-2 <=> [CH2]CCCCCC",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(64.2, 's^-1'), n=2.1, Ea=(15.1, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,7 H-Shift Primary-Primary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 116,
    label = "CCCCCCC[CH2]-2 <=> C[CH]CCCCCC",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1062, 's^-1'), n=1.81, Ea=(13.2, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Kun Wang', 'Stephanie M. Villano', 'Anthony M. Dean'],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = 'Chemphyschem',
        volume = '16',
        pages = '2635-2645',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,7 H-Shift Primary-Secondary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)

entry(
    index = 117,
    label = "C3H3O2 <=> C3H3O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.427, 's^-1'), n=3.311, Ea=(30.765, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3 level with 1D rotor consideration
Jim Chu's calculation
""",
)

entry(
    index = 118,
    label = "C4H5 <=> C4H5-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(3.992e-05, 's^-1'), n=4.805, Ea=(56.041, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 119,
    label = "C4H5-3 <=> C4H5-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(606700, 's^-1'), n=2.347, Ea=(51.259, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 120,
    label = "C4H5-5 <=> C4H5-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.471e+06, 's^-1'), n=1.841, Ea=(29.797, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 121,
    label = "C4H5-7 <=> C4H5-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(481900, 's^-1'), n=2.375, Ea=(40.143, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 122,
    label = "C4H5-2 <=> C4H5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(0.005931, 's^-1'), n=4.271, Ea=(56.912, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 123,
    label = "C4H5-4 <=> C4H5-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.63e+08, 's^-1'), n=1.73, Ea=(49.649, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 124,
    label = "C4H5-6 <=> C4H5-5",
    degeneracy = 3.0,
    kinetics = Arrhenius(A=(5.11e+06, 's^-1'), n=1.95, Ea=(42.693, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 125,
    label = "C4H5-8 <=> C4H5-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.189e+07, 's^-1'), n=1.951, Ea=(50.732, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Ribeiro, J. M.', 'Mebel, A. M.'],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '19 (22)',
        pages = '14543-14554',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/CBS//B2PLYPD3/cc-pVTZ
""",
)

entry(
    index = 126,
    label = "C7H7-11 <=> C7H7-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(74200, 's^-1'), n=2.23, Ea=(10.59, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = 'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 127,
    label = "C7H7-7 <=> C7H7-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(11700, 's^-1'), n=2.78, Ea=(62.71, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = 'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 128,
    label = "C7H7-13 <=> C7H7-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.48e+06, 's^-1'), n=1.85, Ea=(26.83, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['da Silva, G.', 'Cole, J. A.', 'Bozzelli, J. W.'],
        title = 'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = 'The Journal of Physical Chemistry A',
        volume = '114 (6)',
        pages = '2275-2283',
        year = '2010',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
G3SX//B3LYP/6-31G(2df,p)
""",
)

entry(
    index = 129,
    label = "C3H7 <=> C3H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.918e+09, 's^-1'),
        n = 1.39,
        Ea = (166.105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green.

Converted to training reaction from rate rule: R2H_S;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 130,
    label = "C4H9 <=> C4H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.76e+09, 's^-1'),
        n = 0.76,
        Ea = (145.185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 131,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.22e+09, 's^-1'),
        n = 0.13,
        Ea = (86.6088, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.

Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 132,
    label = "C6H13 <=> C6H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.86e+10, 's^-1'),
        n = 0.58,
        Ea = (109.579, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. 

NEEDS TO BE CHECKED

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_single;Cs_H_out_noH
""",
)

entry(
    index = 133,
    label = "CCCCC[CH2]-1 <=> C6H13-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.36e+10, 's^-1'),
        n = -0.66,
        Ea = (59.7475, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green

Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 134,
    label = "C3H7O <=> C3H7O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3e+11, 's^-1'),
        n = 0,
        Ea = (123.01, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R4H_SSS;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 135,
    label = "C4H9O <=> C4H9O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2e+11, 's^-1'),
        n = 0,
        Ea = (112.34, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R4H_SSS;O_rad_out;Cs_H_out_1H
""",
)

entry(
    index = 136,
    label = "C5H11O <=> C5H11O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0,
        Ea = (100.834, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R4H_SSS;O_rad_out;Cs_H_out_noH
""",
)

entry(
    index = 137,
    label = "C4H9O-3 <=> C4H9O-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.75e+10, 's^-1'),
        n = 0,
        Ea = (102.09, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R5H_SSSS;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 138,
    label = "C5H11O-3 <=> C5H11O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.5e+10, 's^-1'),
        n = 0,
        Ea = (87.2364, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R5H_SSSS;O_rad_out;Cs_H_out_1H
""",
)

entry(
    index = 139,
    label = "C6H13O <=> C6H13O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+10, 's^-1'),
        n = 0,
        Ea = (79.9144, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R5H_SSSS;O_rad_out;Cs_H_out_noH
""",
)

entry(
    index = 140,
    label = "C5H11O-5 <=> C5H11O-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.68e+09, 's^-1'),
        n = 0,
        Ea = (93.5124, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R6H_SSSSS;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 141,
    label = "C6H13O-3 <=> C6H13O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.12e+09, 's^-1'),
        n = 0,
        Ea = (79.7052, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R6H_SSSSS;O_rad_out;Cs_H_out_1H
""",
)

entry(
    index = 142,
    label = "C7H15O <=> C7H15O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.56e+09, 's^-1'),
        n = 0,
        Ea = (71.3372, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R6H_SSSSS;O_rad_out;Cs_H_out_noH
""",
)

entry(
    index = 143,
    label = "C6H13O-5 <=> C6H13O-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (5.85e+08, 's^-1'),
        n = 0,
        Ea = (106.901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R7H;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 144,
    label = "C7H15O-3 <=> C7H15O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.9e+08, 's^-1'),
        n = 0,
        Ea = (106.901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R7H;O_rad_out;Cs_H_out_1H
""",
)

entry(
    index = 145,
    label = "C8H17O <=> C8H17O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.95e+08, 's^-1'),
        n = 0,
        Ea = (106.901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Curran's estimstion [8] in his reaction type 12 RO2 isomerization.""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimstion in his reaction type 12 RO2 isomerization.

Converted to training reaction from rate rule: R7H;O_rad_out;Cs_H_out_noH
""",
)

entry(
    index = 146,
    label = "C3H7-2 <=> C3H7",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.86e+09, 's^-1'),
        n = 1.32,
        Ea = (168.615, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 147,
    label = "C3H7 <=> C3H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (718000, 's^-1'),
        n = 2.05,
        Ea = (151.879, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""JWA CCSD(T)-F12/cc-pVTZ-F12 with 1d-HR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 148,
    label = "C4H9-3 <=> C4H9-4",
    degeneracy = 9.0,
    kinetics = Arrhenius(
        A = (7.308e+08, 's^-1'),
        n = 1.66,
        Ea = (169.87, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 149,
    label = "C4H9-4 <=> C4H9-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.04e+10, 's^-1'),
        n = 0.64,
        Ea = (141.838, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 150,
    label = "C5H11-3 <=> C5H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.25e+10, 's^-1'),
        n = 0.6,
        Ea = (154.39, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 151,
    label = "C5H11-4 <=> C5H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.24e+09, 's^-1'),
        n = 1.19,
        Ea = (163.176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 152,
    label = "C3H5 <=> C3H5-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (7.32e+09, 's^-1'),
        n = 1.12,
        Ea = (172.799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;Cd_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 153,
    label = "C3H5-2 <=> C3H5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.36e+11, 's^-1'),
        n = 0.63,
        Ea = (260.245, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cd_H_out_doubleC
""",
)

entry(
    index = 154,
    label = "C5H7 <=> C5H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.448e+10, 's^-1'),
        n = 0.82,
        Ea = (156.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;Cd_rad_out;Cs_H_out_H/OneDe
""",
)

entry(
    index = 155,
    label = "C5H7-2 <=> C5H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.876e+11, 's^-1'),
        n = 0.71,
        Ea = (262.755, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/OneDe;Cd_H_out_doubleC
""",
)

entry(
    index = 156,
    label = "C6H9-7 <=> C6H9-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.06e+09, 's^-1'),
        n = 1.31,
        Ea = (263.174, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_OneDe/Cs;Cd_H_out_doubleC
""",
)

entry(
    index = 157,
    label = "C4H7 <=> C:CC[CH2]",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6.18e+09, 's^-1'),
        n = 1.22,
        Ea = (199.995, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/OneDe;Cs_H_out_2H
""",
)

entry(
    index = 158,
    label = "C:CC[CH2] <=> C4H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.82e+08, 's^-1'),
        n = 1.28,
        Ea = (116.734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 159,
    label = "C5H9 <=> C5H9-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.9e+10, 's^-1'),
        n = 0.75,
        Ea = (190.79, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/OneDe;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 160,
    label = "C5H9-2 <=> C5H9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.682e+10, 's^-1'),
        n = 0.35,
        Ea = (125.102, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe
""",
)

entry(
    index = 161,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.01e+12, 's^-1'),
        n = 0.33,
        Ea = (176.983, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/OneDe;Cs_H_out_Cs2
""",
)

entry(
    index = 162,
    label = "C6H11-2 <=> C6H11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.94e+08, 's^-1'),
        n = 1.27,
        Ea = (125.938, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_H/OneDe
""",
)

entry(
    index = 163,
    label = "C5H9-3 <=> C5H9-4",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.614e+09, 's^-1'),
        n = 1.31,
        Ea = (203.342, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_2H
""",
)

entry(
    index = 164,
    label = "C6H11-3 <=> C6H11-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.26e+10, 's^-1'),
        n = 0.77,
        Ea = (192.464, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 165,
    label = "C7H13 <=> C7H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.62e+13, 's^-1'),
        n = -0.14,
        Ea = (184.096, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_OneDe/Cs;Cs_H_out_Cs2
""",
)

entry(
    index = 166,
    label = "C3H5-3 <=> C3H5-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.24e+11, 's^-1'),
        n = 0.73,
        Ea = (177.402, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_D;Cd_rad_out_singleH;Cd_H_out_singleNd
""",
)

entry(
    index = 167,
    label = "C3H5-4 <=> C3H5-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.24e+11, 's^-1'),
        n = 0.8,
        Ea = (198.74, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_D;Cd_rad_out_singleNd;Cd_H_out_singleH
""",
)

entry(
    index = 168,
    label = "C4H7-2 <=> C4H7-3",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.374e+10, 's^-1'),
        n = 1.08,
        Ea = (169.034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_2H
""",
)

entry(
    index = 169,
    label = "C4H7-3 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.14e+10, 's^-1'),
        n = 0.81,
        Ea = (192.882, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 170,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.266e+11, 's^-1'),
        n = 0.65,
        Ea = (161.921, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 171,
    label = "C5H9-6 <=> C5H9-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.74e+09, 's^-1'),
        n = 0.98,
        Ea = (194.974, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 172,
    label = "C6H11-5 <=> C6H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.9e+11, 's^-1'),
        n = 0.36,
        Ea = (149.787, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy3;Cs_H_out_Cs2
""",
)

entry(
    index = 173,
    label = "C6H11-6 <=> C6H11-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.44e+08, 's^-1'),
        n = 1.39,
        Ea = (197.485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 174,
    label = "C5H9-7 <=> C5H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.75e+09, 's^-1'),
        n = 0.98,
        Ea = (153.134, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 175,
    label = "C5H9-8 <=> C5H9-7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.232e+09, 's^-1'),
        n = 1.2,
        Ea = (174.473, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_2H
""",
)

entry(
    index = 176,
    label = "C6H11-7 <=> C6H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.64e+09, 's^-1'),
        n = 1,
        Ea = (162.339, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 177,
    label = "C6H11-8 <=> C6H11-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.312e+10, 's^-1'),
        n = 0.81,
        Ea = (166.105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 178,
    label = "C7H13-3 <=> C7H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.31e+08, 's^-1'),
        n = 1.21,
        Ea = (162.758, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 179,
    label = "C7H13-4 <=> C7H13-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.86e+10, 's^-1'),
        n = 0.58,
        Ea = (159.829, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy4;Cs_H_out_Cs2
""",
)

entry(
    index = 180,
    label = "C6H11-9 <=> C6H11-10",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.21e+09, 's^-1'),
        n = 1.19,
        Ea = (179.075, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_2H
""",
)

entry(
    index = 181,
    label = "C6H11-10 <=> C6H11-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.35e+09, 's^-1'),
        n = 0.99,
        Ea = (141.001, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 182,
    label = "C7H13-5 <=> C7H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.29e+09, 's^-1'),
        n = 0.89,
        Ea = (152.298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 183,
    label = "C7H13-6 <=> C7H13-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.16e+10, 's^-1'),
        n = 0.81,
        Ea = (172.381, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 184,
    label = "C8H15 <=> C8H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.48e+07, 's^-1'),
        n = 1.45,
        Ea = (156.482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 185,
    label = "C8H15-2 <=> C8H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.24e+11, 's^-1'),
        n = 1.47,
        Ea = (166.523, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2_cy5;Cs_H_out_Cs2
""",
)

entry(
    index = 186,
    label = "C4H9 <=> C4H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.9e+09, 's^-1'),
        n = 0.82,
        Ea = (146.858, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 187,
    label = "C4H9-2 <=> C4H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.19e+08, 's^-1'),
        n = 1.32,
        Ea = (161.502, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 188,
    label = "C5H11-5 <=> C5H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.25e+10, 's^-1'),
        n = 0.66,
        Ea = (137.654, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 189,
    label = "C5H11-6 <=> C5H11-5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.167e+07, 's^-1'),
        n = 1.77,
        Ea = (158.574, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 190,
    label = "C6H13-4 <=> C6H13-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.27e+09, 's^-1'),
        n = 0.66,
        Ea = (144.766, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 191,
    label = "C6H13-5 <=> C6H13-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.42e+07, 's^-1'),
        n = 1.41,
        Ea = (151.042, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 192,
    label = "C3H5-5 <=> C3H5-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.53e+10, 's^-1'),
        n = 0.97,
        Ea = (157.737, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleH;Cs_H_out_2H
""",
)

entry(
    index = 193,
    label = "C3H5-6 <=> C3H5-5",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (19040, 's^-1'),
        n = 2.82,
        Ea = (238.906, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""calculated BMK/cbsb7 Aaron Vandeputte""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_2H;Cd_H_out_singleH
""",
)

entry(
    index = 194,
    label = "C4H7-4 <=> C4H7-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.846e+10, 's^-1'),
        n = 0.74,
        Ea = (145.185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleH;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 195,
    label = "C4H7-5 <=> C4H7-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.32e+10, 's^-1'),
        n = 0.77,
        Ea = (268.194, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_H/NonDeC;Cd_H_out_singleH
""",
)

entry(
    index = 196,
    label = "C5H9-9 <=> C5H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.04e+10, 's^-1'),
        n = 0.59,
        Ea = (135.98, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleH;Cs_H_out_Cs2
""",
)

entry(
    index = 197,
    label = "C5H9-10 <=> C5H9-9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.706e+09, 's^-1'),
        n = 1.27,
        Ea = (267.358, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_Cs2;Cd_H_out_singleH
""",
)

entry(
    index = 198,
    label = "C4H7-6 <=> C4H7-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.58e+09, 's^-1'),
        n = 1.08,
        Ea = (161.921, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleNd;Cs_H_out_2H
""",
)

entry(
    index = 199,
    label = "C4H7-7 <=> C4H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.91e+11, 's^-1'),
        n = 0.63,
        Ea = (255.224, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SD;C_rad_out_2H;Cd_H_out_singleNd
""",
)

entry(
    index = 200,
    label = "C5H9-11 <=> C5H9-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.182e+10, 's^-1'),
        n = 0.86,
        Ea = (149.369, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleNd;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 201,
    label = "C5H9-12 <=> C5H9-11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.92e+10, 's^-1'),
        n = 0.83,
        Ea = (257.734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_H/NonDeC;Cd_H_out_singleNd
""",
)

entry(
    index = 202,
    label = "C6H11-11 <=> C6H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.05e+09, 's^-1'),
        n = 0.86,
        Ea = (139.746, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleNd;Cs_H_out_Cs2
""",
)

entry(
    index = 203,
    label = "C6H11-12 <=> C6H11-11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.05e+10, 's^-1'),
        n = 0.79,
        Ea = (255.224, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SD;C_rad_out_Cs2;Cd_H_out_singleNd
""",
)

entry(
    index = 204,
    label = "C4H7-8 <=> C4H7-9",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.304e+09, 's^-1'),
        n = 1.24,
        Ea = (151.879, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;Cd_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 205,
    label = "C4H7-9 <=> C4H7-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.24e+08, 's^-1'),
        n = 1.14,
        Ea = (172.799, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cd_H_out_doubleC
""",
)

entry(
    index = 206,
    label = "C5H9-13 <=> C5H9-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.32e+09, 's^-1'),
        n = 0.99,
        Ea = (141.419, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;Cd_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 207,
    label = "C5H9-14 <=> C5H9-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.37e+07, 's^-1'),
        n = 1.41,
        Ea = (177.82, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cd_H_out_doubleC
""",
)

entry(
    index = 208,
    label = "C6H11-13 <=> C6H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+10, 's^-1'),
        n = 0.78,
        Ea = (132.633, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;Cd_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 209,
    label = "C6H11-14 <=> C6H11-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.5e+06, 's^-1'),
        n = 1.68,
        Ea = (176.983, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cd_H_out_doubleC
""",
)

entry(
    index = 210,
    label = "C5H9-15 <=> C5H9-16",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.68e+11, 's^-1'),
        n = 0.82,
        Ea = (205.853, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 211,
    label = "C5H9-16 <=> C5H9-15",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.692e+09, 's^-1'),
        n = 1.47,
        Ea = (223.007, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 212,
    label = "C6H11-15 <=> C6H11-16",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.86e+11, 's^-1'),
        n = 0.65,
        Ea = (198.74, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 213,
    label = "C6H11-16 <=> C6H11-15",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.136e+08, 's^-1'),
        n = 1.72,
        Ea = (216.731, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 214,
    label = "C7H13-7 <=> C7H13-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.46e+10, 's^-1'),
        n = 0.76,
        Ea = (199.577, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 215,
    label = "C7H13-8 <=> C7H13-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.228e+11, 's^-1'),
        n = 0.8,
        Ea = (201.25, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 216,
    label = "C5H9-17 <=> C:CCC[CH2]",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.14e+10, 's^-1'),
        n = 0.99,
        Ea = (203.761, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/OneDe;Cs_H_out_2H
""",
)

entry(
    index = 217,
    label = "C:CCC[CH2] <=> C5H9-17",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.32e+08, 's^-1'),
        n = 1.1,
        Ea = (123.01, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 218,
    label = "C6H11-17 <=> C6H11-18",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.354e+10, 's^-1'),
        n = 0.74,
        Ea = (192.882, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/OneDe;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 219,
    label = "C6H11-18 <=> C6H11-17",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.82e+09, 's^-1'),
        n = 0.73,
        Ea = (127.612, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe
""",
)

entry(
    index = 220,
    label = "C7H13-9 <=> C7H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.06e+10, 's^-1'),
        n = 0.44,
        Ea = (182.422, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/OneDe;Cs_H_out_Cs2
""",
)

entry(
    index = 221,
    label = "C7H13-10 <=> C7H13-9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.28e+07, 's^-1'),
        n = 1.56,
        Ea = (126.775, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_H/OneDe
""",
)

entry(
    index = 222,
    label = "C5H9-18 <=> C5H9-19",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (5.34e+09, 's^-1'),
        n = 1.04,
        Ea = (151.879, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_2H
""",
)

entry(
    index = 223,
    label = "C5H9-19 <=> C5H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.72e+09, 's^-1'),
        n = 0.78,
        Ea = (164.431, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 224,
    label = "C6H11-19 <=> C6H11-20",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.78e+09, 's^-1'),
        n = 0.77,
        Ea = (141.419, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 225,
    label = "C6H11-20 <=> C6H11-19",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.73e+08, 's^-1'),
        n = 1.14,
        Ea = (169.034, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 226,
    label = "C7H13-11 <=> C7H13-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.08e+10, 's^-1'),
        n = 0.36,
        Ea = (133.051, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy3;Cs_H_out_Cs2
""",
)

entry(
    index = 227,
    label = "C7H13-12 <=> C7H13-11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.86e+06, 's^-1'),
        n = 1.65,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2_cy3
""",
)

entry(
    index = 228,
    label = "C6H11-21 <=> C6H11-22",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.24e+08, 's^-1'),
        n = 1.25,
        Ea = (165.686, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_2H
""",
)

entry(
    index = 229,
    label = "C6H11-22 <=> C6H11-21",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.09e+09, 's^-1'),
        n = 0.84,
        Ea = (144.348, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 230,
    label = "C7H13-13 <=> C7H13-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.1e+08, 's^-1'),
        n = 0.99,
        Ea = (156.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 231,
    label = "C7H13-14 <=> C7H13-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.69e+08, 's^-1'),
        n = 0.97,
        Ea = (150.206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 232,
    label = "C8H15-3 <=> C8H15-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.2e+09, 's^-1'),
        n = 0.54,
        Ea = (148.532, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy4;Cs_H_out_Cs2
""",
)

entry(
    index = 233,
    label = "C8H15-4 <=> C8H15-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.49e+07, 's^-1'),
        n = 1.38,
        Ea = (148.114, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2_cy4
""",
)

entry(
    index = 234,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (9.42e+08, 's^-1'),
        n = 1.26,
        Ea = (171.962, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_2H
""",
)

entry(
    index = 235,
    label = "C7H13-16 <=> C7H13-15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.9e+09, 's^-1'),
        n = 0.82,
        Ea = (137.654, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 236,
    label = "C8H15-5 <=> C8H15-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.5e+08, 's^-1'),
        n = 1.01,
        Ea = (163.594, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 237,
    label = "C8H15-6 <=> C8H15-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.5e+08, 's^-1'),
        n = 0.9,
        Ea = (143.093, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 238,
    label = "C9H17 <=> C9H17-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.97e+10, 's^-1'),
        n = 0.46,
        Ea = (156.063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2_cy5;Cs_H_out_Cs2
""",
)

entry(
    index = 239,
    label = "C9H17-2 <=> C9H17",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.21e+08, 's^-1'),
        n = 1.04,
        Ea = (143.093, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2_cy5
""",
)

entry(
    index = 240,
    label = "CH3O2 <=> CH3O2-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.71e+08, 's^-1'),
        n = 1.45,
        Ea = (176.858, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
CH3OO to CH2OOH, degeneracy=3, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 241,
    label = "C2H5O2 <=> C2H5O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.66e+08, 's^-1'),
        n = 1.28,
        Ea = (166.272, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
CH3CH2OO to CH3CHOOH, degeneracy=2, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 242,
    label = "C3H7O2 <=> C3H7O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.44e+09, 's^-1'),
        n = 1.17,
        Ea = (165.937, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
CH3CH2CH2OO to CH3CH2CHOOH, degeneracy=2, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 243,
    label = "C4H9O2 <=> C4H9O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.07e+10, 's^-1'),
        n = 0.98,
        Ea = (165.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
(CH3)2CHCH2OO to (CH3)2CHCHOOH, degeneracy=2, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/(NonDeC/Cs/Cs)
""",
)

entry(
    index = 244,
    label = "C5H11O2 <=> C5H11O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.62e+09, 's^-1'),
        n = 1.04,
        Ea = (164.599, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
(CH3)3CCH2OO to (CH3)3CCHOOH, degeneracy=2, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/(NonDeC/Cs/Cs/Cs)
""",
)

entry(
    index = 245,
    label = "C3H7O2-3 <=> C3H7O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.97e+09, 's^-1'),
        n = 1.01,
        Ea = (160.958, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
(CH3)2CHOO to (CH3)2COOH, degeneracy=1, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 246,
    label = "C2H5O2-3 <=> C2H5O2-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.989e+11, 's^-1'),
        n = 0.15,
        Ea = (143.135, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
CH3CH2OO to CH2CH2OOH, degeneracy=3, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 247,
    label = "C3H7O2-5 <=> C3H7O2-6",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (6.36e+08, 's^-1'),
        n = 1.06,
        Ea = (140.206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
(CH3)2CHOO to CH3(CH2)CHOOH, degeneracy=6, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 248,
    label = "C4H9O2-3 <=> C4H9O2-4",
    degeneracy = 9.0,
    kinetics = Arrhenius(
        A = (5.058e+08, 's^-1'),
        n = 1.2,
        Ea = (140.29, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy CBS-Q calculations""",
    longDesc = 
u"""
(CH3)3COO to (CH3)2(CH2)COOH, degeneracy=9, rate for per hydrogen, J. Phys. Chem. A.,Vol.114,No.18,2010

Converted to training reaction from rate rule: R4H_SSS_O(Cs)CsCs;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 249,
    label = "C3H7O2-7 <=> C3H7O2-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4e+08, 's^-1'),
        n = 1.1,
        Ea = (125.897, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 250,
    label = "C4H9O2-5 <=> C4H9O2-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.962e+09, 's^-1'),
        n = 0.88,
        Ea = (123.344, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 251,
    label = "C5H11O2-3 <=> C5H11O2-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.06e+09, 's^-1'),
        n = 0.69,
        Ea = (125.98, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_O(Cs)CsCs;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 252,
    label = "C4H9O2-7 <=> C4H9O2-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.64e+09, 's^-1'),
        n = 0.78,
        Ea = (113.428, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 253,
    label = "C5H11O2-5 <=> C5H11O2-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.25e+09, 's^-1'),
        n = 0.57,
        Ea = (114.265, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 254,
    label = "C6H13O2 <=> C6H13O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.87e+10, 's^-1'),
        n = 0.35,
        Ea = (110.416, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_O(Cs)CsCs;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 255,
    label = "C3H7O2-9 <=> C3H7O2-10",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (5.07e+06, 's^-1'),
        n = 1.55,
        Ea = (87.9477, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 256,
    label = "C4H9O2-9 <=> C4H9O2-10",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.034e+07, 's^-1'),
        n = 1.35,
        Ea = (87.1946, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 257,
    label = "C5H11O2-7 <=> C5H11O2-8",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.305e+08, 's^-1'),
        n = 1.12,
        Ea = (91.5459, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC_CC;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 258,
    label = "C4H9O2-11 <=> C4H9O2-12",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (8.46e+07, 's^-1'),
        n = 1.32,
        Ea = (89.956, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCs(Cs/Cs);O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 259,
    label = "C5H11O2-9 <=> C5H11O2-10",
    degeneracy = 9.0,
    kinetics = Arrhenius(
        A = (9.81e+08, 's^-1'),
        n = 1.23,
        Ea = (90.4581, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCs(Cs/Cs/Cs);O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 260,
    label = "C4H9O2-13 <=> C4H9O2-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.788e+07, 's^-1'),
        n = 1.26,
        Ea = (76.0233, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 261,
    label = "C5H11O2-11 <=> C5H11O2-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.76e+10, 's^-1'),
        n = 0.21,
        Ea = (77.404, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 262,
    label = "C5H11O2-13 <=> C5H11O2-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.174e+08, 's^-1'),
        n = 1.15,
        Ea = (64.3081, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 263,
    label = "C4H9O2-15 <=> C4H9O2-16",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.107e+06, 's^-1'),
        n = 1.52,
        Ea = (83.8892, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman).""",
    longDesc = 
u"""
CBS-QB3 and BH&HLYP calculations (Catherina Wijaya & Sumathy Raman). Including treatment of hindered rotor.

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 264,
    label = "C5H11O2-15 <=> C5H11O2-16",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.24e+06, 's^-1'),
        n = 1.22,
        Ea = (69.4544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. 
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 265,
    label = "C6H13O2-3 <=> C6H13O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.48e+06, 's^-1'),
        n = 1.22,
        Ea = (57.9066, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 266,
    label = "C5H11O2-17 <=> C5H11O2-18",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (271800, 's^-1'),
        n = 1.51,
        Ea = (83.4708, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 267,
    label = "C6H13O2-5 <=> C6H13O2-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.74e+06, 's^-1'),
        n = 0.99,
        Ea = (76.0233, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Curran's [8] estimation in reaction type 19, QOOH = cyclic ether + OH""",
    longDesc = 
u"""
[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. 
Curran's estimation in reaction type 19, QOOH = cyclic ether + OH

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 268,
    label = "C7H15O2 <=> C7H15O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (562000, 's^-1'),
        n = 1.09,
        Ea = (59.7475, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 269,
    label = "CH3O3 <=> CH3O3-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6e+08, 's^-1'),
        n = 1.23,
        Ea = (154.18, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 270,
    label = "C2H5O3 <=> C2H5O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3e+08, 's^-1'),
        n = 1.23,
        Ea = (154.18, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 271,
    label = "C2H5O3-3 <=> C2H5O3-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.22e+08, 's^-1'),
        n = 1.09,
        Ea = (109.37, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 272,
    label = "C3H7O3 <=> C3H7O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.29e+09, 's^-1'),
        n = 0.75,
        Ea = (103.847, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 273,
    label = "C3H7O3-3 <=> C3H7O3-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.84e+09, 's^-1'),
        n = 0.82,
        Ea = (109.956, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 274,
    label = "C4H9O3 <=> C4H9O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.18e+11, 's^-1'),
        n = 0.51,
        Ea = (109.621, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 275,
    label = "C3H7O3-5 <=> C3H7O3-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (23000, 's^-1'),
        n = 2.11,
        Ea = (64.7265, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 276,
    label = "C4H9O3-3 <=> C4H9O3-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.9e+07, 's^-1'),
        n = 1.1,
        Ea = (64.4336, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 277,
    label = "C4H9O3-5 <=> C4H9O3-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.58e+08, 's^-1'),
        n = 1.12,
        Ea = (64.3499, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 278,
    label = "C5H11O3 <=> C5H11O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.17e+11, 's^-1'),
        n = 0.43,
        Ea = (64.4336, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 279,
    label = "C4H9O3-7 <=> C4H9O3-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1098, 's^-1'),
        n = 2.21,
        Ea = (60.1659, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 280,
    label = "C5H11O3-3 <=> C5H11O3-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (72300, 's^-1'),
        n = 1.65,
        Ea = (50.2917, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 281,
    label = "C5H11O3-5 <=> C5H11O3-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.866e+06, 's^-1'),
        n = 0.75,
        Ea = (53.6389, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 282,
    label = "C6H13O3 <=> C6H13O3-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.41e+06, 's^-1'),
        n = 1.09,
        Ea = (52.3, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Sandeep and Sumathy paper (submitted to JPCA 2009), intra_H_migration of ROO & HOOQOO.

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_NDMustO
""",
)

entry(
    index = 283,
    label = "C5H7-3 <=> C5H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.32e+06, 's^-1'),
        n = 1.6229,
        Ea = (184.393, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R4H_SDS;C_rad_out_2H;Cd_H_out_doubleC
""",
)

entry(
    index = 284,
    label = "C5H7-4 <=> C5H7-3",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.33e+08, 's^-1'),
        n = 1.1915,
        Ea = (103.605, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R4H_SDS;Cd_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 285,
    label = "C5H7-5 <=> C5H7-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (438000, 's^-1'),
        n = 1.7613,
        Ea = (160.143, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R5H_SMSD;C_rad_out_2H;Cd_H_out_singleH
""",
)

entry(
    index = 286,
    label = "C5H7-6 <=> C5H7-5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (408000, 's^-1'),
        n = 1.9199,
        Ea = (33.0402, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R5H_DSMS;Cd_rad_out_singleH;Cs_H_out_2H
""",
)

entry(
    index = 287,
    label = "C5H7-7 <=> C5H7-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.59e+07, 's^-1'),
        n = 1.4638,
        Ea = (277.467, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R3H_SD;C_rad_out_2H;Cd_H_out_singleDe
""",
)

entry(
    index = 288,
    label = "C5H7-8 <=> C5H7-7",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.85113e+09, 's^-1'),
        n = 1.0541,
        Ea = (193.078, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1600, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Sandeep's CBS-QB3 calculations.""",
    longDesc = 
u"""
Sandeep's CBS-QB3 calculations.

Converted to training reaction from rate rule: R3H_DS;Cd_rad_out_singleDe;Cs_H_out_2H
""",
)

entry(
    index = 289,
    label = "C4H7O <=> C4H7O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.22e+06, 's^-1', '*|/', 3),
        n = 1.78,
        Ea = (113.721, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MHS CBS-QB3 calculations.""",
    longDesc = 
u"""
MHS CBS-QB3 calculations for CH3-CH2-CH=CH-O* == CH3-C*H-CH=CH-OH.  
Product is the cis configuration because TS is also cis.  
Note--this only affects the tunneling correction (b/c in products).  
Only methyl rotor was considered for TS.

Converted to training reaction from rate rule: R4H_SDS;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 290,
    label = "C4H7O-3 <=> C4H7O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.468e+06, 's^-1', '*|/', 3),
        n = 1.554,
        Ea = (111.445, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations w/1d h.r. corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations with 1-d hindered rotor corrections for CH2=CH-CH2-OO => CH=CH-CH2-OOH

Previous RMG estimate for this reaction was an "Average of average" estimate.  This reaction was of
interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => C2H2+CH2O+OH.  The high-p
limit kinetics were necessary to estimate a k(T,P) for this PES.

Reactant: 2 hindered rotors were considered (the OO and CH2OO torsions)
TS: 0 hindered rotors were considered (MRH did not think 1-d separable rotor approximation was valid
	for cyclic TS)
Product: 3 hindered rotors were considered (the HO, HOO, and HOOCH2 torsions)

All external symmetry numbers were set equal to one.  The k(T) was calculated from 600 - 2000 K,
in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.468e+06 * (T/1K)^1.554 * exp(-26.636 kcal/mol / RT) cm3/mol/s.
The number appearing in the database has been divided by two to account for the reaction path degeneracy.

Converted to training reaction from rate rule: R5H_SSSD;O_rad_out;Cd_H_out_singleH
""",
)

entry(
    index = 291,
    label = "C2H5O4 <=> C2H5O4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.47e+12, 's^-1'),
        n = -0.24,
        Ea = (117.152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 292,
    label = "C3H7O4 <=> C3H7O4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.76e+08, 's^-1'),
        n = 1.2,
        Ea = (107.529, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 293,
    label = "C3H7O4-3 <=> C3H7O4-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.44e+07, 's^-1'),
        n = 1.6,
        Ea = (116.734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 294,
    label = "C4H9O4 <=> C4H9O4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.75e+08, 's^-1'),
        n = 1.7,
        Ea = (108.784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SSS_O(Cs)Cs;O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 295,
    label = "C3H7O4-5 <=> C3H7O4-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (25900, 's^-1'),
        n = 1.9,
        Ea = (78.6592, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 296,
    label = "C4H9O4-3 <=> C4H9O4-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (10980, 's^-1'),
        n = 2.4,
        Ea = (83.2616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 297,
    label = "C5H11O4 <=> C5H11O4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.5, 's^-1'),
        n = 3.6,
        Ea = (74.0568, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS_OCs(Cs/Cs/Cs);O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 298,
    label = "C4H9O4-5 <=> C4H9O4-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (57.9, 's^-1'),
        n = 2.9,
        Ea = (71.128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_SSSS_OCC;O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 299,
    label = "C5H11O4-3 <=> C5H11O4-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (175, 's^-1'),
        n = 3.1,
        Ea = (73.22, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS_OCC_C;O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 300,
    label = "C4H9O4-7 <=> C4H9O4-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2380, 's^-1'),
        n = 1.7,
        Ea = (69.4544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R6H_SSSSS_OO;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 301,
    label = "C5H11O4-5 <=> C5H11O4-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1256, 's^-1'),
        n = 2.2,
        Ea = (72.8016, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R6H_SSSSS_OO(Cs/Cs)Cs;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 302,
    label = "C5H11O-7 <=> C5H11O-8",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1131, 's^-1'),
        n = 2.2,
        Ea = (64.0152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R6H_SSSSS_OOCCC(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 303,
    label = "C6H13O-7 <=> C6H13O-8",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (762, 's^-1'),
        n = 2.6,
        Ea = (67.7808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R6H_SSSSS_OO(Cs/Cs)C(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 304,
    label = "C5H11O4-7 <=> C5H11O4-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (557, 's^-1'),
        n = 1.8,
        Ea = (69.4544, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R7H_OOCs4;O_rad_out;Cs_H_out_OOH/H
""",
)

entry(
    index = 305,
    label = "C6H13O-9 <=> C6H13O-10",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6000, 's^-1'),
        n = 1.9,
        Ea = (62.3416, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Sandeep's DFT/CBSB7 level of calculations.""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R7H_OOCCCC(Cs/Cs);O_rad_out;Cs_H_out_OOH/Cs
""",
)

entry(
    index = 306,
    label = "C4H9O-3 <=> C4H9O-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.2e+11, 's^-1'),
        n = 0,
        Ea = (31.8402, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of primary H (per H atom)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_CCC;O_rad_out;Cs_H_out_2H
""",
)

entry(
    index = 307,
    label = "C5H11O-3 <=> C5H11O-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8e+10, 's^-1'),
        n = 0,
        Ea = (25.7316, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of secondary H (per H atom)""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_CCC;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 308,
    label = "C4H9O-3 <=> C4H9O-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.2e+11, 's^-1'),
        n = 0,
        Ea = (21.3384, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""[AJ]Atkinson recommendation for 1,5 shifts of tertiary H""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_CCC;O_rad_out;Cs_H_out
""",
)

entry(
    index = 309,
    label = "CH3S <=> CH3S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.0722, 's^-1'),
        n = 4.07,
        Ea = (87.4456, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 310,
    label = "C2H5S <=> C2H5S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (85.5, 's^-1'),
        n = 3.04,
        Ea = (48.6181, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3H_SS_Cs;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 311,
    label = "CH3S2 <=> CH3S2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.000821, 's^-1'),
        n = 4.56,
        Ea = (67.1532, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3H_SS_S;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 312,
    label = "C3H7S <=> C3H7S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.73e+08, 's^-1'),
        n = 0.882,
        Ea = (22.3844, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 313,
    label = "C4H9S <=> C4H9S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.21e+10, 's^-1'),
        n = 0.214,
        Ea = (8.53536, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 2,
    shortDesc = u"""A. G. Vandeputte""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_2H;S_H_out
""",
)

entry(
    index = 314,
    label = "C5H11S <=> C5H11S-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.00228, 's^-1'),
        n = 3.95,
        Ea = (46.7353, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_CsS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 315,
    label = "C6H13S <=> C6H13S-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.0564, 's^-1'),
        n = 3.28,
        Ea = (24.7274, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_SSSS_CsCsS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 316,
    label = "C5H11S-3 <=> C5H11S-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.58e-05, 's^-1'),
        n = 4.5,
        Ea = (49.9151, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeS
""",
)

entry(
    index = 317,
    label = "C6H13S-3 <=> C6H13S-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.1016, 's^-1'),
        n = 3.24,
        Ea = (29.037, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeS
""",
)

entry(
    index = 318,
    label = "CH3OS <=> CH3OS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.99e+11, 's^-1'),
        n = 0.26,
        Ea = (66.9022, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 calc 1dhr""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3H_SS;O_rad_out;S_H_out
""",
)

entry(
    index = 319,
    label = "C3H7O-3 <=> C3H7O-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.71, 's^-1'),
        n = 3.021,
        Ea = (105.562, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;O_H_out
""",
)

entry(
    index = 320,
    label = "C4H7S <=> C4H7S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.61e+11, 's^-1'),
        n = 0.22,
        Ea = (88.2824, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1550, 'K'),
    ),
    rank = 6,
    shortDesc = u"""CAC CBS-QB3 calc, HO approx""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SDS;C_rad_out_H/NonDeC;S_H_out
""",
)

entry(
    index = 321,
    label = "C4H9O-5 <=> C4H9O-6",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (83700, 's^-1'),
        n = 1.97,
        Ea = (96.6504, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS;C_rad_out_H/NonDeO;Cs_H_out_2H
""",
)

entry(
    index = 322,
    label = "C2H5O <=> C2H5O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4500, 's^-1'),
        n = 2.62,
        Ea = (129.286, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;O_H_out
""",
)

entry(
    index = 323,
    label = "C4H9O-2 <=> C4H9O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2960, 's^-1'),
        n = 2.11,
        Ea = (84.0984, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS;C_rad_out_H/NonDeC;O_H_out
""",
)

entry(
    index = 324,
    label = "C4H9O-6 <=> C4H9O-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (304, 's^-1'),
        n = 2.77,
        Ea = (62.3834, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS;C_rad_out_2H;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 325,
    label = "C3H7O-5 <=> C3H7O-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (153000, 's^-1'),
        n = 2.26,
        Ea = (88.9937, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2H_S;O_rad_out;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 326,
    label = "C4H9O <=> C4H9O-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (210000, 's^-1'),
        n = 1.76,
        Ea = (53.8899, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""RQCISD(T)/CBS""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 327,
    label = "C4H9O-7 <=> C4H9O-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (18000, 's^-1'),
        n = 2.287,
        Ea = (84.6842, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Obtained by reversing rate rule 1006""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3H_SS;O_rad_out;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 328,
    label = "CCC[CH2]-1 <=> C4H9-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (150000, 's^-1'),
        n = 2.15,
        Ea = (135.478, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Obtained by reversing rate rule 1010""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 329,
    label = "C:CCCC[CH2] <=> C6H11-23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.000226, 's^-1'),
        n = 4.37,
        Ea = (33.723, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 330,
    label = "C:CCCCC[CH2] <=> C7H13-17",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (92.2, 's^-1'),
        n = 3.21,
        Ea = (27.3215, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 331,
    label = "C:CCCC:C[CH2] <=> C7H11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4800, 's^-1'),
        n = 2.15,
        Ea = (92.4664, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 1D-HR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5H_SMSS;C_rad_out_2H;Cs_H_out_H/Cd
""",
)

entry(
    index = 332,
    label = "C7H13-18 <=> C7H13-19",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (0.502, 's^-1'),
        n = 3.86,
        Ea = (41.6308, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe
""",
)

entry(
    index = 333,
    label = "C:CCCCCC[CH2] <=> C8H15-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (92.2, 's^-1'),
        n = 3.21,
        Ea = (27.3215, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R6H_SSSSS;C_rad_out_2H;Cs_H_out_H/OneDe
""",
)

entry(
    index = 334,
    label = "C7H13-20 <=> C7H13-21",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2e+10, 's^-1'),
        n = 0,
        Ea = (418.4, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""estimate""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SDS;C_rad_out_H/NonDeC;Cs_H_out_H/(NonDeC/Cs)
""",
)

entry(
    index = 335,
    label = "CCCCCC[CH2]-1 <=> C7H15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.36e+10, 's^-1'),
        n = -0.66,
        Ea = (59.7475, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R6H_SSSSS;C_rad_out_single;Cs_H_out_1H
""",
)

entry(
    index = 336,
    label = "C3H5O2 <=> C3H5O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.32e+07, 's^-1'),
        n = 1.69,
        Ea = (159.41, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3H_SS_O;O_rad_out;Cs_H_out_H/Cd
""",
)

entry(
    index = 337,
    label = "C3H5O2-3 <=> C3H5O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (274, 's^-1'),
        n = 3.09,
        Ea = (145.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS_OCs;O_rad_out;Cd_H_out_doubleC
""",
)

entry(
    index = 338,
    label = "C3H7O-7 <=> C3H7O-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.4e-16, 's^-1'),
        n = 7.98,
        Ea = (104.6, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/(NonDeC/O)
""",
)

entry(
    index = 339,
    label = "C3H7O-9 <=> C3H7O-10",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.3e-15, 's^-1'),
        n = 8.11,
        Ea = (117.152, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 340,
    label = "C3H7O-2 <=> C3H7O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.6e-09, 's^-1'),
        n = 5.55,
        Ea = (83.68, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R4H_SSS;C_rad_out_2H;O_H_out
""",
)

entry(
    index = 341,
    label = "C3H7O-11 <=> C3H7O-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.4e-20, 's^-1'),
        n = 9.13,
        Ea = (108.784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 342,
    label = "C3H7O-12 <=> C3H7O-11",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.4e-19, 's^-1'),
        n = 8.84,
        Ea = (125.52, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeO;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 343,
    label = "C3H7O-10 <=> C3H7O-9",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6e-15, 's^-1'),
        n = 8.23,
        Ea = (142.674, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeO;Cs_H_out_2H
""",
)

entry(
    index = 344,
    label = "C4H9O-9 <=> C4H9O-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7e-08, 's^-1'),
        n = 6.3,
        Ea = (82.634, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""SSM CBS-QB3 with 1-dHR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R3H_SS;O_rad_out;Cs_H_out_Cs2
""",
)

entry(
    index = 345,
    label = "CH3O <=> CH3O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (25600, 's^-1'),
        n = 2.36,
        Ea = (138.49, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""Aaron BMK/cbsb7 with 1-dHR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;O_H_out
""",
)

entry(
    index = 346,
    label = "C2H5O-3 <=> C2H5O-4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.41e+13, 's^-1', '+|-', 2),
        n = 0,
        Ea = (188.28, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""
RQCISD(T)/CBS TST calculations with Eckart and 1-dHR corrections from Enoch for 
alpha-hydroxyethyl surface, reference: doi 10.1002/kin.20844

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeO;Cs_H_out_2H
""",
)

entry(
    index = 347,
    label = "C2H5O-4 <=> C2H5O-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.7e+13, 's^-1', '+|-', 2),
        n = -0.1,
        Ea = (158.364, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1800, 'K'),
    ),
    rank = 6,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""
RQCISD(T)/CBS TST calculations with Eckart and 1-dHR corrections from Enoch for 
alpha-hydroxyethyl surface, reference: doi 10.1002/kin.20844

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_H/NonDeO
""",
)

entry(
    index = 348,
    label = "C2H5O-2 <=> C2H5O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.3e+14, 's^-1', '+|-', 2),
        n = -0.27,
        Ea = (113.972, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1800, 'K'),
    ),
    rank = 6,
    shortDesc = u"""ED, RQCISD(T)/CBS TST with Eckart and 1-HR""",
    longDesc = 
u"""
RQCISD(T)/CBS TST calculations with Eckart and 1-dHR corrections from Enoch for 
alpha-hydroxyethyl surface, reference: doi 10.1002/kin.20844

Converted to training reaction from rate rule: R2H_S;O_rad_out;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 349,
    label = "C7H11-2 <=> C7H11-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.52e+08, 's^-1'),
        n = 1.11,
        Ea = (87.4456, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Aaron Vandeputte BMK/6-311G(2d,d,p)""",
    longDesc = 
u"""
BMK/6-311G(2d,d,p) TST Eckart, no HR. calculated for cycC5H5-CH2 -> cycC5H4-CH3

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_CdCd
""",
)

entry(
    index = 351,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.48e+08, 's^-1'),
        n = 1.62,
        Ea = (162.172, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked by Paul Green.

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 352,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.39e+09, 's^-1'),
        n = 0.98,
        Ea = (141.252, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 353,
    label = "CCC[CH2]-2 <=> CCC[CH2]-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.54e+09, 's^-1'),
        n = 0.35,
        Ea = (82.6758, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green.

Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SSS;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 354,
    label = "CCCC[CH2]-2 <=> CCCC[CH2]-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.28e+11, 's^-1'),
        n = -1.05,
        Ea = (49.2038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
[5] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 1998, 114, 149. 
Currans's estimation in his reaction type 5. C7H15

Checked By Paul Green

Degeneracy not recalculated

Converted to training reaction from rate rule: R5H_SSSS;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 355,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.45e+09, 's^-1'),
        n = 1.12,
        Ea = (161.921, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_2H;Cs_H_out_2H
""",
)

entry(
    index = 356,
    label = "C6H13-6 <=> C6H13-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.28e+10, 's^-1'),
        n = 0.97,
        Ea = (161.084, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 357,
    label = "C4H9-6 <=> C4H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.38e+09, 's^-1'),
        n = 0.88,
        Ea = (158.992, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 358,
    label = "C2H3 <=> C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.28e+10, 's^-1'),
        n = 0.86,
        Ea = (191.209, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_D;Cd_rad_out_singleH;Cd_H_out_singleH
""",
)

entry(
    index = 359,
    label = "C4H7-10 <=> C4H7-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.94e+11, 's^-1'),
        n = 0.69,
        Ea = (186.606, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_D;Cd_rad_out_singleNd;Cd_H_out_singleNd
""",
)

entry(
    index = 360,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.25e+11, 's^-1'),
        n = 0.6,
        Ea = (184.096, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 361,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.72e+12, 's^-1'),
        n = 0.37,
        Ea = (174.054, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 362,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.69e+11, 's^-1'),
        n = 0.51,
        Ea = (181.167, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy3;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 363,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.56e+12, 's^-1'),
        n = 0.24,
        Ea = (163.176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 364,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.49e+10, 's^-1'),
        n = 0.79,
        Ea = (178.238, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 365,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.71e+11, 's^-1'),
        n = 0.61,
        Ea = (175.31, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 366,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.72e+12, 's^-1'),
        n = 0.26,
        Ea = (164.013, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 367,
    label = "C[CH2] <=> C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.88e+11, 's^-1'),
        n = 0.51,
        Ea = (174.473, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R2H_S_cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 368,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.76e+08, 's^-1'),
        n = 1.17,
        Ea = (153.553, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_2H;Cs_H_out_2H
""",
)

entry(
    index = 369,
    label = "C5H11-7 <=> C5H11-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.5e+08, 's^-1'),
        n = 1.01,
        Ea = (152.298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 370,
    label = "C7H15-2 <=> C7H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.78e+08, 's^-1'),
        n = 1,
        Ea = (147.695, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 371,
    label = "C:C(C)[CH2] <=> C:C(C)[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.93e+09, 's^-1'),
        n = 1.26,
        Ea = (221.334, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_2H;Cs_H_out_2H
""",
)

entry(
    index = 372,
    label = "C6H11-24 <=> C6H11-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+10, 's^-1'),
        n = 0.91,
        Ea = (205.016, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 373,
    label = "C8H15-8 <=> C8H15-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.76e+09, 's^-1'),
        n = 1.18,
        Ea = (183.259, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_2Cd;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 374,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.62e+10, 's^-1'),
        n = 0.69,
        Ea = (146.858, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 375,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.04e+10, 's^-1'),
        n = 0.71,
        Ea = (146.022, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 376,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.16e+11, 's^-1'),
        n = 0.26,
        Ea = (140.164, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 377,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.63e+08, 's^-1'),
        n = 1.01,
        Ea = (189.954, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 378,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.26e+13, 's^-1'),
        n = 0.26,
        Ea = (134.306, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 379,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.68e+07, 's^-1'),
        n = 1.42,
        Ea = (193.719, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 380,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.9e+10, 's^-1'),
        n = 0.57,
        Ea = (166.523, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 381,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.43e+09, 's^-1'),
        n = 0.93,
        Ea = (160.247, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 382,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.9e+11, 's^-1'),
        n = 0.27,
        Ea = (158.574, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 383,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.59e+08, 's^-1'),
        n = 1.2,
        Ea = (166.105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 384,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.63e+12, 's^-1'),
        n = -0.04,
        Ea = (154.808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 385,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.19e+07, 's^-1'),
        n = 1.55,
        Ea = (167.778, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 386,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.85e+10, 's^-1'),
        n = 0.6,
        Ea = (170.707, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_2H
""",
)

entry(
    index = 387,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+09, 's^-1'),
        n = 0.99,
        Ea = (145.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_2H;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 388,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.67e+11, 's^-1'),
        n = 0.29,
        Ea = (159.829, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 389,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.42e+08, 's^-1'),
        n = 1.14,
        Ea = (150.624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 390,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.42e+11, 's^-1'),
        n = 0.12,
        Ea = (156.482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 391,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.58e+06, 's^-1'),
        n = 1.78,
        Ea = (166.105, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 392,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.64e+09, 's^-1'),
        n = 0.84,
        Ea = (27.196, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 393,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.02e+10, 's^-1'),
        n = 0.56,
        Ea = (178.657, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 394,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.22e+11, 's^-1'),
        n = 0.4,
        Ea = (145.603, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 395,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.34e+09, 's^-1'),
        n = 0.81,
        Ea = (182.422, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 396,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.72e+12, 's^-1'),
        n = -0.04,
        Ea = (139.746, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy3;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 397,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.61e+08, 's^-1'),
        n = 1.26,
        Ea = (175.728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy3;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 398,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.78e+11, 's^-1'),
        n = 0.29,
        Ea = (227.191, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy4;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 399,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.48e+10, 's^-1'),
        n = 0.6,
        Ea = (228.446, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 400,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.66e+12, 's^-1'),
        n = 0,
        Ea = (215.058, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 401,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.55e+11, 's^-1'),
        n = 0.37,
        Ea = (216.313, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy4;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 402,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.36e+11, 's^-1'),
        n = 0.46,
        Ea = (197.485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy5;C_rad_out_H/NonDeC;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 403,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.72e+09, 's^-1'),
        n = 0.86,
        Ea = (197.485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 404,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.1e+12, 's^-1'),
        n = 0.23,
        Ea = (185.77, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 405,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.07e+10, 's^-1'),
        n = 0.62,
        Ea = (181.586, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_13cy5;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 406,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.84e+09, 's^-1'),
        n = 1.05,
        Ea = (171.962, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 407,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.51e+09, 's^-1'),
        n = 0.86,
        Ea = (140.164, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 408,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.04e+09, 's^-1'),
        n = 0.74,
        Ea = (162.339, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 409,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.95e+09, 's^-1'),
        n = 0.88,
        Ea = (146.858, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 410,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.44e+10, 's^-1'),
        n = 0.74,
        Ea = (156.9, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy5;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 411,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.85e+07, 's^-1'),
        n = 1.46,
        Ea = (152.298, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy5;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 412,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.28e+08, 's^-1'),
        n = 1.07,
        Ea = (170.289, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_2H
""",
)

entry(
    index = 413,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.93e+10, 's^-1'),
        n = 0.75,
        Ea = (152.716, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_2H;Cs_H_out_Cs2
""",
)

entry(
    index = 414,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.41e+09, 's^-1'),
        n = 0.77,
        Ea = (162.339, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_H/NonDeC
""",
)

entry(
    index = 415,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.96e+09, 's^-1'),
        n = 0.96,
        Ea = (160.666, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_H/NonDeC;Cs_H_out_Cs2
""",
)

entry(
    index = 416,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.37e+10, 's^-1'),
        n = 0.62,
        Ea = (157.318, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_12cy4;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 417,
    label = "CC[CH2] <=> CC[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.96e+07, 's^-1'),
        n = 1.46,
        Ea = (164.85, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Sumathy B3LYP/CCPVDZ calculations""",
    longDesc = 
u"""
Sumathy B3LYP/CCPVDZ calculations (hindered rotor potential barrier calculations at B3LYP/6-31G(d'))

Degeneracy not recalculated

Converted to training reaction from rate rule: R3H_SS_23cy4;C_rad_out_Cs2;Cs_H_out_Cs2
""",
)

entry(
    index = 418,
    label = "CCCCC[CH2]-2 <=> CCCCC[CH2]-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (10500, 's^-1'),
        n = 2.14,
        Ea = (66.8185, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte BMK/cbsb7 HO""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R6H_SSSSS_bicyclopentane;C_rad_out_H/NonDeC;Cs_H_out_H/OneDe
""",
)

entry(
    index = 419,
    label = "CC:C[CH2] <=> CC:C[CH2]",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (418.4, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""estimate""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R4H_SMS;Y_rad_out;XH_out
""",
)

entry(
    index = 420,
    label = "CCCCC[CH2]-2 <=> CCCCC[CH2]-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.28e+11, 's^-1'),
        n = -1.05,
        Ea = (49.2038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 11,
    shortDesc = u"""Currans's estimation [5] in his reaction type 5.""",
    longDesc = 
u"""
Degeneracy not recalculated

Converted to training reaction from rate rule: R6H_SSSSS;C_rad_out_single;Cs_H_out_2H
""",
)

entry(
    index = 421,
    label = "C7H5 <=> C7H5-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.48e+12, 's^-1'), n=0.539, Ea=(83.31, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

entry(
    index = 422,
    label = "C7H5-3 <=> C7H5-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(5.87e+12, 's^-1'), n=0.286, Ea=(65.14, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

entry(
    index = 423,
    label = "C7H5-5 <=> C7H5-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.67e+12, 's^-1'), n=0.258, Ea=(64.77, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

entry(
    index = 424,
    label = "C7H5-7 <=> C7H5-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.04e+11, 's^-1'), n=0.627, Ea=(58.66, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

entry(
    index = 425,
    label = "C7H5-9 <=> C7H5-10",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.66e+11, 's^-1'), n=0.441, Ea=(25.56, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

entry(
    index = 426,
    label = "C7H5-2 <=> C7H5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.11e+11, 's^-1'), n=0.576, Ea=(40.62, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

entry(
    index = 427,
    label = "C7H5-4 <=> C7H5-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.39e+11, 's^-1'), n=0.459, Ea=(26.24, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

entry(
    index = 428,
    label = "C7H5-6 <=> C7H5-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.11e+11, 's^-1'), n=0.472, Ea=(25.95, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)
entry(
    index = 429,
    label = "C7H5-8 <=> C7H5-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.63e+12, 's^-1'), n=0.388, Ea=(94.61, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

entry(
    index = 430,
    label = "C7H5-10 <=> C7H5-9",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.48e+12, 's^-1'), n=0.239, Ea=(65.78, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Gabriel da Silva', 'Adam J. Trevittb'],
        title = 'Chemically activated reactions on the C7H5 energy surface: propargyl+diacetylene, i-C5H3+acetylene, and n-C5H3+acetylene',
        journal = 'Phys. Chem. Chem. Phys.',
        volume = '13 (19)',
        pages = '8940-8952',
        year = '2011',
    ),
    referenceType = "theory",   
    rank = 5,
    longDesc = 
u"""
All species reported here are studied using the G3SX composite theoretical methodology. This method uses B3LYP/6-31G(2df,p) optimized geometries, vibrational
frequencies and scaled zero point energies, with higher-level wavefunction theory calculations for accurate energies (along with empirical scaling corrections).
1D-Hinder rotor is considered.
""",
)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# API db training reactions go here
entry(
    index = 1001011,
    label = "imipramine_4_oo_r2 <=> imipramine_4_ooh_2_rad_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.90675e+08,'s^-1'), 
                         n=0, 
                         Ea=(57.3664,'kJ/mol'), 
                         T0=(1,'K'), 
                         Tmin=(275,'K'), 
                         Tmax=(350,'K'), 
                         comment="""Fitted to 76 data points; dA = *|/ 1.07057, dn = +|- 0, dEa = +|- 0.175867 kJ/mol"""),
    rank = 1,
    shortDesc = u"""MS-TST rate based on fragment""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)

entry(
    index = 2001011,
    label = "imipramine_4_ooh_2_rad <=> imipramine_4_oo_p",
    degeneracy = 1.0,
    kinetics=Arrhenius(A=(5.64481e+08,'s^-1'), 
                       n=0, 
                       Ea=(26.68,'kJ/mol'), 
                       T0=(1,'K'), 
                       Tmin=(275,'K'), 
                       Tmax=(350,'K'), 
                       comment="""Fitted to 76 data points; dA = *|/ 1.05605, dn = +|- 0, dEa = +|- 0.140658 kJ/mol"""),
    rank = 1,
    shortDesc = u"""MS-TST rate based on fragment, reverse 1001011""",
    longDesc =
"""
Calculated by ACS using multiple-structure local-harmonic 
conventional transition state theory with Eckart tunneling 
(MS-LH-CTST/Eckart).

Optfreq: wb97xd/def2svp in vacuum (freq scale factor: 0.986)
SP: dlpno-ccsd(t)/def2-tzvp normalPNO + Cosmo-RS TZVPD-Fine 
Solvent: H2O:MeOH = 0.7:0.3 (mol%)
""",
)


# entry(
#     index = 1001010,
#     label = "imipramine_4_oo_r5 <=> imipramine_4_ooh_5_rad_p",
#     degeneracy = 6.0,
#     kinetics=Arrhenius(A=(5.55355e+10, 's^-1'), n=0, Ea=(50.4749, 'kJ/mol'),
#                        T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
#     rank = 1,
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# ts1047

# TS1 optimized at wb97xd/def2tzvp
# N      -2.82974200   -0.44078400    0.83542100
# C      -2.44010600    0.14791800   -0.44194400
# C      -1.12266900    0.91151100   -0.33422200
# C       0.00126500    0.05561700    0.20532000
# H      -0.86094800    1.29520800   -1.32229400
# H      -1.24189000    1.75938000    0.34335700
# N       1.26608000    0.74049100    0.39434500
# C       1.76059400    1.52104100   -0.72906700
# C       2.20078300   -0.11291200    1.00235500
# H       2.71308700    1.96765200   -0.44944900
# H       1.06709500    2.32883000   -0.95568400
# H       3.23271200    0.20270200    0.88256900
# H       1.91197200   -1.25471800    0.39072000
# H       1.93840800   -0.38002500    2.02609000
# H      -2.34850200   -1.31861100    0.98290000
# H      -3.81788800   -0.64953700    0.84243800
# H       1.90463800    0.91138700   -1.62695600
# H      -3.21332700    0.85938600   -0.73741600
# H      -0.27347400   -0.37512500    1.17200100
# O       0.22712400   -1.00465300   -0.71670900
# O       1.01910600   -1.97367000   -0.11425800
# H      -2.35839600   -0.59050300   -1.24739900
# """,
# )

# entry(
#     index = 2001010,
#     label = "imipramine_4_ooh_5_rad <=> imipramine_4_oo_p",
#     degeneracy = 1.0,
#     kinetics=Arrhenius(A=(3.39354e+10, 's^-1'), n=0, Ea=(10.9994, 'kJ/mol'),
#                        T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
#     rank = 1,
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# ts1047 rev
# """,
# )

# entry(
#     index = 3001010,
#     label = "imipramine_tail_4_oo_r5 <=> imipramine_tail_4_ooh_5_rad_p",
#     degeneracy = 6.0,
#     kinetics=Arrhenius(A=(5.55355e+10, 's^-1'), n=0, Ea=(50.4749, 'kJ/mol'),
#                        T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
#     rank = 1,
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# ts1047

# TS1 optimized at wb97xd/def2tzvp
# N      -2.82974200   -0.44078400    0.83542100
# C      -2.44010600    0.14791800   -0.44194400
# C      -1.12266900    0.91151100   -0.33422200
# C       0.00126500    0.05561700    0.20532000
# H      -0.86094800    1.29520800   -1.32229400
# H      -1.24189000    1.75938000    0.34335700
# N       1.26608000    0.74049100    0.39434500
# C       1.76059400    1.52104100   -0.72906700
# C       2.20078300   -0.11291200    1.00235500
# H       2.71308700    1.96765200   -0.44944900
# H       1.06709500    2.32883000   -0.95568400
# H       3.23271200    0.20270200    0.88256900
# H       1.91197200   -1.25471800    0.39072000
# H       1.93840800   -0.38002500    2.02609000
# H      -2.34850200   -1.31861100    0.98290000
# H      -3.81788800   -0.64953700    0.84243800
# H       1.90463800    0.91138700   -1.62695600
# H      -3.21332700    0.85938600   -0.73741600
# H      -0.27347400   -0.37512500    1.17200100
# O       0.22712400   -1.00465300   -0.71670900
# O       1.01910600   -1.97367000   -0.11425800
# H      -2.35839600   -0.59050300   -1.24739900
# """,
# )

# entry(
#     index = 4001010,
#     label = "imipramine_tail_4_ooh_5_rad <=> imipramine_tail_4_oo_p",
#     degeneracy = 1.0,
#     kinetics=Arrhenius(A=(3.39354e+10, 's^-1'), n=0, Ea=(10.9994, 'kJ/mol'),
#                        T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
#     rank = 1,
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# ts1047 rev
# """,
# )

# entry(
#     index = 3001011,
#     label = "imipramine_tail_4_oo_r2 <=> imipramine_tail_4_ooh_2_rad_p",
#     degeneracy = 2.0,
#     kinetics=Arrhenius(A=(1.46807e+10,'s^-1'), n=0, Ea=(52.6413,'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     rank = 1,
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water

# ts2008 fragment

# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# C      -2.44221400   -0.43974200   -0.65695200
# N      -1.41331300   -0.48824500    0.36312000
# C      -1.76930400    0.28557300    1.53666900
# C      -0.09828500   -0.29978300   -0.15925400
# O       0.06265300    1.05510800   -0.60436200
# O       0.84600400    1.07967000   -1.78053900
# C       1.01644900   -0.66556200    0.84257600
# C       2.40156800   -0.60241800    0.29338600
# H       2.76877200   -1.41154200   -0.34488100
# N       2.95369600    0.66075500    0.01948300
# H      -2.59250700    0.57544000   -1.07360600
# H      -3.39806400   -0.78709400   -0.23539100
# H      -2.17678600   -1.10969200   -1.48817700
# H      -2.74334200   -0.06125700    1.91411300
# H      -1.04085300    0.13604200    2.34494100
# H      -1.84953600    1.37284400    1.33728400
# H       0.00725100   -0.93128700   -1.05665900
# H       1.74698800    1.12447700   -1.39769000
# H       0.94361100    0.01459200    1.70964200
# H       0.81128400   -1.68232700    1.21067700
# H       3.95170200    0.64862700   -0.16986200
# H       2.73640500    1.36338800    0.72346800
# """,
# )

# entry(
#     index = 4001011,
#     label = "imipramine_tail_4_ooh_2_rad <=> imipramine_tail_4_oo_p",
#     degeneracy=1.0,
#     kinetics=Arrhenius(A=(3.46239e+10, 's^-1'), n=0, Ea=(22.2652, 'kJ/mol'),
#                        T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
#     rank=1,
#     longDesc=
#     u"""
#     dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
#     solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
#     ts2008 rev
#     """,
# )

entry(
    index = 1001012,
    label = "imipramine_5_rad_r1 <=> imipramine_1_rad_p",
    degeneracy = 4.0,
    kinetics=Arrhenius(A=(32980, 's^-1'), n=0, Ea=(44.6304, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    rank = 1,
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1022

This TS restricts 5 rotors, the A factor, originally A=(8.01453e+06, 's^-1'),
was divided by a factor of 3^5 = 243

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.38070300   -0.24956800    0.11972200
C       0.70709000   -1.18047800    0.38654100
C      -1.65446000   -0.80105700   -0.13833900
C       1.68022700   -0.66402600    1.44452100
H       0.24035900   -2.09002300    0.76062400
H       1.26305400   -1.46828300   -0.51424400
C      -0.08605700    1.05853000   -0.30707600
C      -1.77756100   -1.91160900   -0.96898600
C      -2.78987100   -0.27790300    0.50364600
C       0.98925100    0.02206400    2.61721700
H       2.27557400   -1.51450700    1.78598000
H       2.38377600    0.05107400    1.01149500
C       1.04123100    1.27012800   -1.11023800
C      -0.87071300    2.16006700    0.06562000
C      -3.00770900   -2.52028300   -1.16949300
H      -0.89540300   -2.30724100   -1.45729400
C      -2.66778000    0.82840200    1.45440300
C      -4.02011000   -0.90658800    0.28463900
N      -0.10373200   -0.74219000    3.19155000
H       0.57958800    0.97190200    2.27329700
H       1.73887300    0.26290500    3.38610800
C       1.39151100    2.53162700   -1.55369300
H       1.64938600    0.42318000   -1.39835400
C      -2.04763800    2.13574800    1.01830200
C      -0.51246200    3.41709300   -0.42214100
C      -4.13609500   -2.01324200   -0.53998400
H      -3.08204600   -3.38417700   -1.81826400
H      -3.60907600    1.02169600    1.96853200
H      -1.91535300    0.38543200    2.50267200
H      -4.89769600   -0.51676700    0.78813800
C      -1.19982800    0.04066400    3.60012300
C       0.31667500   -1.79780100    4.08922300
C       0.60151500    3.62043200   -1.21653600
H       2.27142300    2.65824500   -2.17243200
H      -1.74866400    2.68796600    1.91700600
H      -2.83586500    2.74530400    0.56283500
H      -1.12483000    4.26681400   -0.13928300
H      -5.10202700   -2.48027400   -0.68745700
H      -1.90624500   -0.51204400    4.21673100
H      -0.96386300    1.02516100    4.02229300
H      -0.54135400   -2.40301100    4.38412300
H       0.79365700   -1.40682200    5.00148300
H       1.03215400   -2.45228800    3.58759700
H       0.85208800    4.61545700   -1.56189000
""",
)

entry(
    index = 2001012,
    label = "imipramine_1_rad_r5 <=> imipramine_5_rad_p",
    degeneracy = 6.0,
    kinetics=Arrhenius(A=(99750, 's^-1'), n=0, Ea=(85.8771, 'kJ/mol'),
                       T0=(1, 'K'), Tmin=(275, 'K'), Tmax=(350, 'K')),
    rank = 1,
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1022 rev

This TS restricts 5 rotors, the A factor, originally A=(2.42394e+07, 's^-1'),
was divided by a factor of 3^5 = 243

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.38070300   -0.24956800    0.11972200
C       0.70709000   -1.18047800    0.38654100
C      -1.65446000   -0.80105700   -0.13833900
C       1.68022700   -0.66402600    1.44452100
H       0.24035900   -2.09002300    0.76062400
H       1.26305400   -1.46828300   -0.51424400
C      -0.08605700    1.05853000   -0.30707600
C      -1.77756100   -1.91160900   -0.96898600
C      -2.78987100   -0.27790300    0.50364600
C       0.98925100    0.02206400    2.61721700
H       2.27557400   -1.51450700    1.78598000
H       2.38377600    0.05107400    1.01149500
C       1.04123100    1.27012800   -1.11023800
C      -0.87071300    2.16006700    0.06562000
C      -3.00770900   -2.52028300   -1.16949300
H      -0.89540300   -2.30724100   -1.45729400
C      -2.66778000    0.82840200    1.45440300
C      -4.02011000   -0.90658800    0.28463900
N      -0.10373200   -0.74219000    3.19155000
H       0.57958800    0.97190200    2.27329700
H       1.73887300    0.26290500    3.38610800
C       1.39151100    2.53162700   -1.55369300
H       1.64938600    0.42318000   -1.39835400
C      -2.04763800    2.13574800    1.01830200
C      -0.51246200    3.41709300   -0.42214100
C      -4.13609500   -2.01324200   -0.53998400
H      -3.08204600   -3.38417700   -1.81826400
H      -3.60907600    1.02169600    1.96853200
H      -1.91535300    0.38543200    2.50267200
H      -4.89769600   -0.51676700    0.78813800
C      -1.19982800    0.04066400    3.60012300
C       0.31667500   -1.79780100    4.08922300
C       0.60151500    3.62043200   -1.21653600
H       2.27142300    2.65824500   -2.17243200
H      -1.74866400    2.68796600    1.91700600
H      -2.83586500    2.74530400    0.56283500
H      -1.12483000    4.26681400   -0.13928300
H      -5.10202700   -2.48027400   -0.68745700
H      -1.90624500   -0.51204400    4.21673100
H      -0.96386300    1.02516100    4.02229300
H      -0.54135400   -2.40301100    4.38412300
H       0.79365700   -1.40682200    5.00148300
H       1.03215400   -2.45228800    3.58759700
H       0.85208800    4.61545700   -1.56189000
""",
)

entry(
    index = 1001013,
    label = "imipramine_5_rad_r2 <=> imipramine_2_rad_p",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.46807e+08,'s^-1'), n=0, Ea=(48.7508,'kJ/mol'),
                         T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    rank = 1,
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1023

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.31000500   -0.21198800    0.31644400
C       0.81520800   -1.07594900    0.47504900
C      -1.51164300   -0.82642400   -0.13385500
C       1.87332800   -0.65914300    1.47462300
H       0.45272000   -2.08012900    0.69172600
H       1.53714600   -1.30051400   -0.56708800
C      -0.11966600    1.14959700   -0.04417800
C      -1.49037400   -1.79342200   -1.13310000
C      -2.71547200   -0.45972300    0.46838200
C       3.15974700   -1.43809700    1.23380700
H       2.08309900    0.40892000    1.39961000
H       1.52343300   -0.84979300    2.49360100
C       1.03336400    1.50059000   -0.75424900
C      -1.05249600    2.14903600    0.27737600
C      -2.67073600   -2.39276000   -1.54642100
H      -0.54828600   -2.07257700   -1.58934400
C      -2.69259500    0.57052000    1.55442100
C      -3.89080600   -1.05837000    0.03123600
N       3.69257400   -1.20198500   -0.10636200
H       2.97702200   -2.51545600    1.39363500
H       3.91246600   -1.13087900    1.96084000
C       1.29057000    2.80672800   -1.12502400
H       1.73897600    0.72969400   -1.02746000
C      -2.35996900    1.95987200    1.02197500
C      -0.77261800    3.45589700   -0.12314700
C      -3.87552000   -2.02111800   -0.96811300
H      -2.64743300   -3.14418900   -2.32580000
H      -3.66823200    0.61385900    2.04000000
H      -1.96293700    0.28144600    2.31429100
H      -4.82875900   -0.77583100    0.49570200
C       2.79961800   -1.73070700   -1.09775700
C       5.02107400   -1.78483300   -0.24210700
C       0.37840500    3.80086500   -0.80721800
H       2.19691200    3.04022600   -1.66975200
H      -2.37320000    2.66721700    1.85479300
H      -3.16783300    2.27029900    0.35247300
H      -1.49224700    4.22780300    0.12777100
H      -4.80052800   -2.48339900   -1.28924400
H       2.96074700   -1.33646200   -2.09906800
H       2.67143100   -2.82211900   -1.07745400
H       5.40663400   -1.59704000   -1.24502800
H       5.01250300   -2.87392600   -0.07815000
H       5.70493500   -1.33463600    0.48015200
H       0.55859300    4.83041200   -1.08926400
""",
)

entry(
    index = 2001013,
    label = "imipramine_2_rad_r5 <=> imipramine_5_rad_p",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(5.26516e+08,'s^-1'), n=0, Ea=(66.6256,'kJ/mol'),
                         T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
    rank = 1,
    longDesc =
u"""
dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
ts1023 rev

TS external symmetry: 1, TS optical isomers: 2

Optimized TS geometry:
N      -0.31000500   -0.21198800    0.31644400
C       0.81520800   -1.07594900    0.47504900
C      -1.51164300   -0.82642400   -0.13385500
C       1.87332800   -0.65914300    1.47462300
H       0.45272000   -2.08012900    0.69172600
H       1.53714600   -1.30051400   -0.56708800
C      -0.11966600    1.14959700   -0.04417800
C      -1.49037400   -1.79342200   -1.13310000
C      -2.71547200   -0.45972300    0.46838200
C       3.15974700   -1.43809700    1.23380700
H       2.08309900    0.40892000    1.39961000
H       1.52343300   -0.84979300    2.49360100
C       1.03336400    1.50059000   -0.75424900
C      -1.05249600    2.14903600    0.27737600
C      -2.67073600   -2.39276000   -1.54642100
H      -0.54828600   -2.07257700   -1.58934400
C      -2.69259500    0.57052000    1.55442100
C      -3.89080600   -1.05837000    0.03123600
N       3.69257400   -1.20198500   -0.10636200
H       2.97702200   -2.51545600    1.39363500
H       3.91246600   -1.13087900    1.96084000
C       1.29057000    2.80672800   -1.12502400
H       1.73897600    0.72969400   -1.02746000
C      -2.35996900    1.95987200    1.02197500
C      -0.77261800    3.45589700   -0.12314700
C      -3.87552000   -2.02111800   -0.96811300
H      -2.64743300   -3.14418900   -2.32580000
H      -3.66823200    0.61385900    2.04000000
H      -1.96293700    0.28144600    2.31429100
H      -4.82875900   -0.77583100    0.49570200
C       2.79961800   -1.73070700   -1.09775700
C       5.02107400   -1.78483300   -0.24210700
C       0.37840500    3.80086500   -0.80721800
H       2.19691200    3.04022600   -1.66975200
H      -2.37320000    2.66721700    1.85479300
H      -3.16783300    2.27029900    0.35247300
H      -1.49224700    4.22780300    0.12777100
H      -4.80052800   -2.48339900   -1.28924400
H       2.96074700   -1.33646200   -2.09906800
H       2.67143100   -2.82211900   -1.07745400
H       5.40663400   -1.59704000   -1.24502800
H       5.01250300   -2.87392600   -0.07815000
H       5.70493500   -1.33463600    0.48015200
H       0.55859300    4.83041200   -1.08926400
""",
)

entry(
    index = 9009000,
    label = "NC(O[O])CC(OO)N <=> OO[C](CC(OO)N)N",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e8, 's^-1'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    rank = 2,
    longDesc = 
u"""
W.H. Green: The C-H being attacked here is very reactive, because both the OOH and the N bonded to that C can line up
their lone pairs with the C-H to stabilize the TS and also the radical being formed. If RMG says that this reaction is
slower than some other reaction, I think it is mis-estimating this fast reaction (or wildly mis-estimating the competing
reaction). If you don’t have a computed value for this reaction yet, I suggest just putting in a fast k value
(say 1e8 s^-1) for now so RMG will follow this dominant pathway correctly.
RMG would normally estimate this type of reaction in the reverse direction, which is highly unreliable.
""",
)

# entry(
#     index = 1001014,
#     label = "imipramine_5_oo_r4 <=> imipramine_5_ooh_4_rad_p",
#     degeneracy = 2.0,
#     kinetics = Arrhenius(A=(6.3936e+09,'s^-1'), n=0, Ea=(45.6853,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     rank = 1,
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# based on fragment ts1046

# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# N      -2.97691900   -0.20418800    0.88345800
# C      -2.41889300    0.07848800   -0.43419500
# C      -1.13904700    0.90418600   -0.34550800
# C      -0.06262900    0.19172500    0.42639800
# H      -0.80405200    1.11995200   -1.36258000
# H      -1.36620500    1.86065200    0.13890400
# N       1.21191400    0.77938800    0.51991100
# C       1.70309300    1.48088500   -0.65178800
# C       2.18384200   -0.10508700    1.14783600
# H       2.69094700    1.88619500   -0.43749300
# H       1.04769900    2.31770900   -0.88645900
# H       3.13450200   -0.00589700    0.61557800
# H       2.31700200    0.13099900    2.20650000
# H      -2.49255800   -0.97383000    1.32563400
# H      -3.94614200   -0.47819200    0.80797700
# H       1.77607800    0.82362500   -1.52795000
# H      -3.15655500    0.65772300   -0.99238600
# H      -0.38568200   -0.16170700    1.40789000
# H      -2.21549300   -0.82814400   -1.02073000
# H       0.28724500   -0.95878900   -0.09434400
# O       1.75460800   -1.44726100    1.16225100
# O       1.26626200   -1.79167800   -0.09015600
# """,
# )

# entry(
#     index = 2001014,
#     label = "imipramine_5_ooh_4_rad <=> imipramine_5_oo_p",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(2.54381e+10,'s^-1'), n=0, Ea=(36.7946,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     rank = 1,
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# ts1046 rev
# """,
# )

# entry(
#     index = 3001014,
#     label = "imipramine_tail_5_oo_r4 <=> imipramine_tail_5_ooh_4_rad_p",
#     degeneracy = 2.0,
#     kinetics = Arrhenius(A=(6.3936e+09,'s^-1'), n=0, Ea=(45.6853,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     rank = 1,
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# based on fragment ts1046

# TS external symmetry: 1, TS optical isomers: 2

# Optimized TS geometry:
# N      -2.97691900   -0.20418800    0.88345800
# C      -2.41889300    0.07848800   -0.43419500
# C      -1.13904700    0.90418600   -0.34550800
# C      -0.06262900    0.19172500    0.42639800
# H      -0.80405200    1.11995200   -1.36258000
# H      -1.36620500    1.86065200    0.13890400
# N       1.21191400    0.77938800    0.51991100
# C       1.70309300    1.48088500   -0.65178800
# C       2.18384200   -0.10508700    1.14783600
# H       2.69094700    1.88619500   -0.43749300
# H       1.04769900    2.31770900   -0.88645900
# H       3.13450200   -0.00589700    0.61557800
# H       2.31700200    0.13099900    2.20650000
# H      -2.49255800   -0.97383000    1.32563400
# H      -3.94614200   -0.47819200    0.80797700
# H       1.77607800    0.82362500   -1.52795000
# H      -3.15655500    0.65772300   -0.99238600
# H      -0.38568200   -0.16170700    1.40789000
# H      -2.21549300   -0.82814400   -1.02073000
# H       0.28724500   -0.95878900   -0.09434400
# O       1.75460800   -1.44726100    1.16225100
# O       1.26626200   -1.79167800   -0.09015600
# """,
# )

# entry(
#     index = 4001014,
#     label = "imipramine_tail_5_ooh_4_rad <=> imipramine_tail_5_oo_p",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(2.54381e+10,'s^-1'), n=0, Ea=(36.7946,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(275,'K'), Tmax=(350,'K')),
#     rank = 1,
#     longDesc =
# u"""
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# ts1046 rev
# """,
# )

# entry(
#     index = 1001016,
#     label = "imipramine_tail_2_ooh_4_oo_r2 <=> imipramine_tail_2_ooh_4_ooh_2_rad",
#     degeneracy = 1.0,
#     kinetics = Arrhenius(A=(1.5081e+08,'s^-1'), n=0, Ea=(67.4495,'kJ/mol'),
#                          T0=(1,'K'), Tmin=(200,'K'), Tmax=(495,'K')),
#     rank = 1,
#     longDesc =
# u"""
# This is a fake reaction. products are unstable so forward rate calcualted using '
#                                    'reactant as products. Fitted to 60 data points; dA = *|/ 1.62624, dn = +|- 0, '
#                                    'dEa = +|- 1.26739 kJ/mol
                                   
# dlpno-ccsd(t)/def2-tzvp/def2-tzvp/c//wb97xd/def2tzvp
# solvation: SMD water, sp was corrected using APFD/6-311+G(2d,p) SMD water
# ts1038 forward only

# TS geom
#  N                  2.51752000   -1.07335300   -1.05889900
#  C                  1.51453700   -0.47971400   -0.28901200
#  C                  0.15956600   -1.13100800   -0.28745500
#  C                 -0.98287800   -0.11707700   -0.55433900
#  H                  0.11586200   -1.89937400   -1.06110000
#  H                 -0.00224800   -1.61576900    0.67755800
#  N                 -2.20835100   -0.49660300    0.04572600
#  C                 -3.36558800    0.15224000   -0.53792900
#  C                 -2.24894800   -0.45253700    1.49624700
#  H                 -4.27231500   -0.32399400   -0.15887900
#  H                 -3.35011800    0.03386000   -1.62268900
#  H                 -3.11261400   -1.02241100    1.84578700
#  H                 -2.32837700    0.57124400    1.88501200
#  H                 -1.35338100   -0.90033300    1.92488700
#  H                  2.56009300   -2.08286300   -0.98646400
#  H                  3.42359900   -0.65795000   -0.89194600
#  H                 -1.13043800   -0.03219200   -1.63536700
#  H                 -3.41755600    1.22528300   -0.30539000
#  O                 -0.58359700    1.19063800   -0.09804800
#  O                  0.43090900    1.63287600   -0.93751900
#  H                  1.19923900    0.70282200   -0.80556700
#  O                  1.80871200   -0.13775100    1.04256800
#  O                  2.91687200    0.75794600    1.03187500
#  H                  2.46077200    1.61028200    0.95028200
# """,
# )

# entry(
#     index = 10023,
#     label = "imipramine_2_OOH_4_OO <=> imipramine_2_OOH_4_OOH_5_rad",
#     degeneracy = 6.0,
#     kinetics = Arrhenius(A=(5.0738e+10, 's^-1'), n=0, Ea=(43.3198, 'kJ/mol'), T0=(1,'K'), Tmin=(275,'K'),
#                          Tmax=(350,'K')),
#     rank=1,
#     shortDesc = u"""""",
#     longDesc =
# u"""
# TS1057
# dlpno-ccsd(T)/def2tzvp//wb97xd/def2tzvp with APFD SMD water for solvation sp correction
#
# Optimized TS geometry:
# O      -0.08336300   -0.90551700    3.12781100
# O      -0.84456100   -0.13681400    2.21753300
# C      -0.48128900   -0.45566200    0.87344300
# N       0.84602600   -0.02369200    0.51611600
# C       1.05526500    1.37779800    0.37548700
# C       0.99581600    2.19890700    1.49677600
# C       1.12341800    3.57296200    1.37579600
# C       1.32634400    4.13817200    0.12802800
# C       1.39686600    3.32196600   -0.98922800
# C       1.25135300    1.94477200   -0.88393700
# C       1.37874300    1.04981400   -2.07631400
# C       2.65677700    0.22324000   -1.98842000
# C       2.68351900   -0.87253800   -0.94407100
# C       1.83619000   -0.98397300    0.16981400
# C       1.95927300   -2.11172700    0.99082200
# C       2.89070200   -3.09923200    0.74516400
# C       3.75583600   -2.97492500   -0.32893700
# C       3.63718900   -1.87114400   -1.14743900
# C      -1.57994600    0.21912200    0.05820100
# C      -2.91369400   -0.48529200    0.23040900
# N      -4.02014700    0.22088400   -0.37998700
# C      -5.33050000   -0.21133500    0.08327100
# C      -3.88897700    0.33683600   -1.77370100
# O      -2.91446800   -1.81007800   -0.30614500
# O      -2.59992800   -1.77260900   -1.65974900
# H       0.74376600   -0.40765200    3.18096300
# H      -0.52635300   -1.53600300    0.73729100
# H       0.83151700    1.76050000    2.47093400
# H       1.07092000    4.19745100    2.25827800
# H       1.43219900    5.21048400    0.02413200
# H       1.55870700    3.76007400   -1.96747900
# H       0.51906100    0.37962500   -2.15563600
# H       1.40332100    1.65158800   -2.98588800
# H       3.49667200    0.90472700   -1.81796700
# H       2.83891900   -0.24880900   -2.95616500
# H       1.30371500   -2.20941400    1.84405400
# H       2.94621900   -3.95605500    1.40450000
# H       4.50224700   -3.73122600   -0.53351500
# H       4.29246500   -1.77793300   -2.00667500
# H      -1.68607500    1.26037500    0.36464600
# H      -1.28164000    0.19469400   -0.98643200
# H      -3.12992700   -0.63556700    1.28711400
# H      -6.08224000    0.49121500   -0.27422400
# H      -5.58276600   -1.21642300   -0.26987400
# H      -5.34736600   -0.20807000    1.17250600
# H      -3.34458100   -0.84863100   -2.04468400
# H      -4.83102100    0.50761700   -2.28581300
# H      -3.09566400    1.01038900   -2.09313600
# """,
# )


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# end of API db training reactions

entry(
    index = 431,
    label = "C6H5 <=> C6H5-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.208e+12, 's^-1'), n=1.135, Ea=(109.513, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    longDesc =
u"""
Calculated by Jim at the CBS-QB3 level
""",
)

