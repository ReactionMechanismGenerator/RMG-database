#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C2H2 + C4H9 <=> C6H11",
    degeneracy = 2.0,
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
    index = 1,
    label = "C2H3O3 <=> C2H2O + HO2",
    degeneracy = 1.0,
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
    index = 2,
    label = "CH2O + C3H5O <=> C4H7O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (54.3214, 's^-1', '*|/', 1.1507),
        n = 3.00879,
        Ea = (6.589, 'kcal/mol', '+|-', 0.024),
        T0 = (1, 'K'),
    ),
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
    index = 3,
    label = "allyl + C2H4 <=> pent1en5yl",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (2700, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.7,
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
    index = 4,
    label = "allyl + propene_1 <=> hex1en5yl",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1560, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.53,
        Ea = (11, 'kcal/mol', '+|-', 1),
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
    label = "allyl + propene_2 <=> methylpentenyl",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (137, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.84,
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
    index = 6,
    label = "allyl + butene1_1 <=> hept1en5yl",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1310, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.62,
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
    index = 7,
    label = "allyl + butene1_2 <=> C7H13",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (12.2, 'cm^3/(mol*s)', '*|/', 2),
        n = 3.06,
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
    index = 8,
    label = "allyl + butene2 <=> C7H13_2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (953, 'cm^3/(mol*s)', '*|/', 2),
        n = 2.7,
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
    index = 9,
    label = "C7H8 + H <=> C7H9",
    degeneracy = 1.0,
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
    index = 10,
    label = "C7H8-2 + H <=> C7H9-2",
    degeneracy = 1.0,
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
    index = 11,
    label = "C7H8-3 + H <=> C7H9-3",
    degeneracy = 2.0,
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
    index = 12,
    label = "C7H8-4 + H <=> C7H9-4",
    degeneracy = 2.0,
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
    index = 13,
    label = "C7H9-5 <=> C2H4 + C5H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.87e+11, 's^-1'), n=0.68, Ea=(13.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addB <=> CPDyl + C2H4
""",
)

entry(
    index = 14,
    label = "C7H9-6 <=> C6H6 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.06e+11, 's^-1'), n=1.15, Ea=(39.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product7 <=> FULVENE + CH3
""",
)

entry(
    index = 15,
    label = "C7H9-7 <=> C5H6 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.5e+12, 's^-1'), n=0.81, Ea=(33.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addD <=> CPD + C2H3
""",
)

entry(
    index = 16,
    label = "C7H9-8 <=> C6H6-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.07e+11, 's^-1'), n=0.83, Ea=(22.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product2 <=> BENZENE + CH3
""",
)

entry(
    index = 17,
    label = "C7H9-9 <=> C7H8-5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.03e+09, 's^-1'), n=1.36, Ea=(26.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product2 <=> TOLUENE + H
""",
)

entry(
    index = 18,
    label = "C7H9-10 <=> C7H8-6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.01e+09, 's^-1'), n=1.23, Ea=(28.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product5 <=> product13 + H
""",
)

entry(
    index = 19,
    label = "C7H9-11 <=> C7H8-7 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product12 <=> product14 + H
""",
)

entry(
    index = 20,
    label = "C7H9-12 <=> C7H8-8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.58e+10, 's^-1'), n=1.38, Ea=(48.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product4 <=> product15 + H
""",
)

entry(
    index = 21,
    label = "C7H9-13 <=> C5H6-2 + C2H3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.89e+12, 's^-1'), n=0.87, Ea=(45, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: addC <=> CPD + C2H3
""",
)

entry(
    index = 22,
    label = "C6H6-3 + CH3 <=> C7H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(263, 'cm^3/(mol*s)'), n=2.89, Ea=(6.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + CH3 <=> product18
""",
)

entry(
    index = 23,
    label = "C7H9-15 <=> C7H8-9 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.47e+10, 's^-1'), n=1.17, Ea=(41.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product24 <=> product13 + H
""",
)

entry(
    index = 24,
    label = "C6H6-4 + CH3 <=> C7H9-16",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2790, 'cm^3/(mol*s)'), n=2.91, Ea=(1.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + CH3 <=> product32
""",
)

entry(
    index = 25,
    label = "C6H6-5 + CH3 <=> C7H9-17",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(2470, 'cm^3/(mol*s)'), n=2.88, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + CH3 <=> product31
""",
)

entry(
    index = 26,
    label = "C7H9-18 <=> C7H8-10 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.03e+10, 's^-1'), n=1.22, Ea=(40.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product37 <=> product13 + H
""",
)

entry(
    index = 27,
    label = "C2H2 + C5H5 <=> C7H7",
    degeneracy = 10.0,
    kinetics = Arrhenius(A=(25500, 'cm^3/(mol*s)'), n=2.27, Ea=(10.2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: CPDyl + ethyne <=> product44
""",
)

entry(
    index = 28,
    label = "C7H6 + H <=> C7H7-2",
    degeneracy = 1.0,
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

entry(
    index = 29,
    label = "C3H4 + allyl <=> C6H9",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(42, 'cm^3/(mol*s)'), n=3.27, Ea=(11, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: aC3H5 + C3H4a <=> prod_1
""",
)

entry(
    index = 30,
    label = "C6H9-2 <=> C6H8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.93e+09, 's^-1'), n=1.27, Ea=(31, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_2 <=> prod_3 + H
""",
)

entry(
    index = 31,
    label = "C3H4 + C4H7 <=> C7H11",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(18.6, 'cm^3/(mol*s)'), n=3, Ea=(9.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4a + iC4H7 <=> prod_6
""",
)

entry(
    index = 32,
    label = "C7H11-2 <=> C7H10 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.37e+08, 's^-1'), n=1.3, Ea=(29.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_4 <=> prod_5 + H
""",
)

entry(
    index = 33,
    label = "C3H4-2 + allyl <=> C6H9-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (267000, 'cm^3/(mol*s)'),
        n = 2.15,
        Ea = (12.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4p + aC3H5 <=> prod_7
""",
)

entry(
    index = 34,
    label = "C6H9-4 <=> C6H8-2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.99e+10, 's^-1'), n=1, Ea=(32.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_8 <=> prod_9 + H
""",
)

entry(
    index = 35,
    label = "C3H4-2 + C4H7 <=> C7H11-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(121, 'cm^3/(mol*s)'), n=2.9, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4p + iC4H7 <=> prod_10
""",
)

entry(
    index = 36,
    label = "C7H11-4 <=> C7H10-2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.77e+09, 's^-1'), n=1.4, Ea=(32, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_11 <=> prod_12 + H
""",
)

entry(
    index = 37,
    label = "C3H4 + C4H5 <=> C7H9-19",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(128, 'cm^3/(mol*s)'), n=3.05, Ea=(7.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4a + BD2YL <=> prod_13
""",
)

entry(
    index = 38,
    label = "C7H9-20 <=> C7H8-11 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4e+10, 's^-1'), n=1.27, Ea=(44.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_14 <=> prod_15 + H
""",
)

entry(
    index = 39,
    label = "C3H4-2 + C4H5 <=> C7H9-21",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1900, 'cm^3/(mol*s)'), n=2.92, Ea=(8.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4p + BD2YL <=> prod_16
""",
)

entry(
    index = 40,
    label = "C7H9-22 <=> C7H8-12 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.47e+10, 's^-1'), n=1.22, Ea=(45.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_17 <=> prod_18 + H
""",
)

entry(
    index = 41,
    label = "C3H4-3 + allyl <=> C6H9-5",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(3960, 'cm^3/(mol*s)'), n=2.65, Ea=(11.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: aC3H5 + C3H4a <=> prod_19
""",
)

entry(
    index = 42,
    label = "C3H4-3 + C4H7 <=> C7H11-5",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(37, 'cm^3/(mol*s)'), n=2.89, Ea=(9.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4a + iC4H7 <=> prod_20
""",
)

entry(
    index = 43,
    label = "C2H2 + allyl <=> C5H7",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (238000, 'cm^3/(mol*s)'),
        n = 2.26,
        Ea = (12.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: aC3H5 + C2H2 <=> prod_21
""",
)

entry(
    index = 44,
    label = "C5H7-2 <=> C5H6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.19e+09, 's^-1'), n=1.37, Ea=(31.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_22 <=> CPD + H
""",
)

entry(
    index = 45,
    label = "C2H2 + C3H3 <=> C5H5-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.27e+06, 'cm^3/(mol*s)'),
        n = 2.15,
        Ea = (10.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H3 + C2H2 <=> prod_23
""",
)

entry(
    index = 46,
    label = "C3H4-2 + C3H3 <=> C6H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7040, 'cm^3/(mol*s)'), n=2.87, Ea=(9.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H3 + C3H4p <=> prod_25
""",
)

entry(
    index = 47,
    label = "C3H4-4 + C3H3 <=> C6H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(285, 'cm^3/(mol*s)'), n=2.93, Ea=(11.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H3 + C3H4p <=> prod_27
""",
)

entry(
    index = 48,
    label = "C3H4-3 + C3H3 <=> C6H7-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(850, 'cm^3/(mol*s)'), n=2.81, Ea=(8.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H3 + C3H4a <=> prod_29
""",
)

entry(
    index = 49,
    label = "C5H6 + C5H5 <=> C10H11",
    degeneracy = 10.0,
    kinetics = Arrhenius(A=(288, 'cm^3/(mol*s)'), n=2.8, Ea=(8.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: CPD + CPDyl <=> adducte
""",
)

entry(
    index = 50,
    label = "C5H6-2 + C5H5 <=> C10H11-2",
    degeneracy = 10.0,
    kinetics = Arrhenius(A=(288, 'cm^3/(mol*s)'), n=2.74, Ea=(3.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: CPD + CPDyl <=> adductd
""",
)

entry(
    index = 51,
    label = "C10H10 + H <=> C10H11-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.09e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (2.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt11 + H <=> pdt10bis
""",
)

entry(
    index = 52,
    label = "C10H11-4 <=> C6H6-2 + C4H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.14e+12, 's^-1'), n=0.52, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt12 <=> benzene + butadieneyl
""",
)

entry(
    index = 53,
    label = "C10H10-2 + H <=> C10H11-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.81e+06, 'cm^3/(mol*s)'),
        n = 1.95,
        Ea = (5.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt13 + H <=> pdt12
""",
)

entry(
    index = 54,
    label = "C9H8 + CH3 <=> C10H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2480, 'cm^3/(mol*s)'), n=2.89, Ea=(-0.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt22 + CH3 <=> pdt21
""",
)

entry(
    index = 55,
    label = "C10H11-7 <=> C10H10-3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=1.41, Ea=(38.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt23 <=> pdt30 + H
""",
)

entry(
    index = 56,
    label = "C10H10-4 + H <=> C10H11-8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.09e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (2.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt26 + H <=> pdt19
""",
)

entry(
    index = 57,
    label = "C10H10-5 + H <=> C10H11-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.26e+08, 'cm^3/(mol*s)'),
        n = 1.63,
        Ea = (1.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt31 + H <=> pdt8
""",
)

entry(
    index = 58,
    label = "C10H11-10 <=> C9H8-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.72e+10, 's^-1'), n=1.33, Ea=(51.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt32 <=> pdt22 + CH3
""",
)

entry(
    index = 59,
    label = "C10H10-6 + H <=> C10H11-11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.93e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt31 + H <=> pdt29
""",
)

entry(
    index = 60,
    label = "C10H10-7 + H <=> C10H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.93e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt30 + H <=> pdt29
""",
)

entry(
    index = 61,
    label = "C10H10-8 + H <=> C10H11-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.93e+08, 'cm^3/(mol*s)'),
        n = 1.6,
        Ea = (1.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt35 + H <=> pdt29
""",
)

entry(
    index = 62,
    label = "C10H10-9 + H <=> C10H11-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.61e+07, 'cm^3/(mol*s)'),
        n = 1.71,
        Ea = (4.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt38 + H <=> pdt37
""",
)

entry(
    index = 63,
    label = "C6H6 + H <=> C6H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.69e+09, 'cm^3/(mol*s)'),
        n = 1.46,
        Ea = (-0.7, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + H <=> C5H4CH3
""",
)

entry(
    index = 64,
    label = "C6H6-3 + H <=> C6H7-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.31e+08, 'cm^3/(mol*s)'), n=1.76, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + H <=> C5H5CH2-1
""",
)

entry(
    index = 65,
    label = "C6H6-5 + H <=> C6H7-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.26e+09, 'cm^3/(mol*s)'),
        n = 1.48,
        Ea = (0.4, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + H <=> C5H5CH2-3
""",
)

entry(
    index = 66,
    label = "C6H6-4 + H <=> C6H7-7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.52e+09, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.9, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + H <=> C5H5CH2-2
""",
)

entry(
    index = 67,
    label = "C6H7-8 <=> C6H6-2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.84e+09, 's^-1'), n=1.3, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: cyC6H7 <=> benzene + H
""",
)

entry(
    index = 68,
    label = "C10H8 + H <=> C10H9",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.63e+09, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (0.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: biCPD3ene + H <=> adducta
""",
)

entry(
    index = 69,
    label = "C10H8-2 + H <=> C10H9-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.61e+10, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: biCPD3ene + H <=> adductb
""",
)

entry(
    index = 70,
    label = "C10H8-3 + H <=> C10H9-3",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.61e+10, 'cm^3/(mol*s)'),
        n = 1.52,
        Ea = (0.3, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: biCPD3ene + H <=> adductc
""",
)

entry(
    index = 71,
    label = "C10H9-4 <=> C10H8-4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.34e+08, 's^-1'), n=1.55, Ea=(15.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod4 <=> naphthalene + H
""",
)

entry(
    index = 72,
    label = "CH2CHNH2 + H <=> CH2CH2NH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.141e+07, 'cm^3/(mol*s)'),
        n = 1.767,
        Ea = (3729, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc = 
u"""
CBS-QB3
""",
)

entry(
    index = 73,
    label = "C2H4 + NH2 <=> CH2CH2NH2",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1228, 'cm^3/(mol*s)'), n=2.756, Ea=(1658, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc = 
u"""
CBS-QB3
""",
)

entry(
    index = 74,
    label = "CH2NH + H <=> CH2NH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.475e+08, 'cm^3/(mol*s)'),
        n = 1.674,
        Ea = (2295, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc = 
u"""
CBS-QB3
""",
)

entry(
    index = 75,
    label = "C4H9-1 + C8H8 <=> C12H17-1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (236.006, 'cm^3/(mol*s)'),
        n = 2.7878,
        Ea = (15.4228, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction, kinetics calculated by Lawrence Lai""",
    longDesc = 
u"""
Training reaction, kinetics calculated by Lawrence Lai under the CBS-QB3 level of theory, 2016
More information can be found on pharos ~laitcl/Gaussian/HxBUpdated
""",
)

entry(
    index = 76,
    label = "C9H11-1 <=> C8H8 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.59e+12, 's^-1'),
        n = 0.733,
        Ea = (35.918, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'From 2012 Kislov',
    ),
    longDesc = 
u"""
Originally from reaction library: From 2012 Kislov
""",
)

entry(
    index = 77,
    label = "C9H11-3 <=> C2H4 + C7H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.717e+13, 's^-1'),
        n = 0,
        Ea = (22.905, 'kcal/mol'),
        T0 = (1, 'K'),
        comment = 'CBS-QB3',
    ),
    longDesc = 
u"""
Originally from reaction library: New_Phenyl_Propene_Pathway
CBS-QB3
""",
)

entry(
    index = 78,
    label = "C12H18 + H <=> C12H19-1",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.75247e+08, 'cm^3/(mol*s)'),
        n = 1.70829,
        Ea = (25.4744, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction, kinetics calculated by Lawrence Lai""",
    longDesc = 
u"""
Training reaction, kinetics calculated by Lawrence Lai under the CBS-QB3 level of theory, 2017
Hexylbenzene + H --> CCCCCCC1C=C[CH]C=C1
More information can be found on pharos/home/laitcl/Gaussian/HAdditiontoRing
""",
)

entry(
    index = 79,
    label = "C7H8-27 + H <=> C7H9-23",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.15859e+09, 'cm^3/(mol*s)'),
        n = 1.42903,
        Ea = (22.7647, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction, kinetics calculated by Lawrence Lai""",
    longDesc = 
u"""
Training reaction, kinetics calculated by Lawrence Lai under the CBS-QB3 level of theory, 2017
Toluene + H --> CC1[CH]C=CCC=1
More information can be found on pharos/home/laitcl/Gaussian/HAdditiontoRing
""",
)

entry(
    index = 80,
    label = "C7H8-13 + H <=> C7H9-24",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.04885e+09, 'cm^3/(mol*s)'),
        n = 1.43982,
        Ea = (18.8871, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction, kinetics calculated by Lawrence Lai""",
    longDesc = 
u"""
Training reaction, kinetics calculated by Lawrence Lai under the CBS-QB3 level of theory, 2017
Toluene + H --> CC1=C[CH]C=CC1
More information can be found on pharos/home/laitcl/Gaussian/HAdditiontoRing
""",
)

entry(
    index = 81,
    label = "C7H8-29 + H <=> C7H9-25",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.24659e+09, 'cm^3/(mol*s)'),
        n = 1.42368,
        Ea = (22.5731, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction, kinetics calculated by Lawrence Lai""",
    longDesc = 
u"""
Training reaction, kinetics calculated by Lawrence Lai under the CBS-QB3 level of theory, 2017
Toluene + H --> CC1C=CC[CH]C=1
More information can be found on pharos/home/laitcl/Gaussian/HAdditiontoRing
""",
)

entry(
    index = 82,
    label = "C7H8-5 + H <=> C7H9-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.40866e+08, 'cm^3/(mol*s)'),
        n = 1.56916,
        Ea = (26.7856, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction, kinetics calculated by Lawrence Lai""",
    longDesc = 
u"""
Training reaction, kinetics calculated by Lawrence Lai under the CBS-QB3 level of theory, 2017
Toluene + H --> CC1C=C[CH]C=C1
More information can be found on pharos/home/laitcl/Gaussian/HAdditiontoRing
""",
)

entry(
    index = 83,
    label = "propene_1 + C6H5 <=> C9H11",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3132, 'cm^3/(mol*s)'), n=2.668, Ea=(0.41, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: C6H5 + C3H6 <=> i1
""",
)

entry(
    index = 84,
    label = "propene_2 + C6H5 <=> C9H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (681.8, 'cm^3/(mol*s)'),
        n = 2.75,
        Ea = (2.279, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: C6H5 + C3H6 <=> i2
""",
)

entry(
    index = 85,
    label = "C9H11-4 <=> C9H10 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.532e+07, 's^-1'), n=1.831, Ea=(34.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i1 <=> p2 + H
""",
)

entry(
    index = 86,
    label = "C9H11-5 <=> C9H10-2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.133e+08, 's^-1'), n=1.389, Ea=(34.424, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i1 <=> p3 + H
""",
)

entry(
    index = 87,
    label = "C9H11-6 <=> C8H8-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.169e+10, 's^-1'), n=0.925, Ea=(28.785, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i2 <=> p1 + CH3
""",
)

entry(
    index = 88,
    label = "C9H11-7 <=> C9H10-3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.145e+09, 's^-1'), n=1.255, Ea=(34.391, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i2 <=> p4 + H
""",
)

entry(
    index = 89,
    label = "C9H11-8 <=> C9H10-4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.77e+08, 's^-1'), n=1.506, Ea=(35.156, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i4 <=> p2 + H
""",
)

entry(
    index = 90,
    label = "C9H11-9 <=> C9H10-5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.595e+09, 's^-1'), n=1.097, Ea=(22.941, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i5 <=> p5 + H
""",
)

entry(
    index = 91,
    label = "C9H11-10 <=> C9H10-6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.6e+09, 's^-1'), n=1.106, Ea=(25.978, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i6 <=> p2 + H
""",
)

entry(
    index = 92,
    label = "C9H11-1 <=> C8H8 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.276e+11, 's^-1'), n=0.842, Ea=(35.998, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i7 <=> p1 + CH3
""",
)

entry(
    index = 93,
    label = "C9H11-11 <=> C9H10-7 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.757e+10, 's^-1'), n=1.083, Ea=(40.433, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i7 <=> p3 + H
""",
)

entry(
    index = 94,
    label = "C9H11-12 <=> C8H8-3 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.37e+13, 's^-1'), n=0.61, Ea=(48.173, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i8 <=> p7 + CH3
""",
)

entry(
    index = 95,
    label = "C9H11-13 <=> C9H10-8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.945e+09, 's^-1'), n=1.096, Ea=(26.664, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i8 <=> p8 + H
""",
)

entry(
    index = 96,
    label = "C9H11-14 <=> C9H10-9 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.086e+10, 's^-1'), n=0.921, Ea=(25.035, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i10 <=> p4 + H
""",
)

entry(
    index = 97,
    label = "C9H11-3 <=> C2H4 + C7H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.39e+09, 's^-1'), n=1.1, Ea=(22.881, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry: i4 <=> benzyl + C2H4
""",
)

entry(
    index = 98,
    label = "C7H8-5 + H <=> C7H9-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.65e+06, 'cm^3/(mol*s)'),
        n = 2.063,
        Ea = (3.976, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2001_Tokmakov_H_Toluene_to_CH3_Benzene_high_P""",
    longDesc = 
u"""
Taken from entry: C6H5CH3 + H <=> ipso-(C7H9)
""",
)

entry(
    index = 99,
    label = "C7H9-8 <=> C6H6-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.831e+11, 's^-1'), n=0.669, Ea=(19.862, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2001_Tokmakov_H_Toluene_to_CH3_Benzene_high_P""",
    longDesc = 
u"""
Taken from entry: ipso-(C7H9) <=> C6H6 + CH3
""",
)

entry(
    index = 100,
    label = "C4H6 + C2H3 <=> C6H9-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (39130, 'cm^3/(mol*s)'),
        n = 2.404,
        Ea = (0.42, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: C2H3 + C4H6 <=> C6H9
""",
)

entry(
    index = 101,
    label = "C6H9-7 <=> C6H8-3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.29e+06, 's^-1'), n=2.017, Ea=(40.664, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: C6H9 <=> C6H8 + H
""",
)

entry(
    index = 102,
    label = "C6H9-8 <=> C6H8-4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.972e+07, 's^-1'), n=1.802, Ea=(32.304, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: c5-C6H9 <=> H + c5-C6H8
""",
)

entry(
    index = 103,
    label = "C6H9-9 <=> C6H8-5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.487e+08, 's^-1'), n=1.395, Ea=(33.132, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: c6-C6H9 <=> H + C6H8-c6-13
""",
)

entry(
    index = 104,
    label = "C6H9-10 <=> C6H8-6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.097e+09, 's^-1'), n=1.299, Ea=(33.394, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: c6-C6H9 <=> H + C6H8-c6-14
""",
)

entry(
    index = 105,
    label = "C6H9-11 <=> C5H6-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.961e+11, 's^-1'), n=0.717, Ea=(38.962, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: c5-C6H9-2 <=> C5H6 + CH3
""",
)

entry(
    index = 106,
    label = "C4H4 + C6H5 <=> C10H9-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (32420, 'cm^3/(mol*s)'),
        n = 2.179,
        Ea = (-0.282, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: C6H5 + C4H4 <=> W1
""",
)

entry(
    index = 107,
    label = "C10H9-6 <=> C10H8-5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.456e+08, 's^-1'), n=1.511, Ea=(40.052, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W1 <=> P2 + H
""",
)

entry(
    index = 108,
    label = "C4H4-2 + C6H5 <=> C10H9-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (392600, 'cm^3/(mol*s)'),
        n = 2.192,
        Ea = (4.297, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: C6H5 + C4H4 <=> W2
""",
)

entry(
    index = 109,
    label = "C4H4-3 + C6H5 <=> C10H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (44410, 'cm^3/(mol*s)'),
        n = 2.177,
        Ea = (1.454, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: C6H5 + C4H4 <=> W3
""",
)

entry(
    index = 110,
    label = "C10H9-9 <=> C10H8-6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.076e+12, 's^-1'), n=0.597, Ea=(36.928, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W10 <=> P2 + H
""",
)

entry(
    index = 111,
    label = "C10H9-10 <=> C10H8-7 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.394e+10, 's^-1'), n=1.133, Ea=(39.957, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W16 <=> P2 + H
""",
)

entry(
    index = 112,
    label = "C10H9-11 <=> C10H8-8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.951e+13, 's^-1'), n=0.612, Ea=(49.045, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: W20 <=> P2 + H
""",
)

entry(
    index = 113,
    label = "C4H4-4 + C6H5 <=> C10H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1571, 'cm^3/(mol*s)'), n=2.63, Ea=(2.072, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: C6H5 + C4H4 <=> W14
""",
)

entry(
    index = 114,
    label = "C10H8-9 + H <=> C10H9-13",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.824e+09, 'cm^3/(mol*s)'),
        n = 1.551,
        Ea = (4.518, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: P1 + H <=> W6
""",
)

entry(
    index = 115,
    label = "C10H8-10 + H <=> C10H9-14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.785e+08, 'cm^3/(mol*s)'),
        n = 1.663,
        Ea = (10.356, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: P1 + H <=> W13
""",
)

entry(
    index = 116,
    label = "C10H8-11 + H <=> C10H9-15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.163e+11, 'cm^3/(mol*s)'),
        n = 1.054,
        Ea = (3.968, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: P4 + H <=> W3
""",
)

entry(
    index = 117,
    label = "C10H8-12 + H <=> C10H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.786e+08, 'cm^3/(mol*s)'),
        n = 1.533,
        Ea = (3.846, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: P4 + H <=> W9
""",
)

entry(
    index = 118,
    label = "C10H8-13 + H <=> C10H9-17",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.278e+08, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (5.344, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: P5 + H <=> W3
""",
)

entry(
    index = 119,
    label = "C10H8-14 + H <=> C10H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.149e+09, 'cm^3/(mol*s)'),
        n = 1.595,
        Ea = (4.014, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: P5 + H <=> W20
""",
)

entry(
    index = 120,
    label = "C10H8-15 + H <=> C10H9-19",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.081e+08, 'cm^3/(mol*s)'),
        n = 1.65,
        Ea = (6.797, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry: P6 + H <=> W14
""",
)

entry(
    index = 121,
    label = "C10H10-10 + H <=> C10H11-15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.58,
        Ea = (1.6, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt13 + H <=> pdt25
""",
)

entry(
    index = 122,
    label = "C9H8-3 + CH3 <=> C10H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(643, 'cm^3/(mol*s)'), n=2.8, Ea=(8.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: INDENE + CH3 <=> pdt27
""",
)

entry(
    index = 123,
    label = "C7H9-27 <=> C7H8-13 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.06e+10, 's^-1'), n=1.26, Ea=(28.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product20 <=> TOLUENE + H
""",
)

entry(
    index = 124,
    label = "C3H4-2 + C6H5 <=> C9H9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.075e+06, 'cm^3/(mol*s)'),
        n = 2.038,
        Ea = (3.037, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: phenyl + HCCCH3 <=> W1_2
""",
)

entry(
    index = 125,
    label = "C3H4-4 + C6H5 <=> C9H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (630400, 'cm^3/(mol*s)'),
        n = 2.103,
        Ea = (6.093, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: phenyl + HCCCH3 <=> W3_4
""",
)

entry(
    index = 126,
    label = "C3H4 + C6H5 <=> C9H9-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (28890, 'cm^3/(mol*s)'),
        n = 2.595,
        Ea = (3.241, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: phenyl + H2CCCH2 <=> W6
""",
)

entry(
    index = 127,
    label = "C3H4-3 + C6H5 <=> C9H9-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(4578, 'cm^3/(mol*s)'), n=2.53, Ea=(1.932, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: phenyl + H2CCCH2 <=> W11
""",
)

entry(
    index = 128,
    label = "C2H2 + C7H7-3 <=> C9H9-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (892300, 'cm^3/(mol*s)'),
        n = 2.091,
        Ea = (11.371, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: benzyl + C2H2 <=> W20
""",
)

entry(
    index = 129,
    label = "C9H8-4 + H <=> C9H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.954e+07, 'cm^3/(mol*s)'),
        n = 1.548,
        Ea = (4.985, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: Indene + H <=> W15
""",
)

entry(
    index = 130,
    label = "C9H8-5 + H <=> C9H9-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.514e+08, 'cm^3/(mol*s)'),
        n = 1.545,
        Ea = (3.073, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: Indene + H <=> W22
""",
)

entry(
    index = 131,
    label = "C9H8-6 + H <=> C9H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.739e+10, 'cm^3/(mol*s)'),
        n = 0.881,
        Ea = (-0.465, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: Indene + H <=> W23
""",
)

entry(
    index = 132,
    label = "C9H8-7 + H <=> C9H9-9",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.379e+07, 'cm^3/(mol*s)'),
        n = 1.723,
        Ea = (7.429, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: Indene + H <=> W18
""",
)

entry(
    index = 133,
    label = "C9H8-8 + H <=> C9H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.639e+10, 'cm^3/(mol*s)'),
        n = 1.06,
        Ea = (4.834, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: P2 + H <=> W1_2
""",
)

entry(
    index = 134,
    label = "C9H8-9 + H <=> C9H9-11",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.492e+10, 'cm^3/(mol*s)'),
        n = 1.051,
        Ea = (3.163, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: P2 + H <=> W5
""",
)

entry(
    index = 135,
    label = "C9H8-10 + H <=> C9H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.175e+08, 'cm^3/(mol*s)'),
        n = 1.505,
        Ea = (2.462, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: phenyl-allene + H <=> W1_2
""",
)

entry(
    index = 136,
    label = "C9H8-11 + H <=> C9H9-13",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.339e+08, 'cm^3/(mol*s)'),
        n = 1.587,
        Ea = (2.425, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: phenyl-allene + H <=> W8_9
""",
)

entry(
    index = 137,
    label = "C9H8-12 + H <=> C9H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.113e+08, 'cm^3/(mol*s)'),
        n = 1.511,
        Ea = (4.384, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: phenyl-allene + H <=> W11
""",
)

entry(
    index = 138,
    label = "C9H8-13 + H <=> C9H9-15",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.255e+11, 'cm^3/(mol*s)'),
        n = 1.005,
        Ea = (3.143, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: P4 + H <=> W11
""",
)

entry(
    index = 139,
    label = "C9H8-14 + H <=> C9H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.276e+10, 'cm^3/(mol*s)'),
        n = 1.103,
        Ea = (4.911, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: P4 + H <=> W20
""",
)

entry(
    index = 140,
    label = "C8H6 + CH3 <=> C9H9-17",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (563200, 'cm^3/(mol*s)'),
        n = 2.488,
        Ea = (11.733, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: phenylacetylene + CH3 <=> W3_4
""",
)

entry(
    index = 141,
    label = "C8H6-2 + CH3 <=> C9H9-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (713400, 'cm^3/(mol*s)'),
        n = 2.58,
        Ea = (7.568, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry: phenylacetylene + CH3 <=> W5
""",
)

entry(
    index = 142,
    label = "C10H10-11 + H <=> C10H11-17",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.059e+08, 'cm^3/(mol*s)'),
        n = 1.596,
        Ea = (4.69, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP""",
    longDesc = 
u"""
Taken from entry: 3_methylindene + H <=> W1
""",
)

entry(
    index = 143,
    label = "C10H10-12 + H <=> C10H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.904e+08, 'cm^3/(mol*s)'),
        n = 1.534,
        Ea = (3.418, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP""",
    longDesc = 
u"""
Taken from entry: 1_methylindene + H <=> W1
""",
)

entry(
    index = 144,
    label = "C9H8-5 + CH3 <=> C10H11-19",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3206, 'cm^3/(mol*s)'),
        n = 2.611,
        Ea = (8.195, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP""",
    longDesc = 
u"""
Taken from entry: Indene + CH3 <=> W1
""",
)

entry(
    index = 145,
    label = "C10H10-13 + H <=> C10H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.441e+08, 'cm^3/(mol*s)'),
        n = 1.514,
        Ea = (2.403, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP""",
    longDesc = 
u"""
Taken from entry: 2_methylindene + H <=> W2
""",
)

entry(
    index = 146,
    label = "C9H8-6 + CH3 <=> C10H11-21",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5064, 'cm^3/(mol*s)'),
        n = 2.608,
        Ea = (5.867, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_Indene_CH3_highP""",
    longDesc = 
u"""
Taken from entry: Indene + CH3 <=> W2
""",
)

entry(
    index = 147,
    label = "C4H6 + C6H5 <=> C10H11-22",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(813000, 'cm^3/(mol*s)'), n=2.56, Ea=(0, 'kJ/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: phenyl + 1_3_butadiene <=> 4_phenyl_buten_3_yl
""",
)

entry(
    index = 148,
    label = "C4H6-2 + C6H5 <=> C10H11-23",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(47900, 'cm^3/(mol*s)'), n=2.65, Ea=(16.7, 'kJ/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: phenyl + 1_3_butadiene <=> 3_phenyl_buten_4_yl
""",
)

entry(
    index = 149,
    label = "C10H11-24 <=> C10H10-14 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.61e+07, 's^-1'), n=2.11, Ea=(161.62, 'kJ/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: 4_phenyl_buten_3_yl <=> 1_phenyl_1_3_butadiene + H
""",
)

entry(
    index = 150,
    label = "C10H11-14 <=> C10H10-9 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.38e+10, 's^-1'), n=1.25, Ea=(92.6, 'kJ/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2005_Ismail_C6H5_C4H6_highP""",
    longDesc = 
u"""
Taken from entry: trihydronaphthalene <=> 1_4_dihydro_naphthalene + H
""",
)

entry(
    index = 151,
    label = "C2H2 + C8H7 <=> C10H9-20",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.12e+07, 'cm^3/(mol*s)'),
        n = 1.489,
        Ea = (4.331, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: C6H4C2H3 + C2H2 <=> W5
""",
)

entry(
    index = 152,
    label = "C10H9-21 <=> C10H8-16 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.567e+11, 's^-1'), n=0.787, Ea=(28.205, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W6 <=> P1 + H
""",
)

entry(
    index = 153,
    label = "C10H9-22 <=> C10H8-17 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.191e+09, 's^-1'), n=1.264, Ea=(30.816, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W8 <=> P2 + H
""",
)

entry(
    index = 154,
    label = "C10H9-23 <=> C10H8-18 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.304e+10, 's^-1'), n=1.16, Ea=(37.552, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W5 <=> P5 + H
""",
)

entry(
    index = 155,
    label = "C10H9-24 <=> C10H8-19 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.05e+10, 's^-1'), n=1.329, Ea=(52.477, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W101 <=> P2 + H
""",
)

entry(
    index = 156,
    label = "C10H9-25 <=> C10H8-20 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.923e+11, 's^-1'), n=0.777, Ea=(40.274, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W102 <=> P2 + H
""",
)

entry(
    index = 157,
    label = "C10H9-26 <=> C10H8-21 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.568e+11, 's^-1'), n=0.972, Ea=(78.037, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W103 <=> P105 + H
""",
)

entry(
    index = 158,
    label = "C10H9-27 <=> C10H8-22 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.249e+08, 's^-1'), n=1.2, Ea=(27.426, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W107 <=> P109 + H
""",
)

entry(
    index = 159,
    label = "C10H9-28 <=> C10H8-23 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.956e+11, 's^-1'), n=0.789, Ea=(32.262, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W118 <=> P1 + H
""",
)

entry(
    index = 160,
    label = "C10H9-29 <=> C10H8-24 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.427e+09, 's^-1'), n=1.431, Ea=(66.532, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W106 <=> P109 + H
""",
)

entry(
    index = 161,
    label = "C10H9-30 <=> C10H8-25 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.893e+15, 's^-1'), n=-0.16, Ea=(65.494, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W108 <=> P109 + H
""",
)

entry(
    index = 162,
    label = "C10H9-31 <=> C10H8-26 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.234e+12, 's^-1'), n=0.766, Ea=(43.611, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W119 <=> P2 + H
""",
)

entry(
    index = 163,
    label = "C10H10-16 <=> C10H9-32 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.401e+11, 's^-1'), n=0.549, Ea=(19.678, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W14 <=> P9 + H
""",
)

entry(
    index = 164,
    label = "C2H2 + C8H5 <=> C10H7",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.068e+06, 'cm^3/(mol*s)'),
        n = 1.842,
        Ea = (3.272, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: R1 + C2H2 <=> W1
""",
)

entry(
    index = 165,
    label = "C10H6 + H <=> C10H7-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.775e+09, 'cm^3/(mol*s)'),
        n = 1.414,
        Ea = (6.896, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: P1 + H <=> W1
""",
)

entry(
    index = 166,
    label = "C10H6-2 + H <=> C10H7-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.586e+11, 'cm^3/(mol*s)'),
        n = 0.743,
        Ea = (0.228, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: P2 + H <=> W2
""",
)

entry(
    index = 167,
    label = "C10H6-3 + H <=> C10H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.409e+12, 'cm^3/(mol*s)'),
        n = 0.597,
        Ea = (0.436, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: P2 + H <=> W4
""",
)

entry(
    index = 168,
    label = "C10H6-4 + H <=> C10H7-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.179e+12, 'cm^3/(mol*s)'),
        n = 0.61,
        Ea = (0.09, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: P3 + H <=> W4
""",
)

entry(
    index = 169,
    label = "C10H6-5 + H <=> C10H7-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.919e+13, 'cm^3/(mol*s)'),
        n = 0.168,
        Ea = (-0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: P4 + H <=> W5
""",
)

entry(
    index = 170,
    label = "C10H6-6 + H <=> C10H7-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.919e+13, 'cm^3/(mol*s)'),
        n = 0.168,
        Ea = (-0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: P5 + H <=> W7
""",
)

entry(
    index = 171,
    label = "C6H9-11 <=> C5H6-2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.89e+14, 's^-1'), n=0, Ea=(38.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Wang_K_C6H9""",
    longDesc = 
u"""
Taken from entry: Well_5 <=> CH3 + CPD
""",
)

entry(
    index = 172,
    label = "C10H9-9 <=> C10H8-6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.817e+11, 's^-1'), n=0.838, Ea=(38.356, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5C2H2_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: W3 <=> P4 + H
""",
)

entry(
    index = 173,
    label = "C2H2 + C8H7-2 <=> C10H9-33",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.081e+09, 'cm^3/(mol*s)'),
        n = 1.21,
        Ea = (6.756, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5C2H2_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: R2 + C2H2 <=> W3
""",
)

entry(
    index = 174,
    label = "C10H9-14 <=> C10H8-10 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.581e+10, 's^-1'), n=0.793, Ea=(14.523, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5C2H2_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: W4 <=> P1 + H
""",
)

entry(
    index = 175,
    label = "C8H7-3 <=> C8H6 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.323e+10, 's^-1'), n=1.103, Ea=(38.251, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: W1 <=> P1 + H
""",
)

entry(
    index = 176,
    label = "C2H2 + C6H5 <=> C8H7-4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.954e+07, 'cm^3/(mol*s)'),
        n = 1.638,
        Ea = (3.448, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: R1 + C2H2 <=> W1
""",
)

entry(
    index = 177,
    label = "C6H6-2 + CH3 <=> C7H9-8",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (2195, 'cm^3/(mol*s)'),
        n = 2.878,
        Ea = (10.912, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: benzene_1 + methyl_7 <=> C7H9_12
""",
)

entry(
    index = 178,
    label = "C7H9-9 <=> C7H8-5 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.217e+10, 's^-1'), n=0.87, Ea=(25.199, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C7H9_12 <=> C7H8_17 + H_15
""",
)

entry(
    index = 179,
    label = "C2H2 + C7H7-3 <=> C9H9-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (31630, 'cm^3/(mol*s)'),
        n = 2.479,
        Ea = (11.061, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C7H7_10 + ethyne_8 <=> C9H9_13
""",
)

entry(
    index = 180,
    label = "C9H9-9 <=> C9H8-7 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.597e+10, 's^-1'), n=0.889, Ea=(20.893, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9_14 <=> indene_25 + H_15
""",
)

entry(
    index = 181,
    label = "C6H6-2 + C3H3 <=> C9H9-19",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (144.6, 'cm^3/(mol*s)'),
        n = 2.951,
        Ea = (14.055, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: benzene_1 + C3H3_9 <=> C9H9_2
""",
)

entry(
    index = 182,
    label = "C6H6-2 + C3H3-2 <=> C9H9-20",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (312.3, 'cm^3/(mol*s)'),
        n = 2.973,
        Ea = (16.396, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: benzene_1 + C3H3_9 <=> C9H9_6
""",
)

entry(
    index = 183,
    label = "C9H9-6 <=> C9H8-4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.591e+10, 's^-1'), n=0.886, Ea=(24.975, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H9_5 <=> indene_25 + H_15
""",
)

entry(
    index = 184,
    label = "SO2 + H <=> HOSO",
    degeneracy = 2,
    kinetics = Arrhenius(A=(2.37e+08, 'cm^3/(mol*s)'), n=1.63, Ea=(7339, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (1700, 'K')),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: SOx""",
    longDesc = 
u"""
M.A. Blitz, K.J. Hughes, M.J. Pilling, S.H. Robertson, J. Phys. Chem. A, 2006, 110(9), 2996–3009, doi: 10.1021/jp054722u
As reported by Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017

Originally a Troe expression was given, only k_inf was taken here:
kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.37e+08, 'cm^3/(mol*s)'), n=1.63, Ea=(7339, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (1700, 'K')),
        arrheniusLow = Arrhenius(A=(1.85e+37, 'cm^6/(mol^2*s)'), n=-6.14, Ea=(11075, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (1700, 'K')),
        alpha=0.283, T3=(272, 'K'), T1=(3995, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5}),
""",
)

entry(
    index = 185,
    label = "N2 + H <=> NNH",
    degeneracy = 2,
    kinetics = Arrhenius(A=(7.6e+15, 'cm^3/(mol*s)'), n=-0.64, Ea=(15333, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (25000, 'K')),
    rank = 2,
    shortDesc = u"""Training reaction from kinetics library: NOx""",
    longDesc =
u"""
P.J.S.B. Caridade, S.P.J. Rodrigues, F. Sousa, A.J.C. Varandas, J. Phys. Chem. A ,2005, 109, 2356-2363, doi: 10.1021/jp045102g
Fits to a total of 972 MRCI energies (based on the aug-cc-pVQZ basis set of Dunning27), scaled by the DMBE-SEC
method to account for excitations higher than singles and doubles and the incompleteness of the one-electron basis set.
The paper reports a HO-RR rate, and a sum-over-states rate (where vib-rot aren't assumed to be independent).
The sum-over-states rate was taken here.
""",
)
