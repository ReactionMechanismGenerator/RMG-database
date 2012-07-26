#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_MultipleBond/PrIMe"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 105,
    label = "r00010238",
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 C 0 {1,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2 *2 C 1 {1,S}
3 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (540000,"cm^3/(mol*s)"),
        n = 0.454,
        Ea = (7614.88,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010238/rk00000040.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010238/rk00000040.xml
""",
    history = [
        ("Tue May 17 14:34:34 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010238/rk00000040.xml"""),
    ],
)

entry(
    index = 143,
    label = "r00010564",
    reactant1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,S} {3,S}
2 *2 O 1 {1,S}
3 *3 H 0 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (540000,"cm^3/(mol*s)"),
        n = 0.454,
        Ea = (10878.4,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00010564/rk00000030.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010564/rk00000030.xml
""",
    history = [
        ("Tue May 17 14:34:36 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00010564/rk00000030.xml"""),
    ],
)

entry(
    index = 214,
    label = "r00011282",
    reactant1 = 
"""
1 *2 C 0 {2,D}
2 *1 O 0 {1,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *2 C 1 {2,S}
2 *1 O 0 {1,S} {3,S}
3 *3 H 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (540000,"cm^3/(mol*s)"),
        n = 0.454,
        Ea = (15062.4,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011282/rk00000017.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011282/rk00000017.xml
""",
    history = [
        ("Tue May 17 14:34:46 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011282/rk00000017.xml"""),
    ],
)

entry(
    index = 232,
    label = "r00011402",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,D} {3,S}
2 *2 C 1 {1,D}
3 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (5.6e+06,"cm^3/(mol*s)"),
        n = 0,
        Ea = (10041.6,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00011402/rk00000027.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011402/rk00000027.xml
""",
    history = [
        ("Tue May 17 14:34:47 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00011402/rk00000027.xml"""),
    ],
)

entry(
    index = 296,
    label = "r00012710",
    reactant1 = 
"""
1 *2 C 0 {2,D}
2 *1 C 0 {1,D} {3,D}
3    O 0 {2,D}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *2 C 1 {2,S}
2 *1 C 0 {1,S} {3,D} {4,S}
3    O 0 {2,D}
4 *3 H 0 {2,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (486500,"cm^3/(mol*s)"),
        n = 0.422,
        Ea = (-7342.92,"cal/mol"),
        T0 = (1,"K"),
    ),
    reference = Reference(
        authors = ["Smith, G.P.", "Golden, D.M.", "Frenklach, M.", "Moriarty, N.W.", "Eiteneer, B.", "Goldenberg, M.", "Bowman, C.T.", "Hanson, R.K.", "Song, S.", "Gardiner, W.C., Jr.", "Lissianski, V.V.", "Qin, Z."],
        year = "1999",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00012710/rk00000010.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012710/rk00000010.xml
""",
    history = [
        ("Tue May 17 14:34:57 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00012710/rk00000010.xml"""),
    ],
)

entry(
    index = 347,
    label = "r00015756",
    reactant1 = 
"""
1  *1 C 0 {2,S} {3,S} {11,S}
2     C 0 {1,S} {4,B} {5,B}
3  *2 C 1 {1,S} {9,S}
4     C 0 {2,B} {7,B}
5     C 0 {2,B} {8,B}
6     C 0 {7,B} {8,B}
7     C 0 {4,B} {6,B}
8     C 0 {5,B} {6,B}
9     C 0 {3,S} {10,D}
10    C 0 {9,D}
11 *3 H 0 {1,S}
""",
    product1 = 
"""
1     C 0 {2,S} {3,B} {4,B}
2  *1 C 0 {1,S} {5,D}
3     C 0 {1,B} {6,B}
4     C 0 {1,B} {7,B}
5  *2 C 0 {2,D} {9,S}
6     C 0 {3,B} {8,B}
7     C 0 {4,B} {8,B}
8     C 0 {6,B} {7,B}
9     C 0 {5,S} {10,D}
10    C 0 {9,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (2.4e+12,"s^-1"),
        n = 0,
        Ea = (195811,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Fascella, S.", "Cavallotti, C.", "Rota, R.", "Carra, S."],
        title = u'Quantum chemistry investigation of key reactions involved in the formation of naphthalene and indene',
        journal = "J. Phys. Chem. A",
        volume = "108",
        pages = """3829-3843""",
        year = "2004",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:28 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00015756/rk00000002.xml"""),
        ("Fri Jun  3 16:02:18 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value for activation energy."""),
    ],
)

entry(
    index = 350,
    label = "r00016108",
    reactant1 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {5,B}
3    C 0 {1,B} {6,B}
4    C 0 {5,B} {6,B}
5    C 0 {2,B} {4,B}
6    C 0 {3,B} {4,B}
7 *1 C 0 {1,S} {8,D} {9,S}
8 *2 C 1 {7,D}
9 *3 H 0 {7,S}
""",
    product1 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {5,B}
4    C 0 {2,B} {6,B}
5    C 0 {3,B} {6,B}
6    C 0 {4,B} {5,B}
7 *1 C 0 {1,S} {8,T}
8 *2 C 0 {7,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.8e+11,"s^-1"),
        n = 0.82,
        Ea = (162799,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Tokmakov, I.V.", "Lin, M.C."],
        title = u'Reaction of phenyl radicals with acetylene: Quantum chemical investigation of the mechanism and master equation analysis of the kinetics',
        journal = "J. Am. Chem. Soc.",
        volume = "125",
        pages = """11397-11408""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016108/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016108/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:37 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016108/rk00000001.xml"""),
    ],
)

entry(
    index = 358,
    label = "r00016187",
    reactant1 = 
"""
1 *1 C 0 {2,S} {8,S} {9,S}
2    C 0 {1,S} {3,B} {4,B}
3    C 0 {2,B} {6,B}
4    C 0 {2,B} {7,B}
5    C 0 {6,B} {7,B}
6    C 0 {3,B} {5,B}
7    C 0 {4,B} {5,B}
8 *2 O 1 {1,S}
9 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,B} {3,B} {7,S}
2    C 0 {1,B} {4,B}
3    C 0 {1,B} {6,B}
4    C 0 {2,B} {5,B}
5    C 0 {4,B} {6,B}
6    C 0 {3,B} {5,B}
7 *1 C 0 {1,S} {8,D}
8 *2 O 0 {7,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.27e+14,"s^-1"),
        n = 0,
        Ea = (4614.53,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Brezinsky, K.", "Litzinger, T.A.", "Glassman, I."],
        title = u'The high temperature oxidation of the methyl side chain of toluene',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """1053""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016187/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016187/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016187/rk00000001.xml"""),
    ],
)

entry(
    index = 359,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+16,"s^-1"),
        n = 0,
        Ea = (73250.5,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L.", "McCulloch, R.D.", "Milne, R.T."],
        title = u'Thermochemical and Kinetic Studies of Alkyl Nitrites (RONO)-D(RO-NO), The Reactions between RO. and NO, and the Decomposition RO.',
        journal = "Proc. Symp. Chem. Kinet. Data Upper Lower Atmos. 1974",
        pages = """441""",
        year = "1975",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000001.xml"""),
    ],
)

entry(
    index = 360,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.31e+14,"s^-1"),
        n = 0,
        Ea = (64021.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L.", "McCulloch, R.D."],
        title = u'The Gas-Phase Pyrolysis of Alkyl Nitrites. II. s-Butyl Nitrite',
        journal = "Int. J. Chem. Kinet.",
        volume = "8",
        pages = """911""",
        year = "1976",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000002.xml"""),
    ],
)

entry(
    index = 361,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.76e+14,"s^-1"),
        n = 0,
        Ea = (61111.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000003.xml"""),
    ],
)

entry(
    index = 362,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (64021.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000004.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000004.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000004.xml"""),
    ],
)

entry(
    index = 363,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98e+13,"s^-1"),
        n = 0,
        Ea = (56455.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Choo, K.Y.", "Benson, S.W."],
        title = u'Arrhenius Parameters for the Alkoxy Radical Decomposition Reactions',
        journal = "Int. J. Chem. Kinet.",
        volume = "13",
        pages = """833""",
        year = "1981",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000005.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000005.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000005.xml"""),
    ],
)

entry(
    index = 364,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (64437.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000007.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000007.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000007.xml"""),
    ],
)

entry(
    index = 365,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.35e+13,"s^-1"),
        n = 0,
        Ea = (62774.3,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heiss, A.", "Tardieu de Maleissye, J.", "Viossat, V.", "Sahetchian, K.A."],
        title = u'Reactions of primary and secondary butoxy radicals in oxygen at atmospheric pressure',
        journal = "Int. J. Chem. Kinet.",
        volume = "23",
        pages = """607-622""",
        year = "1991",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000008.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000008.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000008.xml"""),
    ],
)

entry(
    index = 366,
    label = "r00016188",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S}
2 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.25e+13,"s^-1"),
        n = 0,
        Ea = (48900,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000009.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000009.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016188/rk00000009.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 367,
    label = "r00016189",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S} {6,S}
3    C 0 {1,S}
4    C 0 {2,S}
5 *2 O 1 {2,S}
6 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {4,S}
2    C 0 {1,S}
3    C 0 {4,S}
4 *1 C 0 {1,S} {3,S} {5,D}
5 *2 O 0 {4,D}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.51e+13,"s^-1"),
        n = 0,
        Ea = (75600,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016189/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016189/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016189/rk00000001.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 368,
    label = "r00016190",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *3 C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.94e+14,"s^-1"),
        n = 0,
        Ea = (79486.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Batt, L."],
        title = u'The Gas-Phase Decomposition of Alkoxy Radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "11",
        pages = """977""",
        year = "1979",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000001.xml"""),
    ],
)

entry(
    index = 369,
    label = "r00016190",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *3 C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (79902.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000002.xml"""),
    ],
)

entry(
    index = 370,
    label = "r00016190",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *1 C 0 {1,S} {4,S} {5,S}
3    C 0 {1,S}
4 *3 C 0 {2,S}
5 *2 O 1 {2,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *1 C 0 {1,S} {4,D}
4 *2 O 0 {3,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.78e+13,"s^-1"),
        n = 0,
        Ea = (62300,"kJ/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Rauk, A.", "Boyd, R.J.", "Boyd, S.L.", "Henry, D.J.", "Radom, L."],
        title = u'Alkoxy radicals in the gaseous phase: beta-scission reactions and formation by radical addition to carbonyl compounds',
        journal = "Can. J. Chem.",
        volume = "81",
        pages = """431-442""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:39 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016190/rk00000003.xml"""),
        ("Fri Jun  3 17:09:42 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect value of activation energy."""),
    ],
)

entry(
    index = 373,
    label = "r00016656",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5    C 0 {3,S}
6 *2 O 1 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+14,"s^-1"),
        n = 0,
        Ea = (57702.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Marta, F."],
        title = u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """329""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:51 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000001.xml"""),
    ],
)

entry(
    index = 374,
    label = "r00016656",
    reactant1 = 
"""
1 *3 C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5    C 0 {3,S}
6 *2 O 1 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *1 C 0 {1,S} {3,D}
3 *2 O 0 {2,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S}
3 *3 C 1 {1,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+15,"s^-1"),
        n = 0,
        Ea = (64437.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Heicklen, J."],
        title = u'The decomposition of alkyl nitrites and the reactions of alkoxyl radicals',
        journal = "Adv. Photochem.",
        volume = "14",
        pages = """177""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:51 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016656/rk00000002.xml"""),
    ],
)

entry(
    index = 375,
    label = "r00016657",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *1 C 0 {1,S} {5,S} {6,S}
4    C 0 {2,S}
5 *3 C 0 {3,S}
6 *2 O 1 {3,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3    C 0 {1,S}
4 *1 C 0 {2,S} {5,D}
5 *2 O 0 {4,D}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.58e+14,"s^-1"),
        n = 0,
        Ea = (72834.8,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dobe, S.", "Berces, T.", "Marta, F."],
        title = u'Gas phase decomposition and isomerization reactions of 2-pentoxy radicals',
        journal = "Int. J. Chem. Kinet.",
        volume = "18",
        pages = """329""",
        year = "1986",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016657/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016657/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:52 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016657/rk00000001.xml"""),
    ],
)

entry(
    index = 376,
    label = "r00016678",
    reactant1 = 
"""
1 *1 C 0 {2,D} {5,S}
2 *2 C 1 {1,D} {3,S}
3    C 0 {2,S} {4,T}
4    C 0 {3,T}
5 *3 H 0 {1,S}
""",
    product1 = 
"""
1    C 0 {2,S} {3,T}
2 *2 C 0 {1,S} {4,T}
3    C 0 {1,T}
4 *1 C 0 {2,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (216176,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Ghibaudi, E.", "Colussi, A.J."],
        title = u'Kinetics and thermochemistry of the equilibrium 2 (acetylene) = vinylacetylene. Direct evidence against a chain mechanism',
        journal = "J. Phys. Chem.",
        volume = "92",
        pages = """5839""",
        year = "1988",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:35:53 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000002.xml"""),
    ],
)

entry(
    index = 377,
    label = "r00016678",
    reactant1 = 
"""
1 *2 C 0 {2,S} {3,T}
2    C 0 {1,S} {4,T}
3 *1 C 0 {1,T}
4    C 0 {2,T}
""",
    reactant2 = 
"""
1 *3 H 1
""",
    product1 = 
"""
1 *1 C 0 {2,D} {5,S}
2 *2 C 1 {1,D} {3,S}
3    C 0 {2,S} {4,T}
4    C 0 {3,T}
5 *3 H 0 {1,S}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (3.3e+24,"cm^3/(mol*s)"),
        n = -4.92,
        Ea = (45189.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Eiteneer, B.", "Frenklach, M."],
        title = u'Experimental and Modeling Study of Shock-Tube Oxidation of Acetylene',
        journal = "Int J. Chem. Kinet.",
        volume = "35",
        pages = """391-414""",
        year = "2003",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000003.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000003.xml
""",
    history = [
        ("Tue May 17 14:35:53 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016678/rk00000003.xml"""),
    ],
)

entry(
    index = 378,
    label = "r00016682",
    reactant1 = 
"""
1    C 0 {2,S} {3,S}
2 *3 C 0 {1,S} {4,S}
3    C 0 {1,S} {5,S}
4 *1 C 0 {2,S} {6,S}
5    O 0 {3,S}
6 *2 O 1 {4,S}
""",
    product1 = 
"""
1 *1 C 0 {2,D}
2 *2 O 0 {1,D}
""",
    product2 = 
"""
1    C 0 {2,S} {3,S}
2    C 0 {1,S} {4,S}
3 *3 C 1 {1,S}
4    O 0 {2,S}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+13,"s^-1"),
        n = 0,
        Ea = (79486.4,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Baldwin, A.C.", "Barker, J.R.", "Golden, D.M.", "Hendry, D.G."],
        title = u'Photochemical smog. Rate parameter estimates and computer simulations',
        journal = "J. Phys. Chem.",
        volume = "81",
        pages = """2483""",
        year = "1977",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016682/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016682/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:35:53 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016682/rk00000001.xml"""),
    ],
)

entry(
    index = 381,
    label = "r00016804",
    reactant1 = 
"""
1 *3 C 0 {3,S}
2    C 0 {4,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 1 {2,S} {3,D}
""",
    product1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,T}
3 *1 C 0 {2,T}
""",
    product2 = 
"""
1 *3 C 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.01e+13,"s^-1"),
        n = 0,
        Ea = (131369,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600""",
        year = "1985",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:00 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000001.xml"""),
    ],
)

entry(
    index = 382,
    label = "r00016804",
    reactant1 = 
"""
1    C 0 {2,S}
2 *2 C 0 {1,S} {3,T}
3 *1 C 0 {2,T}
""",
    reactant2 = 
"""
1 *3 C 1
""",
    product1 = 
"""
1 *3 C 0 {3,S}
2    C 0 {4,S}
3 *1 C 0 {1,S} {4,D}
4 *2 C 1 {2,S} {3,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (501000,"cm^3/(mol*s)"),
        n = 0,
        Ea = (36833.1,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Getty, R.R.", "Kerr, J.A.", "Trotman-Dickenson, A.F."],
        title = u'The reactions of alkyl radicals. Part XIII. The additions of methyl, isopropyl, and t-butyl radicals to propyne and the isomerisation of alkenyl radicals',
        journal = "J. Chem. Soc. A",
        pages = """1360""",
        year = "1967",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:36:00 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016804/rk00000002.xml"""),
    ],
)

entry(
    index = 394,
    label = "r00016901",
    reactant1 = 
"""
1    C 0 {2,S} {3,D}
2 *1 C 0 {1,S} {4,D} {5,S}
3    C 0 {1,D}
4 *2 C 1 {2,D}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 0 {1,S} {4,T}
4 *2 C 0 {3,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1e+14,"s^-1"),
        n = 0,
        Ea = (172941,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Weissman, M.", "Benson, S.W."],
        title = u'Pyrolysis of methyl chloride, a pathway in the chlorine-catalyzed polymerization of methane',
        journal = "Int. J. Chem. Kinet.",
        volume = "16",
        pages = """307""",
        year = "1984",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:03 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000001.xml"""),
    ],
)

entry(
    index = 395,
    label = "r00016901",
    reactant1 = 
"""
1    C 0 {2,S} {3,D}
2 *1 C 0 {1,S} {4,D} {5,S}
3    C 0 {1,D}
4 *2 C 1 {2,D}
5 *3 H 0 {2,S}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D}
3 *1 C 0 {1,S} {4,T}
4 *2 C 0 {3,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.6e+14,"s^-1"),
        n = 0,
        Ea = (172941,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Colket, M.B., III", "Seery, D.J.", "Palmer, H.B."],
        title = u'The pyrolysis of acetylene initiated by acetone',
        journal = "Combust. Flame",
        volume = "75",
        pages = """343-366""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:36:03 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00016901/rk00000002.xml"""),
    ],
)

entry(
    index = 403,
    label = "r00017011",
    reactant1 = 
"""
1 *3 C 0 {2,D} {3,S}
2    C 0 {1,D} {4,S}
3 *1 C 0 {1,S} {5,D}
4    C 0 {2,S} {6,T}
5 *2 C 1 {3,D}
6    C 0 {4,T}
""",
    product1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    product2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,T}
3 *3 C 1 {1,D}
4    C 0 {2,T}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.98107e+62,"s^-1"),
        n = -14.7,
        Ea = (240580,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."],
        title = u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """1053""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:10 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000001.xml"""),
        ("Fri Jun  3 14:55:12 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect values of the kinetic parameters."""),
    ],
)

entry(
    index = 404,
    label = "r00017011",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,T}
3 *3 C 1 {1,D}
4    C 0 {2,T}
""",
    product1 = 
"""
1 *3 C 0 {2,D} {3,S}
2    C 0 {1,D} {4,S}
3 *1 C 0 {1,S} {5,D}
4    C 0 {2,S} {6,T}
5 *2 C 1 {3,D}
6    C 0 {4,T}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (6.15382e+09,"cm^3/(mol*s)"),
        n = -1.51,
        Ea = (20204.2,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Westmoreland, P.R.", "Dean, A.M.", "Howard, J.B.", "Longwell, J.P."],
        title = u'Forming benzene in flames by chemically activated isomerization',
        journal = "J. Phys. Chem.",
        volume = "93",
        pages = """8171""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:36:10 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017011/rk00000002.xml"""),
    ],
)

entry(
    index = 405,
    label = "r00017013",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D} {4,S}
3 *1 C 0 {1,S} {5,D} {7,S}
4    C 0 {2,S} {6,T}
5 *2 C 1 {3,D}
6    C 0 {4,T}
7 *3 H 0 {3,S}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2    C 0 {1,D} {4,S}
3    C 0 {1,S} {5,T}
4 *1 C 0 {2,S} {6,T}
5    C 0 {3,T}
6 *2 C 0 {4,T}
""",
    product2 = 
"""
1 *3 H 1
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.51189e+58,"s^-1"),
        n = -13.8,
        Ea = (208363,"kcal/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Braun-Unkhoff, M.", "Frank, P.", "Just, Th."],
        title = u'A shock tube study on the thermal decomposition of toluene and of the phenyl radical at high temperatures',
        journal = "Symp. Int. Combust. Proc.",
        volume = "22",
        pages = """1053""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017013/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017013/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:10 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017013/rk00000001.xml"""),
        ("Fri Jun  3 14:55:12 2011","Josh Allen <jwallen@mit.edu>","action","""Fixed incorrect values of the kinetic parameters."""),
    ],
)

entry(
    index = 406,
    label = "r00017118",
    reactant1 = 
"""
1    C 0 {2,D} {3,S}
2 *3 C 0 {1,D} {4,S}
3    C 0 {1,S} {5,D}
4 *1 C 0 {2,S} {6,D}
5    C 0 {3,D}
6 *2 C 1 {4,D}
""",
    product1 = 
"""
1 *2 C 0 {2,T}
2 *1 C 0 {1,T}
""",
    product2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3    C 0 {1,D}
4 *3 C 1 {2,D}
""",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16e+13,"s^-1"),
        n = 0,
        Ea = (180424,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Dean, A.M."],
        title = u'Predictions of pressure and temperature effects upon radical addition and recombination reactions',
        journal = "J. Phys. Chem.",
        volume = "89",
        pages = """4600""",
        year = "1985",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000001.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000001.xml
""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000001.xml"""),
    ],
)

entry(
    index = 407,
    label = "r00017118",
    reactant1 = 
"""
1 *1 C 0 {2,T}
2 *2 C 0 {1,T}
""",
    reactant2 = 
"""
1    C 0 {2,S} {3,D}
2    C 0 {1,S} {4,D}
3    C 0 {1,D}
4 *3 C 1 {2,D}
""",
    product1 = 
"""
1    C 0 {2,D} {3,S}
2 *3 C 0 {1,D} {4,S}
3    C 0 {1,S} {5,D}
4 *1 C 0 {2,S} {6,D}
5    C 0 {3,D}
6 *2 C 1 {4,D}
""",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (7.24474e+08,"cm^3/(mol*s)"),
        n = -1.38,
        Ea = (16628.9,"J/mol"),
        T0 = (1,"K"),
    ),
    reference = Article(
        authors = ["Westmoreland, P.R.", "Dean, A.M.", "Howard, J.B.", "Longwell, J.P."],
        title = u'Forming benzene in flames by chemically activated isomerization',
        journal = "J. Phys. Chem.",
        volume = "93",
        pages = """8171""",
        year = "1989",
        url = "http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000002.xml",
    ),
    referenceType = "",
    shortDesc = u"""""",
    longDesc = 
u"""
Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000002.xml
""",
    history = [
        ("Tue May 17 14:36:12 2011","Josh Allen <jwallen@mit.edu>","action","""Imported from PrIMe database at http://warehouse.primekinetics.org/depository/reactions/data/r00017118/rk00000002.xml"""),
    ],
)

