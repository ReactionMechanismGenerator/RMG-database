#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
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
        authors = ["'J. W. Allen'", "'C. F. Goldsmith'", "'W. H. Green'"],
        title = 'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "'Phys. Chem. Chem. Phys.'",
        volume = "'14'",
        pages = """'1131-1155'""",
        year = "'2012'",
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
        authors = ["'E. E. Dames'", "'W. H. Green'"],
        title = 'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = "'Intl. J. Chem. Kin.'",
        volume = "'48(9)'",
        pages = """'544-555'""",
        year = "'2016'",
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
        authors = ["'E. E. Dames'", "'W. H. Green'"],
        title = 'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = "'Intl. J. Chem. Kin.'",
        volume = "'48(9)'",
        pages = """'544-555'""",
        year = "'2016'",
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
        authors = ["'Krasnoukhov, V. S.'", "'Porfiriev, D. P.'", "'Zavershinskiy, I. P.'", "'Azyazov, V. N.'", "'Mebel, A. M.'"],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'121 (48)'",
        pages = """'9191-9200'""",
        year = "'2017'",
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
        authors = ["'Krasnoukhov, V. S.'", "'Porfiriev, D. P.'", "'Zavershinskiy, I. P.'", "'Azyazov, V. N.'", "'Mebel, A. M.'"],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'121 (48)'",
        pages = """'9191-9200'""",
        year = "'2017'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Kun Wang'", "'Stephanie M. Villano'", "'Anthony M. Dean'"],
        title = 'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "'Chemphyschem'",
        volume = "'16'",
        pages = """'2635-2645'""",
        year = "'2015'",
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
        authors = ["'Ribeiro, J. M.'", "'Mebel, A. M.'"],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (22)'",
        pages = """'14543-14554'""",
        year = "'2017'",
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
        authors = ["'Ribeiro, J. M.'", "'Mebel, A. M.'"],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (22)'",
        pages = """'14543-14554'""",
        year = "'2017'",
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
        authors = ["'Ribeiro, J. M.'", "'Mebel, A. M.'"],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (22)'",
        pages = """'14543-14554'""",
        year = "'2017'",
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
        authors = ["'Ribeiro, J. M.'", "'Mebel, A. M.'"],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (22)'",
        pages = """'14543-14554'""",
        year = "'2017'",
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
        authors = ["'Ribeiro, J. M.'", "'Mebel, A. M.'"],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (22)'",
        pages = """'14543-14554'""",
        year = "'2017'",
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
        authors = ["'Ribeiro, J. M.'", "'Mebel, A. M.'"],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (22)'",
        pages = """'14543-14554'""",
        year = "'2017'",
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
        authors = ["'Ribeiro, J. M.'", "'Mebel, A. M.'"],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (22)'",
        pages = """'14543-14554'""",
        year = "'2017'",
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
        authors = ["'Ribeiro, J. M.'", "'Mebel, A. M.'"],
        title = 'Reaction mechanism and product branching ratios of the CH + C3H4 reactions: a theoretical study',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'19 (22)'",
        pages = """'14543-14554'""",
        year = "'2017'",
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
        authors = ["'da Silva, G.'", "'Cole, J. A.'", "'Bozzelli, J. W.'"],
        title = 'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'114 (6)'",
        pages = """'2275-2283'""",
        year = "'2010'",
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
        authors = ["'da Silva, G.'", "'Cole, J. A.'", "'Bozzelli, J. W.'"],
        title = 'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'114 (6)'",
        pages = """'2275-2283'""",
        year = "'2010'",
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
        authors = ["'da Silva, G.'", "'Cole, J. A.'", "'Bozzelli, J. W.'"],
        title = 'Kinetics of the Cyclopentadienyl + Acetylene, Fulvenallene + H, and 1-Ethynylcyclopentadiene + H Reactions',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'114 (6)'",
        pages = """'2275-2283'""",
        year = "'2010'",
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
    label = "C7H5 <=> C7H5-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.11e+11, 's^-1'), n=0.576, Ea=(40.62, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    longDesc = 
u"""
Training reaction from kinetics library: 2011_Silva_C7H5_highP
Original entry: W4 <=> W5
""",
)

entry(
    index = 130,
    label = "C7H5-3 <=> C7H5-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.39e+11, 's^-1'), n=0.459, Ea=(26.24, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    longDesc = 
u"""
Training reaction from kinetics library: 2011_Silva_C7H5_highP
Original entry: W8 <=> W9
""",
)

entry(
    index = 131,
    label = "C7H5-5 <=> C7H5-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4.11e+11, 's^-1'), n=0.472, Ea=(25.95, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    longDesc = 
u"""
Training reaction from kinetics library: 2011_Silva_C7H5_highP
Original entry: W12 <=> W9
""",
)

entry(
    index = 132,
    label = "C7H5-7 <=> C7H5-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.63e+12, 's^-1'), n=0.388, Ea=(94.61, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    longDesc = 
u"""
Training reaction from kinetics library: 2011_Silva_C7H5_highP
Original entry: W9 <=> W20
""",
)

entry(
    index = 133,
    label = "C7H5-9 <=> C7H5-10",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(8.48e+12, 's^-1'), n=0.239, Ea=(65.78, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    longDesc = 
u"""
Training reaction from kinetics library: 2011_Silva_C7H5_highP
Original entry: W9 <=> W26
""",
)

entry(
    index = 134,
    label = "C7H5-11 <=> C7H5-12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(7.13e+12, 's^-1'), n=0.254, Ea=(68.75, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    longDesc = 
u"""
Training reaction from kinetics library: 2011_Silva_C7H5_highP
Original entry: W9 <=> W13
""",
)

