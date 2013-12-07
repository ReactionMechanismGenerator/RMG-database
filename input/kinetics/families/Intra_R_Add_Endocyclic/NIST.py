#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Endocyclic/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1969KER/SMI1400:3",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 0 {1,S} {3,S} {6,S} {7,S}
3 *2 C 1 {1,S} {2,S} {8,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {3,S}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {3,D} {4,S}
2 *1 C 1 {1,S} {5,S} {6,S}
3 *3 C 0 {1,D} {7,S} {8,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {3,S}
8    H 0 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.51e+10,"s^-1","*|/",5),
        n = 0,
        Ea = (79.902,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (411,"K"),
        Tmax = (4460,"K"),
        Pmin = (6666,"Pa"),
        Pmax = (6666,"Pa"),
    ),
    reference = Article(
        authors = ["Kerr, J.A.", "Smith, A.", "Trotman-Dickenson, A.F."],
        title = u'Reactions of cyclopropyl radicals in the methyl-initiated decomposition of cyclopropanecarbaldehyde',
        journal = "J. Chem. Soc. A",
        pages = """1400""",
        year = "1969",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1969KER/SMI1400:3",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00011188
Uncertainty: 5.0
Bath gas: (tert-C4H9O)2
Excitation technique: Thermal
Analytical technique: Other (direct)
Note: Invalid activation energy uncertainty (8314.472) found and ignored
""",
    history = [
        ("Fri Jul 13 08:17:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1969KER/SMI1400:3"""),
    ],
)

entry(
    index = 2,
    label = "1967GRE/THY1367:1",
    reactant1 = 
"""
1 *1 C 0 {2,S} {3,S} {4,S} {5,S}
2 *3 C 0 {1,S} {3,S} {6,S} {7,S}
3 *2 C 1 {1,S} {2,S} {8,S}
4    H 0 {1,S}
5    H 0 {1,S}
6    H 0 {2,S}
7    H 0 {2,S}
8    H 0 {3,S}
""",
    product1 = 
"""
1 *2 C 0 {2,S} {3,D} {4,S}
2 *1 C 1 {1,S} {5,S} {6,S}
3 *3 C 0 {1,D} {7,S} {8,S}
4    H 0 {1,S}
5    H 0 {2,S}
6    H 0 {2,S}
7    H 0 {3,S}
8    H 0 {3,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+13,"s^-1"),
        n = 0,
        Ea = (92.291,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (313,"K"),
        Tmax = (523,"K"),
    ),
    reference = Article(
        authors = ["Greig, G.", "Thynne, J.C.J."],
        title = u'Reactions of cyclic akyl radicals. Part 2.-Photolysis of cyclopropane carboxaldehyde',
        journal = "Trans. Faraday Soc.",
        volume = "63",
        pages = """1367""",
        year = "1967",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1967GRE/THY1367:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00011188
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00011188/rk00000001.xml
Bath gas: Cyclopropanecarboxaldehyde
""",
    history = [
        ("Fri Jul 13 08:17:26 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1967GRE/THY1367:1"""),
    ],
)

entry(
    index = 3,
    label = "2003MAT/GRE95-119:1",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {5,S} {6,S}
2  *4 C 0 {1,S} {4,S} {7,S} {8,S}
3  *3 C 0 {1,S} {4,S} {9,S} {10,S}
4  *2 C 1 {2,S} {3,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
""",
    product1 = 
"""
1  *4 C 0 {2,S} {3,S} {5,S} {6,S}
2  *2 C 0 {1,S} {4,D} {7,S}
3  *1 C 1 {1,S} {8,S} {9,S}
4  *3 C 0 {2,D} {10,S} {11,S}
5     H 0 {1,S}
6     H 0 {1,S}
7     H 0 {2,S}
8     H 0 {3,S}
9     H 0 {3,S}
10    H 0 {4,S}
11    H 0 {4,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.1e+10,"s^-1"),
        n = 0.79,
        Ea = (108.366,"kJ/mol"),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:1",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00012751
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00012751/rk00000001.xml
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from CBS-Q calculations of Sumathi.
""",
    history = [
        ("Fri Jul 13 08:17:29 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:1"""),
    ],
)

entry(
    index = 4,
    label = "1986GIE/GAW623-637:4",
    reactant1 = 
"""
1  *5 C 0 {2,S} {3,S} {6,S} {7,S}
2  *4 C 0 {1,S} {4,S} {8,S} {9,S}
3  *2 C 0 {1,S} {5,D} {10,S}
4  *1 C 1 {2,S} {11,S} {12,S}
5  *3 C 0 {3,D} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    product1 = 
"""
1  *4 C 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 0 {1,S} {4,S} {8,S} {9,S}
3  *5 C 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 0 {2,S} {5,S} {12,S} {13,S}
5  *2 C 1 {3,S} {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+11,"s^-1","*|/",1.58),
        n = 0,
        Ea = (67.763,"kJ/mol","+|-",1.355),
        T0 = (1,"K"),
        Tmin = (290,"K"),
        Tmax = (310,"K"),
        Pmin = (1013,"Pa"),
        Pmax = (40300,"Pa"),
    ),
    reference = Article(
        authors = ["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."],
        title = u'Mutual isomerization of cyclopentyl and 1-penten-5-yl radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """623-637""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986GIE/GAW623-637:4",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013098
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013098/rk00000001.xml
Uncertainty: 1.58
Bath gas: H2S
""",
    history = [
        ("Fri Jul 13 08:17:32 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986GIE/GAW623-637:4"""),
    ],
)

entry(
    index = 5,
    label = "2006TSA8501-8509:11",
    reactant1 = 
"""
1  *5 C 0 {2,S} {3,S} {6,S} {7,S}
2  *4 C 0 {1,S} {4,S} {8,S} {9,S}
3  *2 C 0 {1,S} {5,D} {10,S}
4  *1 C 1 {2,S} {11,S} {12,S}
5  *3 C 0 {3,D} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    product1 = 
"""
1  *4 C 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 0 {1,S} {4,S} {8,S} {9,S}
3  *5 C 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 0 {2,S} {5,S} {12,S} {13,S}
5  *2 C 1 {3,S} {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.66e+06,"s^-1"),
        n = 1.39,
        Ea = (71.76,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Mechanism and rate constants for the decomposition of 1-pentenyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """8501-8509""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006TSA8501-8509:11",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00013098
Pressure dependence: Rate constant is high pressure limit

The log(k∞/k) values at various pressures were presented in four parameters form
""",
    history = [
        ("Fri Jul 13 08:17:32 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2006TSA8501-8509:11"""),
    ],
)

entry(
    index = 6,
    label = "2003MAT/GRE95-119:2",
    reactant1 = 
"""
1  *5 C 0 {2,S} {3,S} {6,S} {7,S}
2  *4 C 0 {1,S} {4,S} {8,S} {9,S}
3  *2 C 0 {1,S} {5,D} {10,S}
4  *1 C 1 {2,S} {11,S} {12,S}
5  *3 C 0 {3,D} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    product1 = 
"""
1  *4 C 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 0 {1,S} {4,S} {8,S} {9,S}
3  *5 C 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 0 {2,S} {5,S} {12,S} {13,S}
5  *2 C 1 {3,S} {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.2e+08,"s^-1"),
        n = 1.05,
        Ea = (66.107,"kJ/mol"),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:2",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00013098
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from CBS-Q calculations of Sumathi.
""",
    history = [
        ("Fri Jul 13 08:17:32 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:2"""),
    ],
)

entry(
    index = 7,
    label = "1995HAN/WAL1431-1438:7",
    reactant1 = 
"""
1  *4 C 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 0 {1,S} {4,S} {8,S} {9,S}
3  *5 C 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 0 {2,S} {5,S} {12,S} {13,S}
5  *2 C 1 {3,S} {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    product1 = 
"""
1  *5 C 0 {2,S} {3,S} {6,S} {7,S}
2  *4 C 0 {1,S} {4,S} {8,S} {9,S}
3  *2 C 0 {1,S} {5,D} {10,S}
4  *1 C 1 {2,S} {11,S} {12,S}
5  *3 C 0 {3,D} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.38e+13,"s^-1","*|/",5),
        n = 0,
        Ea = (143.84,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (580,"K"),
        Tmax = (783,"K"),
        Pmin = (23300,"Pa"),
        Pmax = (66700,"Pa"),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Addition of cyclopentane to slowly reacting mixtures of H2 + O2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "91",
        pages = """1431-1438""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995HAN/WAL1431-1438:7",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00013098
Uncertainty: 5.0
Bath gas: O2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:17:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1995HAN/WAL1431-1438:7"""),
    ],
)

entry(
    index = 8,
    label = "1986GIE/GAW623-637:1",
    reactant1 = 
"""
1  *4 C 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 0 {1,S} {4,S} {8,S} {9,S}
3  *5 C 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 0 {2,S} {5,S} {12,S} {13,S}
5  *2 C 1 {3,S} {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    product1 = 
"""
1  *5 C 0 {2,S} {3,S} {6,S} {7,S}
2  *4 C 0 {1,S} {4,S} {8,S} {9,S}
3  *2 C 0 {1,S} {5,D} {10,S}
4  *1 C 1 {2,S} {11,S} {12,S}
5  *3 C 0 {3,D} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.38e+14,"s^-1","*|/",1.58),
        n = 0,
        Ea = (133.863,"kJ/mol","+|-",1.339),
        T0 = (1,"K"),
        Tmin = (290,"K"),
        Tmax = (310,"K"),
        Pmin = (5520,"Pa"),
        Pmax = (51100,"Pa"),
    ),
    reference = Article(
        authors = ["Gierczak, T.", "Gawlowski, J.", "Niedzielski, J."],
        title = u'Mutual isomerization of cyclopentyl and 1-penten-5-yl radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """623-637""",
        year = "1986",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1986GIE/GAW623-637:1",
    ),
    referenceType = "experiment",
    shortDesc = u"""RRK(M) extrapolation""",
    longDesc = 
u"""
PrIMe Reaction: r00013098
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00013098/rk00000001.xml
Uncertainty: 1.58
Bath gas: H2S
""",
    history = [
        ("Fri Jul 13 08:17:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1986GIE/GAW623-637:1"""),
    ],
)

entry(
    index = 9,
    label = "2006TSA8501-8509:9",
    reactant1 = 
"""
1  *4 C 0 {2,S} {3,S} {6,S} {7,S}
2  *1 C 0 {1,S} {4,S} {8,S} {9,S}
3  *5 C 0 {1,S} {5,S} {10,S} {11,S}
4  *3 C 0 {2,S} {5,S} {12,S} {13,S}
5  *2 C 1 {3,S} {4,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
""",
    product1 = 
"""
1  *5 C 0 {2,S} {3,S} {6,S} {7,S}
2  *4 C 0 {1,S} {4,S} {8,S} {9,S}
3  *2 C 0 {1,S} {5,D} {10,S}
4  *1 C 1 {2,S} {11,S} {12,S}
5  *3 C 0 {3,D} {13,S} {14,S}
6     H 0 {1,S}
7     H 0 {1,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13    H 0 {5,S}
14    H 0 {5,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.46e+12,"s^-1"),
        n = 0.16,
        Ea = (142.5,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (500,"K"),
        Tmax = (2000,"K"),
    ),
    reference = Article(
        authors = ["Tsang, W."],
        title = u'Mechanism and rate constants for the decomposition of 1-pentenyl radicals',
        journal = "J. Phys. Chem. A",
        volume = "110",
        pages = """8501-8509""",
        year = "2006",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2006TSA8501-8509:9",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00013098
Pressure dependence: Rate constant is high pressure limit

The log(k∞/k) values at various pressures were presented in four parameters form
""",
    history = [
        ("Fri Jul 13 08:17:34 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2006TSA8501-8509:9"""),
    ],
)

entry(
    index = 10,
    label = "2003MAT/GRE95-119:3",
    reactant1 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2  *5 C 0 {1,S} {4,S} {9,S} {10,S}
3  *4 C 0 {1,S} {5,S} {11,S} {12,S}
4  *2 C 0 {2,S} {6,D} {13,S}
5  *1 C 1 {3,S} {14,S} {15,S}
6  *3 C 0 {4,D} {16,S} {17,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
15    H 0 {5,S}
16    H 0 {6,S}
17    H 0 {6,S}
""",
    product1 = 
"""
1  *4 C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *1 C 0 {1,S} {5,S} {11,S} {12,S}
4  *5 C 0 {2,S} {6,S} {13,S} {14,S}
5  *3 C 0 {3,S} {6,S} {15,S} {16,S}
6  *2 C 1 {4,S} {5,S} {17,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+08,"s^-1"),
        n = 0.86,
        Ea = (24.686,"kJ/mol"),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:3",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00015692
Pressure dependence: Rate constant is high pressure limit

Rate expressions derived from transition states from B3LYP/cc-pVTZ calculations of Sumathi.
""",
    history = [
        ("Fri Jul 13 08:17:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003MAT/GRE95-119:3"""),
    ],
)

entry(
    index = 11,
    label = "1995HAN/WAL1431-1438:13",
    reactant1 = 
"""
1     C 0 {2,S} {3,S} {7,S} {8,S}
2  *5 C 0 {1,S} {4,S} {9,S} {10,S}
3  *4 C 0 {1,S} {5,S} {11,S} {12,S}
4  *2 C 0 {2,S} {6,D} {13,S}
5  *1 C 1 {3,S} {14,S} {15,S}
6  *3 C 0 {4,D} {16,S} {17,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {5,S}
15    H 0 {5,S}
16    H 0 {6,S}
17    H 0 {6,S}
""",
    product1 = 
"""
1  *4 C 0 {2,S} {3,S} {7,S} {8,S}
2     C 0 {1,S} {4,S} {9,S} {10,S}
3  *1 C 0 {1,S} {5,S} {11,S} {12,S}
4  *5 C 0 {2,S} {6,S} {13,S} {14,S}
5  *3 C 0 {3,S} {6,S} {15,S} {16,S}
6  *2 C 1 {4,S} {5,S} {17,S}
7     H 0 {1,S}
8     H 0 {1,S}
9     H 0 {2,S}
10    H 0 {2,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {5,S}
16    H 0 {5,S}
17    H 0 {6,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+10,"s^-1"),
        n = 0,
        Ea = (35.004,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (600,"K"),
        Tmax = (1300,"K"),
        Pmin = (667,"Pa"),
        Pmax = (66700,"Pa"),
    ),
    reference = Article(
        authors = ["Handford-Styring, S.M.", "Walker, R.W."],
        title = u'Addition of cyclopentane to slowly reacting mixtures of H2 + O2 between 673 and 783 K: reactions of H and OH with cyclopentane and of cyclopentyl radicals',
        journal = "J. Chem. Soc. Faraday Trans.",
        volume = "91",
        pages = """1431-1438""",
        year = "1995",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1995HAN/WAL1431-1438:13",
    ),
    referenceType = "theory",
    shortDesc = u"""Estimated: thermochemical, kinetic, or other""",
    longDesc = 
u"""
PrIMe Reaction: r00015692
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00015692/rk00000001.xml
Bath gas: O2
""",
    history = [
        ("Fri Jul 13 08:17:47 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1995HAN/WAL1431-1438:13"""),
    ],
)

entry(
    index = 12,
    label = "2003TOK/LIN11397-11408:16",
    reactant1 = 
"""
1  *3 C 0 {2,S} {4,S} {9,S} {10,S}
2  *1 C 0 {1,S} {3,B} {5,B}
3  *4 C 0 {2,B} {4,S} {6,B}
4  *2 C 1 {1,S} {3,S} {11,S}
5     C 0 {2,B} {8,B} {12,S}
6     C 0 {3,B} {7,B} {13,S}
7     C 0 {6,B} {8,B} {14,S}
8     C 0 {5,B} {7,B} {15,S}
9     H 0 {1,S}
10    H 0 {1,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {6,S}
14    H 0 {7,S}
15    H 0 {8,S}
""",
    product1 = 
"""
1  *4 C 0 {2,B} {4,S} {8,B}
2     C 0 {1,B} {3,B} {9,S}
3     C 0 {2,B} {5,B} {10,S}
4  *2 C 0 {1,S} {7,D} {11,S}
5     C 0 {3,B} {6,B} {12,S}
6     C 0 {5,B} {8,B} {13,S}
7  *3 C 0 {4,D} {14,S} {15,S}
8  *1 C 1 {1,B} {6,B}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {5,S}
13    H 0 {6,S}
14    H 0 {7,S}
15    H 0 {7,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.91e+12,"s^-1"),
        n = 0.26,
        Ea = (158.072,"kJ/mol"),
        T0 = (1,"K"),
        Tmin = (250,"K"),
        Tmax = (2000,"K"),
        Pmin = (101000,"Pa"),
        Pmax = (101000,"Pa"),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2003TOK/LIN11397-11408:16",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00017190
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00017190/rk00000001.xml

Ab initio study of reaction pathways for C6H4 (phenyl) plus C2H2 (acetylene). Used G2M(CC5) method (see paper for details). Calculated many different reaction pathways and intermediates. Only a few of the more important ones are abstracted here. Rate expressions for different pressures for some of the channels are also given in the paper. See paper for further details. Used NIST ChemRate program to calculated rate expressions from ab initio transition states. In paper also provide DfHo heats of formation for many of the intermediates.
""",
    history = [
        ("Tue Jul 24 15:30:27 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2003TOK/LIN11397-11408:16"""),
    ],
)

