#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 72,
    label = "C10H9-29 <=> C10H9-30",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(6.258e+10, 's^-1'), n=0.21, Ea=(7.415, 'kcal/mol'), T0=(1, 'K')),
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

Duplicate reaction to 
A. M. Mebel, Y. Georgievskii, A. W. Jasper, S. J. Klippenstein, Temperature- and pressure-dependent rate coefficients for the HACA pathways from benzene to naphthalene, Proceedings of the Combustion Institute, 36(1), 919-926, 2017.

A. J. Vervust, M. R. Djokic, S. S. Merchant, H.-H. Carstensen, A. E. Long, G. B. Marin, W. H. Green, K. M. Van Geem, Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene, Energy & Fuels, 32(3), 3920-3934, 2018.
""",
)

entry(
    index = 76,
    label = "C9H11-5 <=> C9H11-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.255e+12, 's^-1'), n=0.347, Ea=(57.413, 'kcal/mol'), T0=(1, 'K')),
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

Thermo data for C9H11-6 is different for `SABIC_aromatics` library and group additivity.
""",
)

entry(
    index = 81,
    label = "C10H9-29 <=> C10H9-30",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.076e+11, 's^-1'), n=0.228, Ea=(6.982, 'kcal/mol'), T0=(1, 'K')),
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
Taken from entry: W3 <=> W4

Duplicate reaction to
A. M. Mebel, A. Landera, R. I. Kaiser, Formation Mechanisms of Naphthalene and Indene: From the Interstellar Medium to Combustion Flames, Journal of Physical Chemistry A, 121(5), 901-926, 2017.

A. J. Vervust, M. R. Djokic, S. S. Merchant, H.-H. Carstensen, A. E. Long, G. B. Marin, W. H. Green, K. M. Van Geem, Detailed Experimental and Kinetic Modeling Study of Cyclopentadiene Pyrolysis in the Presence of Ethene, Energy & Fuels, 32(3), 3920-3934, 2018.
""",
)

entry(
    index = 91,
    label = "C10H11-7 <=> C10H11-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.39e+10, 's^-1'), n=0.91, Ea=(36.4, 'kcal/mol'), T0=(1, 'K')),
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
Taken from entry: pdt8 <=> pdt9

Thermo data for C10H11-8 is different for `SABIC_aromatics`, `C10H11` library and group additivity.
""",
)

entry(
    index = 101,
    label = "C10H11-27 <=> C10H11-28",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.27e+10, 's^-1'), n=1.01, Ea=(40.7, 'kcal/mol'), T0=(1, 'K')),
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
Taken from entry: pdt23 <=> pdt9

Thermo data for C10H11-28 is different for `SABIC_aromatics`, `C10H11` library and group additivity.
""",
)

