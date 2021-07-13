#!/usr/bin/env python
# encoding: utf-8

name = "Diels_alder_addition_Aromatic/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C6H6 + C6H4 <=> C12H10",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(5809,'cm^3/(mol*s)'), n=2.526, Ea=(5.92,'kcal/mol'), T0=(1,'K')),
    reference = Article(
        authors = ['Comandini, A.', 'Brezinsky, K.'],
        title = 'Theoretical Study of the Formation of Naphthalene from the Radical/pi-Bond Addition between Single-Ring Aromatic Hydrocarbons',
        journal = 'The Journal of Physical Chemistry A',
        volume = '115',
        pages = '5547-5559',
        year = '2011',
    ),
    referenceType = "theory",
    rank = 6,
    longDesc = 
"""
uCCSD(T) with Dunning's correclation-consistent polarized double basis set (cc-pVDZ), TST.
""",
)

entry(
    index = 1,
    label = "C12H10-2 <=> C2H2 + C10H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(7.458e+14,'s^-1'), n=0.0956, Ea=(54.82,'kcal/mol'), T0=(1,'K')),
    reference = Article(
        authors = ['Comandini, A.', 'Brezinsky, K.'],
        title = 'Theoretical Study of the Formation of Naphthalene from the Radical/pi-Bond Addition between Single-Ring Aromatic Hydrocarbons',
        journal = 'The Journal of Physical Chemistry A',
        volume = '115',
        pages = '5547-5559',
        year = '2011',
    ),
    referenceType = "theory",
    rank = 6,
    longDesc = 
"""
uCCSD(T) with Dunning's correclation-consistent polarized double basis set (cc-pVDZ), TST.
""",
)

entry(
    index = 2,
    label = "C12H10-3 + C2H2 <=> C14H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(16.92,'cm^3/(mol*s)'), n=2.6, Ea=(42.193,'kcal/mol'), T0=(1,'K')),
    rank = 8,
    longDesc = 
"""
V. V. Kislov, N. I. Islamova, A. M. Kolker, S. H. Lin, and A. M. Mebel;
Hydrogen Abstraction Acetylene Addition and Diels-Alder Mechanisms of PAH Formation: A Detailed Study Using First Principles Calculations;
J. Chem. Theory Comput. 2005, 1, 908-924.
Original entry: B1 + C2H2 <=> B2
""",
)

entry(
    index = 3,
    label = "C14H10 + C2H2 <=> C16H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(43.24,'cm^3/(mol*s)'), n=2.58, Ea=(41.945,'kcal/mol'), T0=(1,'K')),
    rank = 8,
    longDesc = 
"""
V. V. Kislov, N. I. Islamova, A. M. Kolker, S. H. Lin, and A. M. Mebel;
Hydrogen Abstraction Acetylene Addition and Diels-Alder Mechanisms of PAH Formation: A Detailed Study Using First Principles Calculations;
J. Chem. Theory Comput. 2005, 1, 908-924.
Original entry: P + C2H2 <=> P1
""",
)

entry(
    index = 4,
    label = "C6H6 + C2H2 <=> C8H8",
    degeneracy = 6.0,
    kinetics = Arrhenius(A=(261.981,'cm^3/(mol*s)'), n=2.6786, Ea=(147.644,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2500,'K')),
    reference = Article(
        authors = ['Liu, M.', 'Chu, T.-C.', 'Jocher, A.', 'Smith, M. C.', 'Lengyel, I.', 'Green, W. H.'],
        title = 'Predicting Polycyclic Aromatic Hydrocarbon Formation with an Automatically Generated Mechanism for Acetylene Pyrolysis',
        journal = 'Int. J. Chem. Kinet.',
        volume = '53',
        pages = '1–29',
        year = '2020',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
"""
CBS-QB3 calculation by MLIU
M. Liu, T. -C. Chu, A. Jocher, M. C. Smith, I, Lengyel, and W. H. Green;
Predicting Polycyclic Aromatic Hydrocarbon Formation with an Automatically Generated Mechanism for Acetylene Pyrolysis;
Int. J. Chem. Kinet. 2020, 53, 1–29. https://doi.org/https://doi.org/10.1002/kin.21421.
""",
)

entry(
    index = 5,
    label = "C10H8 + C2H2 <=> C12H10-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(A=(286.399,'cm^3/(mol*s)'), n=2.61957, Ea=(115.627,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2500,'K')),
    reference = Article(
        authors = ['Liu, M.', 'Chu, T.-C.', 'Jocher, A.', 'Smith, M. C.', 'Lengyel, I.', 'Green, W. H.'],
        title = 'Predicting Polycyclic Aromatic Hydrocarbon Formation with an Automatically Generated Mechanism for Acetylene Pyrolysis',
        journal = 'Int. J. Chem. Kinet.',
        volume = '53',
        pages = '1–29',
        year = '2020',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
"""
CBS-QB3 calculation by MLIU
M. Liu, T. -C. Chu, A. Jocher, M. C. Smith, I, Lengyel, and W. H. Green;
Predicting Polycyclic Aromatic Hydrocarbon Formation with an Automatically Generated Mechanism for Acetylene Pyrolysis;
Int. J. Chem. Kinet. 2020, 53, 1–29. https://doi.org/https://doi.org/10.1002/kin.21421.
""",
)

entry(
    index = 6,
    label = "C10H8-2 + C2H2 <=> C12H10-4",
    degeneracy = 8.0,
    kinetics = Arrhenius(A=(133.129,'cm^3/(mol*s)'), n=2.69336, Ea=(173.905,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2500,'K')),
    reference = Article(
        authors = ['Liu, M.', 'Chu, T.-C.', 'Jocher, A.', 'Smith, M. C.', 'Lengyel, I.', 'Green, W. H.'],
        title = 'Predicting Polycyclic Aromatic Hydrocarbon Formation with an Automatically Generated Mechanism for Acetylene Pyrolysis',
        journal = 'Int. J. Chem. Kinet.',
        volume = '53',
        pages = '1–29',
        year = '2020',
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
"""
CBS-QB3 calculation by MLIU
M. Liu, T. -C. Chu, A. Jocher, M. C. Smith, I, Lengyel, and W. H. Green;
Predicting Polycyclic Aromatic Hydrocarbon Formation with an Automatically Generated Mechanism for Acetylene Pyrolysis;
Int. J. Chem. Kinet. 2020, 53, 1–29. https://doi.org/https://doi.org/10.1002/kin.21421.
""",
)

