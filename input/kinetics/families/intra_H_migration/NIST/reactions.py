#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/NIST"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "CH3O <=> CH3O-2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (108.92, 'kJ/mol', '+|-', 9.811),
        T0 = (1, 'K'),
        Tmin = (393, 'K'),
        Tmax = (473, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Batt, L.", "Burrows, J.P.", "Robinson, G.N."],
        title = u'On the Isomerisation of the Methoxy Radical: Relevance to Atmospheric Chemistry and Combustion',
        journal = "Chem. Phys. Lett.",
        volume = "78",
        pages = """467""",
        year = "1981",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1981BAT/BUR467:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00010565
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010565/rk00000001.xml
Rate constant is an upper limit.
Bath gas: N2
""",
)

entry(
    index = 2,
    label = "C3H7 <=> C3H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.56e+10, 's^-1'),
        n = 0.88,
        Ea = (156.063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010505
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010505/rk00000001.xml
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.
""",
)

entry(
    index = 3,
    label = "C2H3O <=> C2H3O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+13, 's^-1'),
        n = 0,
        Ea = (197.053, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (800, 'K'),
        Tmax = (1220, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Colket, M.B., III", "Naegeli, D.W.", "Glassman, I."],
        title = u'High-Temperature Pyrolysis of Acetaldehyde',
        journal = "Int. J. Chem. Kinet.",
        volume = "7",
        pages = """223""",
        year = "1975",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1975COL/NAE223:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00012711
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012711/rk00000001.xml
Bath gas: N2
""",
)

entry(
    index = 4,
    label = "C3H5 <=> C3H5-2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2e+13, 's^-1'),
        n = 0,
        Ea = (197.053, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (302, 'K'),
    ),
    reference = Article(
        authors = ["Ondruschka, B.", "Ziegler, U.", "Zimmermann, G."],
        title = u'Zu moglichen umlagerungen zwischen isomeren C3H5-radikalen',
        journal = "Z. Phys. Chem. (Leipzig)",
        volume = "267",
        pages = """1127""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986OND/ZIE1127:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00015630
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015630/rk00000001.xml
""",
)

entry(
    index = 5,
    label = "C3H5-2 <=> C3H5",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+12, 's^-1'),
        n = 0,
        Ea = (147.166, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (302, 'K'),
    ),
    reference = Article(
        authors = ["Ondruschka, B.", "Ziegler, U.", "Zimmermann, G."],
        title = u'Zu moglichen umlagerungen zwischen isomeren C3H5-radikalen',
        journal = "Z. Phys. Chem. (Leipzig)",
        volume = "267",
        pages = """1127""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986OND/ZIE1127:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Other theoretical""",
    longDesc = 
u"""
PrIMe Reaction: r00015630
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015630/rk00000002.xml
""",
)

entry(
    index = 6,
    label = "C4H9 <=> C4H9-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.32e+12, 's^-1'),
        n = 0,
        Ea = (137.189, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (305, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (120000, 'Pa'),
    ),
    reference = Article(
        authors = ["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."],
        title = u'Isomerization of chemically activated secondary butyl radical',
        journal = "React. Kinet. Catal. Lett.",
        volume = "36",
        pages = """435""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GIE/GAW435:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011212
Bath gas: H2S
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 7,
    label = "C4H9 <=> C4H9-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.2e+14, 's^-1'),
        n = 0,
        Ea = (171.278, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (823, 'K'),
        Tmax = (999, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (80000, 'Pa'),
    ),
    reference = Article(
        authors = ["Lin, M.C.", "Back, M.H."],
        title = u'The thermal decomposition of ethane. Part III. Secondary reactions',
        journal = "Can. J. Chem.",
        volume = "44",
        pages = """2369""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966LIN/BAC2369:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011212
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011212/rk00000001.xml
Bath gas: C2H6
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 8,
    label = "C4H9 <=> C4H9-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.8e+10, 's^-1'),
        n = 0.67,
        Ea = (153.134, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011212
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,3 Hydrogen shift
""",
)

entry(
    index = 9,
    label = "C4H9 <=> C4H9-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.56e+10, 's^-1'),
        n = 0.88,
        Ea = (156.063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011212
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,2 Hydrogen shift
""",
)

entry(
    index = 10,
    label = "C4H9-2 <=> C4H9",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+12, 's^-1'),
        n = 0,
        Ea = (153.818, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        Tmax = (305, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (120000, 'Pa'),
    ),
    reference = Article(
        authors = ["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."],
        title = u'Isomerization of chemically activated secondary butyl radical',
        journal = "React. Kinet. Catal. Lett.",
        volume = "36",
        pages = """435""",
        year = "1988",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1988GIE/GAW435:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011212
Bath gas: H2S
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 11,
    label = "C4H7 <=> C4H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.56e+10, 's^-1'),
        n = 0.88,
        Ea = (123.846, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00010707
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010707/rk00000001.xml
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.
""",
)

entry(
    index = 12,
    label = "C4H9-3 <=> C4H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.56e+10, 's^-1'),
        n = 0.88,
        Ea = (144.766, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00012770
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012770/rk00000001.xml
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.
""",
)

entry(
    index = 13,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.2e+11, 's^-1'),
        n = 0,
        Ea = (83.976, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (438, 'K'),
        Tmax = (923, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Marshall, R.M."],
        title = u'The rate constant for the intramolecular isomerization of pentyl radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "22",
        pages = """935-950""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990MAR935-950:3",
    ),
    referenceType = "review",
    shortDesc = u"""Experimental value and limited review""",
    longDesc = 
u"""
PrIMe Reaction: r00011467
Bath gas: n-C5H12
""",
)

entry(
    index = 14,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (9.12e+11, 's^-1', '*|/', 10),
        n = 0,
        Ea = (98.111, 'kJ/mol', '+|-', 8.813),
        T0 = (1, 'K'),
        Tmin = (737, 'K'),
        Tmax = (923, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (26700, 'Pa'),
    ),
    reference = Article(
        authors = ["Marshall, R.M."],
        title = u'The rate constant for the intramolecular isomerization of pentyl radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "22",
        pages = """935-950""",
        year = "1990",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1990MAR935-950:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011467
Uncertainty: 10.0
Bath gas: n-C5H12
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 15,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.3e+08, 's^-1'),
        n = 0,
        Ea = (63.19, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (297, 'K'),
        Tmax = (435, 'K'),
        Pmin = (13.33, 'Pa'),
        Pmax = (3960, 'Pa'),
    ),
    reference = Article(
        authors = ["Watkins, K.W."],
        title = u'Photolysis of n-Pentylazomethane Vapor. Reactions of the n-Pentyl Radical',
        journal = "J. Am. Chem. Soc.",
        volume = "93",
        pages = """6355""",
        year = "1971",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1971WAT6355:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00011467
Bath gas: CO2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 16,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.4e+07, 's^-1'),
        n = 0,
        Ea = (45.148, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (439, 'K'),
        Tmax = (503, 'K'),
        Pmin = (8933, 'Pa'),
        Pmax = (8933, 'Pa'),
    ),
    reference = Article(
        authors = ["Endrenyi, L.", "Le Roy, D.J."],
        title = u'The isomerization of n-pentyl and 4-oxo-1-pentyl radicals in the gas phase',
        journal = "J. Phys. Chem.",
        volume = "70",
        pages = """4081""",
        year = "1966",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1966END/LER4081:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011467
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011467/rk00000001.xml
Bath gas: (CH3)2CO
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 17,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.56e+10, 's^-1'),
        n = 0.88,
        Ea = (156.063, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011467
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,2 Hydrogen shift
""",
)

entry(
    index = 18,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.85e+11, 's^-1'),
        n = -0.12,
        Ea = (86.19, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:11",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011467
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,4 Hydrogen shift
""",
)

entry(
    index = 19,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.88e+08, 's^-1'),
        n = 0.85,
        Ea = (81.731, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (350, 'K'),
        Tmax = (1300, 'K'),
    ),
    reference = Article(
        authors = ["Yamauchi, N.", "Miyoshi, A.", "Kosaka, K.", "Koshi, M.", "Matsui, H."],
        title = u'Thermal decomposition and isomerization processes of alkyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """2723-2733""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999YAM/MIY2723-2733:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011467
Bath gas: Products
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 20,
    label = "C5H11 <=> C5H11-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.01e+11, 's^-1'),
        n = 0,
        Ea = (88.133, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (438, 'K'),
        Tmax = (502, 'K'),
    ),
    reference = Article(
        authors = ["Watkins, K.W."],
        title = u'On the rate constant for n-pentyl radical isomerization',
        journal = "Can. J. Chem.",
        volume = "50",
        pages = """3738""",
        year = "1972",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1972WAT3738:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011467
""",
)

entry(
    index = 21,
    label = "C5H11-3 <=> C5H11-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.8e+10, 's^-1'),
        n = 0.67,
        Ea = (153.134, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00011468
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011468/rk00000001.xml
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,3 Hydrogen shift
""",
)

entry(
    index = 22,
    label = "C4H9O <=> C4H9O-2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.51e+11, 's^-1'),
        n = 0,
        Ea = (32.26, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00015924
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000001.xml
Bath gas: N2
""",
)

entry(
    index = 23,
    label = "C4H9O <=> C4H9O-2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.51e+11, 's^-1'),
        n = 0,
        Ea = (32.26, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (590, 'K'),
        Tmax = (750, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Golden, D.M."],
        title = u'Alkoxy Radical Reactions: The Isomerization of n-Butoxy Radicals Generated from the Pyrolysis of n-Butyl Nitrite',
        journal = "Chem. Phys. Lett.",
        volume = "60",
        pages = """108""",
        year = "1978",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1978BAL/GOL108:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00015924
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000002.xml
Bath gas: n-C4H9ONO
""",
)

entry(
    index = 24,
    label = "C4H9O <=> C4H9O-2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.78e+11, 's^-1', '*|/', 5),
        n = 0,
        Ea = (33.341, 'kJ/mol', '+|-', 4.34),
        T0 = (1, 'K'),
        Tmin = (265, 'K'),
        Tmax = (393, 'K'),
        Pmin = (53300, 'Pa'),
        Pmax = (53300, 'Pa'),
    ),
    reference = Article(
        authors = ["Morabito, P.", "Heicklen, J."],
        title = u'The reactions of alkoxyl radicals with O2. IV. n-C4H9O radicals',
        journal = "Bull. Chem. Soc. Jpn.",
        volume = "60",
        pages = """2641""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987MOR/HEI2641:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00015924
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000003.xml
Uncertainty: 5.0
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 25,
    label = "C4H9O <=> C4H9O-2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.5e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (40.585, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (298, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00015924
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000005.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 26,
    label = "C4H9O <=> C4H9O-2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.43e+11, 's^-1'),
        n = 0,
        Ea = (34.183, 'kJ/mol'),
        T0 = (1, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Vereecken, L.", "Peeters, J."],
        title = u'The 1,5-H-shift in 1-butoxy: A case study in the rigorous implementation of transition state theory for a multirotamer system',
        journal = "J. Chem. Phys.",
        volume = "119",
        pages = """5159-5170""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003VER/PEE5159-5170:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00015924
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015924/rk00000010.xml
Pressure dependence: Rate constant is pressure dependent

The authors have studied the 1-butoxy H-shift reaction, exploring several approaches for deriving rate constants for a reaction system with multiple reactant rotamers and multiple transition state conformers. It is shown that the various treatments are fully consistent, even if the TST expressions themselves appear different. Rate constants are derived at 298 K and 1 atm pressure and compared with the literature.
""",
)

entry(
    index = 27,
    label = "C6H13 <=> C6H13-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (183, 's^-1', '*|/', 1.5),
        n = 2.55,
        Ea = (45.863, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (1900, 'K'),
        Pmin = (150000, 'Pa'),
        Pmax = (500000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tsang, W.", "Walker, J.A.", "Manion, J.A."],
        title = u'The decomposition of normal hexyl radicals',
        journal = "Proc. Combust. Inst.",
        volume = "31",
        pages = """141-148""",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007TSA/WAL141-148:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Relative value normalized by a reference value""",
    longDesc = 
u"""
PrIMe Reaction: r00011474
Uncertainty: 1.5
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Shock tube
Excitation technique: Thermal
Time resolution: By end product analysis
Analytical technique: Gas chromatography

The high pressure rate expression is based on an RRKM/Master Equation analysis of the the data taken at 1.5 to 5 bar and 890-1020 K. Absolute values were derived assuming
k(1-hexyl -> n-butyl + ethene)/s-1= 1.02x1012T0.30exp(-13726/T)
This expression was derived via detailed balance and low temperature data on the reverse addition 
(Kerr&Parsonage;, Evaluated Kinetic Data ..., Butterworth, London, 1972).

1-hexyl was generated from the n-hexyl iodide and the products of isomerization and decomposition determined. An RRKM model was developed and high pressure rate constants determined normalizing the relative rates against literature values for beta bond fission reactions for the radical. Tabular results for fall-off effect are presented for T = 500-1900 K and pressures of 0.1 - 1000 bar.
""",
)

entry(
    index = 28,
    label = "C6H13 <=> C6H13-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+09, 's^-1', '*|/', 2),
        n = 0,
        Ea = (48.557, 'kJ/mol', '+|-', 1.455),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (453, 'K'),
        Pmin = (14500, 'Pa'),
        Pmax = (28000, 'Pa'),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Reti, F.", "Marta, F."],
        title = u'Isomerization of n-hexyl and s-octyl radicals by 1,5 and 1,4 intramolecular hydrogen atom transfer reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """895""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987DOB/BER895:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011474
Uncertainty: 2.0
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 29,
    label = "C6H13 <=> C6H13-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+07, 's^-1'),
        n = 0,
        Ea = (34.754, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (352, 'K'),
        Tmax = (400, 'K'),
        Pmin = (6133, 'Pa'),
        Pmax = (6133, 'Pa'),
    ),
    reference = Article(
        authors = ["Watkins, K.W.", "Ostreko, L.A."],
        title = u'Isomerization of n-hexyl radicals in the gas phase',
        journal = "J. Phys. Chem.",
        volume = "73",
        pages = """2080""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969WAT/OST2080:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011474
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011474/rk00000001.xml
Bath gas: C2H4
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 30,
    label = "C6H13 <=> C6H13-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.65e+07, 's^-1'),
        n = 0.82,
        Ea = (52.049, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (350, 'K'),
        Tmax = (1300, 'K'),
    ),
    reference = Article(
        authors = ["Yamauchi, N.", "Miyoshi, A.", "Kosaka, K.", "Koshi, M.", "Matsui, H."],
        title = u'Thermal decomposition and isomerization processes of alkyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "103",
        pages = """2723-2733""",
        year = "1999",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1999YAM/MIY2723-2733:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Transition state theory""",
    longDesc = 
u"""
PrIMe Reaction: r00011474
Bath gas: Products
Pressure dependence: Rate constant is high pressure limit
""",
)

entry(
    index = 31,
    label = "C6H13 <=> C6H13-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+10, 's^-1'),
        n = 0,
        Ea = (71.172, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (723, 'K'),
        Tmax = (823, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Imbert, F.E.", "Marshall, R.M."],
        title = u'The mechanism and rate parameters for the pyrolysis of n-hexane in the range 723-823 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """81""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987IMB/MAR81:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011474
Bath gas: N2
""",
)

entry(
    index = 32,
    label = "C6H13-2 <=> C6H13",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.51e+10, 's^-1'),
        n = 0,
        Ea = (88.133, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (723, 'K'),
        Tmax = (823, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (13300, 'Pa'),
    ),
    reference = Article(
        authors = ["Imbert, F.E.", "Marshall, R.M."],
        title = u'The mechanism and rate parameters for the pyrolysis of n-hexane in the range 723-823 K',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """81""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987IMB/MAR81:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011474
Bath gas: N2
""",
)

entry(
    index = 33,
    label = "C5H11O <=> C5H11O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (33.054, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:4",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000088
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000088/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 34,
    label = "C5H11O-3 <=> C5H11O-4",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (3.1e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (40.585, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000089
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000089/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 35,
    label = "C6H11 <=> C6H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+11, 's^-1'),
        n = 0,
        Ea = (84.808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (23300, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Addition of cyclopentane to slowly reacting mixtures of H2 + O2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "91",
        pages = """1431-1438""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995HAN/WAL1431-1438:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00015688
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015688/rk00000001.xml
Bath gas: O2
""",
)

entry(
    index = 36,
    label = "C6H11-3 <=> C6H11-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+12, 's^-1'),
        n = 0,
        Ea = (124.717, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1300, 'K'),
        Pmin = (23300, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Addition of cyclopentane to slowly reacting mixtures of H2 + O2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "91",
        pages = """1431-1438""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995HAN/WAL1431-1438:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00015689
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015689/rk00000001.xml
Bath gas: O2
""",
)

entry(
    index = 37,
    label = "C6H11-3 <=> C6H11-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.67e+12, 's^-1'),
        n = -0.6,
        Ea = (64.015, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    reference = Article(
        authors = ["Matheu, D.M.", "Green, W.H.", "Grenda, J.M."],
        title = u'Capturing pressure-dependence in automated mechanism generation: Reactions through cycloalkyl intermediates',
        journal = "Int. J. Chem. Kinet.",
        volume = "35",
        pages = """95-119""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:13",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00015689
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015689/rk00000002.xml
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,4 Hydrogen shift
""",
)

entry(
    index = 38,
    label = "C4H9O2 <=> C4H9O2-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.58e+11, 's^-1'),
        n = 0,
        Ea = (27.188, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (450, 'K'),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1977BAL/BAR2483:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00016683
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016683/rk00000001.xml
Bath gas: N2
""",
)

entry(
    index = 39,
    label = "C5H11O-5 <=> C5H11O-6",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.4e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (38.911, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (298, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00017157
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017157/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 40,
    label = "C5H11O-5 <=> C5H11O-6",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (1.26e+11, 's^-1', '*|/', 5),
        n = 0,
        Ea = (39.743, 'kJ/mol', '+|-', 4.773),
        T0 = (1, 'K'),
        Tmin = (279, 'K'),
        Tmax = (385, 'K'),
        Pmin = (15100, 'Pa'),
        Pmax = (15100, 'Pa'),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Marta, F."],
        title = u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """329""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986DOB/BER329:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00017157
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017157/rk00000005.xml
Uncertainty: 5.0
Bath gas: CO2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 41,
    label = "C5H11O2 <=> C5H11O2-2",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.58e+12, 's^-1', '*|/', 10),
        n = 0,
        Ea = (123.054, 'kJ/mol', '+|-', 9.811),
        T0 = (1, 'K'),
        Tmin = (660, 'K'),
        Tmax = (750, 'K'),
        Pmin = (53300, 'Pa'),
        Pmax = (200000, 'Pa'),
    ),
    reference = Article(
        authors = ["Hughes, K.J.", "Halford-Maw, P.A.", "Lightfoot, P.D.", "Turanyi, T.", "Pilling, M.J."],
        title = u'Direct measurements of the neopentyl peroxy-hydroperoxy radical isomerisation over the temperature range 660-750 K',
        journal = "Symp. Int. Combust. Proc.",
        volume = "24",
        pages = """645-652""",
        year = "1992",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1992HUG/HAL645-652:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
PrIMe Reaction: r00016217
Uncertainty: 10.0
Bath gas: He
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
)

entry(
    index = 42,
    label = "C5H11O2 <=> C5H11O2-2",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.2e+13, 's^-1'),
        n = 0,
        Ea = (119.728, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (653, 'K'),
        Tmax = (793, 'K'),
        Pmin = (66700, 'Pa'),
        Pmax = (66700, 'Pa'),
    ),
    reference = Article(
        authors = ["Baldwin, R.R.", "Hisham, M.W.M.", "Walker, R.W."],
        title = u'Arrhenius parameters of elementary reactions involved in the oxidation of neopentane',
        journal = "J. Chem. Soc. Faraday Trans. 1",
        volume = "78",
        pages = """1615""",
        year = "1982",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAL/HIS1615:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016217
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016217/rk00000002.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
)

entry(
    index = 43,
    label = "C5H11O2 <=> C5H11O2-2",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (8.87e+07, 's^-1'),
        n = 1.07,
        Ea = (98.667, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (900, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sun, H.", "Bozzelli, J.W."],
        title = u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """1694-1711""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:21",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016217

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
)

entry(
    index = 44,
    label = "C5H11O2 <=> C5H11O2-2",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.44e+35, 's^-1'),
        n = -7.2,
        Ea = (146.243, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (900, 'K'),
        Tmax = (2500, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Sun, H.", "Bozzelli, J.W."],
        title = u'Thermochemical and kinetic analysis on the reactions of neopentyl and hydroperoxy-neopentyl radicals with oxygen: Part I.  OH and initial stable HC product formation',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """1694-1711""",
        year = "2004",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:22",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016217

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
)

entry(
    index = 45,
    label = "C6H13O <=> C6H13O-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.4e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (32.217, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:8",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000087
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000087/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 46,
    label = "C6H13O-3 <=> C6H13O-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.5e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (30.962, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000091
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000091/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 47,
    label = "C6H13O-5 <=> C6H13O-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.7e+11, 's^-1', '*|/', 5), n=0, Ea=(20.92, 'kJ/mol'), T0=(1, 'K')),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000092
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000092/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 48,
    label = "C6H13O-7 <=> C6H13O-8",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.1e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (37.656, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000093
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000093/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 49,
    label = "C6H13O-9 <=> C6H13O-10",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.3e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (40.166, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:5",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000094
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000094/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 50,
    label = "C7H15O <=> C7H15O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+11, 's^-1', '*|/', 5),
        n = 0,
        Ea = (15.481, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:10",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000033
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000033/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 51,
    label = "C7H15O-3 <=> C7H15O-4",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+12, 's^-1', '*|/', 5),
        n = 0,
        Ea = (29.288, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:11",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000034
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000034/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

entry(
    index = 52,
    label = "C6H11O2 <=> C6H11O2-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.51e+11, 's^-1'),
        n = 0,
        Ea = (112.5, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (793, 'K'),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Arrhenius Parameters for the Reaction HO2 + Cyclohexane Between 673 and 773 K, and for H Atom Transfer in Cyclohexylperoxy Radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "3",
        pages = """2043-2052""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001HAN/WAL2043-2052:5",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010491
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010491/rk00000001.xml
Pressure dependence: None reported
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Thermal
Time resolution: By end product analysis
Analytical technique: Gas chromatography

Derived from end product yields in the overall reaction of cyclohexyl + O2.
""",
)

entry(
    index = 53,
    label = "C6H11O2-3 <=> C6H11O2-4",
    degeneracy = 8,
    kinetics = Arrhenius(
        A = (2.57e+12, 's^-1'),
        n = 0,
        Ea = (123.5, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (793, 'K'),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Arrhenius Parameters for the Reaction HO2 + Cyclohexane Between 673 and 773 K, and for H Atom Transfer in Cyclohexylperoxy Radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "3",
        pages = """2043-2052""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001HAN/WAL2043-2052:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010492
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010492/rk00000001.xml
Pressure dependence: None reported
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Thermal
Time resolution: By end product analysis
Analytical technique: Gas chromatography

Derived from end product yields in the overall reaction of cyclohexyl + O2.
""",
)

entry(
    index = 54,
    label = "C6H11O2-5 <=> C6H11O2-6",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.47e+12, 's^-1'),
        n = 0,
        Ea = (135.7, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (673, 'K'),
        Tmax = (793, 'K'),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Arrhenius Parameters for the Reaction HO2 + Cyclohexane Between 673 and 773 K, and for H Atom Transfer in Cyclohexylperoxy Radicals',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "3",
        pages = """2043-2052""",
        year = "2001",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2001HAN/WAL2043-2052:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00010493
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00010493/rk00000001.xml
Pressure dependence: None reported
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Thermal
Time resolution: By end product analysis
Analytical technique: Gas chromatography

Derived from end product yields in the overall reaction of cyclohexyl + O2.
""",
)

entry(
    index = 55,
    label = "C8H17 <=> C8H17-2",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+10, 's^-1', '*|/', 5),
        n = 0,
        Ea = (71.172, 'kJ/mol', '+|-', 8.564),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (385, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (100000, 'Pa'),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Reti, F.", "Marta, F."],
        title = u'Isomerization of n-hexyl and s-octyl radicals by 1,5 and 1,4 intramolecular hydrogen atom transfer reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """895""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987DOB/BER895:2",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011969
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011969/rk00000001.xml
Uncertainty: 5.0
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 56,
    label = "C8H17-3 <=> C8H17-4",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.51e+09, 's^-1', '*|/', 5),
        n = 0,
        Ea = (46.894, 'kJ/mol', '+|-', 4.215),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (385, 'K'),
        Pmin = (6666, 'Pa'),
        Pmax = (100000, 'Pa'),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Reti, F.", "Marta, F."],
        title = u'Isomerization of n-hexyl and s-octyl radicals by 1,5 and 1,4 intramolecular hydrogen atom transfer reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "19",
        pages = """895""",
        year = "1987",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1987DOB/BER895:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00017030
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017030/rk00000001.xml
Uncertainty: 5.0
Bath gas: N2
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
)

entry(
    index = 57,
    label = "C8H7 <=> C8H7-2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (4.57e+09, 's^-1'),
        n = 0.81,
        Ea = (109.914, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003TOK/LIN11397-11408:7",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00017124
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017124/rk00000001.xml

Ab initio study of reaction pathways for C6H4 (phenyl) plus C2H2 (acetylene). Used G2M(CC5) method (see paper for details). Calculated many different reaction pathways and intermediates. Only a few of the more important ones are abstracted here. Rate expressions for different pressures for some of the channels are also given in the paper. See paper for further details. Used NIST ChemRate program to calculated rate expressions from ab initio transition states. In paper also provide DfHo heats of formation for many of the intermediates.
""",
)

entry(
    index = 58,
    label = "C8H7-2 <=> C8H7",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.04e+10, 's^-1'),
        n = 0.7,
        Ea = (115.06, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (250, 'K'),
        Tmax = (2000, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (101000, 'Pa'),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003TOK/LIN11397-11408:6",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00017124
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017124/rk00000002.xml

Ab initio study of reaction pathways for C6H4 (phenyl) plus C2H2 (acetylene). Used G2M(CC5) method (see paper for details). Calculated many different reaction pathways and intermediates. Only a few of the more important ones are abstracted here. Rate expressions for different pressures for some of the channels are also given in the paper. See paper for further details. Used NIST ChemRate program to calculated rate expressions from ab initio transition states. In paper also provide DfHo heats of formation for many of the intermediates.
""",
)

entry(
    index = 59,
    label = "C8H17O <=> C8H17O-2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.6e+11, 's^-1', '*|/', 5),
        n = 0,
        Ea = (16.318, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["Mereau, R.", "Rayez, M.T.", "Caralp, F.", "Rayez, J.C."],
        title = u'Isomerization reactions of alkoxy radicals: theoretical study and structure-activity relationships',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "5",
        pages = """4828-4833""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:12",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00000090
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00000090/rk00000001.xml
Uncertainty: 5.0
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5

It is not clear (to R.H.West) that the tunneling corrections were applied to the rate expressions cited here.
In fact, by crunching the numbers it looks like they were not. The valid temperature range is almost certainly
not 298-298K, as suggested by NIST. How large it is, however, is personal judgement (or the rates should be refit 
with the tunneling corrections included). DOI: 10.1039/b307708j
""",
)

