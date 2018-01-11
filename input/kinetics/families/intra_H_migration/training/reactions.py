#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "C2H3O3 <=> C2H3O3-2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.3e+09, 's^-1', '*|/', 2.51189),
        n = 0.75,
        Ea = (23.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["J. W. Allen", "C. F. Goldsmith", "W. H. Green"],
        title = u'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "14",
        pages = """1131-1155""",
        year = "2012",
    ),
    referenceType = "theory",
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
    index = 2,
    label = "S1C4 <=> S1C4b",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.775e+09, 's^-1', '*|/', 3.0),
        n = 0.686,
        Ea = (6.774, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["E. E. Dames", "W. H. Green"],
        title = u'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = "Intl. J. Chem. Kin.",
        volume = "48(9)",
        pages = """544-555""",
        year = "2016",
    ),
    referenceType = "theory",
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
    label = "S2C4 <=> S2C4b",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.540e+04, 's^-1', '*|/', 3.0),
        n = 2.338,
        Ea = (7.127, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["E. E. Dames", "W. H. Green"],
        title = u'THE EFFECT OF ALCOHOL AND CARBONYL FUNCTIONAL GROUPS ON THE COMPETITION BETWEEN UNIMOLECULAR DECOMPOSITION AND ISOMERIZATION IN C 1 -C 5 ALKOXY RADICALS',
        journal = "Intl. J. Chem. Kin.",
        volume = "48(9)",
        pages = """544-555""",
        year = "2016",
    ),
    referenceType = "theory",
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
    index = 4,
    label = "C4H7O2 <=> C4H7O2b",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (6.358e+01, 's^-1', '*|/', 3.66),
        n = 2.81162,
        Ea = (8.231, 'kcal/mol', '+|-', 1.00),
        T0 = (1, 'K'),
    ),
    reference = None,
    referenceType = "theory",
    shortDesc = u"""TST calculations at M08SO/MG3S level by edames""",
    longDesc = 
u"""
Quantum chemistry calculations at the M08SO/MG3S* level using Qchem. High-pressure-limit rate coefficient computed using Cantherm with 1D hindered rotor treatment for all relevant rotors. (*A computational grid with 75 radial points and 434 angular points per radial point was used in the calculations for all species)
""",
)

entry(
    index = 5,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.97e+06, 's^-1'), n=1.8, Ea=(37.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addA <=> addB
""",
)

entry(
    index = 6,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.81e+07, 's^-1'), n=1.72, Ea=(44.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addC <=> addD
""",
)

entry(
    index = 7,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.37e+06, 's^-1'), n=1.6, Ea=(25.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> product7
""",
)

entry(
    index = 8,
    label = "C7H9-7 <=> C7H9-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.88e+09, 's^-1'), n=1, Ea=(21.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addA <=> product7
""",
)

entry(
    index = 9,
    label = "C7H9-9 <=> C7H9-10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+08, 's^-1'), n=1.39, Ea=(24.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addD <=> product10
""",
)

entry(
    index = 10,
    label = "C7H9-11 <=> C7H9-12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.11e+09, 's^-1'), n=1.34, Ea=(47.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product4 <=> product9
""",
)

entry(
    index = 11,
    label = "C7H9-13 <=> C7H9-14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.03e+06, 's^-1'), n=1.96, Ea=(50.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product2 <=> product5
""",
)

entry(
    index = 12,
    label = "C7H9-15 <=> C7H9-16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(367000, 's^-1'), n=2.24, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product17 <=> product6
""",
)

entry(
    index = 13,
    label = "C7H9-17 <=> C7H9-18",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.9e+10, 's^-1'), n=0.87, Ea=(34.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product29 <=> product23
""",
)

entry(
    index = 14,
    label = "C7H9-19 <=> C7H9-20",
    degeneracy = 1,
    kinetics = Arrhenius(A=(285000, 's^-1'), n=2.15, Ea=(43.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product31 <=> product35
""",
)

entry(
    index = 15,
    label = "C7H9-21 <=> C7H9-22",
    degeneracy = 1,
    kinetics = Arrhenius(A=(671000, 's^-1'), n=2.07, Ea=(48.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product32 <=> product38
""",
)

entry(
    index = 16,
    label = "C7H7 <=> C7H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.41e+08, 's^-1'), n=1.52, Ea=(38.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product34 <=> product46
""",
)

entry(
    index = 17,
    label = "C7H7-3 <=> C7H7-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product44 <=> vinylCPDyl
""",
)

entry(
    index = 18,
    label = "C7H7-5 <=> C7H7-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product44 <=> product41
""",
)

entry(
    index = 19,
    label = "C7H7-7 <=> C7H7-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.08e+06, 's^-1'), n=1.99, Ea=(25.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: vinylCPDyl <=> product41
""",
)



entry(
    index = 20,
    label = "C5H5 <=> C5H5-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.15e+10, 's^-1'), n=0.98, Ea=(26.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_24 <=> CPDyl
""",
)

entry(
    index = 21,
    label = "C6H7 <=> C6H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+10, 's^-1'), n=1.01, Ea=(27.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_26 <=> meCPDyl
""",
)

entry(
    index = 22,
    label = "C6H7-3 <=> C6H7-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.8e+10, 's^-1'), n=1.01, Ea=(28.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_28 <=> meCPDyl
""",
)

entry(
    index = 23,
    label = "C6H7-5 <=> C6H7-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.24e+09, 's^-1'), n=1.12, Ea=(39.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_30 <=> prod_33
""",
)



entry(
    index = 24,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.107, 's^-1'), n=3.67, Ea=(29.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt20
""",
)

entry(
    index = 25,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(250000, 's^-1'), n=1.95, Ea=(24, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt18 <=> pdt25
""",
)

entry(
    index = 26,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+08, 's^-1'), n=1.01, Ea=(26.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt16 <=> pdt20
""",
)

entry(
    index = 27,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.67e+09, 's^-1'), n=1.14, Ea=(22.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt28 <=> pdt29
""",
)

entry(
    index = 28,
    label = "C10H11-9 <=> C10H11-10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.46e+07, 's^-1'), n=1.66, Ea=(31.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt28 <=> pdt23
""",
)

entry(
    index = 29,
    label = "C10H11-11 <=> C10H11-12",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.83e+08, 's^-1'), n=1.45, Ea=(31.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt10bis <=> pdt37
""",
)

entry(
    index = 30,
    label = "C10H11-13 <=> C10H11-14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.36e+06, 's^-1'), n=1.7, Ea=(31.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: adductd <=> pdt55
""",
)

entry(
    index = 31,
    label = "C10H11-15 <=> C10H11-16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.78e+06, 's^-1'), n=1.75, Ea=(25.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt15 <=> pdt55
""",
)

entry(
    index = 32,
    label = "C10H11-17 <=> C10H11-18",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.04e+07, 's^-1'), n=1.61, Ea=(27.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt58 <=> pdt20
""",
)

entry(
    index = 33,
    label = "C6H7-7 <=> C6H7-8",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.00218, 's^-1'), n=4.91, Ea=(40.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: C5H4CH3 <=> C5H5CH2-1
""",
)

entry(
    index = 34,
    label = "C:CC[CH2] <=> C:C[CH]C",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.72E+06, 's^-1'),
        n = 1.99,
        Ea = (27.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 35,
    label = "C:CCC[CH2] <=> C:C[CH]CC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.5E+04, 's^-1'),
        n = 2.28,
        Ea = (28.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 36,
    label = "C:CCCC[CH2] <=> C:C[CH]CCC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.22E+04, 's^-1'),
        n = 1.93,
        Ea = (13.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 37,
    label = "C:CCCCC[CH2] <=> C:C[CH]CCCC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.54E+04, 's^-1'),
        n = 1.87,
        Ea = (7.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 38,
    label = "C:CCCCCC[CH2] <=> C:C[CH]CCCCC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.16E+03, 's^-1'),
        n = 1.94,
        Ea = (6.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 39,
    label = "C:C(C)C[CH2] <=> C:C([CH2])CC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.24E+04, 's^-1'),
        n = 2.04,
        Ea = (19.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 40,
    label = "C:C(C)CC[CH2] <=> C:C([CH2])CCC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (6.90E+03, 's^-1'),
        n = 1.98,
        Ea = (10.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 41,
    label = "C:C(C)CCC[CH2] <=> C:C([CH2])CCCC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.12E+02, 's^-1'),
        n = 2.10,
        Ea = (10.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 42,
    label = "CC:CC[CH2] <=> [CH2]C:CCC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.21E+05, 's^-1'),
        n = 1.90,
        Ea = (13.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 43,
    label = "CC:CCC[CH2] <=> [CH2]C:CCCC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.01E+03, 's^-1'),
        n = 1.94,
        Ea = (13.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 44,
    label = "C:C([CH2])CC:C <=> C:C(C)[CH]C:C",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.08E+04, 's^-1'),
        n = 2.49,
        Ea = (43.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 45,
    label = "C:CCC:C[CH2] <=> C:C[CH]C:CC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.56E+05, 's^-1'),
        n = 2.00,
        Ea = (28.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 46,
    label = "C:C([CH2])C:CC <=> C:C(C)C:C[CH2]",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.44E+06, 's^-1'),
        n = 1.64,
        Ea = (24.0, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 47,
    label = "C:C(C)[CH2] <=> C:C([CH2])C",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.355E+05, 's^-1'),
        n = 2.44,
        Ea = (51.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 48,
    label = "C:C([CH2])CCC:C <=> C:C(C)C[CH]C:C",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.032E+05, 's^-1'),
        n = 2.04,
        Ea = (25.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 49,
    label = "C:C([CH2])CCCC:C <=> C:C(C)CC[CH]C:C",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.884E+04, 's^-1'),
        n = 1.93,
        Ea = (16.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 50,
    label = "C:C([CH2])CCCCC:C <=> C:C(C)CCC[CH]C:C",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.136E+02, 's^-1'),
        n = 2.07,
        Ea = (15.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 51,
    label = "CC:C[CH2] <=> [CH2]C:CC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.00E+05, 's^-1'),
        n = 1.81,
        Ea = (35.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 52,
    label = "C:CCCC:C[CH2] <=> C:C[CH]CC:CC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.52E+05, 's^-1'),
        n = 1.85,
        Ea = (21.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 53,
    label = "C:CCCCC:C[CH2] <=> C:C[CH]CCC:CC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.094E+04, 's^-1'),
        n = 1.94,
        Ea = (20.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 54,
    label = "C:C([CH2])CC:CC <=> C:C(C)CC:C[CH2]",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (6.33E+04, 's^-1'),
        n = 1.92,
        Ea = (21.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 55,
    label = "C[CH2] <=> [CH2]C",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (7.05E+06, 's^-1'),
        n = 1.81,
        Ea = (37.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 56,
    label = "CCC[CH2]-1 <=> CC[CH]C",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.48E+07, 's^-1'),
        n = 1.57,
        Ea = (35.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 57,
    label = "CC[CH2] <=> [CH2]CC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (8.85E+04, 's^-1'),
        n = 2.17,
        Ea = (35.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 58,
    label = "CCCC[CH2] <=> CC[CH]CC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.064E+06, 's^-1'),
        n = 1.93,
        Ea = (33.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 59,
    label = "CCC[CH2]-2 <=> [CH2]CCC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.14E+05, 's^-1'),
        n = 1.74,
        Ea = (19.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 60,
    label = "CCCCCCC[CH2]-1 <=> CCCC[CH]CCC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.54E+05, 's^-1'),
        n = 1.63,
        Ea = (17.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 61,
    label = "CCCC[CH2]-2 <=> [CH2]CCCC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (6.885E+04, 's^-1'),
        n = 1.68,
        Ea = (12.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 62,
    label = "CCCCC[CH2]-1 <=> C[CH]CCCC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.62E+05, 's^-1'),
        n = 1.62,
        Ea = (11.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 63,
    label = "CCCCC[CH2]-2 <=> [CH2]CCCCC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.69E+03, 's^-1'),
        n = 1.79,
        Ea = (11.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 64,
    label = "CCCCCC[CH2]-1 <=> C[CH]CCCCC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.58E+04, 's^-1'),
        n = 1.67,
        Ea = (10.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 65,
    label = "CCCCCC[CH2]-2 <=> [CH2]CCCCCC",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (6.42E+01, 's^-1'),
        n = 2.10,
        Ea = (15.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
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
    index = 66,
    label = "CCCCCCC[CH2]-2 <=> C[CH]CCCCCC",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (10.62E+02, 's^-1'),
        n = 1.81,
        Ea = (13.2, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    reference = Article(
        authors = ["Kun Wang", "Stephanie M. Villano", "Anthony M. Dean"],
        title = u'The Impact of Resonance Stabilization on the Intramolecular H-atom Shift Reactions of Hydrocarbon Radicals',
        journal = "Chemphyschem",
        volume = "16",
        pages = """2635-2645""",
        year = "2015",
    ),
    referenceType = "theory",
    shortDesc = u"""TST calculations at CBS-QB3//B3LYP/6-31G(d) level with 1-D hindered rotor corrections""",
    longDesc = 
u"""
Quantum chemistry calculations at the CBS-QB3//B3LYP/6-31G(d) level
using Gaussian 03 and Gaussian 09.
1,7 H-Shift Primary-Secondary
Reported A factor from article is multiplied by degeneracy because article A-factors are normalized
""",
)
