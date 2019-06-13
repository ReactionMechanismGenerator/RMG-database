#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.32e+10, 's^-1'), n=0.35, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product38 <=> product39
""",
)

entry(
    index = 1,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.95e+12, 's^-1'), n=0.12, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product39 <=> product37
""",
)

entry(
    index = 2,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.69e+11, 's^-1'), n=0.22, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt18 <=> pdt19
""",
)

entry(
    index = 3,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt23
""",
)

entry(
    index = 4,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.02e+11, 's^-1'), n=0.79, Ea=(35.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt55 <=> pdt58
""",
)

entry(
    index = 5,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+12, 's^-1'), n=0.45, Ea=(25.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod2 <=> prod5
""",
)

entry(
    index = 6,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.311e+09, 's^-1'), n=0.537, Ea=(2.307, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = 'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP
Taken from entry: W5 <=> W8
""",
)

entry(
    index = 7,
    label = "C10H7 <=> C10H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.992e+11, 's^-1'), n=0.67, Ea=(58.336, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    longDesc = 
u"""
Effective rate for an adduct of phenyl radical + diacetylene to form either benzofulvenyl or 2-naphthyl radical.
Rate-limiting step is trans-cis isomerization of the adduct, calculated by Zach Buras using CBS-QB3.
From kinetics library: First_to_Second_Aromatic_Ring/phenyl_diacetylene_effective
Taken from entry: i2_trans <=> i3
""",
)

entry(
    index = 8,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.66e+11, 's^-1'), n=0.412, Ea=(27.805, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = 'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 9,
    label = "C9H9-3 <=> C9H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.454e+11, 's^-1'), n=0.447, Ea=(24.536, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = 'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 10,
    label = "C9H9-5 <=> C9H9-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.185e+11, 's^-1'), n=0.586, Ea=(37.614, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = 'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 11,
    label = "C9H9-7 <=> C9H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.241e+10, 's^-1'), n=0.754, Ea=(22.335, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = 'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 12,
    label = "C9H9-9 <=> C9H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.932e+07, 's^-1'), n=1.035, Ea=(14.54, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = 'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 13,
    label = "C9H9-11 <=> C9H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.713e+10, 's^-1'), n=0.481, Ea=(30.309, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = 'Pressure-dependent rate constants for PAH growth: formation of indene and its conversion to naphthalene',
        journal = 'Faraday Discussions',
        volume = '195(0)',
        pages = '637-670',
        year = '2016',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP
""",
)

entry(
    index = 14,
    label = "C10H9-5 <=> C10H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.54e+10, 's^-1'), n=0.69, Ea=(20.376, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = 'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 15,
    label = "C10H9-7 <=> C10H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.423e+09, 's^-1'), n=0.834, Ea=(24.235, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = 'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 16,
    label = "C10H9-9 <=> C10H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.233e+11, 's^-1'), n=0.39, Ea=(35.846, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = 'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 17,
    label = "C10H9-11 <=> C10H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.126e+14, 's^-1'), n=-0.355, Ea=(28.539, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = 'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 18,
    label = "C10H9-13 <=> C10H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.881e+08, 's^-1'), n=1.062, Ea=(16.546, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = 'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 19,
    label = "C10H9-15 <=> C10H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.443e+10, 's^-1'), n=0.474, Ea=(23.82, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'A. Landera', 'R. I. Kaiser'],
        title = 'Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames',
        journal = 'Journal of Physical Chemistry A',
        volume = '121(5)',
        pages = '901-926',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP
""",
)

entry(
    index = 20,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.249e+08, 's^-1'), n=0.846, Ea=(19.298, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Z. J. Buras', 'E. E. Dames', 'S. S. Merchant', 'G. Liu', 'R. M. I. Elsamra', 'W. H. Green'],
        title = 'Kinetics and Products of Vinyl + 1,3-Butadiene, a Potential Route to Benzene',
        journal = 'Journal of Physical Chemistry A',
        volume = '119(28)',
        pages = '7325-7338',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
Calculations done at CCSD(T)-F12a/cc-pVTZ-F12//M08SO/MG3S level of theory
From kinetics library: 2015_Buras_C2H3_C4H6_highP
""",
)

entry(
    index = 21,
    label = "C9H11 <=> C9H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.597e+08, 's^-1'), n=0.953, Ea=(15.885, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Z. J. Buras', 'T.-C. Chu', 'A. Jamal', 'N. W. Yee', 'J. E. Middaugh', 'W. H. Green'],
        title = 'Phenyl radical + propene: a prototypical reaction surface for aromatic-catalyzed 1,2-hydrogen-migration and subsequent resonance-stabilized radical formation',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '20',
        pages = '13191-13214 ',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP
""",
)

entry(
    index = 22,
    label = "C9H11-3 <=> C9H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.732e+09, 's^-1'), n=0.671, Ea=(15.317, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['Z. J. Buras', 'T.-C. Chu', 'A. Jamal', 'N. W. Yee', 'J. E. Middaugh', 'W. H. Green'],
        title = 'Phenyl radical + propene: a prototypical reaction surface for aromatic-catalyzed 1,2-hydrogen-migration and subsequent resonance-stabilized radical formation',
        journal = 'Physical Chemistry Chemical Physics',
        volume = '20',
        pages = '13191-13214 ',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP
""",
)

entry(
    index = 23,
    label = "C10H7-3 <=> C10H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.42e+11, 's^-1'), n=0.258, Ea=(3.797, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. M. Mebel', 'Y. Georgievskii', 'A. W. Jasper', 'S. J. Klippenstein'],
        title = 'Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene',
        journal = 'Proceedings of the Combustion Institute',
        volume = '36(1)',
        pages = '919-926',
        year = '2017',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at G3(MP2,CC)//B3LYP/6-311G** level of theory
From kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP
Taken from entry: W1 <=> W3_6
""",
)

entry(
    index = 24,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.3e+12, 's^-1'), n=0.45, Ea=(25.6, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = 'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: naphthalene_H
Taken from entry: prod2 <=> prod5
""",
)

entry(
    index = 25,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.36e+10, 's^-1'), n=0.44, Ea=(32.2, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = 'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt16 <=> pdt17
""",
)

entry(
    index = 26,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.02e+11, 's^-1'), n=0.79, Ea=(35.3, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = 'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: C10H11
Taken from entry: pdt55 <=> pdt58
""",
)

entry(
    index = 27,
    label = "C7H9-5 <=> C7H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.95e+10, 's^-1'), n=0.53, Ea=(31.5, 'kcal/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ['A. J. Vervust', 'M. R. Djokic', 'S. S. Merchant', 'H.-H. Carstensen', 'A. E. Long', 'G. B. Marin', 'W. H. Green', 'K. M. Van Geem'],
        title = 'Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene',
        journal = 'Energy & Fuels',
        volume = '32(3)',
        pages = '3920-3934',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
Calculations done at CBS-QB3 level of theory
From kinetics library: vinylCPD_H
Taken from entry: product16 <=> product5
""",
)

entry(
    index = 28,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.51e+10, 's^-1'),
        n = 0,
        Ea = (28.6604, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R6_SSS_D;doublebond_intra_2H_pri;radadd_intra_cs2H
""",
)

entry(
    index = 29,
    label = "C6H9-3 <=> C6H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (108.156, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R4_S_D;doublebond_intra_2H_pri;radadd_intra_csHDe
""",
)

entry(
    index = 30,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (196.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R6_SMS_D;doublebond_intra;radadd_intra_cs
""",
)

entry(
    index = 31,
    label = "C6H9-5 <=> C6H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (196.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R6_SSM_D;doublebond_intra;radadd_intra_cs
""",
)

entry(
    index = 32,
    label = "C7H11 <=> C7H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+10, 's^-1'),
        n = 0,
        Ea = (196.02, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 5,
    longDesc = 
u"""
Converted to training reaction from rate rule: R5_SD_D;doublebond_intra_HNd_pri;radadd_intra_csHNd
""",
)

entry(
    index = 33,
    label = "C3H7O2 <=> C3H7O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.724e+10, 's^-1', '*|/', 3),
        n = 0.478,
        Ea = (122.043, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 6,
    shortDesc = u"""MRH CBS-QB3 calculations with 1d h.r. corrections""",
    longDesc = 
u"""
MRH CBS-QB3 calculations for the reaction CH2=CH-CH2-OO => *CH2-cycle(CH-CH2-O-O)

Previous RMG estimate for this reaction was an "Average of average" estimate.  This reaction was of
interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => CH2O+CH2CHO.  The high-p
limit kinetics were necessary to estimate a k(T,P) for this PES.

Reactant: 2 hindered rotors were considered (the OO and CH2OO torsions)
TS: 0 hindered rotors were considered (the only low-frequency torisonal mode corresponded to
	a hindered rotation within the cycle; MRH did not think treating this as a 1-d separable
	hindered rotor was accurate)
Product: 1 hindered rotor was considered (the *CH2 torsion)

All external symmetry numbers were set equal to one.  The k(T) was calculated from 600 - 2000 K,
in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:
k(T) = 2.724e+10 * (T/1K)^0.478 * exp(-29.169 kcal/mol / RT) cm3/mol/s.

Converted to training reaction from rate rule: R5_SS_D;doublebond_intra_2H_pri;radadd_intra_O
""",
)

entry(
    index = 34,
    label = "C5H7 <=> C5H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.41e+10, 's^-1'),
        n = 0.21,
        Ea = (53.5552, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""BMK/cbsb7 + 1D-HR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R5_DS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 35,
    label = "C6H9-7 <=> C6H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.73e+09, 's^-1'),
        n = 0.21,
        Ea = (16.736, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 6,
    shortDesc = u"""BMK/cbsb7 + 1D-HR""",
    longDesc = 
u"""
Converted to training reaction from rate rule: R6_DSS_D;doublebond_intra_2H_pri;radadd_intra_cdsingleH
""",
)

entry(
    index = 36,
    label = "C6H5O2 <=> C6H5O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.785e+11, 's^-1'), n=0.342, Ea=(24.448, 'kcal/mol'), T0=(1, 'K')),
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
The rates have been validated by the rates reported in Proceedings of the Combustion Institute 35 (2015) 1861-1869,
where only 1500, 2000, 2500 K rates were reported.
""",
)

entry(
    index = 37,
    label = "C6H5O2-3 <=> C6H5O2-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.291e+11, 's^-1'), n=0.234, Ea=(29.132, 'kcal/mol'), T0=(1, 'K')),
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
The rates have been validated by the rates reported in Proceedings of the Combustion Institute 35 (2015) 18611869,
where only 1500, 2000, 2500 K rates were reported.
""",
)

entry(
    index = 38,
    label = "C7H5 <=> C7H5-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.05e+09, 's^-1'), n=0.155, Ea=(42.35, 'kcal/mol'), T0=(1, 'K')),
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
    index = 39,
    label = "C12H17-15 <=> C12H17-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.46139e+07, 's^-1'),
        n = 1.30419,
        Ea = (55.0202, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ['Sarah Khanniche', 'Lawrence Lai', 'William H. Green'],
        title = 'Kinetics of Intramolecular Phenyl Migration and Fused Ring Formation in Hexylbenzene Radicals',
        journal = 'J. Phys. Chem. A.',
        volume = '122 (51)',
        pages = '9778-9791',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory""",
    longDesc = 
u"""
Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
Location of calculations Pharos/home/laitcl/Gaussian/2019/
Calculations performed in CBS-QB3 level of theory, with 1-D hindered rotors included in B3LYP/CBSB7 level
Reaction: CCCC[CH]CC1C=CC=CC=1 <=> CCCCC1CC12C=C[CH]C=C2
""",
)

entry(
    index = 40,
    label = "C12H17-17 <=> C12H17-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.1705e+13, 's^-1'),
        n = 0.383545,
        Ea = (19.8224, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ['Sarah Khanniche', 'Lawrence Lai', 'William H. Green'],
        title = 'Kinetics of Intramolecular Phenyl Migration and Fused Ring Formation in Hexylbenzene Radicals',
        journal = 'J. Phys. Chem. A.',
        volume = '122 (51)',
        pages = '9778-9791',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory""",
    longDesc = 
u"""
Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
Location of calculations Pharos/home/laitcl/Gaussian/2019/
Calculations performed in CBS-QB3 level of theory, with 1-D hindered rotors included in B3LYP/CBSB7 level
Reaction: CCCCC1CC12C=C[CH]C=C2 <=> [CH2]C(CCCC)C1C=CC=CC=1
""",
)

entry(
    index = 41,
    label = "C12H17-19 <=> C12H17-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (966131, 's^-1'),
        n = 1.86605,
        Ea = (70.406, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ['Sarah Khanniche', 'Lawrence Lai', 'William H. Green'],
        title = 'Kinetics of Intramolecular Phenyl Migration and Fused Ring Formation in Hexylbenzene Radicals',
        journal = 'J. Phys. Chem. A.',
        volume = '122 (51)',
        pages = '9778-9791',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory""",
    longDesc = 
u"""
Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
Location of calculations Pharos/home/laitcl/Gaussian/2019/
Calculations performed in CBS-QB3 level of theory, with 1-D hindered rotors included in B3LYP/CBSB7 level
Reaction: CCC[CH]CCC1C=CC=CC=1 <=> CCCC1CCC12C=C[CH]C=C2
""",
)

entry(
    index = 42,
    label = "C12H17-21 <=> C12H17-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.0336e+12, 's^-1'),
        n = 0.135082,
        Ea = (42.4869, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ['Sarah Khanniche', 'Lawrence Lai', 'William H. Green'],
        title = 'Kinetics of Intramolecular Phenyl Migration and Fused Ring Formation in Hexylbenzene Radicals',
        journal = 'J. Phys. Chem. A.',
        volume = '122 (51)',
        pages = '9778-9791',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory""",
    longDesc = 
u"""
Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
Location of calculations Pharos/home/laitcl/Gaussian/2019/
Calculations performed in CBS-QB3 level of theory, with 1-D hindered rotors included in B3LYP/CBSB7 level
Reaction: CCCC1CCC12C=C[CH]C=C2 <=> [CH2]CC(CCC)C1C=CC=CC=1
""",
)

entry(
    index = 43,
    label = "C12H17-23 <=> C12H17-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (905.58, 's^-1'),
        n = 2.15236,
        Ea = (31.9171, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ['Sarah Khanniche', 'Lawrence Lai', 'William H. Green'],
        title = 'Kinetics of Intramolecular Phenyl Migration and Fused Ring Formation in Hexylbenzene Radicals',
        journal = 'J. Phys. Chem. A.',
        volume = '122 (51)',
        pages = '9778-9791',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory""",
    longDesc = 
u"""
Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
Location of calculations Pharos/home/laitcl/Gaussian/2019/
Calculations performed in CBS-QB3 level of theory, with 1-D hindered rotors included in B3LYP/CBSB7 level
Reaction: CC[CH]CCCC1C=CC=CC=1 <=> CCC1CCCC12C=C[CH]C=C2
""",
)

entry(
    index = 44,
    label = "C12H17-25 <=> C12H17-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.2027e+12, 's^-1'),
        n = 0.53843,
        Ea = (76.0115, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ['Sarah Khanniche', 'Lawrence Lai', 'William H. Green'],
        title = 'Kinetics of Intramolecular Phenyl Migration and Fused Ring Formation in Hexylbenzene Radicals',
        journal = 'J. Phys. Chem. A.',
        volume = '122 (51)',
        pages = '9778-9791',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory""",
    longDesc = 
u"""
Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
Location of calculations Pharos/home/laitcl/Gaussian/2019/
Calculations performed in CBS-QB3 level of theory, with 1-D hindered rotors included in B3LYP/CBSB7 level
Reaction: CCC1CCCC12C=C[CH]C=C2 <=> [CH2]CCC(CC)C1C=CC=CC=1
""",
)

entry(
    index = 45,
    label = "C12H17-27 <=> C12H17-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (284.136, 's^-1'),
        n = 1.70342,
        Ea = (26.0501, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ['Sarah Khanniche', 'Lawrence Lai', 'William H. Green'],
        title = 'Kinetics of Intramolecular Phenyl Migration and Fused Ring Formation in Hexylbenzene Radicals',
        journal = 'J. Phys. Chem. A.',
        volume = '122 (51)',
        pages = '9778-9791',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory""",
    longDesc = 
u"""
Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
Location of calculations Pharos/home/laitcl/Gaussian/2019/
Calculations performed in CBS-QB3 level of theory, with 1-D hindered rotors included in B3LYP/CBSB7 level
Reaction: C[CH]CCCCC1C=CC=CC=1 <=> CC1CCCCC12C=C[CH]C=C2
""",
)

entry(
    index = 46,
    label = "C12H17-29 <=> C12H17-30",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.86326e+12, 's^-1'),
        n = 0.527375,
        Ea = (90.7394, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (2000, 'K'),
    ),
    reference = Article(
        authors = ['Sarah Khanniche', 'Lawrence Lai', 'William H. Green'],
        title = 'Kinetics of Intramolecular Phenyl Migration and Fused Ring Formation in Hexylbenzene Radicals',
        journal = 'J. Phys. Chem. A.',
        volume = '122 (51)',
        pages = '9778-9791',
        year = '2018',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""Calculation performed by Sarah Khanniche, 2018, CBS-QB3 level of theory""",
    longDesc = 
u"""
Details published in https://pubs.acs.org/doi/10.1021/acs.jpca.8b09749
Location of calculations Pharos/home/laitcl/Gaussian/2019/
Calculations performed in CBS-QB3 level of theory, with 1-D hindered rotors included in B3LYP/CBSB7 level
Reaction: CC1CCCCC12C=C[CH]C=C2 <=> [CH2]CCCC(C)C1C=CC=CC=1
""",
)

entry(
    index = 47,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.32e+08, 's^-1'),
        n = 0.97,
        Ea = (8.9, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 48,
    label = "C5H9 <=> C5H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.56e+08, 's^-1'),
        n = 1,
        Ea = (9.3, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 49,
    label = "C6H11-3 <=> C6H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.47e+08, 's^-1'),
        n = 1.11,
        Ea = (9.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 50,
    label = "C5H9-3 <=> C5H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.68e+09, 's^-1'),
        n = 0.84,
        Ea = (9.2, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling" Trans conformation of pentenyl.
""",
)

entry(
    index = 51,
    label = "C5H9-7 <=> C5H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.08e+09, 's^-1'),
        n = 0.9,
        Ea = (7.3, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 52,
    label = "C5H9-9 <=> C5H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.52e+08, 's^-1'),
        n = 0.89,
        Ea = (10.4, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 53,
    label = "C6H11-13 <=> C6H11-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.85e+09, 's^-1'),
        n = 0.75,
        Ea = (6.2, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 54,
    label = "C6H11-7 <=> C6H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.9e+09, 's^-1'),
        n = 0.79,
        Ea = (8.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 55,
    label = "C5H9-5 <=> C5H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.07e+06, 's^-1'),
        n = 1.46,
        Ea = (14.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 56,
    label = "C6H11-9 <=> C6H11-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.73e+06, 's^-1'),
        n = 1.31,
        Ea = (13.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 57,
    label = "C7H13-9 <=> C7H13-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (102000, 's^-1'),
        n = 1.8,
        Ea = (11.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 58,
    label = "C6H11-11 <=> C6H11-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.65e+06, 's^-1'),
        n = 1.3,
        Ea = (13.8, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling" Trans conformation of hexenyl.
""",
)

entry(
    index = 59,
    label = "C6H11-15 <=> C6H11-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.52e+07, 's^-1'),
        n = 1,
        Ea = (13, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 60,
    label = "C6H11-17 <=> C6H11-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.15e+07, 's^-1'),
        n = 1.08,
        Ea = (12.7, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 61,
    label = "C6H11-19 <=> C6H11-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.48e+06, 's^-1'),
        n = 1.25,
        Ea = (15, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 62,
    label = "C7H13-17 <=> C7H13-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.2e+06, 's^-1'),
        n = 1.3,
        Ea = (11.7, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 63,
    label = "C7H13-19 <=> C7H13-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.6e+07, 's^-1'),
        n = 1.13,
        Ea = (12.4, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 64,
    label = "C7H13-13 <=> C7H13-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.53e+07, 's^-1'),
        n = 1.02,
        Ea = (13.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 65,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (698000, 's^-1'),
        n = 1.33,
        Ea = (4.7, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 66,
    label = "C7H13 <=> C7H13-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (187000, 's^-1'),
        n = 1.48,
        Ea = (3.9, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 67,
    label = "C8H15 <=> C8H15-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (126000, 's^-1'),
        n = 1.48,
        Ea = (3.7, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 68,
    label = "C7H13-3 <=> C7H13-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.72e+06, 's^-1'),
        n = 1.2,
        Ea = (4.3, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling" Trans conformation of heptenyl.
""",
)

entry(
    index = 69,
    label = "C7H13-21 <=> C7H13-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (184000, 's^-1'),
        n = 1.4,
        Ea = (6.2, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 70,
    label = "C7H13-23 <=> C7H13-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.25e+06, 's^-1'),
        n = 1.22,
        Ea = (3.7, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 71,
    label = "C7H13-25 <=> C7H13-26",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.07e+06, 's^-1'),
        n = 1.02,
        Ea = (3.9, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 72,
    label = "C7H13-27 <=> C7H13-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.75e+06, 's^-1'),
        n = 1.04,
        Ea = (4.5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 73,
    label = "C8H15-17 <=> C8H15-18",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.05e+06, 's^-1'),
        n = 1.03,
        Ea = (3.2, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 74,
    label = "C8H15-19 <=> C8H15-20",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.37e+07, 's^-1'),
        n = 0.85,
        Ea = (4.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 75,
    label = "C8H15-21 <=> C8H15-22",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.18e+07, 's^-1'),
        n = 0.99,
        Ea = (4.3, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 76,
    label = "C8H15-5 <=> C8H15-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+07, 's^-1'),
        n = 0.9,
        Ea = (4.3, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 77,
    label = "C7H13-15 <=> C7H13-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (153000, 's^-1'),
        n = 1.26,
        Ea = (5.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 78,
    label = "C8H15-13 <=> C8H15-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (18700, 's^-1'),
        n = 1.43,
        Ea = (4.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 79,
    label = "C9H17-7 <=> C9H17-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2020, 's^-1'),
        n = 1.67,
        Ea = (2.6, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 80,
    label = "C8H15-15 <=> C8H15-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (414000, 's^-1'),
        n = 1.14,
        Ea = (5, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling" Trans conformation of octenyl.
""",
)

entry(
    index = 81,
    label = "C8H15-23 <=> C8H15-24",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (24600, 's^-1'),
        n = 1.32,
        Ea = (6.1, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

entry(
    index = 82,
    label = "C9H17-11 <=> C9H17-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (216000, 's^-1'),
        n = 1.18,
        Ea = (4.3, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    reference = Article(
        authors = ['K. Wang', 'S. Villano', 'A. Dean'],
        title = 'Reactivity-Structure-Based Rate Estimation Rules for Alkyl Radical H Atom Shift and Alkenyl Radical Cycloaddition Reactions',
        journal = 'J. Phys. Chem. A',
        volume = '119(28)',
        pages = '7205-7221',
        year = '2015',
    ),
    referenceType = "theory",
    rank = 5,
    shortDesc = u"""CBS-QB3 calculation with 1-d rotor treatment at B3LYP/6-31G(d)""",
    longDesc = 
u"""
Quantum chemistry calculations CBS-QB3 calculation with 1-d rotor treatment at 
B3LYP/6-31G(d) using Gaussian 03 and Gaussian 09. High-pressure-limit rate 
coefficient computed using TST with Eckart Tunnelling"
""",
)

