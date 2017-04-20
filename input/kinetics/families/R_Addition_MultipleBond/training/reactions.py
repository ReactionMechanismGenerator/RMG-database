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
    reference = None,
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



entry(
    index = 30,
    label = "C3H4 + allyl <=> C6H9",
    degeneracy = 1,
    kinetics = Arrhenius(A=(42, 'cm^3/(mol*s)'), n=3.27, Ea=(11, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: aC3H5 + C3H4a <=> prod_1
""",
)

entry(
    index = 31,
    label = "C6H9-2 <=> C6H8 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.93e+09, 's^-1'), n=1.27, Ea=(31, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_2 <=> prod_3 + H
""",
)

entry(
    index = 32,
    label = "C3H4 + C4H7 <=> C7H11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(18.6, 'cm^3/(mol*s)'), n=3, Ea=(9.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4a + iC4H7 <=> prod_6
""",
)

entry(
    index = 33,
    label = "C7H11-2 <=> C7H10 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.37e+08, 's^-1'), n=1.3, Ea=(29.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_4 <=> prod_5 + H
""",
)

entry(
    index = 34,
    label = "C3H4-2 + allyl <=> C6H9-3",
    degeneracy = 1,
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
    index = 35,
    label = "C6H9-4 <=> C6H8-2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.99e+10, 's^-1'), n=1, Ea=(32.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_8 <=> prod_9 + H
""",
)

entry(
    index = 36,
    label = "C3H4-2 + C4H7 <=> C7H11-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(121, 'cm^3/(mol*s)'), n=2.9, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4p + iC4H7 <=> prod_10
""",
)

entry(
    index = 37,
    label = "C7H11-4 <=> C7H10-2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.77e+09, 's^-1'), n=1.4, Ea=(32, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_11 <=> prod_12 + H
""",
)

entry(
    index = 38,
    label = "C3H4 + C4H5 <=> C7H9-19",
    degeneracy = 1,
    kinetics = Arrhenius(A=(128, 'cm^3/(mol*s)'), n=3.05, Ea=(7.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4a + BD2YL <=> prod_13
""",
)

entry(
    index = 39,
    label = "C7H9-20 <=> C7H8-11 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+10, 's^-1'), n=1.27, Ea=(44.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_14 <=> prod_15 + H
""",
)

entry(
    index = 40,
    label = "C3H4-2 + C4H5 <=> C7H9-21",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1900, 'cm^3/(mol*s)'), n=2.92, Ea=(8.5, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4p + BD2YL <=> prod_16
""",
)

entry(
    index = 41,
    label = "C7H9-22 <=> C7H8-12 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.47e+10, 's^-1'), n=1.22, Ea=(45.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_17 <=> prod_18 + H
""",
)

entry(
    index = 42,
    label = "C3H4-3 + allyl <=> C6H9-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3960, 'cm^3/(mol*s)'), n=2.65, Ea=(11.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: aC3H5 + C3H4a <=> prod_19
""",
)

entry(
    index = 43,
    label = "C3H4-3 + C4H7 <=> C7H11-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(37, 'cm^3/(mol*s)'), n=2.89, Ea=(9.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H4a + iC4H7 <=> prod_20
""",
)

entry(
    index = 44,
    label = "C2H2 + allyl <=> C5H7",
    degeneracy = 1,
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
    index = 45,
    label = "C5H7-2 <=> C5H6 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.19e+09, 's^-1'), n=1.37, Ea=(31.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: prod_22 <=> CPD + H
""",
)

entry(
    index = 46,
    label = "C2H2 + C3H3 <=> C5H5-2",
    degeneracy = 1,
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
    index = 47,
    label = "C3H4-2 + C3H3 <=> C6H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7040, 'cm^3/(mol*s)'), n=2.87, Ea=(9.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H3 + C3H4p <=> prod_25
""",
)

entry(
    index = 48,
    label = "C3H4-4 + C3H3 <=> C6H7-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(285, 'cm^3/(mol*s)'), n=2.93, Ea=(11.1, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H3 + C3H4p <=> prod_27
""",
)

entry(
    index = 49,
    label = "C3H4-3 + C3H3 <=> C6H7-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(850, 'cm^3/(mol*s)'), n=2.81, Ea=(8.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C3""",
    longDesc = 
u"""
Taken from entry: C3H3 + C3H4a <=> prod_29
""",
)



entry(
    index = 50,
    label = "C5H6 + C5H5 <=> C10H11",
    degeneracy = 1,
    kinetics = Arrhenius(A=(288, 'cm^3/(mol*s)'), n=2.8, Ea=(8.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: CPD + CPDyl <=> adducte
""",
)

entry(
    index = 51,
    label = "C5H6-2 + C5H5 <=> C10H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(288, 'cm^3/(mol*s)'), n=2.74, Ea=(3.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: CPD + CPDyl <=> adductd
""",
)

entry(
    index = 52,
    label = "C10H10 + H <=> C10H11-3",
    degeneracy = 1,
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
    index = 53,
    label = "C10H11-4 <=> C6H6-2 + C4H5-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.14e+12, 's^-1'), n=0.52, Ea=(22.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt12 <=> benzene + butadieneyl
""",
)

entry(
    index = 54,
    label = "C10H10-2 + H <=> C10H11-5",
    degeneracy = 1,
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
    index = 55,
    label = "C9H8 + CH3 <=> C10H11-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2480, 'cm^3/(mol*s)'), n=2.89, Ea=(-0.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt22 + CH3 <=> pdt21
""",
)

entry(
    index = 56,
    label = "C10H11-7 <=> C10H10-3 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.49e+09, 's^-1'), n=1.41, Ea=(38.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt23 <=> pdt30 + H
""",
)

entry(
    index = 57,
    label = "C10H10-4 + H <=> C10H11-8",
    degeneracy = 1,
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
    index = 58,
    label = "C10H10-5 + H <=> C10H11-9",
    degeneracy = 1,
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
    index = 59,
    label = "C10H11-10 <=> C9H8-2 + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.72e+10, 's^-1'), n=1.33, Ea=(51.9, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt32 <=> pdt22 + CH3
""",
)

entry(
    index = 60,
    label = "C10H10-6 + H <=> C10H11-11",
    degeneracy = 1,
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
    index = 61,
    label = "C10H10-7 + H <=> C10H11-12",
    degeneracy = 1,
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
    index = 62,
    label = "C10H10-8 + H <=> C10H11-13",
    degeneracy = 1,
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
    index = 63,
    label = "C10H10-9 + H <=> C10H11-14",
    degeneracy = 1,
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
    index = 64,
    label = "C6H6 + H <=> C6H7-4",
    degeneracy = 1,
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
    index = 65,
    label = "C6H6-3 + H <=> C6H7-5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.31e+08, 'cm^3/(mol*s)'), n=1.76, Ea=(2, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: FULVENE + H <=> C5H5CH2-1
""",
)

entry(
    index = 66,
    label = "C6H6-5 + H <=> C6H7-6",
    degeneracy = 1,
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
    index = 67,
    label = "C6H6-4 + H <=> C6H7-7",
    degeneracy = 1,
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
    index = 68,
    label = "C6H7-8 <=> C6H6-2 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.84e+09, 's^-1'), n=1.3, Ea=(27.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Fulvene_H""",
    longDesc = 
u"""
Taken from entry: cyC6H7 <=> benzene + H
""",
)



entry(
    index = 69,
    label = "C10H8 + H <=> C10H9",
    degeneracy = 1,
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
    index = 70,
    label = "C10H8-2 + H <=> C10H9-2",
    degeneracy = 1,
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
    index = 71,
    label = "C10H8-3 + H <=> C10H9-3",
    degeneracy = 1,
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
    index = 72,
    label = "C10H9-4 <=> C10H8-4 + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.34e+08, 's^-1'), n=1.55, Ea=(15.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod4 <=> naphthalene + H
""",
)

entry(
    index = 73,
    label = "CH2CHNH2 + H <=> CH2CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.141e+07, 's^-1'), n=1.767, Ea=(3729, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc = 
u"""
CBS-QB3
""",
)

entry(
    index = 74,
    label = "ethene + NH2 <=> CH2CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.228e+03, 's^-1'), n=2.756, Ea=(1658, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc = 
u"""
CBS-QB3
""",
)

entry(
    index = 75,
    label = "CH2NH + H <=> CH2NH2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.475e+08, 's^-1'), n=1.674, Ea=(2295, 'cal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: Ethylamine""",
    longDesc = 
u"""
CBS-QB3
""",
)

entry(
    index = 77,
    label = "N2 + H <=> NNH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.6e+15, 'cm^3/(mol*s)'), n=-0.64, Ea=(15333, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (25000, 'K')),
    rank = 2,
    shortDesc = u"""Training reaction from kinetics library: SOxNOx""",
    longDesc = 
u"""
P.J.S.B. Caridade, S.P.J. Rodrigues, F. Sousa, A.J.C. Varandas, J. Phys. Chem. A ,2005, 109, 2356-2363, doi: 10.1021/jp045102g
Fits to a total of 972 MRCI energies (based on the aug-cc-pVQZ basis set of Dunning27), scaled by the DMBE-SEC
method to account for excitations higher than singles and doubles and the incompleteness of the one-electron basis set.
The paper reports a HO-RR rate, and a sum-over-states rate (where vib-rot aren't assumed to be independent).
The sum-over-states rate was taken here.
""",
)

entry(
    index = 78,
    label = "N2H3O_a <=> NH2 + HNO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(9.12e+33, 's^-1'), n=-6.68, Ea=(35217, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (3000, 'K')),
    rank = 2,
    shortDesc = u"""Training reaction from kinetics library: SOxNOx""",
    longDesc = 
u"""
P. Raghunath, N.T. Nghia, M.C. Lin, Advances in Quantum Chemistry, 2014, 69, 253-301, doi: 10.1016/B978-0-12-800345-9.00007-6
p. 284
P = 1 atm
calculations done at the CCSD(T)/6-311þG(3df,2p)//CCSD/6-311þþG(d,p) level of theoty
""",
)

entry(
    index = 78,
    label = "N2H3O_b <=> NH2NO + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.57e+34, 's^-1'), n=-6.63, Ea=(44953, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (3000, 'K')),
    rank = 2,
    shortDesc = u"""Training reaction from kinetics library: SOxNOx""",
    longDesc = 
u"""
P. Raghunath, N.T. Nghia, M.C. Lin, Advances in Quantum Chemistry, 2014, 69, 253-301, doi: 10.1016/B978-0-12-800345-9.00007-6
p. 284
P = 1 atm
calculations done at the CCSD(T)/6-311þG(3df,2p)//CCSD/6-311þþG(d,p) level of theoty
""",
)

entry(
    index = 79,
    label = "SO2 + H <=> HOSO",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(2.37e+08, 'cm^3/(mol*s)'), n=1.63, Ea=(7339, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (1700, 'K')),
        arrheniusLow = Arrhenius(A=(1.85e+37, 'cm^6/(mol^2*s)'), n=-6.14, Ea=(11075, 'cal/mol'), T0=(1, 'K'), Tmin = (300, 'K'), Tmax = (1700, 'K')),
        alpha=0.283, T3=(272, 'K'), T1=(3995, 'K'), efficiencies={'O=S=O': 10, 'O': 10, 'O=C=O': 2.5}),
    rank = 1,
    shortDesc = u"""Training reaction from kinetics library: SOxNOx""",
    longDesc = 
u"""
M.A. Blitz, K.J. Hughes, M.J. Pilling, S.H. Robertson, J. Phys. Chem. A, 2006, 110(9), 2996–3009, doi: 10.1021/jp054722u
As reported by Gimenez-Lopez, M. Martinez, A. Millera, R. Bilbao, M.U. Alzueta, Comb. Flame 2011, 158(1), 48-56, doi: 10.1016/j.combustflame.2010.07.017
""",
)

