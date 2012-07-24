#!/usr/bin/env python
# encoding: utf-8

name = "intra_H_migration/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1988GIE/GAW435:4",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *1 C 1 {2,S}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3 *2 C 0 {4,S} {5,S}
4 *1 C 1 {1,S} {3,S}
5 *3 H 0 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.32e+12,"s^-1"),
        n = 0,
        Ea = (137.189,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (295,"K"),
        Tmax = (305,"K"),
        Pmin = (1333,"Pa"),
        Pmax = (120000,"Pa"),
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
Category: Experiment
Data type: Absolute value measured directly
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:02:39 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988GIE/GAW435:4"""),
    ],
)

entry(
    index = 2,
    label = "1966LIN/BAC2369:4",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *1 C 1 {2,S}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3 *2 C 0 {4,S} {5,S}
4 *1 C 1 {1,S} {3,S}
5 *3 H 0 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.2e+14,"s^-1"),
        n = 0,
        Ea = (171.278,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (823,"K"),
        Tmax = (999,"K"),
        Pmin = (1333,"Pa"),
        Pmax = (80000,"Pa"),
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
Category: Experiment
Data type: Derived from fitting to a complex mechanism
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:02:39 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1966LIN/BAC2369:4"""),
    ],
)

entry(
    index = 3,
    label = "2003MAT/GRE95-119:8",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *1 C 1 {2,S}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3 *2 C 0 {4,S} {5,S}
4 *1 C 1 {1,S} {3,S}
5 *3 H 0 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.8e+10,"s^-1"),
        n = 0.67,
        Ea = (153.134,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
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
Category: Theory
Data type: Ab initio
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,3 Hydrogen shift
""",
    history = [
        ("Fri Jul 13 08:02:39 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:8"""),
    ],
)

entry(
    index = 4,
    label = "2003MAT/GRE95-119:7",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *1 C 1 {2,S}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3 *2 C 0 {4,S} {5,S}
4 *1 C 1 {1,S} {3,S}
5 *3 H 0 {3,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.56e+10,"s^-1"),
        n = 0.88,
        Ea = (156.063,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
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
Category: Theory
Data type: Ab initio
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,2 Hydrogen shift
""",
    history = [
        ("Fri Jul 13 08:02:39 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:7"""),
    ],
)

entry(
    index = 5,
    label = "1988GIE/GAW435:2",
    reactant1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3 *2 C 0 {4,S} {5,S}
4 *1 C 1 {1,S} {3,S}
5 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *1 C 1 {2,S}
5 *3 H 0 {2,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+12,"s^-1"),
        n = 0,
        Ea = (153.818,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (295,"K"),
        Tmax = (305,"K"),
        Pmin = (1333,"Pa"),
        Pmax = (120000,"Pa"),
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
Category: Experiment
Data type: Absolute value measured directly
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:02:40 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1988GIE/GAW435:2"""),
    ],
)

entry(
    index = 6,
    label = "1990MAR935-950:3",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *1 C 1 {3,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4 *2 C 0 {5,S} {6,S}
5 *1 C 1 {2,S} {4,S}
6 *3 H 0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.2e+11,"s^-1"),
        n = 0,
        Ea = (83.976,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (438,"K"),
        Tmax = (923,"K"),
        Pmin = (6666,"Pa"),
        Pmax = (26700,"Pa"),
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
Category: Review
Data type: Experimental value and limited review
""",
    history = [
        ("Fri Jul 13 08:02:57 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990MAR935-950:3"""),
    ],
)

entry(
    index = 7,
    label = "1990MAR935-950:4",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *1 C 1 {3,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4 *2 C 0 {5,S} {6,S}
5 *1 C 1 {2,S} {4,S}
6 *3 H 0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (9.12e+11,"s^-1","*|/",10),
        n = 0,
        Ea = (98.111,"kJ/mol","+|-",8.813),
        T0 = (1,"K"),
        Tmin = (737,"K"),
        Tmax = (923,"K"),
        Pmin = (6666,"Pa"),
        Pmax = (26700,"Pa"),
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
Category: Experiment
Data type: Derived from fitting to a complex mechanism
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:02:57 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1990MAR935-950:4"""),
    ],
)

entry(
    index = 8,
    label = "1971WAT6355:4",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *1 C 1 {3,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4 *2 C 0 {5,S} {6,S}
5 *1 C 1 {2,S} {4,S}
6 *3 H 0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.3e+08,"s^-1"),
        n = 0,
        Ea = (63.19,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (297,"K"),
        Tmax = (435,"K"),
        Pmin = (13.33,"Pa"),
        Pmax = (3960,"Pa"),
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
Category: Experiment
Data type: Absolute value measured directly
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:02:57 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1971WAT6355:4"""),
    ],
)

entry(
    index = 9,
    label = "1966END/LER4081:2",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *1 C 1 {3,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4 *2 C 0 {5,S} {6,S}
5 *1 C 1 {2,S} {4,S}
6 *3 H 0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (1.4e+07,"s^-1"),
        n = 0,
        Ea = (45.148,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (439,"K"),
        Tmax = (503,"K"),
        Pmin = (8933,"Pa"),
        Pmax = (8933,"Pa"),
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
Category: Experiment
Data type: Derived from fitting to a complex mechanism
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:02:57 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1966END/LER4081:2"""),
    ],
)

entry(
    index = 10,
    label = "2003MAT/GRE95-119:9",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *1 C 1 {3,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4 *2 C 0 {5,S} {6,S}
5 *1 C 1 {2,S} {4,S}
6 *3 H 0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.56e+10,"s^-1"),
        n = 0.88,
        Ea = (156.063,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
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
Category: Theory
Data type: Ab initio
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,2 Hydrogen shift
""",
    history = [
        ("Fri Jul 13 08:02:57 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:9"""),
    ],
)

entry(
    index = 11,
    label = "2003MAT/GRE95-119:11",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *1 C 1 {3,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4 *2 C 0 {5,S} {6,S}
5 *1 C 1 {2,S} {4,S}
6 *3 H 0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (7.85e+11,"s^-1"),
        n = -0.12,
        Ea = (86.19,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
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
Category: Theory
Data type: Ab initio
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,4 Hydrogen shift
""",
    history = [
        ("Fri Jul 13 08:02:57 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:11"""),
    ],
)

entry(
    index = 12,
    label = "1999YAM/MIY2723-2733:1",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *1 C 1 {3,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4 *2 C 0 {5,S} {6,S}
5 *1 C 1 {2,S} {4,S}
6 *3 H 0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (4.88e+08,"s^-1"),
        n = 0.85,
        Ea = (81.731,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (350,"K"),
        Tmax = (1300,"K"),
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
Category: Theory
Data type: Transition state theory
Pressure dependence: Rate constant is high pressure limit
""",
    history = [
        ("Fri Jul 13 08:02:57 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1999YAM/MIY2723-2733:1"""),
    ],
)

entry(
    index = 13,
    label = "1972WAT3738:1",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *2 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *1 C 1 {3,S}
6 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {5,S}
3    C 0 {1,S}
4 *2 C 0 {5,S} {6,S}
5 *1 C 1 {2,S} {4,S}
6 *3 H 0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (5.01e+11,"s^-1"),
        n = 0,
        Ea = (88.133,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (438,"K"),
        Tmax = (502,"K"),
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
Category: Theory
Data type: Estimated: thermochemical, kinetic, or other
""",
    history = [
        ("Fri Jul 13 08:02:57 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1972WAT3738:1"""),
    ],
)

entry(
    index = 14,
    label = "2003MAT/GRE95-119:10",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {6,S}
2    C 0 {1,S} {4,S}
3 *4 C 0 {1,S} {5,S}
4    C 0 {2,S}
5 *1 C 1 {3,S}
6 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {3,S} {5,S}
2 *4 C 0 {4,S} {5,S}
3    C 0 {1,S}
4 *2 C 0 {2,S} {6,S}
5 *1 C 1 {1,S} {2,S}
6 *3 H 0 {4,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.8e+10,"s^-1"),
        n = 0.67,
        Ea = (153.134,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (1500,"K"),
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
Category: Theory
Data type: Ab initio
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVDZ calculations of Sumathi.Ea is an adjusted value based on a reference reaction and the relative heats of reaction. See paper for more details.

1,3 Hydrogen shift
""",
    history = [
        ("Fri Jul 13 08:03:24 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:10"""),
    ],
)

entry(
    index = 15,
    label = "2007TSA/WAL141-148:2",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *2 C 0 {2,S} {6,S} {7,S}
5    C 0 {3,S}
6 *1 C 1 {4,S}
7 *3 H 0 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {6,S}
4    C 0 {2,S}
5 *2 C 0 {6,S} {7,S}
6 *1 C 1 {3,S} {5,S}
7 *3 H 0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (183,"s^-1","*|/",1.5),
        n = 2.55,
        Ea = (45.863,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (1900,"K"),
        Pmin = (150000,"Pa"),
        Pmax = (500000,"Pa"),
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
Category: Experiment
Data type: Relative value normalized by a reference value
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
    history = [
        ("Fri Jul 13 08:03:29 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2007TSA/WAL141-148:2"""),
    ],
)

entry(
    index = 16,
    label = "1987DOB/BER895:1",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *2 C 0 {2,S} {6,S} {7,S}
5    C 0 {3,S}
6 *1 C 1 {4,S}
7 *3 H 0 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {6,S}
4    C 0 {2,S}
5 *2 C 0 {6,S} {7,S}
6 *1 C 1 {3,S} {5,S}
7 *3 H 0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+09,"s^-1","*|/",2),
        n = 0,
        Ea = (48.557,"kJ/mol","+|-",1.455),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (453,"K"),
        Pmin = (14500,"Pa"),
        Pmax = (28000,"Pa"),
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
Category: Experiment
Data type: Derived from fitting to a complex mechanism
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:03:29 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987DOB/BER895:1"""),
    ],
)

entry(
    index = 17,
    label = "1969WAT/OST2080:1",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *2 C 0 {2,S} {6,S} {7,S}
5    C 0 {3,S}
6 *1 C 1 {4,S}
7 *3 H 0 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {6,S}
4    C 0 {2,S}
5 *2 C 0 {6,S} {7,S}
6 *1 C 1 {3,S} {5,S}
7 *3 H 0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2e+07,"s^-1"),
        n = 0,
        Ea = (34.754,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (352,"K"),
        Tmax = (400,"K"),
        Pmin = (6133,"Pa"),
        Pmax = (6133,"Pa"),
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
Category: Experiment
Data type: Derived from fitting to a complex mechanism
Excitation technique: Direct photolysis
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:03:29 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1969WAT/OST2080:1"""),
    ],
)

entry(
    index = 18,
    label = "1999YAM/MIY2723-2733:2",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *2 C 0 {2,S} {6,S} {7,S}
5    C 0 {3,S}
6 *1 C 1 {4,S}
7 *3 H 0 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {6,S}
4    C 0 {2,S}
5 *2 C 0 {6,S} {7,S}
6 *1 C 1 {3,S} {5,S}
7 *3 H 0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (6.65e+07,"s^-1"),
        n = 0.82,
        Ea = (52.049,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (350,"K"),
        Tmax = (1300,"K"),
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
Category: Theory
Data type: Transition state theory
Pressure dependence: Rate constant is high pressure limit
""",
    history = [
        ("Fri Jul 13 08:03:29 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1999YAM/MIY2723-2733:2"""),
    ],
)

entry(
    index = 19,
    label = "1987IMB/MAR81:6",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *2 C 0 {2,S} {6,S} {7,S}
5    C 0 {3,S}
6 *1 C 1 {4,S}
7 *3 H 0 {4,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {6,S}
4    C 0 {2,S}
5 *2 C 0 {6,S} {7,S}
6 *1 C 1 {3,S} {5,S}
7 *3 H 0 {5,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (3.16e+10,"s^-1"),
        n = 0,
        Ea = (71.172,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (723,"K"),
        Tmax = (823,"K"),
        Pmin = (1333,"Pa"),
        Pmax = (13300,"Pa"),
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
Category: Theory
Data type: Estimated: thermochemical, kinetic, or other
""",
    history = [
        ("Fri Jul 13 08:03:29 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987IMB/MAR81:6"""),
    ],
)

entry(
    index = 20,
    label = "1987IMB/MAR81:5",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {6,S}
4    C 0 {2,S}
5 *2 C 0 {6,S} {7,S}
6 *1 C 1 {3,S} {5,S}
7 *3 H 0 {5,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *2 C 0 {2,S} {6,S} {7,S}
5    C 0 {3,S}
6 *1 C 1 {4,S}
7 *3 H 0 {4,S}
""",
    degeneracy = 4,
    kinetics = Arrhenius(
        A = (2.51e+10,"s^-1"),
        n = 0,
        Ea = (88.133,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (723,"K"),
        Tmax = (823,"K"),
        Pmin = (1333,"Pa"),
        Pmax = (13300,"Pa"),
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
Category: Theory
Data type: Estimated: thermochemical, kinetic, or other
""",
    history = [
        ("Fri Jul 13 08:03:30 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1987IMB/MAR81:5"""),
    ],
)

entry(
    index = 21,
    label = "1992HUG/HAL645-652:1",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S}
3 *2 C 0 {1,S} {7,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *4 O 0 {2,S} {8,S}
7 *3 H 0 {3,S}
8 *1 O 1 {6,S}
""",
    product1 = 
"""
1 *4 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 C 1 {1,S}
6 *5 O 0 {2,S} {7,S}
7 *2 O 0 {6,S} {8,S}
8 *3 H 0 {7,S}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.58e+12,"s^-1","*|/",10),
        n = 0,
        Ea = (123.054,"kJ/mol","+|-",9.811),
        T0 = (1,"K"),
        Tmin = (660,"K"),
        Tmax = (750,"K"),
        Pmin = (53300,"Pa"),
        Pmax = (200000,"Pa"),
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
Category: Experiment
Data type: Absolute value measured directly
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Laser induced fluorescence
""",
    history = [
        ("Fri Jul 13 08:05:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1992HUG/HAL645-652:1"""),
    ],
)

entry(
    index = 22,
    label = "1982BAL/HIS1615:4",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S}
3 *2 C 0 {1,S} {7,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *4 O 0 {2,S} {8,S}
7 *3 H 0 {3,S}
8 *1 O 1 {6,S}
""",
    product1 = 
"""
1 *4 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 C 1 {1,S}
6 *5 O 0 {2,S} {7,S}
7 *2 O 0 {6,S} {8,S}
8 *3 H 0 {7,S}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.2e+13,"s^-1"),
        n = 0,
        Ea = (119.728,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (653,"K"),
        Tmax = (793,"K"),
        Pmin = (66700,"Pa"),
        Pmax = (66700,"Pa"),
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
Category: Experiment
Data type: Derived from fitting to a complex mechanism
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:05:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982BAL/HIS1615:4"""),
    ],
)

entry(
    index = 23,
    label = "2004SUN/BOZ1694-1711:21",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S}
3 *2 C 0 {1,S} {7,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *4 O 0 {2,S} {8,S}
7 *3 H 0 {3,S}
8 *1 O 1 {6,S}
""",
    product1 = 
"""
1 *4 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 C 1 {1,S}
6 *5 O 0 {2,S} {7,S}
7 *2 O 0 {6,S} {8,S}
8 *3 H 0 {7,S}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (8.87e+07,"s^-1"),
        n = 1.07,
        Ea = (98.667,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (300,"K"),
        Tmax = (900,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
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
Category: Theory
Data type: Ab initio

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
    history = [
        ("Fri Jul 13 08:05:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:21"""),
    ],
)

entry(
    index = 24,
    label = "2004SUN/BOZ1694-1711:22",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S}
3 *2 C 0 {1,S} {7,S}
4    C 0 {1,S}
5    C 0 {1,S}
6 *4 O 0 {2,S} {8,S}
7 *3 H 0 {3,S}
8 *1 O 1 {6,S}
""",
    product1 = 
"""
1 *4 C 0 {2,S} {3,S} {4,S} {5,S}
2    C 0 {1,S} {6,S}
3    C 0 {1,S}
4    C 0 {1,S}
5 *1 C 1 {1,S}
6 *5 O 0 {2,S} {7,S}
7 *2 O 0 {6,S} {8,S}
8 *3 H 0 {7,S}
""",
    degeneracy = 9,
    kinetics = Arrhenius(
        A = (1.44e+35,"s^-1"),
        n = -7.2,
        Ea = (146.243,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (900,"K"),
        Tmax = (2500,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
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
Category: Theory
Data type: Ab initio

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
    history = [
        ("Fri Jul 13 08:05:01 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:22"""),
    ],
)

entry(
    index = 25,
    label = "2003MER/RAY4828-4833:10",
    reactant1 = 
"""
1 *2 C 0 {2,S} {5,S} {6,S} {8,S}
2 *5 C 0 {1,S} {3,S}
3    C 0 {2,S} {4,S}
4 *4 C 0 {3,S} {7,S} {9,S}
5    C 0 {1,S}
6    C 0 {1,S}
7    C 0 {4,S}
8 *3 H 0 {1,S}
9 *1 O 1 {4,S}
""",
    product1 = 
"""
1 *5 C 0 {2,S} {4,S} {8,S}
2    C 0 {1,S} {3,S}
3 *4 C 0 {2,S} {7,S}
4    C 0 {1,S}
5    C 0 {7,S}
6    C 0 {7,S}
7 *1 C 1 {3,S} {5,S} {6,S}
8 *2 O 0 {1,S} {9,S}
9 *3 H 0 {8,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.9e+11,"s^-1","*|/",5),
        n = 0,
        Ea = (15.481,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (298,"K"),
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
Category: Theory
Data type: Ab initio
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5
""",
    history = [
        ("Tue Jul 24 18:13:06 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:10"""),
    ],
)

entry(
    index = 26,
    label = "2003MER/RAY4828-4833:11",
    reactant1 = 
"""
1 *4 C 0 {2,S} {5,S} {6,S} {8,S}
2    C 0 {1,S} {3,S}
3 *5 C 0 {2,S} {4,S}
4 *2 C 0 {3,S} {7,S} {9,S}
5    C 0 {1,S}
6    C 0 {1,S}
7    C 0 {4,S}
8 *1 O 1 {1,S}
9 *3 H 0 {4,S}
""",
    product1 = 
"""
1 *5 C 0 {2,S} {4,S} {5,S} {8,S}
2    C 0 {1,S} {3,S}
3 *4 C 0 {2,S} {7,S}
4    C 0 {1,S}
5    C 0 {1,S}
6    C 0 {7,S}
7 *1 C 1 {3,S} {6,S}
8 *2 O 0 {1,S} {9,S}
9 *3 H 0 {8,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+12,"s^-1","*|/",5),
        n = 0,
        Ea = (29.288,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (298,"K"),
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
Category: Theory
Data type: Ab initio
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5
""",
    history = [
        ("Tue Jul 24 18:22:39 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:11"""),
    ],
)

entry(
    index = 27,
    label = "2003MER/RAY4828-4833:8",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,S} {7,S}
2 *5 C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4    C 0 {2,S} {6,S}
5    C 0 {3,S}
6 *4 C 0 {4,S} {8,S}
7 *3 H 0 {1,S}
8 *1 O 1 {6,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2 *4 C 0 {1,S} {6,S}
3    C 0 {5,S} {6,S}
4 *5 C 0 {1,S} {7,S}
5    C 0 {3,S}
6 *1 C 1 {2,S} {3,S}
7 *2 O 0 {4,S} {8,S}
8 *3 H 0 {7,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.4e+12,"s^-1","*|/",5),
        n = 0,
        Ea = (32.217,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (298,"K"),
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
Category: Theory
Data type: Ab initio
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5
""",
    history = [
        ("Tue Jul 24 18:27:53 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:8"""),
    ],
)

entry(
    index = 28,
    label = "2003MER/RAY4828-4833:4",
    reactant1 = 
"""
1 *5 C 0 {2,S} {3,S}
2 *2 C 0 {1,S} {4,S} {6,S}
3    C 0 {1,S} {5,S}
4    C 0 {2,S}
5 *4 C 0 {3,S} {7,S}
6 *3 H 0 {2,S}
7 *1 O 1 {5,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2 *4 C 0 {1,S} {5,S}
3 *5 C 0 {1,S} {6,S}
4    C 0 {5,S}
5 *1 C 1 {2,S} {4,S}
6 *2 O 0 {3,S} {7,S}
7 *3 H 0 {6,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.7e+12,"s^-1","*|/",5),
        n = 0,
        Ea = (33.054,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (298,"K"),
        Tmax = (298,"K"),
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
Category: Theory
Data type: Ab initio
Pressure dependence: Rate constant is high pressure limit

The authors have calculated thermochemical and kinetic parameters for 1,5-H isomerisation reactions of alkoxy radicals up to C8 using density functional theory. Tunneling corrections were applied and the pressure dependence was investigated using RRKM statistical methods.

Generic rate parameters for alkoxy radical 1,5 H transfers from primary, secondary, and tertiary C-Hn groups are suggested for 298 K and 1 atm pressure:
kisom(primary) = 6.2E5 s^-1
kisom(secondary) = 9.3E8 s^-1
kisom(tertiary) = 4.5E8 s^-1

The authors estimate uncertainties in calculated rates to be a factor of 5
""",
    history = [
        ("Tue Jul 24 18:30:54 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MER/RAY4828-4833:4"""),
    ],
)

