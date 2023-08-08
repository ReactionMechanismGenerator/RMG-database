#!/usr/bin/env python
# encoding: utf-8

name = "Intra_ene_reaction/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.39e+07, 's^-1'), n=1.58, Ea=(21.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product21
""",
)

entry(
    index = 1,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.06e+07, 's^-1'), n=1.74, Ea=(24.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product21 <=> product22
""",
)

entry(
    index = 2,
    label = "C9H8 <=> C9H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.2e+09, 's^-1'), n=0.96, Ea=(6.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt22 <=> INDENE
""",
)

entry(
    index = 3,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.08398e+09, 's^-1'),
        n = 0.809263,
        Ea = (163.807, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
u"""
Taken from entry: II <=> VIII
""",
)

entry(
    index = 4,
    label = "C6H6-3 <=> C6H6-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.16475e+09, 's^-1'),
        n = 0.737748,
        Ea = (218.723, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P_reverse""",
    longDesc = 
u"""
Taken from entry: VIII <=> II
""",
)

entry(
    index = 5,
    label = "C6H8 <=> C6H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(3.201e+11, 's^-1'), n=0.6, Ea=(23.767, 'kcal/mol'), T0=(1, 'K')),
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
    index = 6,
    label = "C6H8-3 <=> C6H8-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.432e+11, 's^-1'), n=0.625, Ea=(26.957, 'kcal/mol'), T0=(1, 'K')),
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
    index = 7,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2.27e+10, 's^-1'), n=0.581, Ea=(16.586, 'kcal/mol'), T0=(1, 'K')),
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
    index = 8,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.46e+08, 's^-1'), n=1.46, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: adducta <=> adductb
""",
)

entry(
    index = 9,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.46e+06, 's^-1'), n=2.01, Ea=(27.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: adductb <=> adductc
""",
)

entry(
    index = 10,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.12e+08, 's^-1'), n=1.64, Ea=(22.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: adductd <=> pdt15
""",
)

entry(
    index = 11,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.28e+08, 's^-1'), n=1.55, Ea=(18.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt16
""",
)

entry(
    index = 12,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.18e+08, 's^-1'), n=1.8, Ea=(21.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt15 <=> pdt39
""",
)

entry(
    index = 13,
    label = "C10H9-5 <=> C10H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.429e+08, 's^-1'), n=1.267, Ea=(24.384, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W8 <=> W102
""",
)

entry(
    index = 14,
    label = "C10H9-7 <=> C10H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.548e+09, 's^-1'), n=0.934, Ea=(9.114, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W107 <=> W108
""",
)

entry(
    index = 15,
    label = "C7H7 <=> C7H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.01e+10, 's^-1'), n=0.97, Ea=(19.17, 'kcal/mol'), T0=(1, 'K')),
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
    index = 16,
    label = "C7H7-3 <=> C7H7-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.21e+08, 's^-1'), n=1.38, Ea=(15.29, 'kcal/mol'), T0=(1, 'K')),
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
    index = 17,
    label = "C7H7-5 <=> C7H7-6",
    degeneracy = 14.0,
    kinetics = Arrhenius(A=(5.5e+08, 's^-1'), n=1.56, Ea=(62.12, 'kcal/mol'), T0=(1, 'K')),
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
    index = 18,
    label = "C6H5O2 <=> C6H5O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.125e+09, 's^-1'), n=0.991, Ea=(10.983, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['I. V. Tokmakov', 'G. Kim', 'V. V. Kislov', 'A. M. Mebel', 'M. C. Lin'],
        title = 'The Reaction of Phenyl Radical with Molecular Oxygen: A G2M Study of the Potential Energy Surface',
        journal = 'J. Phys. Chem. A',
        volume = '109 (27)',
        pages = '6114-6127',
        year = '2005',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Using CanTherm to calculate TST rates from the PES at the G2M(MP2)//B3LYP/6-311++G** level of theory
The rates have been validated by the rates reported in Proceedings of the Combustion Institute 35 (2015) 1861–1869,
where only 1500, 2000, 2500 K rates were reported.
""",
)

entry(
    index = 19,
    label = "C6H5O2-2 <=> C6H5O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(9.66e+08, 's^-1'), n=1.162, Ea=(44.283, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['I. V. Tokmakov', 'G. Kim', 'V. V. Kislov', 'A. M. Mebel', 'M. C. Lin'],
        title = 'The Reaction of Phenyl Radical with Molecular Oxygen: A G2M Study of the Potential Energy Surface',
        journal = 'J. Phys. Chem. A',
        volume = '109 (27)',
        pages = '6114-6127',
        year = '2005',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Using CanTherm to calculate TST rates from the PES at the G2M(MP2)//B3LYP/6-311++G** level of theory
The rates have been validated by the rates reported in Proceedings of the Combustion Institute 35 (2015) 1861–1869,
where only 1500, 2000, 2500 K rates were reported.
""",
)

entry(
    index = 20,
    label = "C16H11 <=> C16H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.63e+09, 's^-1'), n=1.089, Ea=(23.05, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    longDesc = 
u"""
Training reaction from kinetics library: Frenklach2019_ProcCombInst_HighP_Phenanthryl
Original entry: W2 <=> W5
""",
)

