#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "C2H2 + C4H9 <=> C6H11",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.01e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (5.31, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (373, 'K'),
        Tmax = (493, 'K'),
    ),
    reference = Article(
        authors = ["Garcia Dominguez, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part IX. The addition of methyl, ethyl, isopropyl, and t-butyl radicals to acetylene and the isomerization of alkenyl radicals',
        journal = "J. Chem. Soc.",
        pages = """940-944""",
        year = "1962",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1962GAR/TRO940-944:1",
    ),
    longDesc = 
u"""
Dominguez et al. Data derived from fitting to a complex mechanism.
Pressure 0.01-0.32 atm. Excitation : direct photolysis, analysis : GC. 
C2H2 + Tert-C4H9 --> (CH3)3CCH=CH

Was in the rules database with rank=4. Richard moved to the training database and checked with NIST database. NIST squib: 1962GAR/TRO940-944
A=5.01e+10 cm^3/(mol*s) is the full rate; NB the degeneracy=2 so the per-site rate is half this.
""",
)

entry(
    index = 2,
    label = "C2H3O3 <=> C2H2O + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.3e+16, 's^-1', '*|/', 2.51189),
        n = -1,
        Ea = (29.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["J. W. Allen", "C. F. Goldsmith", "W. H. Green"],
        title = u'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "???",
        pages = """???-???""",
        year = "2011 (accepted)",
    ),
    referenceType = "theory",
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
""",
)

entry(
    index = 3,
    label = "CH2O + C3H5O <=> C4H7O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (54.3214, 's^-1', '*|/', 1.1507),
        n = 3.00879,
        Ea = (6.589, 'kcal/mol', '+|-', 0.024),
        T0 = (1, 'K'),
    ),
    reference = "",
    referenceType = "theory",
    shortDesc = u"""nyee TST calculations at CBS-QB3 level with hindered rotors level""",
    longDesc =
u"""
Quantum chemistry calculations at the CBS-QB3 level with hindered rotors
using Gaussian 03. High-pressure-limit rate coefficient computed
using Cantherm. One of the rotors had coupling and did not converge back to the
same initial geometry. It was forced to go back by editing the scan log.
""",
)


entry(
    index = 4,
    label = "allyl + ethene <=> pent1en5yl",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.70E+03, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.700,
        Ea = (11.3, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Wang, K.", "Villano, S.M.", "Dean, A.M."],
        title = u'Reactions of allylic radicals that impact molecular weight growth kinetics',
        journal = "PCCP",
        pages = """6255-6273""",
        year = "2015",
        url = "http://pubs.rsc.org/en/content/articlepdf/2015/CP/C4CP05308G",
    ),
    longDesc = 
u"""
Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
Table 4
CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions around single bonds, tunneling with Eckart potentials.
""",
)

entry(
    index = 5,
    label = "allyl + propene_1 <=> hex1en5yl",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.56E+03, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.530,
        Ea = (11.0, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Wang, K.", "Villano, S.M.", "Dean, A.M."],
        title = u'Reactions of allylic radicals that impact molecular weight growth kinetics',
        journal = "PCCP",
        pages = """6255-6273""",
        year = "2015",
        url = "http://pubs.rsc.org/en/content/articlepdf/2015/CP/C4CP05308G",
    ),
    longDesc = 
u"""
Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
Table 4
CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions around single bonds, tunneling with Eckart potentials.
""",
)

entry(
    index = 6,
    label = "allyl + propene_2 <=> methylpentenyl",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.37E+02, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.840,
        Ea = (12.2, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Wang, K.", "Villano, S.M.", "Dean, A.M."],
        title = u'Reactions of allylic radicals that impact molecular weight growth kinetics',
        journal = "PCCP",
        pages = """6255-6273""",
        year = "2015",
        url = "http://pubs.rsc.org/en/content/articlepdf/2015/CP/C4CP05308G",
    ),
    longDesc = 
u"""
Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
Table 4
CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions around single bonds, tunneling with Eckart potentials.
""",
)

entry(
    index = 7,
    label = "allyl + butene1_1 <=> hept1en5yl",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.31E+03, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.620,
        Ea = (10.9, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Wang, K.", "Villano, S.M.", "Dean, A.M."],
        title = u'Reactions of allylic radicals that impact molecular weight growth kinetics',
        journal = "PCCP",
        pages = """6255-6273""",
        year = "2015",
        url = "http://pubs.rsc.org/en/content/articlepdf/2015/CP/C4CP05308G",
    ),
    longDesc = 
u"""
Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
Table 4
CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions around single bonds, tunneling with Eckart potentials.
""",
)

entry(
    index = 8,
    label = "allyl + butene1_2 <=> C7H13",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.22E+01, 'cm^3/(mol*s)', '*|/', 2),
        n = 3.060,
        Ea = (11.7, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Wang, K.", "Villano, S.M.", "Dean, A.M."],
        title = u'Reactions of allylic radicals that impact molecular weight growth kinetics',
        journal = "PCCP",
        pages = """6255-6273""",
        year = "2015",
        url = "http://pubs.rsc.org/en/content/articlepdf/2015/CP/C4CP05308G",
    ),
    longDesc = 
u"""
Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
Table 4
CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions around single bonds, tunneling with Eckart potentials.
""",
)

entry(
    index = 9,
    label = "allyl + butene2 <=> C7H13_2",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (9.53E+02, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.700,
        Ea = (11.2, 'kcal/mol', '+|-', 1),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ["Wang, K.", "Villano, S.M.", "Dean, A.M."],
        title = u'Reactions of allylic radicals that impact molecular weight growth kinetics',
        journal = "PCCP",
        pages = """6255-6273""",
        year = "2015",
        url = "http://pubs.rsc.org/en/content/articlepdf/2015/CP/C4CP05308G",
    ),
    longDesc = 
u"""
Wang et al. Phys. Chem. Chem. Phys., 2015, 17, 6255--6273
Table 4
CBS-QB3, high-P limit, atomization method for energies, hindered rotors for torsions around single bonds, tunneling with Eckart potentials.
""",
)

entry(
    index = 10,
    label = "C7H8 + H <=> C7H9",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.36e+08, 'cm^3/(mol*s)'),
        n = 1.56,
        Ea = (0.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: vinylCPD + H <=> addA
""",
)

entry(
    index = 11,
    label = "C7H8-2 + H <=> C7H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.01e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (2.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: vinylCPD + H <=> addB
""",
)

entry(
    index = 12,
    label = "C7H8-3 + H <=> C7H9-3",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.3e+09, 'cm^3/(mol*s)'),
        n = 1.48,
        Ea = (0.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: vinylCPD + H <=> addC
""",
)

entry(
    index = 13,
    label = "C7H8-4 + H <=> C7H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.41e+08, 'cm^3/(mol*s)'),
        n = 1.57,
        Ea = (1.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: vinylCPD + H <=> addD
""",
)

entry(
    index = 14,
    label = "C7H9-5 <=> ethene + C5H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.87e+11, 's^-1'), n=0.68, Ea=(13.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> CPDyl + C2H4
""",
)

entry(
    index = 15,
    label = "C7H9-6 <=> C6H6 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.06e+11, 's^-1'), n=1.15, Ea=(39.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product7 <=> FULVENE + CH3
""",
)

entry(
    index = 16,
    label = "C7H9-7 <=> C5H6 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+12, 's^-1'), n=0.81, Ea=(33.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addD <=> CPD + C2H3
""",
)

entry(
    index = 17,
    label = "C7H9-8 <=> C6H6-2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.07e+11, 's^-1'), n=0.83, Ea=(22.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product2 <=> BENZENE + CH3
""",
)

entry(
    index = 18,
    label = "C7H9-9 <=> C7H8-5 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.03e+09, 's^-1'), n=1.36, Ea=(26.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product2 <=> TOLUENE + H
""",
)

entry(
    index = 19,
    label = "C7H9-10 <=> C7H8-6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.01e+09, 's^-1'), n=1.23, Ea=(28.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product5 <=> product13 + H
""",
)

entry(
    index = 20,
    label = "C7H9-11 <=> C7H8-7 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product12 <=> product14 + H
""",
)

entry(
    index = 21,
    label = "C7H9-12 <=> C7H8-8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.58e+10, 's^-1'), n=1.38, Ea=(48.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product4 <=> product15 + H
""",
)

entry(
    index = 22,
    label = "C7H9-13 <=> C5H6-2 + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.89e+12, 's^-1'), n=0.87, Ea=(45, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addC <=> CPD + C2H3
""",
)

entry(
    index = 23,
    label = "C6H6-3 + CH3 <=> C7H9-14",
    degeneracy = 1,
    kinetics = Arrhenius(A=(263, 'cm^3/(mol*s)'), n=2.89, Ea=(6.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + CH3 <=> product18
""",
)

entry(
    index = 24,
    label = "C7H9-15 <=> C7H8-9 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product24 <=> product13 + H
""",
)

entry(
    index = 25,
    label = "C6H6-4 + CH3 <=> C7H9-16",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2790, 'cm^3/(mol*s)'), n=2.91, Ea=(1.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + CH3 <=> product32
""",
)

entry(
    index = 26,
    label = "C6H6-5 + CH3 <=> C7H9-17",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2470, 'cm^3/(mol*s)'), n=2.88, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + CH3 <=> product31
""",
)

entry(
    index = 27,
    label = "C7H9-18 <=> C7H8-10 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.03e+10, 's^-1'), n=1.22, Ea=(40.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product37 <=> product13 + H
""",
)

entry(
    index = 28,
    label = "C2H2 + C5H5 <=> C7H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(25500, 'cm^3/(mol*s)'), n=2.27, Ea=(10.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: CPDyl + ethyne <=> product44
""",
)

entry(
    index = 29,
    label = "C7H6 + H <=> C7H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.1e+09, 'cm^3/(mol*s)'),
        n = 1.43,
        Ea = (4.13, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: FA + H <=> vinylCPDyl
""",
)

