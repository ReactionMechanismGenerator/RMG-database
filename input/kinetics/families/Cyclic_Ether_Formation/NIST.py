#!/usr/bin/env python
# encoding: utf-8

name = "Cyclic_Ether_Formation/NIST"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 1,
    label = "1982BAL/HIS1615:8",
    reactant1 = 
"""
1  *4 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 {1,S} {13,S} {14,S} {15,S}
5  *1 C 1 {1,S} {16,S} {17,S}
6  *2 O 0 {2,S} {7,S}
7  *3 O 0 {6,S} {18,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {7,S}
""",
    product1 = 
"""
1  *4 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3  *1 C 0 {1,S} {6,S} {9,S} {10,S}
4     C 0 {1,S} {11,S} {12,S} {13,S}
5     C 0 {1,S} {14,S} {15,S} {16,S}
6  *2 O 0 {2,S} {3,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
15    H 0 {5,S}
16    H 0 {5,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+11,"s^-1"),
        n = 0,
        Ea = (73.001,"kJ/mol"),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=1982BAL/HIS1615:8",
    ),
    referenceType = "experiment",
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
PrIMe Reaction: r00016872
PrIMe Kinetics: http://warehouse.primekinetics.org/depository/reactions/data/r00016872/rk00000002.xml
Bath gas: N2
Excitation technique: Thermal
Analytical technique: Gas chromatography
""",
    history = [
        ("Fri Jul 13 08:21:18 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=1982BAL/HIS1615:8"""),
    ],
)

entry(
    index = 2,
    label = "2004SUN/BOZ1694-1711:23",
    reactant1 = 
"""
1  *4 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 {1,S} {13,S} {14,S} {15,S}
5  *1 C 1 {1,S} {16,S} {17,S}
6  *2 O 0 {2,S} {7,S}
7  *3 O 0 {6,S} {18,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {7,S}
""",
    product1 = 
"""
1  *4 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3  *1 C 0 {1,S} {6,S} {9,S} {10,S}
4     C 0 {1,S} {11,S} {12,S} {13,S}
5     C 0 {1,S} {14,S} {15,S} {16,S}
6  *2 O 0 {2,S} {3,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
15    H 0 {5,S}
16    H 0 {5,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.05e+35,"s^-1"),
        n = -7.46,
        Ea = (100.362,"kJ/mol"),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:23",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016872

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
    history = [
        ("Fri Jul 13 08:21:18 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:23"""),
    ],
)

entry(
    index = 3,
    label = "2004SUN/BOZ1694-1711:24",
    reactant1 = 
"""
1  *4 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {8,S} {9,S}
3     C 0 {1,S} {10,S} {11,S} {12,S}
4     C 0 {1,S} {13,S} {14,S} {15,S}
5  *1 C 1 {1,S} {16,S} {17,S}
6  *2 O 0 {2,S} {7,S}
7  *3 O 0 {6,S} {18,S}
8     H 0 {2,S}
9     H 0 {2,S}
10    H 0 {3,S}
11    H 0 {3,S}
12    H 0 {3,S}
13    H 0 {4,S}
14    H 0 {4,S}
15    H 0 {4,S}
16    H 0 {5,S}
17    H 0 {5,S}
18    H 0 {7,S}
""",
    product1 = 
"""
1  *4 C 0 {2,S} {3,S} {4,S} {5,S}
2     C 0 {1,S} {6,S} {7,S} {8,S}
3  *1 C 0 {1,S} {6,S} {9,S} {10,S}
4     C 0 {1,S} {11,S} {12,S} {13,S}
5     C 0 {1,S} {14,S} {15,S} {16,S}
6  *2 O 0 {2,S} {3,S}
7     H 0 {2,S}
8     H 0 {2,S}
9     H 0 {3,S}
10    H 0 {3,S}
11    H 0 {4,S}
12    H 0 {4,S}
13    H 0 {4,S}
14    H 0 {5,S}
15    H 0 {5,S}
16    H 0 {5,S}
""",
    product2 = 
"""
1 *3 O 1 {2,S}
2    H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.78e+17,"s^-1"),
        n = -2.45,
        Ea = (48.103,"kJ/mol"),
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
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:24",
    ),
    referenceType = "theory",
    shortDesc = u"""Ab initio""",
    longDesc = 
u"""
PrIMe Reaction: r00016872

Quantum calculations of energetics of pathways related to reaction between neopentyl radical and O2 (and subsequent reaction pathways). This includes primary reaction pathways as well as subsequent secondary reactions. Used ab initio CBS-Q method, as well as B3LYP/6-31G(d,p) for some molecules. Many reaction channels are discussed in paper, for some, rate expressions are provided at low pressure limit, high pressure limit, and a number of intermediate pressures. For some reaction channels, no rate expressions are given in paper, but are provided in auxillary information associated with the article in JPC.

Rate expressions reported are derived from ab initio transition states using QRRK analysis of the chemically activated reaction pathways. We have only abstracted rate expressions from the paper for 1 atm and 300-900 K. For other pressures and at higher temperatures see paper.
""",
    history = [
        ("Fri Jul 13 08:21:18 2012","Sean Troiano <stroiano7@gmail.com>","action","""Imported from NIST database at http://kinetics.nist.gov/kinetics/Detail?id=2004SUN/BOZ1694-1711:24"""),
    ],
)

